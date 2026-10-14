#!/usr/bin/env python3
"""Check the published AUL source manifest without third-party modules."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    manifest = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
    if manifest.get("version") != "1.0-draft.1" or manifest.get("osi_approved") is not False:
        print("Manifest metadata is inconsistent with this AUL draft.", file=sys.stderr)
        return 1
    entries = manifest.get("files")
    if not isinstance(entries, dict) or not entries:
        print("Manifest has no file entries.", file=sys.stderr)
        return 1

    failures = []
    for name, expected in entries.items():
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or not isinstance(expected, str):
            failures.append(f"{name}: unsafe path or invalid checksum")
            continue
        target = ROOT.joinpath(*path.parts)
        if not target.is_file() or target.is_symlink():
            failures.append(f"{name}: missing file or symlink")
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected.lower():
            failures.append(f"{name}: sha256 mismatch")

    license_text = (ROOT / "LICENSE.txt").read_text(encoding="utf-8")
    if "AGENT UPSTREAM LICENSE" not in license_text or "Version 1.0-draft.1" not in license_text:
        failures.append("LICENSE.txt: expected draft header missing")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"AUL manifest: verified {len(entries)} files (integrity checks only).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
