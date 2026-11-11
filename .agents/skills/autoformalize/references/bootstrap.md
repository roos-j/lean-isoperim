# Starting from an empty or partial repository

Read this when the target has no working Lean project. First perform the instruction and source discovery in `SKILL.md`; a folder with only a blueprint or some Lean files is a partial project, not disposable scaffolding. Its generic file-creation, paper-structured layout, namespace, and header requirements apply to bootstrapping too. The minimal project configuration files are automatically authorized under the project-configuration exception in `SKILL.md`.

## Establish a reproducible environment

Before any of the steps below, perform Step 0 of `SKILL.md`: ensure the recurring 15-minute wake-up job exists (create it automatically if absent). Bootstrapping an empty repository is not a reason to postpone it.

1. Inspect the directory, any ancestor Git repository or worktree, and available tools (`lean`, `lake`, `elan`). If no Git repository owns the directory, initialize one with `git init`, leaving its history empty and making no initial commit or automatic staging. As part of initialization, create an empty root `README.md`, copy [../assets/LICENSE](../assets/LICENSE) to root `LICENSE`, and copy [../assets/.gitignore](../assets/.gitignore) to root `.gitignore`. These files are already authorized by the initialization rule. Preserve any existing versions instead of overwriting them; merge needed ignore patterns into an existing `.gitignore`. Identify existing `lean-toolchain`, `lakefile.toml` or `lakefile.lean`, `lake-manifest.json`, Lean sources, and source documents before generating other files. Do not initialize over or replace existing work.
2. Use Lean 4 and Mathlib unless the user or project specifies otherwise. Preserve any existing compatible pins. If pins are absent, use the latest Mathlib release, counting release candidates, not only stable releases. Query the Mathlib tags at setup time, for example with `git ls-remote --tags https://github.com/leanprover-community/mathlib4`. Choose the newest `vX.Y.Z` or `vX.Y.Z-rcN` tag in version order; a release candidate of a newer version outranks the previous stable release. Pin the Lean toolchain named in that tag's `lean-toolchain`. When the user or project names a version, use that version instead. Do not hard-code a remembered version. Record the exact selection. A nearby warm checkout may inform the choice, but must not silently become a machine-specific dependency.
3. Determine the exact missing setup files and the paper-structured formalization files (one folder per paper and section, one file per subsection or introduction theorem) before initializing. Create the minimal project configuration files automatically under the standing exception in `SKILL.md`, without asking for file-creation approval. For other files, check the applicable authorization. Use the Mathlib project template supported by the selected Lake version only if its generated files fit that authorization and it will not create commits, after checking its help; disable automatic commits or choose manual setup when necessary. Otherwise create the minimal matching configuration by hand. The standard top-level library import file is required and already authorized; do not let a template generate other unauthorized extra Lean files. If the directory already contains files, add only the authorized missing configuration and integrate it without overwriting existing work. Keep the library root at its default whole-module name and create or maintain the corresponding top-level import file under the standing exception in `SKILL.md`. Add imports for the production modules; never set `roots` to individual proof files or use `globs` to bypass this structure. Preserve reproducible dependency pins and appropriate build/cache ignores. Git history must remain unchanged unless the user explicitly instructs otherwise; configuring a remote or publishing is separate work.
4. Fetch dependencies and the matching prebuilt Mathlib cache through the project's supported commands. Retain the dependency manifest and toolchain pins. Do not upgrade an existing environment, run repeated cache downloads, or rebuild all of Mathlib without evidence that it is necessary. Respect execution and installation permissions; do not turn a setup problem into invented proof assumptions.
5. Build the first formalization file importing Mathlib before writing the rest of the scaffold. Include the required linter-compliant header and generation notice and place its Lean code inside `namespace Auto ... end Auto`. Keep the verification result in the authorized continuation record. If tools or dependencies are unavailable, inspect the source and prepare the precise plan and missing-setup diagnosis; do not present uncompiled Lean as validated.

## Choose a small project structure

Use any user-provided or existing package/module name. Otherwise choose a descriptive Lean package name. The formalization follows the paper-structured layout of `SKILL.md`, with all definitions and proofs of a paper in the namespace `Auto.<PaperTag>` (e.g. `Auto.DIR`). For a package whose source files live under `Project/` and a paper tagged `DIR`, the structure is:

```text
README.md                    # initially empty
LICENSE                      # bundled Apache 2.0 text
.gitignore                   # bundled Lean/Lake/LaTeX patterns
lean-toolchain
lakefile.toml                 # lean_lib Project; omit roots and globs
lake-manifest.json
Project.lean                  # module; public-imports every formalization module
Project/
  DIR/
    1_Introduction/
      Thm_1_1.lean            # Theorem 1.1, surrounding text, its corollaries
      Thm_1_5.lean
    2_Envelope_Functions/
      2_0_Envelope_Functions.lean   # text of §2 before §2.1 (if it has definitions/claims)
      2_1_Computed_Envelopes.lean   # one file per subsection
    3_Variants_Bobkov_Inequality/
      3_0_Variants_Bobkov_Inequality.lean   # section without subsections
  Prerequisites/
    NamedTheorem.lean         # only for a qualifying reusable prerequisite
automation/
  instructions.md
  raw.md                     # timestamped raw prompts; ignored by Git
  Status.md
  ErrorReport.md             # when a discrepancy needs recording
sources/                     # paper input (TeX), e.g. sources/DIR/main.tex
```

