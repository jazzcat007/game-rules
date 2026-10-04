# game-rules

Plain-language rules for tabletop games: one YAML file per game, easy for
people to read and for programs to use. A voice assistant hosting game night
can look up "how does a Grand Escape work?" and answer from these files.

Every file is written **in our own words** and links to the official
rulebook it was checked against. Game mechanics can't be copyrighted, but
the wording of a rulebook can, so nothing here is copied from one.

## Games

| File | Game | Publisher |
|---|---|---|
| [drop-trivia.yaml](games/drop-trivia.yaml) | Drop Trivia (Trivial Pursuit) | Hasbro |
| [finders-creepers.yaml](games/finders-creepers.yaml) | Finders Creepers | MGA Games |
| [uno-express.yaml](games/uno-express.yaml) | UNO Express | Mattel |
| [yahtzee.yaml](games/yahtzee.yaml) | Yahtzee | Hasbro |

## Format

```yaml
id: finders-creepers          # required; must match the file name
title: Finders Creepers       # required
publisher: MGA Games          # required
edition: "First edition (2024)"
players: {min: 2, max: 4}     # required; min is an integer, max optional
ages: 8
playtime_minutes: 30-45
components: [...]
sources:                      # required; at least one
  - url: https://...          # https only
    kind: official            # official | publisher-faq | reference | community
    retrieved: 2026-10-03     # date the source was last checked
    note: optional
summary: >                    # required; two or three sentences
  ...
end:                          # required; how the game finishes
  type: target                # target | rounds | fixed-turns | condition
  target: 3                   # target needs `target`, rounds needs `rounds`,
                              # fixed-turns needs `turns`
winning: ...                  # required; one sentence
```

Everything else is free-form sections such as `setup`, `turn`, `round`,
`scoring`, `fouls`, `variants`, `clarifications` (a list of `q`/`a` pairs)
and `editions` (where printings differ). Each section is a list of short
steps or a mapping of lists. Use whatever sections fit the game, and write
each step so it makes sense on its own when read aloud.

## games/index.json

A generated summary (id, title, publisher, players, end) of every game, for
a consumer that just wants to know what's available without fetching every
file. Rebuild it after adding or editing a game:

```bash
python tools/build_index.py
```

`validate.py` fails if it's out of date.

## Checking a file

```bash
pip install pyyaml
python tools/validate.py            # all games, plus the index
python tools/validate.py games/yahtzee.yaml   # one file only, no index check
```

CI runs the same check on every push and pull request.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: one game per file, your own
words, the official source linked, and differences between editions noted
rather than guessed.

## Licence

Rules files (`games/`) are [CC BY 4.0](LICENSE-CONTENT). Scripts are
[MIT](LICENSE). Game names are trademarks of their owners, used only to
identify the games. This project is not affiliated with any publisher.
