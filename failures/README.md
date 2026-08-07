# Behavioral Failure Corpus

A corpus row represents a concrete undesirable behavior that can be reproduced and judged. It is not a wishlist item.

`corpus.jsonl` fields:

- `id`
- `family`
- `source`: `historical` or `synthetic`
- `prompt_or_fixture`
- `red_behavior`: observable failure
- `green_behavior`: what a genuine repair must do
- `evidence_ref`: historical path/result when applicable
- `notes`

The corpus is allowed to grow only when a new row adds a distinct reproducible failure. Do not duplicate the same weakness with different wording to make the dataset look larger.
