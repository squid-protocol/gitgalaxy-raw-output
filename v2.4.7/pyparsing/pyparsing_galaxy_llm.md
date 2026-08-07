# ARCHITECTURAL_BRIEF: pyparsing
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/pyparsing` |
| **Timestamp** | `2026-08-07T05:25:31.922958+00:00` |
| **Scan Duration** | `1.63s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 153 malicious artifacts.

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
| Total Artifacts | 258 |
| Analyzed Artifacts (Scanned) | 194 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 64 |
| Total LOC | 60228 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 75.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6638 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4636 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5832 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 151 | 25325 | 77.8% |
| HTML | 31 | 34668 | 16.0% |
| MARKDOWN | 7 | 0 | 3.6% |
| PLAINTEXT | 3 | 0 | 1.5% |
| BATCH | 1 | 122 | 0.5% |
| SHELL | 1 | 113 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.99`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 156 | 80.4% |
| file_cluster_13 | 18 | 9.3% |
| file_cluster_16 | 5 | 2.6% |
| file_cluster_9 | 2 | 1.0% |
| file_cluster_11 | 1 | 0.5% |
| file_cluster_0 | 1 | 0.5% |
| file_cluster_7 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 5.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 64*

**Composition by Extension & Reason:**
- `.png`: 28x Excluded (Explicitly Denied Extension: '.png')
- `.tiny`: 11x Excluded (Unsupported Extension: '.tiny')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.pystate`: 4x Excluded (Unsupported Extension: '.pystate')
- `.ini`: 3x Excluded (Unsupported Extension: '.ini')
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.dfm`: 2x Excluded (Unsupported Extension: '.dfm')
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 205 LOC)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.g`: 1x Excluded (Unsupported Extension: '.g')
- `.ics`: 1x Excluded (Unsupported Extension: '.ics')
- `.html`: 1x Excluded (Saturation: Line 93 exceeds 500 chars)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 95.3 | 8.6 | 5.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.1 | 26.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.4 | 3.6 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 1.9 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.2 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 66.6 | 2.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyparsing-3.3.2/examples/decaf_parser_diagram.html` (Hits: 510)
- `pyparsing-3.3.2/examples/antlr_grammar_diagram.html` (Hits: 478)
- `pyparsing-3.3.2/examples/lua_parser_diagram.html` (Hits: 428)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.py** (`pyparsing-3.3.2/pyparsing/util.py`) — 8 inbound connections
2. **warnings.py** (`pyparsing-3.3.2/pyparsing/warnings.py`) — 7 inbound connections
3. **core.py** (`pyparsing-3.3.2/pyparsing/core.py`) — 6 inbound connections
4. **statemachine.py** (`pyparsing-3.3.2/examples/statemachine/statemachine.py`) — 5 inbound connections
5. **tiny_parser.py** (`pyparsing-3.3.2/examples/tiny/tiny_parser.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_unit.py** (`pyparsing-3.3.2/tests/test_unit.py`) — 35 outbound dependencies
2. **core.py** (`pyparsing-3.3.2/pyparsing/core.py`) — 29 outbound dependencies
3. **make_diagram.py** (`pyparsing-3.3.2/examples/make_diagram.py`) — 21 outbound dependencies
4. **test_diagram.py** (`pyparsing-3.3.2/tests/test_diagram.py`) — 16 outbound dependencies
5. **__init__.py** (`pyparsing-3.3.2/pyparsing/__init__.py`) — 15 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `testCuneiformTransformString` (@ `pyparsing-3.3.2/tests/test_unit.py`) -> Impact: **369.8** | LOC: 1576
- `testParseResultsNamesInGroupWithDict` (@ `pyparsing-3.3.2/tests/test_unit.py`) -> Impact: **284.7** | LOC: 1399
  * *Intent:* """test simple case of ParseResults.values()"""
- `testCommonUrlParts` (@ `pyparsing-3.3.2/tests/test_unit.py`) -> Impact: **154.7** | LOC: 566
  * *Intent:* # left arity > 3 - should raise ValueError with self.assertRaises(ValueError): expr = pp.infix_notation( num, [ ("*", 4, pp.OpAssoc.LEFT), ] )
- `Test` (@ `pyparsing-3.3.2/examples/booleansearchparser.py`) -> Impact: **118.3** | LOC: 115
- `handle_meta_command` (@ `pyparsing-3.3.2/examples/tiny/tiny_repl.py`) -> Impact: **110.2** | LOC: 205
- `_collapse_verbose_regex` (@ `pyparsing-3.3.2/pyparsing/diagram/__init__.py`) -> Impact: **99.0** | LOC: 299
- `_assignfunc` (@ `pyparsing-3.3.2/examples/LAparser.py`) -> Impact: **85.1** | LOC: 247
- `find_python_for_version_[Truncated]` (@ `pyparsing-3.3.2/run_perf_all_tags.sh`) -> Impact: **75.7** | LOC: 100
- `expand_state_definition` (@ `pyparsing-3.3.2/examples/statemachine/statemachine.py`) -> Impact: **54.0** | LOC: 200
  * *Intent:* """ Parse action to convert statemachine to corresponding Python classes and methods """
