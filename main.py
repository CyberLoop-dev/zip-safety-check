#!/usr/bin/env python3
"""Read-only ZIP archive safety inspection; never extracts archive members."""
import argparse
import json
import re
import stat
import sys
import zipfile
from pathlib import Path


def inspect_archive(path, max_total_bytes=500 * 1024 * 1024, max_ratio=100.0):
    findings = []
    seen = set()
    total = 0
    with zipfile.ZipFile(path) as archive:
        for info in archive.infolist():
            name = info.filename
            normalized = name.replace("\\", "/")
            parts = normalized.split("/")
            if normalized.startswith("/") or re.match(r"^[A-Za-z]:", normalized) or ".." in parts:
                findings.append((name, "error", "unsafe absolute or parent-traversal path"))
            canonical = "/".join(part for part in parts if part not in ("", "."))
            if canonical in seen:
                findings.append((name, "warning", "duplicate normalized archive path"))
            seen.add(canonical)
            mode = (info.external_attr >> 16) & 0o170000
            if mode == stat.S_IFLNK:
                findings.append((name, "warning", "symbolic link entry"))
            total += info.file_size
            ratio = info.file_size / max(info.compress_size, 1)
            if info.file_size > 0 and ratio > max_ratio:
                findings.append((name, "warning", f"high compression ratio: {ratio:.1f}:1"))
        if total > max_total_bytes:
            findings.append(("<archive>", "error", f"uncompressed size exceeds limit: {total} bytes"))
    return findings, total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("--max-total-mb", type=float, default=500)
    parser.add_argument("--max-ratio", type=float, default=100)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        findings, total = inspect_archive(args.archive, int(args.max_total_mb * 1024 * 1024), args.max_ratio)
    except (OSError, zipfile.BadZipFile, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"uncompressed_bytes": total, "findings": [
            {"entry": n, "severity": s, "message": m} for n, s, m in findings
        ]}, indent=2))
    else:
        print(f"Inspected {args.archive}: {total} uncompressed bytes")
        for name, severity, message in findings:
            print(f"{severity}: {name}: {message}")
        if not findings:
            print("No suspicious entries found.")
    return 1 if any(s == "error" for _, s, _ in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
