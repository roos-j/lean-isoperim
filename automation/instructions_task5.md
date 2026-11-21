# Instructions — Task 5

Task 5 additions to `automation/instructions.md` (the shared file is unchanged). Raw prompts:
`automation/raw.md`, entries T5-1 … T5-5.

- **2026-11-20** (user, T5-1, T5-2): after the cleanup commit, do Task 5 of `automation/splitting.md`;
  commit only once, at the very end of Task 5.
- **2026-11-20** (user, T5-3): do not rebuild the expensive certificate files once they are built
  (keep the `.olean`s); in particular, do not edit them.
- **2026-11-20T19:29-05:00** (user decision, T5-5): [DIR] Theorem 1.10 (`Auto.DIR.thm_1_10`), first
  conjunct, is restricted to $2\beta_0\le p\le2$ (the paper's $p\ge2\beta_0$ is false for large $p$,
  see `automation/ErrorReport_task5.md`).

## Status

Task 5 complete (2026-11-20): all 22 declarations proved; entries in `automation/Status_task5.md`,
discrepancies in `automation/ErrorReport_task5.md`. Full `lake build` green with no warnings and
no `sorry` in the library (2026-11-20); `#print axioms` shows only `propext`, `Classical.choice`,
`Quot.sound` for all 22.

New auxiliary files (rule 1): `Thm_1_1_aux.lean` (subcubes, half-cubes, the chain of Corollary
1.9, also used by [DIRX] Theorems 1.2, 1.3), `Thm_1_6_aux.lean` (digit sums, bounds for
$\mathcal{B}_1$), `Thm_1_10_aux.lean` (certified values of $J$, $b_{\beta_0}(x)+b_{\beta_0}(1-x)\ge
4x(1-x)$, interpolation in $p$), `2_2_Proofs_Theorems_1_1_1_5_1_7_aux.lean` (Lemma 5.2 for
$G_\beta$), [DIRX] `2_1_Reduction_Two_Point_Inequality_aux.lean` ($B_w\ge0$, $B_w(0)=B_w(1)=0$); the
assembly of Theorem 2.2 is in `2_0_Envelope_Functions_aux.lean`.
