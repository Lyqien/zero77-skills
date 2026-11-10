#!/usr/bin/env python3
"""Read-only PNG alpha checks. A pass still requires visual subject/edge QA."""
import argparse
import json
from pathlib import Path

from PIL import Image


def inspect_png(path):
    path = Path(path)
    result = {"file": path.name, "pass": False, "errors": [],
              "scope": "file_alpha_structure_only", "visual_review_required": True}
    try:
        with path.open("rb") as stream:
            if stream.read(8) != b"\x89PNG\r\n\x1a\n":
                raise ValueError("File does not have a PNG signature")
        with Image.open(path) as source:
            source.load()
            if source.format != "PNG":
                raise ValueError("Decoded format is not PNG")
            if getattr(source, "n_frames", 1) != 1:
                raise ValueError("Animated PNG is not a single cutout asset")
            has_alpha = "A" in source.getbands() or "transparency" in source.info
            result.update(width=source.width, height=source.height,
                          source_mode=source.mode, source_has_alpha=has_alpha)
            if not has_alpha:
                result["errors"].append("No source alpha or PNG transparency metadata")
            alpha = source.convert("RGBA").getchannel("A")
            hist = alpha.histogram()
            total = source.width * source.height
            transparent, visible = hist[0], total - hist[0]
            result.update(alpha_min=alpha.getextrema()[0], alpha_max=alpha.getextrema()[1],
                          transparent_pixels=transparent, visible_pixels=visible,
                          semitransparent_pixels=sum(hist[1:255]),
                          transparent_fraction=round(transparent / total, 6),
                          visible_bbox=alpha.getbbox())
            if not transparent:
                result["errors"].append("No fully transparent pixels; background is not cleared")
            if not visible:
                result["errors"].append("Image is completely transparent")
            borders = [alpha.crop((0, 0, source.width, 1)),
                       alpha.crop((0, source.height - 1, source.width, source.height)),
                       alpha.crop((0, 0, 1, source.height)),
                       alpha.crop((source.width - 1, 0, source.width, source.height))]
            border_clear = all(edge.getextrema()[1] == 0 for edge in borders)
            result["transparent_outer_border"] = border_clear
            if not border_clear:
                result["errors"].append("Visible pixels touch canvas edge; cutout padding needs review")
            result["pass"] = not result["errors"]
    except (OSError, ValueError, Image.DecompressionBombError) as exc:
        result["errors"].append(str(exc))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.report:
        if args.report.resolve() == args.image.resolve():
            parser.error("Report path must differ from image path")
        if args.report.exists():
            parser.error("Report already exists; choose a new filename")
    report = inspect_png(args.image)
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open("x", encoding="utf-8") as stream:
            stream.write(payload + "\n")
    print(payload)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
