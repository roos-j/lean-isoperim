# Formalization of sharp isoperimetric inequalities on the Hamming cube

[![Lean build](https://github.com/roos-j/lean-isoperim/actions/workflows/lean_build.yml/badge.svg)](https://github.com/roos-j/lean-isoperim/actions/workflows/lean_build.yml)

This is a Lean 4 formalization of the papers

- [DIR] P. Durcik, P. Ivanisvili, J. Roos, *Sharp isoperimetric inequalities on the Hamming cube
  near the critical exponent*, [arXiv:2407.12674](https://arxiv.org/abs/2407.12674);
- [DIRX] P. Durcik, P. Ivanisvili, J. Roos, X. Xie, *Sharp isoperimetric inequalities on the
  Hamming cube II: The critical exponent*, [arXiv:2602.20462](https://arxiv.org/abs/2602.20462).

The Lean code in this formalization was fully produced by coding agents, specifically Claude Code Opus 5.5 Medium.

The formalization lives in the two folders `Isoperim/DIR` and `Isoperim/DIRX`, respectively. The subfolder structure roughly corresponds to the structure of the paper and most mathematical claims in the paper are represented by corresponding Lean statements as indicated in docstrings. Discrepancies between Lean and paper statements are stated in docstrings, and mostly further explained in the error report files in the `automation` folder. That folder also contains other metadata documenting the autoformalization process, including instructions given to agents.
