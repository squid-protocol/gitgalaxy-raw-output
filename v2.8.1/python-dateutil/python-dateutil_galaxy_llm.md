# ARCHITECTURAL_BRIEF: python-dateutil
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
| Total Artifacts | 24 |
| Analyzed Artifacts (Scanned) | 19 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 3796 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 79.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4609 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4432 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6842 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 16 | 3771 | 84.2% |
| PLAINTEXT | 2 | 0 | 10.5% |
| JSON | 1 | 25 | 5.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 37%, Large Core Modules 37%, Declarative / Non-Code 5%, Defensive Guards Files 5%, I/O & Config Routines Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 17 | 89.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 10.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.7 | 36.3 | 35.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 71.2 | 87.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 90.3 | 21.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 29.8 | 2.5 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 60.2 | 18.3 | 15.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 69.6 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.7 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 64.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 37.2 | 47.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 164 | 8 | 17 | `python-dateutil-2.6.1/dateutil/parser.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 352 | 10 | 59 | `python-dateutil-2.6.1/dateutil/rrule.py` |
| danger | 155 | 11 | 20 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| concurrency | 6 | 1 | 0 | `python-dateutil-2.6.1/dateutil/rrule.py` |
| connectivity | 168 | 12 | 29 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| io | 30 | 6 | 4 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| crypto | 1 | 1 | 0 | `python-dateutil-2.6.1/updatezinfo.py` |
| ipc | 1 | 1 | 0 | `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` |
| time | 56 | 6 | 14 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `python-dateutil-2.6.1/dateutil/parser.py` |
| events | 1 | 1 | 0 | `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` |
| tests | 0 | 0 | 0 | - |
| docs | 87 | 12 | 13 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| debt | 26 | 8 | 4 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| mutation | 2111 | 14 | 382 | `python-dateutil-2.6.1/dateutil/rrule.py` |
| dead_code | 8 | 6 | 1 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| credential | 0 | 0 | 0 | - |
| threat | 43 | 8 | 5 | `python-dateutil-2.6.1/dateutil/parser.py` |
| ml_ai | 1 | 1 | 0 | `python-dateutil-2.6.1/setup.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `python-dateutil-2.6.1/dateutil/tz/tz.py` (Hits: 13)
- `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` (Hits: 8)
- `python-dateutil-2.6.1/updatezinfo.py` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **tz.py** (`python-dateutil-2.6.1/dateutil/tz/tz.py`) — 3 inbound connections
2. **_version.py** (`python-dateutil-2.6.1/dateutil/_version.py`) — 2 inbound connections
3. **win.py** (`python-dateutil-2.6.1/dateutil/tz/win.py`) — 2 inbound connections
4. **relativedelta.py** (`python-dateutil-2.6.1/dateutil/relativedelta.py`) — 1 inbound connections
5. **tzwin.py** (`python-dateutil-2.6.1/dateutil/tzwin.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **tz.py** (`python-dateutil-2.6.1/dateutil/tz/tz.py`) — 14 outbound dependencies
2. **rrule.py** (`python-dateutil-2.6.1/dateutil/rrule.py`) — 13 outbound dependencies
3. **parser.py** (`python-dateutil-2.6.1/dateutil/parser.py`) — 12 outbound dependencies
4. **relativedelta.py** (`python-dateutil-2.6.1/dateutil/relativedelta.py`) — 7 outbound dependencies
5. **win.py** (`python-dateutil-2.6.1/dateutil/tz/win.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **466.0** | LOC: 254
- `_parse` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/parser.py`) -> Impact: **382.1** | LOC: 446
- `_parse_rfc` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **166.8** | LOC: 111
- `_iter` **(Compute Cores)** (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **162.7** | LOC: 255
- `__init__` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/relativedelta.py`) -> Impact: **159.7** | LOC: 125
- `parse` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/parser.py`) -> Impact: **113.3** | LOC: 152
- `rebuild` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **94.5** | LOC: 129
  * *Intent:* # Every mask is 7 days longer to handle cross-year weekly periods. rr = self.rrule if year != self.lastyear: self.yearlen = 365 + calendar.isleap(year...
- `parse` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/parser.py`) -> Impact: **93.7** | LOC: 127
  * *Intent:* """ Parse the date/time string into a :class:`datetime.datetime` object. :param timestr: Any date/time string using the supported formats. :param defa...
- `resolve_ymd` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/parser.py`) -> Impact: **90.9** | LOC: 73
- `_read_tzfile` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> Impact: **82.0** | LOC: 219

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `python-dateutil-2.6.1/dateutil` | 8 | 4721.96 | 40.08% | 3.41% |
| `python-dateutil-2.6.1/dateutil/tz` | 4 | 1897.02 | 40.56% | 23.94% |
| `python-dateutil-2.6.1/dateutil/zoneinfo` | 2 | 143.6 | 34.7% | 76.27% |
| `python-dateutil-2.6.1` | 5 | 76.14 | 12.93% | 16.35% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` -> **90.2888%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **82.5498%** Exposure
- `python-dateutil-2.6.1/setup.py` -> **81.7574%** Exposure
- `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` -> **62.2459%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **13.2077%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `python-dateutil-2.6.1/dateutil/easter.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/parser.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/rrule.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **0** Orphaned Functions | **13** Duplicates
- `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `77` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `python-dateutil-2.6.1/dateutil/tz/tz.py` (PYTHON) -> Cumulative Risk: **690.72**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.90)
- **Magnitude:** 1417.98 | **LOC:** 1512 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6236%), Tech Debt (82.5498%)
- **Heaviest Functions:** `_read_tzfile` (Many-Argument Workhorses, Impact: 82.0), `_parse_rfc` (Compute Cores, Impact: 80.3), `gettz` (Defensive Guards, Impact: 44.6)

### 2. `python-dateutil-2.6.1/dateutil/relativedelta.py` (PYTHON) -> Cumulative Risk: **648.55**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.83)
- **Magnitude:** 684.6 | **LOC:** 550 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.1331%), Documentation (93.1034%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 159.7), `__add__` (Compute Cores, Impact: 70.1), `__eq__` (Compute Cores, Impact: 46.3)

### 3. `python-dateutil-2.6.1/dateutil/parser.py` (PYTHON) -> Cumulative Risk: **632.69**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.82)
- **Magnitude:** 1589.4 | **LOC:** 1375 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.7796%), Cognitive Load (85.2622%)
- **Heaviest Functions:** `_parse` (Many-Argument Workhorses, Impact: 382.1), `parse` (Many-Argument Workhorses, Impact: 113.3), `parse` (Many-Argument Workhorses, Impact: 93.7)

### 4. `python-dateutil-2.6.1/dateutil/rrule.py` (PYTHON) -> Cumulative Risk: **607.95**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.91)
- **Magnitude:** 2316.7 | **LOC:** 1611 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.4775%), Cognitive Load (80.7833%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 466.0), `_parse_rfc` (Many-Argument Workhorses, Impact: 166.8), `_iter` (Compute Cores, Impact: 162.7)

### 5. `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` (PYTHON) -> Cumulative Risk: **591.26**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.55)
- **Magnitude:** 108.48 | **LOC:** 184 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.7105%), Tech Debt (90.2888%)
- **Heaviest Functions:** `__init__` (Defensive Guards, Impact: 17.1), `gettz` (Compute Cores, Impact: 7.5), `get_zonefile_instance` (Compute Cores, Impact: 7.0)

### 6. `python-dateutil-2.6.1/dateutil/tz/_common.py` (PYTHON) -> Cumulative Risk: **582.77**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.02)
- **Magnitude:** 238.64 | **LOC:** 395 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.8548%), Verification (80.0%)
- **Heaviest Functions:** `fromutc` (Compute Cores, Impact: 13.7), `_isdst` (Compute Cores, Impact: 13.1), `_fromutc` (Compute Cores, Impact: 8.7)

### 7. `python-dateutil-2.6.1/dateutil/tz/win.py` (PYTHON) -> Cumulative Risk: **567.28**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.13)
- **Magnitude:** 227.32 | **LOC:** 333 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.3252%), Verification (80.0%)
- **Heaviest Functions:** `__eq__` (Compute Cores, Impact: 23.4), `valuestodict` (Compute Cores, Impact: 12.5), `picknthweekday` (Many-Argument Workhorses, Impact: 5.9)

### 8. `python-dateutil-2.6.1/dateutil/_common.py` (PYTHON) -> Cumulative Risk: **507.04**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.21)
- **Magnitude:** 31.98 | **LOC:** 35 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.1837%), Safety Score (68.0112%)
- **Heaviest Functions:** `__eq__` (Defensive Guards, Impact: 5.5), `__call__` (Compute Cores, Impact: 5.4), `__repr__` (Interface Declarations, Impact: 4.5)

### 9. `python-dateutil-2.6.1/updatezinfo.py` (PYTHON) -> Cumulative Risk: **455.34**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.29)
- **Magnitude:** 34.62 | **LOC:** 56 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (87.7764%), Cognitive Load (61.7748%)
- **Heaviest Functions:** `main` (I/O & Config Routines, Impact: 7.8)

### 10. `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` (PYTHON) -> Cumulative Risk: **424.82**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.36)
- **Magnitude:** 35.12 | **LOC:** 53 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.997%), Safety Score (77.7547%), Tech Debt (62.2459%)
- **Heaviest Functions:** `rebuild` (Defensive Guards, Impact: 11.2), `_print_on_nosuchfile` (Compute Cores, Impact: 6.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `python-dateutil-2.6.1/dateutil/rrule.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2316.7 | **LOC:** 1611 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.7833%), Tech Debt (8.2212%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 466.0)
  * `_parse_rfc` **(Many-Argument Workhorses)** (Impact: 166.8)
  * `_iter` **(Compute Cores)** (Impact: 162.7)
  * `rebuild` **(Many-Argument Workhorses)** (Impact: 94.5)
    * *Intent:* # Every mask is 7 days longer to handle cross-year weekly periods. rr = self.rrule if year != self.l...
  * `between` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* """ Returns all the occurrences of the rrule between after and before. The inc keyword defines what ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 314 instances
