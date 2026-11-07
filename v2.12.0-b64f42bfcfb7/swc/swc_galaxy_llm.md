# ARCHITECTURAL_BRIEF: swc
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/swc-project/swc.git` |
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
- **Scope:** 58032 analyzed artifact(s), 4648876 LOC.
- **Load-bearing artifact:** `crates/swc_common/src/syntax_pos.rs` -- 616 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `crates/swc_ecma_parser/benches/files/cal.com.tsx` -- pulls in 528 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `crates/swc_ecma_minifier/benches/full/echarts.js` at magnitude 81021.62 (structural weight, not risk).
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
| Total Artifacts | 82586 |
| Analyzed Artifacts (Scanned) | 58032 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 24554 |
| Total LOC | 4648876 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6468 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0594 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8383 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 359 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 28569 | 1569692 | 49.2% |
| JSON | 19428 | 1969920 | 33.5% |
| TYPESCRIPT | 6727 | 256137 | 11.6% |
| RUST | 1340 | 697857 | 2.3% |
| CSS | 1337 | 151530 | 2.3% |
| PLAINTEXT | 217 | 2 | 0.4% |
| MARKDOWN | 137 | 0 | 0.2% |
| XML | 111 | 52 | 0.2% |
| SHELL | 90 | 917 | 0.2% |
| BMS | 48 | 674 | 0.1% |
| YAML | 25 | 2007 | 0.0% |
| PYTHON | 3 | 88 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 57563 |
| utf-8 | bom | 468 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 70%, Declarative / Non-Code 8%, State Mutators Files 6%, Callbacks & Closures Files 5%, Interface Declarations Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 57663 | 99.4% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 353 | 0.6% |
| Static: Minified & Vendor Opaque Mass | 15 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 24554*

**Composition by Extension & Reason:**
- `.js`: 5008x Excluded: Neighborhood Micro-Mass Limit Exceeded, 478x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 18x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.rust-debug`: 3966x Excluded (Unsupported Extension: '.rust-debug')
- `.ts`: 2706x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 533x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.swc-stderr`: 2859x Excluded (Unsupported Extension: '.swc-stderr'), 358x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.html`: 2676x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1147x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 145x Excluded: Neighborhood Micro-Mass Limit Exceeded, 7x Excluded (Static Asset Blob without Intent: 1155 LOC)
- `.stderr`: 1920x Excluded (Unsupported Extension: '.stderr')
- `.css`: 538x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 41x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 98 exceeds 500 chars)
- `.debug`: 230x Excluded (Unsupported Extension: '.debug'), 5x Unsupported Format (.debug)
- `.toml`: 149x Unsupported Format (.toml), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Unsupported Extension: '.toml')
- `.stdout`: 102x Excluded (Unsupported Extension: '.stdout'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable)
- `.mjs`: 75x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 39 exceeds 500 chars)
- `.snap`: 61x Excluded (Unsupported Extension: '.snap')
- `.map`: 15x Excluded (Saturation: Line 1 exceeds 500 chars), 10x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 11 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.0 | 12.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 0.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.7 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 31.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 68.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7079 | 1163 | 0 | `crates/swc_css_visit/src/generated.rs` |
| cleanup | 1723 | 185 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/syncfusion/933-e9f9a6bf671b96fc/input.js` |
| guards | 130229 | 6439 | 1 | `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/input.js` |
| danger | 62248 | 5699 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/output.js` |
| concurrency | 21272 | 2558 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` |
| connectivity | 47943 | 9083 | 1 | `crates/swc_ecma_parser/benches/files/cal.com.tsx` |
| io | 3785 | 589 | 0 | `crates/swc_bundler/tests/fixture/deno-9591/output/entry.inlined.ts` |
| crypto | 5 | 5 | 0 | `crates/swc_ecma_parser/tests/typescript/next/stack-overflow/1/input.ts` |
| ipc | 219 | 48 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/33265/static/chunks/d6e1aeb5-38a8d7ae57119c23/input.js` |
| time | 2915 | 373 | 0 | `crates/swc_ecma_minifier/benches/full/antd.js` |
| serialization | 961 | 290 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/input.js` |
| regex | 5337 | 348 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/syncfusion/933-e9f9a6bf671b96fc/input.js` |
| events | 10528 | 448 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/33265/static/chunks/d6e1aeb5-38a8d7ae57119c23/input.js` |
| tests | 12290 | 1792 | 0 | `crates/swc_ecma_minifier/tests/exec.rs` |
| docs | 61915 | 2155 | 0 | `crates/swc_ecma_minifier/benches/full/antd.js` |
| debt | 33360 | 9123 | 1 | `crates/swc_css_visit/src/generated.rs` |
| mutation | 609679 | 21771 | 5 | `crates/swc_ecma_minifier/benches/full/antd.js` |
| dead_code | 24180 | 8414 | 1 | `crates/swc_ecma_minifier/benches/full/echarts.js` |
| credential | 73 | 30 | 0 | `crates/swc_ecma_minifier/benches/full/victory.js` |
| threat | 234 | 72 | 0 | `crates/hstr/src/wtf8/mod.rs` |
| ml_ai | 1229 | 194 | 0 | `crates/swc_ecma_parser/benches/files/three-0.138.3.js` |
| ui | 38393 | 829 | 0 | `crates/swc_ecma_visit/src/generated.rs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/swc_bundler/tests/fixture/deno-9591/output/entry.inlined.ts` (Hits: 278)
- `crates/swc_bundler/tests/fixture/deno-9591/output/entry.ts` (Hits: 278)
- `crates/swc_bundler/tests/fixture/deno-9620/case1/output/entry.inlined.ts` (Hits: 207)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **syntax_pos.rs** (`crates/swc_common/src/syntax_pos.rs`) — 616 inbound connections
2. **lib.rs** (`crates/swc_ecma_ast/src/lib.rs`) — 464 inbound connections
3. **lib.rs** (`crates/swc_atoms/src/lib.rs`) — 267 inbound connections
4. **generated.rs** (`crates/swc_ecma_visit/src/generated.rs`) — 228 inbound connections
5. **lib.rs** (`crates/swc_ecma_visit/src/lib.rs`) — 167 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cal.com.tsx** (`crates/swc_ecma_parser/benches/files/cal.com.tsx`) — 528 outbound dependencies
2. **cal.com.tsx** (`crates/swc_es_parser/benches/files/cal.com.tsx`) — 528 outbound dependencies
3. **lib.rs** (`crates/swc_ecma_ast/src/lib.rs`) — 458 outbound dependencies
4. **lib.rs** (`crates/swc_es_ast/src/lib.rs`) — 162 outbound dependencies
5. **typescript.rs** (`crates/swc_estree_compat/src/babelify/typescript.rs`) — 158 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `flushPendingUnsafeLifecycleWarnings` **(Defensive Guards)** (@ `crates/swc_ecma_minifier/tests/projects/output/react-dom-17.0.2.js`) -> Impact: **2848.8** | LOC: 6617
- `$$$reconciler` **(Defensive Guards)** (@ `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/input.js`) -> Impact: **2710.5** | LOC: 5392
  * *Intent:* * react-reconciler.production.min.js * * Copyright (c) Facebook, Inc. and its affiliates. * * This source code is licensed under the MIT license found...
- `r1` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/output.js`) -> Impact: **2665.7** | LOC: 1727
- `process_token` **(Many-Argument Workhorses)** (@ `crates/swc_html_parser/src/parser/mod.rs`) -> Impact: **1646.2** | LOC: 5605
- `parse` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_minifier/tests/benches-full/terser.js`) -> Impact: **1373.1** | LOC: 1619
- `parse` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_minifier/benches/full/terser.js`) -> Impact: **1167.2** | LOC: 2421
  * *Intent:* /* -----[ Parser ]----- */
