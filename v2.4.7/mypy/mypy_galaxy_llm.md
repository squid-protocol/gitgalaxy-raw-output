# ARCHITECTURAL_BRIEF: mypy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/mypy` |
| **Timestamp** | `2026-08-07T04:00:33.111264+00:00` |
| **Scan Duration** | `2.35s` |
| **Git Branch** | `master` |
| **Git Commit** | `d7e3268ddd200ff390989d7359dd1e1b42bb94df` |
| **Git Remote** | `https://github.com/python/mypy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 242 malicious artifacts.

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
| Total Artifacts | 1866 |
| Analyzed Artifacts (Scanned) | 266 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1600 |
| Total LOC | 87815 |
| Volatility Index | 0.011 |
| % Scanned of codebase = | 14.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4292 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2026 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 18.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8716 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 225 | 84062 | 84.6% |
| PLAINTEXT | 12 | 0 | 4.5% |
| CPP | 11 | 3554 | 4.1% |
| MARKDOWN | 7 | 0 | 2.6% |
| SHELL | 3 | 14 | 1.1% |
| XML | 3 | 0 | 1.1% |
| YAML | 1 | 75 | 0.4% |
| DOCKERFILE | 1 | 8 | 0.4% |
| CSS | 1 | 70 | 0.4% |
| MAKEFILE | 1 | 8 | 0.4% |
| BATCH | 1 | 24 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.384`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 89 | 33.5% |
| file_cluster_8 | 84 | 31.6% |
| file_cluster_16 | 63 | 23.7% |
| file_cluster_11 | 6 | 2.3% |
| file_cluster_0 | 3 | 1.1% |
| file_cluster_17 | 1 | 0.4% |
| file_cluster_12 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 19 | 7.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1600*

**Composition by Extension & Reason:**
- `.pyi`: 855x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.test`: 261x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 214x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 211 LOC), 1x Excluded (Machine-Generated Source Code Signature: 403 LOC)
- `.c`: 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 22x Excluded (Unsupported Extension: '.rst')
- `.h`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.typed')
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4772 LOC)
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 7x Excluded (Unsupported Extension: '.patch'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pump`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 92.5 | 19.0 | 13.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.5 | 43.8 | 50.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.8 | 13.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 36.7 | 2.7 | 80.0 |
| API Exposure | 0.0 | 17.0 | 5.5 | 5.3 | 0.0 |
| Concurrency Exposure | 0.0 | 52.8 | 0.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 42.5 | 27.3 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.9 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.3 | 1.6 | 1.1 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 13.3 | 6.7 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 51.4 | 41.5 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `mypy/modulefinder.py` (Hits: 81)
- `mypy/report.py` (Hits: 53)
- `mypy/dmypy_server.py` (Hits: 51)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **nodes.py** (`mypy/nodes.py`) — 83 inbound connections
2. **types.py** (`mypy/types.py`) — 78 inbound connections
3. **options.py** (`mypy/options.py`) — 41 inbound connections
4. **ops.py** (`mypyc/ir/ops.py`) — 40 inbound connections
5. **util.py** (`mypy/util.py`) — 33 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **semanal.py** (`mypy/semanal.py`) — 55 outbound dependencies
2. **checker.py** (`mypy/checker.py`) — 50 outbound dependencies
3. **checkexpr.py** (`mypy/checkexpr.py`) — 45 outbound dependencies
4. **gtest.cc** (`mypyc/external/googletest/src/gtest.cc`) — 37 outbound dependencies
5. **stubutil.py** (`mypy/stubutil.py`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `check_enum` (@ `mypy/checker.py`) -> Impact: **3283.8** | LOC: 6302
- `visit_op_expr` (@ `mypy/checkexpr.py`) -> Impact: **1569.2** | LOC: 3255
- `function_fullname` (@ `mypy/semanal.py`) -> Impact: **846.7** | LOC: 1380
- `typeddict_key_must_be_string_literal` (@ `mypy/messages.py`) -> Impact: **759.1** | LOC: 1262
- `__repr__` (@ `mypy/nodes.py`) -> Impact: **548.8** | LOC: 1658
  * *Intent:* # Is this TempNode used to indicate absence of a right hand side in an annotated assignment? # (e.g. for 'x: int' the rvalue is TempNode(AnyType(TypeO...
- `error_message_templates` (@ `mypy/modulefinder.py`) -> Impact: **402.3** | LOC: 840
  * *Intent:* # Stub PyPI package (typically types-pkgname) known to exist but not installed.
- `__repr__` (@ `mypyc/ir/rtypes.py`) -> Impact: **264.0** | LOC: 950
  * *Intent:* # If True, error/undefined value overlaps with a valid value. To # detect an exception, PyErr_Occurred() must be used in addition # to checking for er...
- `get_prefix` (@ `mypy/config_parser.py`) -> Impact: **174.9** | LOC: 311
- `visit_unbound_type_nonoptional` (@ `mypy/typeanal.py`) -> Impact: **167.2** | LOC: 225
  * *Intent:* # We don't need to worry about double-wrapping Optionals or # wrapping Anys: Union simplification will take care of that.
- `visit_instance` (@ `mypy/constraints.py`) -> Impact: **155.7** | LOC: 274
  * *Intent:* # Errors # We can't do anything useful with a partial type here. assert False, "Internal error" # Non-trivial leaf type def visit_type_var(self, templ...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `mypy` | 111 | 43416.36 | 21.6% | 42.75% |
| `mypyc/ir` | 7 | 2745.44 | 32.22% | 46.63% |
| `mypy/plugins` | 11 | 2046.7 | 14.39% | 25.97% |
| `mypy/server` | 10 | 1332.32 | 15.16% | 32.99% |
| `mypyc/analysis` | 6 | 1182.06 | 18.9% | 66.55% |
| `misc` | 20 | 1141.68 | 12.7% | 23.54% |
| `mypyc/transform` | 10 | 791.04 | 23.23% | 78.17% |
| `mypyc` | 12 | 737.38 | 23.33% | 25.56% |
| `mypy/typeshed/stubs/mypy-extensions` | 1 | 371.23 | 11.01% | 0.0% |
| `mypyc/primitives` | 17 | 305.78 | 2.32% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `mypy/erasetype.py` -> **100.0%** Exposure
- `mypy/error_formatter.py` -> **100.0%** Exposure
- `mypy/evalexpr.py` -> **100.0%** Exposure
- `mypy/git.py` -> **100.0%** Exposure
- `mypy/indirection.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `mypy/strconv.py` -> **100.0%** Exposure
- `mypy/stubdoc.py` -> **100.0%** Exposure
- `mypyc/analysis/blockfreq.py` -> **100.0%** Exposure
- `mypyc/options.py` -> **100.0%** Exposure
- `misc/docker/run.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `mypy/types.py` -> **0** Orphaned Functions | **300** Duplicates
- `mypy/nodes.py` -> **0** Orphaned Functions | **225** Duplicates
- `mypy/traverser.py` -> **0** Orphaned Functions | **184** Duplicates
- `mypy/visitor.py` -> **0** Orphaned Functions | **162** Duplicates
- `mypy/type_visitor.py` -> **0** Orphaned Functions | **104** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`misc/diff-cache.py`** -> AI Confidence: **99.31%**
2. **`misc/incremental_checker.py`** -> AI Confidence: **99.31%**
3. **`mypy/argmap.py`** -> AI Confidence: **99.31%**
4. **`mypy/checker.py`** -> AI Confidence: **99.31%**
5. **`mypy/checkexpr.py`** -> AI Confidence: **99.31%**
6. **`mypy/checkmember.py`** -> AI Confidence: **99.31%**
7. **`mypy/checkpattern.py`** -> AI Confidence: **99.31%**
8. **`mypy/checkstrformat.py`** -> AI Confidence: **99.31%**
9. **`mypy/config_parser.py`** -> AI Confidence: **99.31%**
10. **`mypy/constraints.py`** -> AI Confidence: **99.31%**
11. **`mypy/dmypy_server.py`** -> AI Confidence: **99.31%**
12. **`mypy/errors.py`** -> AI Confidence: **99.31%**
13. **`mypy/fastparse.py`** -> AI Confidence: **99.31%**
14. **`mypy/fixup.py`** -> AI Confidence: **99.31%**
15. **`mypy/inspections.py`** -> AI Confidence: **99.31%**
16. **`mypy/ipc.py`** -> AI Confidence: **99.31%**
17. **`mypy/join.py`** -> AI Confidence: **99.31%**
18. **`mypy/main.py`** -> AI Confidence: **99.31%**
19. **`mypy/meet.py`** -> AI Confidence: **99.31%**
20. **`mypy/memprofile.py`** -> AI Confidence: **99.31%**
21. **`mypy/messages.py`** -> AI Confidence: **99.31%**
22. **`mypy/modulefinder.py`** -> AI Confidence: **99.31%**
23. **`mypy/nativeparse.py`** -> AI Confidence: **99.31%**
24. **`mypy/options.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2067` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `mypy/types.py` (PYTHON) -> Cumulative Risk: **645.31**
- **Archetype:** `file_cluster_16` (Distance: 13.155 IQR)
- **Magnitude:** 2544.84 | **LOC:** 4453 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 44.1%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (95.5418%)
- **Heaviest Functions:** `visit_callable_type` (Impact: 88.0), `read_type` (Impact: 38.5), `visit_instance` (Impact: 29.1)

### 2. `mypyc/ir/ops.py` (PYTHON) -> Cumulative Risk: **641.46**
- **Archetype:** `file_cluster_16` (Distance: 13.052 IQR)
- **Magnitude:** 985.04 | **LOC:** 2107 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.8802%)
- **Heaviest Functions:** `__init__` (Impact: 78.0), `__repr__` (Impact: 64.7), `__init__` (Impact: 9.3)

