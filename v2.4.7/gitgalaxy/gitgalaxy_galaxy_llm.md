# ARCHITECTURAL_BRIEF: gitgalaxy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/gitgalaxy` |
| **Timestamp** | `2026-08-07T04:59:13.902305+00:00` |
| **Scan Duration** | `1.88s` |
| **Git Branch** | `main` |
| **Git Commit** | `6d4138bf29d304c22e10e06ec9dfe1ea10948cd7` |
| **Git Remote** | `https://github.com/squid-protocol/gitgalaxy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 42 malicious artifacts.

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
| Total Artifacts | 657 |
| Analyzed Artifacts (Scanned) | 52 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 605 |
| Total LOC | 19076 |
| Volatility Index | 0.115 |
| % Scanned of codebase = | 7.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2037 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7693 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8022 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 26 | 4098 | 50.0% |
| PYTHON | 16 | 12671 | 30.8% |
| HTML | 4 | 1917 | 7.7% |
| MARKDOWN | 2 | 0 | 3.8% |
| PLAINTEXT | 2 | 0 | 3.8% |
| CSS | 2 | 390 | 3.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.22`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 33 | 63.5% |
| file_cluster_17 | 3 | 5.8% |
| file_cluster_2 | 3 | 5.8% |
| file_cluster_13 | 3 | 5.8% |
| file_cluster_4 | 3 | 5.8% |
| file_cluster_0 | 1 | 1.9% |
| file_cluster_9 | 1 | 1.9% |
| file_cluster_16 | 1 | 1.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 7.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 605*