- `testLocatedExprUsingLocated` (@ `pyparsing-3.3.2/tests/test_unit.py`) -> Impact: **41.3** | LOC: 271

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pyparsing-3.3.2/examples` | 132 | 8311.52 | 6.35% | 0.0% |
| `pyparsing-3.3.2/tests` | 17 | 2886.54 | 3.66% | 0.0% |
| `pyparsing-3.3.2/pyparsing` | 11 | 2534.8 | 19.04% | 30.64% |
| `pyparsing-3.3.2/examples/tiny` | 7 | 790.12 | 12.61% | 0.0% |
| `pyparsing-3.3.2/examples/statemachine` | 6 | 307.6 | 28.18% | 0.0% |
| `pyparsing-3.3.2` | 4 | 247.14 | 23.82% | 14.82% |
| `pyparsing-3.3.2/dest` | 3 | 220.82 | 8.37% | 33.33% |
| `pyparsing-3.3.2/examples/regex_inverter` | 3 | 220.82 | 8.37% | 0.0% |
| `pyparsing-3.3.2/pyparsing/diagram` | 1 | 184.4 | 17.35% | 11.25% |
| `pyparsing-3.3.2/examples/tiny/tests` | 3 | 107.78 | 4.37% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `pyparsing-3.3.2/dest/inv_regex.py` -> **99.9999%** Exposure
- `pyparsing-3.3.2/pyparsing/util.py` -> **99.9962%** Exposure
- `pyparsing-3.3.2/pyparsing/exceptions.py` -> **99.8867%** Exposure
- `pyparsing-3.3.2/pyparsing/results.py` -> **97.7023%** Exposure
- `pyparsing-3.3.2/run_perf_all_tags.sh` -> **59.2934%** Exposure
### Highest State Flux (Mutation/Volatility)
- `pyparsing-3.3.2/run_perf_all_tags.sh` -> **100.0%** Exposure
- `pyparsing-3.3.2/pyparsing/util.py` -> **99.9772%** Exposure
- `pyparsing-3.3.2/pyparsing/core.py` -> **99.9625%** Exposure
- `pyparsing-3.3.2/pyparsing/exceptions.py` -> **99.6404%** Exposure
- `pyparsing-3.3.2/pyparsing/actions.py` -> **99.6275%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyparsing-3.3.2/tests/test_unit.py` -> **82** Orphaned Functions | **25** Duplicates
- `pyparsing-3.3.2/examples/adventureEngine.py` -> **0** Orphaned Functions | **47** Duplicates
- `pyparsing-3.3.2/tests/test_pre_pep8_deprecation_warnings.py` -> **45** Orphaned Functions | **0** Duplicates
- `pyparsing-3.3.2/examples/tiny/tiny_ast.py` -> **0** Orphaned Functions | **25** Duplicates
- `pyparsing-3.3.2/tests/test_examples.py` -> **19** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pyparsing-3.3.2/pyparsing/core.py`** -> AI Confidence: **99.31%**
2. **`pyparsing-3.3.2/pyparsing/diagram/__init__.py`** -> AI Confidence: **99.31%**
3. **`pyparsing-3.3.2/pyparsing/helpers.py`** -> AI Confidence: **99.31%**
4. **`pyparsing-3.3.2/pyparsing/results.py`** -> AI Confidence: **99.31%**
5. **`pyparsing-3.3.2/pyparsing/tools/cvt_pyparsing_pep8_names.py`** -> AI Confidence: **99.31%**
6. **`pyparsing-3.3.2/pyparsing/util.py`** -> AI Confidence: **99.31%**
7. **`pyparsing-3.3.2/tests/test_unit.py`** -> AI Confidence: **99.31%**
8. **`pyparsing-3.3.2/run_perf_all_tags.sh`** -> AI Confidence: **99.29%**
9. **`pyparsing-3.3.2/examples/tiny/tiny_repl.py`** -> AI Confidence: **99.24%**
10. **`pyparsing-3.3.2/examples/tiny/tiny_run.py`** -> AI Confidence: **99.24%**
11. **`pyparsing-3.3.2/tests/test_pre_pep8_deprecation_warnings.py`** -> AI Confidence: **99.23%**
12. **`pyparsing-3.3.2/tests/test_util.py`** -> AI Confidence: **99.23%**
13. **`pyparsing-3.3.2/pyparsing/exceptions.py`** -> AI Confidence: **99.18%**
14. **`pyparsing-3.3.2/examples/TAP.py`** -> AI Confidence: **99.17%**
15. **`pyparsing-3.3.2/tests/test_matplotlib_cases.py`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `476` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyparsing-3.3.2/run_perf_all_tags.sh` (SHELL) -> Cumulative Risk: **596.96**
- **Archetype:** `file_cluster_8` (Distance: 12.483 IQR)
- **Magnitude:** 135.46 | **LOC:** 160 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.0892%), Cognitive Load (95.2972%)
- **Heaviest Functions:** `find_python_for_version_[Truncated]` (Impact: 75.7), `__global_context__` (Impact: 4.5)

