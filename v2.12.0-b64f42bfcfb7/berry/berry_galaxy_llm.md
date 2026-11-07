# ARCHITECTURAL_BRIEF: berry
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/yarnpkg/berry.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1152 analyzed artifact(s), 88423 LOC.
- **Load-bearing artifact:** `packages/yarnpkg-core/sources/Configuration.ts` -- 77 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/acceptance-tests/pkg-tests-specs/sources/pnp.test.js` -- pulls in 46 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/yarnpkg-core/sources/Project.ts` at magnitude 1936.1 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 3799 |
| Analyzed Artifacts (Scanned) | 1152 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2647 |
| Total LOC | 88423 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 30.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7687 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1599 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3134 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 83 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 480 | 67791 | 41.7% |
| JAVASCRIPT | 309 | 14900 | 26.8% |
| PLAINTEXT | 212 | 0 | 18.4% |
| MARKDOWN | 52 | 0 | 4.5% |
| YAML | 40 | 2032 | 3.5% |
| SHELL | 26 | 902 | 2.3% |
| CSS | 10 | 834 | 0.9% |
| JSON | 9 | 1779 | 0.8% |
| XML | 6 | 0 | 0.5% |
| C | 2 | 62 | 0.2% |
| DOCKERFILE | 2 | 16 | 0.2% |
| PYTHON | 1 | 0 | 0.1% |
| PERL | 1 | 101 | 0.1% |
| BATCH | 1 | 1 | 0.1% |
| POWERSHELL | 1 | 5 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1152 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 52%, Declarative / Non-Code 17%, Large Core Modules (3) 6%, Callbacks & Closures Files 5%, Parameter Forwarders Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 887 | 77.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 264 | 22.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2647*

