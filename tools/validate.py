#!/usr/bin/env python3
"""Check every games/*.yaml file against the format described in README.md.

Usage: python tools/validate.py [files...]   (defaults to games/*.yaml)
Exits 1 and prints one line per problem if anything is wrong.
"""

from __future__ import annotations

import datetime
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ('id', 'title', 'publisher', 'players', 'sources', 'summary', 'end', 'winning')
SOURCE_KINDS = ('official', 'publisher-faq', 'reference', 'community')
END_TYPES = {'target': 'target', 'rounds': 'rounds', 'fixed-turns': 'turns', 'condition': None}
ID = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')


def check(path: Path) -> list[str]:
    try:
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
    except yaml.YAMLError as exc:
        return [f'not valid YAML: {exc}']
    if not isinstance(data, dict):
        return ['top level must be a mapping']
    problems = [f'missing {key}' for key in REQUIRED if key not in data]

    gid = data.get('id')
    if gid is not None and (not isinstance(gid, str) or not ID.match(gid)):
        problems.append('id must be lowercase words joined by hyphens')
    elif gid != path.stem:
        problems.append(f'id {gid!r} must match the file name {path.stem!r}')

    players = data.get('players')
    if players is not None:
        if not isinstance(players, dict) or not isinstance(players.get('min'), int):
            problems.append('players needs an integer min')
        elif isinstance(players.get('max'), int) and players['max'] < players['min']:
            problems.append('players max is below min')

    sources = data.get('sources')
    if sources is not None:
        if not isinstance(sources, list) or not sources:
            problems.append('sources must be a non-empty list')
        else:
            for i, src in enumerate(sources):
                where = f'sources[{i}]'
                if not isinstance(src, dict):
                    problems.append(f'{where} must be a mapping')
                    continue
                if not str(src.get('url', '')).startswith('https://'):
                    problems.append(f'{where}.url must be an https URL')
                if src.get('kind') not in SOURCE_KINDS:
                    problems.append(f'{where}.kind must be one of {", ".join(SOURCE_KINDS)}')
                if not isinstance(src.get('retrieved'), datetime.date):
                    problems.append(f'{where}.retrieved must be a date (YYYY-MM-DD)')

    end = data.get('end')
    if end is not None:
        kind = end.get('type') if isinstance(end, dict) else None
        if kind not in END_TYPES:
            problems.append(f'end.type must be one of {", ".join(END_TYPES)}')
        elif END_TYPES[kind] and not isinstance(end.get(END_TYPES[kind]), int):
            problems.append(f'end type {kind} needs an integer {END_TYPES[kind]}')
    return problems


def main(argv: list[str]) -> int:
    paths = [Path(a) for a in argv] or sorted((ROOT / 'games').glob('*.yaml'))
    failed = 0
    for path in paths:
        for problem in check(path):
            print(f'{path.name}: {problem}')
            failed += 1
    if not failed:
        print(f'{len(paths)} game file(s) OK')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