**Composition by Extension & Reason:**
- `.js`: 390x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 59x Excluded (Explicitly Denied Extension: '.png')
- `.db`: 12x Excluded (Unsupported Extension: '.db')
- `.sqlite`: 10x Excluded (Unsupported Extension: '.sqlite')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 8980 commas in 1082 LOC), 1x Excluded (Machine-Generated Source Code Signature: 453 LOC)
- `.wasm`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.odt`: 3x Excluded (Explicitly Denied Extension: '.odt')
- `.html`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 1x Excluded (Machine-Generated Source Code Signature: 244 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 93.3 | 29.2 | 24.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.5 | 64.7 | 67.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 33.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 40.8 | 41.4 | 80.0 |
| API Exposure | 0.0 | 8.6 | 2.7 | 2.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 65.8 | 92.9 | 100.0 |
| Commented Logic Exposure | 0.0 | 98.5 | 2.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 95.0 | 34.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 28.0 | 24.5 | 0.0 |
| Documentation Exposure | 1.2 | 99.1 | 22.3 | 17.9 | 17.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `gitgalaxy/language_standards.py` (Hits: 29)
- `gitgalaxy/galaxyscope.py` (Hits: 10)
- `airgap_observatory/index.html` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **language_standards.py** (`gitgalaxy/language_standards.py`) — 4 inbound connections
2. **gitgalaxy_config.py** (`gitgalaxy/gitgalaxy_config.py`) — 3 inbound connections
3. **audit_recorder.py** (`gitgalaxy/audit_recorder.py`) — 1 inbound connections
4. **chronometer.py** (`gitgalaxy/chronometer.py`) — 1 inbound connections
5. **detector.py** (`gitgalaxy/detector.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **galaxyscope.py** (`gitgalaxy/galaxyscope.py`) — 39 outbound dependencies
2. **detector.py** (`gitgalaxy/detector.py`) — 10 outbound dependencies
3. **audit_recorder.py** (`gitgalaxy/audit_recorder.py`) — 9 outbound dependencies
4. **language_lens.py** (`gitgalaxy/language_lens.py`) — 8 outbound dependencies
5. **llm_recorder.py** (`gitgalaxy/llm_recorder.py`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_parse_threat_score` (@ `gitgalaxy/llm_recorder.py`) -> Impact: **492.9** | LOC: 852
- `run_mission` (@ `gitgalaxy/galaxyscope.py`) -> Impact: **424.2** | LOC: 1105
- `summarize_galaxy_metrics` (@ `gitgalaxy/signal_processor.py`) -> Impact: **403.0** | LOC: 900
- `generate_report` (@ `gitgalaxy/audit_recorder.py`) -> Impact: **270.6** | LOC: 434
- `_tier_2_fingerprint_check` (@ `gitgalaxy/language_lens.py`) -> Impact: **227.4** | LOC: 388
  * *Intent:* # THE FIX: If the extension is highly contested, refuse to lock it at Tier 1. # This forces the pipeline to fall back to Tier 1.5 Ecosystem Gravity # ...
- `calculate_risk_vector` (@ `gitgalaxy/signal_processor.py`) -> Impact: **161.2** | LOC: 361
- `_calibrate_matrix` (@ `gitgalaxy/prism.py`) -> Impact: **147.3** | LOC: 313
- `audit` (@ `gitgalaxy/spectral_auditor.py`) -> Impact: **141.5** | LOC: 336
  * *Intent:* # Save the language definitions so we can check for execution geometry later self.lang_defs = lang_defs or {} # SCHEMA CONSTANTS (32 Signal Keys repre...
- `updateHUD` (@ `airgap_observatory/index.html`) -> Impact: **135.7** | LOC: 168
- `copyHUDData` (@ `airgap_observatory/index.html`) -> Impact: **130.6** | LOC: 187

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `gitgalaxy` | 15 | 7936.56 | 26.67% | 7.2% |
| `airgap_observatory/core` | 5 | 1832.6 | 45.45% | 42.2% |
| `airgap_observatory/lib/three/addons/utils` | 15 | 1795.84 | 23.79% | 42.1% |
| `airgap_observatory` | 2 | 1190.4 | 89.26% | 76.98% |
| `airgap_observatory/config` | 1 | 116.32 | 7.82% | 32.49% |
| `__monolith__` | 5 | 16.26 | 1.0% | 0.0% |
| `airgap_observatory/lib/three/addons/tsl/utils` | 1 | 7.88 | 3.23% | 0.0% |
| `airgap_observatory/css` | 2 | 1.79 | 5.05% | 14.69% |
| `airgap_observatory/tools` | 6 | 0.63 | 35.73% | 69.27% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `airgap_observatory/lib/three/addons/utils/SortUtils.js` -> **99.9998%** Exposure
- `airgap_observatory/tools/search.js` -> **99.9985%** Exposure
- `airgap_observatory/lib/three/addons/utils/ShadowMapViewer.js` -> **99.9748%** Exposure
- `airgap_observatory/lib/three/addons/utils/LDrawUtils.js` -> **99.9713%** Exposure
- `airgap_observatory/lib/three/addons/utils/ShadowMapViewerGPU.js` -> **99.9541%** Exposure
### Highest State Flux (Mutation/Volatility)
- `airgap_observatory/core/data-parser.js` -> **100.0%** Exposure
- `airgap_observatory/core/galaxy-engine.js` -> **100.0%** Exposure
- `airgap_observatory/core/materials.js` -> **100.0%** Exposure
- `airgap_observatory/lib/three/addons/utils/BufferGeometryUtils.js` -> **100.0%** Exposure
- `airgap_observatory/lib/three/addons/utils/GeometryCompressionUtils.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `airgap_observatory/index.html` -> **10** Orphaned Functions | **8** Duplicates
- `airgap_observatory/main.js` -> **3** Orphaned Functions | **4** Duplicates
- `airgap_observatory/core/metavisualizer.html` -> **1** Orphaned Functions | **6** Duplicates
- `airgap_observatory/lib/three/addons/utils/SortUtils.js` -> **0** Orphaned Functions | **6** Duplicates
- `airgap_observatory/tools/style_guide.html` -> **1** Orphaned Functions | **5** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`gitgalaxy/llm_recorder.py`** -> AI Confidence: **99.48%**
2. **`gitgalaxy/audit_recorder.py`** -> AI Confidence: **99.39%**
3. **`gitgalaxy/language_lens.py`** -> AI Confidence: **99.39%**
4. **`gitgalaxy/chronometer.py`** -> AI Confidence: **99.31%**
5. **`gitgalaxy/detector.py`** -> AI Confidence: **99.31%**
6. **`gitgalaxy/galaxyscope.py`** -> AI Confidence: **99.31%**
7. **`gitgalaxy/guidestar_lens.py`** -> AI Confidence: **99.31%**
8. **`gitgalaxy/security_auditor.py`** -> AI Confidence: **99.31%**
9. **`gitgalaxy/signal_processor.py`** -> AI Confidence: **99.31%**
10. **`airgap_observatory/core/galaxy-engine.js`** -> AI Confidence: **99.23%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `137` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `airgap_observatory/main.js` (JAVASCRIPT) -> Cumulative Risk: **779.64**
- **Archetype:** `file_cluster_4` (Distance: 13.031 IQR)
- **Magnitude:** 284.96 | **LOC:** 561 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9991%), Tech Debt (99.2438%)
- **Heaviest Functions:** `init` (Impact: 65.0), `toggleGlobalWeb` (Impact: 10.7), `toggleLines` (Impact: 10.6)

### 2. `airgap_observatory/core/galaxy-engine.js` (JAVASCRIPT) -> Cumulative Risk: **714.77**
- **Archetype:** `file_cluster_17` (Distance: 14.023 IQR)
- **Magnitude:** 1087.02 | **LOC:** 1137 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.3907%), Stability (94.5447%)
- **Heaviest Functions:** `handleInteraction` (Impact: 124.4), `loadSector` (Impact: 84.1), `setupEvents` (Impact: 43.6)