**Composition by Extension & Reason:**
- `.zip`: 2223x Excluded (Explicitly Denied Extension: '.zip')
- `no_extension`: 101x Unsupported Format (.undeterminable), 68x Excluded (Binary Format Detected), 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mdx`: 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 33 exceeds 500 chars), 1x Excluded (Saturation: Line 65 exceeds 500 chars)
- `.diff`: 35x Excluded (Unsupported Extension: '.diff')
- `.ts`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 289 LOC)
- `.js`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 5 exceeds 500 chars), 2x Excluded (Embedded Array/Matrix Payload: 90519 commas in 941 LOC)
- `.json`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 180 LOC)
- `.snap`: 13x Excluded (Unsupported Extension: '.snap'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 13x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.idx`: 6x Excluded (Unsupported Extension: '.idx')
- `.pack`: 6x Excluded (Unsupported Extension: '.pack')
- `.txt`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 22.2 | 12.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 82.7 | 36.5 | 50.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 24.8 | 21.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 36.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 43.2 | 20.6 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1059 | 157 | 1 | `packages/yarnpkg-libzip/tests/ZipFS.test.ts` |
| cleanup | 92 | 28 | 0 | `packages/yarnpkg-fslib/tests/patchedFs.test.ts` |
| guards | 2523 | 329 | 6 | `packages/yarnpkg-libzip/sources/ZipFS.ts` |
| danger | 2005 | 325 | 5 | `packages/yarnpkg-libzip/sources/ZipFS.ts` |
| concurrency | 10399 | 376 | 22 | `packages/yarnpkg-shell/tests/shell.test.ts` |
| connectivity | 3477 | 627 | 7 | `packages/plugin-constraints/sources/tauProlog.d.ts` |
| io | 3847 | 357 | 8 | `packages/acceptance-tests/pkg-tests-specs/sources/node-modules.test.ts` |
| crypto | 10 | 10 | 0 | `packages/plugin-compat/extra/typescript/gen-typescript-patch.js` |
| ipc | 35 | 20 | 0 | `packages/yarnpkg-core/sources/TaskPool.ts` |
| time | 135 | 35 | 0 | `packages/acceptance-tests/pkg-tests-core/sources/utils/tests.ts` |
| serialization | 243 | 89 | 0 | `packages/acceptance-tests/pkg-tests-specs/sources/pnp.test.js` |
| regex | 407 | 136 | 1 | `packages/yarnpkg-sdks/sources/sdks/base.ts` |
| events | 611 | 154 | 1 | `packages/yarnpkg-shell/tests/shell.test.ts` |
| tests | 4230 | 155 | 8 | `packages/yarnpkg-shell/tests/shell.test.ts` |
| docs | 687 | 149 | 1 | `packages/acceptance-tests/pkg-tests-specs/sources/plugins/plugin-typescript.test.ts` |
| debt | 562 | 158 | 1 | `packages/plugin-constraints/sources/tauProlog.d.ts` |
| mutation | 15082 | 739 | 34 | `packages/yarnpkg-core/sources/Project.ts` |
| dead_code | 133 | 64 | 0 | `packages/plugin-constraints/sources/tauProlog.d.ts` |
| credential | 3 | 3 | 0 | `packages/yarnpkg-libzip/sources/libzipAsync.js` |
| threat | 11 | 8 | 0 | `packages/yarnpkg-libzip/sources/libzipAsync.js` |
| ml_ai | 104 | 31 | 0 | `packages/docusaurus/src/components/StarrySky.tsx` |
| ui | 467 | 35 | 0 | `packages/plugin-interactive-tools/sources/commands/search.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/acceptance-tests/pkg-tests-specs/sources/node-modules.test.ts` (Hits: 265)
- `packages/acceptance-tests/pkg-tests-specs/sources/features/installArtifactCleanup.test.ts` (Hits: 188)
- `packages/acceptance-tests/pkg-tests-specs/sources/pnp-esm.test.ts` (Hits: 124)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Configuration.ts** (`packages/yarnpkg-core/sources/Configuration.ts`) — 77 inbound connections
2. **StreamReport.ts** (`packages/yarnpkg-core/sources/StreamReport.ts`) — 38 inbound connections
3. **types.ts** (`packages/yarnpkg-core/sources/types.ts`) — 27 inbound connections
4. **path.ts** (`packages/yarnpkg-fslib/sources/path.ts`) — 25 inbound connections
5. **Manifest.ts** (`packages/yarnpkg-core/sources/Manifest.ts`) — 20 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **pnp.test.js** (`packages/acceptance-tests/pkg-tests-specs/sources/pnp.test.js`) — 46 outbound dependencies
2. **index.ts** (`packages/plugin-essentials/sources/index.ts`) — 41 outbound dependencies
3. **Project.ts** (`packages/yarnpkg-core/sources/Project.ts`) — 38 outbound dependencies
4. **index.ts** (`packages/yarnpkg-core/sources/index.ts`) — 36 outbound dependencies
5. **README.md** (`README.md`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `makeApi` **(Many-Argument Workhorses)** (@ `packages/yarnpkg-pnp/sources/loader/makeApi.ts`) -> Impact: **372.5** | LOC: 1007
- `load` **(Many-Argument Workhorses)** (@ `packages/yarnpkg-core/sources/Manifest.ts`) -> Impact: **272.7** | LOC: 465
- `addPackageToTree` **(Many-Argument Workhorses)** (@ `packages/yarnpkg-nm/sources/buildNodeModulesTree.ts`) -> Impact: **187.6** | LOC: 152
- `linkEverything` **(Compute Cores)** (@ `packages/yarnpkg-core/sources/Project.ts`) -> Impact: **180.4** | LOC: 526
- `persistNodeModules` **(Many-Argument Workhorses)** (@ `packages/plugin-nm/sources/NodeModulesLinker.ts`) -> Impact: **164.1** | LOC: 282
- `exportTo` **(Many-Argument Workhorses)** (@ `packages/yarnpkg-core/sources/Manifest.ts`) -> Impact: **152.9** | LOC: 217
- `fetchPackageFromCache` **(Many-Argument Workhorses)** (@ `packages/yarnpkg-core/sources/Cache.ts`) -> Impact: **149.8** | LOC: 277
- `applyPatch` **(Many-Argument Workhorses)** (@ `packages/yarnpkg-pnp/sources/loader/applyPatch.ts`) -> Impact: **147.2** | LOC: 312
- `applyVirtualResolutionMutations` **(Many-Argument Workhorses)** (@ `packages/yarnpkg-core/sources/Project.ts`) -> Impact: **139.8** | LOC: 504
  * *Intent:* /** * This function is worth some documentation. It takes a set of packages, * traverses them all, and generates virtual packages for each package tha...
- `resolveToUnqualified` **(Many-Argument Workhorses)** (@ `packages/yarnpkg-pnp/sources/loader/makeApi.ts`) -> Impact: **126.8** | LOC: 257
  * *Intent:* /** * Transforms a request (what's typically passed as argument to the require function) into an unqualified path. * This path is called "unqualified"...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/yarnpkg-core/sources` | 44 | 9431.99 | 44.54% | 7.13% |
| `packages/acceptance-tests/pkg-tests-specs/sources` | 14 | 6834.59 | 14.53% | 0.0% |
| `packages/acceptance-tests/pkg-tests-specs/sources/commands` | 25 | 6520.02 | 26.72% | 0.0% |
| `packages/acceptance-tests/pkg-tests-specs/sources/features` | 35 | 5392.87 | 21.66% | 0.0% |
| `packages/yarnpkg-fslib/sources` | 18 | 4556.24 | 41.77% | 7.56% |
| `packages/yarnpkg-libzip/sources` | 15 | 3238.08 | 30.5% | 9.31% |
| `packages/yarnpkg-fslib/tests` | 8 | 1990.81 | 13.99% | 0.0% |
| `packages/plugin-essentials/sources/commands` | 18 | 1656.22 | 56.59% | 4.96% |
| `packages/yarnpkg-pnp/sources/loader` | 10 | 1650.93 | 35.49% | 22.37% |
| `packages/acceptance-tests/pkg-tests-specs/sources/protocols` | 10 | 1522.09 | 8.2% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug-report.yml` -> **100.0%** Exposure
- `packages/plugin-constraints/sources/tauProlog.d.ts` -> **100.0%** Exposure
- `packages/yarnpkg-fslib/sources/statUtils.ts` -> **100.0%** Exposure
- `packages/yarnpkg-libzip/artifacts/lib/zipstruct.c` -> **99.9999%** Exposure
- `packages/yarnpkg-core/sources/RefCountedCache.ts` -> **99.9447%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/docusaurus/config/webpack/ansi-loader.js` -> **100.0%** Exposure
- `packages/docusaurus/static/js/custom.js` -> **100.0%** Exposure
- `packages/yarnpkg-libzip/sources/libzipSync.js` -> **100.0%** Exposure
- `packages/yarnpkg-pnp/sources/loader/node-options.js` -> **100.0%** Exposure
- `packages/acceptance-tests/pkg-tests-core/sources/utils/exec.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/plugin-constraints/sources/tauProlog.d.ts` -> **19** Orphaned Functions | **45** Duplicates
- `packages/yarnpkg-fslib/sources/statUtils.ts` -> **0** Orphaned Functions | **18** Duplicates
- `packages/yarnpkg-libzip/artifacts/lib/zipstruct.c` -> **8** Orphaned Functions | **0** Duplicates
- `packages/acceptance-tests/pkg-tests-specs/sources/commands/config.test.ts` -> **6** Orphaned Functions | **0** Duplicates
- `packages/yarnpkg-core/tests/TestPlugin.ts` -> **0** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `18` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1517` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/yarnpkg-core/sources/Project.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.768)
- **Top Global Matches:** file_cluster_4: 7.768, file_cluster_6: 8.749, file_cluster_12: 14.796
- **Magnitude:** 1936.1 | **LOC:** 2771 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **38**; blast radius 6.126; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.8%), Connectivity (formerly Api Exposure) (63.8%)
- **Documentation Coverage:** 97.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `linkEverything` **(Compute Cores)** (Impact: 180.4)
  * `applyVirtualResolutionMutations` **(Many-Argument Workhorses)** (Impact: 139.8)
    * *Intent:* /** * This function is worth some documentation. It takes a set of packages, * traverses them all, a...
  * `resolvePeerDependenciesImpl` **(Many-Argument Workhorses)** (Impact: 126.4)
  * `resolveEverything` **(Compute Cores)** (Impact: 64.1)
  * `install` **(Defensive Guards)** (Impact: 64.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 42 instances
* *Amplified Cascading Flux:* 137 instances
* *Concurrency (weighted view):* 356
* *State Mutation (weighted view):* 491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 422`, `structural_boundaries: 403`, `args: 138`, `func_start: 72`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 217`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 44`, `concurrency: 146`, `import: 41`
* *Defense:* `safety: 57`, `doc: 19`, `sync_locks: 2`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.126
  * `Choke Point (Betweenness):` 0.00152 | `Ripple Effect (Closeness):` 0.045048
  * `Imports (Out-Degree: 26):` Cache, Configuration, Fetcher, Installer, LegacyMigrationResolver, Linker, LockfileResolver, Manifest...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `packages/acceptance-tests/pkg-tests-specs/sources/node-modules.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.46)
- **Top Global Matches:** file_cluster_10: 5.46, file_cluster_2: 6.627, file_cluster_13: 6.916
- **Magnitude:** 1673.37 | **LOC:** 2105 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.6%), Complexity Load (formerly Cognitive Load) (23.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 445
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 419`, `args: 82`, `func_start: 64`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 265`, `api: 5`, `concurrency: 400`, `import: 25`
* *Defense:* `safety: 13`, `doc: 6`, `test: 192`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , package.json, core, fslib, package.json, dep, has-bin-entries, symlink...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-fslib/tests/patchedFs.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.62)
- **Top Global Matches:** file_cluster_10: 5.62, file_cluster_2: 8.272, file_cluster_13: 8.411
- **Magnitude:** 1603.1 | **LOC:** 728 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.542; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (43.3%), Guard Balance (formerly Safety Score) (39.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 219
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 235`, `args: 83`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 51`, `concurrency: 194`, `import: 11`
* *Defense:* `safety: 9`, `doc: 1`, `test: 114`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` sources, NodeFS, PosixFS, patchFs, path, xfs, libzip, fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/acceptance-tests/pkg-tests-specs/sources/pnp-esm.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.972)
- **Top Global Matches:** file_cluster_10: 4.972, file_cluster_2: 6.352, file_cluster_13: 6.985
- **Magnitude:** 1531.34 | **LOC:** 1164 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.3%), Complexity Load (formerly Cognitive Load) (26.8%), Mutation Surface (formerly State Flux) (9.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Concurrency (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 361`, `args: 55`, `func_start: 47`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 124`, `api: 14`, `concurrency: 210`, `import: 41`
* *Defense:* `safety: 9`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` #bar, #foo, foo, index.js, $pathToFileURL(npath.fromPortablePath(ppath.join(path, bar.cjs, baz, cjs-bin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/plugin-nm/sources/NodeModulesLinker.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.557)
- **Top Global Matches:** file_cluster_6: 7.557, file_cluster_4: 11.407, file_cluster_8: 15.887
- **Magnitude:** 1461.98 | **LOC:** 1399 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.772; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `persistNodeModules` **(Many-Argument Workhorses)** (Impact: 164.1)
  * `syncPreinstallStateWithDisk` **(Many-Argument Workhorses)** (Impact: 56.1)
    * *Intent:* /** * Synchronizes previous install state with the actual directories available on disk * * */
  * `syncNodeWithDisk` **(Many-Argument Workhorses)** (Impact: 52.5)
  * `createBinSymlinkMap` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `removeDir` **(Defensive Guards)** (Impact: 39.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 102 instances
* *Concurrency (weighted view):* 322
* *State Mutation (weighted view):* 320
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 236`, `args: 64`, `func_start: 50`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 116`
* *Architecture:* `io: 7`, `api: 20`, `concurrency: 137`, `import: 17`
* *Defense:* `safety: 44`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.772
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.000868
  * `Imports (Out-Degree: 2):` core, fslib, libzip, nm, parsers, plugin-pnp, pnp, cmd-shim...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-libzip/sources/ZipFS.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.24)
- **Top Global Matches:** file_cluster_0: 8.24, file_cluster_12: 8.788, file_cluster_15: 9.1
- **Magnitude:** 1416.42 | **LOC:** 1527 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 3.288; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.1%), Complexity Load (formerly Cognitive Load) (91.7%), Guard Balance (formerly Safety Score) (57.3%)
- **Documentation Coverage:** 99.1736% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveFilename` **(Many-Argument Workhorses)** (Impact: 45.1)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `readdirSync` **(Defensive Guards)** (Impact: 37.8)
  * `getFileSource` **(Stateful Encapsulated Methods)** (Impact: 24.2)
  * `statImpl` **(Many-Argument Workhorses)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 149
* *State Mutation (weighted view):* 187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 339`, `structural_boundaries: 196`, `args: 206`, `func_start: 199`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 69`, `duplicate_logic: 4`
* *Architecture:* `io: 21`, `api: 49`, `concurrency: 104`, `import: 15`
* *Defense:* `safety: 18`, `doc: 2`, `immutability_locks: 9`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.288
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.0062
  * `Imports (Out-Degree: 3):` libzipImpl, fslib, fs, stream, util, zlib
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-core/sources/Configuration.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.619)
- **Top Global Matches:** file_cluster_4: 7.619, file_cluster_6: 9.761, file_cluster_12: 12.875
- **Magnitude:** 1243.82 | **LOC:** 2084 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **77** in-repo importer(s); it depends on **32**; blast radius 37.347; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Concurrency Surface (formerly Concurrency) (98.3%), Connectivity (formerly Api Exposure) (74.7%), Guard Balance (formerly Safety Score) (58.5%)
- **Documentation Coverage:** 89.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find` **(Many-Argument Workhorses)** (Impact: 108.2)
    * *Intent:* * * Note that some extra plugins will be automatically added based on the * content of the rc files ...
  * `use` **(Many-Argument Workhorses)** (Impact: 73.4)
  * `parseSingleValue` **(Many-Argument Workhorses)** (Impact: 71.7)
  * `getDefaultValue` **(Compute Cores)** (Impact: 70.5)
  * `normalizePackage` **(Compute Cores)** (Impact: 48.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 82 instances
* *Concurrency (weighted view):* 122
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 438`, `args: 82`, `func_start: 56`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 99`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 48`, `api: 57`, `concurrency: 62`, `import: 33`
* *Defense:* `safety: 37`, `doc: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.347
  * `Choke Point (Betweenness):` 0.003895 | `Ripple Effect (Closeness):` 0.072234
  * `Imports (Out-Degree: 21):` CorePlugin, Manifest, MultiFetcher, MultiResolver, Plugin, Report, TelemetryManager, VirtualFetcher...
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-fslib/sources/MountFS.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.978)
- **Top Global Matches:** file_cluster_0: 8.978, file_cluster_10: 9.808, file_cluster_12: 10.565
- **Magnitude:** 1175.58 | **LOC:** 1143 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.633; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (92.6%), Mutation Surface (formerly State Flux) (88.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `limitOpenFiles` **(Stateful Encapsulated Methods)** (Impact: 28.5)
  * `writePromise` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `writeSync` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `findMount` **(Stateful Encapsulated Methods)** (Impact: 14.6)
  * `makeCallPromise` **(Stateful Encapsulated Methods)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 314
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 516`, `args: 276`, `func_start: 204`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 47`, `planned_debt: 3`
* *Architecture:* `io: 13`, `api: 57`, `concurrency: 254`, `import: 9`
* *Defense:* `safety: 19`, `doc: 3`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003272
  * `Imports (Out-Degree: 5):` FakeFS, NodeFS, watchFile, errors, path, fs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-core/sources/Manifest.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.903)
