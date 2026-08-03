# ARCHITECTURAL_BRIEF: regex
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/regex` |
| **Timestamp** | `2026-08-03T21:24:43.453512+00:00` |
| **Scan Duration** | `1.24s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 9 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 16 |
| Analyzed Artifacts (Scanned) | 11 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 15961 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.8% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 6 | 8338 | 54.5% |
| C | 3 | 7623 | 27.3% |
| PLAINTEXT | 2 | 0 | 18.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.541`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 7 | 63.6% |
| file_cluster_13 | 2 | 18.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 18.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.c`: 1x Excluded (Monolithic Amalgamation: 31587 LOC exceeds safe regex boundaries)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 96.4 | 24.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 39.2 | 50.4 | 80.0 |
| Tech Debt Exposure | 0.0 | 17.9 | 4.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.3 | 0.5 | 0.0 |
| API Exposure | 0.0 | 16.8 | 6.4 | 4.7 | 1.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 55.8 | 92.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 5.2 | 1.7 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 88.9 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 48.2 | 20.0 | 20.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 45.5 | 9.9 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 46.7 | 20.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `regex-2026.4.4/regex/tests/test_regex.py` (Hits: 16)
- `regex-2026.4.4/tools/build_regex_unicode.py` (Hits: 7)
- `regex-2026.4.4/regex/_regex_core.py` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_main.py** (`regex-2026.4.4/regex/_main.py`) — 1 inbound connections
2. **_regex_core.py** (`regex-2026.4.4/regex/_regex_core.py`) — 1 inbound connections
3. **_regex.h** (`regex-2026.4.4/src/_regex.h`) — 1 inbound connections
4. **_regex_unicode.h** (`regex-2026.4.4/src/_regex_unicode.h`) — 1 inbound connections
5. **LICENSE.txt** (`regex-2026.4.4/LICENSE.txt`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **build_regex_unicode.py** (`regex-2026.4.4/tools/build_regex_unicode.py`) — 10 outbound dependencies
2. **test_regex.py** (`regex-2026.4.4/regex/tests/test_regex.py`) — 8 outbound dependencies
3. **_regex_core.py** (`regex-2026.4.4/regex/_regex_core.py`) — 7 outbound dependencies
4. **_regex.c** (`regex-2026.4.4/src/_regex.c`) — 7 outbound dependencies
5. **_main.py** (`regex-2026.4.4/regex/_main.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `re_compile` (@ `regex-2026.4.4/src/_regex.c`) -> Impact: **658.3** | LOC: 438
- `test_hg_bugs` (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> Impact: **510.1** | LOC: 1126
- `test_properties` (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> Impact: **388.5** | LOC: 183
- `write_summary` (@ `regex-2026.4.4/tools/build_regex_unicode.py`) -> Impact: **336.1** | LOC: 142
- `test_scanner` (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> Impact: **179.8** | LOC: 202
- `unicode_at_default_boundary` (@ `regex-2026.4.4/src/_regex.c`) -> Impact: **156.7** | LOC: 134
- `parse_value_aliases` (@ `regex-2026.4.4/tools/build_regex_unicode.py`) -> Impact: **150.4** | LOC: 99
- `parse_multivalue` (@ `regex-2026.4.4/tools/build_regex_unicode.py`) -> Impact: **117.4** | LOC: 62
- `pattern_repr` (@ `regex-2026.4.4/src/_regex.c`) -> Impact: **109.6** | LOC: 92
- `test_issue_18468` (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> Impact: **94.7** | LOC: 75

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__init__` (@ `regex-2026.4.4/regex/_regex_core.py`) -> **O(2^N) [Recursive]**
- `re_compile` (@ `regex-2026.4.4/src/_regex.c`) -> **O(2^N) [Recursive]**
- `__getitem__` (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> **O(2^N) [Recursive]**
- `__getitem__` (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> **O(2^N) [Recursive]**
- `match` (@ `regex-2026.4.4/regex/_main.py`) -> **O(2^N) [Recursive]**
- `finditer` (@ `regex-2026.4.4/regex/_main.py`) -> **O(2^N) [Recursive]**
- `sub` (@ `regex-2026.4.4/regex/_main.py`) -> **O(2^N) [Recursive]**
- `subf` (@ `regex-2026.4.4/regex/_main.py`) -> **O(2^N) [Recursive]**
- `subn` (@ `regex-2026.4.4/regex/_main.py`) -> **O(2^N) [Recursive]**
- `subfn` (@ `regex-2026.4.4/regex/_main.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `re_compile` (@ `regex-2026.4.4/src/_regex.c`) -> DB Complexity: **113**
- `match_fuzzy_changes` (@ `regex-2026.4.4/src/_regex.c`) -> DB Complexity: **18**
- `unicode_at_default_boundary` (@ `regex-2026.4.4/src/_regex.c`) -> DB Complexity: **16**
- `pattern_repr` (@ `regex-2026.4.4/src/_regex.c`) -> DB Complexity: **16**
- `pattern_findall` (@ `regex-2026.4.4/src/_regex.c`) -> DB Complexity: **14**
- `locale_all_turkic_i` (@ `regex-2026.4.4/src/_regex.c`) -> DB Complexity: **13**
- `unicode_all_turkic_i` (@ `regex-2026.4.4/src/_regex.c`) -> DB Complexity: **11**
- `capture_getitem` (@ `regex-2026.4.4/src/_regex.c`) -> DB Complexity: **10**
- `test_zerowidth` (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> DB Complexity: **9**
  * *Intent:* # Issue 3262. if sys.version_info >= (3, 7, 0): self.assertEqual(regex.split(r"\b", "a b"), ['', 'a', ' ', 'b', '']) else: self.assertEqual(regex.spli...
- `test_unmatched_in_sub` (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> DB Complexity: **9**
  * *Intent:* # Issue 1519638. if sys.version_info >= (3, 7, 0): self.assertEqual(regex.sub(r"(?V0)(x)?(y)?", r"\2-\1", "xy"), 'y-x-') else: self.assertEqual(regex....

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `regex-2026.4.4/src` | 3 | 8409.26 | 33.55% | 3.05% |
| `regex-2026.4.4/regex/tests` | 1 | 2694.98 | 4.52% | 0.0% |
| `regex-2026.4.4/regex` | 3 | 1551.0 | 29.87% | 4.44% |
| `regex-2026.4.4` | 3 | 53.38 | 1.67% | 0.0% |
| `regex-2026.4.4/tools` | 1 | 1.25 | 21.22% | 17.87% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **17.8716%** Exposure
- `regex-2026.4.4/regex/_main.py` -> **13.319%** Exposure
- `regex-2026.4.4/src/_regex.c` -> **9.1459%** Exposure
### Highest State Flux (Mutation/Volatility)
- `regex-2026.4.4/src/_regex.c` -> **100.0%** Exposure
- `regex-2026.4.4/setup.py` -> **99.9556%** Exposure
- `regex-2026.4.4/regex/_regex_core.py` -> **99.8974%** Exposure
- `regex-2026.4.4/regex/_main.py` -> **98.7454%** Exposure
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **92.4915%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `regex-2026.4.4/regex/tests/test_regex.py` -> **86** Orphaned Functions | **2** Duplicates
- `regex-2026.4.4/src/_regex.c` -> **14** Orphaned Functions | **0** Duplicates
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **5** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`regex-2026.4.4/regex/tests/test_regex.py`** -> AI Confidence: **99.48%**
2. **`regex-2026.4.4/src/_regex.c`** -> AI Confidence: **99.34%**
3. **`regex-2026.4.4/regex/_regex_core.py`** -> AI Confidence: **99.31%**
4. **`regex-2026.4.4/tools/build_regex_unicode.py`** -> AI Confidence: **99.31%**
5. **`regex-2026.4.4/regex/_main.py`** -> AI Confidence: **99.13%**
6. **`regex-2026.4.4/setup.py`** -> AI Confidence: **98.87%**
7. **`regex-2026.4.4/regex/__init__.py`** -> AI Confidence: **98.84%**
8. **`regex-2026.4.4/src/_regex.h`** -> AI Confidence: **98.84%**
9. **`regex-2026.4.4/src/_regex_unicode.h`** -> AI Confidence: **98.73%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `regex-2026.4.4/regex/_main.py` -> **100.0%** Exposure
- `regex-2026.4.4/regex/_regex_core.py` -> **100.0%** Exposure
- `regex-2026.4.4/regex/tests/test_regex.py` -> **100.0%** Exposure
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **100.0%** Exposure
- `regex-2026.4.4/src/_regex.c` -> **20.0%** Exposure
### Algorithmic DoS Exposure
- `regex-2026.4.4/regex/_main.py` -> **100.0%** Exposure
- `regex-2026.4.4/regex/tests/test_regex.py` -> **100.0%** Exposure
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **100.0%** Exposure
- `regex-2026.4.4/src/_regex.c` -> **100.0%** Exposure
- `regex-2026.4.4/regex/_regex_core.py` -> **9.9182%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `42` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `regex-2026.4.4/src/_regex.c` (C) -> Cumulative Risk: **659.05**
- **Archetype:** `file_cluster_8` (Distance: 14.642 IQR)
- **Magnitude:** 8241.92 | **LOC:** 26651 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.4517%)
- **Heaviest Functions:** `re_compile` (Impact: 658.3), `unicode_at_default_boundary` (Impact: 156.7), `pattern_repr` (Impact: 109.6)

### 2. `regex-2026.4.4/tools/build_regex_unicode.py` (PYTHON) -> Cumulative Risk: **640.34**
- **Archetype:** `file_cluster_8` (Distance: 11.027 IQR)
- **Magnitude:** 1.25 | **LOC:** 1786 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (96.3583%)
- **Heaviest Functions:** `write_summary` (Impact: 336.1), `parse_value_aliases` (Impact: 150.4), `parse_multivalue` (Impact: 117.4)

### 3. `regex-2026.4.4/regex/_main.py` (PYTHON) -> Cumulative Risk: **639.21**
- **Archetype:** `file_cluster_8` (Distance: 11.84 IQR)
- **Magnitude:** 288.08 | **LOC:** 757 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (98.7454%)
- **Heaviest Functions:** `escape` (Impact: 86.8), `match` (Impact: 20.2), `compile` (Impact: 7.6)

### 4. `regex-2026.4.4/regex/_regex_core.py` (PYTHON) -> Cumulative Risk: **603.16**
- **Archetype:** `file_cluster_8` (Distance: 12.635 IQR)
- **Magnitude:** 1250.36 | **LOC:** 4677 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.8974%), Documentation (83.0439%)
- **Heaviest Functions:** `__init__` (Impact: 67.9), `__repr__` (Impact: 40.4)

### 5. `regex-2026.4.4/regex/tests/test_regex.py` (PYTHON) -> Cumulative Risk: **374.17**
- **Archetype:** `file_cluster_8` (Distance: 10.548 IQR)
- **Magnitude:** 2694.98 | **LOC:** 4541 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_hg_bugs` (Impact: 510.1), `test_properties` (Impact: 388.5), `test_scanner` (Impact: 179.8)

### 6. `regex-2026.4.4/setup.py` (PYTHON) -> Cumulative Risk: **318.0**
- **Archetype:** `file_cluster_13` (Distance: 8.841 IQR)
- **Magnitude:** 18.24 | **LOC:** 17 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9556%), Spec Match (80.0%), Safety Score (71.6667%), Stability (50.0%)

### 7. `regex-2026.4.4/src/_regex_unicode.h` (C) -> Cumulative Risk: **273.31**
- **Archetype:** `file_cluster_8` (Distance: 7.631 IQR)
- **Magnitude:** 146.0 | **LOC:** 319 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Stability (50.0%), Api Exposure (16.7684%)

### 8. `regex-2026.4.4/src/_regex.h` (C) -> Cumulative Risk: **182.79**
- **Archetype:** `file_cluster_8` (Distance: 6.106 IQR)
- **Magnitude:** 21.34 | **LOC:** 236 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Documentation (13.9558%), State Flux (10.9519%)

### 9. `regex-2026.4.4/regex/__init__.py` (PYTHON) -> Cumulative Risk: **176.42**
- **Archetype:** `file_cluster_13` (Distance: 6.344 IQR)
- **Magnitude:** 12.56 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (80.0%), Stability (50.0%), Spec Match (20.0%), Documentation (20.0%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `regex-2026.4.4/src/_regex.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.642 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.229 IQR)
- **Top Global Matches:** file_cluster_8: 14.642, file_cluster_11: 14.872, file_cluster_0: 14.902
- **Magnitude:** 8241.92 | **LOC:** 26651 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 113
- **Risk Profile:** Cognitive Load (96.4033%), Tech Debt (9.1459%)
**Top Internal Functions/Classes:**
  * `re_compile` (Impact: 658.3 | O(2^N) | DB: 113)
  * `unicode_at_default_boundary` (Impact: 156.7 | O(N^5) | DB: 16)
  * `pattern_repr` (Impact: 109.6 | O(N^5) | DB: 16)
  * `match_fuzzy_changes` (Impact: 43.8 | O(N^3) | DB: 18)
  * `pattern_findall` (Impact: 37.9 | O(N^3) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2131`, `structural_boundaries: 947`, `args: 85`, `func_start: 78`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 70`, `state_mutation: 4652`, `orphaned_logic: 14`
* *Architecture:* `api: 2048`, `import: 7`
* *Defense:* `safety: 148`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pythread.h, ctype.h, _regex.h, pyport.h, Python.h, time.h, structmember.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/regex/tests/test_regex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.548 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.281 IQR)
- **Top Global Matches:** file_cluster_8: 10.548, file_cluster_7: 10.954, file_cluster_1: 11.184
- **Magnitude:** 2694.98 | **LOC:** 4541 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (4.5204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_hg_bugs` (Impact: 510.1 | O(N^3) | DB: 8)
  * `test_properties` (Impact: 388.5 | O(N^5))
  * `test_scanner` (Impact: 179.8 | O(N^3))
  * `test_issue_18468` (Impact: 94.7 | O(N^4) | DB: 6)
  * `test_repeat_minmax` (Impact: 82.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 701`, `structural_boundaries: 164`, `args: 117`, `func_start: 111`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 9`, `dead_code: 1`, `fragile_debt: 66`, `duplicate_logic: 2`, `orphaned_logic: 86`
* *Architecture:* `io: 16`, `api: 113`, `import: 8`
* *Defense:* `safety: 7`, `doc: 138`, `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string, copy, unittest, weakref, regex, pickle, sys, array
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/regex/_regex_core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.635 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.092 IQR)
- **Top Global Matches:** file_cluster_8: 12.635, file_cluster_0: 12.933, file_cluster_13: 13.029
- **Magnitude:** 1250.36 | **LOC:** 4677 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (51.2914%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 67.9 | O(2^N) | DB: 5)
  * `__repr__` (Impact: 40.4 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 937`, `structural_boundaries: 912`, `args: 355`, `func_start: 353`, `class_start: 61`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 760`, `dead_code: 5`
* *Architecture:* `io: 3`, `api: 316`, `import: 6`
* *Defense:* `safety: 111`, `doc: 12`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 162.354
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 0):` enum, unicodedata, string, collections, is, regex, random
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `regex-2026.4.4/regex/_main.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.84 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.971 IQR)
- **Top Global Matches:** file_cluster_8: 11.84, file_cluster_13: 11.869, file_cluster_7: 12.092
- **Magnitude:** 288.08 | **LOC:** 757 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (33.315%), Tech Debt (13.319%)
**Top Internal Functions/Classes:**
  * `escape` (Impact: 86.8 | O(N^4) | DB: 8)
  * `match` (Impact: 20.2 | O(2^N))
  * `compile` (Impact: 7.6 | O(N^2))
  * `finditer` (Impact: 7.3 | O(2^N))
  * `sub` (Impact: 7.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 89`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 56`, `fragile_debt: 1`
* *Architecture:* `api: 21`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 22`, `doc: 28`, `sync_locks: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 116.756
  * `Choke Point (Betweenness):` 0.011111 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` threading, copyreg, regex, regex._regex_core, locale
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `regex-2026.4.4/src/_regex_unicode.h` (C | Tier 0 | 🚨 AI THREAT: 98.73%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.631 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.486 IQR)
- **Top Global Matches:** file_cluster_8: 7.631, file_cluster_7: 8.603, file_cluster_1: 8.849
- **Magnitude:** 146.0 | **LOC:** 319 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.241%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 125`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 162.354
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `regex-2026.4.4/changelog.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 30.96 | **LOC:** 1548 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/src/_regex.h` (C | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.106 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.524 IQR)
- **Top Global Matches:** file_cluster_8: 6.106, file_cluster_7: 7.468, file_cluster_1: 7.565
- **Magnitude:** 21.34 | **LOC:** 236 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 116.756
  * `Choke Point (Betweenness):` 0.011111 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` _regex_unicode.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `regex-2026.4.4/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.841 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.854 IQR)
- **Top Global Matches:** file_cluster_13: 8.841, file_cluster_8: 9.162, file_cluster_7: 9.964
- **Magnitude:** 18.24 | **LOC:** 17 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` setuptools, os.path, sysconfig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/regex/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.344 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.235 IQR)
- **Top Global Matches:** file_cluster_13: 6.344, file_cluster_8: 6.852, file_cluster_7: 7.778
- **Magnitude:** 12.56 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` regex._main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/LICENSE.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 4.18 | **LOC:** 209 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/tools/build_regex_unicode.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.027 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.136 IQR)
- **Top Global Matches:** file_cluster_8: 11.027, file_cluster_7: 11.346, file_cluster_13: 11.385
- **Magnitude:** 1.25 | **LOC:** 1786 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (21.2195%), Tech Debt (17.8716%)
**Top Internal Functions/Classes:**
  * `write_summary` (Impact: 336.1 | O(N^6) | DB: 6)
  * `parse_value_aliases` (Impact: 150.4 | O(N^5) | DB: 2)
  * `parse_multivalue` (Impact: 117.4 | O(N^5))
  * `parse_numeric_values` (Impact: 53.6 | O(N^5))
  * `parse_script_extensions` (Impact: 53.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 146`, `args: 59`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 129`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 7`, `api: 47`, `import: 10`
* *Defense:* `safety: 12`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` contextlib, os.path, time, re, codecs, os, itertools, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `regex-2026.4.4/setup.py` (PYTHON) | Magnitude: 18.24 | Delta: **0.321 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, state_mutation: 3, import: 3, encapsulation: 3
- `regex-2026.4.4/regex/__init__.py` (PYTHON) | Magnitude: 12.56 | Delta: **0.508 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 5, structural_boundaries: 3, import: 2, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `regex-2026.4.4/regex/_main.py` (PYTHON) | Magnitude: 288.08 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 269, encapsulation: 118, structural_boundaries: 89, branch: 87
- `regex-2026.4.4/src/_regex.c` (C) | Magnitude: 8241.92 | Delta: **0.23 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 6410, state_mutation: 4652, pointers: 2477, branch: 2131
- `regex-2026.4.4/regex/_regex_core.py` (PYTHON) | Magnitude: 1250.36 | Delta: **0.298 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 3055, branch: 937, structural_boundaries: 912, state_mutation: 760
- `regex-2026.4.4/tools/build_regex_unicode.py` (PYTHON) | Magnitude: 1.25 | Delta: **0.319 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 998, branch: 315, structural_boundaries: 146, state_mutation: 129
- `regex-2026.4.4/regex/tests/test_regex.py` (PYTHON) | Magnitude: 2694.98 | Delta: **0.406 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 3546, branch: 701, sec_reflection_metaprogramming: 410, bitwise_ops: 301

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `regex-2026.4.4/regex/_main.py` -> **Severity: 1.097** (Bridge: 0.0111 * Flux: 98.7454%)
- `regex-2026.4.4/src/_regex.h` -> **Severity: 0.122** (Bridge: 0.0111 * Flux: 10.9519%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `regex-2026.4.4/regex/_main.py` -> **Severity: 5.038** (Embedded: 0.1 * Error Risk: 50.3762%)
- `regex-2026.4.4/regex/_regex_core.py` -> **Severity: 2.297** (Embedded: 0.1333 * Error Risk: 17.2288%)
- `regex-2026.4.4/src/_regex.h` -> **Severity: 0.535** (Embedded: 0.1 * Error Risk: 5.3483%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `regex-2026.4.4/src/_regex_unicode.h` -> **Severity: 16235.4** (Blast Radius: 162.354 * Doc Risk: 100.0%)
- `regex-2026.4.4/regex/_regex_core.py` -> **Severity: 13482.509** (Blast Radius: 162.354 * Doc Risk: 83.0439%)
- `regex-2026.4.4/src/_regex.c` -> **Severity: 6213.385** (Blast Radius: 63.111 * Doc Risk: 98.4517%)
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **Severity: 6081.269** (Blast Radius: 63.111 * Doc Risk: 96.3583%)
- `regex-2026.4.4/src/_regex.h` -> **Severity: 1629.423** (Blast Radius: 116.756 * Doc Risk: 13.9558%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
