# ARCHITECTURAL_BRIEF: more-itertools
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
| Total Artifacts | 26 |
| Analyzed Artifacts (Scanned) | 15 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11 |
| Total LOC | 10498 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 9 | 10467 | 60.0% |
| PLAINTEXT | 5 | 0 | 33.3% |
| MAKEFILE | 1 | 31 | 6.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 53%, Large Core Modules 27%, Generic / Templated Code Files 13%, I/O & Config Routines Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 10 | 66.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 33.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 22 LOC)
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 38.8 | 11.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.5 | 62.9 | 71.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.3 | 16.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 32.7 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 83.9 | 31.3 | 14.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 12.9 | 1.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.8 | 7.4 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 5.0 | 1.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 70.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 45.3 | 43.7 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 901 | 4 | 155 | `more_itertools-11.0.1/tests/test_more.py` |
| cleanup | 1 | 1 | 0 | `more_itertools-11.0.1/more_itertools/more.py` |
| guards | 251 | 6 | 30 | `more_itertools-11.0.1/more_itertools/more.py` |
| danger | 252 | 8 | 79 | `more_itertools-11.0.1/more_itertools/more.py` |
| concurrency | 328 | 6 | 107 | `more_itertools-11.0.1/more_itertools/more.pyi` |
| connectivity | 1395 | 7 | 197 | `more_itertools-11.0.1/tests/test_more.py` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 28 | 1 | 0 | `more_itertools-11.0.1/tests/test_more.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 15 | 2 | 3 | `more_itertools-11.0.1/tests/test_more.py` |
| tests | 914 | 2 | 196 | `more_itertools-11.0.1/tests/test_more.py` |
| docs | 355 | 7 | 106 | `more_itertools-11.0.1/more_itertools/more.py` |
| debt | 51 | 4 | 15 | `more_itertools-11.0.1/more_itertools/more.pyi` |
| mutation | 4447 | 7 | 1021 | `more_itertools-11.0.1/tests/test_more.py` |
| dead_code | 421 | 3 | 93 | `more_itertools-11.0.1/tests/test_more.py` |
| credential | 0 | 0 | 0 | - |
| threat | 18 | 5 | 6 | `more_itertools-11.0.1/more_itertools/more.py` |
| ml_ai | 6 | 3 | 2 | `more_itertools-11.0.1/more_itertools/recipes.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `more_itertools-11.0.1/MANIFEST.in` (Hits: 0)
- `more_itertools-11.0.1/requirements/development.txt` (Hits: 0)
- `more_itertools-11.0.1/requirements/packaging.txt` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_more.py** (`more_itertools-11.0.1/tests/test_more.py`) — 25 outbound dependencies
2. **more.py** (`more_itertools-11.0.1/more_itertools/more.py`) — 23 outbound dependencies
3. **test_recipes.py** (`more_itertools-11.0.1/tests/test_recipes.py`) — 13 outbound dependencies
4. **recipes.py** (`more_itertools-11.0.1/more_itertools/recipes.py`) — 11 outbound dependencies
5. **more.pyi** (`more_itertools-11.0.1/more_itertools/more.pyi`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_islice_helper` **(Compute Cores)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **72.8** | LOC: 106
- `distinct_permutations` **(Many-Argument Workhorses)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **57.6** | LOC: 148
  * *Intent:* """Yield successive distinct permutations of the elements in *iterable*. >>> sorted(distinct_permutations([1, 0, 1])) [(0, 1, 1), (1, 0, 1), (1, 1, 0)...
- `set_partitions` **(Many-Argument Workhorses)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **53.1** | LOC: 79
  * *Intent:* """ Yield the set partitions of *iterable* into *k* parts. Set partitions are not order-preserving. >>> iterable = 'abc' >>> for part in set_partition...
- `minmax` **(Many-Argument Workhorses)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **35.1** | LOC: 75
  * *Intent:* """Returns both the smallest and largest items from an iterable or from two or more arguments. >>> minmax([3, 1, 5]) (1, 5) >>> minmax(4, 2, 6) (2, 6)
- `_get_slice` **(Compute Cores)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **32.4** | LOC: 25
  * *Intent:* # Normalize the slice's arguments step = 1 if (index.step is None) else index.step if step > 0: start = 0 if (index.start is None) else index.start st...
- `replace` **(Many-Argument Workhorses)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **27.8** | LOC: 66
  * *Intent:* """Yield the items from *iterable*, replacing the items for which *pred* returns ``True`` with the items from the iterable *substitutes*. >>> iterable...
- `sample` **(Many-Argument Workhorses)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **26.1** | LOC: 81
  * *Intent:* """Return a *k*-length list of elements chosen (without replacement) from the *iterable*. Similar to :func:`random.sample`, but works on inputs that a...
- `zip_broadcast` **(Many-Argument Workhorses)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **24.6** | LOC: 53
  * *Intent:* """A version of :func:`zip` that "broadcasts" any scalar (i.e., non-iterable) items into output tuples. >>> iterable_1 = [1, 2, 3] >>> iterable_2 = ['...
- `constrained_batches` **(Many-Argument Workhorses)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **24.4** | LOC: 48
- `nth_combination_with_replacement` **(Many-Argument Workhorses)** (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **24.1** | LOC: 41
  * *Intent:* """Equivalent to ``list(combinations_with_replacement(iterable, r))[index]``. The subsequences with repetition of *iterable* that are of length *r* ca...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `more_itertools-11.0.1/tests` | 3 | 5400.42 | 14.4% | 0.0% |
| `more_itertools-11.0.1/more_itertools` | 6 | 5001.74 | 12.55% | 26.77% |
| `more_itertools-11.0.1` | 2 | 20.32 | 0.0% | 0.0% |
| `more_itertools-11.0.1/requirements` | 4 | 4.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `more_itertools-11.0.1/more_itertools/more.pyi` -> **98.2742%** Exposure
- `more_itertools-11.0.1/more_itertools/more.py` -> **51.5413%** Exposure
- `more_itertools-11.0.1/more_itertools/recipes.py` -> **10.8042%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `more_itertools-11.0.1/more_itertools/more.py` -> **100.0%** Exposure
- `more_itertools-11.0.1/more_itertools/recipes.py` -> **100.0%** Exposure
- `more_itertools-11.0.1/more_itertools/recipes.pyi` -> **26.6225%** Exposure
- `more_itertools-11.0.1/more_itertools/__init__.py` -> **16.7982%** Exposure
- `more_itertools-11.0.1/more_itertools/more.pyi` -> **14.727%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `more_itertools-11.0.1/tests/test_more.py` -> **323** Orphaned Functions | **4** Duplicates
- `more_itertools-11.0.1/tests/test_recipes.py` -> **93** Orphaned Functions | **0** Duplicates
- `more_itertools-11.0.1/more_itertools/more.pyi` -> **0** Orphaned Functions | **25** Duplicates
- `more_itertools-11.0.1/more_itertools/more.py` -> **0** Orphaned Functions | **14** Duplicates

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
- **Unknown Dependencies:** `86` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `more_itertools-11.0.1/more_itertools/more.py` (PYTHON) -> Cumulative Risk: **625.14**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.44)
- **Magnitude:** 3375.76 | **LOC:** 5584 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.5264%), Verification (80.0%)
- **Heaviest Functions:** `_islice_helper` (Compute Cores, Impact: 72.8), `distinct_permutations` (Many-Argument Workhorses, Impact: 57.6), `set_partitions` (Many-Argument Workhorses, Impact: 53.1)

### 2. `more_itertools-11.0.1/more_itertools/more.pyi` (PYTHON) -> Cumulative Risk: **591.52**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.44)
- **Magnitude:** 678.26 | **LOC:** 1006 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.2742%), Api Exposure (82.773%)
- **Heaviest Functions:** `zip_broadcast` (Generic / Templated Code, Impact: 3.7), `zip_offset` (Generic / Templated Code, Impact: 3.3), `zip_offset` (Generic / Templated Code, Impact: 3.3)

### 3. `more_itertools-11.0.1/more_itertools/recipes.py` (PYTHON) -> Cumulative Risk: **540.2**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.94)
- **Magnitude:** 745.98 | **LOC:** 1477 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.439%), Verification (80.0%)
- **Heaviest Functions:** `iter_index` (Many-Argument Workhorses, Impact: 22.1), `is_prime` (Compute Cores, Impact: 20.7), `grouper` (Many-Argument Workhorses, Impact: 17.6)

### 4. `more_itertools-11.0.1/more_itertools/recipes.pyi` (PYTHON) -> Cumulative Risk: **512.49**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.12)
- **Magnitude:** 178.14 | **LOC:** 212 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Api Exposure (83.9454%), Verification (80.0%)
- **Heaviest Functions:** `grouper` (Generic / Templated Code, Impact: 2.5), `iter_index` (Generic / Templated Code, Impact: 2.5), `unique` (Generic / Templated Code, Impact: 2.2)

### 5. `more_itertools-11.0.1/tests/test_more.py` (PYTHON) -> Cumulative Risk: **370.89**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.70)
- **Magnitude:** 4375.42 | **LOC:** 6892 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (88.1356%), Safety Score (82.039%), Stability (50.0%)
- **Heaviest Functions:** `test_elements_lifecycle` (Tests & Verification, Impact: 14.0), `test_concurrent_consumers` (Compute Cores, Impact: 13.5), `test_concurrent_calls` (Compute Cores, Impact: 13.0)

### 6. `more_itertools-11.0.1/tests/test_recipes.py` (PYTHON) -> Cumulative Risk: **314.75**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.63)
- **Magnitude:** 1014.48 | **LOC:** 1658 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (73.8392%), Documentation (64.8276%), Stability (50.0%)
- **Heaviest Functions:** `test_vs_statistics_median_windowed` (Type Conversions, Impact: 9.0), `test_vs_statistics_median` (Compute Cores, Impact: 8.0), `test_multiple` (C Struct Operations, Impact: 6.8)

### 7. `more_itertools-11.0.1/Makefile` (MAKEFILE) -> Cumulative Risk: **214.08**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.23)
- **Magnitude:** 19.32 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Documentation (50.0%), Api Exposure (11.7125%)
- **Heaviest Functions:** `check` (I/O & Config Routines, Impact: 1.3), `coverage` (I/O & Config Routines, Impact: 1.3), `requirements` (I/O & Config Routines, Impact: 1.2)

### 8. `more_itertools-11.0.1/more_itertools/__init__.py` (PYTHON) -> Cumulative Risk: **140.72**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Data / Markup / Trivial` (z +0.00)
- **Magnitude:** 12.56 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (71.6205%), Stability (50.0%), State Flux (16.7982%), Verification (2.2977%)

### 9. `more_itertools-11.0.1/more_itertools/__init__.pyi` (PYTHON) -> Cumulative Risk: **122.5**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Data / Markup / Trivial` (z +0.00)
- **Magnitude:** 11.04 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (70.2063%), Stability (50.0%), Verification (2.2977%)

### 10. `more_itertools-11.0.1/tests/__init__.py` (PYTHON) -> Cumulative Risk: **50.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Composition Archetype:** `Data / Markup / Trivial` (z +0.00)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `more_itertools-11.0.1/tests/test_more.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 4375.42 | **LOC:** 6892 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.2378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_elements_lifecycle` **(Tests & Verification)** (Impact: 14.0)
    * *Intent:* # CPython does reference counting. # GC is not required when ref counting is supported. refCountSupp...
  * `test_concurrent_consumers` **(Compute Cores)** (Impact: 13.5)
  * `test_concurrent_calls` **(Compute Cores)** (Impact: 13.0)
  * `_target` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `test_concurrent_calls` **(Compute Cores)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 370 instances
* *State Mutation (weighted view):* 1933
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 1003`, `args: 810`, `func_start: 634`, `class_start: 126`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 1193`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 323`
* *Architecture:* `api: 727`, `concurrency: 1`, `import: 25`
* *Defense:* `safety: 14`, `doc: 106`, `test: 717`, `sync_locks: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, cmath, collections, collections.abc, datetime, decimal, doctest, fractions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/more.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3375.76 | **LOC:** 5584 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.7868%), Tech Debt (51.5413%)
**Top Internal Functions/Classes:**
  * `_islice_helper` **(Compute Cores)** (Impact: 72.8)
  * `distinct_permutations` **(Many-Argument Workhorses)** (Impact: 57.6)
    * *Intent:* """Yield successive distinct permutations of the elements in *iterable*. >>> sorted(distinct_permuta...
  * `set_partitions` **(Many-Argument Workhorses)** (Impact: 53.1)
    * *Intent:* """ Yield the set partitions of *iterable* into *k* parts. Set partitions are not order-preserving. ...
  * `minmax` **(Many-Argument Workhorses)** (Impact: 35.1)
    * *Intent:* """Returns both the smallest and largest items from an iterable or from two or more arguments. >>> m...
  * `_get_slice` **(Compute Cores)** (Impact: 32.4)
    * *Intent:* # Normalize the slice's arguments step = 1 if (index.step is None) else index.step if step > 0: star...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 448 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 603`, `structural_boundaries: 549`, `args: 217`, `func_start: 206`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 503`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 14`
* *Architecture:* `api: 155`, `concurrency: 2`, `import: 19`
* *Defense:* `safety: 87`, `doc: 124`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .recipes, cmath, collections, collections.abc, concurrent.future, concurrent.futures, contextlib, dataclasses...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/tests/test_recipes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1014.48 | **LOC:** 1658 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9562%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_vs_statistics_median_windowed` **(Type Conversions)** (Impact: 9.0)
  * `test_vs_statistics_median` **(Compute Cores)** (Impact: 8.0)
  * `test_multiple` **(C Struct Operations)** (Impact: 6.8)
    * *Intent:* """ensure can catch multiple exceptions"""
  * `test_basics` **(Type Conversions)** (Impact: 6.8)
  * `test_multidimensional` **(Type Conversions)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 406
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 306`, `args: 168`, `func_start: 146`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 220`, `unreferenced_by_name: 93`
* *Architecture:* `api: 197`, `import: 14`
* *Defense:* `safety: 7`, `doc: 70`, `test: 196`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, decimal, doctest, fractions, functools, itertools, math, more_itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/recipes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 745.98 | **LOC:** 1477 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5146%), Tech Debt (10.8042%)
**Top Internal Functions/Classes:**
  * `iter_index` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* """Yield the index of each place in *iterable* that *value* occurs, beginning with index *start* and...
  * `is_prime` **(Compute Cores)** (Impact: 20.7)
    * *Intent:* """Return ``True`` if *n* is prime and ``False`` otherwise. Basic examples: >>> is_prime(37) True >>...
  * `grouper` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* """Group elements from *iterable* into fixed-length groups of length *n*. >>> list(grouper('ABCDEF',...
  * `partition` **(Compute Cores)** (Impact: 15.8)
    * *Intent:* """ Returns a 2-tuple of iterables derived from the input iterable. The first yields the items that ...
  * `factor` **(Compute Cores)** (Impact: 15.7)
    * *Intent:* """Yield the prime factors of n. >>> list(factor(360)) [2, 2, 2, 3, 3, 5] Finds small factors with t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 304
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 182`, `args: 64`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 110`, `planned_debt: 3`
* *Architecture:* `api: 53`, `import: 14`
* *Defense:* `safety: 14`, `doc: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bisect, collections, contextlib, functools, heapq, itertools, math, more_itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/more.pyi` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 678.26 | **LOC:** 1006 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (98.2742%)
**Top Internal Functions/Classes:**
  * `zip_broadcast` **(Generic / Templated Code)** (Impact: 3.7)
  * `zip_offset` **(Generic / Templated Code)** (Impact: 3.3)
  * `zip_offset` **(Generic / Templated Code)** (Impact: 3.3)
  * `zip_broadcast` **(Generic / Templated Code)** (Impact: 3.3)
  * `zip_broadcast` **(Generic / Templated Code)** (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 282`, `args: 227`, `func_start: 227`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 16`, `duplicate_logic: 25`
* *Architecture:* `api: 194`, `concurrency: 1`, `import: 10`
* *Defense:* `doc: 1`, `sync_locks: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections.abc, contextlib, dataclasses, decimal, fractions, threading, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/recipes.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 178.14 | **LOC:** 212 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `grouper` **(Generic / Templated Code)** (Impact: 2.5)
  * `iter_index` **(Generic / Templated Code)** (Impact: 2.5)
  * `unique` **(Generic / Templated Code)** (Impact: 2.2)
  * `iter_except` **(Generic / Templated Code)** (Impact: 2.2)
  * `iter_except` **(Generic / Templated Code)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 74`, `args: 60`, `func_start: 60`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 7`
* *Architecture:* `api: 60`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections.abc, decimal, fractions, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 19.32 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check` **(I/O & Config Routines)** (Impact: 1.3)
  * `coverage` **(I/O & Config Routines)** (Impact: 1.3)
  * `requirements` **(I/O & Config Routines)** (Impact: 1.2)
  * `format` **(I/O & Config Routines)** (Impact: 1.2)
  * `test` **(I/O & Config Routines)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 8`
* *Risk/State:* None
* *Architecture:* `api: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 12.56 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .more, .recipes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/__init__.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 11.04 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .more, .recipes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/requirements/development.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/requirements/packaging.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/requirements/testing.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/requirements/typechecks.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
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

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `more_itertools-11.0.1/more_itertools/more.pyi` -> **Severity: 6666.7** (Blast Radius: 66.667 * Doc Risk: 100.0%)
- `more_itertools-11.0.1/more_itertools/recipes.pyi` -> **Severity: 6666.7** (Blast Radius: 66.667 * Doc Risk: 100.0%)
- `more_itertools-11.0.1/tests/test_more.py` -> **Severity: 5875.736** (Blast Radius: 66.667 * Doc Risk: 88.1356%)
- `more_itertools-11.0.1/tests/test_recipes.py` -> **Severity: 4321.862** (Blast Radius: 66.667 * Doc Risk: 64.8276%)
- `more_itertools-11.0.1/Makefile` -> **Severity: 3333.35** (Blast Radius: 66.667 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
