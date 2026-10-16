---
name: autoformalize
description: Translate mathematical definitions, theorem statements, and informal proofs into Lean, or complete and repair Lean proofs in this repository.
---

# Autoformalize

Read the root `AGENTS.md` for the toolchain, module layout, and verification rules.

## Establish the statement

Extract the objects, domains, quantifiers, hypotheses, and conclusion from the
source mathematics. Preserve strict versus non-strict inequalities, nonemptiness,
regularity, and finiteness assumptions. If an ambiguity changes the theorem,
identify it explicitly; do not silently choose an easier claim. Distinguish
formalizing a statement from completing its proof.

Inspect existing definitions and imports before introducing representations. This
repository depends on Mathlib and LeanCert. Search their sources under
`.lake/packages/` and import the modules needed for their tactics and declarations.
If another dependency is needed, explain why and select a revision
compatible with the pinned Lean version; do not change Lean to make it fit.

## Build the proof

Search local sources with `rg` for existing declarations. Use small `#check` or
`#print` probes through `lake env lean` to confirm types, namespaces, and implicit
arguments. Check coercions, typeclass requirements, and notation scopes when an
apparently matching lemma fails.

Translate the informal argument into intermediate claims with explicit types.
Compile small increments, inspect the actual goal and error, and resolve the first
underlying failure before adjusting downstream proofs. Prefer reusable lemmas and
focused tactics to brittle automation. Use only tactics available in the imports.
Remove temporary probes and scratch files when they have served their purpose.

Do not replace missing mathematics with axioms, assume the target conclusion,
weaken the target statement, or use unsafe mechanisms to bypass kernel checking.
If the source claim is false or lacks a hypothesis, explain the obstruction.

## Verify and report

Check the changed modules and run `lake build` after wiring their imports into
`Isoperim.lean`. Inspect completed proofs for `sorry` and `admit`; for substantive
new theorems, use a temporary `#print axioms` probe to check for `sorryAx` or
unexpected custom axioms. Standard Lean axioms such as `Classical.choice`,
`propext`, and `Quot.sound` are not proof holes.

Report the correspondence between the formal statement and the source, the checks
actually run, and any remaining holes or environmental blockers. A successful
build alone does not certify that the formal statement matches the intended math.
