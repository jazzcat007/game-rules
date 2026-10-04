#!/usr/bin/env python3
"""Regenerate games/index.json from games/*.yaml.

A consumer that only needs to know what's available (id, title, publisher,
player count, how the game ends) can fetch this one small file instead of
every game file. Run after adding or editing a game:

    python tools/build_index.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ('id', 'title', 'publisher', 'players', 'end')


def build() -> list[dict]:
    games = []
    for path in sorted((ROOT / 'games').glob('*.yaml')):
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
        games.append({k: data.get(k) for k in FIELDS})
    return games


def main() -> int:
    index = build()
    out = ROOT / 'games' / 'index.json'
    out.write_text(json.dumps(index, indent=2) + '\n', encoding='utf-8')
    print(f'wrote {len(index)} game(s) to {out.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