### 2. `pyparsing-3.3.2/pyparsing/util.py` (PYTHON) -> Cumulative Risk: **591.96**
- **Archetype:** `file_cluster_13` (Distance: 12.24 IQR)
- **Magnitude:** 256.0 | **LOC:** 515 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9962%), State Flux (99.9772%), Verification (80.0%)
- **Heaviest Functions:** `replaced_by_pep8` (Impact: 14.2), `_set` (Impact: 10.7), `_flatten` (Impact: 10.7)

### 3. `pyparsing-3.3.2/pyparsing/exceptions.py` (PYTHON) -> Cumulative Risk: **575.19**
- **Archetype:** `file_cluster_13` (Distance: 11.555 IQR)
- **Magnitude:** 128.74 | **LOC:** 354 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8867%), State Flux (99.6404%), Verification (80.0%)
- **Heaviest Functions:** `explain_exception` (Impact: 25.0), `found` (Impact: 11.1), `__str__` (Impact: 5.7)

### 4. `pyparsing-3.3.2/pyparsing/results.py` (PYTHON) -> Cumulative Risk: **524.05**
- **Archetype:** `file_cluster_16` (Distance: 12.625 IQR)
- **Magnitude:** 440.36 | **LOC:** 929 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.4878%), Tech Debt (97.7023%), Verification (80.0%)
- **Heaviest Functions:** `dump` (Impact: 39.5), `deepcopy` (Impact: 21.7), `pop` (Impact: 18.9)

### 5. `pyparsing-3.3.2/dest/inv_regex.py` (PYTHON) -> Cumulative Risk: **508.68**
- **Archetype:** `file_cluster_8` (Distance: 9.078 IQR)
- **Magnitude:** 187.98 | **LOC:** 349 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Verification (80.0%), Documentation (66.5728%)
- **Heaviest Functions:** `handle_macro` (Impact: 14.9), `handle_repetition` (Impact: 14.8), `make_generator` (Impact: 11.1)

### 6. `pyparsing-3.3.2/pyparsing/actions.py` (PYTHON) -> Cumulative Risk: **460.1**
- **Archetype:** `file_cluster_16` (Distance: 11.672 IQR)
- **Magnitude:** 75.22 | **LOC:** 265 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6275%), Safety Score (89.6805%), Verification (80.0%)
- **Heaviest Functions:** `with_attribute` (Impact: 13.2), `pa` (Impact: 10.5), `with_class` (Impact: 5.4)

### 7. `pyparsing-3.3.2/pyparsing/core.py` (PYTHON) -> Cumulative Risk: **390.55**
- **Archetype:** `file_cluster_16` (Distance: 13.87 IQR)
- **Magnitude:** 1200.44 | **LOC:** 6952 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9625%), Safety Score (65.2906%), Stability (50.0%)
- **Heaviest Functions:** `enable_all_warnings` (Impact: 3.6), `enable_diag` (Impact: 2.2), `disable_diag` (Impact: 2.2)

### 8. `pyparsing-3.3.2/pyparsing/diagram/__init__.py` (PYTHON) -> Cumulative Risk: **379.6**
- **Archetype:** `file_cluster_13` (Distance: 11.113 IQR)
- **Magnitude:** 184.4 | **LOC:** 762 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (51.695%), Stability (50.0%)
- **Heaviest Functions:** `_collapse_verbose_regex` (Impact: 99.0), `_apply_diagram_item_enhancements` (Impact: 12.5), `_make_bookmark` (Impact: 7.0)

### 9. `pyparsing-3.3.2/pyparsing/helpers.py` (PYTHON) -> Cumulative Risk: **368.8**
- **Archetype:** `file_cluster_8` (Distance: 11.035 IQR)
- **Magnitude:** 201.52 | **LOC:** 1221 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Stability (50.0%), Safety Score (48.3999%)
- **Heaviest Functions:** `indentedBlock` (Impact: 36.7), `_makeTags` (Impact: 12.8), `checkUnindent` (Impact: 10.4)