This layout authorizes exactly these kinds of files; apply the file-creation rules and standing authorizations in `SKILL.md` for anything else. Reuse established source locations such as `blueprint/` or `blueprints/`, but the instructions, status, and error-report Markdown files must reside in `automation/`. Bring any active legacy records from `meta/` or elsewhere into `automation/`, preserving their history and updating references rather than starting competing records. Keep definitions, auxiliary claims and helpers in the file of the subsection where the paper introduces them; do not add `Basic.lean` or convenience modules. Files longer than 10,000 lines are split along subsubsections. When a substantial missing general fact qualifies under `SKILL.md`'s reusable-prerequisites exception, create exactly one dedicated file directly in `Prerequisites/`, without seeking authorization again; its theorem statement and local defining vocabulary must depend only on Mathlib and definitions local to that same file. Document the justification and work in `automation/Status.md`. Do not pre-create speculative prerequisite files during setup. The paper-structured layout, the namespace `Auto`, the 10,000-line limit per Lean file, and the required generation notice are generic requirements.

For every machine-generated Lean file, follow the linter-compliant header in `SKILL.md`: `/-` alone on line 1; line 2 `Copyright (c) YYYY <user's established name>. All rights reserved.` (never omitted or left as a placeholder); line 3 `Released under Apache 2.0 license as described in the file LICENSE.` (with the cited root `LICENSE` present, or the project's actual license line configured via `linter.style.header.license`); line 4 `Authors: Codex` without a trailing period; `-/` alone on line 5. Use Lean's module system from the start: after the header put the line `module`, then the imports as `public import …`, then the module docstring whose first paragraph after its `#` title is exactly `This file was automatically generated by Codex.`, then `@[expose] public section`, then `namespace Auto`. The top-level import file is likewise a `module` consisting of `public import` lines. Use the project's actual legal notices and preserve existing attribution.

Retain original source names, labels, and version information. For online sources, record the verified URL and version/date. Prefer source TeX when available; keep paper PDFs usable without requiring TeX conversion. Never replace a supplied blueprint with a newly generated one simply to fit this layout.

## Leave enough local guidance to resume

In `automation/instructions.md` (or the existing capitalization/effort-specific name within `automation/`), record:

- The exact source(s), intended main statements, scoped prerequisites, and explicit exclusions.
- The paper-structured layout (paper tags, section folders, files), any qualifying reusable-prerequisite files under `Prerequisites/`, the `Auto` namespace, any user-specified exceptions, toolchain/dependency pins, and tested build commands.
- The paths to the status and error-report files within `automation/`, and their conventions.
- Any substantive interpretation of the source or local implementation choice.
- The selected next source item, required dependencies, and any real setup blocker.
- Each task-specific user prompt in distilled form with its timestamp and a pointer to its raw entry in `automation/raw.md`, as required by `SKILL.md`; record the initial request before implementing it and preserve subsequent corrections and decisions. All timestamps use the computer's local timezone with the appropriate UTC offset. The latest specific user instructions override conflicting earlier instructions and this skill.

Keep the raw prompt log in `automation/raw.md` and ensure `automation/raw.md` is included in the root `.gitignore` by default, including when resuming an existing repository. Move any embedded raw log there, preserving timestamps and wording except for required path normalization. Never write absolute filesystem paths to any files; use repository-relative or user-directory-relative paths such as `~/.codex`, including in raw prompts and saved commands.

If there is no existing agent entry point, propose a short root `AGENTS.md` pointing future agents to these instructions and the status ledger; create it only when authorized. Do not copy the entire global skill into the repository or turn tentative decisions into immutable user restrictions.

Read the target proofs and populate the ledger before implementing their steps, with one fine-grained row per individual source step, equation, or lemma, listed in forward reasoning order as `SKILL.md` requires. Put main theorem statement rows first, reusable-prerequisite sections with their justifications and work rows immediately afterward, and main-proof rows after those sections. Initial rows are `not started` unless actual source inspection and verification establish otherwise. When starting directly from a paper, this ledger and the precise statements in continuation notes provide a working proof plan; a separate publication-ready blueprint, website, dependency visualization, or submission package is unnecessary unless requested.

Once setup is complete, continue through the ledger one logical work item at a time until all scoped main results are fully proved and pass the standard-axiom and build checks. Record every source/formalization discrepancy concisely with a timestamp and resolution in `ErrorReport.md`. If resolving a discrepancy requires changing the mathematics of a main result, stop, report, and ask for the user's direction, as required in `SKILL.md`.
