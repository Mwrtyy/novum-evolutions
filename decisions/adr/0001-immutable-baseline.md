# ADR 0001 — Keep NOVUM 2.0.0 byte-immutable

Status: accepted

## Decision

The inherited `2.0.0` archive is the scientific baseline and is preserved byte-for-byte. Corrections, normalization, or repackaging must create a new artifact identity.

## Why

The lab needs an unambiguous behavioral control and rollback target. Historical candidate results are meaningful only if the baseline cannot drift under them.

## Trade-off

Known packaging quirks remain in the artifact. This is preferable to silently rewriting history.