### 10. `pyparsing-3.3.2/examples/macro_expander.py` (PYTHON) -> Cumulative Risk: **324.54**
- **Archetype:** `file_cluster_9` (Distance: 23.111 IQR)
- **Magnitude:** 4.22 | **LOC:** 65 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Dead Code (98.6714%), Safety Score (67.2285%), Stability (50.0%)
- **Heaviest Functions:** `process_macro_ref` (Impact: 1.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyparsing-3.3.2/tests/test_unit.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.619 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.296 IQR)
- **Top Global Matches:** file_cluster_8: 11.619, file_cluster_7: 11.869, file_cluster_13: 12.097
- **Magnitude:** 2011.26 | **LOC:** 11447 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.8098%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testCuneiformTransformString` (Impact: 369.8)
  * `testParseResultsNamesInGroupWithDict` (Impact: 284.7)
    * *Intent:* """test simple case of ParseResults.values()"""
  * `testCommonUrlParts` (Impact: 154.7)
    * *Intent:* # left arity > 3 - should raise ValueError with self.assertRaises(ValueError): expr = pp.infix_notat...
  * `testLocatedExprUsingLocated` (Impact: 41.3)
  * `testWarnUsingLshiftForward` (Impact: 27.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 603`, `structural_boundaries: 554`, `args: 303`, `func_start: 264`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 4`, `state_mutation: 70`, `dead_code: 7`, `fragile_debt: 6`, `duplicate_logic: 25`, `orphaned_logic: 82`
* *Architecture:* `io: 21`, `api: 266`, `import: 45`
* *Defense:* `safety: 130`, `doc: 454`, `test: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pprint, operator, io, sysconfig, shlex, unicodedata, itertools, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/pyparsing/core.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.87 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.112 IQR)
- **Top Global Matches:** file_cluster_16: 13.87, file_cluster_8: 14.0, file_cluster_13: 14.026
- **Magnitude:** 1200.44 | **LOC:** 6952 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.1642%), Tech Debt (10.4982%)
**Top Internal Functions/Classes:**
  * `enable_all_warnings` (Impact: 3.6)
  * `enable_diag` (Impact: 2.2)
  * `disable_diag` (Impact: 2.2)
  * `enable_all_warnings` (Impact: 1.9)
  * `_should_enable_warnings` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1031`, `structural_boundaries: 775`, `args: 304`, `func_start: 290`, `class_start: 62`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 908`, `dead_code: 7`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 10`, `api: 209`, `concurrency: 1`, `import: 29`
* *Defense:* `safety: 234`, `doc: 332`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.254
  * `Choke Point (Betweenness):` 0.000654 | `Ripple Effect (Closeness):` 0.031572
  * `Imports (Out-Degree: 7):` collections.abc, operator, functools, .unicode, pathlib, types, .results, typing...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/ebnf.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.288 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.809 IQR)
- **Top Global Matches:** file_cluster_8: 9.288, file_cluster_13: 9.739, file_cluster_17: 9.94
- **Magnitude:** 928.74 | **LOC:** 186 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.8664%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 41`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 14`, `import: 2`
* *Defense:* `safety: 4`, `doc: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005155
  * `Imports (Out-Degree: 0):` pyparsing, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/gen_ctypes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.566 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.791 IQR)
