# ARCHITECTURAL_BRIEF: CobolCraft
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/meyfa/CobolCraft` |
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
- **Scope:** 277 analyzed artifact(s), 23551 LOC.
- **Load-bearing artifact:** `src/_copybooks/state/DD-PLAYERS.cpy` -- 57 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `cpp/cobolcraft_util.cpp` -- pulls in 15 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `codegen/generators/blocks_loot_table.cob` at magnitude 800.04 (structural weight, not risk).
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
| Total Artifacts | 282 |
| Analyzed Artifacts (Scanned) | 277 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 23551 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 98.2% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5273 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2845 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 35.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0496 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 268 | 22845 | 96.8% |
| YAML | 3 | 102 | 1.1% |
| CPP | 2 | 475 | 0.7% |
| DOCKERFILE | 1 | 23 | 0.4% |
| MAKEFILE | 1 | 100 | 0.4% |
| MARKDOWN | 1 | 0 | 0.4% |
| JSON | 1 | 6 | 0.4% |

## 4.1 SOURCE ENCODINGS
All 277 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 31%, Data / Markup / Trivial 25%, Compute Cores Files 10%, Parameter Forwarders Files 10%, Declarative / Non-Code 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 276 | 99.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 170 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 88.5 | 20.5 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.1 | 46.0 | 53.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 6.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 28.4 | 3.2 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 51.6 | 50.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.7 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 13.7 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 44 | 18 | 0 | `src/loot-tables.cob` |
| cleanup | 24 | 11 | 0 | `Makefile` |
| guards | 8 | 5 | 0 | `cpp/cobolcraft_util.cpp` |
| danger | 1427 | 192 | 13 | `src/encoding/nbt-encode.cob` |
| concurrency | 2 | 2 | 0 | `.github/workflows/publish.yml` |
| connectivity | 565 | 173 | 6 | `codegen/generators/blocks_loot_table.cob` |
| io | 73 | 14 | 0 | `Makefile` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2659 | 195 | 22 | `src/server.cob` |
| time | 3 | 2 | 0 | `cpp/cobolcraft_util.cpp` |
| serialization | 84 | 28 | 0 | `codegen/generators/blocks_loot_table.cob` |
| regex | 1059 | 126 | 4 | `tests/encoding/encode.test.cob` |
| events | 1 | 1 | 0 | `cpp/cobolcraft_util.cpp` |
| tests | 368 | 29 | 1 | `tests/encoding/encode.test.cob` |
| docs | 27 | 4 | 0 | `cpp/cobolcraft_util.h` |
| debt | 348 | 98 | 3 | `src/datapack.cob` |
| mutation | 4527 | 198 | 50 | `src/world/chunk-io.cob` |
| dead_code | 168 | 15 | 0 | `tests/encoding/json-parse.test.cob` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 88 | 25 | 0 | `src/world/blocks.cob` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 23)
- `cpp/cobolcraft_util.cpp` (Hits: 13)
- `Dockerfile` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DD-PLAYERS.cpy** (`src/_copybooks/state/DD-PLAYERS.cpy`) — 57 inbound connections
2. **registries.cob** (`src/registries.cob`) — 54 inbound connections
3. **encode.cob** (`src/encoding/encode.cob`) — 51 inbound connections
4. **packets.cob** (`src/packets.cob`) — 50 inbound connections
5. **PROC-PACKET-INIT.cpy** (`src/_copybooks/procedures/PROC-PACKET-INIT.cpy`) — 47 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cobolcraft_util.cpp** (`cpp/cobolcraft_util.cpp`) — 15 outbound dependencies
2. **entities.cob** (`src/world/entities.cob`) — 9 outbound dependencies
3. **sign.cob** (`src/blockentities/sign.cob`) — 8 outbound dependencies
4. **client-chunks.cob** (`src/client-chunks.cob`) — 8 outbound dependencies
5. **item.cob** (`src/entities/item.cob`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `COMPONENTS-LENGTHOF` **(Many-Argument Workhorses)** (@ `src/components.cob`) -> Impact: **270.9** | LOC: 377
- `PLAYERS-LOADPLAYER` **(Many-Argument Workhorses)** (@ `src/players/player-io.cob`) -> Impact: **103.0** | LOC: 180
- `PARSE-RECIPE-SHAPED` **(Many-Argument Workhorses)** (@ `src/parsers/recipe/shaped.cob`) -> Impact: **93.0** | LOC: 139
- `CALLBACK-USE` **(Many-Argument Workhorses)** (@ `src/items/door.cob`) -> Impact: **83.4** | LOC: 133
- `JSONPARSE-SKIPVALUE` **(Many-Argument Workhorses)** (@ `src/encoding/json-parse.cob`) -> Impact: **70.5** | LOC: 130
- `DATAPACK-LOADRECIPE` **(Many-Argument Workhorses)** (@ `src/datapack.cob`) -> Impact: **63.2** | LOC: 104
- `DECODESECTIONBLOCKSTATES` **(Many-Argument Workhorses)** (@ `src/world/chunk-io.cob`) -> Impact: **62.7** | LOC: 127
- `SERVERPROPERTIES-DESERIALIZE` **(Many-Argument Workhorses)** (@ `src/server-properties.cob`) -> Impact: **56.8** | LOC: 96
- `REGION-WRITECHUNKDATA` **(Many-Argument Workhorses)** (@ `src/region.cob`) -> Impact: **56.3** | LOC: 120
- `CALLBACK-USE` **(Many-Argument Workhorses)** (@ `src/items/slab.cob`) -> Impact: **54.4** | LOC: 83

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 17 | 3522.2 | 49.89% | 14.6% |
| `src/encoding` | 8 | 2265.26 | 72.23% | 3.53% |
| `tests/encoding` | 8 | 1316.16 | 4.38% | 0.0% |
| `codegen/generators` | 4 | 1114.78 | 41.49% | 6.38% |
| `src/items` | 14 | 1075.3 | 51.28% | 16.83% |
| `src/world` | 6 | 879.78 | 60.38% | 4.94% |
| `src/packets/clientbound/play` | 37 | 670.84 | 7.97% | 8.55% |
| `src/inventory` | 3 | 497.84 | 64.83% | 18.2% |
| `cpp` | 2 | 489.7 | 36.64% | 43.63% |
| `src/players` | 2 | 488.78 | 64.42% | 12.84% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/packets/serverbound/play/use-item.cob` -> **99.9447%** Exposure
- `cpp/cobolcraft_util.cpp` -> **87.267%** Exposure
- `src/server.cob` -> **86.3682%** Exposure
- `src/datapack.cob` -> **83.5306%** Exposure
- `src/blocks/sign.cob` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `codegen/common/data.cob` -> **100.0%** Exposure
- `codegen/common/optimizer.cob` -> **100.0%** Exposure
- `codegen/common/templates.cob` -> **100.0%** Exposure
- `codegen/common/util.cob` -> **100.0%** Exposure
- `src/client-chunks.cob` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/encoding/json-parse.test.cob` -> **26** Orphaned Functions | **0** Duplicates
- `tests/encoding/encode.test.cob` -> **18** Orphaned Functions | **6** Duplicates
- `tests/encoding/nbt-decode.test.cob` -> **20** Orphaned Functions | **0** Duplicates
- `tests/encoding/nbt-encode.test.cob` -> **20** Orphaned Functions | **0** Duplicates
- `cpp/cobolcraft_util.cpp` -> **20** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `555` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `codegen/generators/blocks_loot_table.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.235)
- **Top Global Matches:** file_cluster_4: 9.235, file_cluster_12: 10.172, file_cluster_7: 11.597
- **Magnitude:** 800.04 | **LOC:** 1527 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 1.761; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.5%), Complexity Load (formerly Cognitive Load) (47.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CG-BLOCKSLOOTTABLE-CONDITION` **(Compute Cores)** (Impact: 48.3)
  * `GenerateFunctions` **(Compute Cores)** (Impact: 38.1)
  * `CG-BLOCKSLOOTTABLE-NUMBER` **(Compute Cores)** (Impact: 35.1)
  * `CG-BLOCKSLOOTTABLE-MAIN` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `CG-BLOCKSLOOTTABLE-ENTRYITEM` **(Many-Argument Workhorses)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 308`, `args: 512`, `func_start: 21`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 125`, `planned_debt: 17`
* *Architecture:* `api: 41`, `import: 58`
* *Defense:* `test: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.761
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.003623
  * `Imports (Out-Degree: 12):` ASSERT, ASSERT-FAILED, DD-CODEGEN-DIR-LIST, DD-CODEGEN-JSON, DD-CODEGEN-TEMPLATE
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/encoding/json-parse.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.22)
- **Top Global Matches:** file_cluster_6: 8.22, file_cluster_4: 10.225, file_cluster_12: 15.882
- **Magnitude:** 587.34 | **LOC:** 642 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **1**; blast radius 7.271; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.1%), Complexity Load (formerly Cognitive Load) (65.7%), Connectivity (formerly Api Exposure) (8.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `JSONPARSE-SKIPVALUE` **(Many-Argument Workhorses)** (Impact: 70.5)
  * `JSONPARSE-STRING` **(Many-Argument Workhorses)** (Impact: 50.2)
  * `JSONPARSE-FLOAT` **(Many-Argument Workhorses)** (Impact: 22.4)
  * `JSONPARSE-BOOLEAN` **(Many-Argument Workhorses)** (Impact: 19.3)
  * `JSONPARSE-FINDVALUE` **(Many-Argument Workhorses)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 138`, `args: 94`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 123`
* *Architecture:* `api: 14`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.271
  * `Choke Point (Betweenness):` 0.002817 | `Ripple Effect (Closeness):` 0.180104
  * `Imports (Out-Degree: 2):` PROC-SKIP-WHITESPACE
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/encoding/nbt-decode.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.675)
- **Top Global Matches:** file_cluster_12: 9.675, file_cluster_4: 9.89, file_cluster_7: 10.818
- **Magnitude:** 539.04 | **LOC:** 784 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **2**; blast radius 5.136; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.7%), Complexity Load (formerly Cognitive Load) (72.2%), Debt Markers (formerly Tech Debt) (19.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NBTDECODE-SKIPVALUE` **(Many-Argument Workhorses)** (Impact: 48.3)
  * `NBTDECODE-LONG` **(Many-Argument Workhorses)** (Impact: 32.4)
  * `NBTDECODE-LIST` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `NBTDECODE-FLOAT` **(Many-Argument Workhorses)** (Impact: 21.7)
  * `NBTDECODE-DOUBLE` **(Many-Argument Workhorses)** (Impact: 21.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 149`, `args: 168`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 92`, `planned_debt: 12`
* *Architecture:* `api: 20`, `import: 22`
* *Defense:* `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.136
  * `Choke Point (Betweenness):` 0.000682 | `Ripple Effect (Closeness):` 0.159523
  * `Imports (Out-Degree: 3):` ASSERT, DD-NBT-DECODER
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/region.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.019)
- **Top Global Matches:** file_cluster_6: 6.019, file_cluster_4: 11.816, file_cluster_8: 13.695
- **Magnitude:** 529.9 | **LOC:** 637 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 2.287; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.3%), Complexity Load (formerly Cognitive Load) (62.8%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `REGION-WRITECHUNKDATA` **(Many-Argument Workhorses)** (Impact: 56.3)
  * `REGION-READCHUNKDATA` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `REGION-OPEN` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `OpenFile` **(I/O & Config Routines)** (Impact: 19.9)
  * `REGION-CLOSELEASTRECENTLYUSED` **(Compute Cores)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 103 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 99`, `args: 167`, `func_start: 1`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 125`
* *Architecture:* `api: 9`, `import: 14`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.287
  * `Choke Point (Betweenness):` 0.003151 | `Ripple Effect (Closeness):` 0.152394
  * `Imports (Out-Degree: 5):` DD-REGION-FILE-REF, DD-REGION-FILES, DD-SERVER-PROPERTIES
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `cpp/cobolcraft_util.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.156)
- **Top Global Matches:** file_cluster_9: 6.156, file_cluster_15: 7.638, file_cluster_16: 8.857
- **Magnitude:** 474.24 | **LOC:** 558 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.592; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (87.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SocketRead` **(Compute Cores)** (Impact: 21.5)
  * `ZlibCompress` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `ZlibDecompress` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `GzipCompress` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `GzipDecompress` **(Many-Argument Workhorses)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 86`, `args: 26`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 79`, `unreferenced_by_name: 20`
* *Architecture:* `io: 13`, `import: 15`
* *Defense:* `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.592
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` chrono, cobolcraft_util.h, csignal, cstring, dirent.h, errno.h, fcntl.h, in.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/encoding/nbt-encode.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.782)
- **Top Global Matches:** file_cluster_7: 7.782, file_cluster_14: 9.464, file_cluster_12: 9.846
- **Magnitude:** 453.2 | **LOC:** 607 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **2**; blast radius 4.173; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.1%), Complexity Load (formerly Cognitive Load) (66.9%), Connectivity (formerly Api Exposure) (9.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NBTENCODE-BYTE` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `NBTENCODE-INT` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `NBTENCODE-LONG` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `NBTENCODE-BYTEARRAY` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `NBTENCODE-INTARRAY` **(Many-Argument Workhorses)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 96`, `args: 172`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 98`
* *Architecture:* `io: 2`, `api: 18`, `import: 20`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.000386 | `Ripple Effect (Closeness):` 0.153803
  * `Imports (Out-Degree: 3):` ASSERT, DD-NBT-ENCODER
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/datapack.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.613)
- **Top Global Matches:** file_cluster_6: 9.613, file_cluster_4: 14.557, file_cluster_8: 15.318
- **Magnitude:** 423.2 | **LOC:** 644 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.68; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (83.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DATAPACK-LOADRECIPE` **(Many-Argument Workhorses)** (Impact: 63.2)
  * `DATAPACK-LOADTAGDIR` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `DATAPACK-EXPANDTAGREFS` **(Compute Cores)** (Impact: 25.9)
  * `DATAPACK-LOADTAGS` **(Many-Argument Workhorses)** (Impact: 24.7)
  * `DATAPACK-LOADTAGFILE` **(Many-Argument Workhorses)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 141`, `args: 151`, `func_start: 3`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 72`, `planned_debt: 40`
* *Architecture:* `api: 8`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.68
  * `Choke Point (Betweenness):` 0.007627 | `Ripple Effect (Closeness):` 0.119506
  * `Imports (Out-Degree: 8):` DD-RECIPES, DD-TAGS
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/components.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.392)
- **Top Global Matches:** file_cluster_11: 8.392, file_cluster_4: 8.543, file_cluster_15: 8.961
- **Magnitude:** 352.12 | **LOC:** 585 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 5.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (30.0%), Complexity Load (formerly Cognitive Load) (27.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `COMPONENTS-LENGTHOF` **(Many-Argument Workhorses)** (Impact: 270.9)
  * `BlockPredicate` **(Interface Declarations)** (Impact: 8.2)
  * `Slot` **(Interface Declarations)** (Impact: 4.9)
  * `IdSet` **(Interface Declarations)** (Impact: 4.5)
  * `FireworkExplosion` **(Interface Declarations)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 217`, `args: 216`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `planned_debt: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.573
  * `Choke Point (Betweenness):` 0.000589 | `Ripple Effect (Closeness):` 0.139798
  * `Imports (Out-Degree: 3):` DD-NBT-DECODER
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/server.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 9.18)
- **Top Global Matches:** file_cluster_15: 9.18, file_cluster_11: 9.211, file_cluster_16: 10.373
- **Magnitude:** 343.26 | **LOC:** 934 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **8**; blast radius 9.283; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (86.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ServerLoop` **(I/O & Config Routines)** (Impact: 29.4)
  * `SERVER-SPAWNPLAYER` **(Compute Cores)** (Impact: 16.1)
  * `SERVER-DISCONNECTCLIENT` **(Compute Cores)** (Impact: 15.0)
  * `ReceivePacket` **(I/O & Config Routines)** (Impact: 14.5)
  * `NetworkRead` **(I/O & Config Routines)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 45 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 122`, `args: 202`, `func_start: 27`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 82`, `planned_debt: 5`, `unreferenced_by_name: 17`
* *Architecture:* `io: 4`, `api: 3`, `import: 30`
* *Defense:* `test: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.283
  * `Choke Point (Betweenness):` 0.240599 | `Ripple Effect (Closeness):` 0.1589
  * `Imports (Out-Degree: 89):` ASSERT, ASSERT-FAILED, DD-CLIENT-STATES, DD-CLIENTS, DD-PACKET-DIRECTIONS, DD-PLAYERS, DD-SERVER-PROPERTIES, DD-VERSION
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/blocks.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.561)
- **Top Global Matches:** file_cluster_4: 7.561, file_cluster_12: 9.242, file_cluster_15: 10.383
- **Magnitude:** 319.84 | **LOC:** 615 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **2**; blast radius 10.113; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.0%), Complexity Load (formerly Cognitive Load) (42.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BLOCKS-PARSE-BLOCK` **(Many-Argument Workhorses)** (Impact: 50.3)
  * `BLOCKS-PARSE-STATE` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `BLOCKS-FROMDESCRIPTION` **(Compute Cores)** (Impact: 18.8)
  * `BLOCKS-COMPAREBLOCKTYPE` **(Compute Cores)** (Impact: 15.0)
  * `BLOCKS-PARSE` **(Many-Argument Workhorses)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 153`, `args: 165`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 51`, `planned_debt: 2`
* *Architecture:* `api: 17`, `import: 17`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.113
  * `Choke Point (Betweenness):` 0.004928 | `Ripple Effect (Closeness):` 0.19978
  * `Imports (Out-Degree: 4):` DD-BLOCK-STATE, DD-BLOCKS
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `tests/encoding/json-parse.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.73)
- **Top Global Matches:** file_cluster_11: 6.73, file_cluster_2: 8.082, file_cluster_13: 8.284
- **Magnitude:** 280.36 | **LOC:** 651 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 4.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST-JSONPARSE` **(I/O & Config Routines)** (Impact: 1.8)
  * `EscapedUnicodeChar` **(Interface Declarations)** (Impact: 1.5)
  * `Simple` **(State Mutators)** (Impact: 1.4)
  * `Missing` **(Interface Declarations)** (Impact: 1.4)
  * `Simple` **(State Mutators)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 68`, `args: 195`, `func_start: 57`, `class_start: 14`