### 3. `airgap_observatory/tools/poster.js` (JAVASCRIPT) -> Cumulative Risk: **663.06**
- **Archetype:** `file_cluster_4` (Distance: 12.768 IQR)
- **Magnitude:** 0.25 | **LOC:** 781 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.6089%), State Flux (99.4512%), Stability (94.5447%)
- **Heaviest Functions:** `_renderTiledPrintCanvas` (Impact: 59.2), `generatePreview` (Impact: 45.1), `boostNetwork` (Impact: 12.2)

### 4. `gitgalaxy/llm_recorder.py` (PYTHON) -> Cumulative Risk: **594.31**
- **Archetype:** `file_cluster_17` (Distance: 14.19 IQR)
- **Magnitude:** 1120.06 | **LOC:** 967 | **CtrlFlow:** 85.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Safety Score (98.5318%)
- **Heaviest Functions:** `_parse_threat_score` (Impact: 492.9), `__init__` (Impact: 5.8)

### 5. `airgap_observatory/core/data-parser.js` (JAVASCRIPT) -> Cumulative Risk: **577.45**
- **Archetype:** `file_cluster_8` (Distance: 12.057 IQR)
- **Magnitude:** 239.78 | **LOC:** 265 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (94.5447%), Safety Score (91.7147%)
- **Heaviest Functions:** `transformEntity` (Impact: 36.4), `addToGroup` (Impact: 33.1), `parse` (Impact: 30.0)

### 6. `airgap_observatory/lib/three/addons/utils/SortUtils.js` (JAVASCRIPT) -> Cumulative Risk: **575.51**
- **Archetype:** `file_cluster_8` (Distance: 12.206 IQR)
- **Magnitude:** 179.26 | **LOC:** 176 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9998%), Safety Score (92.5567%)
- **Heaviest Functions:** `radixSort` (Impact: 51.9), `insertionSortBlock` (Impact: 17.5), `insertionSortBlock` (Impact: 14.1)

### 7. `airgap_observatory/tools/ally.js` (JAVASCRIPT) -> Cumulative Risk: **574.3**
- **Archetype:** `file_cluster_8` (Distance: 12.431 IQR)
- **Magnitude:** 0.06 | **LOC:** 262 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (94.5447%), Safety Score (92.8977%)
- **Heaviest Functions:** `loadGalaxy` (Impact: 6.4), `announce` (Impact: 3.1), `init` (Impact: 2.4)

### 8. `airgap_observatory/core/materials.js` (JAVASCRIPT) -> Cumulative Risk: **572.53**
- **Archetype:** `file_cluster_2` (Distance: 13.822 IQR)
- **Magnitude:** 86.24 | **LOC:** 158 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.5667%), Stability (94.5447%)
- **Heaviest Functions:** `resolveBasalColor` (Impact: 24.1), `refresh` (Impact: 11.4), `constructor` (Impact: 1.7)

### 9. `gitgalaxy/gpu_recorder.py` (PYTHON) -> Cumulative Risk: **544.03**
- **Archetype:** `file_cluster_13` (Distance: 12.355 IQR)
- **Magnitude:** 225.8 | **LOC:** 357 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (91.914%), Churn (84.64%)
- **Heaviest Functions:** `record_mission` (Impact: 114.0), `__init__` (Impact: 7.2)

