# ARCHITECTURAL_BRIEF: CobolCraft
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/meyfa/CobolCraft` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 282 |
| Analyzed Artifacts (Scanned) | 273 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9 |
| Total LOC | 23390 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.8% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6302 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2973 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.1405 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 21 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 268 | 22786 | 98.2% |
| CPP | 2 | 475 | 0.7% |
| DOCKERFILE | 1 | 23 | 0.4% |
| MAKEFILE | 1 | 100 | 0.4% |
| JSON | 1 | 6 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z +1.86; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 46%, Data / Markup / Trivial 23%, Interface Declarations Files 14%, I/O & Config Routines Files 8%, State Mutators Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 273 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9*

**Composition by Extension & Reason:**
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 170 LOC), 1x Excluded (Machine-Generated Source Code Signature: 81 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 83.0 | 20.6 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 60.0 | 68.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 80.3 | 5.0 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 52.2 | 69.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.7 | 1.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 70.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 13.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 32.2 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 30.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 502 | 83 | 2 | `cpp/cobolcraft_util.cpp` |
| cleanup | 24 | 11 | 0 | `Makefile` |
| guards | 4 | 2 | 0 | `cpp/cobolcraft_util.cpp` |
| danger | 1427 | 192 | 14 | `src/encoding/nbt-encode.cob` |
| concurrency | 1 | 1 | 0 | `Dockerfile` |
| connectivity | 963 | 182 | 8 | `src/datapack.cob` |
| io | 248 | 30 | 1 | `src/inventory/inventory.cob` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2647 | 183 | 22 | `src/server.cob` |
| time | 3 | 2 | 0 | `cpp/cobolcraft_util.cpp` |
| serialization | 329 | 71 | 4 | `src/encoding/strings.cob` |
| regex | 1055 | 126 | 4 | `tests/encoding/encode.test.cob` |
| events | 1 | 1 | 0 | `cpp/cobolcraft_util.cpp` |
| tests | 367 | 28 | 1 | `tests/encoding/encode.test.cob` |
| docs | 21 | 1 | 0 | `cpp/cobolcraft_util.h` |
| debt | 402 | 99 | 3 | `src/datapack.cob` |
| mutation | 4541 | 196 | 50 | `src/world/chunk-io.cob` |
| dead_code | 284 | 71 | 2 | `tests/encoding/json-parse.test.cob` |
| credential | 0 | 0 | 0 | - |
| threat | 39 | 22 | 0 | `src/encoding/nbt-decode.cob` |
| ml_ai | 88 | 25 | 0 | `src/world/blocks.cob` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/inventory/inventory.cob` (Hits: 37)
- `src/client-chunks.cob` (Hits: 28)
- `Makefile` (Hits: 23)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DD-PLAYERS.cpy** (`src/_copybooks/state/DD-PLAYERS.cpy`) — 57 inbound connections
2. **PROC-PACKET-INIT.cpy** (`src/_copybooks/procedures/PROC-PACKET-INIT.cpy`) — 47 inbound connections
3. **DD-PACKET.cpy** (`src/_copybooks/structs/DD-PACKET.cpy`) — 47 inbound connections
4. **DD-CLIENTS.cpy** (`src/_copybooks/state/DD-CLIENTS.cpy`) — 42 inbound connections
5. **DD-SERVER-PROPERTIES.cpy** (`src/_copybooks/state/DD-SERVER-PROPERTIES.cpy`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cobolcraft_util.cpp** (`cpp/cobolcraft_util.cpp`) — 15 outbound dependencies
2. **entities.cob** (`src/world/entities.cob`) — 9 outbound dependencies
3. **sign.cob** (`src/blockentities/sign.cob`) — 8 outbound dependencies
4. **client-chunks.cob** (`src/client-chunks.cob`) — 8 outbound dependencies
5. **item.cob** (`src/entities/item.cob`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `OpenFile` **(Compute Cores)** (@ `src/region.cob`) -> Impact: **82.5** | LOC: 511
- `LoadChunkEntities` **(Compute Cores)** (@ `src/world/chunk-io.cob`) -> Impact: **69.6** | LOC: 392
- `CHAR-ALPHA` **(Compute Cores)** (@ `src/encoding/json-parse.cob`) -> Impact: **57.5** | LOC: 251
- `INVENTORY-SLOT` **(Compute Cores)** (@ `src/players/player-io.cob`) -> Impact: **56.5** | LOC: 189
- `PATTERN-SLOTS` **(Compute Cores)** (@ `src/parsers/recipe/shaped.cob`) -> Impact: **52.5** | LOC: 149
- `InsertEntry` **(Compute Cores)** (@ `src/datapack.cob`) -> Impact: **47.2** | LOC: 205
- `AssertOk` **(Compute Cores)** (@ `codegen/generators/blocks_loot_table.cob`) -> Impact: **43.7** | LOC: 214
- `CHAR-ALPHA` **(Compute Cores)** (@ `src/encoding/json-parse.cob`) -> Impact: **40.8** | LOC: 196
- `PARTS` **(Compute Cores)** (@ `src/commands.cob`) -> Impact: **38.8** | LOC: 235
- `GenerateFunctions` **(Compute Cores)** (@ `codegen/generators/blocks_loot_table.cob`) -> Impact: **38.1** | LOC: 103

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 17 | 2564.52 | 47.95% | 21.64% |
| `src/encoding` | 8 | 1619.16 | 68.74% | 18.51% |
| `tests/encoding` | 8 | 1211.68 | 4.36% | 0.0% |
| `codegen/generators` | 4 | 934.36 | 41.51% | 7.64% |
| `src/packets/clientbound/play` | 37 | 921.14 | 7.97% | 32.64% |
| `src/items` | 14 | 769.1 | 51.28% | 28.59% |
| `src/world` | 6 | 733.33 | 61.53% | 23.55% |
| `src/packets/serverbound/play` | 22 | 522.64 | 18.15% | 37.47% |
| `cpp` | 2 | 489.7 | 36.64% | 44.22% |
| `src/blocks` | 12 | 412.74 | 26.94% | 25.62% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/packets/serverbound/play/use-item.cob` -> **99.9797%** Exposure
- `src/world/entities.cob` -> **99.8352%** Exposure
- `src/packets/clientbound/play/spawn-entity.cob` -> **99.3307%** Exposure
- `src/items/common.cob` -> **98.9995%** Exposure
- `src/packets/clientbound/play/set-container-content.cob` -> **97.0688%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `codegen/common/data.cob` -> **100.0%** Exposure
- `codegen/common/optimizer.cob` -> **100.0%** Exposure
- `codegen/common/templates.cob` -> **100.0%** Exposure
- `codegen/common/util.cob` -> **100.0%** Exposure
- `src/client-chunks.cob` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/encoding/encode.test.cob` -> **18** Orphaned Functions | **6** Duplicates
- `tests/encoding/json-parse.test.cob` -> **24** Orphaned Functions | **0** Duplicates
- `tests/encoding/nbt-encode.test.cob` -> **21** Orphaned Functions | **0** Duplicates
- `tests/encoding/nbt-decode.test.cob` -> **20** Orphaned Functions | **0** Duplicates
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
- **Unknown Dependencies:** `545` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/world/entities.cob` (COBOL) -> Cumulative Risk: **665.56**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.52)
- **Magnitude:** 239.9 | **LOC:** 450 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8352%)
- **Heaviest Functions:** `LK-ENTITY` (I/O & Config Routines, Impact: 12.6), `LK-ENTITY` (I/O & Config Routines, Impact: 11.1), `LK-ENTITY` (Interface Declarations, Impact: 7.0)

### 2. `src/datapack.cob` (COBOL) -> Cumulative Risk: **641.29**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.00)
- **Magnitude:** 347.6 | **LOC:** 644 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9994%), Safety Score (94.4156%)
- **Heaviest Functions:** `InsertEntry` (Compute Cores, Impact: 47.2), `ExpandTag` (I/O & Config Routines, Impact: 10.2), `ExpandOtherTag` (I/O & Config Routines, Impact: 3.5)

### 3. `cpp/cobolcraft_util.cpp` (CPP) -> Cumulative Risk: **634.85**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.22)
- **Magnitude:** 474.24 | **LOC:** 558 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (93.1242%)
- **Heaviest Functions:** `SocketRead` (Compute Cores, Impact: 21.5), `ZlibCompress` (Many-Argument Workhorses, Impact: 19.9), `ZlibDecompress` (Many-Argument Workhorses, Impact: 19.9)

### 4. `src/server.cob` (COBOL) -> Cumulative Risk: **631.04**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.79)
- **Magnitude:** 334.68 | **LOC:** 934 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9737%), Tech Debt (85.3221%)
- **Heaviest Functions:** `ServerLoop` (Compute Cores, Impact: 29.4), `HandleServerError` (Compute Cores, Impact: 28.9), `ReceivePacket` (Interface Declarations, Impact: 13.9)

### 5. `src/parsers/recipe/shapeless.cob` (COBOL) -> Cumulative Risk: **615.0**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.84)
- **Magnitude:** 117.42 | **LOC:** 204 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9965%), Safety Score (87.2434%)
- **Heaviest Functions:** `INGREDIENT-CHOICE-COMBINED-IDS` (Compute Cores, Impact: 27.6), `ParseIngredients` (Compute Cores, Impact: 25.7), `INGREDIENT-IDS` (I/O & Config Routines, Impact: 2.4)

### 6. `src/inventory/inventory.cob` (COBOL) -> Cumulative Risk: **605.38**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.24)
- **Magnitude:** 200.18 | **LOC:** 377 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9992%), Safety Score (88.6213%)
- **Heaviest Functions:** `MatchShapedRecipes` (Compute Cores, Impact: 19.6), `LK-INVENTORY` (I/O & Config Routines, Impact: 14.0), `TEMP-SLOT` (I/O & Config Routines, Impact: 12.6)

### 7. `src/world/chunk-io.cob` (COBOL) -> Cumulative Risk: **573.92**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.58)
- **Magnitude:** 6.11 | **LOC:** 1020 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.6614%)
- **Heaviest Functions:** `LoadChunkEntities` (Compute Cores, Impact: 69.6), `SaveChunkRegion` (Compute Cores, Impact: 34.5), `LoadChunkRegion` (Compute Cores, Impact: 27.7)

### 8. `src/parsers/recipe/shaped.cob` (COBOL) -> Cumulative Risk: **569.47**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.30)
- **Magnitude:** 240.84 | **LOC:** 360 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.7879%)
- **Heaviest Functions:** `PATTERN-SLOTS` (Compute Cores, Impact: 52.5), `ParseKey` (Compute Cores, Impact: 26.4), `ParsePattern` (Interface Declarations, Impact: 7.2)

### 9. `src/packets/serverbound/play/use-item-on.cob` (COBOL) -> Cumulative Risk: **567.67**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z -0.16)
- **Magnitude:** 35.26 | **LOC:** 93 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9722%), Tech Debt (95.3234%)
- **Heaviest Functions:** `CURSOR-POS` (I/O & Config Routines, Impact: 13.7), `LOCATION` (I/O & Config Routines, Impact: 1.2)

### 10. `src/players/player-io.cob` (COBOL) -> Cumulative Risk: **564.76**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z -0.21)
- **Magnitude:** 167.2 | **LOC:** 376 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9993%), Safety Score (92.4027%)
- **Heaviest Functions:** `INVENTORY-SLOT` (Compute Cores, Impact: 56.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `codegen/generators/blocks_loot_table.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 680.72 | **LOC:** 1527 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.3743%), Tech Debt (15.212%)
**Top Internal Functions/Classes:**
  * `AssertOk` **(Compute Cores)** (Impact: 43.7)
  * `GenerateFunctions` **(Compute Cores)** (Impact: 38.1)
  * `AssertOk` **(Compute Cores)** (Impact: 31.9)
  * `ReplaceBody` **(Interface Declarations)** (Impact: 17.8)
  * `AssertOk` **(I/O & Config Routines)** (Impact: 17.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 329`, `args: 512`, `func_start: 20`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 125`, `planned_debt: 17`
* *Architecture:* `io: 1`, `api: 70`, `import: 58`
* *Defense:* `test: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ASSERT, ASSERT-FAILED, DD-CODEGEN-DIR-LIST, DD-CODEGEN-JSON, DD-CODEGEN-TEMPLATE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/cobolcraft_util.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 474.24 | **LOC:** 558 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.2795%), Tech Debt (88.4464%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` chrono, cobolcraft_util.h, csignal, cstring, dirent.h, errno.h, fcntl.h, in.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/encoding/json-parse.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 466.54 | **LOC:** 642 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.6658%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CHAR-ALPHA` **(Compute Cores)** (Impact: 57.5)
  * `CHAR-ALPHA` **(Compute Cores)** (Impact: 40.8)
  * `CHAR-ALPHA` **(I/O & Config Routines)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 152`, `args: 94`, `func_start: 3`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 123`, `dead_code: 4`
* *Architecture:* `api: 14`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PROC-SKIP-WHITESPACE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/region.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 432.4 | **LOC:** 637 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.8375%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `OpenFile` **(Compute Cores)** (Impact: 82.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 103 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 116`, `args: 167`, `func_start: 1`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 125`, `dead_code: 2`
* *Architecture:* `io: 14`, `api: 9`, `import: 14`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` DD-REGION-FILE-REF, DD-REGION-FILES, DD-SERVER-PROPERTIES
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/datapack.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 347.6 | **LOC:** 644 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.6139%), Tech Debt (84.9003%)
**Top Internal Functions/Classes:**
  * `InsertEntry` **(Compute Cores)** (Impact: 47.2)
  * `ExpandTag` **(I/O & Config Routines)** (Impact: 10.2)
  * `ExpandOtherTag` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 163`, `args: 151`, `func_start: 3`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 72`, `planned_debt: 40`
* *Architecture:* `api: 103`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DD-RECIPES, DD-TAGS
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 334.68 | **LOC:** 934 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.0947%), Tech Debt (85.3221%)
**Top Internal Functions/Classes:**
  * `ServerLoop` **(Compute Cores)** (Impact: 29.4)
  * `HandleServerError` **(Compute Cores)** (Impact: 28.9)
  * `ReceivePacket` **(Interface Declarations)** (Impact: 13.9)
  * `NetworkRead` **(Interface Declarations)** (Impact: 10.5)
  * `RegisterItems` **(Interface Declarations)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 48 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 149`, `args: 202`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 82`, `dead_code: 4`, `planned_debt: 5`, `unreferenced_by_name: 16`
