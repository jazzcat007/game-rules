# Contributing

1. **One game per file**: `games/<id>.yaml`, where the id is lowercase words
   joined by hyphens.
2. **Your own words.** Read the official rulebook, then write the rules
   from scratch. Don't paste or lightly reword its text, and don't include
   its images or card text.
3. **Link the source.** Prefer the publisher's own rulebook or FAQ
   (`kind: official` or `publisher-faq`). A well-known reference such as
   pagat.com is `reference`. Forums and wikis are `community`, and should
   only back a clarification, never a core rule. Give the date you checked
   it.
4. **Name the edition.** When printings differ, describe the one you
   checked and note the difference under `editions`.
5. **No guesses.** If the rulebook doesn't settle a question, say so in
   `clarifications` and leave it for the table to decide.
6. **Keep steps short.** Each step should make sense on its own when read
   aloud.
7. **Rebuild the index:** `python tools/build_index.py` and include the
   updated `games/index.json` in your commit.
8. **Validate before you open a pull request:** `python tools/validate.py`.

By contributing, you agree to license your rules text under CC BY 4.0 and
any code under MIT.
