# ADR 0001 — Pin NOVUM 2.0.0 as an immutable source artifact

Status: accepted

## Decision

NOVUM Innovation `2.0.0` is the scientific baseline. Its authority is the exact archive in `Mwrtyy/novum-innovation-lab` at commit `e591937931d2a04f2b308e23f2edca488bea9fcd`, path `NOVUM/accepted/novum-innovation-v2.0.0.zip`, Git blob `66c87b983d126d0c1a21bae17e83b6a30a17a770`, SHA-256 `e38cd4e62439c5759bf99bf2fc72e165abf2876f75396c170f445d6a3c529dda`.

The Evolution Lab stores this as a commit-pinned reference rather than a second connector-copied binary. Any materialized archive must verify the expected SHA-256 before use.

## Why

The lab needs an unambiguous control and rollback target. A commit-pinned source artifact plus cryptographic identities prevents baseline drift without pretending a transported copy is authoritative.

## Trade-off

Experiments need source-repository access (or a separately verified local copy) to materialize the package. This is preferable to silently accepting a binary copy whose transport integrity was not established.
