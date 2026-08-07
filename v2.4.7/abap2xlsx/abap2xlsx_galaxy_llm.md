# ARCHITECTURAL_BRIEF: abap2xlsx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/abap2xlsx` |
| **Timestamp** | `2026-08-07T03:46:27.439592+00:00` |
| **Scan Duration** | `1.15s` |
| **Git Branch** | `main` |
| **Git Commit** | `f33b94c8efbe3f5228aa6bdb85ecedf25e0b5def` |
| **Git Remote** | `https://github.com/abap2xlsx/abap2xlsx.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 103 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 407 |
| Analyzed Artifacts (Scanned) | 389 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 32529 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 95.6% |
| Dominant Lang | ABAP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| XML | 276 | 0 | 71.0% |
| ABAP | 103 | 32192 | 26.5% |
| JSON | 4 | 335 | 1.0% |
| MARKDOWN | 3 | 0 | 0.8% |
| PLAINTEXT | 2 | 1 | 0.5% |
| YAML | 1 | 1 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.817`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 383 | 98.5% |
| Unknown | 1 | 0.3% |
| file_cluster_9 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 1.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 18*

**Composition by Extension & Reason:**
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.abap`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 56.7 | 6.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 91.6 | 6.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 16.5 | 0.1 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 2.3 | 0.7 | 0.2 | 0.2 |
| API Exposure | 0.0 | 5.3 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 43.0 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 31.8 | 6.7 | 6.7 |
| Instability Exposure | 0.0 | 3.2 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 92.0 | 11.7 | 4.3 | 0.8 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/not_cloud/zcl_excel_converter_alv.clas.abap` (Hits: 37)
- `src/zcl_excel_reader_2007.clas.abap` (Hits: 17)
- `src/not_cloud/zcl_excel_converter.clas.abap` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **SECURITY.md** (`SECURITY.md`) — 0 inbound connections
4. **_config.yml** (`_config.yml`) — 0 inbound connections
5. **abap_transpile.json** (`abap_transpile.json`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **zcl_excel_reader_huge_file.clas.abap** (`src/zcl_excel_reader_huge_file.clas.abap`) — 1 outbound dependencies
2. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 outbound dependencies
3. **README.md** (`README.md`) — 0 outbound dependencies
4. **SECURITY.md** (`SECURITY.md`) — 0 outbound dependencies
5. **_config.yml** (`_config.yml`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `get_reference` (@ `src/zcl_excel_table.clas.abap`) -> Impact: **5.7** | LOC: 33
- `assert` (@ `src/zcl_excel_worksheet.clas.testclasses.abap`) -> Impact: **5.0** | LOC: 15
- `escape_string_value` (@ `src/zcl_excel_writer_2007.clas.abap`) -> Impact: **5.0** | LOC: 20
- `assert` (@ `src/zcl_excel_worksheet.clas.testclasses.abap`) -> Impact: **3.3** | LOC: 9
- `assert` (@ `src/zcl_excel_worksheet.clas.testclasses.abap`) -> Impact: **2.5** | LOC: 11
- `utclong_to_excel_string` (@ `src/zcl_excel_common.clas.abap`) -> Impact: **2.1** | LOC: 13
  * *Intent:* *--------------------------------------------------------------------* * Check for range names *------------------------------------------------------...
- `run_cut` (@ `src/zcl_excel_reader_2007.clas.testclasses.abap`) -> Impact: **1.4** | LOC: 7
- `assert` (@ `src/zcl_excel_worksheet.clas.testclasses.abap`) -> Impact: **1.4** | LOC: 7
- `class_constructor` (@ `src/zcl_excel_worksheet.clas.abap`) -> Impact: **1.2** | LOC: 5
- `escaped_character_inside_text` (@ `src/zcl_excel_reader_2007.clas.testclasses.abap`) -> Impact: **1.1** | LOC: 2

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 335 | 110101.53 | 5.91% | 0.17% |
| `src/not_cloud` | 44 | 40948.53 | 7.3% | 0.0% |
| `__monolith__` | 10 | 5081.22 | 1.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/zcl_excel_worksheet.clas.testclasses.abap` -> **16.5339%** Exposure
- `src/zcl_excel_writer_huge_file.clas.abap` -> **11.6098%** Exposure
- `src/zcl_excel_common.clas.abap` -> **10.8574%** Exposure
- `src/zcl_excel_reader_2007.clas.abap` -> **8.6804%** Exposure
- `src/zcl_excel_writer_2007.clas.locals_imp.abap` -> **8.4495%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/zcl_excel_legacy_palette.clas.abap` -> **100.0%** Exposure
- `src/not_cloud/zexcel_template_get_types.prog.abap` -> **99.7507%** Exposure
- `src/not_cloud/zcl_excel_converter_alv.clas.abap` -> **92.6088%** Exposure
- `src/zcl_excel_fill_template.clas.abap` -> **75.1593%** Exposure
- `src/zcl_excel_writer_huge_file.clas.abap` -> **58.9413%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/zcl_excel_worksheet.clas.testclasses.abap` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/zcl_excel_writer_huge_file.clas.abap`** -> AI Confidence: **99.29%**
2. **`src/not_cloud/zcl_excel_converter_alv.clas.abap`** -> AI Confidence: **99.17%**
3. **`src/not_cloud/zexcel_template_get_types.prog.abap`** -> AI Confidence: **99.17%**
4. **`src/zcl_excel_graph_bars.clas.abap`** -> AI Confidence: **99.17%**
5. **`src/zcl_excel_graph_line.clas.abap`** -> AI Confidence: **99.17%**
6. **`src/zcl_excel_writer_2007.clas.locals_imp.abap`** -> AI Confidence: **99.17%**
7. **`src/zcl_excel_reader_2007.clas.abap`** -> AI Confidence: **99.11%**
8. **`src/not_cloud/zcl_excel_converter.clas.abap`** -> AI Confidence: **99.06%**
9. **`src/not_cloud/zcl_excel_converter_result.clas.abap`** -> AI Confidence: **99.06%**
10. **`src/not_cloud/zcl_excel_converter_result_wd.clas.abap`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/zcl_excel_legacy_palette.clas.abap` (ABAP) -> Cumulative Risk: **375.08**
- **Archetype:** `file_cluster_8` (Distance: 10.802 IQR)
- **Magnitude:** 196.82 | **LOC:** 162 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (91.6498%), Cognitive Load (56.6825%)

### 2. `src/not_cloud/zexcel_template_get_types.prog.abap` (ABAP) -> Cumulative Risk: **319.92**
- **Archetype:** `file_cluster_8` (Distance: 10.775 IQR)
- **Magnitude:** 1815.89 | **LOC:** 385 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7507%), Safety Score (70.6337%), Cognitive Load (33.6398%)

### 3. `src/zcl_excel_reader_2007.clas.abap` (ABAP) -> Cumulative Risk: **312.23**
- **Archetype:** `file_cluster_8` (Distance: 10.751 IQR)
- **Magnitude:** 51579.44 | **LOC:** 4488 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Safety Score (42.5507%), State Flux (25.5146%)

### 4. `src/not_cloud/zcl_excel_converter_alv.clas.abap` (ABAP) -> Cumulative Risk: **298.67**
- **Archetype:** `file_cluster_8` (Distance: 10.349 IQR)
- **Magnitude:** 1628.68 | **LOC:** 601 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (92.6088%), Safety Score (69.1119%), Cognitive Load (20.9064%)

### 5. `src/zcl_excel_worksheet_pagebreaks.clas.abap` (ABAP) -> Cumulative Risk: **282.06**
- **Archetype:** `file_cluster_8` (Distance: 6.387 IQR)
- **Magnitude:** 34.94 | **LOC:** 51 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (72.5237%), Documentation (64.332%), State Flux (30.7959%)

### 6. `src/not_cloud/zcl_excel_ole.clas.locals_def.abap` (ABAP) -> Cumulative Risk: **276.55**
- **Archetype:** `file_cluster_8` (Distance: 6.206 IQR)
- **Magnitude:** 17.46 | **LOC:** 47 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (80.27%), Safety Score (79.5835%), Cognitive Load (10.6174%)

### 7. `src/zcl_excel_fill_template.clas.abap` (ABAP) -> Cumulative Risk: **267.29**
- **Archetype:** `file_cluster_8` (Distance: 9.831 IQR)
- **Magnitude:** 2144.09 | **LOC:** 650 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (75.1593%), Safety Score (60.9955%), Cognitive Load (14.3267%)

### 8. `src/zcl_excel_autofilters.clas.abap` (ABAP) -> Cumulative Risk: **267.14**
- **Archetype:** `file_cluster_8` (Distance: 7.423 IQR)
- **Magnitude:** 173.25 | **LOC:** 121 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (62.3217%), Documentation (48.1197%), Churn (26.09%)

### 9. `src/not_cloud/zcl_excel_ole.clas.abap` (ABAP) -> Cumulative Risk: **266.23**
- **Archetype:** `file_cluster_8` (Distance: 11.63 IQR)
- **Magnitude:** 15822.08 | **LOC:** 2092 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (58.0152%), State Flux (32.0073%), Churn (26.09%)

### 10. `src/zcl_excel_writer_2007.clas.locals_imp.abap` (ABAP) -> Cumulative Risk: **263.68**
- **Archetype:** `file_cluster_8` (Distance: 9.396 IQR)
- **Magnitude:** 5709.36 | **LOC:** 1834 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (48.6322%), Churn (45.2%), State Flux (26.8639%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/zcl_excel_reader_2007.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.751 IQR)
- **Top Global Matches:** file_cluster_8: 10.751, file_cluster_7: 11.536, file_cluster_0: 11.738
- **Magnitude:** 51579.44 | **LOC:** 4488 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (9.7492%), Tech Debt (8.6804%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 175`, `args: 160`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 79`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 17`, `api: 1`
* *Defense:* `safety: 181`, `immutability_locks: 9`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zcl_excel_converter.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.97 IQR)
- **Top Global Matches:** file_cluster_8: 9.97, file_cluster_7: 10.74, file_cluster_16: 10.932
- **Magnitude:** 18651.92 | **LOC:** 1818 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.8756%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 105`, `args: 68`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 46`, `dead_code: 2`
* *Architecture:* `io: 12`, `api: 1`
* *Defense:* `safety: 41`, `immutability_locks: 5`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zcl_excel_ole.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.63 IQR)
- **Top Global Matches:** file_cluster_8: 11.63, file_cluster_0: 12.024, file_cluster_9: 12.073
- **Magnitude:** 15822.08 | **LOC:** 2092 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.288%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 159`, `args: 61`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 48`, `dead_code: 26`
* *Architecture:* `io: 9`, `api: 1`
* *Defense:* `safety: 15`, `doc: 1`, `immutability_locks: 1`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_drawing.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.97 IQR)
- **Top Global Matches:** file_cluster_8: 8.97, file_cluster_7: 9.929, file_cluster_1: 10.127
- **Magnitude:** 13017.62 | **LOC:** 1137 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.472%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 84`, `args: 270`, `func_start: 24`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 38`, `immutability_locks: 18`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_style_changer.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.183 IQR)
- **Top Global Matches:** file_cluster_8: 8.183, file_cluster_7: 9.225, file_cluster_1: 9.391
- **Magnitude:** 7700.7 | **LOC:** 1673 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6596%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 106`, `args: 32`, `func_start: 98`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`
* *Defense:* `safety: 9`, `immutability_locks: 2`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_writer_2007.clas.locals_imp.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.396 IQR)
- **Top Global Matches:** file_cluster_8: 9.396, file_cluster_7: 10.285, file_cluster_1: 10.503
- **Magnitude:** 5709.36 | **LOC:** 1834 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (8.8869%), Tech Debt (8.4495%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 51`, `args: 8`, `func_start: 23`
* *Risk/State:* `state_mutation: 42`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 44`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_theme_font_scheme.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.616 IQR)
- **Top Global Matches:** file_cluster_8: 9.616, file_cluster_7: 10.504, file_cluster_0: 10.714
- **Magnitude:** 2604.67 | **LOC:** 505 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.3941%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 38`, `args: 11`, `func_start: 10`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 4`, `api: 1`
* *Defense:* `safety: 38`, `immutability_locks: 14`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_fill_template.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.831 IQR)
- **Top Global Matches:** file_cluster_8: 9.831, file_cluster_7: 10.622, file_cluster_16: 10.727
- **Magnitude:** 2144.09 | **LOC:** 650 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.3267%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 28`, `args: 11`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 39`
* *Architecture:* `api: 1`
* *Defense:* `safety: 9`, `immutability_locks: 6`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_theme_color_scheme.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.198 IQR)
- **Top Global Matches:** file_cluster_8: 9.198, file_cluster_7: 10.175, file_cluster_1: 10.352
- **Magnitude:** 2136.3 | **LOC:** 448 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.549%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 35`, `args: 5`, `func_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `safety: 37`, `immutability_locks: 19`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_writer_csv.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.711 IQR)
- **Top Global Matches:** file_cluster_8: 8.711, file_cluster_7: 9.614, file_cluster_1: 9.873
- **Magnitude:** 2085.26 | **LOC:** 378 | **CtrlFlow:** 68.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.2379%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 21`, `args: 16`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `safety: 10`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_writer_huge_file.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.43 IQR)
- **Top Global Matches:** file_cluster_8: 9.43, file_cluster_7: 10.283, file_cluster_1: 10.521
- **Magnitude:** 1842.2 | **LOC:** 817 | **CtrlFlow:** 81.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.4135%), Tech Debt (11.6098%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 17`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 37`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `safety: 15`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zexcel_template_get_types.prog.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.775 IQR)
- **Top Global Matches:** file_cluster_8: 10.775, file_cluster_2: 11.243, file_cluster_17: 11.437
- **Magnitude:** 1815.89 | **LOC:** 385 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.6398%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 13`, `args: 14`, `func_start: 4`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* `io: 2`
* *Defense:* `safety: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_reader_huge_file.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.034 IQR)
- **Top Global Matches:** file_cluster_8: 8.034, file_cluster_7: 9.048, file_cluster_13: 9.269
- **Magnitude:** 1737.0 | **LOC:** 334 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.8709%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 29`, `args: 15`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 5`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TYPE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_graph_bars.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.012 IQR)
- **Top Global Matches:** file_cluster_8: 7.012, file_cluster_7: 8.165, file_cluster_1: 8.385
- **Magnitude:** 1734.24 | **LOC:** 284 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.9508%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 23`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_graph_line.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.014 IQR)
- **Top Global Matches:** file_cluster_8: 7.014, file_cluster_7: 8.168, file_cluster_1: 8.387
- **Magnitude:** 1733.2 | **LOC:** 282 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.0772%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 23`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zcl_excel_converter_alv.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.349 IQR)
- **Top Global Matches:** file_cluster_8: 10.349, file_cluster_16: 10.92, file_cluster_7: 11.073
- **Magnitude:** 1628.68 | **LOC:** 601 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.9064%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 21`, `args: 3`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 56`
* *Architecture:* `io: 37`, `api: 1`
* *Defense:* `safety: 13`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_common.clas.testclasses.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.252 IQR)
- **Top Global Matches:** file_cluster_8: 8.252, file_cluster_7: 9.316, file_cluster_1: 9.458
- **Magnitude:** 1585.44 | **LOC:** 1856 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3762%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 156`, `args: 15`, `func_start: 89`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* None
* *Defense:* `safety: 30`, `test: 189`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_sheet_setup.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.707 IQR)
- **Top Global Matches:** file_cluster_8: 8.707, file_cluster_7: 9.736, file_cluster_1: 9.929
- **Magnitude:** 1353.04 | **LOC:** 479 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.4213%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 42`, `args: 5`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `safety: 31`, `immutability_locks: 82`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_autofilter.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.285 IQR)
- **Top Global Matches:** file_cluster_8: 8.285, file_cluster_7: 9.229, file_cluster_1: 9.453
- **Magnitude:** 1231.2 | **LOC:** 431 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.8189%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 37`, `args: 13`, `func_start: 14`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 1`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zcl_excel_converter_salv_table.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.313 IQR)
- **Top Global Matches:** file_cluster_8: 8.313, file_cluster_7: 9.244, file_cluster_2: 9.368
- **Magnitude:** 1074.85 | **LOC:** 274 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.1612%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 16`, `args: 28`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `dead_code: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 5`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zcl_excel_converter_result_wd.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.11 IQR)
- **Top Global Matches:** file_cluster_8: 9.11, file_cluster_7: 9.977, file_cluster_16: 10.015
- **Magnitude:** 907.92 | **LOC:** 251 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0042%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 8`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `safety: 7`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_row.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.269 IQR)
- **Top Global Matches:** file_cluster_8: 9.269, file_cluster_7: 10.135, file_cluster_9: 10.172
- **Magnitude:** 739.49 | **LOC:** 238 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.9107%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 26`, `args: 14`, `func_start: 14`
* *Risk/State:* `dead_code: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 6`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_reader_huge_file.clas.testclasses.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.316 IQR)
- **Top Global Matches:** file_cluster_8: 9.316, file_cluster_7: 10.196, file_cluster_1: 10.416
- **Magnitude:** 639.52 | **LOC:** 400 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.8576%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 41`, `args: 13`, `func_start: 19`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* None
* *Defense:* `safety: 10`, `test: 35`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.762 IQR)
- **Top Global Matches:** file_cluster_8: 6.762, file_cluster_7: 7.968, file_cluster_1: 8.133
- **Magnitude:** 530.6 | **LOC:** 701 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.2694%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 23`, `args: 37`, `func_start: 7`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/zcx_excel.clas.abap` (ABAP) | Magnitude: 220.0 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 7, branch: 6, args: 6
- `src/zcl_excel_template_data.clas.abap` (ABAP) | Magnitude: 26.7 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 26, pointers: 10, structural_boundaries: 5, generics: 4
- `src/not_cloud/zcl_excel_ole.clas.abap` (ABAP) | Magnitude: 15822.08 | Delta: **0.394 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1409, pointers: 247, branch: 190, structural_boundaries: 159
- `src/not_cloud/zexcel_template_get_types.prog.abap` (ABAP) | Magnitude: 1815.89 | Delta: **0.468 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 240, pointers: 69, state_mutation: 53, branch: 41
- `src/not_cloud/zcl_excel_converter_alv.clas.abap` (ABAP) | Magnitude: 1628.68 | Delta: **0.571 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 482, pointers: 107, branch: 65, state_mutation: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/zcl_excel_obsolete_func_wrap.clas.abap` (ABAP) | Magnitude: 37.08 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, encapsulation: 2, branch: 1, structural_boundaries: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/not_cloud/zcl_excel_converter.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 18651.92
- `src/not_cloud/zcl_excel_ole.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 15822.08
- `src/zcl_excel.clas.abap` -> **Abo** (100.0% isolated ownership) | Magnitude: 530.6
- `src/zcl_excel_reader_2007.clas.locals_imp.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 518.04
- `src/zcl_excel_autofilters.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 173.25

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/zif_excel_reader.intf.abap` -> **Severity: 236.513** (Blast Radius: 2.571 * Doc Risk: 91.9928%)
- `src/not_cloud/zcl_excel_ole.clas.locals_def.abap` -> **Severity: 206.374** (Blast Radius: 2.571 * Doc Risk: 80.27%)
- `src/zcl_excel_obsolete_func_wrap.clas.abap` -> **Severity: 200.49** (Blast Radius: 2.571 * Doc Risk: 77.9812%)
- `src/zcl_excel_security.clas.abap` -> **Severity: 184.449** (Blast Radius: 2.571 * Doc Risk: 71.7422%)
- `src/zif_excel_book_protection.intf.abap` -> **Severity: 180.5** (Blast Radius: 2.571 * Doc Risk: 70.2063%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
