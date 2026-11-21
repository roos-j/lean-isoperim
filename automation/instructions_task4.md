# Instructions — Task 4

Task 4 additions to `automation/instructions.md` (the shared file is unchanged).

- **2026-11-16T19:40-08:00** (Task 4 start, raw entry in `automation/raw.md`): formalize Task 4
  following the instructions; for the Kahn–Park reduction consult `sources/two_point_general_beta.tex`
  (proof for $\frac12\le\beta\le1$); do not stop until Task 4 is complete unless there is an error or a
  problem, in which case stop and report it.
- **2026-11-16T20:07-08:00** (raw entry): approved adding $\beta\le1$ to `Auto.DIR.prop_2_1`; continue
  Task 4.

## Status

Task 4 complete (2026-11-17): all 89 declarations proved; `#print axioms` shows only `propext`,
`Classical.choice`, `Quot.sound` for all 89. `Auto.DIR.prop_2_1` assumes $\beta\le1$ (user decision,
`automation/ErrorReport_task4.md`, 2026-11-16). Entries in `automation/Status_task4.md`.

Auxiliary files: one `_aux.lean` file per main file (the original per-module structure); the
certificates of (5.11), (7.3)/(7.4) and [DIRX] (4.2)/(4.3) are the last section of the `_aux` file of
their main file.