- **Top Global Matches:** file_cluster_8: 8.566, file_cluster_13: 9.413, file_cluster_17: 9.413
- **Magnitude:** 828.93 | **LOC:** 206 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.0937%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 17`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 5`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyparsing, ctypes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/adventureEngine.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.119 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.611 IQR)
- **Top Global Matches:** file_cluster_8: 11.119, file_cluster_0: 11.318, file_cluster_13: 11.435
- **Magnitude:** 534.84 | **LOC:** 745 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.8779%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createRooms` (Impact: 33.7)
    * *Intent:* """ create rooms, using multiline string showing map layout string contains symbols for the followin...
  * `_do_command` (Impact: 16.5)
  * `_do_command` (Impact: 12.8)
  * `_do_command` (Impact: 12.8)
  * `describe` (Impact: 12.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 131`, `args: 73`, `func_start: 72`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 103`, `duplicate_logic: 47`
* *Architecture:* `io: 7`, `api: 60`, `import: 4`
* *Defense:* `safety: 5`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005155
  * `Imports (Out-Degree: 0):` string, random, pyparsing, contextlib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/lucene_grammar.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.306 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.699 IQR)
- **Top Global Matches:** file_cluster_8: 8.306, file_cluster_7: 8.921, file_cluster_13: 8.952
- **Magnitude:** 460.72 | **LOC:** 380 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8118%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 8`, `args: 6`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 1`, `import: 4`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005155
  * `Imports (Out-Degree: 0):` sys, pyparsing, contextlib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/pyparsing/results.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.625 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.382 IQR)
- **Top Global Matches:** file_cluster_16: 12.625, file_cluster_13: 12.648, file_cluster_8: 12.697
- **Magnitude:** 440.36 | **LOC:** 929 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.1022%), Tech Debt (97.7023%)
**Top Internal Functions/Classes:**
  * `dump` (Impact: 39.5)
  * `deepcopy` (Impact: 21.7)
  * `pop` (Impact: 18.9)
  * `get_name` (Impact: 18.6)
  * `__new__` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 127`, `args: 46`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 77`, `duplicate_logic: 10`
* *Architecture:* `api: 35`, `import: 6`
* *Defense:* `safety: 39`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.025
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.027491
  * `Imports (Out-Degree: 1):` collections.abc, pprint, json, typing, pyparsing, .util, collections, __future__
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/tests/test_pre_pep8_deprecation_warnings.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.808 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.464 IQR)
- **Top Global Matches:** file_cluster_8: 11.808, file_cluster_13: 12.08, file_cluster_7: 12.436
- **Magnitude:** 315.22 | **LOC:** 438 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.0421%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_enablePackrat_emits_DeprecationWarn` (Impact: 10.9)
    * *Intent:* # Record initial packrat state; restore it after test completes initially_enabled = getattr(ParserEl...
  * `test_one_of_asKeyword_kwarg_emits_Deprec` (Impact: 10.6)
  * `test_scanString_emits_DeprecationWarning` (Impact: 8.9)
  * `test_infixNotation_emits_DeprecationWarn` (Impact: 5.8)
  * `test_replaceHTMLEntity_emits_Deprecation` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 136`, `args: 52`, `func_start: 46`
* *Risk/State:* `orphaned_logic: 45`
* *Architecture:* `api: 46`, `import: 15`
* *Defense:* `safety: 54`, `doc: 2`, `test: 138`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pyparsing, pyparsing.results, pytest, warnings, pyparsing.actions, pyparsing.helpers, datetime
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/directx_x_file_parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.778 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.127 IQR)
- **Top Global Matches:** file_cluster_8: 7.778, file_cluster_7: 8.414, file_cluster_1: 8.643
- **Magnitude:** 304.07 | **LOC:** 204 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.3197%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 12`, `args: 5`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyparsing, contextlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/booleansearchparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.19 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.771 IQR)
- **Top Global Matches:** file_cluster_8: 10.19, file_cluster_7: 10.538, file_cluster_13: 10.73
- **Magnitude:** 274.14 | **LOC:** 454 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.7298%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Test` (Impact: 118.3)
  * `parser` (Impact: 21.9)
  * `evaluateWord` (Impact: 16.4)
    * *Intent:* """ This function returns a parser. The grammar should be like most full text search engines (Google...
  * `_split_words` (Impact: 9.5)
  * `main` (Impact: 9.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 49`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 27`, `planned_debt: 1`
* *Architecture:* `api: 21`, `import: 2`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string, pyparsing, booleansearchparser, re, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/pyparsing/util.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.24 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.516 IQR)
- **Top Global Matches:** file_cluster_13: 12.24, file_cluster_16: 12.388, file_cluster_0: 12.42
- **Magnitude:** 256.0 | **LOC:** 515 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.3354%), Tech Debt (99.9962%)
**Top Internal Functions/Classes:**
  * `replaced_by_pep8` (Impact: 14.2)
  * `_set` (Impact: 10.7)
  * `_flatten` (Impact: 10.7)
  * `_convert_escaped_numerics_to_char` (Impact: 10.4)
    * *Intent:* # Developer notes: # - Do not optimize this code assuming that the given input string # or internal ...
  * `get_suffixes_from_common_prefixes` (Impact: 10.3)
    * *Intent:* # _ is unimportant, is just used to identify groups # chars is an iterator of one or more consecutiv...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 83`, `args: 37`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 80`, `duplicate_logic: 15`
* *Architecture:* `api: 26`, `import: 9`
* *Defense:* `safety: 14`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.558
  * `Choke Point (Betweenness):` 0.000102 | `Ripple Effect (Closeness):` 0.044551
  * `Imports (Out-Degree: 1):` typing, functools, contextlib, re, pyparsing.util, warnings, itertools, .warnings...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/tiny/tiny_engine.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.267 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.035 IQR)
- **Top Global Matches:** file_cluster_16: 11.267, file_cluster_8: 11.474, file_cluster_13: 11.64
- **Magnitude:** 241.76 | **LOC:** 417 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.6685%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `eval_expr` (Impact: 33.9)
  * `_apply_op` (Impact: 30.9)
  * `call_function` (Impact: 19.2)
    * *Intent:* # Unary + or - : [op, operand]
  * `assign_var` (Impact: 13.2)
  * `_coerce` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 83`, `args: 30`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 10`, `duplicate_logic: 2`
* *Architecture:* `api: 32`, `import: 4`
* *Defense:* `safety: 27`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015464
  * `Imports (Out-Degree: 1):` .tiny_ast, operator, pyparsing, __future__
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/LAparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.726 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.943 IQR)
- **Top Global Matches:** file_cluster_8: 10.726, file_cluster_17: 10.947, file_cluster_13: 10.975
- **Magnitude:** 228.14 | **LOC:** 577 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.7539%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_assignfunc` (Impact: 85.1)
  * `_addfunc` (Impact: 27.0)
  * `_expfunc` (Impact: 25.1)
    * *Intent:* ## Binary infix operator (BIO) functions. These are called when the stack evaluator ## pops a binary...
  * `_mulfunc` (Impact: 25.0)
  * `_outermulfunc` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 61`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 16`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `io: 15`, `api: 6`, `import: 4`
