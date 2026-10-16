# Repository instructions

This is a blank Lean library, pinned to `leanprover/lean4:v4.35.0` in
`lean-toolchain`. Preserve that pin unless the user requests an upgrade.
Mathlib and LeanCert are pinned to their `v4.35.0` releases in `lakefile.toml`.
Preserve compatible dependency pins when adding or updating packages.

## Layout and validation

- `lakefile.toml` defines the `Isoperim` library and default build target.
- Put new modules under `Isoperim/` and import public modules from `Isoperim.lean`
  so `lake build` checks them.
- Run commands from the repository root: `lake env lean --version`,
  `lake env lean Isoperim/Module.lean`, and finally `lake build`.
- Keep Lake's generated `lake-manifest.json` tracked when present; do not edit
  it manually. Build outputs in `.lake/` are ignored.

## Formalization

Use the repository's `autoformalize` skill for translating mathematical statements
and proofs into Lean. Codex discovers it at `.agents/skills/autoformalize/SKILL.md`;
Claude Code discovers it at `.claude/skills/autoformalize/SKILL.md`.
Keep both skill copies in sync.

Preserve the intended statement, quantifiers, domains, and hypotheses. Do not
weaken a theorem or assume its conclusion to obtain a compiling proof. Completed
proofs must contain no `sorry`, `admit`, or new axioms that bypass proof obligations.
Temporary holes are acceptable during development but must be resolved or clearly
reported as unfinished. Never describe an uncompiled proof as verified.

Prefer existing lemmas and small named helper results. Check installed source and
Lean's elaborator for actual APIs rather than inventing lemma names. Report changed
declarations, verification commands and outcomes, and any remaining proof gaps.