### 3. `mypy/fastparse.py` (PYTHON) -> Cumulative Risk: **631.34**
- **Archetype:** `file_cluster_16` (Distance: 12.608 IQR)
- **Magnitude:** 1209.34 | **LOC:** 2257 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 28.6%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (96.6584%), State Flux (91.5098%)
- **Heaviest Functions:** `fix_function_overloads` (Impact: 87.0), `visit_Call` (Impact: 26.8), `visit_Call` (Impact: 21.6)

### 4. `mypy/nodes.py` (PYTHON) -> Cumulative Risk: **630.56**
- **Archetype:** `file_cluster_16` (Distance: 13.072 IQR)
- **Magnitude:** 2206.36 | **LOC:** 5368 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (97.8503%), Documentation (86.5381%)
- **Heaviest Functions:** `__repr__` (Impact: 548.8), `is_trivial_self` (Impact: 18.2), `deserialize` (Impact: 13.2)

### 5. `mypy/stubdoc.py` (PYTHON) -> Cumulative Risk: **617.69**
- **Archetype:** `file_cluster_13` (Distance: 12.815 IQR)
- **Magnitude:** 540.52 | **LOC:** 546 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.1505%), Documentation (84.7615%)
- **Heaviest Functions:** `add_token` (Impact: 121.5), `parse_signature` (Impact: 21.6), `infer_sig_from_docstring` (Impact: 16.8)

### 6. `mypyc/ir/func_ir.py` (PYTHON) -> Cumulative Risk: **606.23**
- **Archetype:** `file_cluster_16` (Distance: 11.886 IQR)
- **Magnitude:** 321.66 | **LOC:** 485 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.2391%)
- **Heaviest Functions:** `get_text_signature` (Impact: 33.8), `_extract_python_literal` (Impact: 23.0), `all_values` (Impact: 20.4)

### 7. `mypy/semanal_pass1.py` (PYTHON) -> Cumulative Risk: **602.56**
- **Archetype:** `file_cluster_13` (Distance: 11.457 IQR)
- **Magnitude:** 100.26 | **LOC:** 160 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9894%), State Flux (98.69%)
- **Heaviest Functions:** `visit_file` (Impact: 20.8), `visit_func_def` (Impact: 9.5), `visit_if_stmt` (Impact: 7.3)

### 8. `mypyc/analysis/ircheck.py` (PYTHON) -> Cumulative Risk: **595.7**
- **Archetype:** `file_cluster_16` (Distance: 11.74 IQR)
- **Magnitude:** 392.08 | **LOC:** 499 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9956%), Verification (80.0%)
- **Heaviest Functions:** `check_op_sources_valid` (Impact: 29.9), `visit_load_literal` (Impact: 24.1), `check_func_ir` (Impact: 23.5)