### 10. `airgap_observatory/tools/perf_monitor.js` (JAVASCRIPT) -> Cumulative Risk: **541.25**
- **Archetype:** `file_cluster_2` (Distance: 13.193 IQR)
- **Magnitude:** 0.24 | **LOC:** 273 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.589%), Stability (94.5447%)
- **Heaviest Functions:** `setTheme` (Impact: 46.9), `renderStats` (Impact: 17.5), `assessQuality` (Impact: 12.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `gitgalaxy/guidestar_lens.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.904 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.296 IQR)
- **Top Global Matches:** file_cluster_8: 10.904, file_cluster_13: 11.009, file_cluster_16: 11.183
- **Magnitude:** 2775.58 | **LOC:** 353 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.6753%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 46`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 12`
* *Architecture:* `io: 6`, `api: 3`, `import: 7`
* *Defense:* `safety: 14`, `doc: 28`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 1):` typing, logging, .gitgalaxy_config, json, pathlib, re, fnmatch
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `gitgalaxy/llm_recorder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.19 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.573 IQR)
- **Top Global Matches:** file_cluster_17: 14.19, file_cluster_8: 14.213, file_cluster_13: 14.231
- **Magnitude:** 1120.06 | **LOC:** 967 | **CtrlFlow:** 85.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.8264%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_parse_threat_score` (Impact: 492.9)
  * `__init__` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 44`, `args: 27`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 592`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 12`, `import: 8`
* *Defense:* `safety: 15`, `doc: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` typing, logging, , datetime, pathlib, sqlite3, statistics, collections
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `airgap_observatory/core/galaxy-engine.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.023 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.183 IQR)
- **Top Global Matches:** file_cluster_17: 14.023, file_cluster_8: 14.045, file_cluster_4: 14.057
- **Magnitude:** 1087.02 | **LOC:** 1137 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.2503%), Tech Debt (36.9752%)
**Top Internal Functions/Classes:**
  * `handleInteraction` (Impact: 124.4)
  * `loadSector` (Impact: 84.1)
  * `setupEvents` (Impact: 43.6)
  * `pushAttrs` (Impact: 28.6)
  * `animate` (Impact: 28.5)
    * *Intent:* // 2. SATELLITE (MOON) REFRACTION
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 57`, `args: 43`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 612`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 20`, `import: 6`
* *Defense:* `safety: 30`, `doc: 1`, `immutability_locks: 142`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BloomNode.js, phase-6-shaders.js, three, webgpu, tsl
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `airgap_observatory/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.643 IQR)
- **Top Global Matches:** file_cluster_0: 11.643, file_cluster_17: 11.858, file_cluster_11: 12.034
- **Magnitude:** 905.44 | **LOC:** 1369 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.2464%), Tech Debt (54.7191%)
**Top Internal Functions/Classes:**
  * `updateHUD` (Impact: 135.7)
  * `copyHUDData` (Impact: 130.6)
  * `updateSingularityHUD` (Impact: 57.1)
  * `populateStoryHUD` (Impact: 40.9)
    * *Intent:* // --- POPULATE THE STORY HUD ---
  * `updateConstellationHUD` (Impact: 39.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 264`, `args: 87`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 15`, `state_mutation: 182`, `duplicate_logic: 8`, `orphaned_logic: 10`
* *Architecture:* `io: 8`, `api: 62`, `concurrency: 13`, `import: 1`
* *Defense:* `safety: 50`, `doc: 1`, `immutability_locks: 105`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` styles.css, tween.umd.js, poster.js, colors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/galaxyscope.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.946 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.098 IQR)
- **Top Global Matches:** file_cluster_8: 11.946, file_cluster_13: 11.974, file_cluster_16: 12.291
- **Magnitude:** 730.36 | **LOC:** 1628 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.526%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_mission` (Impact: 424.2)
  * `_process_file_worker` (Impact: 127.8)
  * `_init_worker` (Impact: 27.0)
  * `__init__` (Impact: 9.8)
  * `resolve_mission_control` (Impact: 6.7)
    * *Intent:* # --------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 150`, `args: 27`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 102`
* *Architecture:* `io: 10`, `api: 6`, `concurrency: 3`, `import: 44`
* *Defense:* `safety: 38`, `doc: 36`, `test: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` typing, datetime, .security_auditor, signal, .aperture, .record_keeper, .language_standards, concurrent.futures...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/signal_processor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.429 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.238 IQR)
- **Top Global Matches:** file_cluster_8: 11.429, file_cluster_16: 11.549, file_cluster_7: 11.781
- **Magnitude:** 696.2 | **LOC:** 1483 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.7804%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `summarize_galaxy_metrics` (Impact: 403.0)
  * `calculate_risk_vector` (Impact: 161.2)
  * `_get_context_multipliers` (Impact: 19.9)
  * `get_avg` (Impact: 12.4)
    * *Intent:* # ========================================================================== # GLOBAL SYNTHESIS & 2-...
  * `_classify_archetype` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 124`, `args: 39`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 51`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 53`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` typing, logging, , os, math, re, statistics
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `gitgalaxy/detector.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.52 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.17 IQR)
- **Top Global Matches:** file_cluster_8: 11.52, file_cluster_13: 11.545, file_cluster_16: 11.598
- **Magnitude:** 419.52 | **LOC:** 1847 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.1823%), Tech Debt (8.9084%)
**Top Internal Functions/Classes:**
  * `_decode_comment_stream` (Impact: 99.7)
  * `splice` (Impact: 70.1)
  * `coding_analysis` (Impact: 66.7)
    * *Intent:* # Check if the closest dampener is within the blast radius if damp_idx < damp_len and abs(dampeners[...
  * `_partition_segments` (Impact: 28.2)
  * `_find_balanced_end` (Impact: 21.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 72`, `args: 13`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 60`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 14`, `import: 11`
