# ADR 0002 — Final holdouts are selected after candidate freeze

Status: accepted

## Decision

Exact promotion holdout tasks must not be available to candidate-development reasoning before mutation bytes and judge instructions are frozen.

## Why

The historical six-task benchmark was visible and therefore useful for regression, but repeated development against visible tasks turns the benchmark into a target. Post-freeze selection reduces Goodhart pressure.

## Trade-off

The repository cannot fully contain the final exam in advance. Auditability comes from recording the post-freeze generation/selection process, seed/owner, timestamps, and hashes rather than precommitting visible task text.