### 9. `mypy/strconv.py` (PYTHON) -> Cumulative Risk: **594.04**
- **Archetype:** `file_cluster_16` (Distance: 12.979 IQR)
- **Magnitude:** 803.38 | **LOC:** 708 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.119%)
- **Heaviest Functions:** `visit_mypy_file` (Impact: 138.7), `dump_tagged` (Impact: 21.3), `func_helper` (Impact: 20.5)

### 10. `mypy/type_visitor.py` (PYTHON) -> Cumulative Risk: **591.27**
- **Archetype:** `file_cluster_16` (Distance: 10.937 IQR)
- **Magnitude:** 461.5 | **LOC:** 613 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (83.462%)
- **Heaviest Functions:** `query_types` (Impact: 19.8), `visit_callable_type` (Impact: 10.4), `visit_union_type` (Impact: 8.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `mypy/checker.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.445 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.863 IQR)
- **Top Global Matches:** file_cluster_11: 14.445, file_cluster_16: 14.488, file_cluster_13: 14.552
- **Magnitude:** 5109.28 | **LOC:** 9583 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 46.4%
- **Risk Profile:** Cognitive Load (31.7789%), Tech Debt (21.6474%)
**Top Internal Functions/Classes:**
  * `check_enum` (Impact: 3283.8)
  * `_visit_overloaded_func_def` (Impact: 65.6)
    * *Intent:* # If exit_condition is set, assume it must be False on exit from the loop: if exit_condition: _, els...
  * `visit_class_def` (Impact: 59.5)
  * `check_overlapping_overloads` (Impact: 58.1)
  * `require_correct_self_argument` (Impact: 53.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2371`, `structural_boundaries: 1549`, `args: 346`, `func_start: 341`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 553`, `dead_code: 25`, `planned_debt: 70`, `fragile_debt: 9`, `duplicate_logic: 2`
* *Architecture:* `api: 337`, `concurrency: 2`, `import: 47`
* *Defense:* `safety: 727`, `doc: 334`, `test: 74`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.188
  * `Choke Point (Betweenness):` 0.00666 | `Ripple Effect (Closeness):` 0.038133
  * `Imports (Out-Degree: 40):` mypy.constraints, mypy.literals, mypy.semanal_enum, collections.abc, unfollowed, mypy.expandtype, mypy.patterns, mypy.nodes...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/semanal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.239 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.728 IQR)
- **Top Global Matches:** file_cluster_16: 14.239, file_cluster_11: 14.24, file_cluster_8: 14.263
- **Magnitude:** 3202.86 | **LOC:** 8436 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (33.3921%), Tech Debt (15.387%)
**Top Internal Functions/Classes:**
  * `function_fullname` (Impact: 846.7)
  * `check_and_set_up_type_alias` (Impact: 127.8)
  * `store_final_status` (Impact: 51.4)
    * *Intent:* """Check if s defines a typed dict."""
  * `unwrap_final` (Impact: 51.3)
  * `visit_import_from` (Impact: 48.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2220`, `structural_boundaries: 1422`, `args: 346`, `func_start: 342`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 579`, `dead_code: 19`, `planned_debt: 42`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 350`, `concurrency: 10`, `import: 37`
* *Defense:* `safety: 648`, `doc: 276`, `test: 102`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.802
  * `Choke Point (Betweenness):` 0.002918 | `Ripple Effect (Closeness):` 0.035735
  * `Imports (Out-Degree: 27):` x, over, mypy.exprtotype, mypy.semanal_enum, it, cycles., collections.abc, mypy.patterns...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mypy/checkexpr.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.774 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.726 IQR)
- **Top Global Matches:** file_cluster_16: 13.774, file_cluster_8: 13.805, file_cluster_11: 13.807
- **Magnitude:** 2842.28 | **LOC:** 6998 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 36.8%
- **Risk Profile:** Cognitive Load (21.9869%), Tech Debt (17.6101%)
**Top Internal Functions/Classes:**
  * `visit_op_expr` (Impact: 1569.2)
  * `visit_call_expr_inner` (Impact: 131.5)
  * `analyze_ref_expr` (Impact: 40.2)
  * `combine_function_signatures` (Impact: 31.6)
  * `analyze_type_type_callee` (Impact: 30.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1569`, `structural_boundaries: 1031`, `args: 223`, `func_start: 212`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 297`, `dead_code: 26`, `planned_debt: 36`, `fragile_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 223`, `import: 44`
* *Defense:* `safety: 484`, `doc: 256`, `test: 50`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.436
  * `Choke Point (Betweenness):` 0.001845 | `Ripple Effect (Closeness):` 0.029373
  * `Imports (Out-Degree: 35):` mypy.exprtotype, mypy.literals, mypy.semanal_enum, it, cycles., collections.abc, mypy.expandtype, time...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mypy/types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.155 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.94 IQR)