* *State Mutation (weighted view):* 1004
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 431`, `structural_boundaries: 156`, `args: 52`, `func_start: 50`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 376`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 36`, `import: 15`
* *Defense:* `safety: 33`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ._common, calendar, datetime, dateutil, dateutil.rrule, fractions, heapq, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1589.4 | **LOC:** 1375 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.2622%), Tech Debt (9.5084%)
**Top Internal Functions/Classes:**
  * `_parse` **(Many-Argument Workhorses)** (Impact: 382.1)
  * `parse` **(Many-Argument Workhorses)** (Impact: 113.3)
  * `parse` **(Many-Argument Workhorses)** (Impact: 93.7)
    * *Intent:* """ Parse the date/time string into a :class:`datetime.datetime` object. :param timestr: Any date/ti...
  * `resolve_ymd` **(Many-Argument Workhorses)** (Impact: 90.9)
  * `get_token` **(Compute Cores)** (Impact: 64.8)
    * *Intent:* """ This function breaks the time string into lexical units (tokens), which can be parsed by the par...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 206 instances
* *State Mutation (weighted view):* 644
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 152`, `args: 41`, `func_start: 41`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 232`, `fragile_debt: 1`
* *Architecture:* `api: 29`, `import: 11`
* *Defense:* `safety: 37`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , __future__, calendar, collections, datetime, dateutil.parser, dateutil.tz, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tz/tz.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1417.98 | **LOC:** 1512 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.1372%), Tech Debt (82.5498%)
**Top Internal Functions/Classes:**
  * `_read_tzfile` **(Many-Argument Workhorses)** (Impact: 82.0)
  * `_parse_rfc` **(Compute Cores)** (Impact: 80.3)
  * `gettz` **(Defensive Guards)** (Impact: 44.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 39.1)
  * `_delta` **(Many-Argument Workhorses)** (Impact: 30.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 228 instances
* *State Mutation (weighted view):* 726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 244`, `args: 79`, `func_start: 79`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 270`, `dead_code: 2`, `duplicate_logic: 13`
* *Architecture:* `io: 13`, `api: 40`, `import: 16`
* *Defense:* `safety: 29`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 76.922
  * `Choke Point (Betweenness):` 0.029412 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 2):` ._common, .win, bisect, datetime, dateutil, dateutil.relativedelta, dateutil.tz, dateutil.zoneinfo...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/relativedelta.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 684.6 | **LOC:** 550 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.7388%), Tech Debt (9.5349%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 159.7)
  * `__add__` **(Compute Cores)** (Impact: 70.1)
  * `__eq__` **(Compute Cores)** (Impact: 46.3)
  * `__sub__` **(Compute Cores)** (Impact: 34.3)
  * `__bool__` **(Compute Cores)** (Impact: 23.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 57`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 116`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 18`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 54.36
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.126984
  * `Imports (Out-Degree: 0):` ._common, calendar, datetime, math, operator, six, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/tz/_common.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 238.64 | **LOC:** 395 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.2857%), Tech Debt (13.2077%)
**Top Internal Functions/Classes:**
  * `fromutc` **(Compute Cores)** (Impact: 13.7)
    * *Intent:* """ Given a datetime in UTC, return local time """
  * `_isdst` **(Compute Cores)** (Impact: 13.1)
  * `_fromutc` **(Compute Cores)** (Impact: 8.7)
    * *Intent:* """ Given a timezone-aware datetime in a given timezone, calculates a timezone-aware datetime in a n...
  * `enfold` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* """ Provides a unified interface for assigning the ``fold`` attribute to datetimes both before and a...
  * `utcoffset` **(Compute Cores)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 70`, `args: 24`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `state_mutation: 39`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 18`, `import: 3`
* *Defense:* `safety: 3`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, functools, six
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tz/win.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 227.32 | **LOC:** 333 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.8076%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__eq__` **(Compute Cores)** (Impact: 23.4)
    * *Intent:* # Compare on all relevant dimensions, including name. if not isinstance(other, tzwinbase): return No...
  * `valuestodict` **(Compute Cores)** (Impact: 12.5)
    * *Intent:* """Convert a registry key's values to a dictionary."""
  * `picknthweekday` **(Many-Argument Workhorses)** (Impact: 5.9)
    * *Intent:* """ dayofweek == 0 means Sunday, whichweek 5 means last instance """
  * `transitions` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* """ For a given year, get the DST on and off transition times, expressed always on the standard time...
  * `name_from_string` **(Many-Argument Workhorses)** (Impact: 4.9)
    * *Intent:* """ Parse strings as returned from the Windows registry into the time zone name as defined in the re...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 69`, `args: 20`, `func_start: 20`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 76`, `dead_code: 1`
* *Architecture:* `api: 14`, `import: 7`
* *Defense:* `safety: 8`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 262.26
  * `Choke Point (Betweenness):` 0.013072 | `Ripple Effect (Closeness):` 0.173611
  * `Imports (Out-Degree: 1):` ._common, ctypes, datetime, dateutil.tzwin, six, six.moves, struct
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 108.48 | **LOC:** 184 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.8064%), Tech Debt (90.2888%)
**Top Internal Functions/Classes:**
  * `__init__` **(Defensive Guards)** (Impact: 17.1)
  * `gettz` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* """ This retrieves a time zone from the local zoneinfo tarball that is packaged with dateutil. :para...
  * `get_zonefile_instance` **(Compute Cores)** (Impact: 7.0)
    * *Intent:* """ This is a convenience function which provides a :class:`ZoneInfoFile` instance using the data pr...
  * `gettz_db_metadata` **(I/O & Config Routines)** (Impact: 5.0)
    * *Intent:* """ Get the zonefile metadata See `zonefile_metadata`_ :returns: A dictionary with the database meta...
  * `get` **(Parameter Forwarders)** (Impact: 2.8)
    * *Intent:* """ Wrapper for :func:`ZoneInfoFile.zones.get`. This is a convenience method for retrieving zones fr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 33`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 20`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 11`, `import: 7`
* *Defense:* `safety: 5`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` contextlib, dateutil.tz, io, json, pkgutil, tarfile, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/easter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 60.64 | **LOC:** 90 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.9213%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `easter` **(Many-Argument Workhorses)** (Impact: 14.1)
    * *Intent:* """ This method was ported from the work done by GM Arts, on top of the algorithm by Claus Tondering...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 35.12 | **LOC:** 53 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.5999%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `rebuild` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* """Rebuild the internal timezone info in dateutil/zoneinfo/zoneinfo*tar* filename is the timezone ta...
  * `_print_on_nosuchfile` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* """Print helpful troubleshooting message e is an exception raised by subprocess.check_call() """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 18`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 1`, `import: 7`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dateutil.zoneinfo, json, logging, os, shutil, subprocess, tempfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/updatezinfo.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 34.62 | **LOC:** 56 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.7748%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 21`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 4`, `api: 1`, `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dateutil.zoneinfo, hashlib, io, json, os, six.moves.urllib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/_common.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 31.98 | **LOC:** 35 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.9009%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__eq__` **(Defensive Guards)** (Impact: 5.5)
  * `__call__` **(Compute Cores)** (Impact: 5.4)
  * `__repr__` **(Interface Declarations)** (Impact: 4.5)
  * `__init__` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 12`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 5`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/_version.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 17.6 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 5`
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.82 | **LOC:** 48 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.8657%), Tech Debt (81.7574%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` codecs, dateutil._version, os, os.path, re, setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/zonefile_metadata.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.5 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tz/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 13.08 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .tz
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ._version
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tzwin.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 244.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.115741
  * `Imports (Out-Degree: 1):` .tz.win
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/NEWS` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 9.2 | **LOC:** 460 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
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

- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **Severity: 2.941** (Bridge: 0.0294 * Flux: 100.0%)
- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **Severity: 1.307** (Bridge: 0.0131 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **Severity: 16.897** (Embedded: 0.1736 * Error Risk: 97.3252%)
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **Severity: 16.604** (Embedded: 0.1667 * Error Risk: 99.6236%)
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **Severity: 12.334** (Embedded: 0.127 * Error Risk: 97.1331%)
- `python-dateutil-2.6.1/dateutil/_version.py` -> **Severity: 7.557** (Embedded: 0.1111 * Error Risk: 68.0112%)
- `python-dateutil-2.6.1/dateutil/tzwin.py` -> **Severity: 7.473** (Embedded: 0.1157 * Error Risk: 64.5656%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **Severity: 15373.865** (Blast Radius: 262.26 * Doc Risk: 58.6207%)
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **Severity: 6003.67** (Blast Radius: 76.922 * Doc Risk: 78.0488%)
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **Severity: 5061.101** (Blast Radius: 54.36 * Doc Risk: 93.1034%)
- `python-dateutil-2.6.1/dateutil/_common.py` -> **Severity: 2166.8** (Blast Radius: 21.668 * Doc Risk: 100.0%)
- `python-dateutil-2.6.1/dateutil/parser.py` -> **Severity: 1704.55** (Blast Radius: 21.668 * Doc Risk: 78.6667%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
