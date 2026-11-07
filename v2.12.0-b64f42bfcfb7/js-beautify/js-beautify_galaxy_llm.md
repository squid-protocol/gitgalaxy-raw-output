# ARCHITECTURAL_BRIEF: js-beautify
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 40 analyzed artifact(s), 10220 LOC.
- **Load-bearing artifact:** `package/js/src/core/pattern.js` -- 4 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/js/lib/cli.js` -- pulls in 8 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/js/lib/beautifier.js` at magnitude 5715.36 (structural weight, not risk).
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
| Total Artifacts | 46 |
| Analyzed Artifacts (Scanned) | 40 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 10220 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.495 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0262 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5534 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 38 | 10220 | 95.0% |
| MARKDOWN | 1 | 0 | 2.5% |
| PLAINTEXT | 1 | 0 | 2.5% |

## 4.1 SOURCE ENCODINGS
All 40 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Callbacks & Closures Files 38%, Large Core Modules (2) 32%, Data / Markup / Trivial 15%, Parameter Forwarders Files 8%, Compute Cores Files 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 38 | 95.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 5.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1694 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3243 LOC)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.6 | 57.2 | 64.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.7 | 57.4 | 59.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 78.1 | 10.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 10.6 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 60.2 | 22.8 | 21.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 56.1 | 2.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 82.9 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 29.0 | 8.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 86.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 0 | 0 | 0 | - |
| guards | 1456 | 28 | 69 | `package/js/lib/beautifier.js` |
| danger | 120 | 11 | 9 | `package/js/lib/cli.js` |
| concurrency | 30 | 3 | 0 | `package/js/lib/beautifier.js` |
| connectivity | 138 | 27 | 6 | `package/js/lib/beautifier.js` |
| io | 34 | 6 | 1 | `package/js/lib/cli.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 219 | 19 | 18 | `package/js/lib/beautifier.js` |
| events | 35 | 6 | 2 | `package/js/lib/beautifier.js` |
| tests | 74 | 6 | 10 | `package/js/lib/unpackers/javascriptobfuscator_unpacker.js` |
| docs | 87 | 4 | 0 | `package/js/lib/beautifier.js` |
| debt | 63 | 7 | 2 | `package/js/lib/cli.js` |
| mutation | 4527 | 37 | 251 | `package/js/lib/beautifier.js` |
| dead_code | 81 | 17 | 4 | `package/js/lib/beautifier.js` |
| credential | 0 | 0 | 0 | - |
| threat | 5 | 2 | 0 | `package/js/lib/beautifier.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.4629**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/js/lib/cli.js` (Hits: 15)
- `package/js/src/cli.js` (Hits: 15)
- `package/js/lib/beautifier.js` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **pattern.js** (`package/js/src/core/pattern.js`) — 4 inbound connections
2. **cli.js** (`package/js/lib/cli.js`) — 3 inbound connections
3. **directives.js** (`package/js/src/core/directives.js`) — 3 inbound connections
4. **inputscanner.js** (`package/js/src/core/inputscanner.js`) — 3 inbound connections
5. **options.js** (`package/js/src/core/options.js`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cli.js** (`package/js/lib/cli.js`) — 8 outbound dependencies
2. **cli.js** (`package/js/src/cli.js`) — 8 outbound dependencies
3. **tokenizer.js** (`package/js/src/javascript/tokenizer.js`) — 6 outbound dependencies
4. **beautifier.js** (`package/js/src/javascript/beautifier.js`) — 5 outbound dependencies
5. **tokenizer.js** (`package/js/src/core/tokenizer.js`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `TagOpenParserToken` **(Many-Argument Workhorses)** (@ `package/js/lib/beautifier.js`) -> Impact: **349.9** | LOC: 838
- `_set_tag_position` **(Many-Argument Workhorses)** (@ `package/js/lib/beautifier.js`) -> Impact: **326.3** | LOC: 745
- `TagOpenParserToken` **(Many-Argument Workhorses)** (@ `package/js/src/html/beautifier.js`) -> Impact: **299.2** | LOC: 304
- `_set_tag_position` **(Many-Argument Workhorses)** (@ `package/js/src/html/beautifier.js`) -> Impact: **270.3** | LOC: 213
- `handle_word` **(Defensive Guards)** (@ `package/js/lib/beautifier.js`) -> Impact: **232.1** | LOC: 229
- `handle_word` **(Defensive Guards)** (@ `package/js/src/javascript/beautifier.js`) -> Impact: **232.1** | LOC: 229
- `handle_operator` **(Defensive Guards)** (@ `package/js/lib/beautifier.js`) -> Impact: **120.0** | LOC: 194
- `handle_operator` **(Defensive Guards)** (@ `package/js/src/javascript/beautifier.js`) -> Impact: **120.0** | LOC: 194
- `beautify` **(I/O & Config Routines)** (@ `package/js/lib/beautifier.js`) -> Impact: **103.5** | LOC: 389
  * *Intent:* /*_____________________--------------------_____________________*/
- `beautify` **(I/O & Config Routines)** (@ `package/js/src/css/beautifier.js`) -> Impact: **103.3** | LOC: 386
  * *Intent:* /*_____________________--------------------_____________________*/

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/js/lib` | 2 | 6268.36 | 73.11% | 12.84% |
| `package/js/src/javascript` | 4 | 1969.8 | 59.07% | 5.99% |
| `package/js/src/html` | 4 | 1766.0 | 60.01% | 2.34% |
| `package/js/src/core` | 10 | 1503.5 | 89.82% | 0.0% |
| `package/js/src` | 2 | 576.26 | 50.81% | 6.2% |
| `package/js/src/css` | 4 | 405.6 | 42.81% | 2.61% |
| `package/js/lib/unpackers` | 4 | 190.72 | 42.33% | 41.39% |
| `package/js/src/unpackers` | 4 | 190.72 | 42.33% | 41.39% |
| `package/js/bin` | 3 | 33.64 | 0.0% | 0.0% |
| `package/js` | 1 | 23.4 | 42.4% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/js/lib/unpackers/myobfuscate_unpacker.js` -> **78.1356%** Exposure
- `package/js/src/unpackers/myobfuscate_unpacker.js` -> **78.1356%** Exposure
- `package/js/lib/unpackers/urlencode_unpacker.js` -> **37.7541%** Exposure
- `package/js/src/unpackers/urlencode_unpacker.js` -> **37.7541%** Exposure
- `package/js/lib/unpackers/p_a_c_k_e_r_unpacker.js` -> **27.657%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/js/lib/beautifier.js` -> **100.0%** Exposure
- `package/js/lib/cli.js` -> **100.0%** Exposure
- `package/js/lib/unpackers/p_a_c_k_e_r_unpacker.js` -> **100.0%** Exposure
- `package/js/src/cli.js` -> **100.0%** Exposure
- `package/js/src/core/directives.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/js/lib/beautifier.js` -> **0** Orphaned Functions | **6** Duplicates
- `package/js/lib/unpackers/myobfuscate_unpacker.js` -> **2** Orphaned Functions | **0** Duplicates
- `package/js/src/unpackers/myobfuscate_unpacker.js` -> **2** Orphaned Functions | **0** Duplicates
- `package/js/lib/unpackers/javascriptobfuscator_unpacker.js` -> **1** Orphaned Functions | **0** Duplicates
- `package/js/lib/unpackers/p_a_c_k_e_r_unpacker.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/js/lib/beautifier.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.268)
- **Top Global Matches:** file_cluster_4: 7.268, file_cluster_15: 11.89, file_cluster_6: 11.988
- **Magnitude:** 5715.36 | **LOC:** 6134 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.0%), Guard Balance (formerly Safety Score) (64.7%), Connectivity (formerly Api Exposure) (58.1%)
- **Documentation Coverage:** 99.6429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TagOpenParserToken` **(Many-Argument Workhorses)** (Impact: 349.9)
  * `_set_tag_position` **(Many-Argument Workhorses)** (Impact: 326.3)
  * `handle_word` **(Defensive Guards)** (Impact: 232.1)
  * `handle_operator` **(Defensive Guards)** (Impact: 120.0)
  * `beautify` **(I/O & Config Routines)** (Impact: 103.5)
    * *Intent:* /*_____________________--------------------_____________________*/
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 732 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 2651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1271`, `structural_boundaries: 676`, `args: 280`, `func_start: 251`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1187`, `dead_code: 23`, `planned_debt: 2`, `fragile_debt: 7`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 52`, `concurrency: 9`
* *Defense:* `safety: 663`, `doc: 84`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/js/src/javascript/beautifier.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.582)
- **Top Global Matches:** file_cluster_6: 7.582, file_cluster_4: 11.171, file_cluster_8: 16.002
- **Magnitude:** 1730.12 | **LOC:** 1481 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 25.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.3%), Guard Balance (formerly Safety Score) (57.6%), Concurrency Surface (formerly Concurrency) (56.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_word` **(Defensive Guards)** (Impact: 232.1)
  * `handle_operator` **(Defensive Guards)** (Impact: 120.0)
  * `handle_start_expr` **(Defensive Guards)** (Impact: 98.2)
  * `handle_start_block` **(Defensive Guards)** (Impact: 90.0)
  * `handle_token` **(Defensive Guards)** (Impact: 59.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 215 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 661
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 601`, `structural_boundaries: 142`, `args: 43`, `func_start: 43`
* *Risk/State:* `state_mutation: 231`, `dead_code: 13`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 244`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.03
  * `Choke Point (Betweenness):` 0.029577 | `Ripple Effect (Closeness):` 0.056587
  * `Imports (Out-Degree: 4):` output, token, acorn, options, tokenizer
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/js/src/html/beautifier.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.972)
- **Top Global Matches:** file_cluster_6: 7.972, file_cluster_8: 12.83, file_cluster_4: 14.074
- **Magnitude:** 1616.94 | **LOC:** 921 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 25.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TagOpenParserToken` **(Many-Argument Workhorses)** (Impact: 299.2)
  * `_set_tag_position` **(Many-Argument Workhorses)** (Impact: 270.3)
  * `_do_optional_end_element` **(Defensive Guards)** (Impact: 83.1)
  * `_print_custom_beatifier_text` **(Many-Argument Workhorses)** (Impact: 63.1)
  * `_handle_inside_tag` **(Defensive Guards)** (Impact: 58.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 169 instances
* *State Mutation (weighted view):* 542
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 89`, `args: 40`, `func_start: 40`
* *Risk/State:* `state_mutation: 204`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 110`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.03
  * `Choke Point (Betweenness):` 0.024854 | `Ripple Effect (Closeness):` 0.056587
  * `Imports (Out-Degree: 3):` output, options, tokenizer
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/js/lib/cli.js` (JAVASCRIPT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.214)
- **Top Global Matches:** file_cluster_4: 6.214, file_cluster_6: 10.622, file_cluster_12: 11.007
- **Magnitude:** 553.0 | **LOC:** 713 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 48.139; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.8%), Complexity Load (formerly Cognitive Load) (66.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkFiles` **(Defensive Guards)** (Impact: 35.5)
  * `set_file_editorconfig_opts` **(Defensive Guards)** (Impact: 31.5)
  * `getOutputType` **(Defensive Guards)** (Impact: 18.6)
  * `processInputSync` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* // main iterator, {cfg} passed as thisArg of forEach call
  * `interpret` **(Defensive Guards)** (Impact: 17.5)
    * *Intent:* // var cli = require('js-beautify/cli'); cli.interpret();
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 68 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 54`, `args: 33`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 7`, `state_mutation: 192`, `dead_code: 5`, `planned_debt: 2`
* *Architecture:* `io: 15`, `api: 2`, `import: 10`
* *Defense:* `safety: 52`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 48.139
  * `Choke Point (Betweenness):` 0.048583 | `Ripple Effect (Closeness):` 0.076923
  * `Imports (Out-Degree: 2):` package.json, index, config-chain, editorconfig, fs, glob, nopt, path
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/js/src/cli.js` (JAVASCRIPT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.21)
- **Top Global Matches:** file_cluster_4: 6.21, file_cluster_6: 10.62, file_cluster_12: 11.005
- **Magnitude:** 552.0 | **LOC:** 713 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 13.561; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.8%), Complexity Load (formerly Cognitive Load) (66.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkFiles` **(Defensive Guards)** (Impact: 35.5)
  * `set_file_editorconfig_opts` **(Defensive Guards)** (Impact: 31.5)
  * `getOutputType` **(Defensive Guards)** (Impact: 18.6)
  * `processInputSync` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* // main iterator, {cfg} passed as thisArg of forEach call
  * `interpret` **(Defensive Guards)** (Impact: 17.5)
    * *Intent:* // var cli = require('js-beautify/cli'); cli.interpret();
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 68 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 54`, `args: 33`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 7`, `state_mutation: 192`, `dead_code: 5`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 15`, `api: 1`, `import: 10`
* *Defense:* `safety: 52`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 13.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` package.json, index, config-chain, editorconfig, fs, glob, nopt, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/js/src/core/output.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.566)
- **Top Global Matches:** file_cluster_10: 5.566, file_cluster_15: 7.966, file_cluster_2: 8.476
- **Magnitude:** 486.18 | **LOC:** 420 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 31.29; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.3%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ensure_empty_line_above` **(Defensive Guards)** (Impact: 11.1)
  * `trim` **(Defensive Guards)** (Impact: 9.2)
  * `get_code` **(Defensive Guards)** (Impact: 8.3)
  * `IndentStringCache` **(State Mutators)** (Impact: 7.8)
  * `add_new_line` **(Callbacks & Closures)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 45`, `args: 39`, `func_start: 39`
* *Risk/State:* `state_mutation: 137`
* *Architecture:* `api: 10`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.098485
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/js/src/css/beautifier.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.179)
- **Top Global Matches:** file_cluster_4: 8.179, file_cluster_6: 9.574, file_cluster_9: 13.807
- **Magnitude:** 354.46 | **LOC:** 548 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 25.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Guard Balance (formerly Safety Score) (57.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `beautify` **(I/O & Config Routines)** (Impact: 103.3)
    * *Intent:* /*_____________________--------------------_____________________*/
  * `foundNestedPseudoClass` **(Defensive Guards)** (Impact: 12.2)
    * *Intent:* // Nested pseudo-class if we are insideRule // and the next special character found opens // a new b...
  * `eatString` **(Defensive Guards)** (Impact: 9.2)
  * `eatWhitespace` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* // Skips any white space in the source text from the current position. // When allowAtLeastOneNewLin...
  * `Beautifier` **(State Mutators)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 55`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 89`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 69`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.03
  * `Choke Point (Betweenness):` 0.013045 | `Ripple Effect (Closeness):` 0.056587
  * `Imports (Out-Degree: 4):` directives, inputscanner, output, options
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/js/src/core/inputscanner.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.718)
- **Top Global Matches:** file_cluster_10: 6.718, file_cluster_15: 8.306, file_cluster_16: 9.307
- **Magnitude:** 233.4 | **LOC:** 193 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 26.585; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.4%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_regexp` **(Defensive Guards)** (Impact: 12.9)
  * `read` **(Compute Cores)** (Impact: 12.7)
  * `__match` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* // This is a JavaScript only helper function (not in python) // Javascript doesn't have a match meth...
  * `test` **(Compute Cores)** (Impact: 9.2)
  * `readUntil` **(Compute Cores)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 31`, `args: 17`, `func_start: 17`