- **Top Global Matches:** file_cluster_16: 13.155, file_cluster_0: 13.241, file_cluster_11: 13.318
- **Magnitude:** 2544.84 | **LOC:** 4453 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 44.1%
- **Risk Profile:** Cognitive Load (38.8157%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `visit_callable_type` (Impact: 88.0)
  * `read_type` (Impact: 38.5)
  * `visit_instance` (Impact: 29.1)
    * *Intent:* # This can't be everything, but it can be a class reference, # a generic class instance, a union, An...
  * `read` (Impact: 26.6)
  * `with_normalized_var_args` (Impact: 25.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 1132`, `args: 385`, `func_start: 385`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 470`, `dead_code: 4`, `planned_debt: 16`, `fragile_debt: 3`, `duplicate_logic: 300`
* *Architecture:* `io: 1`, `api: 362`, `import: 16`
* *Defense:* `safety: 195`, `doc: 130`, `test: 101`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.712
  * `Choke Point (Betweenness):` 0.023228 | `Ripple Effect (Closeness):` 0.305048
  * `Imports (Out-Degree: 9):` sys, is, mypy.options, mypy.util, typing_extensions, abc, collections.abc, typing...
  * `Imported By (In-Degree: 78):` (Excluded from Brief to save tokens)

### `mypy/nodes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.072 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.895 IQR)
- **Top Global Matches:** file_cluster_16: 13.072, file_cluster_0: 13.136, file_cluster_11: 13.201
- **Magnitude:** 2206.36 | **LOC:** 5368 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (29.6097%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 548.8)
    * *Intent:* # Is this TempNode used to indicate absence of a right hand side in an annotated assignment? # (e.g....
  * `is_trivial_self` (Impact: 18.2)
    * *Intent:* # TODO: figure out how to reliably set end position (we don't know the impl here). self.set_line(ite...
  * `deserialize` (Impact: 13.2)
  * `deserialize` (Impact: 11.9)
  * `serialize` (Impact: 11.6)
    * *Intent:* # the majority). In cases where self is not annotated and there are no Self # in the signature we ca...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 938`, `args: 329`, `func_start: 328`, `class_start: 99`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 615`, `dead_code: 15`, `planned_debt: 25`, `fragile_debt: 4`, `duplicate_logic: 225`
* *Architecture:* `io: 1`, `api: 343`, `import: 17`
* *Defense:* `safety: 126`, `doc: 202`, `test: 76`, `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 53.267
  * `Choke Point (Betweenness):` 0.031307 | `Ripple Effect (Closeness):` 0.341693
  * `Imports (Out-Degree: 9):` replaces, statements., collections.abc, ..., mypy.patterns, mypy.options, os, a.b.c...
  * `Imported By (In-Degree: 83):` (Excluded from Brief to save tokens)

### `mypy/messages.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.019 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.764 IQR)
- **Top Global Matches:** file_cluster_8: 12.019, file_cluster_16: 12.021, file_cluster_13: 12.282
- **Magnitude:** 1398.26 | **LOC:** 3428 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (22.2977%), Tech Debt (8.793%)
**Top Internal Functions/Classes:**
  * `typeddict_key_must_be_string_literal` (Impact: 759.1)
  * `dangerous_comparison` (Impact: 21.1)
  * `requires_int_or_single_byte` (Impact: 14.8)
  * `ignore_last_known_values` (Impact: 12.8)
  * `reveal_locals` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 759`, `structural_boundaries: 624`, `args: 193`, `func_start: 191`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 110`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 244`, `concurrency: 3`, `import: 21`
* *Defense:* `safety: 146`, `doc: 94`, `test: 13`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.125
  * `Choke Point (Betweenness):` 0.01016 | `Ripple Effect (Closeness):` 0.181764
  * `Imports (Out-Degree: 12):` difflib, context., collections.abc, mypy.options, mypy.errorcodes, contextlib, mypy, mypy.subtypes...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `mypy/fastparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.608 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.188 IQR)
- **Top Global Matches:** file_cluster_16: 12.608, file_cluster_8: 12.673, file_cluster_17: 12.721
- **Magnitude:** 1209.34 | **LOC:** 2257 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (36.375%), Tech Debt (96.6584%)
**Top Internal Functions/Classes:**
  * `fix_function_overloads` (Impact: 87.0)
  * `visit_Call` (Impact: 26.8)
  * `visit_Call` (Impact: 21.6)
  * `translate_type_params` (Impact: 20.7)
  * `visit_Constant` (Impact: 20.2)
    * *Intent:* # Call(expr func, expr* args, keyword* keywords) # keyword = (identifier? arg, expr value) def visit...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 404`, `args: 142`, `func_start: 141`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 207`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 27`
* *Architecture:* `io: 8`, `api: 197`, `import: 19`
* *Defense:* `safety: 122`, `doc: 34`, `test: 15`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.076
  * `Choke Point (Betweenness):` 0.000921 | `Ripple Effect (Closeness):` 0.035734
  * `Imports (Out-Degree: 11):` sys, mypy.options, mypy.util, warnings, mypy, mypy.reachability, mypy.sharedparse, collections.abc...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mypy/typeanal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.437 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.712 IQR)