* *Architecture:* `io: 7`, `api: 11`, `import: 30`
* *Defense:* `test: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` ASSERT, ASSERT-FAILED, DD-CLIENT-STATES, DD-CLIENTS, DD-PACKET-DIRECTIONS, DD-PLAYERS, DD-SERVER-PROPERTIES, DD-VERSION
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/encoding/nbt-decode.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 288.24 | **LOC:** 784 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.2143%), Tech Debt (38.2193%)
**Top Internal Functions/Classes:**
  * `INT32-BYTES` **(Interface Declarations)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 155`, `args: 168`, `func_start: 1`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 92`, `dead_code: 7`, `planned_debt: 12`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`, `import: 22`
* *Defense:* `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ASSERT, DD-NBT-DECODER
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/encoding/nbt-encode.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 266.5 | **LOC:** 607 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.9491%), Tech Debt (10.4606%)
**Top Internal Functions/Classes:**
  * `INT32-BYTES` **(Interface Declarations)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 97`, `args: 172`, `func_start: 1`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 98`, `dead_code: 15`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 18`, `import: 20`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ASSERT, DD-NBT-ENCODER
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/encoding/json-parse.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 261.92 | **LOC:** 651 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MissingEnd` **(Tests & Verification)** (Impact: 2.0)
  * `Simple` **(State Mutators)** (Impact: 1.4)
  * `Missing` **(Interface Declarations)** (Impact: 1.4)
  * `Simple` **(State Mutators)** (Impact: 1.4)
  * `Missing` **(Interface Declarations)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 68`, `args: 195`, `func_start: 55`, `class_start: 14`
* *Risk/State:* `state_mutation: 173`, `planned_debt: 1`, `unreferenced_by_name: 24`
* *Architecture:* `import: 128`
* *Defense:* `test: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` TEST-ASSERT, TEST-CASE, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/encoding/nbt-decode.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 257.64 | **LOC:** 625 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.8963%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `NotAtEnd` **(Interface Declarations)** (Impact: 2.5)
  * `AtEnd` **(State Mutators)** (Impact: 2.4)
  * `Basic` **(Interface Declarations)** (Impact: 1.6)
  * `WithinCompound` **(Interface Declarations)** (Impact: 1.5)
  * `NestedCompound` **(Interface Declarations)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 73`, `args: 153`, `func_start: 51`, `class_start: 15`