* *Risk/State:* `state_mutation: 47`, `dead_code: 1`
* *Architecture:* `api: 10`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.121557
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/js/src/core/templatablepattern.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.232)
- **Top Global Matches:** file_cluster_4: 8.232, file_cluster_6: 9.676, file_cluster_9: 13.667
- **Magnitude:** 204.08 | **LOC:** 217 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 21.159; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_read_template` **(Defensive Guards)** (Impact: 32.6)
  * `TemplatablePattern` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* // This lets templates appear anywhere we would do a readUntil // The cost is higher but it is pay t...
  * `__set_templated_pattern` **(I/O & Config Routines)** (Impact: 9.6)
  * `read` **(I/O & Config Routines)** (Impact: 8.2)
  * `read_options` **(Defensive Guards)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 19`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 48`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.159
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.080247
  * `Imports (Out-Degree: 1):` pattern
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/js/src/core/options.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.655)
- **Top Global Matches:** file_cluster_10: 7.655, file_cluster_15: 7.729, file_cluster_16: 8.956
- **Magnitude:** 165.68 | **LOC:** 194 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 92.459; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.3%), Guard Balance (formerly Safety Score) (68.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_selection_list` **(Defensive Guards)** (Impact: 12.9)
  * `_get_array` **(Defensive Guards)** (Impact: 12.7)
  * `_mergeOpts` **(Defensive Guards)** (Impact: 11.3)
    * *Intent:* // merges child options up with the parent options object // Example: obj = {a: 1, b: {a: 2}} // mer...
  * `Options` **(Many-Argument Workhorses)** (Impact: 9.1)
  * `_get_number` **(Callbacks & Closures)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 25`, `args: 11`, `func_start: 10`
* *Risk/State:* `state_mutation: 37`
* *Architecture:* `api: 4`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 92.459
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.131282
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/js/src/javascript/tokenizer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.62)
- **Top Global Matches:** file_cluster_9: 7.62, file_cluster_12: 8.321, file_cluster_15: 9.106
- **Magnitude:** 156.9 | **LOC:** 587 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 18.88; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (52.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Tokenizer` **(Compute Cores)** (Impact: 11.6)
  * `in_array` **(Defensive Guards)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 106`, `args: 20`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 113`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 109`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.88
  * `Choke Point (Betweenness):` 0.021255 | `Ripple Effect (Closeness):` 0.054656
  * `Imports (Out-Degree: 5):` directives, inputscanner, pattern, templatablepattern, tokenizer, acorn
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/js/src/core/tokenizer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.627)
- **Top Global Matches:** file_cluster_10: 5.627, file_cluster_15: 8.156, file_cluster_2: 8.522
- **Magnitude:** 109.82 | **LOC:** 141 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 21.159; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.2%), Guard Balance (formerly Safety Score) (79.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tokenize` **(I/O & Config Routines)** (Impact: 10.2)
  * `_get_next_token` **(Callbacks & Closures)** (Impact: 5.6)
  * `Tokenizer` **(State Mutators)** (Impact: 3.9)
  * `_create_token` **(Callbacks & Closures)** (Impact: 2.0)
  * `_is_closing` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 22`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.159
  * `Choke Point (Betweenness):` 0.022267 | `Ripple Effect (Closeness):` 0.080247
  * `Imports (Out-Degree: 4):` inputscanner, token, tokenstream, whitespacepattern
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/js/src/html/tokenizer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.363)
- **Top Global Matches:** file_cluster_10: 6.363, file_cluster_2: 7.173, file_cluster_15: 7.368
- **Magnitude:** 109.82 | **LOC:** 390 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 20.653; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (68.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Tokenizer` **(Defensive Guards)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 65`, `args: 18`, `func_start: 17`
* *Risk/State:* `state_mutation: 79`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 66`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.653
  * `Choke Point (Betweenness):` 0.022605 | `Ripple Effect (Closeness):` 0.054656
  * `Imports (Out-Degree: 4):` directives, pattern, templatablepattern, tokenizer
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/js/lib/unpackers/p_a_c_k_e_r_unpacker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.072)
- **Top Global Matches:** file_cluster_10: 7.072, file_cluster_15: 10.437, file_cluster_13: 10.72
- **Magnitude:** 88.9 | **LOC:** 120 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.7%), Complexity Load (formerly Cognitive Load) (62.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unpack_chunk` **(Defensive Guards)** (Impact: 6.7)
  * `get_chunks` **(Callbacks & Closures)** (Impact: 5.9)
  * `run_tests` **(Callbacks & Closures)** (Impact: 4.5)
  * `unpack` **(Callbacks & Closures)** (Impact: 3.3)
  * `detect` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 44`, `args: 22`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 46`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `safety: 4`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/js/src/unpackers/p_a_c_k_e_r_unpacker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.072)
- **Top Global Matches:** file_cluster_10: 7.072, file_cluster_15: 10.437, file_cluster_13: 10.72
- **Magnitude:** 88.9 | **LOC:** 120 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.7%), Complexity Load (formerly Cognitive Load) (62.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unpack_chunk` **(Defensive Guards)** (Impact: 6.7)
  * `get_chunks` **(Callbacks & Closures)** (Impact: 5.9)
  * `run_tests` **(Callbacks & Closures)** (Impact: 4.5)
  * `unpack` **(Callbacks & Closures)** (Impact: 3.3)
  * `detect` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 44`, `args: 22`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 46`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `safety: 4`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/js/src/core/whitespacepattern.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.789)