- **Top Global Matches:** file_cluster_8: 12.437, file_cluster_16: 12.486, file_cluster_11: 12.591
- **Magnitude:** 1164.54 | **LOC:** 2804 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 27.8%
- **Risk Profile:** Cognitive Load (35.0373%), Tech Debt (89.1499%)
**Top Internal Functions/Classes:**
  * `visit_unbound_type_nonoptional` (Impact: 167.2)
    * *Intent:* # We don't need to worry about double-wrapping Optionals or # wrapping Anys: Union simplification wi...
  * `try_analyze_special_unbound_type` (Impact: 144.8)
  * `validate_instance` (Impact: 61.6)
  * `analyze_literal_param` (Impact: 48.9)
  * `check_and_warn_deprecated` (Impact: 30.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 637`, `structural_boundaries: 609`, `args: 128`, `func_start: 127`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 205`, `dead_code: 2`, `planned_debt: 24`, `fragile_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `api: 134`, `import: 20`
* *Defense:* `safety: 166`, `doc: 50`, `test: 30`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 0.000517 | `Ripple Effect (Closeness):` 0.037781
  * `Imports (Out-Degree: 15):` collections.abc, mypy.expandtype, mypy.tvar_scope, was, mypy.messages, mypy.options, mypy.errorcodes, contextlib...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/traverser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.037 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.89 IQR)
- **Top Global Matches:** file_cluster_16: 10.037, file_cluster_8: 10.261, file_cluster_13: 10.789
- **Magnitude:** 993.88 | **LOC:** 1106 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (11.3394%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `visit_try_stmt` (Impact: 14.7)
  * `visit_class_def` (Impact: 12.6)
  * `visit_func` (Impact: 10.6)
    * *Intent:* # Visit methods
  * `visit_template_str_expr` (Impact: 10.4)
  * `visit_if_stmt` (Impact: 8.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 340`, `args: 198`, `func_start: 198`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 30`, `planned_debt: 1`, `duplicate_logic: 184`
* *Architecture:* `api: 210`, `import: 5`
* *Defense:* `safety: 3`, `doc: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.749
  * `Choke Point (Betweenness):` 0.000311 | `Ripple Effect (Closeness):` 0.085763
  * `Imports (Out-Degree: 4):` mypy_extensions, mypy.visitor, mypy.patterns, mypy.nodes, __future__
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `mypy/constraints.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.375 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.208 IQR)
- **Top Global Matches:** file_cluster_11: 13.375, file_cluster_16: 13.403, file_cluster_13: 13.473
- **Magnitude:** 985.16 | **LOC:** 1688 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (53.8571%), Tech Debt (46.7316%)
**Top Internal Functions/Classes:**
  * `visit_instance` (Impact: 155.7)
    * *Intent:* # Errors # We can't do anything useful with a partial type here. assert False, "Internal error" # No...
  * `visit_callable_type` (Impact: 77.3)
  * `visit_tuple_type` (Impact: 51.8)
  * `any_constraints` (Impact: 46.5)
  * `filter_imprecise_kinds` (Impact: 23.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 321`, `args: 54`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 261`, `dead_code: 2`, `planned_debt: 15`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 72`, `import: 13`
* *Defense:* `safety: 170`, `doc: 48`, `test: 39`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.59
  * `Choke Point (Betweenness):` 0.002277 | `Ripple Effect (Closeness):` 0.147604
  * `Imports (Out-Degree: 10):` mypy.nodes, mypy.typestate, mypy.subtypes, mypy.maptype, mypy.erasetype, collections.abc, typing, mypy.types...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `mypyc/ir/ops.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.052 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.079 IQR)
- **Top Global Matches:** file_cluster_16: 13.052, file_cluster_0: 13.197, file_cluster_13: 13.498
- **Magnitude:** 985.04 | **LOC:** 2107 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (30.9501%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 78.0)
  * `__repr__` (Impact: 64.7)
  * `__init__` (Impact: 9.3)
  * `__init__` (Impact: 5.6)
  * `unique_sources` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 575`, `args: 250`, `func_start: 250`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 297`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 81`
* *Architecture:* `api: 254`, `import: 11`
* *Defense:* `safety: 52`, `doc: 122`, `test: 35`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.899
  * `Choke Point (Betweenness):` 0.018058 | `Ripple Effect (Closeness):` 0.201999
  * `Imports (Out-Degree: 6):` mypy_extensions, mypyc.common, mypyc.ir.rtypes, mypyc.codegen.literals, abc, collections.abc, typing, mypyc.ir.func_ir...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `mypy/subtypes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.471 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.825 IQR)
- **Top Global Matches:** file_cluster_8: 11.471, file_cluster_13: 11.648, file_cluster_16: 11.683
- **Magnitude:** 977.02 | **LOC:** 2319 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (34.3905%), Tech Debt (40.0105%)
**Top Internal Functions/Classes:**
  * `visit_instance` (Impact: 124.4)
    * *Intent:* # None is compatible with Hashable (and other similar protocols). This is # None is also compatible ...
  * `visit_callable_type` (Impact: 58.5)
  * `visit_overloaded` (Impact: 52.6)
    * *Intent:* # Non-required key is not compatible with a required key since # indexing may fail unexpectedly if a...
  * `variadic_tuple_subtype` (Impact: 49.9)
  * `get_member_flags` (Impact: 48.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 633`, `structural_boundaries: 522`, `args: 64`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 37`, `dead_code: 7`, `planned_debt: 21`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 82`, `import: 21`
* *Defense:* `safety: 156`, `doc: 40`, `test: 33`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.028
  * `Choke Point (Betweenness):` 0.026523 | `Ripple Effect (Closeness):` 0.187262
  * `Imports (Out-Degree: 16):` mypy.constraints, collections.abc, mypy.expandtype, mypy.solve, mypy.applytype, mypy.options, contextlib, mypy.maptype...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `mypy/strconv.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.979 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.124 IQR)
- **Top Global Matches:** file_cluster_16: 12.979, file_cluster_13: 13.119, file_cluster_11: 13.277
- **Magnitude:** 803.38 | **LOC:** 708 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (76.841%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `visit_mypy_file` (Impact: 138.7)
  * `dump_tagged` (Impact: 21.3)
  * `func_helper` (Impact: 20.5)
  * `visit_call_expr` (Impact: 14.8)
  * `visit_template_str_expr` (Impact: 11.3)
    * *Intent:* # REVEAL_LOCALS
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 238`, `args: 98`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 267`
* *Architecture:* `io: 3`, `api: 148`, `import: 16`
* *Defense:* `safety: 9`, `doc: 12`, `test: 2`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.222029
  * `Imports (Out-Degree: 6):` mypy.options, mypy.util, os, mypy.visitor, collections.abc, typing, mypy.types, re...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/nativeparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.479 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.398 IQR)
- **Top Global Matches:** file_cluster_8: 11.479, file_cluster_16: 11.828, file_cluster_13: 11.838
- **Magnitude:** 736.76 | **LOC:** 2095 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (20.0967%), Tech Debt (8.6846%)
**Top Internal Functions/Classes:**
  * `read_statement` (Impact: 116.5)
  * `read_type` (Impact: 81.6)
  * `read_pattern` (Impact: 48.5)
    * *Intent:* # Process keyword arguments for kw_name, kw_value in kwargs: if kw_name == "name": # MULTIPLE_VALUES...
  * `read_call_type` (Impact: 40.0)
  * `read_func_def` (Impact: 37.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 221`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 192`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 39`, `import: 15`
* *Defense:* `safety: 53`, `doc: 38`, `test: 21`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.496
  * `Choke Point (Betweenness):` 0.000175 | `Ripple Effect (Closeness):` 0.019211
  * `Imports (Out-Degree: 10):` mypy.options, mypy.util, mypy, os, mypy.reachability, mypy.sharedparse, ast_serialize, dependencies...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/join.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 12.691 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.034 IQR)
- **Top Global Matches:** file_cluster_11: 12.691, file_cluster_13: 12.765, file_cluster_16: 12.837
- **Magnitude:** 721.8 | **LOC:** 917 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (31.8618%), Tech Debt (75.7011%)
**Top Internal Functions/Classes:**
  * `join_tuples` (Impact: 71.1)
  * `join_instances` (Impact: 62.8)
  * `visit_instance` (Impact: 34.6)
  * `visit_callable_type` (Impact: 33.0)
  * `join_instances_via_supertype` (Impact: 31.9)
    * *Intent:* # join(int, float) == float, for example. for p in t.type._promote: if is_subtype(p, s): return join...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 280`, `args: 46`, `func_start: 46`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 87`, `dead_code: 2`, `planned_debt: 11`, `duplicate_logic: 4`