* *Risk/State:* `state_mutation: 173`, `planned_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `import: 128`
* *Defense:* `test: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.128
  * `Choke Point (Betweenness):` 0.000446 | `Ripple Effect (Closeness):` 0.077017
  * `Imports (Out-Degree: 5):` TEST-ASSERT, TEST-CASE, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parsers/recipe/shaped.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.132)
- **Top Global Matches:** file_cluster_8: 11.132, file_cluster_3: 13.465, file_cluster_6: 23.574
- **Magnitude:** 278.16 | **LOC:** 360 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.77; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.3%), Guard Balance (formerly Safety Score) (71.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PARSE-RECIPE-SHAPED` **(Many-Argument Workhorses)** (Impact: 93.0)
  * `ParseKey` **(Compute Cores)** (Impact: 26.5)
  * `ParsePattern` **(I/O & Config Routines)** (Impact: 10.0)
  * `MirrorShapedRecipe` **(I/O & Config Routines)** (Impact: 1.5)
  * `MirrorComplexRecipe` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 61`, `args: 66`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 61`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.77
  * `Choke Point (Betweenness):` 0.000856 | `Ripple Effect (Closeness):` 0.096211
  * `Imports (Out-Degree: 6):` DD-RECIPES, DD-TAGS
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/encoding/nbt-decode.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.232)
- **Top Global Matches:** file_cluster_11: 7.232, file_cluster_15: 8.599, file_cluster_2: 8.81
- **Magnitude:** 274.94 | **LOC:** 625 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 4.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.8%), Complexity Load (formerly Cognitive Load) (35.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NotAtEnd` **(I/O & Config Routines)** (Impact: 2.5)
  * `AtEnd` **(I/O & Config Routines)** (Impact: 2.4)
  * `TEST-NBTDECODE` **(I/O & Config Routines)** (Impact: 1.9)
  * `Basic` **(Interface Declarations)** (Impact: 1.6)
  * `WithinCompound` **(Interface Declarations)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 73`, `args: 153`, `func_start: 51`, `class_start: 15`
* *Risk/State:* `state_mutation: 157`, `unreferenced_by_name: 20`
* *Architecture:* `import: 131`
* *Defense:* `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.128
  * `Choke Point (Betweenness):` 0.000471 | `Ripple Effect (Closeness):` 0.077017
  * `Imports (Out-Degree: 6):` DD-NBT-DECODER, TEST-ASSERT, TEST-CASE, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/encoding/encode.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.093)