- `WebGLTextures` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_parser/benches/files/three-0.138.3.js`) -> Impact: **1105.1** | LOC: 1228
- `WebGLTextures` **(Many-Argument Workhorses)** (@ `crates/swc_es_parser/benches/files/three-0.138.3.js`) -> Impact: **1105.1** | LOC: 1228
- `Yd` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_minifier/tests/fixture/next/asmjs/1/input.js`) -> Impact: **1055.1** | LOC: 1402
- `Yd` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_minifier/tests/fixture/next/asmjs/1/output.js`) -> Impact: **1027.5** | LOC: 850

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `crates/swc_ecma_minifier/benches/full` | 10 | 274605.47 | 66.0% | 31.53% |
| `crates/swc_ecma_parser/tests/tsc` | 7344 | 131617.13 | 1.08% | 0.0% |
| `crates/swc_ecma_minifier/tests/benches-full` | 9 | 130976.02 | 32.41% | 0.0% |
| `crates/swc/tests/tsc-references` | 8643 | 123328.28 | 2.82% | 0.0% |
| `crates/swc_es_parser/tests/snapshots/ecma_reuse/tsc` | 4290 | 70426.22 | 0.0% | 0.0% |
| `crates/swc_ecma_parser/benches/files` | 8 | 64280.22 | 64.88% | 46.76% |
| `crates/swc_es_parser/benches/files` | 8 | 64280.22 | 64.88% | 46.76% |
| `crates/swc_ecma_minifier/tests/projects/files` | 8 | 46143.5 | 71.07% | 0.0% |
| `crates/swc_css_visit/src` | 2 | 38774.22 | 2.12% | 49.04% |
| `crates/swc_ecma_minifier/tests/projects/output` | 7 | 32826.16 | 77.93% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/minifier/src/binding.d.ts` -> **100.0%** Exposure
- `crates/swc_allocator/src/allocators/scoped.rs` -> **100.0%** Exposure
- `crates/swc_common/src/pos.rs` -> **100.0%** Exposure
- `crates/swc_ecma_ast/src/source_map.rs` -> **100.0%** Exposure
- `crates/swc_ecma_codegen/src/text_writer.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `crates/swc/tests/fixture/next.js/shared/lib/router/1/output/index.ts` -> **100.0%** Exposure
- `crates/swc_ecma_transforms_module/tests/fixture/common/issue-5042/2/output.umd.ts` -> **100.0%** Exposure
- `crates/swc_bundler/src/bundler/helpers/_require.js` -> **100.0%** Exposure
- `crates/swc_ecma_minifier/benches/full/d3.js` -> **100.0%** Exposure
- `crates/swc_ecma_minifier/benches/full/echarts.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/swc_css_visit/src/generated.rs` -> **0** Orphaned Functions | **2935** Duplicates
- `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` -> **142** Orphaned Functions | **621** Duplicates
- `crates/swc_ecma_minifier/benches/full/victory.js` -> **24** Orphaned Functions | **668** Duplicates
- `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/input.js` -> **0** Orphaned Functions | **613** Duplicates
- `crates/swc_ecma_regexp_visit/src/generated.rs` -> **0** Orphaned Functions | **476** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `crates/swc/tests/fixture/ecosystem-ci/1/input/1.ts` -> **67.9689%** Exposure
- `crates/swc/tests/fixture/ecosystem-ci/1/output/1.ts` -> **67.9689%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `25947` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `crates/swc_ecma_minifier/benches/full/echarts.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 16.579)
- **Top Global Matches:** file_cluster_4: 16.579, file_cluster_12: 18.658, file_cluster_15: 19.583
- **Magnitude:** 81021.62 | **LOC:** 91563 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.016; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.4%)
- **Documentation Coverage:** 79.9235% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ECharts` **(Many-Argument Workhorses)** (Impact: 540.7)
  * `List` **(I/O & Config Routines)** (Impact: 381.7)
  * `internalField` **(I/O & Config Routines)** (Impact: 242.6)
    * *Intent:* // need to strictly hide private methods to JS users.
  * `LineView` **(Compute Cores)** (Impact: 218.3)
  * `TooltipView` **(Compute Cores)** (Impact: 215.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 9058 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 118
* *State Mutation (weighted view):* 31139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14588`, `structural_boundaries: 18401`, `args: 6057`, `func_start: 4883`
* *Risk/State:* `safety_bypasses: 1029`, `high_risk_execution: 15`, `state_mutation: 13023`, `dead_code: 307`, `planned_debt: 176`, `fragile_debt: 203`, `duplicate_logic: 149`, `unreferenced_by_name: 82`
* *Architecture:* `io: 11`, `api: 58`, `concurrency: 28`, `import: 3`
* *Defense:* `safety: 2875`, `doc: 1161`, `immutability_locks: 12`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` option, component, XxxModel, charts, components
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/antd.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.796)
- **Top Global Matches:** file_cluster_4: 11.796, file_cluster_12: 12.84, file_cluster_15: 14.057
- **Magnitude:** 55757.22 | **LOC:** 129144 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.016; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.4%), Guard Balance (formerly Safety Score) (56.1%)
- **Documentation Coverage:** 87.741% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Select` **(Many-Argument Workhorses)** (Impact: 348.7)
  * `InnerRangePicker` **(Defensive Guards)** (Impact: 333.2)
  * `Tree` **(Many-Argument Workhorses)** (Impact: 327.3)
    * *Intent:* // TODO: https://www.w3.org/TR/2017/NOTE-wai-aria-practices-1.1-20171214/examples/treeview/treeview-...
  * `generateSelector` **(Defensive Guards)** (Impact: 293.3)
    * *Intent:* /** * This function is in internal usage. * Do not use it in your prod env since we may refactor thi...
  * `InnerSlider` **(Compute Cores)** (Impact: 289.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 111 instances
* *Amplified Cascading Flux:* 4416 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 742
* *State Mutation (weighted view):* 17571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11705`, `structural_boundaries: 25981`, `args: 9138`, `func_start: 6526`
* *Risk/State:* `safety_bypasses: 1219`, `high_risk_execution: 5`, `state_mutation: 8739`, `dead_code: 16`, `planned_debt: 11`, `fragile_debt: 29`, `duplicate_logic: 227`
* *Architecture:* `io: 2`, `api: 264`, `concurrency: 187`, `import: 7`
* *Defense:* `safety: 4712`, `doc: 8268`, `sync_locks: 8`, `cleanup: 100`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment, react, react-dom, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/echarts.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 16.439)
- **Top Global Matches:** file_cluster_4: 16.439, file_cluster_12: 17.813, file_cluster_5: 19.394
- **Magnitude:** 52057.28 | **LOC:** 48464 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.016; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.4%), Complexity Load (formerly Cognitive Load) (36.8%), Concurrency Surface (formerly Concurrency) (13.3%), Dead Code Surface (formerly Dead Code) (6.9%)
- **Documentation Coverage:** 59.4857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ECharts` **(Defensive Guards)** (Impact: 494.0)
  * `containPath` **(Many-Argument Workhorses)** (Impact: 371.6)
  * `brush` **(Defensive Guards)** (Impact: 333.5)
  * `LineView` **(Compute Cores)** (Impact: 270.9)
  * `internalField` **(Defensive Guards)** (Impact: 226.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 3606 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 66
* *State Mutation (weighted view):* 11935
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13483`, `structural_boundaries: 9504`, `args: 5757`, `func_start: 4088`
* *Risk/State:* `safety_bypasses: 1280`, `high_risk_execution: 14`, `state_mutation: 4723`, `dead_code: 211`, `planned_debt: 112`, `fragile_debt: 129`, `duplicate_logic: 153`, `unreferenced_by_name: 119`
* *Architecture:* `io: 11`, `api: 3`, `concurrency: 26`, `import: 3`
* *Defense:* `safety: 2436`, `doc: 1035`, `immutability_locks: 12`, `cleanup: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` option, component, XxxModel, charts, components
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/three.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 13.529)
- **Top Global Matches:** file_cluster_4: 13.529, file_cluster_12: 15.094, file_cluster_15: 15.53
- **Magnitude:** 39404.92 | **LOC:** 38298 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.4%)
- **Documentation Coverage:** 96.6417% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WebGLTextures` **(Many-Argument Workhorses)** (Impact: 707.8)
  * `WebGLRenderer` **(Defensive Guards)** (Impact: 493.8)
  * `ObjectLoader` **(Defensive Guards)** (Impact: 319.9)
  * `WebGLState` **(Many-Argument Workhorses)** (Impact: 250.8)
  * `WebGLMaterials` **(Compute Cores)** (Impact: 211.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 4822 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 18434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5127`, `structural_boundaries: 6593`, `args: 2418`, `func_start: 3806`
* *Risk/State:* `safety_bypasses: 285`, `state_mutation: 8790`, `dead_code: 39`, `planned_debt: 25`, `fragile_debt: 2`, `duplicate_logic: 134`
* *Architecture:* `io: 4`, `api: 520`, `concurrency: 13`
* *Defense:* `safety: 2196`, `doc: 58`, `test: 1`, `sync_locks: 6`, `immutability_locks: 3`, `cleanup: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_css_visit/src/generated.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 41.646)
- **Top Global Matches:** file_cluster_0: 41.646, file_cluster_4: 41.898, file_cluster_16: 42.13
- **Magnitude:** 38760.62 | **LOC:** 121691 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **4**; blast radius 0.172; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.6%), Connectivity (formerly Api Exposure) (48.1%)
- **Documentation Coverage:** 71.3029% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `experimental_raw_children` **(Many-Argument Workhorses)** (Impact: 182.2)
  * `visit_children_with_ast_path` **(Many-Argument Workhorses)** (Impact: 22.0)
  * `fold_children_with_ast_path` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `visit_mut_children_with_ast_path` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `visit_children_with_ast_path` **(Many-Argument Workhorses)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7060`, `structural_boundaries: 35154`, `args: 11484`, `func_start: 11191`, `class_start: 191`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 33`, `duplicate_logic: 2935`
* *Architecture:* `api: 375`, `import: 4`
* *Defense:* `safety: 112`, `doc: 4056`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000927
  * `Imports (Out-Degree: 4):` ::swc_visit::All, self::fields::AstParentKind, self::fields::AstParentNodeRef, swc_css_ast::*
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `crates/swc_ecma_parser/benches/files/three-0.138.3.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.523)
- **Top Global Matches:** file_cluster_4: 12.523, file_cluster_15: 14.285, file_cluster_12: 14.935
- **Magnitude:** 29794.0 | **LOC:** 36950 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.1%)
- **Documentation Coverage:** 97.6005% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WebGLTextures` **(Many-Argument Workhorses)** (Impact: 1105.1)
  * `WebGLRenderer` **(Many-Argument Workhorses)** (Impact: 561.7)
  * `WebGLPrograms` **(Many-Argument Workhorses)** (Impact: 435.2)
  * `WebGLState` **(Many-Argument Workhorses)** (Impact: 297.6)
  * `setProgram` **(Many-Argument Workhorses)** (Impact: 267.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 2945 instances
* *Concurrency (weighted view):* 110
* *State Mutation (weighted view):* 13581
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4091`, `structural_boundaries: 3828`, `args: 2291`, `func_start: 2266`, `class_start: 207`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 7691`, `dead_code: 33`, `planned_debt: 21`, `fragile_debt: 1`, `duplicate_logic: 109`, `unreferenced_by_name: 108`
* *Architecture:* `io: 5`, `api: 442`, `concurrency: 30`
* *Defense:* `safety: 2062`, `doc: 59`, `test: 1`, `sync_locks: 6`, `immutability_locks: 3`, `cleanup: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 3.4e-05
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/swc_es_parser/benches/files/three-0.138.3.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.523)
- **Top Global Matches:** file_cluster_4: 12.523, file_cluster_15: 14.285, file_cluster_12: 14.935
- **Magnitude:** 29794.0 | **LOC:** 36950 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.1%)
- **Documentation Coverage:** 97.6005% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WebGLTextures` **(Many-Argument Workhorses)** (Impact: 1105.1)
  * `WebGLRenderer` **(Many-Argument Workhorses)** (Impact: 561.7)
  * `WebGLPrograms` **(Many-Argument Workhorses)** (Impact: 435.2)
  * `WebGLState` **(Many-Argument Workhorses)** (Impact: 297.6)
  * `setProgram` **(Many-Argument Workhorses)** (Impact: 267.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 2945 instances
* *Concurrency (weighted view):* 110
* *State Mutation (weighted view):* 13581
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4091`, `structural_boundaries: 3828`, `args: 2291`, `func_start: 2266`, `class_start: 207`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 7691`, `dead_code: 33`, `planned_debt: 21`, `fragile_debt: 1`, `duplicate_logic: 109`, `unreferenced_by_name: 108`
* *Architecture:* `io: 5`, `api: 442`, `concurrency: 30`
* *Defense:* `safety: 2062`, `doc: 59`, `test: 1`, `sync_locks: 6`, `immutability_locks: 3`, `cleanup: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/victory.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.009)
- **Top Global Matches:** file_cluster_4: 12.009, file_cluster_12: 12.099, file_cluster_15: 13.057
- **Magnitude:** 29577.32 | **LOC:** 49427 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.016; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.8%)
- **Documentation Coverage:** 91.6192% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Many-Argument Workhorses)** (Impact: 204.4)
  * `VictoryTooltip` **(Defensive Guards)** (Impact: 170.3)
  * `getTransitionPropsFactory` **(Many-Argument Workhorses)** (Impact: 110.5)
    * *Intent:* * so that each child will be synchoronized for each stage of a transition * animation. It will also ...
  * `clipEdge` **(Many-Argument Workhorses)** (Impact: 103.6)
    * *Intent:* // Liang–Barsky line clipping.
  * `getScopedEvents` **(Defensive Guards)** (Impact: 96.5)
    * *Intent:* /* Returns a modified events object where each event handler is replaced by a new * function that ca...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 2721 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 9593
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6934`, `structural_boundaries: 11186`, `args: 4761`, `func_start: 2761`
* *Risk/State:* `safety_bypasses: 411`, `high_risk_execution: 1`, `state_mutation: 4151`, `planned_debt: 10`, `fragile_debt: 2`, `duplicate_logic: 668`, `unreferenced_by_name: 24`
* *Architecture:* `api: 225`, `concurrency: 11`, `import: 3`
* *Defense:* `safety: 2136`, `doc: 2150`, `test: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/d3.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 13.031)
- **Top Global Matches:** file_cluster_4: 13.031, file_cluster_12: 13.219, file_cluster_15: 14.183
- **Magnitude:** 23135.6 | **LOC:** 19567 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `brush$1` **(Defensive Guards)** (Impact: 235.6)
  * `started` **(Compute Cores)** (Impact: 176.3)
  * `clipRectangle` **(Many-Argument Workhorses)** (Impact: 130.8)
    * *Intent:* // TODO Use d3-polygon’s polygonContains here for the ring check? // TODO Eliminate duplicate buffer...
  * `zoom` **(Defensive Guards)** (Impact: 119.8)
  * `clipLine` **(Many-Argument Workhorses)** (Impact: 106.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 2739 instances
* *Concurrency (weighted view):* 95
* *State Mutation (weighted view):* 9701
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3765`, `structural_boundaries: 3682`, `args: 2246`, `func_start: 2031`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 216`, `high_risk_execution: 4`, `state_mutation: 4223`, `dead_code: 2`, `planned_debt: 18`, `duplicate_logic: 113`, `unreferenced_by_name: 50`
* *Architecture:* `io: 4`, `api: 549`, `concurrency: 20`
* *Defense:* `safety: 901`, `test: 6`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/three.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 15.471)
- **Top Global Matches:** file_cluster_12: 15.471, file_cluster_7: 16.394, file_cluster_4: 16.507
- **Magnitude:** 21546.24 | **LOC:** 16409 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (78.1%), Guard Balance (formerly Safety Score) (62.9%), Complexity Load (formerly Cognitive Load) (48.1%), Concurrency Surface (formerly Concurrency) (13.3%)
- **Documentation Coverage:** 96.0745% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WebGLTextures` **(Defensive Guards)** (Impact: 643.6)
  * `WebGLRenderer` **(Defensive Guards)** (Impact: 404.4)
  * `WebGLProgram` **(Many-Argument Workhorses)** (Impact: 396.0)
  * `earcutLinked` **(Many-Argument Workhorses)** (Impact: 290.7)
  * `ObjectLoader` **(Defensive Guards)** (Impact: 228.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1563 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 5193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4612`, `structural_boundaries: 3972`, `args: 2378`, `func_start: 2190`
* *Risk/State:* `safety_bypasses: 919`, `state_mutation: 2067`, `dead_code: 22`, `planned_debt: 12`, `duplicate_logic: 134`
* *Architecture:* `io: 4`, `api: 309`, `concurrency: 13`
* *Defense:* `safety: 1969`, `doc: 46`, `sync_locks: 6`, `immutability_locks: 3`, `cleanup: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/terser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.522)
- **Top Global Matches:** file_cluster_4: 12.522, file_cluster_12: 13.625, file_cluster_15: 15.031
- **Magnitude:** 19996.28 | **LOC:** 31780 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.03; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.1%)
- **Documentation Coverage:** 94.8606% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 1167.2)
    * *Intent:* /* -----[ Parser ]----- */
  * `tighten_body` **(Defensive Guards)** (Impact: 1018.9)
    * *Intent:* /** Tighten a bunch of statements together, and perform statement-level optimization. */
  * `collapse` **(Defensive Guards)** (Impact: 597.4)
    * *Intent:* // Search from right to left for assignment-like expressions: // - `var a = x;` // - `a = x;` // - `...
  * `tokenizer` **(Many-Argument Workhorses)** (Impact: 502.2)
  * `inline_into_call` **(Defensive Guards)** (Impact: 246.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Race Conditions:* 46 instances
* *Amplified Cascading Flux:* 2230 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 356
* *State Mutation (weighted view):* 7384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5865`, `structural_boundaries: 4103`, `args: 1808`, `func_start: 1037`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 509`, `high_risk_execution: 12`, `state_mutation: 2924`, `dead_code: 17`, `planned_debt: 10`, `fragile_debt: 8`, `duplicate_logic: 71`
* *Architecture:* `io: 22`, `api: 84`, `concurrency: 126`, `import: 5`
* *Defense:* `safety: 2135`, `doc: 52`, `test: 36`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 1.7e-05
  * `Imports (Out-Degree: 0):` source-map, acorn, assert_clause:, is_default:
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/swc_ecma_minifier/tests/benches-full/victory.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.793)
- **Top Global Matches:** file_cluster_12: 10.793, file_cluster_4: 11.056, file_cluster_7: 12.655
- **Magnitude:** 19985.42 | **LOC:** 34756 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.016; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.9%), Concurrency Surface (formerly Concurrency) (12.6%), Complexity Load (formerly Cognitive Load) (10.3%)
- **Documentation Coverage:** 77.0981% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clipEdges` **(Many-Argument Workhorses)** (Impact: 180.7)
  * `exports` **(Defensive Guards)** (Impact: 170.2)
  * `getTransitionPropsFactory` **(Many-Argument Workhorses)** (Impact: 166.9)
  * `default` **(Defensive Guards)** (Impact: 141.4)
  * `voronoiContainerMixin` **(Defensive Guards)** (Impact: 118.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1202 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 3910
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7625`, `structural_boundaries: 6709`, `args: 4452`, `func_start: 1826`
* *Risk/State:* `safety_bypasses: 1124`, `state_mutation: 1506`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 285`, `unreferenced_by_name: 40`
* *Architecture:* `api: 6`, `concurrency: 11`, `import: 4`
* *Defense:* `safety: 1743`, `doc: 2027`, `test: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_hooks/src/generated.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.651)
- **Top Global Matches:** file_cluster_0: 7.651, file_cluster_13: 8.351, file_cluster_15: 9.225
- **Magnitude:** 17827.96 | **LOC:** 35076 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **48** in-repo importer(s); it depends on **2**; blast radius 0.204; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (3.2%)
- **Documentation Coverage:** 63.0339% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `enter_opt_ts_import_call_options` **(Generic / Templated Code)** (Impact: 4.5)
  * `enter_opt_ts_type_param_instantiation` **(Generic / Templated Code)** (Impact: 4.5)
  * `exit_opt_ts_type_param_instantiation` **(Generic / Templated Code)** (Impact: 4.5)
  * `enter_ts_union_or_intersection_type` **(Parameter Forwarders)** (Impact: 4.5)
  * `exit_ts_union_or_intersection_type` **(Parameter Forwarders)** (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2368`, `structural_boundaries: 16845`, `args: 5310`, `func_start: 5310`, `class_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 604`, `import: 2`
* *Defense:* `safety: 1180`, `doc: 1801`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001078
  * `Imports (Out-Degree: 2):` swc_ecma_ast::*, swc_ecma_visit::*
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `crates/swc_ecma_minifier/tests/projects/files/react-dom-17.0.2.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.272)
- **Top Global Matches:** file_cluster_4: 10.272, file_cluster_12: 13.691, file_cluster_15: 13.806
- **Magnitude:** 17483.62 | **LOC:** 30853 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.016; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (76.5%), Guard Balance (formerly Safety Score) (53.2%), Concurrency Surface (formerly Concurrency) (13.2%), Connectivity (formerly Api Exposure) (5.0%)
- **Documentation Coverage:** 92.7027% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ChildReconciler` **(Defensive Guards)** (Impact: 324.6)
    * *Intent:* // to be able to optimize each path individually by branching early. This needs // a compiler or we ...
  * `completeWork` **(Many-Argument Workhorses)** (Impact: 234.0)
  * `diffHydratedProperties` **(Many-Argument Workhorses)** (Impact: 216.7)
  * `diffProperties` **(Many-Argument Workhorses)** (Impact: 209.7)
  * `beginWork` **(Many-Argument Workhorses)** (Impact: 160.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1688 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 5896
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4298`, `structural_boundaries: 4209`, `args: 1057`, `func_start: 1007`
* *Risk/State:* `safety_bypasses: 143`, `high_risk_execution: 21`, `state_mutation: 2520`, `dead_code: 3`, `planned_debt: 171`, `fragile_debt: 62`, `duplicate_logic: 42`, `unreferenced_by_name: 12`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 14`, `import: 2`
* *Defense:* `safety: 2425`, `doc: 109`, `test: 7`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/d3.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 12.736)
- **Top Global Matches:** file_cluster_12: 12.736, file_cluster_4: 14.063, file_cluster_7: 14.282
- **Magnitude:** 14807.9 | **LOC:** 11247 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.2%), Complexity Load (formerly Cognitive Load) (48.4%), Concurrency Surface (formerly Concurrency) (16.2%), Dead Code Surface (formerly Dead Code) (4.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clipRectangle` **(Many-Argument Workhorses)** (Impact: 206.6)
    * *Intent:* // TODO Use d3-polygon’s polygonContains here for the ring check? // TODO Eliminate duplicate buffer...
  * `brush$1` **(Defensive Guards)** (Impact: 204.7)
  * `started` **(Defensive Guards)** (Impact: 155.6)
  * `zoom` **(Defensive Guards)** (Impact: 104.8)
  * `formatLocale` **(Defensive Guards)** (Impact: 98.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 957 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 3142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3593`, `structural_boundaries: 3304`, `args: 2227`, `func_start: 1907`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 497`, `high_risk_execution: 3`, `state_mutation: 1228`, `dead_code: 2`, `planned_debt: 15`, `duplicate_logic: 114`, `unreferenced_by_name: 196`
* *Architecture:* `io: 4`, `concurrency: 20`
* *Defense:* `safety: 692`, `test: 6`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/output/react-dom-17.0.2.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 16.666)
- **Top Global Matches:** file_cluster_4: 16.666, file_cluster_6: 18.194, file_cluster_12: 18.789
- **Magnitude:** 14425.38 | **LOC:** 11759 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.016; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (92.8%), Guard Balance (formerly Safety Score) (63.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.9%), Concurrency Surface (formerly Concurrency) (14.2%)
- **Documentation Coverage:** 94.4724% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flushPendingUnsafeLifecycleWarnings` **(Defensive Guards)** (Impact: 2848.8)
  * `completeWork` **(Many-Argument Workhorses)** (Impact: 594.9)
  * `dispatchEventForPluginEventSystem` **(Many-Argument Workhorses)** (Impact: 524.1)
  * `beginWork` **(Defensive Guards)** (Impact: 333.6)
  * `ChildReconciler` **(Defensive Guards)** (Impact: 257.8)
    * *Intent:* // to be able to optimize each path individually by branching early. This needs // a compiler or we ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 636 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 2149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3926`, `structural_boundaries: 2512`, `args: 853`, `func_start: 625`
