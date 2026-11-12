# Repository instructions

> **Task agents (proof stage): your task prompt and declaration list are in `automation/splitting.md`.**

## PROOF STAGE RULES (read first; binding for every coding agent)

1. **Auxiliary files.** If a proof gets longer than 100 lines, or needs additional lemmas,
   definitions or details beyond what the scaffold states, put that work in a separate file in
   the same folder named after the file with the suffix `_aux`, e.g.
   `Isoperim/DIRX/2_Preliminaries/2_2_Properties_J_aux.lean` for `2_2_Properties_J.lean`.
   The main file imports its `_aux` file; the `_aux` file must not import the main file (state
   results of the main file that an auxiliary lemma needs as hypotheses of that lemma). Same
   header, namespace (`Auto.DIR` / `Auto.DIRX`), notation and docstring conventions as the main
   files; add the `_aux` module to `Isoperim.lean`. Do not change the statements of the scaffold.
2. **Completion.** A proof is complete only when it no longer depends on `sorry`, directly or
   transitively (check with `#print axioms <name>`).
3. **Axioms.** Allowed: the standard Lean axioms `propext`, `Classical.choice`, `Quot.sound`; and,
   only for the computer-assisted (🚗) claims and declarations depending on them, the standard
   axioms used by LeanCert's certified-computation tactics. No other axioms, no `admit`, no
   `implemented_by`/`extern` tricks.
4. **Start condition.** Work on a proof may start only when the proofs of all its dependencies
   are complete. The dependencies of every declaration (statement plus paper-proof
   dependencies) are listed in `automation/proof_dependencies.txt`; Lean's import order and
   file order are consistent with them.
5. **Work split. TASK AGENTS: START WITH `automation/splitting.md`** — it contains your task prompt, the list
   of your declarations, and the order of work. The work is split into Tasks 1–5 (Task 1
   preparation; Tasks 2, 3, 4 disjoint and parallel; Task 5 wrap-up). Work only on declarations
   of your task.
6. **Commits.** See `CLAUDE.md` (author = prompting user, one-line `[claude]` message,
   `Co-authored-by: Claude` trailer).

This Lean library formalizes the papers [DIR] (arXiv:2407.12674) and [DIRX]
(arXiv:2602.20462); it is pinned to `leanprover/lean4:v4.35.0` in
`lean-toolchain`. Preserve that pin unless the user requests an upgrade.
Mathlib and LeanCert are pinned to their `v4.35.0` releases in `lakefile.toml`.
Preserve compatible dependency pins when adding or updating packages.

## Layout and validation

- `lakefile.toml` defines the `Isoperim` library and default build target.
- The formalization follows the paper-structured layout under `Isoperim/DIR/` and
  `Isoperim/DIRX/` (one folder per section, one file per subsection or introduction
  theorem). Import all modules from `Isoperim.lean` so `lake build` checks them.
- Before working, read `automation/instructions.md` (local conventions, scope, status
  pointers) and `automation/Status.md`. These local instructions supersede conflicting
  guidance in the skill; the user's current explicit instructions take precedence over both.
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