- **Top Global Matches:** file_cluster_11: 7.093, file_cluster_2: 8.299, file_cluster_13: 8.525
- **Magnitude:** 250.5 | **LOC:** 654 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 4.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST-ENCODE` **(I/O & Config Routines)** (Impact: 1.8)
  * `Simple` **(I/O & Config Routines)** (Impact: 1.6)
  * `HelloWorld` **(Interface Declarations)** (Impact: 1.5)
  * `WikiVgExample` **(Interface Declarations)** (Impact: 1.5)
  * `Empty` **(I/O & Config Routines)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 68`, `args: 182`, `func_start: 69`, `class_start: 14`
* *Risk/State:* `state_mutation: 133`, `duplicate_logic: 6`, `unreferenced_by_name: 18`
* *Architecture:* `import: 153`
* *Defense:* `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.128
  * `Choke Point (Betweenness):` 0.002158 | `Ripple Effect (Closeness):` 0.077017
  * `Imports (Out-Degree: 7):` DD-INVENTORY-SLOT, TEST-ASSERT, TEST-CASE, TEST-SKIP, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/world/entities.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.379)
- **Top Global Matches:** file_cluster_15: 6.379, file_cluster_12: 7.81, file_cluster_16: 8.271
- **Magnitude:** 249.9 | **LOC:** 450 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **9**; blast radius 5.975; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%), Complexity Load (formerly Cognitive Load) (59.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WORLD-REMOVEENTITY` **(Compute Cores)** (Impact: 16.5)
  * `WORLD-UPDATEENTITYCHUNK` **(Compute Cores)** (Impact: 14.3)
  * `WORLD-DROPITEM` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `WORLD-SPAWNENTITY` **(Compute Cores)** (Impact: 8.9)
  * `WORLD-DROPITEM-FROMPLAYER` **(Compute Cores)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 65`, `args: 64`, `func_start: 1`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 80`, `planned_debt: 3`
* *Architecture:* `api: 8`, `import: 25`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.975
  * `Choke Point (Betweenness):` 0.065801 | `Ripple Effect (Closeness):` 0.139278
  * `Imports (Out-Degree: 17):` DD-CHUNK-ENTITY, DD-CHUNK-REF, DD-CLIENT-STATES, DD-CLIENTS, DD-ENTITY, DD-INVENTORY-SLOT, DD-PLAYERS, DD-SERVER-PROPERTIES...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/players/player-io.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.549)
