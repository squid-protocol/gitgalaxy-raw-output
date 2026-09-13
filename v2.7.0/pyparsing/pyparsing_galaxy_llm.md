# ARCHITECTURAL_BRIEF: pyparsing
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 258 |
| Analyzed Artifacts (Scanned) | 197 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 61 |
| Total LOC | 64011 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6057 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6746 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1419 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 152 | 28694 | 77.2% |
| HTML | 31 | 34666 | 15.7% |
| MARKDOWN | 7 | 0 | 3.6% |
| PLAINTEXT | 3 | 0 | 1.5% |
| YAML | 1 | 15 | 0.5% |
| BATCH | 1 | 101 | 0.5% |
| SHELL | 1 | 113 | 0.5% |
| C | 1 | 422 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 187 | 94.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 5.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 61*

**Composition by Extension & Reason:**
- `.png`: 28x Excluded (Explicitly Denied Extension: '.png')
- `.tiny`: 11x Excluded (Unsupported Extension: '.tiny')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.pystate`: 4x Excluded (Unsupported Extension: '.pystate')
- `.ini`: 3x Excluded (Unsupported Extension: '.ini')
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.dfm`: 2x Excluded (Unsupported Extension: '.dfm')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 205 LOC)
- `.g`: 1x Excluded (Unsupported Extension: '.g')
- `.ics`: 1x Excluded (Unsupported Extension: '.ics')
- `.html`: 1x Excluded (Saturation: Line 93 exceeds 500 chars)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 95.5 | 25.6 | 21.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 64.4 | 79.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 73.1 | 0.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 79.1 | 21.4 | 11.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 1.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 74.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 36.3 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 639 | 70 | 6 | `pyparsing-3.3.2/tests/test_unit.py` |
| cleanup | 4 | 2 | 0 | `pyparsing-3.3.2/run_perf_all_tags.sh` |
| guards | 1179 | 79 | 12 | `pyparsing-3.3.2/pyparsing/core.py` |
| danger | 691 | 81 | 7 | `pyparsing-3.3.2/pyparsing/core.py` |
| concurrency | 88 | 15 | 0 | `pyparsing-3.3.2/pyparsing/core.py` |
| connectivity | 2437 | 138 | 27 | `pyparsing-3.3.2/tests/test_unit.py` |
| io | 3107 | 53 | 22 | `pyparsing-3.3.2/examples/decaf_parser_diagram.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 1 | 0 | `pyparsing-3.3.2/tests/test_unit.py` |
| time | 99 | 6 | 0 | `pyparsing-3.3.2/examples/delta_time.py` |
| serialization | 5 | 1 | 0 | `pyparsing-3.3.2/tests/test_unit.py` |
| regex | 27 | 8 | 0 | `pyparsing-3.3.2/pyparsing/core.py` |
| events | 5 | 3 | 0 | `pyparsing-3.3.2/examples/snmp_api.h` |
| tests | 264 | 17 | 0 | `pyparsing-3.3.2/tests/test_pre_pep8_deprecation_warnings.py` |
| docs | 919 | 120 | 7 | `pyparsing-3.3.2/tests/test_unit.py` |
| debt | 1256 | 112 | 8 | `pyparsing-3.3.2/tests/test_unit.py` |
| mutation | 24234 | 179 | 221 | `pyparsing-3.3.2/tests/test_unit.py` |
| dead_code | 525 | 47 | 2 | `pyparsing-3.3.2/tests/test_unit.py` |
| credential | 9 | 3 | 0 | `pyparsing-3.3.2/tests/test_unit.py` |
| threat | 183 | 35 | 1 | `pyparsing-3.3.2/tests/test_unit.py` |
| ml_ai | 40382 | 34 | 419 | `pyparsing-3.3.2/examples/antlr_grammar_diagram.html` |
| ui | 34 | 3 | 0 | `pyparsing-3.3.2/dest/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyparsing-3.3.2/examples/decaf_parser_diagram.html` (Hits: 510)
- `pyparsing-3.3.2/examples/antlr_grammar_diagram.html` (Hits: 478)
- `pyparsing-3.3.2/examples/lua_parser_diagram.html` (Hits: 428)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.py** (`pyparsing-3.3.2/pyparsing/util.py`) — 8 inbound connections
2. **warnings.py** (`pyparsing-3.3.2/pyparsing/warnings.py`) — 7 inbound connections
3. **tiny_parser.py** (`pyparsing-3.3.2/examples/tiny/tiny_parser.py`) — 6 inbound connections
4. **core.py** (`pyparsing-3.3.2/pyparsing/core.py`) — 6 inbound connections
5. **jsonParser.py** (`pyparsing-3.3.2/examples/jsonParser.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`pyparsing-3.3.2/examples/README.md`) — 106 outbound dependencies
2. **test_unit.py** (`pyparsing-3.3.2/tests/test_unit.py`) — 35 outbound dependencies
3. **core.py** (`pyparsing-3.3.2/pyparsing/core.py`) — 29 outbound dependencies
4. **make_diagram.py** (`pyparsing-3.3.2/examples/make_diagram.py`) — 21 outbound dependencies
5. **test_diagram.py** (`pyparsing-3.3.2/tests/test_diagram.py`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_to_diagram_element` (@ `pyparsing-3.3.2/pyparsing/diagram/__init__.py`) -> Impact: **224.5** | LOC: 252
- `run_tests` (@ `pyparsing-3.3.2/pyparsing/core.py`) -> Impact: **172.1** | LOC: 241
- `__init__` (@ `pyparsing-3.3.2/pyparsing/core.py`) -> Impact: **170.4** | LOC: 120
- `with_line_numbers` (@ `pyparsing-3.3.2/pyparsing/testing.py`) -> Impact: **100.9** | LOC: 121
- `Test` (@ `pyparsing-3.3.2/examples/booleansearchparser.py`) -> Impact: **97.7** | LOC: 115
  * *Intent:* # fmt: off exprs = { "0": "help", "1": "help or hulp", "2": "help and hulp", "3": "help hulp", "4": "help and hulp or hilp", "5": "help or hulp and hi...
- `__init__` (@ `pyparsing-3.3.2/pyparsing/core.py`) -> Impact: **94.8** | LOC: 126
- `_parseNoCache` (@ `pyparsing-3.3.2/pyparsing/core.py`) -> Impact: **90.7** | LOC: 100
  * *Intent:* # @profile
- `make_compressed_re` (@ `pyparsing-3.3.2/pyparsing/util.py`) -> Impact: **89.6** | LOC: 93
- `one_of` (@ `pyparsing-3.3.2/pyparsing/helpers.py`) -> Impact: **87.7** | LOC: 138
- `infix_notation` (@ `pyparsing-3.3.2/pyparsing/helpers.py`) -> Impact: **86.2** | LOC: 203

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pyparsing-3.3.2/examples` | 134 | 9465.86 | 23.97% | 0.0% |
| `pyparsing-3.3.2/pyparsing` | 11 | 8532.06 | 38.28% | 11.43% |
| `pyparsing-3.3.2/tests` | 17 | 6615.16 | 10.71% | 0.0% |
| `pyparsing-3.3.2/dest` | 3 | 1351.97 | 51.24% | 0.0% |
| `pyparsing-3.3.2/examples/regex_inverter` | 3 | 1351.97 | 51.24% | 0.0% |
| `pyparsing-3.3.2/examples/tiny` | 7 | 1147.62 | 32.82% | 0.0% |
| `pyparsing-3.3.2/pyparsing/diagram` | 1 | 675.36 | 56.1% | 11.18% |
| `pyparsing-3.3.2/examples/statemachine` | 6 | 390.5 | 32.5% | 0.0% |
| `pyparsing-3.3.2` | 5 | 210.82 | 15.03% | 0.0% |
| `pyparsing-3.3.2/examples/tiny/tests` | 3 | 196.78 | 21.67% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pyparsing-3.3.2/pyparsing/util.py` -> **73.1059%** Exposure
- `pyparsing-3.3.2/pyparsing/core.py` -> **43.7306%** Exposure
- `pyparsing-3.3.2/pyparsing/diagram/__init__.py` -> **11.1784%** Exposure
- `pyparsing-3.3.2/pyparsing/helpers.py` -> **8.9338%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pyparsing-3.3.2/pyparsing/actions.py` -> **100.0%** Exposure
- `pyparsing-3.3.2/pyparsing/core.py` -> **100.0%** Exposure
- `pyparsing-3.3.2/pyparsing/diagram/__init__.py` -> **100.0%** Exposure
- `pyparsing-3.3.2/pyparsing/exceptions.py` -> **100.0%** Exposure
- `pyparsing-3.3.2/pyparsing/helpers.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyparsing-3.3.2/tests/test_unit.py` -> **314** Orphaned Functions | **15** Duplicates
- `pyparsing-3.3.2/tests/test_pre_pep8_deprecation_warnings.py` -> **45** Orphaned Functions | **0** Duplicates
- `pyparsing-3.3.2/pyparsing/core.py` -> **0** Orphaned Functions | **20** Duplicates
- `pyparsing-3.3.2/tests/test_examples.py` -> **19** Orphaned Functions | **0** Duplicates
- `pyparsing-3.3.2/examples/tiny/tests/test_tiny_ast_nodes.py` -> **15** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `478` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyparsing-3.3.2/pyparsing/util.py` (PYTHON) -> Cumulative Risk: **696.9**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 482.6 | **LOC:** 515 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.7946%), Documentation (89.8305%)
- **Heaviest Functions:** `make_compressed_re` (Impact: 89.6), `_collapse_string_to_ranges` (Impact: 21.6), `replaced_by_pep8` (Impact: 14.3)

### 2. `pyparsing-3.3.2/pyparsing/core.py` (PYTHON) -> Cumulative Risk: **652.47**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 5607.8 | **LOC:** 6952 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.2844%), Verification (80.0%)
- **Heaviest Functions:** `run_tests` (Impact: 172.1), `__init__` (Impact: 170.4), `__init__` (Impact: 94.8)

### 3. `pyparsing-3.3.2/pyparsing/testing.py` (PYTHON) -> Cumulative Risk: **632.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 391.72 | **LOC:** 399 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.6326%)
- **Heaviest Functions:** `with_line_numbers` (Impact: 100.9), `assertRunTestResults` (Impact: 59.5), `restore` (Impact: 13.1)

### 4. `pyparsing-3.3.2/pyparsing/helpers.py` (PYTHON) -> Cumulative Risk: **624.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 798.42 | **LOC:** 1221 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.0595%), Verification (80.0%)
- **Heaviest Functions:** `one_of` (Impact: 87.7), `infix_notation` (Impact: 86.2), `nested_expr` (Impact: 64.3)

### 5. `pyparsing-3.3.2/dest/inv_regex.py` (PYTHON) -> Cumulative Risk: **607.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 229.18 | **LOC:** 349 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9991%), Safety Score (87.1384%), Verification (80.0%)
- **Heaviest Functions:** `handle_repetition` (Impact: 12.3), `handle_macro` (Impact: 12.3), `make_generator` (Impact: 9.2)

### 6. `pyparsing-3.3.2/pyparsing/diagram/__init__.py` (PYTHON) -> Cumulative Risk: **593.44**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 675.36 | **LOC:** 762 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.939%), Verification (80.0%)
- **Heaviest Functions:** `_to_diagram_element` (Impact: 224.5), `to_railroad` (Impact: 35.0), `mark_for_extraction` (Impact: 21.0)

### 7. `pyparsing-3.3.2/pyparsing/results.py` (PYTHON) -> Cumulative Risk: **581.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 640.56 | **LOC:** 929 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.4369%), Verification (80.0%)
- **Heaviest Functions:** `dump` (Impact: 40.6), `__init__` (Impact: 39.1), `pop` (Impact: 21.1)

### 8. `pyparsing-3.3.2/pyparsing/actions.py` (PYTHON) -> Cumulative Risk: **575.14**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 99.82 | **LOC:** 265 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8892%), Verification (80.0%)
- **Heaviest Functions:** `with_attribute` (Impact: 16.7), `pa` (Impact: 10.5), `with_class` (Impact: 8.0)

### 9. `pyparsing-3.3.2/pyparsing/exceptions.py` (PYTHON) -> Cumulative Risk: **570.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 184.54 | **LOC:** 354 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.5608%), Verification (80.0%)
- **Heaviest Functions:** `explain_exception` (Impact: 25.6), `found` (Impact: 9.2), `mark_input_line` (Impact: 8.8)

### 10. `pyparsing-3.3.2/pyparsing/tools/cvt_pyparsing_pep8_names.py` (PYTHON) -> Cumulative Risk: **491.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 0.06 | **LOC:** 143 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Safety Score (92.4653%), Documentation (66.6667%)
- **Heaviest Functions:** `update_special_changes` (Impact: 6.8), `camel_to_snake` (Impact: 5.9), `show_diffs` (Impact: 3.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyparsing-3.3.2/pyparsing/core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5607.8 | **LOC:** 6952 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.3033%), Tech Debt (43.7306%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 172.1)
  * `__init__` (Impact: 170.4)
  * `__init__` (Impact: 94.8)
  * `_parseNoCache` (Impact: 90.7)
    * *Intent:* # @profile
  * `parseImpl` (Impact: 73.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 725 instances
* *State Mutation (weighted view):* 2399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 964`, `structural_boundaries: 794`, `args: 304`, `func_start: 290`, `class_start: 62`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 949`, `dead_code: 7`, `fragile_debt: 2`, `duplicate_logic: 20`
* *Architecture:* `io: 9`, `api: 230`, `concurrency: 1`, `import: 29`
* *Defense:* `safety: 216`, `doc: 139`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.967
  * `Choke Point (Betweenness):` 0.000641 | `Ripple Effect (Closeness):` 0.03125
  * `Imports (Out-Degree: 7):` .actions, .diagram, .exceptions, .results, .testing, .unicode, .util, .warnings...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/tests/test_unit.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5288.38 | **LOC:** 11447 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.582%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testQuotedStrings` (Impact: 60.3)
  * `testInfixNotationEvalBoolExprUsingAstClasses` (Impact: 46.9)
  * `testRepeater` (Impact: 39.1)
  * `testNumericExpressions` (Impact: 34.3)
    * *Intent:* # disable parse actions that do type conversion so we don't accidentally trigger # conversion except...
  * `testNestedExpressionRandom` (Impact: 23.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 423 instances
* *High Risk Execution (weighted view):* 16
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 2651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 543`, `structural_boundaries: 1300`, `args: 520`, `func_start: 456`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 19`, `state_mutation: 1805`, `dead_code: 7`, `fragile_debt: 6`, `duplicate_logic: 15`, `unreferenced_by_name: 314`
* *Architecture:* `io: 22`, `api: 456`, `import: 55`
* *Defense:* `safety: 144`, `doc: 215`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ast, collections, contextlib, datetime, examples, examples.fourFn, examples.jsonParser, examples.simpleSQL...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/dest/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1121.59 | **LOC:** 250 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.4302%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 37`, `args: 17`, `func_start: 3`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 31`
* *Architecture:* `io: 8`, `api: 7`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.css, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/regex_inverter/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1121.59 | **LOC:** 250 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.4302%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 37`, `args: 17`, `func_start: 3`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 31`
* *Architecture:* `io: 8`, `api: 7`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.222
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005102
  * `Imports (Out-Degree: 0):` core.css, core.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/pyparsing/helpers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 798.42 | **LOC:** 1221 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.4499%), Tech Debt (8.9338%)
**Top Internal Functions/Classes:**
  * `one_of` (Impact: 87.7)
  * `infix_notation` (Impact: 86.2)
  * `nested_expr` (Impact: 64.3)
  * `indentedBlock` (Impact: 41.1)
    * *Intent:* """ .. deprecated:: 3.0.0 Use the :class:`IndentedBlock` class instead. Note that `IndentedBlock` ha...
  * `counted_array` (Impact: 15.5)
    * *Intent:* # # global helpers #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 353
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 77`, `args: 44`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 151`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 26`, `import: 8`
* *Defense:* `safety: 18`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.344
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.015306
  * `Imports (Out-Degree: 2):` , .core, .util, html.entities, operator, re, sys, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/adventureEngine.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 724.84 | **LOC:** 745 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.8298%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createRooms` (Impact: 28.3)
    * *Intent:* """ create rooms, using multiline string showing map layout string contains symbols for the followin...
  * `_do_command` (Impact: 16.5)
  * `_do_command` (Impact: 12.8)
  * `_do_command` (Impact: 12.8)
  * `_do_command` (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 334
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 133`, `args: 73`, `func_start: 72`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 168`
* *Architecture:* `io: 7`, `api: 60`, `import: 4`
* *Defense:* `safety: 5`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010204
  * `Imports (Out-Degree: 0):` contextlib, pyparsing, random, string
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/pyparsing/diagram/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 675.36 | **LOC:** 762 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.1039%), Tech Debt (11.1784%)
**Top Internal Functions/Classes:**
  * `_to_diagram_element` (Impact: 224.5)
  * `to_railroad` (Impact: 35.0)
  * `mark_for_extraction` (Impact: 21.0)
  * `_inner` (Impact: 20.8)
  * `extract_into_diagram` (Impact: 12.0)
    * *Intent:* """ Used when we encounter the same token twice in the same tree. When this happens, we replace all ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 88`, `args: 23`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 93`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 16`, `import: 11`
* *Defense:* `safety: 23`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, dataclasses, inspect, io, itertools, jinja2, pyparsing, railroad...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/pyparsing/results.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 640.56 | **LOC:** 929 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.9018%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dump` (Impact: 40.6)
    * *Intent:* """ Diagnostic method for listing out the contents of a :class:`ParseResults`. Accepts an optional `...
  * `__init__` (Impact: 39.1)
    * *Intent:* # Performance tuning: we construct a *lot* of these, so keep this # constructor as small and fast as...
  * `pop` (Impact: 21.1)
    * *Intent:* """ Removes and returns item at specified index (default= ``last``). Supports both ``list`` and ``di...
  * `deepcopy` (Impact: 18.1)
    * *Intent:* """ Returns a new deep copy of a :class:`ParseResults` object. .. versionadded:: 3.1.0 """
  * `get_name` (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 128`, `args: 46`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 90`
* *Architecture:* `api: 36`, `import: 6`
* *Defense:* `safety: 38`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.883
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 1):` .util, __future__, collections, collections.abc, json, pprint, pyparsing, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/pyparsing/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 482.6 | **LOC:** 515 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.0809%), Tech Debt (73.1059%)
**Top Internal Functions/Classes:**
  * `make_compressed_re` (Impact: 89.6)
  * `_collapse_string_to_ranges` (Impact: 21.6)
  * `replaced_by_pep8` (Impact: 14.3)
    * *Intent:* # Unwrap staticmethod/classmethod fn = getattr(fn, "__func__", fn) # (Presence of 'self' arg in sign...
  * `_set` (Impact: 10.7)
  * `deprecate_argument` (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 84`, `args: 37`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 91`, `duplicate_logic: 4`
* *Architecture:* `api: 23`, `import: 9`
* *Defense:* `safety: 12`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.125
  * `Choke Point (Betweenness):` 0.0001 | `Ripple Effect (Closeness):` 0.044096
  * `Imports (Out-Degree: 1):` .warnings, contextlib, functools, inspect, itertools, pyparsing.util, re, types...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/tests/test_pre_pep8_deprecation_warnings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 423.52 | **LOC:** 438 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.8827%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_one_of_asKeyword_kwarg_emits_DeprecationWarning` (Impact: 5.2)
  * `test_scanString_emits_DeprecationWarning` (Impact: 4.2)
  * `test_enablePackrat_emits_DeprecationWarning_and_cleanup` (Impact: 3.5)
    * *Intent:* # Record initial packrat state; restore it after test completes initially_enabled = getattr(ParserEl...
  * `test_runTests_emits_DeprecationWarning` (Impact: 3.1)
  * `test_infixNotation_emits_DeprecationWarning` (Impact: 2.6)
    * *Intent:* # simple arithmetic with '+' only integer = Word(nums).set_parse_action(lambda t: int(t[0])) with py...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 181`, `args: 52`, `func_start: 46`
* *Risk/State:* `state_mutation: 91`, `unreferenced_by_name: 45`
* *Architecture:* `api: 46`, `import: 15`
* *Defense:* `safety: 53`, `doc: 1`, `test: 90`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` datetime, pyparsing, pyparsing.actions, pyparsing.helpers, pyparsing.results, pytest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/delta_time.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 409.66 | **LOC:** 596 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.1272%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_all_tests` (Impact: 26.7)
  * `offset_weekday` (Impact: 19.6)
  * `_convert_abs_day_reference_to_date` (Impact: 17.1)
  * `make_weekday_time_references` (Impact: 13.4)
  * `_compute_timestamp` (Impact: 11.3)
    * *Intent:* # accumulate values from parsed time and day subexpressions - fill in defaults for omitted parts now...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 63`, `args: 24`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 118`, `dead_code: 2`
* *Architecture:* `api: 20`, `import: 6`
* *Defense:* `safety: 1`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010204
  * `Imports (Out-Degree: 0):` calendar, contextlib, datetime, itertools, pyparsing, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/pyparsing/testing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 391.72 | **LOC:** 399 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.6145%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `with_line_numbers` (Impact: 100.9)
  * `assertRunTestResults` (Impact: 59.5)
  * `restore` (Impact: 13.1)
    * *Intent:* # reset pyparsing global state if ( ParserElement.DEFAULT_WHITE_CHARS != self._save_context["default...
  * `assertRaisesParseException` (Impact: 9.5)
  * `assertParseAndCheckList` (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 38`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 56`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 8`, `doc: 8`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.439
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019231
  * `Imports (Out-Degree: 1):` , .core, contextlib, re, typing, unittest
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/LAparser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 364.18 | **LOC:** 577 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.6477%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `post_test` (Impact: 27.1)
    * *Intent:* # copy exprStack to evaluate and clear before running next test parsed_stack = exprStack[:] exprStac...
  * `_expfunc` (Impact: 25.1)
    * *Intent:* ## The '^' operator is used for exponentiation on scalars and ## as a marker for unary operations on...
  * `_mulfunc` (Impact: 25.0)
  * `test` (Impact: 22.9)
    * *Intent:* ##----------------------------------------------------------------------------------- """ Tests the ...
  * `parse` (Impact: 22.0)
    * *Intent:* ##---------------------------------------------------------------------------- # The parse function ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 61`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 70`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `io: 17`, `api: 6`, `import: 4`
* *Defense:* `safety: 18`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.222
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005102
  * `Imports (Out-Degree: 0):` os, pyparsing, re, sys, this
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/tiny/tiny_engine.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 348.96 | **LOC:** 417 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.8016%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `eval_expr` (Impact: 34.1)
    * *Intent:* # ----- Expression Evaluation ----- """Evaluate an expression built by pyparsing's infix_notation an...
  * `_apply_op` (Impact: 30.9)
    * *Intent:* # Boolean ops if op in {"&&", "||"}: lv = bool(lhs) rv = bool(rhs) return _op_map[op](lv, rv) # Rela...
  * `call_function` (Impact: 15.4)
    * *Intent:* # ----- Functions API (execution helper to share with CallStmtNode) ----- """Call a user-defined fun...
  * `assign_var` (Impact: 13.2)
    * *Intent:* """Assign to an existing variable; if undeclared, declare using inferred type."""
  * `declare_var` (Impact: 12.1)
    * *Intent:* # ----- Variables API -----
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 83`, `args: 30`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 45`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 27`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.682
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015306
  * `Imports (Out-Degree: 1):` .tiny_ast, __future__, operator, pyparsing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/tests/perf_pyparsing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 340.86 | **LOC:** 361 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.3323%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gen_expr_sequence` (Impact: 20.8)
  * `main` (Impact: 16.2)
    * *Intent:* # ---------- Main suite ----------
  * `gen_csv` (Impact: 12.8)
    * *Intent:* # ---------- Corpora generators ----------
  * `bench_matchfirst_vs_or` (Impact: 11.2)
  * `make_term` (Impact: 10.8)
    * *Intent:* # base integer t = str(rnd.randint(0, 1000)) # with some probability, turn it into a small subexpres...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 71`, `args: 34`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 78`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 27`, `import: 13`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` contextlib, datetime, io, littletable, os, pathlib, pyparsing, random...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/booleansearchparser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 335.04 | **LOC:** 454 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.9147%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Test` (Impact: 97.7)
    * *Intent:* # fmt: off exprs = { "0": "help", "1": "help or hulp", "2": "help and hulp", "3": "help hulp", "4": ...
  * `parser` (Impact: 19.0)
    * *Intent:* """ This function returns a parser. The grammar should be like most full text search engines (Google...
  * `evaluateWord` (Impact: 16.4)
  * `_split_words` (Impact: 11.4)
  * `GetWordWildcard` (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 49`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 43`, `planned_debt: 1`
* *Architecture:* `api: 21`, `import: 2`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, booleansearchparser, pyparsing, re, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/verilog_parse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 325.28 | **LOC:** 948 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.0134%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_verilog_bnf` (Impact: 23.0)
  * `main` (Impact: 11.8)
  * `test` (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 19`, `args: 4`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 192`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 4`, `import: 7`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.222
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005102
  * `Imports (Out-Degree: 0):` gc, pathlib, pprint, pyparsing, sys, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/tiny/tiny_ast.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 286.28 | **LOC:** 474 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.424%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `from_parsed` (Impact: 11.2)
  * `execute` (Impact: 10.9)
    * *Intent:* # Repeat-Until is a do-while: execute body, then check condition; stop when condition is true while ...
  * `from_parsed` (Impact: 10.9)
  * `from_parsed` (Impact: 10.8)
  * `from_parsed` (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *Amplified Sql Injection:* 12 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 90`, `args: 29`, `func_start: 29`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 38`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 39`, `import: 5`
* *Defense:* `safety: 6`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020408
  * `Imports (Out-Degree: 0):` __future__, abc, dataclasses, pyparsing, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/lua_parser_diagram.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 279.08 | **LOC:** 4364 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 363`, `args: 63`, `func_start: 91`, `class_start: 91`
* *Risk/State:* None
* *Architecture:* `io: 428`, `api: 90`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.222
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005102
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/statemachine/statemachine.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 273.4 | **LOC:** 373 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.4251%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expand_named_state_definition` (Impact: 38.8)
    * *Intent:* """ Parse action to convert statemachine with named transitions to corresponding Python classes and ...
  * `expand_state_definition` (Impact: 15.1)
    * *Intent:* """ Parse action to convert statemachine to corresponding Python classes and methods """
  * `find_module` (Impact: 6.3)
  * `load_module` (Impact: 6.0)
  * `checkpath_iter` (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 87`, `args: 32`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 66`, `dead_code: 3`
* *Architecture:* `io: 8`, `api: 13`, `import: 8`
* *Defense:* `safety: 6`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02551
  * `Imports (Out-Degree: 0):` handler, importlib, importlib.machinery, imputil, keyword, os, pyparsing, statemachine...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/decaf_parser_diagram.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 268.68 | **LOC:** 4264 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 343`, `args: 10`, `func_start: 86`, `class_start: 86`
* *Risk/State:* None
* *Architecture:* `io: 510`, `api: 85`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.222
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005102
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/mongodb_query_expression.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 261.34 | **LOC:** 671 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.9902%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `binary_array_comparison_op` (Impact: 36.8)
    * *Intent:* """ Parse action to handle array membership tests, such as 'in', 'not in', etc. """
  * `binary_multi_op` (Impact: 29.4)
    * *Intent:* """ Parse action to handle binary Boolean operators 'and' and 'or', combining 2 or more condition ex...
  * `binary_comparison_op` (Impact: 16.9)
    * *Intent:* """ Parse action called for '<', '>', '<=', and '>=' comparisons. Includes logic to handle chained i...
  * `regex_comparison_op` (Impact: 14.6)
    * *Intent:* """ Parse action to handle regex and wildcard ("LIKE" syntax) matching. """
  * `main` (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 54`, `args: 18`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 51`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 19`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.222
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005102
  * `Imports (Out-Degree: 0):` contextlib, datetime, pprint, pyparsing, re, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/antlr_grammar_diagram.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 247.18 | **LOC:** 4161 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
  * `style` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 307`, `func_start: 77`, `class_start: 77`
* *Risk/State:* `planned_debt: 2`
* *Architecture:* `io: 478`, `api: 76`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/tiny/tiny_repl.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 244.86 | **LOC:** 332 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.3915%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_meta_command` (Impact: 48.5)
    * *Intent:* # normalize to lowercase, and collapse whitespace lower = " ".join(cmd.lower().split()) line = cmd.s...
  * `repl` (Impact: 25.6)
  * `_load_functions_from_file` (Impact: 18.6)
  * `_print_functions` (Impact: 5.5)
  * `_build_nodes_from_stmt_seq` (Impact: 4.8)
    * *Intent:* """Convert a parsed `stmt_seq` group into prebuilt `TinyNode` instances."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 80`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 48`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 7`, `api: 6`, `import: 10`
* *Defense:* `safety: 21`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .tiny_ast, .tiny_engine, .tiny_parser, .tiny_run, __future__, commands, pathlib, pyparsing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/dest/inv_regex.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 229.18 | **LOC:** 349 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2759%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_repetition` (Impact: 12.3)
  * `handle_macro` (Impact: 12.3)
  * `make_generator` (Impact: 9.2)
  * `handle_literal` (Impact: 9.0)
  * `recurse_list` (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 81`, `args: 33`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `state_mutation: 38`
* *Architecture:* `api: 31`, `import: 1`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyparsing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pyparsing-3.3.2/pyparsing/core.py` -> **Severity: 0.064** (Bridge: 0.0006 * Flux: 100.0%)
- `pyparsing-3.3.2/pyparsing/util.py` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 100.0%)
- `pyparsing-3.3.2/pyparsing/actions.py` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 100.0%)
- `pyparsing-3.3.2/pyparsing/helpers.py` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 100.0%)
- `pyparsing-3.3.2/pyparsing/exceptions.py` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyparsing-3.3.2/pyparsing/util.py` -> **Severity: 4.356** (Embedded: 0.0441 * Error Risk: 98.7946%)
- `pyparsing-3.3.2/pyparsing/core.py` -> **Severity: 3.04** (Embedded: 0.0312 * Error Risk: 97.2844%)
- `pyparsing-3.3.2/pyparsing/results.py` -> **Severity: 2.57** (Embedded: 0.0272 * Error Risk: 94.4369%)
- `pyparsing-3.3.2/examples/statemachine/statemachine.py` -> **Severity: 2.515** (Embedded: 0.0255 * Error Risk: 98.5956%)
- `pyparsing-3.3.2/examples/tiny/tiny_parser.py` -> **Severity: 2.454** (Embedded: 0.0306 * Error Risk: 80.1724%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyparsing-3.3.2/pyparsing/util.py` -> **Severity: 2436.652** (Blast Radius: 27.125 * Doc Risk: 89.8305%)
- `pyparsing-3.3.2/pyparsing/core.py` -> **Severity: 1308.386** (Blast Radius: 17.967 * Doc Risk: 72.8216%)
- `pyparsing-3.3.2/examples/statemachine/statemachine.py` -> **Severity: 1301.797** (Blast Radius: 21.925 * Doc Risk: 59.375%)
- `pyparsing-3.3.2/pyparsing/testing.py` -> **Severity: 643.9** (Blast Radius: 6.439 * Doc Risk: 100.0%)
- `pyparsing-3.3.2/pyparsing/results.py` -> **Severity: 595.683** (Blast Radius: 8.883 * Doc Risk: 67.0588%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