* *Defense:* `safety: 20`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 1):` typing, logging, .language_standards, hashlib, math, re, bisect, .analysis_lens...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `gitgalaxy/language_standards.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.435 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.531 IQR)
- **Top Global Matches:** file_cluster_8: 10.435, file_cluster_0: 10.874, file_cluster_7: 10.981
- **Magnitude:** 379.04 | **LOC:** 10517 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.4822%), Tech Debt (99.1535%)
**Top Internal Functions/Classes:**
  * `closures` (Impact: 23.6)
    * *Intent:* # 16. ui_framework (The View Layer) # Density of layout primitives and Tailwind utilities.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1652`, `structural_boundaries: 484`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 15`, `state_mutation: 104`, `dead_code: 11`, `planned_debt: 210`, `fragile_debt: 260`
* *Architecture:* `io: 29`, `api: 19`, `concurrency: 96`, `import: 12`
* *Defense:* `safety: 147`, `doc: 38`, `test: 59`, `sync_locks: 78`, `immutability_locks: 41`, `cleanup: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.956
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.078431
  * `Imports (Out-Degree: 0):` re, path
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `airgap_observatory/lib/three/addons/utils/BufferGeometryUtils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.592 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.961 IQR)
- **Top Global Matches:** file_cluster_8: 12.592, file_cluster_13: 12.817, file_cluster_7: 12.84
- **Magnitude:** 375.64 | **LOC:** 1436 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5446%), Tech Debt (28.1406%)
**Top Internal Functions/Classes:**
  * `mergeGeometries` (Impact: 53.1)
  * `mergeAttributes` (Impact: 40.2)
  * `computeMikkTSpaceTangents` (Impact: 34.4)
    * *Intent:* /** * @module BufferGeometryUtils * @three_import import * as BufferGeometryUtils from 'three/addons...
  * `mergeVertices` (Impact: 20.3)
  * `interleaveAttributes` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 65`, `args: 11`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 129`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 20`, `doc: 31`, `immutability_locks: 72`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BufferGeometryUtils.js, three
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `airgap_observatory/core/metavisualizer.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.026 IQR)
- **Top Global Matches:** file_cluster_17: 11.026, file_cluster_0: 11.211, file_cluster_8: 11.477
- **Magnitude:** 371.52 | **LOC:** 550 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.9801%), Tech Debt (75.4721%)
**Top Internal Functions/Classes:**
  * `processGalaxyData` (Impact: 112.3)
  * `renderMetric` (Impact: 52.5)
  * `calculateHistogram` (Impact: 49.6)
  * `findIdx` (Impact: 14.4)
  * `renderMetric` (Impact: 13.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 147`, `args: 62`, `func_start: 14`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 51`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 14`
* *Defense:* `safety: 29`, `doc: 5`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` output.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/audit_recorder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.274 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.582 IQR)
- **Top Global Matches:** file_cluster_8: 10.274, file_cluster_13: 10.542, file_cluster_7: 10.725
- **Magnitude:** 340.42 | **LOC:** 520 | **CtrlFlow:** 76.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.0115%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate_report` (Impact: 270.6)
  * `descale` (Impact: 14.1)
  * `format_label` (Impact: 7.6)
  * `__init__` (Impact: 5.8)
  * `decode_galaxy` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 30`, `args: 8`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 24`
* *Architecture:* `io: 3`, `api: 9`, `import: 9`
* *Defense:* `safety: 15`, `doc: 10`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` typing, , logging, os, datetime, json, pathlib, argparse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `gitgalaxy/language_lens.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.35 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.559 IQR)
- **Top Global Matches:** file_cluster_8: 10.35, file_cluster_16: 10.528, file_cluster_13: 10.727
- **Magnitude:** 325.5 | **LOC:** 918 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.8947%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_tier_2_fingerprint_check` (Impact: 227.4)
    * *Intent:* # THE FIX: If the extension is highly contested, refuse to lock it at Tier 1. # This forces the pipe...
  * `_calibrate_lookup_maps` (Impact: 21.7)
  * `_tier_1_metadata_lock` (Impact: 8.7)
  * `focus` (Impact: 4.9)
  * `inspect` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 95`, `args: 17`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 42`
* *Architecture:* `io: 2`, `api: 6`, `import: 8`
* *Defense:* `safety: 13`, `doc: 14`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 2):` typing, logging, .gitgalaxy_config, .language_standards, pathlib, math, re, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `gitgalaxy/prism.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.747 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.314 IQR)
- **Top Global Matches:** file_cluster_16: 11.747, file_cluster_8: 11.844, file_cluster_13: 11.973
- **Magnitude:** 304.96 | **LOC:** 537 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.9088%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_calibrate_matrix` (Impact: 147.3)
  * `refract` (Impact: 34.1)
  * `_refract_segment` (Impact: 26.8)
  * `callback` (Impact: 6.4)
  * `__init__` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 65`, `args: 19`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 72`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 4`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 1):` typing, re, logging, .language_standards
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `airgap_observatory/main.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.031 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.695 IQR)
- **Top Global Matches:** file_cluster_4: 13.031, file_cluster_17: 13.382, file_cluster_13: 13.419
- **Magnitude:** 284.96 | **LOC:** 561 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (87.2751%), Tech Debt (99.2438%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 65.0)
  * `toggleGlobalWeb` (Impact: 10.7)
  * `toggleLines` (Impact: 10.6)
  * `waitForEngine` (Impact: 9.5)
  * `discoverGalaxies` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 34`, `args: 26`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 89`, `duplicate_logic: 4`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `concurrency: 35`, `import: 3`
* *Defense:* `safety: 14`, `doc: 2`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` data-parser.js, phase-6-shaders.js, galaxy-engine.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `airgap_observatory/lib/three/addons/utils/GeometryCompressionUtils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.161 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.409 IQR)
- **Top Global Matches:** file_cluster_8: 11.161, file_cluster_13: 11.336, file_cluster_0: 11.411
- **Magnitude:** 254.48 | **LOC:** 548 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.011%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `octEncodeBest` (Impact: 64.8)
  * `octEncodeVec3` (Impact: 34.0)
  * `octDecodeVec2` (Impact: 26.4)
  * `quantizedEncode` (Impact: 20.9)
  * `compressUvs` (Impact: 20.7)
    * *Intent:* /** * @module GeometryCompressionUtils * @three_import import * as GeometryCompressionUtils from 'th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 28`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 43`, `dead_code: 2`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 5`, `doc: 4`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` three, GeometryCompressionUtils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/spectral_auditor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.564 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.694 IQR)
- **Top Global Matches:** file_cluster_8: 11.564, file_cluster_16: 11.625, file_cluster_13: 11.656
- **Magnitude:** 246.78 | **LOC:** 473 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.6367%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `audit` (Impact: 141.5)
    * *Intent:* # Save the language definitions so we can check for execution geometry later self.lang_defs = lang_d...
  * `_is_necrotic` (Impact: 9.8)
  * `_is_threat` (Impact: 9.5)
  * `__init__` (Impact: 9.2)
  * `_is_highly_blended` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 37`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 58`
* *Architecture:* `io: 2`, `api: 3`, `import: 5`
* *Defense:* `safety: 9`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` typing, logging, os, math, statistics
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `airgap_observatory/core/data-parser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.057 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.827 IQR)
- **Top Global Matches:** file_cluster_8: 12.057, file_cluster_7: 12.453, file_cluster_17: 12.465
- **Magnitude:** 239.78 | **LOC:** 265 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (59.9589%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `transformEntity` (Impact: 36.4)
  * `addToGroup` (Impact: 33.1)
  * `parse` (Impact: 30.0)
  * `transformSatellite` (Impact: 9.2)
  * `constructor` (Impact: 2.4)
    * *Intent:* /** * GitGalaxy * Copyright (c) 2026 Joe Esquibel *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 16`, `args: 12`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 116`
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/gpu_recorder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.355 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.384 IQR)
- **Top Global Matches:** file_cluster_13: 12.355, file_cluster_8: 12.458, file_cluster_16: 12.474
- **Magnitude:** 225.8 | **LOC:** 357 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (53.698%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `record_mission` (Impact: 114.0)
  * `__init__` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 24`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 95`
* *Architecture:* `io: 3`, `api: 5`, `import: 8`
* *Defense:* `safety: 6`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` typing, logging, , json, pathlib, gc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `airgap_observatory/lib/three/addons/utils/SceneOptimizer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.441 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.816 IQR)
- **Top Global Matches:** file_cluster_8: 11.441, file_cluster_17: 11.745, file_cluster_7: 11.818
- **Magnitude:** 180.58 | **LOC:** 459 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.9685%), Tech Debt (10.5738%)
**Top Internal Functions/Classes:**
  * `_createBatchedMeshes` (Impact: 20.2)
  * `_getMaterialPropertiesHash` (Impact: 18.2)
  * `disposeMeshes` (Impact: 13.4)
  * `_analyzeModel` (Impact: 13.0)
  * `_bufferToHash` (Impact: 11.7)
    * *Intent:* /** * Constructs a new scene optimizer.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 30`, `args: 21`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 10`, `doc: 14`, `immutability_locks: 43`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SceneOptimizer.js, three
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/security_auditor.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.689 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.593 IQR)
- **Top Global Matches:** file_cluster_8: 11.689, file_cluster_13: 11.696, file_cluster_17: 11.873
- **Magnitude:** 180.28 | **LOC:** 287 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.7524%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_resolve_dependency_graph` (Impact: 33.7)
  * `__init__` (Impact: 29.9)
    * *Intent:* # Load the Universal Schemas to map the raw vectors back to names self.SIGNAL_SCHEMA = RECORDING_SCH...
  * `_construct_feature_matrix` (Impact: 29.1)
  * `audit_galaxy` (Impact: 25.9)
  * `get_nth_degree` (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 33`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 42`
* *Architecture:* `io: 1`, `api: 5`, `import: 8`
* *Defense:* `safety: 10`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` logging, numpy, pathlib, math, xgboost, pandas, .analysis_lens, collections
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `airgap_observatory/lib/three/addons/utils/SortUtils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.206 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.276 IQR)
- **Top Global Matches:** file_cluster_8: 12.206, file_cluster_15: 12.457, file_cluster_7: 12.495
- **Magnitude:** 179.26 | **LOC:** 176 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.9911%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `radixSort` (Impact: 51.9)
  * `insertionSortBlock` (Impact: 17.5)
  * `insertionSortBlock` (Impact: 14.1)
  * `recurse` (Impact: 10.9)
  * `recurse` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 26`, `args: 10`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`, `duplicate_logic: 6`
* *Architecture:* `api: 2`
* *Defense:* `doc: 4`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SortUtils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/chronometer.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.054 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.357 IQR)
- **Top Global Matches:** file_cluster_13: 12.054, file_cluster_8: 12.179, file_cluster_16: 12.315
- **Magnitude:** 162.18 | **LOC:** 344 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.6899%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_load_ignored_revs` (Impact: 72.1)
  * `_survey_boundaries` (Impact: 33.4)
  * `_calibrate_temporal_field` (Impact: 10.1)
  * `__init__` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 38`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 30`
* *Architecture:* `io: 8`, `api: 3`, `import: 7`
* *Defense:* `safety: 19`, `doc: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` typing, logging, , os, pathlib, subprocess, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `airgap_observatory/lib/three/addons/utils/WorkerPool.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.697 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.097 IQR)
- **Top Global Matches:** file_cluster_4: 14.697, file_cluster_7: 15.247, file_cluster_8: 15.263
- **Magnitude:** 137.18 | **LOC:** 168 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.2986%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_onMessage` (Impact: 7.8)
    * *Intent:* /** * The current worker status. * * @type {number}
  * `postMessage` (Impact: 6.3)
  * `_getIdleWorker` (Impact: 4.6)
    * *Intent:* /** * An array with resolve functions for messages.
  * `_initWorker` (Impact: 4.5)
    * *Intent:* /** * A message queue. * * @type {Array<Object>}
  * `constructor` (Impact: 3.5)
    * *Intent:* /** * A simple pool for managing Web Workers. * * @three_import import { WorkerPool } from 'three/ad...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 8`, `args: 10`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `api: 5`, `concurrency: 24`
* *Defense:* `safety: 1`, `doc: 24`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WorkerPool.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `airgap_observatory/lib/three/addons/utils/SceneUtils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.527 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.2 IQR)
- **Top Global Matches:** file_cluster_8: 11.527, file_cluster_7: 11.548, file_cluster_13: 11.592
- **Magnitude:** 132.86 | **LOC:** 364 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.3947%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sortInstancedMesh` (Impact: 24.1)
  * `createMeshesFromMultiMaterialMesh` (Impact: 23.6)
  * `reduceVertices` (Impact: 16.4)
    * *Intent:* /**
  * `traverseVisibleGenerator` (Impact: 7.5)
  * `createMeshesFromInstancedMesh` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 27`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 37`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 6`, `doc: 25`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SceneUtils.js, three, BufferGeometryUtils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `airgap_observatory/config/colors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.019 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.327 IQR)
- **Top Global Matches:** file_cluster_8: 8.019, file_cluster_7: 8.673, file_cluster_1: 8.979
- **Magnitude:** 116.32 | **LOC:** 410 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.8169%), Tech Debt (32.4863%)
**Top Internal Functions/Classes:**
  * `getMetricColor` (Impact: 68.7)
  * `getLanguageColor` (Impact: 8.4)
  * `get` (Impact: 6.1)
  * `get` (Impact: 6.0)
  * `getAuthorColor` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 36`, `args: 7`, `func_start: 6`
* *Risk/State:* `state_mutation: 12`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `safety: 4`, `doc: 5`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `airgap_observatory/index.html` (HTML) | Magnitude: 905.44 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1152, branch: 272, structural_boundaries: 264, globals: 208

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `airgap_observatory/lib/three/addons/utils/ShadowMapViewerGPU.js` (JAVASCRIPT) | Magnitude: 51.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 43, state_mutation: 30, doc: 10, globals: 6
- `gitgalaxy/gpu_recorder.py` (PYTHON) | Magnitude: 225.8 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 222, state_mutation: 95, branch: 34, explicit_casts: 33
- `gitgalaxy/chronometer.py` (PYTHON) | Magnitude: 162.18 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 196, branch: 59, structural_boundaries: 38, state_mutation: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `gitgalaxy/prism.py` (PYTHON) | Magnitude: 304.96 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 301, branch: 103, state_mutation: 72, structural_boundaries: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `airgap_observatory/core/galaxy-engine.js` (JAVASCRIPT) | Magnitude: 1087.02 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 651, state_mutation: 612, branch: 144, immutability_locks: 142
- `gitgalaxy/llm_recorder.py` (PYTHON) | Magnitude: 1120.06 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 652, state_mutation: 592, branch: 261, structural_boundaries: 44
- `airgap_observatory/core/metavisualizer.html` (HTML) | Magnitude: 371.52 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 466, structural_boundaries: 147, branch: 123, immutability_locks: 71

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `airgap_observatory/tools/perf_monitor.js` (JAVASCRIPT) | Magnitude: 0.24 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 145, state_mutation: 135, branch: 30, globals: 20
- `airgap_observatory/core/materials.js` (JAVASCRIPT) | Magnitude: 86.24 | Delta: **0.192 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 48, branch: 15, immutability_locks: 11
- `airgap_observatory/tools/search.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.316 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 6, globals: 3, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `airgap_observatory/tools/poster.js` (JAVASCRIPT) | Magnitude: 0.25 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 242, state_mutation: 75, branch: 59, immutability_locks: 58
- `airgap_observatory/main.js` (JAVASCRIPT) | Magnitude: 284.96 | Delta: **0.351 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 177, state_mutation: 89, branch: 41, concurrency: 35
- `airgap_observatory/lib/three/addons/utils/WorkerPool.js` (JAVASCRIPT) | Magnitude: 137.18 | Delta: **0.55 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 74, indent_tabs: 57, doc: 24, concurrency: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `gitgalaxy/security_auditor.py` (PYTHON) | Magnitude: 180.28 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 195, branch: 56, state_mutation: 42, structural_boundaries: 33
- `airgap_observatory/lib/three/addons/utils/WebGPUTextureUtils.js` (JAVASCRIPT) | Magnitude: 16.54 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 35, immutability_locks: 8, structural_boundaries: 6, doc: 6
- `airgap_observatory/lib/three/addons/utils/SceneUtils.js` (JAVASCRIPT) | Magnitude: 132.86 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 140, immutability_locks: 43, state_mutation: 37, branch: 31
- `gitgalaxy/detector.py` (PYTHON) | Magnitude: 419.52 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 546, branch: 159, structural_boundaries: 72, state_mutation: 60
- `gitgalaxy/galaxyscope.py` (PYTHON) | Magnitude: 730.36 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1056, branch: 279, structural_boundaries: 150, state_mutation: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `airgap_observatory/css/input.css` (CSS) | Magnitude: 0.63 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: dead_code: 4, doc: 3, import: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `gitgalaxy/llm_recorder.py` -> Churn: **100.0%** | Cog Load: 57.8264% | Debt: 0.0%
- `gitgalaxy/gpu_recorder.py` -> Churn: **84.64%** | Cog Load: 53.698% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `gitgalaxy/guidestar_lens.py` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 2775.58
- `gitgalaxy/llm_recorder.py` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 1120.06
- `airgap_observatory/core/galaxy-engine.js` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 1087.02
- `airgap_observatory/index.html` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 905.44
- `gitgalaxy/galaxyscope.py` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 730.36

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `gitgalaxy/language_standards.py` -> **Severity: 3.801** (Embedded: 0.0784 * Error Risk: 48.4601%)
- `gitgalaxy/gitgalaxy_config.py` -> **Severity: 3.206** (Embedded: 0.0588 * Error Risk: 54.5037%)
- `gitgalaxy/llm_recorder.py` -> **Severity: 1.932** (Embedded: 0.0196 * Error Risk: 98.5318%)
- `gitgalaxy/gpu_recorder.py` -> **Severity: 1.802** (Embedded: 0.0196 * Error Risk: 91.914%)
- `gitgalaxy/spectral_auditor.py` -> **Severity: 1.686** (Embedded: 0.0196 * Error Risk: 85.9709%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `gitgalaxy/language_standards.py` -> **Severity: 1054.157** (Blast Radius: 58.956 * Doc Risk: 17.8804%)
- `airgap_observatory/lib/three/addons/utils/SortUtils.js` -> **Severity: 827.288** (Blast Radius: 17.708 * Doc Risk: 46.7183%)
- `gitgalaxy/gitgalaxy_config.py` -> **Severity: 767.427** (Blast Radius: 42.92 * Doc Risk: 17.8804%)
- `gitgalaxy/audit_recorder.py` -> **Severity: 649.272** (Blast Radius: 18.866 * Doc Risk: 34.4149%)
- `gitgalaxy/gpu_recorder.py` -> **Severity: 608.6** (Blast Radius: 18.866 * Doc Risk: 32.2591%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
