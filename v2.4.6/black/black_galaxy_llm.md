# ARCHITECTURAL_BRIEF: black
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/black` |
| **Timestamp** | `2026-08-03T19:35:10.412123+00:00` |
| **Scan Duration** | `1.25s` |
| **Git Branch** | `main` |
| **Git Commit** | `e079b7e100d1e181d4ee860ee4512bf3326f32c3` |
| **Git Remote** | `https://github.com/psf/black.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 312 malicious artifacts.

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
| Total Artifacts | 453 |
| Analyzed Artifacts (Scanned) | 327 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 126 |
| Total LOC | 29067 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 72.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3391 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1814 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5034 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 311 | 28817 | 95.1% |
| PLAINTEXT | 7 | 0 | 2.1% |
| MARKDOWN | 6 | 0 | 1.8% |
| DOCKERFILE | 1 | 18 | 0.3% |
| YAML | 1 | 77 | 0.3% |
| JSON | 1 | 155 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.469`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 245 | 74.9% |
| file_cluster_13 | 35 | 10.7% |
| file_cluster_16 | 20 | 6.1% |
| file_cluster_4 | 5 | 1.5% |
| file_cluster_0 | 4 | 1.2% |
| file_cluster_17 | 3 | 0.9% |
| file_cluster_7 | 2 | 0.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 4.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 126*

**Composition by Extension & Reason:**
- `.md`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 8x Excluded (Unsupported Extension: '.toml'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 8002 LOC), 1x Excluded (Monolithic Amalgamation: 41441 LOC exceeds safe regex boundaries)
- `.ipynb`: 6x Excluded (Unsupported Extension: '.ipynb')
- `.cfg`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.diff`: 4x Excluded (Unsupported Extension: '.diff')
- `.pie`: 3x Excluded (Unsupported Extension: '.pie'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.ini')
- `.vim`: 2x Excluded (Unsupported Extension: '.vim')
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 92.0 | 8.5 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 23.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 15.1 | 3.9 | 1.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 77.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.9 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 65.5 | 4.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 17.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `action/main.py` (Hits: 32)
- `tests/data/cases/remove_with_brackets.py` (Hits: 30)
- `tests/test_black.py` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **abc.py** (`tests/data/ignore_directory_gitignore_tests/abc.py`) — 24 inbound connections
2. **mode.py** (`src/black/mode.py`) — 14 inbound connections
3. **pytree.py** (`src/blib2to3/pytree.py`) — 13 inbound connections
4. **nodes.py** (`src/black/nodes.py`) — 10 inbound connections
5. **output.py** (`src/black/output.py`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_black.py** (`tests/test_black.py`) — 40 outbound dependencies
2. **__init__.py** (`src/black/__init__.py`) — 39 outbound dependencies
3. **concurrency.py** (`src/black/concurrency.py`) — 21 outbound dependencies
4. **files.py** (`src/black/files.py`) — 21 outbound dependencies
5. **linegen.py** (`src/black/linegen.py`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `visit_STANDALONE_COMMENT` (@ `src/black/linegen.py`) -> Impact: **2764.4** | LOC: 1577
  * *Intent:* """End of file. Process outstanding comments and end with a newline."""
- `test_get_future_imports` (@ `tests/test_black.py`) -> Impact: **1267.6** | LOC: 2315
- `_validate_msg` (@ `src/black/trans.py`) -> Impact: **1103.2** | LOC: 847
- `calcfirst` (@ `src/blib2to3/pgen2/pgen.py`) -> Impact: **691.7** | LOC: 255
  * *Intent:* # print name, self.first[name].keys()
- `parse_tokens` (@ `src/blib2to3/pgen2/driver.py`) -> Impact: **625.4** | LOC: 187
- `tokenize` (@ `src/blib2to3/pgen2/tokenize.py`) -> Impact: **333.1** | LOC: 114
- `parse_graminit_h` (@ `src/blib2to3/pgen2/conv.py`) -> Impact: **208.2** | LOC: 162
  * *Intent:* """ # Python imports import re # Local imports from blib2to3.pgen2 import grammar, token
- `test` (@ `tests/data/cases/composition_no_trailing_comma.py`) -> Impact: **205.1** | LOC: 223
- `get_grammars` (@ `tests/data/cases/pattern_matching_generic.py`) -> Impact: **183.8** | LOC: 77
- `has_triple_quotes` (@ `src/black/strings.py`) -> Impact: **176.3** | LOC: 126

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `stringify_node` (@ `src/black/comments.py`) -> **O(2^N) [Recursive]**
- `parse_tokens` (@ `src/blib2to3/pgen2/driver.py`) -> **O(2^N) [Recursive]**
- `calcfirst` (@ `src/blib2to3/pgen2/pgen.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # print name, self.first[name].keys()
- `tokenize` (@ `src/blib2to3/pgen2/tokenize.py`) -> **O(2^N) [Recursive]**
- `_recursive_matches` (@ `src/blib2to3/pytree.py`) -> **O(2^N) [Recursive]**
- `test` (@ `tests/data/cases/composition.py`) -> **O(2^N) [Recursive]**
- `test` (@ `tests/data/cases/composition_no_trailing_comma.py`) -> **O(2^N) [Recursive]**
- `visit_default` (@ `src/black/linegen.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Special case for async def/for/with statements. `visit_async_stmt` # adds an `ASYNC` leaf then visits the child def/for/with statement # `ASYNC` lea...
- `blackify` (@ `scripts/migrate-black.py`) -> **O(2^N) [Recursive]**
- `read` (@ `src/black/cache.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_get_future_imports` (@ `tests/test_black.py`) -> DB Complexity: **63**
- `visit_STANDALONE_COMMENT` (@ `src/black/linegen.py`) -> DB Complexity: **49**
  * *Intent:* """End of file. Process outstanding comments and end with a newline."""
- `parse_tokens` (@ `src/blib2to3/pgen2/driver.py`) -> DB Complexity: **42**
- `find_black_version_in_array` (@ `action/main.py`) -> DB Complexity: **34**
- `read_version_specifier_from_pyproject` (@ `action/main.py`) -> DB Complexity: **24**
- `parse_graminit_h` (@ `src/blib2to3/pgen2/conv.py`) -> DB Complexity: **22**
  * *Intent:* """ # Python imports import re # Local imports from blib2to3.pgen2 import grammar, token
- `initialize` (@ `src/blib2to3/pygram.py`) -> DB Complexity: **22**
- `add_template_to_changes` (@ `scripts/release.py`) -> DB Complexity: **12**
  * *Intent:* <!-- Changes to Black's terminal output and error messages --> ### _Blackd_ <!-- Changes to blackd --> ### Integrations <!-- For example, Docker, GitH...
- `calcfirst` (@ `src/blib2to3/pgen2/pgen.py`) -> DB Complexity: **12**
  * *Intent:* # print name, self.first[name].keys()
- `generate_matches` (@ `src/blib2to3/pytree.py`) -> DB Complexity: **10**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/black` | 24 | 8634.78 | 14.51% | 15.81% |
| `tests` | 13 | 2980.24 | 8.64% | 0.0% |
| `src/blib2to3/pgen2` | 9 | 2969.18 | 17.84% | 20.94% |
| `src/blib2to3` | 6 | 1306.0 | 8.84% | 31.96% |
| `src/blackd` | 4 | 659.83 | 25.16% | 0.0% |
| `scripts` | 10 | 568.12 | 9.78% | 23.74% |
| `action` | 1 | 253.08 | 14.63% | 13.12% |
| `__monolith__` | 8 | 163.8 | 12.03% | 5.54% |
| `src/black/resources` | 2 | 28.62 | 2.5% | 0.0% |
| `profiling` | 1 | 17.04 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/release_tests.py` -> **100.0%** Exposure
- `src/black/rusty.py` -> **100.0%** Exposure
- `src/blib2to3/pytree.py` -> **100.0%** Exposure
- `src/black/schema.py` -> **99.9996%** Exposure
- `scripts/fuzz.py` -> **99.9729%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Dockerfile` -> **100.0%** Exposure
- `src/blib2to3/pytree.py` -> **99.9531%** Exposure
- `src/blib2to3/pgen2/parse.py` -> **99.9286%** Exposure
- `src/blib2to3/pgen2/pgen.py` -> **99.9071%** Exposure
- `src/blib2to3/pgen2/conv.py` -> **99.4367%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/blib2to3/pytree.py` -> **0** Orphaned Functions | **48** Duplicates
- `tests/test_blackd.py` -> **33** Orphaned Functions | **10** Duplicates
- `tests/data/cases/generics_wrapping.py` -> **0** Orphaned Functions | **42** Duplicates
- `tests/data/cases/return_annotation_brackets.py` -> **0** Orphaned Functions | **39** Duplicates
- `tests/data/cases/funcdef_return_type_trailing_comma.py` -> **0** Orphaned Functions | **37** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`action/main.py`** -> AI Confidence: **99.31%**
2. **`src/black/__init__.py`** -> AI Confidence: **99.31%**
3. **`src/black/comments.py`** -> AI Confidence: **99.31%**
4. **`src/black/concurrency.py`** -> AI Confidence: **99.31%**
5. **`src/black/linegen.py`** -> AI Confidence: **99.31%**
6. **`src/black/lines.py`** -> AI Confidence: **99.31%**
7. **`src/black/output.py`** -> AI Confidence: **99.31%**
8. **`src/black/parsing.py`** -> AI Confidence: **99.31%**
9. **`src/black/trans.py`** -> AI Confidence: **99.31%**
10. **`Dockerfile`** -> AI Confidence: **99.29%**
11. **`tests/data/cases/attribute_access_on_number_literals.py`** -> AI Confidence: **99.29%**
12. **`tests/data/cases/comments3.py`** -> AI Confidence: **99.29%**
13. **`tests/data/cases/conditional_expression.py`** -> AI Confidence: **99.29%**
14. **`tests/data/cases/expression.py`** -> AI Confidence: **99.29%**
15. **`tests/data/cases/fmtskip5.py`** -> AI Confidence: **99.29%**
16. **`tests/data/cases/fmtskip_multiple_strings.py`** -> AI Confidence: **99.29%**
17. **`tests/data/cases/fstring.py`** -> AI Confidence: **99.29%**
18. **`tests/data/cases/is_simple_lookup_for_doublestar_expression.py`** -> AI Confidence: **99.29%**
19. **`tests/data/cases/line_ranges_indentation.py`** -> AI Confidence: **99.29%**
20. **`tests/data/cases/long_strings_flag_disabled.py`** -> AI Confidence: **99.29%**
21. **`tests/data/cases/pattern_matching_complex.py`** -> AI Confidence: **99.29%**
22. **`tests/data/cases/pattern_matching_generic.py`** -> AI Confidence: **99.29%**
23. **`tests/data/cases/pattern_matching_simple.py`** -> AI Confidence: **99.29%**
24. **`tests/data/cases/pattern_matching_style.py`** -> AI Confidence: **99.29%**
25. **`tests/data/cases/pep_572_py310.py`** -> AI Confidence: **99.29%**
26. **`tests/data/cases/pep_572_py39.py`** -> AI Confidence: **99.29%**
27. **`tests/data/cases/prefer_rhs_split.py`** -> AI Confidence: **99.29%**
28. **`tests/data/cases/prefer_rhs_split_reformatted.py`** -> AI Confidence: **99.29%**
29. **`tests/data/cases/preview_cantfit_string.py`** -> AI Confidence: **99.29%**
30. **`tests/data/cases/preview_remove_multiline_lone_list_item_parens.py`** -> AI Confidence: **99.29%**
31. **`tests/data/cases/preview_wrap_comprehension_in.py`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `action/main.py` -> **100.0%** Exposure
- `scripts/diff_shades_gha_helper.py` -> **100.0%** Exposure
- `scripts/release.py` -> **100.0%** Exposure
- `scripts/release_tests.py` -> **100.0%** Exposure
- `src/black/brackets.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `scripts/diff_shades_gha_helper.py` -> **100.0%** Exposure
- `src/black/cache.py` -> **100.0%** Exposure
- `src/blib2to3/pgen2/grammar.py` -> **100.0%** Exposure
- `src/blib2to3/pygram.py` -> **100.0%** Exposure
- `tests/data/cases/fmtonoff.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `action/main.py` -> **100.0%** Exposure
- `scripts/check_version_in_basics_example.py` -> **100.0%** Exposure
- `scripts/diff_shades_gha_helper.py` -> **100.0%** Exposure
- `scripts/migrate-black.py` -> **100.0%** Exposure
- `scripts/release.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `561` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/blib2to3/pytree.py` (PYTHON) -> Cumulative Risk: **814.68**
- **Archetype:** `file_cluster_16` (Distance: 13.073 IQR)
- **Magnitude:** 1263.56 | **LOC:** 971 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `optimize` (Impact: 114.0), `generate_matches` (Impact: 86.6), `_recursive_matches` (Impact: 84.7)

### 2. `src/blib2to3/pgen2/driver.py` (PYTHON) -> Cumulative Risk: **752.07**
- **Archetype:** `file_cluster_13` (Distance: 10.894 IQR)
- **Magnitude:** 743.82 | **LOC:** 314 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `parse_tokens` (Impact: 625.4), `__next__` (Impact: 18.1), `eat` (Impact: 17.8)

### 3. `src/blib2to3/pgen2/pgen.py` (PYTHON) -> Cumulative Risk: **745.42**
- **Archetype:** `file_cluster_16` (Distance: 12.288 IQR)
- **Magnitude:** 966.22 | **LOC:** 389 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `calcfirst` (Impact: 691.7), `make_label` (Impact: 104.5), `make_grammar` (Impact: 32.4)

### 4. `src/black/concurrency.py` (PYTHON) -> Cumulative Risk: **736.69**
- **Archetype:** `file_cluster_4` (Distance: 11.613 IQR)
- **Magnitude:** 131.74 | **LOC:** 222 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 16.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (99.999%), Verification (80.0%)
- **Heaviest Functions:** `shutdown` (Impact: 28.9), `maybe_use_uvloop` (Impact: 14.6), `cancel` (Impact: 12.3)

### 5. `src/blib2to3/pgen2/parse.py` (PYTHON) -> Cumulative Risk: **728.78**
- **Archetype:** `file_cluster_16` (Distance: 11.952 IQR)
- **Magnitude:** 436.0 | **LOC:** 396 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_addtoken` (Impact: 105.1), `addtoken` (Impact: 49.4), `pop` (Impact: 44.1)

### 6. `src/blib2to3/pgen2/grammar.py` (PYTHON) -> Cumulative Risk: **706.02**
- **Archetype:** `file_cluster_16` (Distance: 10.057 IQR)
- **Magnitude:** 91.7 | **LOC:** 229 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), Logic Bomb (99.9911%)
- **Heaviest Functions:** `dump` (Impact: 28.6), `copy` (Impact: 17.0), `load` (Impact: 14.2)

### 7. `src/black/output.py` (PYTHON) -> Cumulative Risk: **676.23**
- **Archetype:** `file_cluster_13` (Distance: 10.568 IQR)
- **Magnitude:** 155.14 | **LOC:** 123 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `color_diff` (Impact: 28.8), `dump_to_file` (Impact: 26.5), `diff` (Impact: 18.9)

### 8. `src/black/handle_ipynb_magics.py` (PYTHON) -> Cumulative Risk: **663.86**
- **Archetype:** `file_cluster_13` (Distance: 11.067 IQR)
- **Magnitude:** 388.14 | **LOC:** 516 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `put_trailing_semicolon_back` (Impact: 142.7), `visit_Assign` (Impact: 105.3), `validate_cell` (Impact: 32.7)

### 9. `scripts/release_tests.py` (PYTHON) -> Cumulative Risk: **662.24**
- **Archetype:** `file_cluster_13` (Distance: 9.77 IQR)
- **Magnitude:** 43.28 | **LOC:** 70 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `test_get_next_version` (Impact: 11.2), `tearDown` (Impact: 5.3), `test_tuple_calver` (Impact: 2.9)

### 10. `src/black/brackets.py` (PYTHON) -> Cumulative Risk: **651.62**
- **Archetype:** `file_cluster_16` (Distance: 11.37 IQR)
- **Magnitude:** 527.12 | **LOC:** 384 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `is_split_before_delimiter` (Impact: 163.8), `mark` (Impact: 85.3), `get_leaves_inside_matching_brackets` (Impact: 67.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/black/linegen.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.881 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.441 IQR)
- **Top Global Matches:** file_cluster_13: 11.881, file_cluster_16: 11.941, file_cluster_7: 11.994
- **Magnitude:** 3380.86 | **LOC:** 2049 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (28.2693%), Tech Debt (11.9091%)
**Top Internal Functions/Classes:**
  * `visit_STANDALONE_COMMENT` (Impact: 2764.4 | O(N^6) | DB: 49)
    * *Intent:* """End of file. Process outstanding comments and end with a newline."""
  * `visit_default` (Impact: 84.4 | O(2^N) | DB: 4)
    * *Intent:* # Special case for async def/for/with statements. `visit_async_stmt` # adds an `ASYNC` leaf then vis...
  * `visit_simple_stmt` (Impact: 57.5 | O(N^4))
  * `visit_funcdef` (Impact: 55.9 | O(N^6))
  * `visit_dictsetmaker` (Impact: 55.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 501`, `structural_boundaries: 358`, `args: 64`, `func_start: 64`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 139`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 66`, `import: 17`
* *Defense:* `safety: 40`, `doc: 88`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.748
  * `Choke Point (Betweenness):` 3.9e-05 | `Ripple Effect (Closeness):` 0.003067
  * `Imports (Out-Degree: 10):` black.strings, from, re, black.mode, dataclasses, black.comments, collections.abc, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_black.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.897 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.55 IQR)
- **Top Global Matches:** file_cluster_8: 11.897, file_cluster_16: 11.971, file_cluster_13: 12.041
- **Magnitude:** 2066.24 | **LOC:** 3302 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (3.5957%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_get_future_imports` (Impact: 1267.6 | O(N^6) | DB: 63)
  * `test_get_features_used` (Impact: 59.4 | O(N^3))
  * `cache_dir` (Impact: 39.5 | O(2^N))
  * `test_one_empty_line_ff` (Impact: 37.2 | O(N^5) | DB: 9)
  * `test_skip_magic_trailing_comma` (Impact: 27.4 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 554`, `args: 209`, `func_start: 183`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 3`, `state_mutation: 48`, `dead_code: 1`, `planned_debt: 8`, `duplicate_logic: 3`, `orphaned_logic: 31`
* *Architecture:* `io: 27`, `api: 187`, `concurrency: 13`, `import: 54`
* *Defense:* `safety: 150`, `doc: 108`, `test: 353`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` some.module, pytest, types, platform, dataclasses, pathlib, click, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/black/trans.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.172 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.015 IQR)
- **Top Global Matches:** file_cluster_13: 11.172, file_cluster_16: 11.222, file_cluster_8: 11.277
- **Magnitude:** 1468.72 | **LOC:** 2561 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (18.8874%), Tech Debt (23.0251%)
**Top Internal Functions/Classes:**
  * `_validate_msg` (Impact: 1103.2 | O(N^6) | DB: 9)
  * `do_match` (Impact: 117.6 | O(N^6) | DB: 2)
  * `make_naked` (Impact: 27.4 | O(N^5) | DB: 1)
  * `handle_is_simple_look_up_prev` (Impact: 20.9 | O(N^3) | DB: 1)
  * `is_simple_operand` (Impact: 20.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 227`, `args: 33`, `func_start: 31`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 64`, `dead_code: 4`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 33`, `import: 15`
* *Defense:* `safety: 25`, `doc: 110`, `test: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.000189 | `Ripple Effect (Closeness):` 0.006902
  * `Imports (Out-Degree: 9):` black.strings, re, black.mode, dataclasses, black.comments, collections.abc, black.nodes, blib2to3.pgen2...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/blib2to3/pytree.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.073 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.83 IQR)
- **Top Global Matches:** file_cluster_16: 13.073, file_cluster_11: 13.232, file_cluster_13: 13.246
- **Magnitude:** 1263.56 | **LOC:** 971 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (41.8714%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `optimize` (Impact: 114.0 | O(2^N) | DB: 4)
  * `generate_matches` (Impact: 86.6 | O(N^6) | DB: 10)
  * `_recursive_matches` (Impact: 84.7 | O(2^N) | DB: 2)
  * `_iterative_matches` (Impact: 68.1 | O(N^6) | DB: 4)
  * `_submatch` (Impact: 63.8 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 232`, `args: 69`, `func_start: 68`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 135`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 48`
* *Architecture:* `io: 3`, `api: 63`, `import: 7`
* *Defense:* `safety: 45`, `doc: 116`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.758
  * `Choke Point (Betweenness):` 0.000308 | `Ripple Effect (Closeness):` 0.042604
  * `Imports (Out-Degree: 3):` .pgen2, collections.abc, sys, typing, .pgen2.token, , io, blib2to3.pgen2.grammar
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/blib2to3/pgen2/pgen.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.288 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.576 IQR)
- **Top Global Matches:** file_cluster_16: 12.288, file_cluster_13: 12.407, file_cluster_8: 12.432
- **Magnitude:** 966.22 | **LOC:** 389 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (49.5981%), Tech Debt (20.1878%)
**Top Internal Functions/Classes:**
  * `calcfirst` (Impact: 691.7 | O(2^N) | DB: 12)
    * *Intent:* # print name, self.first[name].keys()
  * `make_label` (Impact: 104.5 | O(N^5) | DB: 4)
    * *Intent:* # XXX Maybe this should be a method on a subclass of converter? ilabel = len(c.labels) if label[0].i...
  * `make_grammar` (Impact: 32.4 | O(N^5) | DB: 6)
  * `addfirstsets` (Impact: 13.3 | O(N^4))
  * `__init__` (Impact: 12.7 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 102`, `args: 25`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 72`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 25`, `import: 5`
* *Defense:* `safety: 31`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` os, blib2to3.pgen2.tokenize, collections.abc, typing, blib2to3.pgen2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/blib2to3/pgen2/driver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.894 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.622 IQR)
- **Top Global Matches:** file_cluster_13: 10.894, file_cluster_16: 11.235, file_cluster_0: 11.282
- **Magnitude:** 743.82 | **LOC:** 314 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (18.9201%), Tech Debt (89.5296%)
**Top Internal Functions/Classes:**
  * `parse_tokens` (Impact: 625.4 | O(2^N) | DB: 42)
  * `__next__` (Impact: 18.1 | O(N^4))
  * `eat` (Impact: 17.8 | O(N^4) | DB: 1)
    * *Intent:* # Lock the last release range to the final position that
  * `release` (Impact: 10.8 | O(N^3) | DB: 1)
  * `can_advance` (Impact: 10.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 86`, `args: 17`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 22`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 15`, `api: 18`, `import: 14`
* *Defense:* `safety: 14`, `doc: 16`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.276
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.009398
  * `Imports (Out-Degree: 4):` os, logging, pkgutil, blib2to3.pgen2.tokenize, dataclasses, collections.abc, sys, blib2to3.pytree...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/black/brackets.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.37 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.293 IQR)
- **Top Global Matches:** file_cluster_16: 11.37, file_cluster_13: 11.396, file_cluster_8: 11.432
- **Magnitude:** 527.12 | **LOC:** 384 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (21.6991%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `is_split_before_delimiter` (Impact: 163.8 | O(N^3))
  * `mark` (Impact: 85.3 | O(N^5) | DB: 6)
  * `get_leaves_inside_matching_brackets` (Impact: 67.2 | O(N^5) | DB: 2)
  * `max_delimiter_priority_in_atom` (Impact: 46.1 | O(N^4))
  * `maybe_decrement_after_for_loop_variable` (Impact: 18.0 | O(N^3) | DB: 1)
    * *Intent:* """ if not self.delimiters: return 0 priority = priority or self.max_delimiter_priority() return sum...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 107`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`
* *Architecture:* `api: 22`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 10`, `doc: 34`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008521
  * `Imports (Out-Degree: 3):` dataclasses, collections.abc, black.nodes, blib2to3.pytree, typing, blib2to3.pgen2
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/black/ranges.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.753 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.933 IQR)
- **Top Global Matches:** file_cluster_16: 10.753, file_cluster_8: 10.866, file_cluster_13: 10.951
- **Magnitude:** 449.56 | **LOC:** 535 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (14.0019%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_convert_unchanged_line_by_line` (Impact: 89.3 | O(N^4) | DB: 3)
  * `_get_line_range` (Impact: 74.8 | O(N^4))
    * *Intent:* # called all the decorators are collapsed into a single leaf node.insert_child(1, Leaf(NEWLINE, "\n"...
  * `_contains_standalone_comment` (Impact: 50.4 | O(2^N))
  * `_convert_nodes_to_standalone_comment` (Impact: 41.5 | O(N^4) | DB: 2)
  * `_convert_node_to_standalone_comment` (Impact: 37.6 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 76`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 40`
* *Architecture:* `api: 14`, `import: 5`
* *Defense:* `safety: 10`, `doc: 28`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.203
  * `Choke Point (Betweenness):` 0.00035 | `Ripple Effect (Closeness):` 0.017042
  * `Imports (Out-Degree: 3):` difflib, re, dataclasses, collections.abc, black.nodes, blib2to3.pgen2.token
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/blib2to3/pgen2/parse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.952 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.219 IQR)
- **Top Global Matches:** file_cluster_16: 11.952, file_cluster_13: 11.975, file_cluster_0: 12.262
- **Magnitude:** 436.0 | **LOC:** 396 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (24.4049%), Tech Debt (78.7433%)
**Top Internal Functions/Classes:**
  * `_addtoken` (Impact: 105.1 | O(N^6) | DB: 3)
  * `addtoken` (Impact: 49.4 | O(N^5))
  * `pop` (Impact: 44.1 | O(2^N) | DB: 4)
  * `classify` (Impact: 41.9 | O(N^5))
    * *Intent:* # If there are multiple states which we can advance (only # happen under soft-keywords), then we wil...
  * `add_token` (Impact: 33.9 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 84`, `args: 17`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 50`, `duplicate_logic: 3`
* *Architecture:* `api: 17`, `import: 7`
* *Defense:* `safety: 11`, `doc: 24`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.066
  * `Choke Point (Betweenness):` 0.000104 | `Ripple Effect (Closeness):` 0.010605
  * `Imports (Out-Degree: 4):` blib2to3.pytree, collections.abc, typing, contextlib, blib2to3.pgen2.driver, , blib2to3.pgen2.grammar
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_blackd.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.989 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.185 IQR)
- **Top Global Matches:** file_cluster_8: 9.989, file_cluster_4: 9.994, file_cluster_16: 10.114
- **Magnitude:** 431.5 | **LOC:** 450 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (47.911%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_blackd_format_code_limits_executor_` (Impact: 44.6 | O(N^6) | DB: 1)
  * `test_blackd_main` (Impact: 13.3 | O(N^4))
  * `test_blackd_request_syntax_error` (Impact: 8.4 | O(N^3))
  * `test_preserves_line_endings` (Impact: 8.4 | O(N^3))
  * `test_normalizes_line_endings` (Impact: 8.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 172`, `args: 64`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `planned_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 33`
* *Architecture:* `io: 2`, `api: 50`, `concurrency: 123`, `import: 15`
* *Defense:* `safety: 4`, `test: 44`, `sync_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` aiohttp.test_utils, threading, aiohttp, blackd.client, unittest.mock, datetime, pytest, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/black/handle_ipynb_magics.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.067 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.873 IQR)
- **Top Global Matches:** file_cluster_13: 11.067, file_cluster_16: 11.163, file_cluster_8: 11.358
- **Magnitude:** 388.14 | **LOC:** 516 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (8.904%), Tech Debt (97.8998%)
**Top Internal Functions/Classes:**
  * `put_trailing_semicolon_back` (Impact: 142.7 | O(N^5) | DB: 3)
  * `visit_Assign` (Impact: 105.3 | O(N^6) | DB: 2)
  * `validate_cell` (Impact: 32.7 | O(N^3))
  * `jupyter_dependencies_are_installed` (Impact: 14.4 | O(N^3))
  * `visit_Expr` (Impact: 14.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 84`, `args: 19`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 16`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 23`, `import: 16`
* *Defense:* `safety: 18`, `doc: 34`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.365
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.009816
  * `Imports (Out-Degree: 6):` tokenize_rt, ast, re, importlib.util, dataclasses, black.mode, collections.abc, secrets...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/blackd/client.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.829 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.808 IQR)
- **Top Global Matches:** file_cluster_4: 10.829, file_cluster_13: 10.964, file_cluster_8: 10.973
- **Magnitude:** 368.41 | **LOC:** 93 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (47.5482%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 3`, `api: 2`, `concurrency: 16`, `import: 3`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.739
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003067
  * `Imports (Out-Degree: 0):` aiohttp, aiohttp.typedefs, black
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/black/comments.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.649 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.162 IQR)
- **Top Global Matches:** file_cluster_13: 10.649, file_cluster_8: 10.662, file_cluster_16: 10.682
- **Magnitude:** 352.66 | **LOC:** 828 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 41.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (20.0078%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `list_comments` (Impact: 86.2 | O(N^4) | DB: 1)
  * `stringify_node` (Impact: 84.5 | O(2^N))
  * `make_comment` (Impact: 32.7 | O(N^2))
  * `_find_compound_statement_context` (Impact: 22.4 | O(N^2))
  * `is_fmt_on` (Impact: 14.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 142`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 33`, `dead_code: 2`
* *Architecture:* `api: 16`, `import: 9`
* *Defense:* `safety: 18`, `doc: 40`, `test: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.414
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.009816
  * `Imports (Out-Degree: 4):` re, black.mode, dataclasses, collections.abc, black.nodes, blib2to3.pytree, functools, typing...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/blib2to3/pgen2/tokenize.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.046 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.361 IQR)
- **Top Global Matches:** file_cluster_13: 9.046, file_cluster_8: 9.268, file_cluster_7: 9.475
- **Magnitude:** 351.38 | **LOC:** 278 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (10.6406%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tokenize` (Impact: 333.1 | O(2^N) | DB: 1)
  * `transform_whitespace` (Impact: 1.1 | O(N^1))
  * `printtoken` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 54`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 6`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 5`, `doc: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.001
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.015822
  * `Imports (Out-Degree: 3):` , pytokens, collections.abc, sys, blib2to3.pgen2.token, blib2to3.pgen2.grammar
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/black/parsing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.465 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.62 IQR)
- **Top Global Matches:** file_cluster_13: 11.465, file_cluster_16: 11.787, file_cluster_11: 11.916
- **Magnitude:** 282.06 | **LOC:** 245 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (21.6317%), Tech Debt (13.1644%)
**Top Internal Functions/Classes:**
  * `_stringify_ast` (Impact: 149.0 | O(N^6))
  * `parse_ast` (Impact: 36.0 | O(N^4) | DB: 3)
    * *Intent:* # TODO: support Python 4+ ;)
  * `_unwrap_tuples` (Impact: 32.3 | O(2^N))
  * `get_grammars` (Impact: 29.4 | O(N^3) | DB: 3)
  * `_normalize` (Impact: 3.9 | O(N^1))
    * *Intent:* # To normalize, we strip any leading and trailing space from
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 54`, `args: 10`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 13`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 9`, `import: 12`
* *Defense:* `safety: 27`, `doc: 10`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.64
  * `Choke Point (Betweenness):` 0.000345 | `Ripple Effect (Closeness):` 0.012781
  * `Imports (Out-Degree: 7):` blib2to3.pgen2.grammar, blib2to3.pgen2.parse, blib2to3.pgen2.tokenize, ast, blib2to3, black.mode, collections.abc, sys...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/blib2to3/pgen2/conv.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.998 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.933 IQR)
- **Top Global Matches:** file_cluster_8: 12.998, file_cluster_17: 13.03, file_cluster_13: 13.118
- **Magnitude:** 271.92 | **LOC:** 257 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (18.1171%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_graminit_h` (Impact: 208.2 | O(N^6) | DB: 22)
    * *Intent:* """ # Python imports import re # Local imports from blib2to3.pgen2 import grammar, token
  * `finish_off` (Impact: 22.2 | O(N^4) | DB: 2)
  * `run` (Impact: 3.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 50`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 30`
* *Architecture:* `io: 4`, `api: 5`, `import: 2`
* *Defense:* `safety: 39`, `doc: 12`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, blib2to3.pgen2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `action/main.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.354 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.574 IQR)
- **Top Global Matches:** file_cluster_8: 9.354, file_cluster_13: 9.553, file_cluster_7: 10.029
- **Magnitude:** 253.08 | **LOC:** 202 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (14.634%), Tech Debt (13.1217%)
**Top Internal Functions/Classes:**
  * `find_black_version_in_array` (Impact: 160.8 | O(N^5) | DB: 34)
  * `read_version_specifier_from_pyproject` (Impact: 47.5 | O(N^3) | DB: 24)
  * `determine_version_specifier` (Impact: 35.5 | O(N^3) | DB: 6)
    * *Intent:* """Determine the version of Black to install. The version can be specified either via the `with.vers...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 30`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `planned_debt: 1`
* *Architecture:* `io: 32`, `api: 3`, `import: 8`
* *Defense:* `safety: 7`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, re, subprocess, pathlib, sys, shutil, tomllib, shlex
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/black/nodes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.567 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.689 IQR)
- **Top Global Matches:** file_cluster_8: 10.567, file_cluster_16: 10.639, file_cluster_7: 10.836
- **Magnitude:** 249.24 | **LOC:** 1112 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (11.1059%), Tech Debt (8.5863%)
**Top Internal Functions/Classes:**
  * `get_annotation_type` (Impact: 24.6 | O(N^3))
    * *Intent:* """ if leaf.type == token.LPAR: leaf.value = "(" elif leaf.type == token.RPAR: leaf.value = ")" def ...
  * `first_leaf` (Impact: 24.4 | O(2^N))
  * `last_leaf` (Impact: 24.4 | O(2^N))
  * `has_sibling_with_type` (Impact: 18.1 | O(N^3))
  * `wrap_in_parentheses` (Impact: 14.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 413`, `args: 57`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 67`, `import: 9`
* *Defense:* `safety: 27`, `doc: 94`, `test: 6`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.688
  * `Choke Point (Betweenness):` 0.000869 | `Ripple Effect (Closeness):` 0.033162
  * `Imports (Out-Degree: 5):` black.cache, black.mode, blib2to3, collections.abc, blib2to3.pytree, blib2to3.pgen2, typing, statement....
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/blackd/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.532 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.9 IQR)
- **Top Global Matches:** file_cluster_8: 9.532, file_cluster_13: 9.807, file_cluster_0: 9.985
- **Magnitude:** 236.56 | **LOC:** 335 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (21.1924%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_python_variant_header` (Impact: 134.6 | O(N^6))
  * `parse_mode` (Impact: 62.5 | O(N^5))
  * `make_app` (Impact: 2.2 | O(N^1))
  * `patched_main` (Impact: 1.9 | O(N^1))
  * `executor` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 66`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `io: 3`, `api: 10`, `concurrency: 14`, `import: 14`
* *Defense:* `safety: 20`, `sync_locks: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` aiohttp, os, datetime, logging, black.concurrency, concurrent.futures, multiprocessing, click...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/black/lines.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.466 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.686 IQR)
- **Top Global Matches:** file_cluster_13: 11.466, file_cluster_0: 11.584, file_cluster_16: 11.731
- **Magnitude:** 199.28 | **LOC:** 1122 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (22.5568%), Tech Debt (11.8177%)
**Top Internal Functions/Classes:**
  * `append_safe` (Impact: 36.8 | O(N^5) | DB: 1)
  * `is_def` (Impact: 28.6 | O(N^3))
  * `is_class_paren_empty` (Impact: 24.8 | O(N^3))
  * `_is_triple_quoted_string` (Impact: 14.2 | O(N^3))
  * `is_class` (Impact: 10.8 | O(N^3))
    * *Intent:* """Is this a with_stmt line?"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 74`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 17`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 6`, `doc: 84`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.414
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.009816
  * `Imports (Out-Degree: 6):` line, black.mode, dataclasses, collections.abc, black.nodes, black.brackets, typing, blib2to3.pytree...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/black/strings.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.789 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.689 IQR)
- **Top Global Matches:** file_cluster_8: 9.789, file_cluster_13: 9.799, file_cluster_7: 9.945
- **Magnitude:** 187.72 | **LOC:** 392 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (8.9545%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `has_triple_quotes` (Impact: 176.3 | O(N^4) | DB: 1)
  * `sub_twice` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 32`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `doc: 39`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.794
  * `Choke Point (Betweenness):` 0.000203 | `Ripple Effect (Closeness):` 0.026015
  * `Imports (Out-Degree: 2):` re, blib2to3.pytree, sys, functools, typing, black._width_table
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/black/files.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.864 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.262 IQR)
- **Top Global Matches:** file_cluster_13: 10.864, file_cluster_16: 11.103, file_cluster_0: 11.248
- **Magnitude:** 179.82 | **LOC:** 427 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.0728%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `strip_specifier_set` (Impact: 41.0 | O(N^4) | DB: 4)
  * `parse_pyproject_toml` (Impact: 20.6 | O(N^3))
  * `get_gitignore` (Impact: 16.6 | O(N^3) | DB: 3)
  * `parse_req_python_specifier` (Impact: 15.6 | O(N^2))
  * `best_effort_relative_path` (Impact: 13.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 107`, `args: 18`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 12`
* *Architecture:* `io: 6`, `api: 18`, `import: 22`
* *Defense:* `safety: 24`, `doc: 24`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.951
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.006135
  * `Imports (Out-Degree: 5):` tomli, pathlib, sys, black.handle_ipynb_magics, pathspec, packaging.specifiers, mypy_extensions, os...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/migrate-black.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.048 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.387 IQR)
- **Top Global Matches:** file_cluster_8: 7.048, file_cluster_13: 7.673, file_cluster_7: 8.057
- **Magnitude:** 171.76 | **LOC:** 97 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (13.3334%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `blackify` (Impact: 164.1 | O(2^N) | DB: 9)
  * `git` (Impact: 4.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 3`, `api: 2`, `import: 5`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, logging, argparse, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/black/report.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.936 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.23 IQR)
- **Top Global Matches:** file_cluster_13: 10.936, file_cluster_16: 11.252, file_cluster_0: 11.326
- **Magnitude:** 171.68 | **LOC:** 108 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (24.4566%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `done` (Impact: 66.8 | O(N^5))
  * `__str__` (Impact: 57.6 | O(N^4) | DB: 3)
  * `return_code` (Impact: 14.5 | O(N^3))
  * `path_ignored` (Impact: 8.2 | O(N^3))
  * `failed` (Impact: 3.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 22`, `args: 5`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 11`, `import: 5`
* *Defense:* `safety: 2`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.969
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.019632
  * `Imports (Out-Degree: 1):` pathlib, dataclasses, click, black.output, enum
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `tests/test_ipynb.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.784 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.356 IQR)
- **Top Global Matches:** file_cluster_8: 9.784, file_cluster_16: 10.129, file_cluster_13: 10.264
- **Magnitude:** 160.92 | **LOC:** 566 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (3.634%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_entire_notebook_empty_metadata` (Impact: 29.0 | O(N^3))
  * `test_trailing_semicolon_indented` (Impact: 19.0 | O(N^3))
  * `test_ipynb_flag` (Impact: 18.1 | O(N^3) | DB: 3)
  * `test_unmask_cell_raises_when_token_is_no` (Impact: 9.0 | O(N^2))
  * `test_multiline_magic` (Impact: 8.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 88`, `args: 45`, `func_start: 40`
* *Risk/State:* `duplicate_logic: 2`, `orphaned_logic: 12`
* *Architecture:* `io: 4`, `api: 40`, `import: 14`
* *Defense:* `safety: 24`, `test: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, re, dataclasses, pathlib, black.handle_ipynb_magics, contextlib, tests.util, black...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `src/black/const.py` (PYTHON) | **Drift Ratio: 1.54x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.636 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.6 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/data/cases/dummy_implementations.py` (PYTHON) | Magnitude: 0.14 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 88, indent_spaces: 65, args: 58, func_start: 58
- `tests/data/miscellaneous/debug_visitor.py` (PYTHON) | Magnitude: 0.03 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, encapsulation: 5, branch: 4
- `tests/data/cases/comments9.py` (PYTHON) | Magnitude: 0.13 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 86, indent_spaces: 58, api: 46, safety_bypasses: 40
- `tests/data/cases/comments5.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.196 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, branch: 8, structural_boundaries: 8, decorators: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/test_no_ipynb.py` (PYTHON) | Magnitude: 9.16 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, test: 6, import: 5
- `src/black/comments.py` (PYTHON) | Magnitude: 352.66 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 462, branch: 175, structural_boundaries: 142, doc: 40
- `scripts/diff_shades_gha_helper.py` (PYTHON) | Magnitude: 37.82 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 128, structural_boundaries: 45, branch: 31, io: 15
- `src/black/trans.py` (PYTHON) | Magnitude: 1468.72 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 941, branch: 268, structural_boundaries: 227, doc: 110
- `src/black/linegen.py` (PYTHON) | Magnitude: 3380.86 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1327, branch: 501, structural_boundaries: 358, state_mutation: 139

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/data/cases/async_stmts.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 10, concurrency: 6, indent_spaces: 6, args: 4
- `tests/data/line_ranges_formatted/basic.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 14, branch: 7, api: 5
- `src/blib2to3/pgen2/parse.py` (PYTHON) | Magnitude: 436.0 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 84, state_mutation: 50, branch: 48
- `src/black/brackets.py` (PYTHON) | Magnitude: 527.12 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 228, structural_boundaries: 107, branch: 98, state_mutation: 36
- `tests/data/cases/skip_magic_trailing_comma_generic_wrap.py` (PYTHON) | Magnitude: 0.1 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 64, indent_spaces: 64, args: 32, func_start: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/data/cases/pep_572_do_not_remove_parens.py` (PYTHON) | Magnitude: 0.03 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 30, structural_boundaries: 10, safety_bypasses: 7, indent_spaces: 6
- `tests/data/cases/pep_572_py39.py` (PYTHON) | Magnitude: 0.03 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 15, branch: 1, comprehensions: 1
- `tests/data/cases/pep_572_py310.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.528 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 30, branch: 11, comprehensions: 4, indent_spaces: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/data/miscellaneous/async_as_identifier.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 24, concurrency: 24, indent_spaces: 14, args: 8
- `src/black/concurrency.py` (PYTHON) | Magnitude: 131.74 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 131, concurrency: 52, branch: 50, structural_boundaries: 47
- `src/blackd/client.py` (PYTHON) | Magnitude: 368.41 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, branch: 17, concurrency: 16, structural_boundaries: 14
- `tests/data/cases/remove_await_parens.py` (PYTHON) | Magnitude: 0.28 | Delta: **0.426 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 156, structural_boundaries: 100, indent_spaces: 85, thread_sleeps: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/data/cases/docstring.py` (PYTHON) | Magnitude: 0.13 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 136, structural_boundaries: 96, api: 74, args: 72
- `tests/data/cases/docstring_no_extra_empty_line_before_eof.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/data/cases/docstring_no_string_normalization.py` (PYTHON) | Magnitude: 0.09 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 76, structural_boundaries: 60, api: 40, args: 38
- `tests/test_blackd.py` (PYTHON) | Magnitude: 431.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 349, structural_boundaries: 172, concurrency: 123, args: 64
- `src/black/strings.py` (PYTHON) | Magnitude: 187.72 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, doc: 39, branch: 33, structural_boundaries: 32
- `tests/data/cases/no_blank_line_before_docstring.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 20, structural_boundaries: 16, api: 14, class_start: 10
- `tests/data/cases/module_docstring_followed_by_function.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 4, args: 2, func_start: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/black/brackets.py` -> **Hugo van Kemenade** (100.0% isolated ownership) | Magnitude: 527.12
- `src/blib2to3/pgen2/conv.py` -> **Gordon Messmer** (100.0% isolated ownership) | Magnitude: 271.92
- `scripts/migrate-black.py` -> **Hugo van Kemenade** (100.0% isolated ownership) | Magnitude: 171.76
- `tests/test_ipynb.py` -> **Jelle Zijlstra** (100.0% isolated ownership) | Magnitude: 160.92
- `src/black/output.py` -> **Hugo van Kemenade** (100.0% isolated ownership) | Magnitude: 155.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/black/debug.py` -> **Severity: 0.037** (Bridge: 0.0006 * Flux: 65.6296%)
- `src/black/ranges.py` -> **Severity: 0.033** (Bridge: 0.0003 * Flux: 93.5448%)
- `src/blib2to3/pytree.py` -> **Severity: 0.031** (Bridge: 0.0003 * Flux: 99.9531%)
- `src/black/parsing.py` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 71.3038%)
- `src/black/trans.py` -> **Severity: 0.011** (Bridge: 0.0002 * Flux: 55.8534%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/blib2to3/pgen2/grammar.py` -> **Severity: 2.907** (Embedded: 0.0363 * Error Risk: 80.0%)
- `src/black/output.py` -> **Severity: 2.51** (Embedded: 0.0377 * Error Risk: 66.5854%)
- `src/blib2to3/pytree.py` -> **Severity: 2.298** (Embedded: 0.0426 * Error Risk: 53.9411%)
- `src/black/debug.py` -> **Severity: 0.919** (Embedded: 0.0138 * Error Risk: 66.5854%)
- `tests/util.py` -> **Severity: 0.906** (Embedded: 0.0196 * Error Risk: 46.129%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/blib2to3/pytree.py` -> **Severity: 1475.8** (Blast Radius: 14.758 * Doc Risk: 100.0%)
- `src/black/output.py` -> **Severity: 1301.9** (Blast Radius: 13.019 * Doc Risk: 100.0%)
- `src/blib2to3/pgen2/grammar.py` -> **Severity: 1221.705** (Blast Radius: 12.246 * Doc Risk: 99.7636%)
- `src/black/mode.py` -> **Severity: 1030.993** (Blast Radius: 12.136 * Doc Risk: 84.9533%)
- `src/black/nodes.py` -> **Severity: 689.379** (Blast Radius: 10.688 * Doc Risk: 64.5003%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
