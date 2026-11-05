#!/usr/bin/env python3
"""Install Arc Dark's GTK 4 user stylesheet in a GTK configuration directory."""

import argparse
import base64
import os
from pathlib import Path
import re
import stat
import tempfile

ASSETS = Path(__file__).resolve().parents[1] / "assets"
IMPORT = b'@import url("arc-dark-49-apps.css");\n'


def embed_asset(match):
    name = match.group(1)
    image = (ASSETS / name).read_bytes()
    data = base64.b64encode(image).decode("ascii")
    return f'url("data:image/png;base64,{data}")'


def replace_file(path, data):
    # Follow existing dotfile symlinks; keep custom CSS and permissions.
    path = path.resolve()
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as staged:
        try:
            staged.write(data)
            staged.flush()
            os.chmod(staged.name, mode)
            os.replace(staged.name, path)
        finally:
            Path(staged.name).unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gtk-dir", type=Path, default=Path(
        os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config") / "gtk-4.0")
    args = parser.parse_args()
    source = Path(__file__).with_name("arc-dark-apps.css").read_text()
    sheet = re.sub(r'url\("assets/([\w@.-]+\.png)"\)', embed_asset, source).encode()
    args.gtk_dir.mkdir(parents=True, exist_ok=True)
    replace_file(args.gtk_dir / "arc-dark-49-apps.css", sheet)
    entry = args.gtk_dir / "gtk.css"
    previous = entry.read_bytes() if entry.exists() else b""
    if IMPORT.rstrip() not in previous.splitlines():
        replace_file(entry, IMPORT + previous)
    print(f"Installed Arc Dark application styles in {args.gtk_dir}")


if __name__ == "__main__":
    main()
