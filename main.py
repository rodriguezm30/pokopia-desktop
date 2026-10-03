"""Pokopia Desktop — A local helper for Pokémon Pokopia island folders, saves, and photo albums on Windows and macOS."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='pokopia_desktop',
        description='A local helper for Pokémon Pokopia island folders, saves, and photo albums on Windows and macOS.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Pokopia Desktop')
    print('Keep the island folder tidy before a DLC or town reset.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