* *Risk/State:* `state_mutation: 157`, `unreferenced_by_name: 20`
* *Architecture:* `import: 131`
* *Defense:* `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DD-NBT-DECODER, TEST-ASSERT, TEST-CASE, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parsers/recipe/shaped.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 240.84 | **LOC:** 360 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.3422%), Tech Debt (16.6107%)
**Top Internal Functions/Classes:**
  * `PATTERN-SLOTS` **(Compute Cores)** (Impact: 52.5)
  * `ParseKey` **(Compute Cores)** (Impact: 26.4)
  * `ParsePattern` **(Interface Declarations)** (Impact: 7.2)
  * `PATTERN-KEYS` **(I/O & Config Routines)** (Impact: 3.4)
    * *Intent:* *> key
  * `PATTERN-TEXT` **(I/O & Config Routines)** (Impact: 2.1)
    * *Intent:* *> pattern; first as text (such as rows like "/_/" or "## "), then as resolved item IDs
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 75`, `args: 66`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 61`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DD-RECIPES, DD-TAGS
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/world/entities.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 239.9 | **LOC:** 450 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.9711%), Tech Debt (99.8352%)
**Top Internal Functions/Classes:**
  * `LK-ENTITY` **(I/O & Config Routines)** (Impact: 12.6)
  * `LK-ENTITY` **(I/O & Config Routines)** (Impact: 11.1)
  * `LK-ENTITY` **(Interface Declarations)** (Impact: 7.0)
    * *Intent:* *> The entity data. ID, UUID, and some internal data will be set by this program.
  * `SendMetadata` **(I/O & Config Routines)** (Impact: 6.8)
  * `LK-VELOCITY` **(I/O & Config Routines)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 69`, `args: 64`, `func_start: 16`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 80`, `planned_debt: 3`, `duplicate_logic: 6`, `unreferenced_by_name: 2`
* *Architecture:* `api: 8`, `import: 25`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` DD-CHUNK-ENTITY, DD-CHUNK-REF, DD-CLIENT-STATES, DD-CLIENTS, DD-ENTITY, DD-INVENTORY-SLOT, DD-PLAYERS, DD-SERVER-PROPERTIES...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/encoding/encode.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 234.4 | **LOC:** 654 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Simple` **(Interface Declarations)** (Impact: 1.6)
  * `HelloWorld` **(Interface Declarations)** (Impact: 1.5)
  * `WikiVgExample` **(Interface Declarations)** (Impact: 1.5)
  * `Empty` **(State Mutators)** (Impact: 1.5)
  * `ByteMin` **(Interface Declarations)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 68`, `args: 182`, `func_start: 69`, `class_start: 14`
