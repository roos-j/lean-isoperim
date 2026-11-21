# Formalization of sharp isoperimetric inequalities on the Hamming cube

[![Lean build](https://github.com/roos-j/lean-isoperim/actions/workflows/lean_build.yml/badge.svg)](https://github.com/roos-j/lean-isoperim/actions/workflows/lean_build.yml)

This is a Lean 4 formalization of the papers

- [DIR] P. Durcik, P. Ivanisvili, J. Roos, *Sharp isoperimetric inequalities on the Hamming cube
  near the critical exponent*, Adv. Math. 503 (2026), 111264,
  [doi:10.1016/j.aim.2026.111264](https://doi.org/10.1016/j.aim.2026.111264),
  [arXiv:2407.12674](https://arxiv.org/abs/2407.12674);
- [DIRX] P. Durcik, P. Ivanisvili, J. Roos, X. Xie, *Sharp isoperimetric inequalities on the
  Hamming cube II: The critical exponent*, [arXiv:2602.20462](https://arxiv.org/abs/2602.20462).

The Lean code in this formalization was fully produced by coding agents, specifically Claude Code Opus 5.5 Medium.

The formalization lives in the two folders `Isoperim/DIR` and `Isoperim/DIRX`, respectively. The subfolder structure roughly corresponds to the structure of the paper and most mathematical claims in the paper are represented by corresponding Lean statements as indicated in docstrings. Discrepancies between Lean and paper statements are stated in docstrings, and mostly further explained in the error report files in the `automation` folder. That folder also contains other metadata documenting the autoformalization process, including instructions given to agents.

## Palomar submission

The files `Challenge.lean`, `Solution.lean`, `comparator.json` and `formalization.yaml` prepare a
submission to the [Palomar Registry](https://palomar-registry.org). The compared theorems are:

- `Auto.DIRX.thm_1_1`: [DIRX] Theorem 1.1, the sharp isoperimetric inequality at the critical
  exponent;
- `Auto.DIRX.thm_1_2`: [DIRX] Theorem 1.2, the conjecture of Kahn and Park on cube partitions;
- `Auto.DIRX.thm_1_3`: [DIRX] Theorem 1.3, the sharp L1 Poincare inequality for Boolean-valued
  functions;
- `Auto.DIRX.eqn_2_5`: [DIRX] inequality (2.5);
- `Auto.DIR.cor_2_5`: [DIR] Corollary 2.5.

`Challenge.lean` repeats the definitions of `Isoperim/Definitions.lean` verbatim (this module
collects all definitions on which the compared statements depend), followed by the statements;
`Solution.lean` imports the library `Isoperim`.