- **Top Global Matches:** file_cluster_8: 8.549, file_cluster_6: 18.153, file_cluster_3: 20.528
- **Magnitude:** 247.1 | **LOC:** 376 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 1.839; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (66.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PLAYERS-LOADPLAYER` **(Many-Argument Workhorses)** (Impact: 103.0)
  * `PLAYERS-SAVEPLAYER` **(Many-Argument Workhorses)** (Impact: 31.4)
  * `PLAYERS-PLAYERFILENAME` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 37`, `args: 227`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 44`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.000668 | `Ripple Effect (Closeness):` 0.099554
  * `Imports (Out-Degree: 10):` DD-INVENTORY-SLOT, DD-NBT-DECODER, DD-NBT-ENCODER, DD-PLAYERS, DD-SERVER-PROPERTIES
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/players/players.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.782)
- **Top Global Matches:** file_cluster_12: 6.782, file_cluster_15: 7.776, file_cluster_16: 9.165
- **Magnitude:** 241.68 | **LOC:** 440 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **4**; blast radius 3.486; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.8%), Complexity Load (formerly Cognitive Load) (61.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PLAYERS-HANDLEMOVE` **(Many-Argument Workhorses)** (Impact: 29.8)
  * `PLAYERS-DAMAGE` **(Many-Argument Workhorses)** (Impact: 22.4)
  * `PLAYERS-CONNECT` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `PLAYERS-FINDCONNECTEDBYUUID` **(Compute Cores)** (Impact: 7.4)
  * `BuildDeathMessage` **(I/O & Config Routines)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 72`, `args: 48`, `func_start: 6`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 51`, `planned_debt: 5`
* *Architecture:* `api: 6`, `import: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.486
  * `Choke Point (Betweenness):` 0.016189 | `Ripple Effect (Closeness):` 0.125047
  * `Imports (Out-Degree: 12):` DD-CLIENT-STATES, DD-CLIENTS, DD-PLAYERS, DD-SERVER-PROPERTIES
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/callbacks.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.327)
- **Top Global Matches:** file_cluster_15: 5.327, file_cluster_2: 7.41, file_cluster_12: 7.551
- **Magnitude:** 235.36 | **LOC:** 563 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **41** in-repo importer(s); it depends on **1**; blast radius 10.944; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.4%), Complexity Load (formerly Cognitive Load) (34.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GETCALLBACK-BLOCKDESTROY` **(Compute Cores)** (Impact: 3.8)
  * `GETCALLBACK-BLOCKINTERACT` **(Compute Cores)** (Impact: 3.8)
  * `GETCALLBACK-BLOCKFACE` **(Compute Cores)** (Impact: 3.8)
  * `GETCALLBACK-BLOCKREPLACEABLE` **(Compute Cores)** (Impact: 3.8)
  * `GETCALLBACK-BLOCKITEM` **(Compute Cores)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 189`, `args: 56`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 50`
* *Architecture:* `api: 28`, `import: 29`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.944
  * `Choke Point (Betweenness):` 0.001055 | `Ripple Effect (Closeness):` 0.196523
  * `Imports (Out-Degree: 2):` DD-CALLBACKS
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `src/world/chunks.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.92)
- **Top Global Matches:** file_cluster_9: 5.92, file_cluster_15: 8.236, file_cluster_16: 8.77
- **Magnitude:** 230.82 | **LOC:** 330 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 2.633; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.8%), Complexity Load (formerly Cognitive Load) (65.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WORLD-ALLOCATECHUNK` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `WORLD-UNLOADCHUNKS` **(Compute Cores)** (Impact: 19.4)
  * `WORLD-GENERATECHUNK` **(Compute Cores)** (Impact: 13.9)
  * `WORLD-ENSURESPAWNCHUNKS` **(Compute Cores)** (Impact: 11.0)
  * `WORLD-FREECHUNK` **(Compute Cores)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 40 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 65`, `args: 40`, `class_start: 7`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `api: 7`, `import: 16`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.633
  * `Choke Point (Betweenness):` 0.006889 | `Ripple Effect (Closeness):` 0.138607
  * `Imports (Out-Degree: 8):` DD-CHUNK-ENTITY, DD-CHUNK-REF, DD-PLAYERS, DD-SERVER-PROPERTIES, DD-WORLD
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/inventory/inventory.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.324)
- **Top Global Matches:** file_cluster_4: 6.324, file_cluster_15: 10.878, file_cluster_6: 10.902
- **Magnitude:** 226.4 | **LOC:** 377 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **4**; blast radius 3.402; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.7%), Guard Balance (formerly Safety Score) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `INVENTORY-UPDATECRAFTINGOUTPUT` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `MatchShapedRecipes` **(I/O & Config Routines)** (Impact: 19.8)
  * `INVENTORY-PICKITEM` **(Compute Cores)** (Impact: 19.6)
  * `INVENTORY-STOREITEM` **(Compute Cores)** (Impact: 16.6)
  * `INVENTORY-COMPAREITEMS` **(Many-Argument Workhorses)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 75`, `args: 26`, `func_start: 6`, `class_start: 6`
* *Risk/State:* `state_mutation: 50`, `dead_code: 2`, `planned_debt: 4`
* *Architecture:* `api: 6`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.402
  * `Choke Point (Betweenness):` 0.002863 | `Ripple Effect (Closeness):` 0.137942
  * `Imports (Out-Degree: 7):` DD-CLIENTS, DD-INVENTORY-SLOT, DD-PLAYERS, DD-RECIPES
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/packets.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.93)
- **Top Global Matches:** file_cluster_12: 6.93, file_cluster_7: 9.286, file_cluster_15: 9.617
- **Magnitude:** 217.56 | **LOC:** 319 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **50** in-repo importer(s); it depends on **7**; blast radius 36.025; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%), Complexity Load (formerly Cognitive Load) (64.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PACKETS-REGISTER` **(Many-Argument Workhorses)** (Impact: 29.2)
  * `REGISTERPACKETHANDLER` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `PACKETS-GETREFERENCE` **(Many-Argument Workhorses)** (Impact: 14.4)
  * `HANDLEPACKET` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `PACKETS-GETID` **(Compute Cores)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 62`, `args: 52`, `func_start: 1`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 47`
* *Architecture:* `api: 8`, `import: 21`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.025
  * `Choke Point (Betweenness):` 0.224225 | `Ripple Effect (Closeness):` 0.222092
  * `Imports (Out-Degree: 9):` ASSERT, ASSERT-FAILED, DD-CLIENT-STATES, DD-CLIENTS, DD-PACKET-DIRECTIONS, DD-PACKET-HANDLERS, DD-PACKET-IDS
  * `Imported By (In-Degree: 50):` (Excluded from Brief to save tokens)

### `src/items/door.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.027)
- **Top Global Matches:** file_cluster_3: 7.027, file_cluster_8: 20.667, file_cluster_6: 33.504
- **Magnitude:** 212.48 | **LOC:** 208 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.68; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.5%), Complexity Load (formerly Cognitive Load) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CALLBACK-USE` **(Many-Argument Workhorses)** (Impact: 83.4)
  * `REGISTERITEM-DOOR` **(I/O & Config Routines)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 14`, `args: 46`, `class_start: 2`