* *Risk/State:* `state_mutation: 133`, `duplicate_logic: 6`, `unreferenced_by_name: 18`
* *Architecture:* `import: 153`
* *Defense:* `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` DD-INVENTORY-SLOT, TEST-ASSERT, TEST-CASE, TEST-SKIP, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/blocks.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 203.64 | **LOC:** 615 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.3271%), Tech Debt (10.4072%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 188`, `args: 165`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 51`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 65`, `import: 17`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DD-BLOCK-STATE, DD-BLOCKS
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/inventory/inventory.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 200.18 | **LOC:** 377 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.2235%), Tech Debt (46.9229%)
**Top Internal Functions/Classes:**
  * `MatchShapedRecipes` **(Compute Cores)** (Impact: 19.6)
  * `LK-INVENTORY` **(I/O & Config Routines)** (Impact: 14.0)
  * `TEMP-SLOT` **(I/O & Config Routines)** (Impact: 12.6)
  * `LK-ITEM` **(Interface Declarations)** (Impact: 10.2)
  * `FindEmptySlot` **(I/O & Config Routines)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 91`, `args: 26`, `func_start: 13`, `class_start: 6`
* *Risk/State:* `state_mutation: 50`, `dead_code: 4`, `planned_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 37`, `api: 6`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` DD-CLIENTS, DD-INVENTORY-SLOT, DD-PLAYERS, DD-RECIPES
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/encoding/decode.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 192.78 | **LOC:** 579 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `NegativeMax` **(Interface Declarations)** (Impact: 1.6)
  * `ByteNegative128` **(Interface Declarations)** (Impact: 1.4)
  * `ShortMax` **(Interface Declarations)** (Impact: 1.4)
  * `ShortMin` **(Interface Declarations)** (Impact: 1.4)
  * `IntMax` **(Interface Declarations)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 68`, `args: 164`, `func_start: 54`, `class_start: 14`
* *Risk/State:* `state_mutation: 111`, `unreferenced_by_name: 15`
* *Architecture:* `import: 123`
* *Defense:* `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DD-INVENTORY-SLOT, TEST-ASSERT, TEST-CASE, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/packets/clientbound/play/chunkdata.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 188.54 | **LOC:** 291 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.722%), Tech Debt (34.4441%)
**Top Internal Functions/Classes:**
  * `LK-BLOCK-ENTITIES` **(Compute Cores)** (Impact: 32.0)
  * `LK-SECTIONS` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 43`, `args: 90`, `func_start: 2`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 69`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 19`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DD-BLOCK-ENTITY, DD-CALLBACKS, DD-NBT-ENCODER, DD-PACKET, PROC-PACKET-INIT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/encoding/nbt-encode.test.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 183.44 | **LOC:** 551 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `NamedString` **(Interface Declarations)** (Impact: 1.6)
  * `NamedByte` **(Interface Declarations)** (Impact: 1.5)
  * `NamedShort` **(Interface Declarations)** (Impact: 1.5)
  * `NamedInt` **(Interface Declarations)** (Impact: 1.5)
  * `Basic` **(Interface Declarations)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 78`, `args: 125`, `func_start: 37`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 122`, `unreferenced_by_name: 21`
* *Architecture:* `import: 105`
* *Defense:* `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DD-NBT-ENCODER, TEST-ASSERT, TEST-CASE, TEST-SUITE, TEST-UNIT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/encoding/decode.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 172.32 | **LOC:** 419 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.6753%), Tech Debt (26.7963%)
**Top Internal Functions/Classes:**
  * `BYTE-ALPHA` **(I/O & Config Routines)** (Impact: 10.5)
  * `LK-VALUE` **(I/O & Config Routines)** (Impact: 6.4)
  * `LK-SLOT` **(Interface Declarations)** (Impact: 5.8)
  * `VALUE-BYTES` **(Interface Declarations)** (Impact: 4.2)
  * `VALUE-BYTES` **(Interface Declarations)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 92`, `args: 64`, `func_start: 12`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 60`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ASSERT, DD-INVENTORY-SLOT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/players/players.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 170.58 | **LOC:** 440 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.9139%), Tech Debt (34.9981%)
**Top Internal Functions/Classes:**
  * `HandleHitGround` **(I/O & Config Routines)** (Impact: 15.9)
  * `LK-FLAGS` **(I/O & Config Routines)** (Impact: 11.7)
  * `BuildDeathMessage` **(I/O & Config Routines)** (Impact: 6.7)
  * `PickDamageSound` **(I/O & Config Routines)** (Impact: 5.7)
  * `TickPlayer` **(I/O & Config Routines)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 79`, `args: 48`, `func_start: 9`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 51`, `dead_code: 1`, `planned_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` DD-CLIENT-STATES, DD-CLIENTS, DD-PLAYERS, DD-SERVER-PROPERTIES
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/world/blocks.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 167.7 | **LOC:** 314 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.772%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `LK-POSITION` **(Compute Cores)** (Impact: 16.1)
  * `LK-POSITION` **(I/O & Config Routines)** (Impact: 9.2)
  * `LK-POSITION` **(Interface Declarations)** (Impact: 6.5)
  * `LK-BLOCK-ENTITY` **(Interface Declarations)** (Impact: 4.2)
  * `LK-POSITION` **(Interface Declarations)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 33 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 69`, `args: 48`, `func_start: 7`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `dead_code: 2`
* *Architecture:* `api: 6`, `import: 22`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` DD-BLOCK-ENTITY, DD-CALLBACKS, DD-CHUNK-REF, DD-CLIENT-STATES, DD-CLIENTS, DD-SERVER-PROPERTIES, DD-WORLD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/players/player-io.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 167.2 | **LOC:** 376 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.9354%), Tech Debt (12.1994%)
**Top Internal Functions/Classes:**
  * `INVENTORY-SLOT` **(Compute Cores)** (Impact: 56.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 42`, `args: 227`, `func_start: 1`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 44`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DD-INVENTORY-SLOT, DD-NBT-DECODER, DD-NBT-ENCODER, DD-PLAYERS, DD-SERVER-PROPERTIES
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/callbacks.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 165.36 | **LOC:** 563 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.9601%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 189`, `args: 56`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 50`
* *Architecture:* `api: 28`, `import: 29`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DD-CALLBACKS
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server-properties.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 164.6 | **LOC:** 235 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.0724%), Tech Debt (15.8869%)
**Top Internal Functions/Classes:**
  * `AppendKeyValue` **(I/O & Config Routines)** (Impact: 1.7)
  * `AppendNewline` **(I/O & Config Routines)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 53`, `args: 22`, `func_start: 2`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 54`, `planned_debt: 2`
* *Architecture:* `io: 7`, `api: 40`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DD-SERVER-PROPERTIES
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/encoding/encode.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 162.1 | **LOC:** 413 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.8709%), Tech Debt (20.8609%)
**Top Internal Functions/Classes:**
  * `BYTE-ALPHA` **(I/O & Config Routines)** (Impact: 14.8)
  * `LK-VALUE-IN` **(I/O & Config Routines)** (Impact: 8.7)
  * `VALUE-BYTES` **(Interface Declarations)** (Impact: 2.8)
  * `LK-SLOT` **(Interface Declarations)** (Impact: 2.8)
  * `VALUE-BYTES` **(Interface Declarations)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 93`, `args: 57`, `func_start: 13`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 56`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DD-INVENTORY-SLOT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/encoding/decode.cob` -> **Simon Sobisch** (100.0% isolated ownership) | Magnitude: 172.32
- `src/world/world.cob` -> **Simon Sobisch** (100.0% isolated ownership) | Magnitude: 105.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/_copybooks/assert/ASSERT.cpy` -> **Severity: 4.41** (Embedded: 0.0625 * Error Risk: 70.5637%)
- `src/_copybooks/callbacks/DD-CALLBACK-ITEM-USE.cpy` -> **Severity: 2.986** (Embedded: 0.0478 * Error Risk: 62.4806%)
- `src/_copybooks/callbacks/DD-CALLBACK-BLOCK-FACE.cpy` -> **Severity: 2.297** (Embedded: 0.0368 * Error Risk: 62.4806%)
- `src/_copybooks/assert/ASSERT-FAILED.cpy` -> **Severity: 1.557** (Embedded: 0.0221 * Error Risk: 70.5637%)
- `src/_copybooks/constants/DD-COMMAND-CONSTANTS.cpy` -> **Severity: 1.302** (Embedded: 0.0221 * Error Risk: 59.0077%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/_copybooks/state/DD-CALLBACKS.cpy` -> **Severity: 561.3** (Blast Radius: 5.613 * Doc Risk: 100.0%)
- `src/_copybooks/state/DD-RECIPES.cpy` -> **Severity: 553.2** (Blast Radius: 5.532 * Doc Risk: 100.0%)
- `src/_copybooks/structs/DD-CHUNK-REF.cpy` -> **Severity: 386.9** (Blast Radius: 3.869 * Doc Risk: 100.0%)
- `src/_copybooks/structs/DD-CHUNK-ENTITY.cpy` -> **Severity: 359.9** (Blast Radius: 3.599 * Doc Risk: 100.0%)
- `codegen/_copybooks/DD-CODEGEN-DIR-LIST.cpy` -> **Severity: 354.7** (Blast Radius: 3.547 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