- **Top Global Matches:** file_cluster_10: 5.789, file_cluster_15: 7.649, file_cluster_2: 8.242
- **Magnitude:** 84.92 | **LOC:** 106 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 18.057; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.4%), Guard Balance (formerly Safety Score) (79.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__split` **(Compute Cores)** (Impact: 7.9)
  * `WhitespacePattern` **(State Mutators)** (Impact: 5.7)
  * `read` **(Callbacks & Closures)** (Impact: 4.8)
  * `__set_whitespace_patterns` **(State Mutators)** (Impact: 2.2)
  * `matching` **(Callbacks & Closures)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.057
  * `Choke Point (Betweenness):` 0.000675 | `Ripple Effect (Closeness):` 0.073906
  * `Imports (Out-Degree: 1):` pattern
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/js/src/javascript/options.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.846)
- **Top Global Matches:** file_cluster_9: 5.846, file_cluster_15: 12.202, file_cluster_16: 12.259
- **Magnitude:** 74.56 | **LOC:** 94 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 30.348; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.3%), Guard Balance (formerly Safety Score) (78.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Options` **(Defensive Guards)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 5`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 25`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.348
  * `Choke Point (Betweenness):` 0.002924 | `Ripple Effect (Closeness):` 0.069231
  * `Imports (Out-Degree: 1):` options
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/js/src/core/pattern.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.251)
- **Top Global Matches:** file_cluster_10: 5.251, file_cluster_2: 8.393, file_cluster_15: 8.575
- **Magnitude:** 69.0 | **LOC:** 95 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 54.491; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.6%), Guard Balance (formerly Safety Score) (75.9%), Connectivity (formerly Api Exposure) (60.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Pattern` **(State Mutators)** (Impact: 4.2)
  * `read` **(Callbacks & Closures)** (Impact: 3.4)
  * `until_after` **(Callbacks & Closures)** (Impact: 1.8)
  * `until` **(Callbacks & Closures)** (Impact: 1.8)
  * `starting_with` **(Callbacks & Closures)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 12`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 54.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.113174
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/js/src/core/tokenstream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.268)
- **Top Global Matches:** file_cluster_10: 5.268, file_cluster_2: 8.414, file_cluster_15: 8.544
- **Magnitude:** 67.62 | **LOC:** 79 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 18.057; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.3%), Guard Balance (formerly Safety Score) (76.9%), Connectivity (formerly Api Exposure) (50.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `peek` **(Callbacks & Closures)** (Impact: 6.1)
  * `add` **(Callbacks & Closures)** (Impact: 3.2)
  * `next` **(Callbacks & Closures)** (Impact: 2.4)
  * `TokenStream` **(State Mutators)** (Impact: 1.8)
  * `restart` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 6`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 6`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.073906
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/js/src/core/token.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.183)
- **Top Global Matches:** file_cluster_2: 6.183, file_cluster_15: 7.129, file_cluster_17: 7.492
- **Magnitude:** 45.1 | **LOC:** 55 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 23.376; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.7%), Complexity Load (formerly Cognitive Load) (54.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Token` **(Many-Argument Workhorses)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.376
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.100513
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/js/lib/unpackers/javascriptobfuscator_unpacker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.662)
- **Top Global Matches:** file_cluster_10: 6.662, file_cluster_15: 8.422, file_cluster_9: 9.041
- **Magnitude:** 44.92 | **LOC:** 133 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (40.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unpack` **(Compute Cores)** (Impact: 10.6)
  * `_fix_quotes` **(Callbacks & Closures)** (Impact: 6.3)
  * `detect` **(Callbacks & Closures)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 14`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `safety: 3`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/js/src/unpackers/javascriptobfuscator_unpacker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.662)
- **Top Global Matches:** file_cluster_10: 6.662, file_cluster_15: 8.422, file_cluster_9: 9.041
- **Magnitude:** 44.92 | **LOC:** 133 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (40.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unpack` **(Compute Cores)** (Impact: 10.6)
  * `_fix_quotes` **(Callbacks & Closures)** (Impact: 6.3)
  * `detect` **(Callbacks & Closures)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 14`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `safety: 3`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/js/src/core/directives.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.225)
- **Top Global Matches:** file_cluster_10: 6.225, file_cluster_15: 8.497, file_cluster_2: 8.609
- **Magnitude:** 37.7 | **LOC:** 63 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 26.478; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (75.4%), Guard Balance (formerly Safety Score) (59.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Directives` **(Defensive Guards)** (Impact: 5.6)
  * `get_directives` **(Callbacks & Closures)** (Impact: 5.0)
  * `readIgnored` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 5`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 3`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.115385
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/js/lib/unpackers/myobfuscate_unpacker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.196)
- **Top Global Matches:** file_cluster_10: 5.196, file_cluster_2: 8.23, file_cluster_15: 8.331
- **Magnitude:** 33.36 | **LOC:** 120 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (78.1%), Guard Balance (formerly Safety Score) (53.4%), Complexity Load (formerly Cognitive Load) (50.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `detect` **(Callbacks & Closures)** (Impact: 8.4)
  * `run_tests` **(Callbacks & Closures)** (Impact: 3.1)
  * `starts_with` **(Callbacks & Closures)** (Impact: 1.9)
  * `ends_with` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `args: 6`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 7`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/js/src/unpackers/myobfuscate_unpacker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.196)
- **Top Global Matches:** file_cluster_10: 5.196, file_cluster_2: 8.23, file_cluster_15: 8.331
- **Magnitude:** 33.36 | **LOC:** 120 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (78.1%), Guard Balance (formerly Safety Score) (53.4%), Complexity Load (formerly Cognitive Load) (50.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `detect` **(Callbacks & Closures)** (Impact: 8.4)
  * `run_tests` **(Callbacks & Closures)** (Impact: 3.1)
  * `starts_with` **(Callbacks & Closures)** (Impact: 1.9)
  * `ends_with` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `args: 6`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 7`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.561
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `package/js/src/core/options.js` (JAVASCRIPT) | Magnitude: 165.68 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 37, branch: 28, structural_boundaries: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `package/js/src/css/options.js` (JAVASCRIPT) | Magnitude: 32.4 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 9, branch: 4, structural_boundaries: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/js/src/index.js` -> **Severity: 8.501** (Bridge: 0.085 * Flux: 99.9849%)
- `package/js/index.js` -> **Severity: 7.422** (Bridge: 0.0742 * Flux: 99.9994%)
- `package/js/lib/cli.js` -> **Severity: 4.858** (Bridge: 0.0486 * Flux: 100.0%)
- `package/js/src/javascript/beautifier.js` -> **Severity: 2.958** (Bridge: 0.0296 * Flux: 100.0%)
- `package/js/src/html/beautifier.js` -> **Severity: 2.485** (Bridge: 0.0249 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/js/src/core/inputscanner.js` -> **Severity: 10.136** (Embedded: 0.1216 * Error Risk: 83.3874%)
- `package/js/src/core/options.js` -> **Severity: 8.952** (Embedded: 0.1313 * Error Risk: 68.1916%)
- `package/js/src/core/pattern.js` -> **Severity: 8.589** (Embedded: 0.1132 * Error Risk: 75.8902%)
- `package/js/src/core/output.js` -> **Severity: 8.376** (Embedded: 0.0985 * Error Risk: 85.048%)
- `package/js/src/core/token.js` -> **Severity: 7.404** (Embedded: 0.1005 * Error Risk: 73.6639%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/js/src/core/options.js` -> **Severity: 9245.9** (Blast Radius: 92.459 * Doc Risk: 100.0%)
- `package/js/src/core/pattern.js` -> **Severity: 5449.1** (Blast Radius: 54.491 * Doc Risk: 100.0%)
- `package/js/lib/cli.js` -> **Severity: 4813.9** (Blast Radius: 48.139 * Doc Risk: 100.0%)
- `package/js/src/index.js` -> **Severity: 4737.7** (Blast Radius: 47.377 * Doc Risk: 100.0%)
- `package/js/src/html/options.js` -> **Severity: 3212.1** (Blast Radius: 32.121 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1441 call pairs -- scoped 14.2%, unique 0.0%, ambiguous 0.3%, external 85.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 1441 | 14.2% | 0.0% | 0.3% | 85.5% |

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