* *Architecture:* `api: 67`, `import: 12`
* *Defense:* `safety: 110`, `doc: 16`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.996
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.124399
  * `Imports (Out-Degree: 8):` mypy.subtypes, mypy.maptype, collections.abc, typing, mypy.state, mypy.types, mypy.expandtype, mypy.typeops...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `mypy/meet.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.635 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.853 IQR)
- **Top Global Matches:** file_cluster_8: 12.635, file_cluster_11: 12.679, file_cluster_13: 12.687
- **Magnitude:** 718.9 | **LOC:** 1276 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (21.8292%), Tech Debt (16.0124%)
**Top Internal Functions/Classes:**
  * `narrow_declared_type` (Impact: 84.3)
  * `visit_instance` (Impact: 64.8)
  * `meet_tuples` (Impact: 47.5)
    * *Intent:* # TODO: Implement a better algorithm that covers at least the same cases # as TypeJoinVisitor.visit_...
  * `meet_types` (Impact: 36.7)
  * `visit_callable_type` (Impact: 29.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 368`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 50`, `dead_code: 3`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `api: 69`, `import: 11`
* *Defense:* `safety: 187`, `doc: 32`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.037
  * `Choke Point (Betweenness):` 0.001465 | `Ripple Effect (Closeness):` 0.151864
  * `Imports (Out-Degree: 8):` mypy, mypy.subtypes, mypy.maptype, mypy.erasetype, collections.abc, mypy.state, mypy.types, mypy.join...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `mypy/suggestions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.794 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.916 IQR)
- **Top Global Matches:** file_cluster_13: 12.794, file_cluster_16: 12.826, file_cluster_11: 12.878
- **Magnitude:** 705.8 | **LOC:** 1069 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.4897%), Tech Debt (91.8864%)
**Top Internal Functions/Classes:**
  * `refine_type` (Impact: 30.9)
    * *Intent:* # Note: for default arguments, we just assume that they # are required. This isn't right, but neithe...
  * `extract_from_decorator` (Impact: 29.2)
  * `visit_instance` (Impact: 27.5)
  * `score_type` (Impact: 26.9)
  * `find_node` (Impact: 26.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 241`, `args: 66`, `func_start: 64`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 91`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 3`, `api: 80`, `import: 25`
* *Defense:* `safety: 59`, `doc: 74`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.389
  * `Choke Point (Betweenness):` 0.001015 | `Ripple Effect (Closeness):` 0.006709
  * `Imports (Out-Degree: 16):` mypy.build, mypy.join, mypy.modulefinder, collections.abc, mypy.meet, mypy.options, contextlib, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/typeops.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.928 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.335 IQR)
- **Top Global Matches:** file_cluster_13: 12.928, file_cluster_11: 12.952, file_cluster_17: 12.969
- **Magnitude:** 690.14 | **LOC:** 1345 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 47.1%
- **Risk Profile:** Cognitive Load (13.8501%), Tech Debt (13.671%)
**Top Internal Functions/Classes:**
  * `false_only` (Impact: 50.1)
    * *Intent:* # If deleted subtypes had more general truthiness, use that
  * `type_object_type` (Impact: 46.2)
  * `_remove_redundant_union_items` (Impact: 45.4)
  * `custom_special_method` (Impact: 33.4)
    * *Intent:* # Non-empty enums cannot subclass each other so simply removing duplicates is enough. items = [ try_...
  * `is_singleton_identity_type` (Impact: 28.9)
    * *Intent:* """If the given expression or type corresponds to a string literal or a union of string literals, re...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 306`, `args: 52`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 33`, `dead_code: 9`, `planned_debt: 10`
* *Architecture:* `api: 68`, `import: 18`
* *Defense:* `safety: 114`, `doc: 62`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.99
  * `Choke Point (Betweenness):` 0.014847 | `Ripple Effect (Closeness):` 0.193459
  * `Imports (Out-Degree: 12):` mypy.checker_state, mypy.copytype, mypy.subtypes, mypy.maptype, collections.abc, typing, mypy.state, mypy.types...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `mypyc/ir/rtypes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.027 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.992 IQR)
- **Top Global Matches:** file_cluster_0: 13.027, file_cluster_16: 13.035, file_cluster_11: 13.203
- **Magnitude:** 654.18 | **LOC:** 1445 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 64.3%
- **Risk Profile:** Cognitive Load (38.1377%), Tech Debt (99.9685%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 264.0)
    * *Intent:* # If True, error/undefined value overlaps with a valid value. To # detect an exception, PyErr_Occurr...
  * `flatten_nested_unions` (Impact: 12.6)
  * `optional_value_type` (Impact: 10.4)
  * `make_simplified_union` (Impact: 6.5)
  * `check_native_int_range` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 335`, `args: 136`, `func_start: 136`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 162`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 25`
* *Architecture:* `api: 113`, `import: 8`
* *Defense:* `safety: 106`, `doc: 42`, `test: 18`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.435
  * `Choke Point (Betweenness):` 0.007949 | `Ripple Effect (Closeness):` 0.199321
  * `Imports (Out-Degree: 3):` mypyc.ir.ops, mypyc.common, abc, mypyc.namegen, typing, __future__, mypyc.ir.class_ir, mypyc.ir.deps
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `mypy/modulefinder.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 11.92 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.342 IQR)
- **Top Global Matches:** file_cluster_11: 11.92, file_cluster_13: 11.927, file_cluster_16: 12.022
- **Magnitude:** 593.16 | **LOC:** 1003 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (39.7222%), Tech Debt (40.4106%)
**Top Internal Functions/Classes:**
  * `error_message_templates` (Impact: 402.3)
    * *Intent:* # Stub PyPI package (typically types-pkgname) known to exist but not installed.
  * `load_stdlib_py_versions` (Impact: 20.9)
    * *Intent:* # If provided, insert the caller-supplied extra module path to the # beginning (highest priority) of...
  * `typeshed_py_version` (Impact: 2.3)
  * `asdict` (Impact: 2.1)
    * *Intent:* # paths in typeshed
  * `__init__` (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 150`, `args: 32`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 122`, `dead_code: 2`, `planned_debt: 15`, `fragile_debt: 4`
* *Architecture:* `io: 81`, `api: 29`, `import: 19`
* *Defense:* `safety: 17`, `doc: 34`, `test: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.637
  * `Choke Point (Betweenness):` 0.004697 | `Ripple Effect (Closeness):` 0.038593
  * `Imports (Out-Degree: 8):` mypy.fscache, mypy.options, mypy, os, of, mypy.errors, pathspec.patterns.gitignore, subprocess...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `mypy/stubgenc.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 12.008 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.762 IQR)