* *Risk/State:* `state_mutation: 45`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.68
  * `Choke Point (Betweenness):` 0.000509 | `Ripple Effect (Closeness):` 0.118847
  * `Imports (Out-Degree: 8):` DD-BLOCK-STATE, DD-CALLBACK-ITEM-USE, DD-PLAYERS
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/client-chunks.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.63)
- **Top Global Matches:** file_cluster_15: 6.63, file_cluster_9: 8.046, file_cluster_11: 8.215
- **Magnitude:** 211.82 | **LOC:** 312 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.68; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.5%), Complexity Load (formerly Cognitive Load) (65.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SENDCHUNKS` **(Compute Cores)** (Impact: 24.1)
  * `ENQUEUESURROUNDINGCHUNKS` **(Compute Cores)** (Impact: 14.1)
  * `ENQUEUECHUNK` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `PROCESSCHUNKQUEUE` **(Compute Cores)** (Impact: 8.5)
  * `PROCESSCLIENTCHUNKS` **(I/O & Config Routines)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 60`, `args: 39`, `func_start: 1`, `class_start: 7`
* *Risk/State:* `state_mutation: 51`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 17`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.68
  * `Choke Point (Betweenness):` 0.007854 | `Ripple Effect (Closeness):` 0.118602
  * `Imports (Out-Degree: 12):` ASSERT, DD-CHUNK-ENTITY, DD-CHUNK-REF, DD-CLIENT-STATES, DD-CLIENTS, DD-PLAYERS, DD-SERVER-PROPERTIES, DD-WORLD
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/encoding/decode.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.763)
- **Top Global Matches:** file_cluster_11: 6.763, file_cluster_2: 8.138, file_cluster_13: 8.29
- **Magnitude:** 208.88 | **LOC:** 579 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 4.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST-DECODE` **(I/O & Config Routines)** (Impact: 1.8)
  * `NegativeMax` **(I/O & Config Routines)** (Impact: 1.6)
  * `ByteNegative128` **(Interface Declarations)** (Impact: 1.4)
  * `ShortMax` **(Interface Declarations)** (Impact: 1.4)
  * `ShortMin` **(Interface Declarations)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 68`, `args: 164`, `func_start: 54`, `class_start: 14`
* *Risk/State:* `state_mutation: 111`, `unreferenced_by_name: 15`
* *Architecture:* `import: 123`
* *Defense:* `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.128
  * `Choke Point (Betweenness):` 0.000529 | `Ripple Effect (Closeness):` 0.077017
  * `Imports (Out-Degree: 6):` DD-INVENTORY-SLOT, TEST-ASSERT, TEST-CASE, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/encoding/nbt-encode.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.859)
