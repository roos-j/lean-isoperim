# Error report — Task 4

Task 4 additions to `automation/ErrorReport.md` (kept separate so that the shared file is unchanged).

## Proof stage, Task 4 ([DIR] §1, §2, §5.4, §7, [DIRX] §4, 2026-11-16)

- 2026-11-16T19:53-08:00 — [DIR] Proposition 2.1 (`Auto.DIR.prop_2_1`, Task 4), cited from [KP20]:
  stated (as in the paper) for all $\beta\ge\frac12$. The induction proof (`sources/two_point_general_beta.tex`)
  needs $\frac12\le\beta\le1$ (triangle inequality for $\ell^{1/\beta}$; $(k+1)^\beta\ge1+(2^\beta-1)k^\beta$,
  false for $\beta=2$, $k=2$). Numerically the statement fails for $\beta>1$: for $\beta=2$ the
  piecewise-linear $B$ through the largest grid solution of (2.2) (step $\frac1{32}$) satisfies
  $G_2[B]\ge0$ on a grid of step $\frac1{512}$ and has $B(\frac18)=\frac{13}8>\frac98\ge\mathcal{B}_2(\frac18)$;
  similarly for $\beta=1.5$. All uses ($\beta_0$, $\frac12$) have $\beta\le1$. Unresolved: proposed fix
  is the extra hypothesis $\beta\le1$; awaiting the user's decision (statement change).
- 2026-11-16T20:07-08:00 — Resolution of the previous entry (user decision): `Auto.DIR.prop_2_1` gets the
  extra hypothesis $\beta\le1$ (docstring: discrepancy paragraph).
- 2026-11-17T01:20-05:00 — [DIR] (7.4), ancillary `anc/partitions.py`: for the partition of $g_{P,3}$ the script
  reports a minimum lower bound $0.000767<0.001$ (the paper claims $>0.001$). With the paper's tight lower
  bound as formalized (`gP3lo_le`) the minimum over the same 26 boxes is $\approx0.0012$, so (7.4) holds as
  stated with the paper's partition. Resolved (no change).