* *Risk/State:* `safety_bypasses: 645`, `high_risk_execution: 21`, `state_mutation: 877`, `dead_code: 2`, `planned_debt: 103`, `fragile_debt: 59`, `duplicate_logic: 43`, `unreferenced_by_name: 24`
* *Architecture:* `api: 1`, `concurrency: 14`, `import: 3`
* *Defense:* `safety: 1994`, `doc: 65`, `test: 6`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, test-utils, unstable_mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/files/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.136)
- **Top Global Matches:** file_cluster_4: 10.136, file_cluster_12: 13.035, file_cluster_6: 14.361
- **Magnitude:** 13297.22 | **LOC:** 21880 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (64.1%), Concurrency Surface (formerly Concurrency) (31.2%), Dead Code Surface (formerly Dead Code) (4.8%)
- **Documentation Coverage:** 62.2951% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getterFn` **(Many-Argument Workhorses)** (Impact: 610.3)
  * `$CompileProvider` **(Many-Argument Workhorses)** (Impact: 555.6)
  * `applyDirectivesToNode` **(Many-Argument Workhorses)** (Impact: 333.5)
    * *Intent:* * scope argument is auto-generated to the new * child of the transcluded parent scope. * argument ha...
  * `link` **(Many-Argument Workhorses)** (Impact: 230.9)
  * `minErr` **(Compute Cores)** (Impact: 179.9)
    * *Intent:* * * If fewer arguments are specified than necessary for interpolation, the extra * interpolation mar...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 1329 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 180
* *State Mutation (weighted view):* 4358
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2148`, `structural_boundaries: 1529`, `args: 1055`, `func_start: 689`
* *Risk/State:* `safety_bypasses: 188`, `high_risk_execution: 21`, `state_mutation: 1700`, `dead_code: 5`, `planned_debt: 17`, `fragile_debt: 12`, `duplicate_logic: 10`, `unreferenced_by_name: 50`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 40`
* *Defense:* `safety: 413`, `doc: 438`, `test: 203`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/benches/files/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.362)
- **Top Global Matches:** file_cluster_4: 10.362, file_cluster_12: 13.13, file_cluster_6: 14.373
- **Magnitude:** 13240.84 | **LOC:** 20369 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%), Complexity Load (formerly Cognitive Load) (53.5%)
- **Documentation Coverage:** 62.0558% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getterFn` **(Many-Argument Workhorses)** (Impact: 601.6)
  * `$CompileProvider` **(Many-Argument Workhorses)** (Impact: 533.0)
  * `applyDirectivesToNode` **(Many-Argument Workhorses)** (Impact: 324.8)
    * *Intent:* * scope argument is auto-generated to the new * child of the transcluded parent scope. * argument ha...
  * `link` **(Many-Argument Workhorses)** (Impact: 227.1)
  * `minErr` **(Compute Cores)** (Impact: 178.7)
    * *Intent:* * * If fewer arguments are specified than necessary for interpolation, the extra * interpolation mar...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 1351 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 190