- **Top Global Matches:** file_cluster_11: 12.008, file_cluster_16: 12.132, file_cluster_13: 12.145
- **Magnitude:** 555.0 | **LOC:** 1047 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (51.2583%), Tech Debt (96.1042%)
**Top Internal Functions/Classes:**
  * `generate_module` (Impact: 73.1)
    * *Intent:* """Strips unnecessary module names from typ. If typ represents a type that is inside module or is a ...
  * `get_default_function_sig` (Impact: 69.3)
    * *Intent:* # Add additional implicit imports. # C-extensions are given more latitude since they do not import t...
  * `_indent_docstring` (Impact: 18.2)
  * `get_type_annotation` (Impact: 12.8)
  * `get_property_type` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 190`, `args: 49`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 149`, `dead_code: 4`, `planned_debt: 11`, `fragile_debt: 1`, `duplicate_logic: 7`, `orphaned_logic: 6`
* *Architecture:* `io: 6`, `api: 42`, `import: 16`
* *Defense:* `safety: 28`, `doc: 42`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` enum, the, mypy.fastparse, mypy.stubutil, glob, keyword, types, mypy.moduleinspect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mypy/stubdoc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.815 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.691 IQR)
- **Top Global Matches:** file_cluster_13: 12.815, file_cluster_16: 12.824, file_cluster_11: 12.867
- **Magnitude:** 540.52 | **LOC:** 546 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.9837%), Tech Debt (68.1542%)
**Top Internal Functions/Classes:**
  * `add_token` (Impact: 121.5)
  * `parse_signature` (Impact: 21.6)
  * `infer_sig_from_docstring` (Impact: 16.8)
  * `parse_all_signatures` (Impact: 14.9)
    * *Intent:* # Ad-hoc fixes. sig = sig.replace("(self)", "") return sig def parse_all_signatures(lines: Sequence[...
  * `has_catchall_args` (Impact: 14.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 107`, `args: 27`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 198`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 35`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 4`, `doc: 36`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.684
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.007547
  * `Imports (Out-Degree: 1):` tokenize, keyword, mypy.util, collections.abc, typing, re, io, contextlib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mypy/errors.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.093 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.897 IQR)
- **Top Global Matches:** file_cluster_16: 12.093, file_cluster_13: 12.241, file_cluster_8: 12.344
- **Magnitude:** 539.9 | **LOC:** 1472 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (21.0794%), Tech Debt (14.6655%)
**Top Internal Functions/Classes:**
  * `render_messages` (Impact: 47.2)
    * *Intent:* # If shadow file mapping is not found, read source lines mapped_path = self.find_shadow_file_mapping...
  * `generate_unused_ignore_errors` (Impact: 33.5)
  * `is_ignored_error` (Impact: 23.3)
  * `sort_within_context` (Impact: 15.0)
  * `clear_errors_in_targets` (Impact: 14.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 234`, `args: 70`, `func_start: 66`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 206`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `io: 10`, `api: 70`, `import: 21`
* *Defense:* `safety: 13`, `doc: 80`, `test: 8`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.769
  * `Choke Point (Betweenness):` 0.00955 | `Ripple Effect (Closeness):` 0.16191
  * `Imports (Out-Degree: 11):` context., collections.abc, pdb, mypy.options, mypy.errorcodes, mypy, os.path, mypy.cache...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `mypy/treetransform.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.996 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.799 IQR)
- **Top Global Matches:** file_cluster_16: 9.996, file_cluster_8: 10.13, file_cluster_13: 10.522
- **Magnitude:** 539.56 | **LOC:** 821 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (9.9497%), Tech Debt (52.6634%)
**Top Internal Functions/Classes:**
  * `visit_func_def` (Impact: 10.8)
  * `copy_ref` (Impact: 10.8)
  * `visit_index_expr` (Impact: 9.2)
  * `duplicate_generator` (Impact: 9.1)
  * `visit_mapping_pattern` (Impact: 9.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 280`, `args: 108`, `func_start: 108`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 14`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 186`, `import: 9`
* *Defense:* `safety: 21`, `doc: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.362
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028762
  * `Imports (Out-Degree: 6):` mypy.util, mypy.visitor, collections.abc, typing, mypy.traverser, mypy.types, mypy.patterns, mypy.nodes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/visitor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.656 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.98 IQR)
- **Top Global Matches:** file_cluster_16: 9.656, file_cluster_0: 9.901, file_cluster_8: 10.194
- **Magnitude:** 531.26 | **LOC:** 640 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (4.487%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `visit_int_expr` (Impact: 2.1)
  * `visit_str_expr` (Impact: 2.1)
  * `visit_bytes_expr` (Impact: 2.1)
  * `visit_float_expr` (Impact: 2.1)
  * `visit_complex_expr` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 261`, `args: 166`, `func_start: 166`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 81`, `planned_debt: 1`, `duplicate_logic: 162`
* *Architecture:* `api: 174`, `import: 6`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.006
  * `Choke Point (Betweenness):` 0.000196 | `Ripple Effect (Closeness):` 0.242492
  * `Imports (Out-Degree: 3):` mypy_extensions, cycle, abc, typing, mypy.patterns, mypy.nodes, __future__
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `mypy/expandtype.py` (PYTHON) | Magnitude: 421.28 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 417, structural_boundaries: 194, branch: 125, generics: 70
- `mypyc/ir/rtypes.py` (PYTHON) | Magnitude: 654.18 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 732, structural_boundaries: 335, state_mutation: 162, generics: 155
- `mypy/semanal_shared.py` (PYTHON) | Magnitude: 235.04 | Delta: **0.239 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 288, structural_boundaries: 96, api: 76, generics: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `misc/analyze_cache.py` (PYTHON) | Magnitude: 161.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 50, branch: 34, generics: 18
- `mypy/modulefinder.py` (PYTHON) | Magnitude: 593.16 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 615, branch: 214, structural_boundaries: 150, state_mutation: 122
- `mypy/constraints.py` (PYTHON) | Magnitude: 985.16 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1152, branch: 405, structural_boundaries: 321, state_mutation: 261
- `mypy/checker.py` (PYTHON) | Magnitude: 5109.28 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 6535, branch: 2371, structural_boundaries: 1549, safety: 727
- `mypy/join.py` (PYTHON) | Magnitude: 721.8 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 623, structural_boundaries: 280, branch: 243, safety: 110

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `misc/docker/run.sh` (SHELL) | Magnitude: 0.97 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 6, structural_boundaries: 3, safety: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `mypyc/external/googletest/src/gtest-typed-test.cc` (CPP) | Magnitude: 0.09 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, state_mutation: 51, branch: 15, immutability_locks: 8
- `mypy/checkpattern.py` (PYTHON) | Magnitude: 471.16 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 640, branch: 188, structural_boundaries: 155, state_mutation: 66
- `mypy/stubdoc.py` (PYTHON) | Magnitude: 540.52 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 359, state_mutation: 198, branch: 145, structural_boundaries: 107
- `mypy/find_sources.py` (PYTHON) | Magnitude: 131.12 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 57, branch: 45, generics: 21
- `mypy/options.py` (PYTHON) | Magnitude: 262.48 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 312, state_mutation: 121, structural_boundaries: 49, generics: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `mypy/semanal.py` (PYTHON) | Magnitude: 3202.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 6147, branch: 2220, structural_boundaries: 1422, safety: 648
- `mypyc/ir/func_ir.py` (PYTHON) | Magnitude: 321.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 330, structural_boundaries: 127, branch: 69, state_mutation: 67
- `mypy/fixup.py` (PYTHON) | Magnitude: 331.92 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 338, branch: 107, structural_boundaries: 93, api: 70
- `mypy/config_parser.py` (PYTHON) | Magnitude: 398.8 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 488, branch: 183, structural_boundaries: 118, state_mutation: 73
- `mypy/checkexpr.py` (PYTHON) | Magnitude: 2842.28 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4998, branch: 1569, structural_boundaries: 1031, safety: 484

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `mypy/solve.py` (PYTHON) | Magnitude: 217.46 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 333, branch: 176, structural_boundaries: 102, state_mutation: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `mypy/messages.py` (PYTHON) | Magnitude: 1398.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 2714, branch: 759, structural_boundaries: 624, generics: 258
- `misc/gen_blog_post_html.py` (PYTHON) | Magnitude: 104.42 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 105, branch: 30, state_mutation: 27, regex_execution: 22
- `mypy/server/mergecheck.py` (PYTHON) | Magnitude: 46.24 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 22, branch: 20, debug_prints: 7
- `mypy/semanal_typeddict.py` (PYTHON) | Magnitude: 87.3 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 489, branch: 155, structural_boundaries: 114, safety: 55
- `mypy/meet.py` (PYTHON) | Magnitude: 718.9 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 852, branch: 382, structural_boundaries: 368, safety: 187

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `mypy/types.py` -> Churn: **66.94%** | Cog Load: 38.8157% | Debt: 100.0%
- `mypy/nodes.py` -> Churn: **64.56%** | Cog Load: 29.6097% | Debt: 100.0%
- `mypyc/ir/ops.py` -> Churn: **58.22%** | Cog Load: 30.9501% | Debt: 100.0%
- `mypy/fastparse.py` -> Churn: **54.15%** | Cog Load: 36.375% | Debt: 96.6584%
- `mypy/typeanal.py` -> Churn: **53.63%** | Cog Load: 35.0373% | Debt: 89.1499%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `mypy/nativeparse.py` -> **Ivan Levkivskyi** (83.3% isolated ownership) | Magnitude: 736.76
- `mypy/suggestions.py` -> **Marc Mueller** (100.0% isolated ownership) | Magnitude: 705.8
- `mypy/plugins/dataclasses.py` -> **Shantanu** (100.0% isolated ownership) | Magnitude: 463.36
- `mypy/inspections.py` -> **Marc Mueller** (100.0% isolated ownership) | Magnitude: 395.42
- `mypy/typeshed/stubs/mypy-extensions/mypy_extensions.pyi` -> **Shantanu** (100.0% isolated ownership) | Magnitude: 371.23

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `mypy/plugins/ctypes.py` -> **Severity: 4.912** (Bridge: 0.0522 * Flux: 94.1446%)
- `mypy/util.py` -> **Severity: 4.832** (Bridge: 0.0534 * Flux: 90.4011%)
- `mypy/nodes.py` -> **Severity: 3.063** (Bridge: 0.0313 * Flux: 97.8503%)
- `mypy/types.py` -> **Severity: 2.219** (Bridge: 0.0232 * Flux: 95.5418%)
- `mypy/options.py` -> **Severity: 1.987** (Bridge: 0.0199 * Flux: 99.9983%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `mypy/options.py` -> **Severity: 24.568** (Embedded: 0.2719 * Error Risk: 90.3411%)
- `mypy/visitor.py` -> **Severity: 22.313** (Embedded: 0.2425 * Error Risk: 92.0168%)
- `mypy/strconv.py` -> **Severity: 21.119** (Embedded: 0.222 * Error Risk: 95.119%)
- `mypy/typeshed/stubs/mypy-extensions/mypy_extensions.pyi` -> **Severity: 20.756** (Embedded: 0.314 * Error Risk: 66.0935%)
- `mypy/nodes.py` -> **Severity: 20.495** (Embedded: 0.3417 * Error Risk: 59.9817%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `mypy/typeshed/stubs/mypy-extensions/mypy_extensions.pyi` -> **Severity: 6958.3** (Blast Radius: 69.583 * Doc Risk: 100.0%)
- `mypy/types.py` -> **Severity: 4871.2** (Blast Radius: 48.712 * Doc Risk: 100.0%)
- `mypy/nodes.py` -> **Severity: 4609.625** (Blast Radius: 53.267 * Doc Risk: 86.5381%)
- `mypyc/ir/ops.py` -> **Severity: 3689.9** (Blast Radius: 36.899 * Doc Risk: 100.0%)
- `mypy/util.py` -> **Severity: 3425.897** (Blast Radius: 43.679 * Doc Risk: 78.4335%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