* *Defense:* `safety: 19`, `doc: 10`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyparsing, re, sys, os, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/tiny/tiny_ast.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.102 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.459 IQR)
- **Top Global Matches:** file_cluster_0: 12.102, file_cluster_16: 12.312, file_cluster_11: 12.395
- **Magnitude:** 222.28 | **LOC:** 474 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.7843%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `from_parsed` (Impact: 11.2)
    * *Intent:* # Prebuilt main-body statements return_type: str = "int" parameters: list[tuple[str, str]] = field(d...
  * `execute` (Impact: 10.9)
  * `from_parsed` (Impact: 10.9)
  * `from_parsed` (Impact: 10.8)
    * *Intent:* """Node representing a function declaration/definition. This node accepts parser groups tagged with ...
  * `from_parsed` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 90`, `args: 29`, `func_start: 29`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 27`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 25`
* *Architecture:* `api: 39`, `import: 5`
* *Defense:* `safety: 19`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.439
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020619
  * `Imports (Out-Degree: 0):` typing, pyparsing, abc, dataclasses, __future__
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/pyparsing/helpers.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.035 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.812 IQR)
- **Top Global Matches:** file_cluster_8: 11.035, file_cluster_16: 11.059, file_cluster_13: 11.192
- **Magnitude:** 201.52 | **LOC:** 1221 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.9543%), Tech Debt (28.993%)
**Top Internal Functions/Classes:**
  * `indentedBlock` (Impact: 36.7)
  * `_makeTags` (Impact: 12.8)
  * `checkUnindent` (Impact: 10.4)
  * `match_previous_literal` (Impact: 9.1)
  * `copy_token_to_repeater` (Impact: 8.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 77`, `args: 44`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 20`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 28`, `import: 8`
* *Defense:* `safety: 18`, `doc: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.462
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.015464
  * `Imports (Out-Degree: 2):` operator, typing, , .core, re, sys, .util, html.entities
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/delta_time.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.629 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.569 IQR)
- **Top Global Matches:** file_cluster_8: 8.629, file_cluster_16: 8.985, file_cluster_0: 9.089
- **Magnitude:** 198.26 | **LOC:** 596 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3776%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_all_tests` (Impact: 38.5)
    * *Intent:* # - show an example of using one of the results fields in Python print("Computed time:", result.comp...
  * `make_weekday_time_references` (Impact: 20.3)
  * `_convert_abs_day_reference_to_date` (Impact: 19.5)
  * `_compute_timestamp` (Impact: 15.4)
    * *Intent:* # accumulate values from parsed time and day subexpressions - fill in defaults for omitted parts now...
  * `_remove_temp_keys` (Impact: 6.8)
    * *Intent:* # strip out keys that are just used internally all_keys = list(t.keys()) for k in all_keys: if k not...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 62`, `args: 24`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `dead_code: 2`
* *Architecture:* `api: 20`, `import: 6`
* *Defense:* `safety: 1`, `doc: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005155
  * `Imports (Out-Degree: 0):` typing, pyparsing, contextlib, itertools, calendar, datetime
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/statemachine/statemachine.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.851 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.783 IQR)
- **Top Global Matches:** file_cluster_13: 11.851, file_cluster_0: 12.004, file_cluster_11: 12.076
- **Magnitude:** 197.0 | **LOC:** 373 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.2812%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expand_state_definition` (Impact: 54.0)
    * *Intent:* """ Parse action to convert statemachine to corresponding Python classes and methods """
  * `load_module` (Impact: 7.7)
  * `find_module` (Impact: 6.3)
    * *Intent:* # if the value in sys.path_importer_cache is None, then this # path *should* be imported by the buil...
  * `checkpath_iter` (Impact: 5.7)
  * `__init__` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 84`, `args: 32`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 58`, `dead_code: 3`, `duplicate_logic: 7`
* *Architecture:* `io: 10`, `api: 15`, `import: 9`
* *Defense:* `safety: 8`, `doc: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.275
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025773
  * `Imports (Out-Degree: 0):` imputil, pyparsing, statemachine, importlib, urllib.parse, sys, os, keyword...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyparsing-3.3.2/examples/lox_parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.09 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.729 IQR)
- **Top Global Matches:** file_cluster_8: 8.09, file_cluster_7: 8.596, file_cluster_1: 8.801
- **Magnitude:** 195.98 | **LOC:** 239 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5454%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 8`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 1`, `doc: 24`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` textwrap, pyparsing, contextlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/lua_parser_diagram.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.805 IQR)
- **Top Global Matches:** file_cluster_8: 7.805, file_cluster_0: 8.378, file_cluster_7: 8.865
- **Magnitude:** 188.48 | **LOC:** 4364 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 363`, `args: 333`, `class_start: 91`
* *Risk/State:* None
* *Architecture:* `io: 428`, `api: 90`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/dest/inv_regex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.078 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.676 IQR)
- **Top Global Matches:** file_cluster_8: 9.078, file_cluster_7: 9.349, file_cluster_13: 9.701
- **Magnitude:** 187.98 | **LOC:** 349 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.8379%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `handle_macro` (Impact: 14.9)
  * `handle_repetition` (Impact: 14.8)
  * `make_generator` (Impact: 11.1)
  * `group_gen` (Impact: 10.9)
  * `handle_literal` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 81`, `args: 33`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `state_mutation: 10`, `duplicate_logic: 15`
* *Architecture:* `api: 31`, `import: 1`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyparsing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/inv_regex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.078 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.676 IQR)
- **Top Global Matches:** file_cluster_8: 9.078, file_cluster_7: 9.349, file_cluster_13: 9.701
- **Magnitude:** 187.98 | **LOC:** 349 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.8379%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_macro` (Impact: 14.9)
  * `handle_repetition` (Impact: 14.8)
  * `make_generator` (Impact: 11.1)
  * `group_gen` (Impact: 10.9)
  * `handle_literal` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 81`, `args: 33`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `state_mutation: 10`, `duplicate_logic: 15`
* *Architecture:* `api: 31`, `import: 1`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyparsing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/regex_inverter/inv_regex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.078 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.676 IQR)
- **Top Global Matches:** file_cluster_8: 9.078, file_cluster_7: 9.349, file_cluster_13: 9.701
- **Magnitude:** 187.98 | **LOC:** 349 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.8379%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_macro` (Impact: 14.9)
  * `handle_repetition` (Impact: 14.8)
  * `make_generator` (Impact: 11.1)
  * `group_gen` (Impact: 10.9)
  * `handle_literal` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 81`, `args: 33`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `state_mutation: 10`, `duplicate_logic: 15`
* *Architecture:* `api: 31`, `import: 1`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyparsing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/pyparsing/diagram/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.113 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.461 IQR)
- **Top Global Matches:** file_cluster_13: 11.113, file_cluster_16: 11.147, file_cluster_8: 11.159
- **Magnitude:** 184.4 | **LOC:** 762 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.3528%), Tech Debt (11.2524%)
**Top Internal Functions/Classes:**
  * `_collapse_verbose_regex` (Impact: 99.0)
  * `_apply_diagram_item_enhancements` (Impact: 12.5)
    * *Intent:* # Just because this is marked for extraction doesn't mean we can do it yet. We may have to wait for ...
  * `_make_bookmark` (Impact: 7.0)
  * `_visible_exprs` (Impact: 6.5)
  * `_worth_extracting` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 91`, `args: 28`, `func_start: 27`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 27`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 16`, `import: 11`
* *Defense:* `safety: 25`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyparsing, typing, io, re, dataclasses, railroad, itertools, jinja2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/examples/decaf_parser_diagram.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.896 IQR)
- **Top Global Matches:** file_cluster_8: 7.896, file_cluster_0: 8.413, file_cluster_7: 8.945
- **Magnitude:** 181.68 | **LOC:** 4264 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 343`, `args: 265`, `class_start: 86`
* *Risk/State:* None
* *Architecture:* `io: 510`, `api: 85`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyparsing-3.3.2/tests/perf_pyparsing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.17 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.683 IQR)
- **Top Global Matches:** file_cluster_13: 10.17, file_cluster_8: 10.204, file_cluster_17: 10.542
- **Magnitude:** 176.66 | **LOC:** 361 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9721%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 31.2)
    * *Intent:* # ---------- Main suite ----------
  * `gen_expr_sequence` (Impact: 23.6)
  * `gen_csv` (Impact: 12.8)
    * *Intent:* # ---------- Corpora generators ----------
  * `bench_matchfirst_vs_or` (Impact: 11.2)
  * `bench_expr_parse` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 69`, `args: 34`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 15`, `duplicate_logic: 4`
* *Architecture:* `io: 8`, `api: 27`, `import: 13`
* *Defense:* `safety: 7`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` littletable, typing, pyparsing, io, random, statistics, contextlib, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pyparsing-3.3.2/examples/tiny/tiny_ast.py` (PYTHON) | Magnitude: 222.28 | Delta: **0.21 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 210, structural_boundaries: 90, branch: 52, generics: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pyparsing-3.3.2/examples/TAP.py` (PYTHON) | Magnitude: 123.0 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 109, state_mutation: 79, branch: 31, planned_debt: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pyparsing-3.3.2/examples/tiny/tests/test_tiny_grammar.py` (PYTHON) | Magnitude: 12.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, doc: 4, debug_prints: 4
- `pyparsing-3.3.2/pyparsing/diagram/__init__.py` (PYTHON) | Magnitude: 184.4 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 421, branch: 117, structural_boundaries: 91, doc: 60
- `pyparsing-3.3.2/tests/perf_pyparsing.py` (PYTHON) | Magnitude: 176.66 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 219, structural_boundaries: 69, branch: 44, args: 34
- `pyparsing-3.3.2/examples/antlr_grammar_tests.py` (PYTHON) | Magnitude: 23.08 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, doc: 16, structural_boundaries: 11, api: 8
- `pyparsing-3.3.2/examples/tiny/tests/test_tiny.py` (PYTHON) | Magnitude: 19.42 | Delta: **0.139 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 30, indent_spaces: 29, test: 21, safety: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pyparsing-3.3.2/pyparsing/results.py` (PYTHON) | Magnitude: 440.36 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 394, encapsulation: 163, structural_boundaries: 127, branch: 124
- `pyparsing-3.3.2/examples/tiny/tests/test_tiny_ast_nodes.py` (PYTHON) | Magnitude: 75.74 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 72, test: 68, doc: 40
- `pyparsing-3.3.2/pyparsing/actions.py` (PYTHON) | Magnitude: 75.22 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 34, doc: 18, generics: 16
- `pyparsing-3.3.2/pyparsing/core.py` (PYTHON) | Magnitude: 1200.44 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3395, branch: 1031, state_mutation: 908, structural_boundaries: 775
- `pyparsing-3.3.2/examples/tiny/tiny_engine.py` (PYTHON) | Magnitude: 241.76 | Delta: **0.207 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 244, structural_boundaries: 83, encapsulation: 80, branch: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pyparsing-3.3.2/pyparsing/warnings.py` (PYTHON) | Magnitude: 14.56 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 3, class_start: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pyparsing-3.3.2/tests/test_diagram.py` (PYTHON) | Magnitude: 82.74 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 75, test: 36, safety: 28
- `pyparsing-3.3.2/pyparsing/helpers.py` (PYTHON) | Magnitude: 201.52 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 472, branch: 122, structural_boundaries: 77, doc: 55
- `pyparsing-3.3.2/examples/bf.py` (PYTHON) | Magnitude: 85.08 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 34, api: 26, args: 20
- `pyparsing-3.3.2/examples/one_to_ninety_nine.py` (PYTHON) | Magnitude: 5.52 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 6, doc: 4, args: 3
- `pyparsing-3.3.2/examples/statemachine/vending_machine.py` (PYTHON) | Magnitude: 53.08 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, state_mutation: 21, encapsulation: 14, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pyparsing-3.3.2/examples/macro_expander.py` (PYTHON) | Magnitude: 4.22 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 6, dead_code: 6, indent_spaces: 5, fragile_debt: 4
- `pyparsing-3.3.2/examples/SimpleCalc.py` (PYTHON) | Magnitude: 16.0 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 41, branch: 18, dead_code: 14, debug_prints: 14

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pyparsing-3.3.2/pyparsing/core.py` -> **Severity: 0.065** (Bridge: 0.0007 * Flux: 99.9625%)
- `pyparsing-3.3.2/pyparsing/util.py` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 99.9772%)
- `pyparsing-3.3.2/pyparsing/actions.py` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 99.6275%)
- `pyparsing-3.3.2/pyparsing/exceptions.py` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.6404%)
- `pyparsing-3.3.2/pyparsing/helpers.py` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 29.86%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyparsing-3.3.2/pyparsing/util.py` -> **Severity: 3.535** (Embedded: 0.0446 * Error Risk: 79.3516%)
- `pyparsing-3.3.2/pyparsing/core.py` -> **Severity: 2.061** (Embedded: 0.0316 * Error Risk: 65.2906%)
- `pyparsing-3.3.2/pyparsing/actions.py` -> **Severity: 2.059** (Embedded: 0.023 * Error Risk: 89.6805%)
- `pyparsing-3.3.2/examples/statemachine/statemachine.py` -> **Severity: 2.049** (Embedded: 0.0258 * Error Risk: 79.5109%)
- `pyparsing-3.3.2/pyparsing/exceptions.py` -> **Severity: 1.583** (Embedded: 0.023 * Error Risk: 68.9402%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyparsing-3.3.2/pyparsing/util.py` -> **Severity: 1295.003** (Blast Radius: 27.558 * Doc Risk: 46.9919%)
- `pyparsing-3.3.2/pyparsing/warnings.py` -> **Severity: 785.856** (Blast Radius: 42.954 * Doc Risk: 18.2953%)
- `pyparsing-3.3.2/pyparsing/unicode.py` -> **Severity: 507.528** (Blast Radius: 7.923 * Doc Risk: 64.0576%)
- `pyparsing-3.3.2/pyparsing/exceptions.py` -> **Severity: 299.747** (Blast Radius: 8.124 * Doc Risk: 36.8965%)
- `pyparsing-3.3.2/dest/inv_regex.py` -> **Severity: 282.468** (Blast Radius: 4.243 * Doc Risk: 66.5728%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