* *State Mutation (weighted view):* 4371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2150`, `structural_boundaries: 1529`, `args: 1055`, `func_start: 684`
* *Risk/State:* `safety_bypasses: 188`, `high_risk_execution: 21`, `state_mutation: 1669`, `dead_code: 5`, `planned_debt: 17`, `fragile_debt: 12`, `duplicate_logic: 6`, `unreferenced_by_name: 50`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 40`
* *Defense:* `safety: 413`, `doc: 438`, `test: 203`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/benches/files/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.362)
- **Top Global Matches:** file_cluster_4: 10.362, file_cluster_12: 13.13, file_cluster_6: 14.373
- **Magnitude:** 13240.84 | **LOC:** 20369 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%), Complexity Load (formerly Cognitive Load) (53.5%)
- **Documentation Coverage:** 62.0558% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getterFn` **(Many-Argument Workhorses)** (Impact: 601.6)
  * `$CompileProvider` **(Many-Argument Workhorses)** (Impact: 533.0)
  * `applyDirectivesToNode` **(Many-Argument Workhorses)** (Impact: 324.8)
    * *Intent:* * scope argument is auto-generated to the new * child of the transcluded parent scope. * argument ha...
  * `link` **(Many-Argument Workhorses)** (Impact: 227.1)
  * `minErr` **(Compute Cores)** (Impact: 178.7)
    * *Intent:* * * If fewer arguments are specified than necessary for interpolation, the extra * interpolation mar...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 1351 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 190
* *State Mutation (weighted view):* 4371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2150`, `structural_boundaries: 1529`, `args: 1055`, `func_start: 684`
* *Risk/State:* `safety_bypasses: 188`, `high_risk_execution: 21`, `state_mutation: 1669`, `dead_code: 5`, `planned_debt: 17`, `fragile_debt: 12`, `duplicate_logic: 6`, `unreferenced_by_name: 50`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 40`
* *Defense:* `safety: 413`, `doc: 438`, `test: 203`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/lodash.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 4.845)
- **Top Global Matches:** file_cluster_7: 4.845, file_cluster_12: 6.809, file_cluster_5: 8.449
- **Magnitude:** 10924.41 | **LOC:** 17210 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.016; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (63.7%), Concurrency Surface (formerly Concurrency) (26.3%), Complexity Load (formerly Cognitive Load) (20.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 1411
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 1577`, `args: 693`, `func_start: 512`
* *Risk/State:* `safety_bypasses: 338`, `state_mutation: 1387`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 300`, `doc: 680`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/vue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.299)
- **Top Global Matches:** file_cluster_4: 10.299, file_cluster_12: 13.945, file_cluster_15: 14.103
- **Magnitude:** 9660.4 | **LOC:** 11966 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.0%), Guard Balance (formerly Safety Score) (61.0%)
- **Documentation Coverage:** 80.6499% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPatchFunction` **(Compute Cores)** (Impact: 348.4)
  * `parseHTML` **(Many-Argument Workhorses)** (Impact: 147.7)
  * `patchVnode` **(Many-Argument Workhorses)** (Impact: 98.9)
  * `enter` **(Many-Argument Workhorses)** (Impact: 97.6)
    * *Intent:* /* */
  * `addHandler` **(Many-Argument Workhorses)** (Impact: 88.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 983 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 152
* *State Mutation (weighted view):* 3227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2431`, `structural_boundaries: 2000`, `args: 675`, `func_start: 645`
* *Risk/State:* `safety_bypasses: 63`, `high_risk_execution: 11`, `state_mutation: 1261`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 13`
* *Architecture:* `api: 17`, `concurrency: 32`
* *Defense:* `safety: 649`, `doc: 118`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/output/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.787)
- **Top Global Matches:** file_cluster_4: 11.787, file_cluster_12: 13.138, file_cluster_7: 14.511
- **Magnitude:** 8546.32 | **LOC:** 12187 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.2%), Complexity Load (formerly Cognitive Load) (48.9%), Concurrency Surface (formerly Concurrency) (38.2%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 55.4276% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getterFn` **(Many-Argument Workhorses)** (Impact: 527.3)
  * `$CompileProvider` **(Many-Argument Workhorses)** (Impact: 464.4)
    * *Intent:* * var templateHTML = angular.element('<p>{{total}}</p>'), * scope = ....; * * var clonedElement = $c...
  * `compileNodes` **(Many-Argument Workhorses)** (Impact: 340.8)
    * *Intent:* /** * Compile function matches each node in nodeList against the directives. Once all directives * f...
  * `applyDirectivesToNode` **(Many-Argument Workhorses)** (Impact: 340.4)
    * *Intent:* * scope argument is auto-generated to the new * child of the transcluded parent scope. * argument ha...
  * `link` **(Many-Argument Workhorses)** (Impact: 195.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 520 instances
* *High Risk Execution (weighted view):* 12
* *Concurrency (weighted view):* 128
* *State Mutation (weighted view):* 1781
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1847`, `structural_boundaries: 1179`, `args: 1024`, `func_start: 527`
* *Risk/State:* `safety_bypasses: 300`, `high_risk_execution: 18`, `state_mutation: 741`, `dead_code: 4`, `planned_debt: 14`, `fragile_debt: 11`, `duplicate_logic: 5`, `unreferenced_by_name: 12`
* *Architecture:* `io: 19`, `api: 1`, `concurrency: 38`
* *Defense:* `safety: 360`, `doc: 375`, `test: 160`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/benches/files/cal.com.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.644)
- **Top Global Matches:** file_cluster_4: 11.644, file_cluster_15: 12.56, file_cluster_12: 12.677
- **Magnitude:** 7859.44 | **LOC:** 30592 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **528**; blast radius 0.016; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (69.3%), Guard Balance (formerly Safety Score) (47.2%), Mutation Surface (formerly State Flux) (30.3%), Complexity Load (formerly Cognitive Load) (21.8%)
- **Documentation Coverage:** 96.5795% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Success` **(Many-Argument Workhorses)** (Impact: 254.4)
  * `BookingListItem` **(Defensive Guards)** (Impact: 182.8)
  * `Signup` **(Compute Cores)** (Impact: 89.3)
  * `getServerSideProps` **(Defensive Guards)** (Impact: 82.3)
  * `EventTypeSingleLayout` **(Many-Argument Workhorses)** (Impact: 62.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 63 instances
* *Amplified Cascading Flux:* 304 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 963
* *State Mutation (weighted view):* 1053
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3341`, `structural_boundaries: 6121`, `args: 1708`, `func_start: 751`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 9`, `state_mutation: 445`, `dead_code: 7`, `planned_debt: 38`, `fragile_debt: 8`, `unreferenced_by_name: 27`
* *Architecture:* `io: 42`, `api: 653`, `concurrency: 648`, `import: 2597`
* *Defense:* `safety: 1433`, `doc: 72`, `sync_locks: 11`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , [type], [slug], billing, index, [slug], [type], [uid]...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/benches/files/cal.com.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.644)
- **Top Global Matches:** file_cluster_4: 11.644, file_cluster_15: 12.56, file_cluster_12: 12.677
- **Magnitude:** 7859.44 | **LOC:** 30592 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **528**; blast radius 0.016; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (69.3%), Guard Balance (formerly Safety Score) (47.2%), Mutation Surface (formerly State Flux) (30.3%), Complexity Load (formerly Cognitive Load) (21.8%)
- **Documentation Coverage:** 96.5795% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Success` **(Many-Argument Workhorses)** (Impact: 254.4)
  * `BookingListItem` **(Defensive Guards)** (Impact: 182.8)
  * `Signup` **(Compute Cores)** (Impact: 89.3)
  * `getServerSideProps` **(Defensive Guards)** (Impact: 82.3)
  * `EventTypeSingleLayout` **(Many-Argument Workhorses)** (Impact: 62.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 63 instances
* *Amplified Cascading Flux:* 304 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 963
* *State Mutation (weighted view):* 1053
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3341`, `structural_boundaries: 6121`, `args: 1708`, `func_start: 751`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 9`, `state_mutation: 445`, `dead_code: 7`, `planned_debt: 38`, `fragile_debt: 8`, `unreferenced_by_name: 27`
* *Architecture:* `io: 42`, `api: 653`, `concurrency: 648`, `import: 2597`
* *Defense:* `safety: 1433`, `doc: 72`, `sync_locks: 11`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , [type], [slug], billing, index, [slug], [type], [uid]...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/vue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.124)
- **Top Global Matches:** file_cluster_4: 12.124, file_cluster_6: 13.497, file_cluster_12: 15.289
- **Magnitude:** 7206.08 | **LOC:** 4452 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (65.3%), Guard Balance (formerly Safety Score) (59.4%), Connectivity (formerly Api Exposure) (44.8%), Complexity Load (formerly Cognitive Load) (37.1%)
- **Documentation Coverage:** 77.4257% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ast` **(Defensive Guards)** (Impact: 337.1)
    * *Intent:* /* */ var ref$1 = (baseCompile = function(template, options) {
  * `patch` **(Defensive Guards)** (Impact: 293.6)
  * `createComponent` **(Many-Argument Workhorses)** (Impact: 194.2)
  * `patchVnode` **(Defensive Guards)** (Impact: 144.8)
  * `genData$2` **(Defensive Guards)** (Impact: 130.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 419 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 127
* *State Mutation (weighted view):* 1327
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2428`, `structural_boundaries: 1203`, `args: 617`, `func_start: 407`
* *Risk/State:* `safety_bypasses: 178`, `high_risk_execution: 6`, `state_mutation: 489`, `planned_debt: 1`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 18`, `concurrency: 32`
* *Defense:* `safety: 561`, `doc: 97`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/swc_css_parser/benches/compare.rs` (RUST) | Magnitude: 25.64 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 38, args: 18, closures: 8
- `crates/swc_ecma_transforms_react/src/display_name/tests.rs` (RUST) | Magnitude: 6.18 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, args: 6, core_var_decl: 6, design_snake_case: 6
- `crates/swc_ecma_parser/tests/tsc/jsDeclarationsDefault.ts` (TYPESCRIPT) | Magnitude: 18.56 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 15, api: 10, branch: 6, doc: 4
- `crates/swc_ecma_transforms_proposal/src/decorators/legacy/mod.rs` (RUST) | Magnitude: 164.62 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 371, structural_boundaries: 106, branch: 36, core_var_decl: 34
- `crates/swc_ecma_parser/tests/tsc/iteratorSpreadInCall7.ts` (TYPESCRIPT) | Magnitude: 6.78 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 7, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `crates/swc/tests/tsc-references/logicalNotOperatorWithNumberType.1.normal.js` (JAVASCRIPT) | Magnitude: 10.4 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 23, indent_spaces: 17, core_var_decl: 16, design_pascal_case: 13
- `crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2799_1/input.js` (JAVASCRIPT) | Magnitude: 8.18 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 4, args: 4, func_start: 3
- `crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2017_async_to_generator.rs/super_update.js` (JAVASCRIPT) | Magnitude: 15.24 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 21, args: 15, func_start: 7
- `crates/swc_ecma_minifier/tests/terser/compress/drop_unused/drop_assign/output.mangleOnly.js` (JAVASCRIPT) | Magnitude: 10.92 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, args: 6, func_start: 5
- `crates/swc_ecma_minifier/tests/terser/compress/drop_unused/keep_assign/output.mangleOnly.js` (JAVASCRIPT) | Magnitude: 10.92 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, args: 6, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/swc_ecma_parser/tests/tsc/jsDeclarationsFunctionLikeClasses2.ts` (TYPESCRIPT) | Magnitude: 49.04 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 11, structural_boundaries: 9, args: 8
- `crates/swc/tests/tsc-references/deleteOperatorWithStringType.1.normal.js` (JAVASCRIPT) | Magnitude: 10.38 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 46, indent_spaces: 17, core_var_decl: 17, design_pascal_case: 14
- `crates/swc_ecma_minifier/tests/terser/compress/drop_unused/keep_assign/output.js` (JAVASCRIPT) | Magnitude: 10.92 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, args: 6, func_start: 5
- `crates/swc_ecma_minifier/tests/terser/compress/drop_unused/keep_assign/output.terser.js` (JAVASCRIPT) | Magnitude: 10.92 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, args: 6, func_start: 5
- `crates/swc/tests/tsc-references/computedPropertyNames43_ES5.1.normal.js` (JAVASCRIPT) | Magnitude: 10.66 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, func_start: 12, structural_boundaries: 11, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `crates/swc/tests/tsc-references/outFilerootDirModuleNamesSystem.1.normal.js` (JAVASCRIPT) | Magnitude: 10.28 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, args: 7, structural_boundaries: 6, closures: 6
- `crates/swc_ecma_minifier/tests/fixture/next/react-ace/chunks/8a28b14e.d8fbda268ed281a1/input.js` (JAVASCRIPT) | Magnitude: 7.13 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 26404, state_mutation: 4467, structural_boundaries: 3957, core_var_decl: 3568
- `crates/swc_ecma_parser/tests/tsc/switchStatements.ts` (TYPESCRIPT) | Magnitude: 3.54 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: branch: 37, indent_spaces: 24, structural_boundaries: 11, args: 5
- `crates/swc/tests/fixture/next.js/40399/2/output/index.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 9, branch: 4, args: 4
- `.github/workflows/CI.yml` (YAML) | Magnitude: 128.94 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 397, branch: 71, func_start: 47, structural_boundaries: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/swc/tests/fixture/rspack-10260/es2020_default/output/index.ts` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, state_mutation: 2, debug_prints: 2
- `crates/swc/tests/fixture/issues-8xxx/8367/input/index.ts` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1
- `crates/swc/tests/tsc-references/objectTypeWithStringNamedPropertyOfIllegalCharacters.2.minified.js` (JAVASCRIPT) | Magnitude: 14.16 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: bitwise_ops: 10, indent_spaces: 3, structural_boundaries: 2, decorators: 1
- `crates/swc_ecma_minifier/tests/terser/compress/harmony/format_methods/output.js` (JAVASCRIPT) | Magnitude: 5.82 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, args: 3, func_start: 3, unreferenced_by_name: 3
- `crates/swc_ecma_minifier/tests/terser/compress/harmony/format_methods/output.terser.js` (JAVASCRIPT) | Magnitude: 5.82 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, args: 3, func_start: 3, unreferenced_by_name: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `crates/swc/tests/tsc-references/callOverload.1.normal.js` (JAVASCRIPT) | Magnitude: 15.2 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 2, safety_bypasses: 2, reflection_metaprogramming: 2, decorators: 1
- `packages/helpers/esm/_using.js` (JAVASCRIPT) | Magnitude: 32.26 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 15, branch: 11, safety: 7, structural_boundaries: 4
- `crates/swc_ecma_transforms_base/src/helpers/_using.js` (JAVASCRIPT) | Magnitude: 31.26 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 16, branch: 11, safety: 7, structural_boundaries: 3
- `crates/swc_ecma_transforms_module/tests/fixture/common/issue-2344/2/output.cjs` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, args: 4, class_start: 4
- `crates/swc_ecma_minifier/tests/terser/compress/evaluate/unsafe_array/output.js` (JAVASCRIPT) | Magnitude: 15.22 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 8, safety_bypasses: 2, debug_prints: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `crates/swc_ecma_codegen/tests/test262-min/ecba8fb326c2c985.js` (JAVASCRIPT) | Magnitude: 46.52 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 18, state_mutation: 12, structural_boundaries: 1
- `crates/swc_ecma_parser/tests/tsc/parserRealSource13.ts` (TYPESCRIPT) | Magnitude: 232.58 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 132, func_start: 111, branch: 109, unreferenced_by_name: 107
- `crates/swc/tests/fixture/issues-7xxx/7220/1/input/index.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, class_start: 2, api: 2
- `crates/swc/tests/tsc-references/tsxSfcReturnNull.1.normal.js` (JAVASCRIPT) | Magnitude: 3.56 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, args: 3, func_start: 3
- `crates/swc/tests/tsc-references/tsxSfcReturnNullStrictNullChecks.1.normal.js` (JAVASCRIPT) | Magnitude: 3.56 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/swc_ecma_transforms_compat/tests/private-in-object/to-native-fields/class-expression-instance/input.js` (JAVASCRIPT) | Magnitude: 5.16 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, args: 2, func_start: 2
- `crates/swc_ecma_transforms_compat/tests/private-in-object/to-native-fields/class-expression-static/input.js` (JAVASCRIPT) | Magnitude: 5.16 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, args: 2, func_start: 2
- `crates/swc_ecma_transforms_compat/tests/class_fields_use_set/basic/4/output.js` (JAVASCRIPT) | Magnitude: 8.48 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, state_mutation: 4, encapsulation: 4, args: 3
- `crates/swc/tests/babel-exec/packages/babel-plugin-proposal-private-methods/test/fixtures/private-static-method-loose/class-check/exec.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, args: 2, func_start: 2
- `crates/swc/tests/babel-exec/packages/babel-plugin-proposal-private-methods/test/fixtures/private-static-method-privateFieldsAsProperties/class-check/exec.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/swc_css_parser/src/parser/macros.rs` (RUST) | Magnitude: 23.86 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 119, branch: 17, reflection_metaprogramming: 12, macros: 12
- `crates/swc_ecma_parser/src/parser/macros.rs` (RUST) | Magnitude: 17.78 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 10, core_var_decl: 9, design_snake_case: 8
- `crates/swc_css_prefixer/tests/fixture/important/output.css` (CSS) | Magnitude: 0.01 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 3, indent_spaces: 3, class_start: 1
- `crates/swc_ecma_parser/tests/span/ts/expr/const-assertion.ts` (TYPESCRIPT) | Magnitude: 10.52 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 1
- `crates/swc_ecma_parser/tests/typescript/custom/issue-432-readonly-array/input.ts` (TYPESCRIPT) | Magnitude: 10.52 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `crates/swc/tests/tsc-references/ArrowFunction4.1.normal.js` (JAVASCRIPT) | Magnitude: 1.82 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: func_start: 2, structural_boundaries: 1, args: 1, core_var_decl: 1
- `crates/swc/tests/tsc-references/parserX_ArrowFunction4.1.normal.js` (JAVASCRIPT) | Magnitude: 1.82 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: func_start: 2, structural_boundaries: 1, args: 1, core_var_decl: 1
- `crates/swc_ecma_transforms_base/tests/resolver/issues/1140/output.js` (JAVASCRIPT) | Magnitude: 15.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 13, core_var_decl: 3, structural_boundaries: 2, design_snake_case: 2
- `crates/jsdoc/tests/fixtures/moduletag8.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 5, api: 4, args: 2
- `crates/swc_ecma_minifier/tests/fixture/issues/10720/input.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 6, branch: 4, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/swc_xml_parser/src/parser/mod.rs` (RUST) | Magnitude: 256.62 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 523, structural_boundaries: 106, branch: 56, core_var_decl: 56
- `crates/swc_ecma_minifier/src/program_data.rs` (RUST) | Magnitude: 584.18 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 550, structural_boundaries: 107, state_mutation: 105, branch: 92
- `crates/swc_ecma_minifier/tests/fixture/issues/react-instancesearch/002/output.js` (JAVASCRIPT) | Magnitude: 0.18 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 102, args: 68, branch: 41
- `crates/swc_ecma_minifier/benches/full/victory.js` (JAVASCRIPT) | Magnitude: 29577.32 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29994, structural_boundaries: 11186, core_var_decl: 9102, branch: 6934
- `crates/swc_ecma_minifier/tests/fixture/next/styled-components/1/input.js` (JAVASCRIPT) | Magnitude: 3.6 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 9502, structural_boundaries: 1001, core_var_decl: 896, branch: 731

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `crates/swc/examples/transform.rs` (RUST) | Magnitude: 4.4 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, import: 4, core_var_decl: 4
- `crates/swc_ecma_parser/tests/tsc/subtypingWithConstructSignatures3.ts` (TYPESCRIPT) | Magnitude: 38.6 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 136, indent_spaces: 91, args: 45, generics: 29
- `crates/swc_common/src/source_map.rs` (RUST) | Magnitude: 740.34 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1233, structural_boundaries: 315, core_var_decl: 223, doc: 221
- `crates/swc_ecma_lints/src/rules/no_param_reassign.rs` (RUST) | Magnitude: 115.42 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 233, structural_boundaries: 37, branch: 30, args: 25
- `crates/swc_plugin_backend_tests/tests/fixture/swc_internal_plugin/src/lib.rs` (RUST) | Magnitude: 0.03 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 85, doc: 22, structural_boundaries: 19, debug_prints: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/swc_ecma_parser/tests/tsc/additionOperatorWithAnyAndEveryType.ts` (TYPESCRIPT) | Magnitude: 4.84 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 32, core_var_decl: 20, design_snake_case: 20, design_short_vars: 9
- `crates/swc_ecma_minifier/tests/fixture/issues/8924/output.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, core_var_decl: 2, design_snake_case: 2
- `crates/swc_ecma_transforms_compat/tests/es2021_logcal_assignments.rs` (RUST) | Magnitude: 11.18 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 79, safety_bypasses: 18, core_var_decl: 11, design_snake_case: 11
- `crates/swc_ecma_minifier/tests/fixture/projects/jquery/26/input.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, core_var_decl: 3, branch: 2
- `crates/swc_ecma_codegen/tests/test262/f658dbaa20c36388.js` (JAVASCRIPT) | Magnitude: 12.6 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 3, branch: 2, args: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/swc_ecma_parser/src/parser/expr.rs` (RUST) | Magnitude: 1448.46 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 2415, branch: 595, structural_boundaries: 519, core_var_decl: 335

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/swc_ecma_transforms_macros/src/fast.rs` (RUST) | Magnitude: 45.58 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 31, branch: 16, core_var_decl: 16
- `crates/swc_ecma_minifier/tests/terser/compress/transform/if_return/input.js` (JAVASCRIPT) | Magnitude: 21.8 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: branch: 8, indent_spaces: 8, structural_boundaries: 5, args: 1
- `crates/swc_ecma_minifier/tests/terser/compress/transform/if_return/output.mangleOnly.js` (JAVASCRIPT) | Magnitude: 20.8 | Delta: **0.184** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: branch: 8, indent_spaces: 8, structural_boundaries: 5, args: 1

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/CI.yml` -> Churn: **74.15%** | Cog Load: 8.9274% | Debt: 99.5207%
- `crates/swc_ecma_transforms_base/src/helpers/_wrap_reg_exp.js` -> Churn: **50.61%** | Cog Load: 100.0% | Debt: 79.35%
- `packages/helpers/esm/_wrap_reg_exp.js` -> Churn: **50.61%** | Cog Load: 100.0% | Debt: 49.2285%
- `crates/swc_ecma_minifier/src/compress/optimize/mod.rs` -> Churn: **50.61%** | Cog Load: 29.3144% | Debt: 73.1873%
- `crates/swc_ecma_minifier/src/program_data.rs` -> Churn: **50.61%** | Cog Load: 54.6604% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/swc_ecma_minifier/tests/benches-full/victory.js` -> **Austaras** (100.0% isolated ownership) | Magnitude: 19985.42
- `crates/swc_ecma_minifier/tests/projects/output/react-dom-17.0.2.js` -> **Austaras** (100.0% isolated ownership) | Magnitude: 14425.38
- `crates/swc_es_parser/src/parser.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 3766.7
- `crates/swc_ecma_parser/src/parser/typescript.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 2636.34
- `crates/swc_ecma_transforms_proposal/src/decorator_impl.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 1682.64

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/swc_common/src/syntax_pos.rs` -> **Severity: 0.588** (Embedded: 0.0119 * Error Risk: 49.2831%)
- `crates/swc_common/src/syntax_pos/hygiene.rs` -> **Severity: 0.413** (Embedded: 0.0074 * Error Risk: 55.784%)
- `crates/ast_node/src/lib.rs` -> **Severity: 0.395** (Embedded: 0.0068 * Error Risk: 58.0343%)
- `crates/swc_common/src/sync.rs` -> **Severity: 0.394** (Embedded: 0.0081 * Error Risk: 48.5658%)
- `crates/swc_common/src/syntax_pos/analyze_source_file.rs` -> **Severity: 0.386** (Embedded: 0.0072 * Error Risk: 53.2771%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/swc_ecma_ast/src/lib.rs` -> **Severity: 205.182** (Blast Radius: 2.257 * Doc Risk: 90.9091%)
- `crates/swc_common/src/syntax_pos.rs` -> **Severity: 173.311** (Blast Radius: 2.797 * Doc Risk: 61.9632%)
- `crates/swc_atoms/src/lib.rs` -> **Severity: 78.283** (Blast Radius: 0.944 * Doc Risk: 82.9268%)
- `crates/swc_ecma_visit/src/generated.rs` -> **Severity: 65.18** (Blast Radius: 0.759 * Doc Risk: 85.8757%)
- `crates/swc_common/src/sync.rs` -> **Severity: 62.871** (Blast Radius: 0.663 * Doc Risk: 94.8276%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 14621 literal sites + 299 sites through wrappers = 14920
- **`panics_and_aborts`:** 9265 literal sites + 244 sites through wrappers = 9509

- `throwError` (function, panics_and_aborts, primitive): 39 call sites in 1 files -- `crates/swc_ecma_minifier/benches/full/echarts.js`
- `throwError` (function, panics_and_aborts, primitive): 39 call sites in 1 files -- `crates/swc_ecma_minifier/tests/benches-full/echarts.js`
- `fn` (function, debug_prints, primitive): 24 call sites in 1 files -- `crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/collapse_vars_side_effects_2/input.js`
- `fn` (function, debug_prints, primitive): 24 call sites in 1 files -- `crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/collapse_vars_side_effects_2/output.js`
- `fn` (function, debug_prints, primitive): 24 call sites in 1 files -- `crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/collapse_vars_side_effects_2/output.terser.js`
- `r` (function, debug_prints, primitive): 24 call sites in 1 files -- `crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/collapse_vars_side_effects_2/output.mangleOnly.js`
- `log` (function, debug_prints, primitive): 17 call sites in 1 files -- `crates/swc_ecma_minifier/scripts/x/terser/compress.js`
- `disposedWarning` (function, debug_prints, primitive): 13 call sites in 1 files -- `crates/swc_ecma_minifier/tests/benches-full/echarts.js`
- `P` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/input.js`
- `noRouter` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `crates/swc/tests/fixture/next.js/server/render/1/input/index.tsx`
- `noRouter` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `crates/swc/tests/fixture/next.js/server/render/1/output/index.tsx`
- `noRouter` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `crates/swc_ecma_transforms_typescript/tests/fixture/next/server/render/1/input.tsx`
*(+172 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 314177 call pairs -- scoped 28.1%, unique 0.0%, ambiguous 34.1%, external 37.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 196314 | 27.3% | 0.0% | 39.0% | 33.7% |
| rust | 90001 | 27.2% | 0.0% | 24.2% | 48.6% |
| typescript | 27581 | 36.4% | 0.0% | 32.4% | 31.2% |
| shell | 259 | 1.5% | 0.0% | 0.0% | 98.5% |
| python | 22 | 4.5% | 0.0% | 0.0% | 95.5% |

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