- **Top Global Matches:** file_cluster_7: 7.859, file_cluster_12: 8.271, file_cluster_5: 10.196
- **Magnitude:** 201.84 | **LOC:** 551 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 4.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (65.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST-NBTENCODE` **(I/O & Config Routines)** (Impact: 1.9)
  * `NamedString` **(I/O & Config Routines)** (Impact: 1.6)
  * `NamedByte` **(Interface Declarations)** (Impact: 1.5)
  * `NamedShort` **(Interface Declarations)** (Impact: 1.5)
  * `NamedInt` **(Interface Declarations)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 78`, `args: 125`, `func_start: 37`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 122`, `unreferenced_by_name: 20`
* *Architecture:* `import: 105`
* *Defense:* `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.128
  * `Choke Point (Betweenness):` 0.000503 | `Ripple Effect (Closeness):` 0.077017
  * `Imports (Out-Degree: 6):` DD-NBT-ENCODER, TEST-ASSERT, TEST-CASE, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/components.cob` (COBOL) | Magnitude: 352.12 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 511, structural_boundaries: 217, args: 216, branch: 144

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/commands/time.cob` (COBOL) | Magnitude: 50.74 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 56, args: 22, state_mutation: 14, ipc_rpc_bridges: 14
- `src/blockentities/sign.cob` (COBOL) | Magnitude: 114.4 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 172, args: 106, structural_boundaries: 44, ipc_rpc_bridges: 39
- `codegen/templates/items/main.tpl.cob` (COBOL) | Magnitude: 7.72 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 11, state_mutation: 3, args: 2
- `src/packets/clientbound/play/system-chat.cob` (COBOL) | Magnitude: 43.08 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 42, state_mutation: 24, args: 20, structural_boundaries: 6
- `src/packets/clientbound/login/login-success.cob` (COBOL) | Magnitude: 11.72 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 19, args: 11, state_mutation: 7, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/packets/clientbound/play/respawn.cob` (COBOL) | Magnitude: 25.02 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 19, args: 16, structural_boundaries: 6
- `src/packets/clientbound/play/login-play.cob` (COBOL) | Magnitude: 38.22 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 54, args: 39, state_mutation: 29, ipc_rpc_bridges: 11
- `src/server.cob` (COBOL) | Magnitude: 343.26 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 607, args: 202, ipc_rpc_bridges: 181, structural_boundaries: 122
- `src/packets/clientbound/play/block-update.cob` (COBOL) | Magnitude: 6.28 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, args: 13, structural_boundaries: 6, ipc_rpc_bridges: 3
- `src/packets/clientbound/play/entity-animation.cob` (COBOL) | Magnitude: 8.24 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, args: 10, structural_boundaries: 6, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/registries.cob` (COBOL) | Magnitude: 68.18 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 61, args: 19, state_mutation: 15
- `src/loot-tables.cob` (COBOL) | Magnitude: 156.08 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 62, args: 32, state_mutation: 26

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/encoding/decode.cob` -> **Simon Sobisch** (100.0% isolated ownership) | Magnitude: 194.92
- `src/world/world.cob` -> **Simon Sobisch** (100.0% isolated ownership) | Magnitude: 122.06

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/server.cob` -> **Severity: 24.05** (Bridge: 0.2406 * Flux: 99.96%)
- `src/packets.cob` -> **Severity: 22.422** (Bridge: 0.2242 * Flux: 100.0%)
- `src/world/entities.cob` -> **Severity: 6.58** (Bridge: 0.0658 * Flux: 100.0%)
- `src/world/blocks.cob` -> **Severity: 4.165** (Bridge: 0.0416 * Flux: 100.0%)
- `src/loot-tables.cob` -> **Severity: 2.182** (Bridge: 0.0218 * Flux: 99.9997%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/encoding/encode.cob` -> **Severity: 18.568** (Embedded: 0.2647 * Error Risk: 70.152%)
- `src/registries.cob` -> **Severity: 16.804** (Embedded: 0.2654 * Error Risk: 63.308%)
- `src/packets.cob` -> **Severity: 16.153** (Embedded: 0.2221 * Error Risk: 72.7304%)
- `src/encoding/json-parse.cob` -> **Severity: 14.612** (Embedded: 0.1801 * Error Risk: 81.1326%)
- `src/_copybooks/assert/ASSERT.cpy` -> **Severity: 13.232** (Embedded: 0.2413 * Error Risk: 54.8419%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/packets.cob` -> **Severity: 3602.5** (Blast Radius: 36.025 * Doc Risk: 100.0%)
- `tests/test.cob` -> **Severity: 3286.6** (Blast Radius: 32.866 * Doc Risk: 100.0%)
- `src/registries.cob` -> **Severity: 2415.9** (Blast Radius: 24.159 * Doc Risk: 100.0%)
- `src/encoding/encode.cob` -> **Severity: 2307.3** (Blast Radius: 23.073 * Doc Risk: 100.0%)
- `src/encoding/decode.cob` -> **Severity: 1405.0** (Blast Radius: 14.05 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `262` files carry mainframe facts -- `2653` call sites, `0` dataset bindings, `4078` record items.

### `codegen/generators/blocks_loot_table.cob` (COBOL)
- **Calls:** `CALL Codegen-TemplateLoad`, `CALL Codegen-Start`, `CALL Codegen-TemplateEval`, `CALL Codegen-Optimize`, `CALL Codegen-Append`, `CALL Codegen-End`, `CALL Codegen-ReadDataDirectory`, `CALL TrimFileExt`, `CALL Codegen-ProgramId`, `CALL Codegen-ReadDataFile`, `CALL JsonParse-ObjectStart`, `CALL JsonParse-ObjectKey` … (+16)
- **Record layouts (192 items):** `FUNCTION-POSITIONS (3)`, `FUNCTION-POSITIONS (3)`, `BUFFER (1)`, `BUFFERLEN (1)`, `REPLACE-PTR (1)`, `INIT-DONE (1)`, `REPLACE-PTR (1)`, `CURRENT-FILENAME (1)`, `DIR-INDEX (1)`, `LK-VARNAME (1)`, `LK-BUFFER (1)`, `LK-LENGTH (1)` … (+176 more)
- **Data moves:** 114 (ADD 23, COMPUTE 2, INITIALIZE 3, MOVE 67, STRING 19); most-fed items `JSONPOS`, `JSONPOS-BACKUP`, `LK-BUFFER`, `BLOCK-NAME`, `CURRENT-FILENAME`, `FUNCTION-POSITION`

### `src/world/chunk-io.cob` (COBOL)
- **Calls:** `CALL Registries-LookupRegistry`, `CALL NbtEncode-RootCompound`, `CALL NbtEncode-Int`, `CALL NbtEncode-List`, `CALL NbtEncode-Compound`, `CALL NbtEncode-Byte`, `CALL Blocks-ToDescription`, `CALL NbtEncode-String`, `CALL NbtEncode-EndCompound`, `CALL NbtEncode-EndList`, `CALL LeadingZeros32`, `CALL NbtEncode-LongArray` … (+30)
- **Record layouts (113 items):** `BLOCK-ENTITY-Z (2)`, `PALETTE-INDICES (2)`, `LK-BLOCKS (2)`, `LK-BIOMES (2)`, `BIOME-REGISTRY-ID (1)`, `BLOCK-ENTITY-REGISTRY-ID (1)`, `ENTITY-REGISTRY-ID (1)`, `FILE-TYPE (1)`, `BUFFER (1)`, `BUFFER-LENGTH (1)`, `CHUNK-SECTION-MIN-Y (1)`, `TAG (1)` … (+97 more)
- **Data moves:** 202 (ADD 13, COMPUTE 43, DIVIDE 40, INITIALIZE 10, MOVE 86, MULTIPLY 4, SUBTRACT 6); most-fed items `LONG-ARRAY-ENTRY`, `PALETTE-INDEX`, `INT32`, `SEEK-NBTDEC`, `CURRENT-BLOCK-ID`, `ENTRIES-PER-LONG`

### `src/server.cob` (COBOL)
- **Calls:** `CALL Callbacks-Init`, `CALL Region-Init`, `CALL IgnoreSIGPIPE`, `CALL SetConsoleNonBlocking`, `CALL Generated-Registries`, `CALL Registries-Count`, `CALL Registries-Create`, `CALL Generated-Items`, `CALL Items-Count`, `CALL Files-ReadAll`, `CALL Blocks-Parse`, `CALL Blocks-Count` … (+103)
- **Record layouts (72 items):** `DEBUG-SAMPLE (5)`, `DISPLAY-INT (2)`, `FILE-BLOCKS (1)`, `FILE-DATAPACK-ROOT (1)`, `AUTOSAVE-INTERVAL (1)`, `LAST-AUTOSAVE (1)`, `GAME-TICK-INTERVAL (1)`, `KEEPALIVE-SEND-INTERVAL (1)`, `KEEPALIVE-RECV-TIMEOUT (1)`, `DATA-BUFFER (1)`, `DATA-BUFFER-LEN (1)`, `DATA-FAILURE (1)` … (+55 more)
- **Data moves:** 101 (ADD 3, COMPUTE 25, INITIALIZE 2, MOVE 69, STRING 2); most-fed items `TEMP-INT64`, `PACKET-STATE`, `DISPLAY-INT`, `CLIENT-STATE`, `DEBUG-SAMPLE-FULL`, `DEBUG-SAMPLE-TASKS`

### `src/region.cob` (COBOL)
- **Calls:** `CALL SystemTimeMillis`, `CALL Region-CloseLeastRecentlyUsed`, `CALL Region-RegionFileName`, `CALL CBL_OPEN_FILE`, `CALL CBL_CREATE_FILE`, `CALL Region-WriteToHandle`, `CALL CBL_CLOSE_FILE`, `CALL Region-ReadFromHandle`, `CALL Decode-UnsignedInt`, `CALL Region-Close`, `CALL CBL_READ_FILE`, `CALL CBL_WRITE_FILE` … (+9)
- **Record layouts (91 items):** `DISPLAY-X (1)`, `DISPLAY-Z (1)`, `LK-TYPE (1)`, `LK-X (1)`, `LK-Z (1)`, `LK-FILE-NAME (1)`, `REGION-INDEX (1)`, `SECTOR-INDEX (1)`, `SECTOR-BUFFER (1)`, `FILE-OFFSET (1)`, `FILE-LENGTH (1)`, `CHUNK-SECTOR-LOCATION (1)` … (+79 more)
- **Data moves:** 200 (ADD 5, COMPUTE 45, DIVIDE 52, INITIALIZE 2, MOVE 79, STRING 12, SUBTRACT 5); most-fed items `FILE-OFFSET`, `CHUNK-SECTOR-LENGTH`, `CHUNK-SECTOR-OFFSET`, `IS`, `LOCATION-INDEX`, `MODE`

### `tests/encoding/json-parse.test.cob` (COBOL)
- **Calls:** `CALL Test-JsonParse-ObjectStart`, `CALL Test-JsonParse-ObjectEnd`, `CALL Test-JsonParse-ArrayStart`, `CALL Test-JsonParse-ArrayEnd`, `CALL Test-JsonParse-Comma`, `CALL Test-JsonParse-String`, `CALL Test-JsonParse-ObjectKey`, `CALL Test-JsonParse-Null`, `CALL Test-JsonParse-Boolean`, `CALL Test-JsonParse-Integer`, `CALL Test-JsonParse-Float`, `CALL Test-JsonParse-SkipValue` … (+14)
- **Record layouts (44 items):** `STR (1)`, `OFFSET (1)`, `FLAG (1)`, `STR (1)`, `OFFSET (1)`, `FLAG (1)`, `STR (1)`, `OFFSET (1)`, `FLAG (1)`, `STR (1)`, `OFFSET (1)`, `FLAG (1)` … (+32 more)
- **Data moves:** 173 (MOVE 173)

### `tests/encoding/nbt-decode.test.cob` (COBOL)
- **Calls:** `CALL Test-NbtDecode-Byte`, `CALL Test-NbtDecode-Int`, `CALL Test-NbtDecode-Short`, `CALL Test-NbtDecode-Long`, `CALL Test-NbtDecode-Float`, `CALL Test-NbtDecode-Double`, `CALL Test-NbtDecode-String`, `CALL Test-NbtDecode-List`, `CALL Test-NbtDecode-Compound`, `CALL Test-NbtDecode-RootCompound`, `CALL Test-NbtDecode-EndCompound`, `CALL Test-NbtDecode-Peek` … (+16)
- **Record layouts (27 items):** `BUFFER (1)`, `RESULT (1)`, `BUFFER (1)`, `RESULT (1)`, `BUFFER (1)`, `RESULT (1)`, `BUFFER (1)`, `RESULT (1)`, `BUFFER (1)`, `RESULT (1)`, `BUFFER (1)`, `RESULT (1)` … (+15 more)
- **Data moves:** 154 (INITIALIZE 50, MOVE 104)

### `tests/encoding/encode.test.cob` (COBOL)
- **Calls:** `CALL Test-Encode-Byte`, `CALL Test-Encode-UnsignedShort`, `CALL Test-Encode-UnsignedInt`, `CALL Test-Encode-VarInt`, `CALL Test-Encode-GetVarIntLength`, `CALL Test-Encode-UnsignedLong`, `CALL Test-Encode-Long`, `CALL Test-Encode-Double`, `CALL Test-Encode-Float`, `CALL Test-Encode-String`, `CALL Test-Encode-Angle`, `CALL Test-Encode-Position` … (+14)
- **Record layouts (43 items):** `VALUE-IN (4)`, `VALUE-IN (1)`, `BUFFER (1)`, `BUFFERPOS (1)`, `VALUE-IN (1)`, `BUFFER (1)`, `BUFFERPOS (1)`, `VALUE-IN (1)`, `BUFFER (1)`, `BUFFERPOS (1)`, `VALUE-IN (1)`, `BUFFER (1)` … (+28 more)
- **Data moves:** 129 (INITIALIZE 2, MOVE 127)

### `tests/encoding/decode.test.cob` (COBOL)
- **Calls:** `CALL Test-Decode-Byte`, `CALL Test-Decode-UnsignedShort`, `CALL Test-Decode-Short`, `CALL Test-Decode-UnsignedInt`, `CALL Test-Decode-Int`, `CALL Test-Decode-VarInt`, `CALL Test-Decode-UnsignedLong`, `CALL Test-Decode-Long`, `CALL Test-Decode-Double`, `CALL Test-Decode-Float`, `CALL Test-Decode-String`, `CALL Test-Decode-Position` … (+14)
- **Record layouts (43 items):** `RESULT (4)`, `BUFFER (1)`, `BUFFERPOS (1)`, `RESULT (1)`, `BUFFER (1)`, `BUFFERPOS (1)`, `RESULT (1)`, `BUFFER (1)`, `BUFFERPOS (1)`, `RESULT (1)`, `BUFFER (1)`, `BUFFERPOS (1)` … (+28 more)
- **Data moves:** 111 (ADD 1, INITIALIZE 2, MOVE 108)

### `src/datapack.cob` (COBOL)
- **Calls:** `CALL Registries-Count`, `CALL Registries-Name`, `CALL Datapack-LoadRegistry`, `CALL Datapack-LoadTags`, `CALL Datapack-LoadRecipes`, `CALL OpenDirectory`, `CALL ReadDirectory`, `CALL TrimFileExt`, `CALL Registries-CreateEntry`, `CALL CloseDirectory`, `CALL IsDirectory`, `CALL Datapack-LoadTagDir` … (+15)
- **Record layouts (82 items):** `REGISTRY-COUNT (1)`, `REGISTRY-ID (1)`, `REGISTRY-NAME (1)`, `LK-ROOT-PATH (1)`, `LK-PACK-NAME (1)`, `LK-FAILURE (1)`, `DIR-PATH (1)`, `DIR-PATH-LENGTH (1)`, `DIR-HANDLE (1)`, `EOF (1)`, `DIR-ENTRY (1)`, `ENTRY-NAME (1)` … (+70 more)
- **Data moves:** 92 (ADD 5, INITIALIZE 10, MOVE 42, STRING 32, SUBTRACT 3); most-fed items `TAGS-CURRENT-TAG-ENTRY`, `DISPLAY-INT`, `ENTRY-NAME`, `OTHER-TAG-NAME`, `TAG-NAME`, `TAG-REFERENCES-COUNT`

### `src/encoding/json-parse.cob` (COBOL)
- **Calls:** `CALL JsonParse-String-Unicode`, `CALL DecodeHexChar`, `CALL JsonParse-String`, `CALL JsonParse-Integer`, `CALL JsonParse-Float`, `CALL JsonParse-SkipValue`, `CALL JsonParse-Comma`, `CALL JsonParse-ObjectKey`
- **Record layouts (78 items):** `CHAR-ALPHA (2)`, `CHAR-ALPHA (2)`, `CHAR-ALPHA (2)`, `INPUT-LENGTH (1)`, `LK-INPUT (1)`, `LK-OFFSET (1)`, `LK-FLAG (1)`, `INPUT-LENGTH (1)`, `LK-INPUT (1)`, `LK-OFFSET (1)`, `LK-FLAG (1)`, `INPUT-LENGTH (1)` … (+63 more)
- **Data moves:** 120 (ADD 31, COMPUTE 11, DIVIDE 2, MOVE 75, SUBTRACT 1); most-fed items `LK-VALUE`, `CHAR-ALPHA`, `LK-CHARCODE`, `VALUE-ABS`, `LK-OFFSET`, `LK-STRING`

### `src/world/blocks.cob` (COBOL)
- **Calls:** `CALL World-FindChunkIndex`, `CALL Blocks-CompareBlockType`, `CALL SendPacket-BlockUpdate`, `CALL SendPacket-WorldEvent`, `CALL ALLOCATE-PTR`, `CALL SendPacket-BlockEntityData`
- **Record layouts (63 items):** `LK-POSITION (4)`, `LK-POSITION (4)`, `LK-POSITION (4)`, `LK-POSITION (4)`, `LK-POSITION (4)`, `LK-POSITION (4)`, `LK-RESULT (1)`, `POS-CHUNK-X (1)`, `POS-CHUNK-Z (1)`, `CHUNK-INDEX (1)`, `SECTION-INDEX (1)`, `BLOCK-INDEX (1)` … (+33 more)
- **Data moves:** 124 (ADD 1, COMPUTE 24, DIVIDE 80, MOVE 16, SUBTRACT 3); most-fed items `IS`, `MODE`, `TOWARD-LESSER`, `BLOCK-IN-CHUNK-INDEX`, `BLOCK-INDEX`, `POS-CHUNK-X`

### `tests/encoding/nbt-encode.test.cob` (COBOL)
- **Calls:** `CALL Test-NbtEncode-Byte`, `CALL Test-NbtEncode-Short`, `CALL Test-NbtEncode-Int`, `CALL Test-NbtEncode-Long`, `CALL Test-NbtEncode-Float`, `CALL Test-NbtEncode-Double`, `CALL Test-NbtEncode-String`, `CALL Test-NbtEncode-ByteArray`, `CALL Test-NbtEncode-List`, `CALL Test-NbtEncode-Compound`, `CALL Test-NbtEncode-RootCompound`, `CALL Test-NbtEncode-EndCompound` … (+19)
- **Record layouts (28 items):** `BUFFER (1)`, `VALUE-IN (1)`, `BUFFER (1)`, `VALUE-IN (1)`, `BUFFER (1)`, `VALUE-IN (1)`, `BUFFER (1)`, `VALUE-IN (1)`, `BUFFER (1)`, `VALUE-IN (1)`, `BUFFER (1)`, `VALUE-IN (1)` … (+16 more)
- **Data moves:** 114 (INITIALIZE 31, MOVE 83)

### `src/encoding/nbt-decode.cob` (COBOL)
- **Calls:** `CALL Decode-UnsignedShort`, `CALL NbtDecode-Long`, `CALL NbtDecode-SkipString`, `CALL Decode-Byte`, `CALL Decode-Short`, `CALL Decode-Int`, `CALL Decode-Long`, `CALL Decode-Float`, `CALL Decode-Double`, `CALL NbtDecode-List`, `CALL NbtDecode-EndList`, `CALL NbtDecode-SkipValue` … (+4)
- **Record layouts (70 items):** `INT32-BYTES (2)`, `UINT16 (1)`, `LK-BUFFER (1)`, `INT64 (1)`, `LK-BUFFER (1)`, `LK-VALUE (1)`, `INT64 (1)`, `LK-BUFFER (1)`, `LK-VALUE (1)`, `INT64 (1)`, `LK-BUFFER (1)`, `LK-VALUE (1)` … (+57 more)
- **Data moves:** 86 (ADD 20, COMPUTE 6, MOVE 56, SUBTRACT 4); most-fed items `TAG`, `LK-VALUE`, `LK-NBTDEC-OFFSET`, `LK-NBTDEC-STACK-TYPE`, `LIST-TAG`, `LK-NBTDEC-STACK-LIST-COUNT`

### `src/encoding/nbt-encode.cob` (COBOL)
- **Calls:** `CALL Encode-UnsignedShort`, `CALL NbtEncode-WriteString`, `CALL Encode-Byte`, `CALL Encode-Short`, `CALL Encode-Int`, `CALL Encode-Long`, `CALL Encode-Float`, `CALL Encode-Double`, `CALL NbtEncode-ByteArray`, `CALL NbtEncode-IntArray`, `CALL NbtEncode-Int`
- **Record layouts (56 items):** `INT32-BYTES (2)`, `UINT16 (1)`, `LK-BUFFER (1)`, `LK-OFFSET (1)`, `LK-STRING (1)`, `LK-BUFFER (1)`, `LK-NAME (1)`, `LK-VALUE (1)`, `LK-BUFFER (1)`, `LK-NAME (1)`, `LK-VALUE (1)`, `LK-BUFFER (1)` … (+43 more)
- **Data moves:** 88 (ADD 27, MOVE 52, SUBTRACT 9); most-fed items `LK-BUFFER`, `LK-NBTENC-STACK-LIST-COUNT`, `LK-NBTENC-STACK-INDEX`, `TEMP-OFFSET`, `UINT16`

### `src/players/player-io.cob` (COBOL)
- **Calls:** `CALL UUID-ToString`, `CALL Registries-LookupRegistry`, `CALL NbtEncode-RootCompound`, `CALL NbtEncode-UUID`, `CALL NbtEncode-Byte`, `CALL NbtEncode-List`, `CALL NbtEncode-Double`, `CALL NbtEncode-EndList`, `CALL NbtEncode-Float`, `CALL NbtEncode-Short`, `CALL NbtEncode-Int`, `CALL NbtEncode-Compound` … (+25)
- **Record layouts (36 items):** `UUID-STR (1)`, `LK-PLAYER-UUID (1)`, `LK-PLAYER-FILE-NAME (1)`, `ITEM-REGISTRY (1)`, `PLAYER-FILE-NAME (1)`, `ERRNO (1)`, `BUFFER (1)`, `BUFFER-LENGTH (1)`, `COMPRESSED-BUFFER (1)`, `COMPRESSED-LENGTH (1)`, `STR (1)`, `LEN (1)` … (+24 more)
- **Data moves:** 48 (ADD 2, COMPUTE 3, INITIALIZE 2, MOVE 33, STRING 6, SUBTRACT 2); most-fed items `BUFFER-LENGTH`, `COMPRESSED-BUFFER`, `COMPRESSED-LENGTH`, `INT16`, `INT32`, `INT8`

### `src/world/entities.cob` (COBOL)
- **Calls:** `CALL World-EnsureChunk`, `CALL World-NextEntityId`, `CALL RandomUUID`, `CALL World-SendEntity`, `CALL SendPacket-BundleDelimiter`, `CALL SendPacket-SpawnEntity`, `CALL Registries-Lookup`, `CALL Encode-VarInt`, `CALL Encode-InventorySlot`, `CALL SendPacket-SetEntityMetadata`, `CALL SendPacket-RemoveEntity`, `CALL World-SpawnEntity` … (+1)
- **Record layouts (66 items):** `LK-POSITION (4)`, `LK-VELOCITY (4)`, `ITEM-POS (4)`, `ITEM-VELOCITY (4)`, `ITEM-POS (4)`, `ITEM-VELOCITY (4)`, `LK-BLOCK-POSITION (4)`, `LAST-ENTITY-ID (1)`, `LK-ENTITY-ID (1)`, `CHUNK-INDEX (1)`, `CLIENT-ID (1)`, `LK-ENTITY (1)` … (+33 more)
- **Data moves:** 82 (ADD 4, COMPUTE 19, DIVIDE 32, INITIALIZE 1, MOVE 23, SUBTRACT 3); most-fed items `IS`, `ITEM-VELOCITY-X`, `ITEM-VELOCITY-Z`, `MODE`, `TOWARD-LESSER`, `ITEM-Y`

### `src/blocks.cob` (COBOL)
- **Calls:** `CALL JsonParse-ObjectStart`, `CALL JsonParse-ObjectKey`, `CALL Registries-Lookup`, `CALL Blocks-Parse-Block`, `CALL JsonParse-Comma`, `CALL JsonParse-ObjectEnd`, `CALL JsonParse-String`, `CALL JsonParse-SkipValue`, `CALL Blocks-Parse-Property`, `CALL JsonParse-ArrayStart`, `CALL Blocks-Parse-State`, `CALL JsonParse-ArrayEnd` … (+2)
- **Record layouts (68 items):** `LK-PROPERTY (4)`, `BLOCK-NAME (1)`, `BLOCK-ID (1)`, `BLOCK-INDEX (1)`, `OFFSET (1)`, `EXIT-LOOP (1)`, `LK-JSON (1)`, `LK-JSON-LEN (1)`, `LK-FAILURE (1)`, `EXIT-LOOP (1)`, `OBJECT-KEY (1)`, `STATE-ID (1)` … (+53 more)
- **Data moves:** 58 (ADD 3, COMPUTE 10, DIVIDE 4, INITIALIZE 1, MOVE 40); most-fed items `PROPERTY-CODE`, `LK-STATE-ID`, `BLOCK-INDEX`, `LK-MAXIMUM-ID`, `LK-STATE-PROPERTY-VALUE`, `PROPERTY-VALUE-INDEX`

### `src/packets/clientbound/play/chunkdata.cob` (COBOL)
- **Calls:** `CALL Blocks-MaximumStateId`, `CALL Registries-LookupRegistry`, `CALL Registries-EntryCount`, `CALL Encode-Int`, `CALL Encode-Short`, `CALL EncodePalette-SingleValued`, `CALL EncodePalette`, `CALL Encode-VarInt`, `CALL NbtEncode-Compound`, `CALL SERIALIZE-PTR`, `CALL NbtEncode-EndCompound`, `CALL SendPacket` … (+1)
- **Record layouts (51 items):** `LK-SECTIONS (7)`, `LK-BLOCK-ENTITIES (3)`, `LONG-BYTES (2)`, `LK-IDS (2)`, `PAYLOAD (1)`, `PAYLOADPOS (1)`, `PAYLOADLEN (1)`, `BLOCK-COUNT (1)`, `BLOCK-STATES-LENGTH (1)`, `BIOMES-LENGTH (1)`, `MAX-BLOCK-STATE (1)`, `MAX-BIOME-ID (1)` … (+29 more)
- **Data moves:** 83 (ADD 11, COMPUTE 16, DIVIDE 18, INITIALIZE 1, MOVE 34, SUBTRACT 3); most-fed items `INT32`, `LONG`, `CURRENT-MULTIPLIER`, `DATA-ARRAY-LENGTH`, `IS`, `LK-BUFFER`

### `src/encoding/decode.cob` (COBOL)
- **Calls:** `CALL Decode-VarInt`, `CALL Decode-UnsignedLong`, `CALL Components-LengthOf`
- **Record layouts (83 items):** `LK-VALUE (4)`, `VALUE-BYTES (2)`, `VALUE-BYTES (2)`, `VALUE-BYTES (2)`, `VALUE-BYTES (2)`, `VALUE-BYTES (2)`, `BYTE-ALPHA (2)`, `VALUE-BYTES (2)`, `VALUE-BYTES (2)`, `VALUE-BYTES (2)`, `VALUE-BYTES (2)`, `BYTE-COUNT (1)` … (+58 more)
- **Data moves:** 67 (ADD 4, COMPUTE 16, DIVIDE 8, MOVE 31, MULTIPLY 2, SUBTRACT 6); most-fed items `CURRENT-VALUE`, `LK-VALUE`, `VALUE-BYTES`, `BYTE-ALPHA`, `COMPONENTS-OFFSET`, `LK-SLOT-NBT-LENGTH`

### `src/client-chunks.cob` (COBOL)
- **Calls:** `CALL SendPacket-SetCenterChunk`, `CALL EnqueueChunk`, `CALL ProcessChunkQueue`, `CALL SendChunks`, `CALL World-UnloadChunks`, `CALL World-EnsureChunk`, `CALL SendPacket-ChunkData`, `CALL World-SendEntity`
- **Record layouts (35 items):** `PLAYER-ID (1)`, `LK-CLIENT (1)`, `X-START (1)`, `X-END (1)`, `Z-START (1)`, `Z-END (1)`, `X-POS (1)`, `Z-POS (1)`, `LK-CLIENT (1)`, `LK-CLIENT (1)`, `CLIENT-ID (1)`, `UNLOAD-FAILURE (1)` … (+23 more)
- **Data moves:** 103 (ADD 2, COMPUTE 55, DIVIDE 32, MOVE 14); most-fed items `X-END`, `X-START`, `Z-END`, `Z-START`, `IS`, `MODE`

*(+242 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 71% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: application programs (source or load-module list) (84 gaps); JCL and PROC libraries (31 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2253 call pairs -- scoped 18.4%, unique 74.2%, ambiguous 0.0%, external 7.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 2187 | 18.9% | 76.5% | 0.0% | 4.7% |
| cpp | 66 | 3.0% | 0.0% | 0.0% | 97.0% |

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