- **Top Global Matches:** file_cluster_4: 5.903, file_cluster_6: 10.396, file_cluster_12: 11.283
- **Magnitude:** 1142.92 | **LOC:** 1024 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **8**; blast radius 28.562; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.6%), Concurrency Surface (formerly Concurrency) (84.3%), Guard Balance (formerly Safety Score) (76.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Many-Argument Workhorses)** (Impact: 272.7)
  * `exportTo` **(Many-Argument Workhorses)** (Impact: 152.9)
  * `setRawField` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `getForScope` **(Compute Cores)** (Impact: 9.3)
  * `ensureDependencyMeta` **(Compute Cores)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 163 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 141`, `args: 38`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 171`
* *Architecture:* `io: 9`, `api: 44`, `concurrency: 8`, `import: 9`
* *Defense:* `safety: 20`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.562
  * `Choke Point (Betweenness):` 0.00087 | `Ripple Effect (Closeness):` 0.062765
  * `Imports (Out-Degree: 5):` WorkspaceResolver, miscUtils, semverUtils, structUtils, types, fslib, parsers, semver
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-fslib/sources/FakeFS.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.156)
- **Top Global Matches:** file_cluster_0: 8.156, file_cluster_5: 9.349, file_cluster_12: 9.499
- **Magnitude:** 1110.38 | **LOC:** 813 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **6**; blast radius 8.2; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.2%), Connectivity (formerly Api Exposure) (94.7%), Complexity Load (formerly Cognitive Load) (92.3%)
- **Documentation Coverage:** 96.2085% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copySync` **(Many-Argument Workhorses)** (Impact: 33.6)
  * `removePromise` **(Defensive Guards)** (Impact: 24.4)
  * `mkdirpPromise` **(Defensive Guards)** (Impact: 22.7)
  * `mkdirpSync` **(Defensive Guards)** (Impact: 22.7)
  * `lockPromise` **(Defensive Guards)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 253
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 217`, `args: 174`, `func_start: 165`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 31`
* *Architecture:* `io: 11`, `api: 74`, `concurrency: 123`, `import: 9`
* *Defense:* `safety: 42`, `doc: 4`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.2
  * `Choke Point (Betweenness):` 0.000302 | `Ripple Effect (Closeness):` 0.043801
  * `Imports (Out-Degree: 2):` copyPromise, path, crypto, events, fs, os
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-pnp/sources/loader/makeApi.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.022)
- **Top Global Matches:** file_cluster_4: 7.022, file_cluster_6: 9.377, file_cluster_12: 13.154
- **Magnitude:** 922.14 | **LOC:** 1028 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 1.033; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%), Complexity Load (formerly Cognitive Load) (55.1%)
- **Documentation Coverage:** 52.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeApi` **(Many-Argument Workhorses)** (Impact: 372.5)
  * `resolveToUnqualified` **(Many-Argument Workhorses)** (Impact: 126.8)
    * *Intent:* /** * Transforms a request (what's typically passed as argument to the require function) into an unq...
  * `applyNodeExtensionResolution` **(Many-Argument Workhorses)** (Impact: 35.2)
    * *Intent:* /** * Implements the node resolution for folder access and extension selection */
  * `resolveUnqualified` **(Defensive Guards)** (Impact: 23.2)
    * *Intent:* /** * Transforms an unqualified path into a qualified path by using the Node resolution algorithm (w...
  * `findPackageLocator` **(Compute Cores)** (Impact: 22.0)
    * *Intent:* /** * Finds the package locator that owns the specified path. If none is found, returns null instead...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 114`, `args: 41`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 48`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 16`, `api: 4`, `import: 10`
* *Defense:* `safety: 38`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.033
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.003125
  * `Imports (Out-Degree: 5):` resolve.js, types, internalTools, node-options.js, nodeUtils, fslib, module, url...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/acceptance-tests/pkg-tests-specs/sources/features/prunedNativeDeps.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.767)
- **Top Global Matches:** file_cluster_10: 4.767, file_cluster_13: 6.689, file_cluster_2: 6.781
- **Magnitude:** 919.85 | **LOC:** 375 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (52.9%), Guard Balance (formerly Safety Score) (49.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 131
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 109`, `args: 29`, `func_start: 10`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 33`, `api: 1`, `concurrency: 61`, `import: 3`
* *Defense:* `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fslib, parsers, pkg-tests-core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-shell/sources/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.857)
- **Top Global Matches:** file_cluster_4: 6.857, file_cluster_6: 11.182, file_cluster_15: 11.78
- **Magnitude:** 884.58 | **LOC:** 1090 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 3.015; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (91.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluateVariable` **(Many-Argument Workhorses)** (Impact: 95.4)
  * `interpolateArguments` **(Many-Argument Workhorses)** (Impact: 55.7)
  * `executeCommandChainImpl` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `executeCommandLine` **(Many-Argument Workhorses)** (Impact: 29.7)
    * *Intent:* /** * Execute a command line. A command line is a list of command shells linked * together thanks to...
  * `getFileDescriptorStream` **(Compute Cores)** (Impact: 27.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 62 instances
* *Concurrency (weighted view):* 196
* *State Mutation (weighted view):* 204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 262`, `args: 81`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 80`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 71`, `import: 12`
* *Defense:* `safety: 8`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.015
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.002604
  * `Imports (Out-Degree: 4):` entry, errors, globUtils, pipe, fslib, parsers, chalk, os...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/acceptance-tests/pkg-tests-specs/sources/commands/pack.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.553)
- **Top Global Matches:** file_cluster_10: 6.553, file_cluster_12: 8.51, file_cluster_15: 8.516
- **Magnitude:** 860.44 | **LOC:** 910 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.6%), Mutation Surface (formerly State Flux) (40.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genPackList` **(Callbacks & Closures)** (Impact: 1.8)
  * `onentry` **(Parameter Forwarders)** (Impact: 1.5)
  * `onentry` **(Parameter Forwarders)** (Impact: 1.5)
  * `onentry` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 95 instances
* *Concurrency (weighted view):* 731
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 267`, `args: 56`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 38`, `planned_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 70`, `concurrency: 256`, `import: 3`
* *Defense:* `test: 141`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fslib, pkg-tests-core, tar
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-pnpify/sources/NodeModulesFS.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.841)
- **Top Global Matches:** file_cluster_0: 7.841, file_cluster_5: 8.482, file_cluster_12: 8.959
- **Magnitude:** 800.12 | **LOC:** 649 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 0.903; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (86.6%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readdirPromise` **(Defensive Guards)** (Impact: 18.6)
  * `readdirSync` **(Defensive Guards)** (Impact: 18.6)
  * `watch` **(Compute Cores)** (Impact: 16.8)
  * `writePromise` **(Compute Cores)** (Impact: 15.0)
  * `writeSync` **(Compute Cores)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 129
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 176`, `args: 158`, `func_start: 151`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 20`, `duplicate_logic: 2`
* *Architecture:* `io: 16`, `api: 65`, `concurrency: 114`, `import: 14`
* *Defense:* `safety: 14`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.903
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001736
  * `Imports (Out-Degree: 3):` WatchManager, dynamicRequire, resolveNodeModulesPath, fslib, nm, pnp, fs
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/acceptance-tests/pkg-tests-specs/sources/commands/workspaces/foreach.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.015)
- **Top Global Matches:** file_cluster_10: 7.015, file_cluster_12: 7.704, file_cluster_15: 8.301
- **Magnitude:** 780.38 | **LOC:** 973 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (84.5%), Guard Balance (formerly Safety Score) (52.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setupWorkspaces` **(I/O & Config Routines)** (Impact: 5.7)
  * `getClientContent` **(Parameter Forwarders)** (Impact: 3.4)
  * `extractWorkspaces` **(Callbacks & Closures)** (Impact: 3.0)
  * `makeWorkspacesForeachSinceEnv` **(Callbacks & Closures)** (Impact: 2.6)
  * `git` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 101 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 659
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 163`, `args: 44`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 82`, `planned_debt: 3`
* *Architecture:* `io: 10`, `concurrency: 154`, `import: 6`
* *Defense:* `safety: 7`, `test: 62`, `sync_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` package.json, fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-fslib/sources/NodeFS.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.431)
- **Top Global Matches:** file_cluster_5: 8.431, file_cluster_12: 10.047, file_cluster_0: 11.003
- **Magnitude:** 747.56 | **LOC:** 606 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **3**; blast radius 2.241; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (88.9%), Complexity Load (formerly Cognitive Load) (86.9%), Guard Balance (formerly Safety Score) (55.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readdirPromise` **(Generic / Templated Code)** (Impact: 16.4)
  * `readdirSync` **(Type Conversions)** (Impact: 16.3)
  * `writePromise` **(Compute Cores)** (Impact: 15.1)
  * `writeSync` **(Compute Cores)** (Impact: 15.0)
  * `appendFilePromise` **(Generic / Templated Code)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 194`, `args: 172`, `func_start: 133`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 2`, `planned_debt: 2`
* *Architecture:* `io: 20`, `api: 59`, `concurrency: 147`, `import: 6`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.241
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.035637
  * `Imports (Out-Degree: 2):` FakeFS, path, fs
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `packages/acceptance-tests/pkg-tests-specs/sources/script.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.938)
- **Top Global Matches:** file_cluster_10: 4.938, file_cluster_2: 6.509, file_cluster_13: 6.892
- **Magnitude:** 710.32 | **LOC:** 687 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.7%), Complexity Load (formerly Cognitive Load) (45.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 248
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 151`, `args: 34`, `func_start: 32`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 12`
* *Architecture:* `io: 92`, `api: 8`, `concurrency: 133`, `import: 17`
* *Defense:* `safety: 4`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` log, fslib, child_process, fs, no-deps-scripted-to-deeply-fail, no-deps-scripted-to-fail, log, log.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-libzip/sources/libzipAsync.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.235)
- **Top Global Matches:** file_cluster_12: 7.235, file_cluster_15: 7.588, file_cluster_10: 8.051
- **Magnitude:** 697.76 | **LOC:** 987 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stringToUTF8Array` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `ccall` **(Defensive Guards)** (Impact: 31.4)
  * `getValue` **(Compute Cores)** (Impact: 25.1)
  * `lengthBytesUTF8` **(Compute Cores)** (Impact: 14.8)
  * `run` **(Compute Cores)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 98 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 295`, `args: 126`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 127`, `unreferenced_by_name: 3`
* *Architecture:* `io: 7`, `api: 1`, `concurrency: 13`, `import: 3`
* *Defense:* `safety: 59`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-shell/tests/shell.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.366)
- **Top Global Matches:** file_cluster_10: 6.366, file_cluster_0: 9.219, file_cluster_13: 9.489
- **Magnitude:** 694.46 | **LOC:** 2119 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.542; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.2%), Complexity Load (formerly Cognitive Load) (38.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bufferResult` **(Generic / Templated Code)** (Impact: 7.0)
  * `[                ]` **(Callbacks & Closures)** (Impact: 4.4)
  * `getNumbers` **(Generic / Templated Code)** (Impact: 3.2)
  * `[              ]` **(Callbacks & Closures)** (Impact: 2.8)
  * `[            ]` **(Callbacks & Closures)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 625
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 607`, `args: 236`, `func_start: 138`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 8`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `concurrency: 550`, `import: 5`
* *Defense:* `safety: 7`, `test: 217`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fslib, shell, stream, strip-ansi, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/acceptance-tests/pkg-tests-specs/sources/features/cache.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.002)
- **Top Global Matches:** file_cluster_7: 7.002, file_cluster_12: 7.02, file_cluster_10: 8.841
- **Magnitude:** 689.29 | **LOC:** 449 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Guard Balance (formerly Safety Score) (49.3%), Mutation Surface (formerly State Flux) (17.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Concurrency (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 110`, `args: 29`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`
* *Architecture:* `io: 51`, `concurrency: 93`, `import: 3`
* *Defense:* `safety: 8`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core, fslib, pkg-tests-core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/acceptance-tests/pkg-tests-specs/sources/pnp.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.955)
- **Top Global Matches:** file_cluster_10: 6.955, file_cluster_15: 7.737, file_cluster_12: 7.906
- **Magnitude:** 686.3 | **LOC:** 2286 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **46**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.6%), Complexity Load (formerly Cognitive Load) (34.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter` **(Parameter Forwarders)** (Impact: 1.5)
  * `filter` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Concurrency (weighted view):* 603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 498`, `args: 121`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 13`, `duplicate_logic: 2`
* *Architecture:* `io: 27`, `api: 29`, `concurrency: 473`, `import: 123`
* *Defense:* `safety: 30`, `doc: 4`, `test: 212`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` #foo, exist.cjs, index.js, a.js, b.js, doesntwork, fileb, foo.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/acceptance-tests/pkg-tests-core/sources/utils/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.827)
- **Top Global Matches:** file_cluster_12: 7.827, file_cluster_5: 8.399, file_cluster_10: 10.489
- **Magnitude:** 681.9 | **LOC:** 1159 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **22**; blast radius 1.382; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `[RequestType.PackageInfo]` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `[RequestType.Publish]` **(Defensive Guards)** (Impact: 22.1)
  * `[RequestType.PackageVersion]` **(Stateful Encapsulated Methods)** (Impact: 21.9)
  * `listener` **(Defensive Guards)** (Impact: 17.4)
  * `[RequestType.BulkAdvisories]` **(Defensive Guards)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 213
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 323`, `args: 88`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 44`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 57`, `api: 38`, `concurrency: 98`, `import: 27`
* *Defense:* `safety: 28`, `test: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.382
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002604
  * `Imports (Out-Degree: 2):` exec, fs, core, fslib, plugin-npm-cli, assert, crypto, finalhandler...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-libzip/sources/libzipSync.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.247)
- **Top Global Matches:** file_cluster_12: 6.247, file_cluster_15: 7.003, file_cluster_10: 8.476
- **Magnitude:** 671.36 | **LOC:** 772 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.651; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%), Guard Balance (formerly Safety Score) (65.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stringToUTF8Array` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `ccall` **(Defensive Guards)** (Impact: 31.4)
  * `getValue` **(Compute Cores)** (Impact: 25.1)
  * `lengthBytesUTF8` **(Compute Cores)** (Impact: 14.8)
  * `run` **(Compute Cores)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 98 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 326
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 239`, `args: 67`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 130`
* *Architecture:* `io: 3`, `api: 4`, `concurrency: 3`, `import: 3`
* *Defense:* `safety: 53`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001157
  * `Imports (Out-Degree: 0):` fs, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/acceptance-tests/pkg-tests-specs/sources/commands/add.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.438)
- **Top Global Matches:** file_cluster_10: 5.438, file_cluster_13: 7.13, file_cluster_2: 7.318
- **Magnitude:** 658.7 | **LOC:** 641 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.542; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (42.9%), Mutation Surface (formerly State Flux) (17.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Concurrency (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 160`, `args: 48`, `func_start: 37`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 91`, `concurrency: 142`, `import: 3`
* *Defense:* `safety: 4`, `test: 82`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fslib, parsers, pkg-tests-core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/plugin-npm/sources/NpmTagResolver.ts` (TYPESCRIPT) | Magnitude: 80.4 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 30, branch: 20, core_var_decl: 13
- `packages/yarnpkg-fslib/tests/ProxiedFS.test.ts` (TYPESCRIPT) | Magnitude: 19.36 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 16, core_var_decl: 12, design_camel_case: 12
- `packages/yarnpkg-pnpify/sources/commands/SdkCommand.ts` (TYPESCRIPT) | Magnitude: 16.3 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, state_mutation: 3, api: 2
- `packages/docusaurus/config/docusaurus/plugins/cli-docs.ts` (TYPESCRIPT) | Magnitude: 131.84 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 311, structural_boundaries: 78, args: 36, core_var_decl: 30
- `packages/docusaurus/src/components/HomepageFeatures/index.tsx` (TYPESCRIPT) | Magnitude: 10.62 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 9, core_var_decl: 9, ui_framework: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/yarnpkg-fslib/sources/statUtils.ts` (TYPESCRIPT) | Magnitude: 173.52 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 190, structural_boundaries: 68, state_mutation: 49, core_var_decl: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/yarnpkg-pnp/sources/loader/internalTools.ts` (TYPESCRIPT) | Magnitude: 31.74 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 41, core_var_decl: 13, design_upper_case: 10, structural_boundaries: 9
- `packages/plugin-essentials/sources/commands/entries/clipanion.ts` (TYPESCRIPT) | Magnitude: 19.44 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 10, core_var_decl: 7, branch: 5
- `packages/yarnpkg-core/sources/StreamReport.ts` (TYPESCRIPT) | Magnitude: 551.16 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 517, branch: 153, structural_boundaries: 106, core_var_decl: 99
- `packages/yarnpkg-core/tests/tgzUtils.test.ts` (TYPESCRIPT) | Magnitude: 50.65 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 14, concurrency: 9, test: 8
- `packages/yarnpkg-core/sources/LegacyMigrationResolver.ts` (TYPESCRIPT) | Magnitude: 75.78 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 91, branch: 45, structural_boundaries: 41, bitwise_ops: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/yarnpkg-builder/sources/boot-cli-dev.js` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 2, decorators: 1
- `packages/yarnpkg-pnp/sources/esm-loader/built-loader.d.ts` (TYPESCRIPT) | Magnitude: 0.11 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, args: 1, func_start: 1
- `packages/acceptance-tests/pkg-tests-specs/sources/commands/why.test.ts` (TYPESCRIPT) | Magnitude: 152.0 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 182, structural_boundaries: 34, decorators: 32, io: 26
- `packages/vscode-zipfs/rollup.config.js` (JAVASCRIPT) | Magnitude: 18.74 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 11, import: 8, branch: 3
- `packages/plugin-essentials/sources/index.ts` (TYPESCRIPT) | Magnitude: 63.44 | Delta: **0.189** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 103, indent_spaces: 84, import: 42, api: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `scripts/detect-unsafe-writes.ts` (TYPESCRIPT) | Magnitude: 15.82 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, io: 5, concurrency: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/plugin-http/sources/urlUtils.ts` (TYPESCRIPT) | Magnitude: 10.76 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 5, branch: 3, safety: 2
- `packages/yarnpkg-fslib/sources/errors.ts` (TYPESCRIPT) | Magnitude: 33.68 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 25, args: 13, func_start: 13, indent_spaces: 13
- `packages/yarnpkg-core/sources/structUtils.ts` (TYPESCRIPT) | Magnitude: 353.58 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 300, structural_boundaries: 173, branch: 135, args: 60
- `packages/yarnpkg-core/sources/WorkspaceResolver.ts` (TYPESCRIPT) | Magnitude: 37.9 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 22, args: 9, func_start: 8
- `packages/docusaurus/config/typedoc/plugin.ts` (TYPESCRIPT) | Magnitude: 27.02 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 9, branch: 6, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/yarnpkg-core/sources/index.ts` (TYPESCRIPT) | Magnitude: 61.14 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 69, api: 45, import: 45
- `packages/yarnpkg-fslib/sources/index.ts` (TYPESCRIPT) | Magnitude: 60.96 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 71, api: 45, import: 45, io: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/plugin-npm/sources/index.ts` (TYPESCRIPT) | Magnitude: 28.74 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 41, branch: 11, api: 10
- `packages/yarnpkg-cli/sources/boot-cli-dev.js` (JAVASCRIPT) | Magnitude: 13.64 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 5, io: 3, decorators: 2, core_var_decl: 2
- `packages/yarnpkg-libui/sources/libuiUtils.ts` (TYPESCRIPT) | Magnitude: 5.8 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, import: 3, branch: 2
- `packages/acceptance-tests/pkg-tests-core/sources/index.ts` (TYPESCRIPT) | Magnitude: 15.16 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 8, import: 5, io: 3, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/plugin-constraints/sources/Constraints.ts` (TYPESCRIPT) | Magnitude: 184.54 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 237, structural_boundaries: 69, branch: 53, core_var_decl: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/yarnpkg-core/sources/formatUtils.ts` (TYPESCRIPT) | Magnitude: 207.72 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 431, structural_boundaries: 190, args: 64, core_var_decl: 59
- `packages/yarnpkg-pnpify/sources/WatchManager.ts` (TYPESCRIPT) | Magnitude: 55.68 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 13, state_mutation: 12, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/acceptance-tests/pkg-tests-specs/sources/features/cache.test.ts` (TYPESCRIPT) | Magnitude: 689.29 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 339, structural_boundaries: 110, concurrency: 93, io: 51
- `packages/plugin-stage/sources/stageUtils.ts` (TYPESCRIPT) | Magnitude: 139.14 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 31, branch: 30, core_var_decl: 22
- `packages/acceptance-tests/pkg-tests-core/sources/utils/yarn.ts` (TYPESCRIPT) | Magnitude: 81.16 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 20, concurrency: 11, indent_spaces: 8, branch: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/plugin-essentials/sources/commands/install.ts` -> Churn: **71.24%** | Cog Load: 97.5055% | Debt: 89.3524%
- `packages/acceptance-tests/pkg-tests-specs/sources/commands/install.test.ts` -> Churn: **56.46%** | Cog Load: 100.0% | Debt: 0.0%
- `packages/plugin-git/sources/gitUtils.ts` -> Churn: **56.46%** | Cog Load: 71.5038% | Debt: 0.0%
- `packages/plugin-npm/sources/npmHttpUtils.ts` -> Churn: **56.46%** | Cog Load: 88.498% | Debt: 18.9727%
- `packages/yarnpkg-core/sources/Configuration.ts` -> Churn: **56.46%** | Cog Load: 53.634% | Debt: 8.7674%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/yarnpkg-core/sources/Project.ts` -> **Maël Nison** (100.0% isolated ownership) | Magnitude: 1936.1
- `packages/acceptance-tests/pkg-tests-specs/sources/node-modules.test.ts` -> **Maël Nison** (100.0% isolated ownership) | Magnitude: 1673.37
- `packages/yarnpkg-fslib/tests/patchedFs.test.ts` -> **Clement Yan** (100.0% isolated ownership) | Magnitude: 1603.1
- `packages/yarnpkg-pnp/sources/loader/makeApi.ts` -> **Clement Yan** (100.0% isolated ownership) | Magnitude: 922.14
- `packages/acceptance-tests/pkg-tests-specs/sources/commands/pack.test.js` -> **Marc Hassan** (100.0% isolated ownership) | Magnitude: 860.44

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/yarnpkg-core/sources/Configuration.ts` -> **Severity: 0.384** (Bridge: 0.0039 * Flux: 98.552%)
- `packages/yarnpkg-core/sources/Project.ts` -> **Severity: 0.152** (Bridge: 0.0015 * Flux: 99.9537%)
- `packages/yarnpkg-core/sources/Manifest.ts` -> **Severity: 0.087** (Bridge: 0.0009 * Flux: 100.0%)
- `packages/yarnpkg-core/sources/Cache.ts` -> **Severity: 0.051** (Bridge: 0.0007 * Flux: 74.3216%)
- `packages/yarnpkg-core/sources/structUtils.ts` -> **Severity: 0.045** (Bridge: 0.001 * Flux: 44.0819%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/yarnpkg-core/sources/Manifest.ts` -> **Severity: 4.8** (Embedded: 0.0628 * Error Risk: 76.4689%)
- `packages/yarnpkg-core/sources/Configuration.ts` -> **Severity: 4.229** (Embedded: 0.0722 * Error Risk: 58.5454%)
- `packages/yarnpkg-core/sources/miscUtils.ts` -> **Severity: 3.733** (Embedded: 0.0588 * Error Risk: 63.4615%)
- `packages/yarnpkg-core/sources/semverUtils.ts` -> **Severity: 3.411** (Embedded: 0.0579 * Error Risk: 58.9289%)
- `packages/yarnpkg-core/sources/Report.ts` -> **Severity: 3.346** (Embedded: 0.0564 * Error Risk: 59.3196%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/yarnpkg-core/sources/Configuration.ts` -> **Severity: 3336.331** (Blast Radius: 37.347 * Doc Risk: 89.3333%)
- `packages/yarnpkg-core/sources/Manifest.ts` -> **Severity: 2856.2** (Blast Radius: 28.562 * Doc Risk: 100.0%)
- `packages/yarnpkg-fslib/sources/path.ts` -> **Severity: 1229.4** (Blast Radius: 12.294 * Doc Risk: 100.0%)
- `packages/yarnpkg-core/sources/Report.ts` -> **Severity: 1070.8** (Blast Radius: 10.708 * Doc Risk: 100.0%)
- `packages/yarnpkg-core/sources/MessageName.ts` -> **Severity: 1049.7** (Blast Radius: 10.497 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 339 literal sites + 1 sites through wrappers = 340
- **`panics_and_aborts`:** 1111 literal sites + 1 sites through wrappers = 1112

- `makeCommandOrRawLine` (function, debug_prints, primitive): 1 call sites in 1 files -- `packages/docusaurus/config/remark/commandLineHighlight.ts`
- `registeredFactory` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/yarnpkg-libzip/sources/instance.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 9902 call pairs -- scoped 24.3%, unique 0.0%, ambiguous 22.2%, external 53.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 8963 | 24.2% | 0.0% | 23.4% | 52.4% |
| javascript | 788 | 26.9% | 0.0% | 12.9% | 60.2% |
| shell | 120 | 13.3% | 0.0% | 0.0% | 86.7% |
| perl | 27 | 22.2% | 0.0% | 0.0% | 77.8% |
| c | 3 | 0.0% | 0.0% | 0.0% | 100.0% |
| powershell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
