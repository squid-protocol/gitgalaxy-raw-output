# ARCHITECTURAL_BRIEF: asm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/asm` |
| **Timestamp** | `2026-08-03T19:26:44.535567+00:00` |
| **Scan Duration** | `0.17s` |
| **Git Branch** | `master` |
| **Git Commit** | `0b63ccb7aabbc575b9e80dba61f4cfddf9212a65` |
| **Git Remote** | `https://github.com/0xAX/asm.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 10 malicious artifacts.

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
| Total Artifacts | 63 |
| Analyzed Artifacts (Scanned) | 36 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 27 |
| Total LOC | 388 |
| Volatility Index | 0.194 |
| % Scanned of codebase = | 57.1% |
| Dominant Lang | ASSEMBLY |

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
| MARKDOWN | 18 | 0 | 50.0% |
| MAKEFILE | 8 | 42 | 22.2% |
| ASSEMBLY | 7 | 319 | 19.4% |
| C | 2 | 27 | 5.6% |
| PLAINTEXT | 1 | 0 | 2.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.567`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 10 | 27.8% |
| file_cluster_9 | 4 | 11.1% |
| file_cluster_17 | 2 | 5.6% |
| file_cluster_13 | 1 | 2.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 19 | 52.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 27*

**Composition by Extension & Reason:**
- `.svg`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 55.8 | 13.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 53.4 | 8.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.5 | 0.0 | 0.0 |
| Testing Exposure | 0.8 | 80.0 | 10.8 | 1.9 | 0.8 |
| API Exposure | 2.7 | 10.6 | 7.1 | 9.2 | 9.2 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 79.0 | 23.3 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 64.3 | 73.3 | 33.3 |
| Instability Exposure | 0.0 | 4.8 | 2.0 | 0.0 | 4.5 |
| Volatility Exposure | 0.0 | 100.0 | 28.0 | 9.0 | 9.0 |
| Documentation Exposure | 17.9 | 100.0 | 48.8 | 33.3 | 33.3 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 35.3 | 2.3 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 3.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `float/dot_product.asm` (Hits: 11)
- `stack/stack.asm` (Hits: 4)
- `strings/reverse.asm` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CODEOWNERS** (`CODEOWNERS`) — 0 inbound connections
2. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections
3. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
4. **CONTRIBUTORS.md** (`CONTRIBUTORS.md`) — 0 inbound connections
5. **README.md** (`README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **casm.c** (`casm/casm2/casm.c`) — 2 outbound dependencies
2. **casm.c** (`casm/casm3/casm.c`) — 2 outbound dependencies
3. **CODEOWNERS** (`CODEOWNERS`) — 0 outbound dependencies
4. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 outbound dependencies
5. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__repeat` (@ `stack/stack.asm`) -> Impact: **22.1** | LOC: 18
- `_parse_first_float_vector` (@ `float/dot_product.asm`) -> Impact: **18.7** | LOC: 35
  * *Intent:* ;; Parse the floating-point values from the input buffer.
- `_parse_second_float_vector` (@ `float/dot_product.asm`) -> Impact: **18.7** | LOC: 35
  * *Intent:* ;; Parse the floating-point values from the input buffer.
- `_calculate_dot_product` (@ `float/dot_product.asm`) -> Impact: **14.2** | LOC: 29
  * *Intent:* ;; Prepare to calculate the dot product of the two vectors.
- `int_to_str` (@ `stack/stack.asm`) -> Impact: **13.7** | LOC: 20
  * *Intent:* ;; Convert the sum to a string and print it to the standard output.
- `_loop` (@ `float/dot_product.asm`) -> Impact: **13.6** | LOC: 18
  * *Intent:* ;; Calculate the the dot product in the loop.
- `reverseStringAndPrint` (@ `strings/reverse.asm`) -> Impact: **13.5** | LOC: 15
  * *Intent:* ;; Calculate the length of the input string and prepare to reverse it.
- `reverseString` (@ `strings/reverse.asm`) -> Impact: **13.5** | LOC: 15
  * *Intent:* ;; Reverse the string and store it in the output buffer.
- `_start` (@ `stack/stack.asm`) -> Impact: **12.3** | LOC: 34
  * *Intent:* ;; Entry point
- `.loop` (@ `casm/casm3/casm.asm`) -> Impact: **11.1** | LOC: 9

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_parse_first_float_vector` (@ `float/dot_product.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ;; Parse the floating-point values from the input buffer.
- `_parse_second_float_vector` (@ `float/dot_product.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ;; Parse the floating-point values from the input buffer.
- `_loop` (@ `float/dot_product.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ;; Calculate the the dot product in the loop.
- `__repeat` (@ `stack/stack.asm`) -> **O(2^N) [Recursive]**
- `int_to_str` (@ `stack/stack.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ;; Convert the sum to a string and print it to the standard output.
- `reverseStringAndPrint` (@ `strings/reverse.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ;; Calculate the length of the input string and prepare to reverse it.
- `reverseString` (@ `strings/reverse.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ;; Reverse the string and store it in the output buffer.

### Highest Data Gravity (Database Complexity)
- `_read_first_float_vector` (@ `float/dot_product.asm`) -> DB Complexity: **9**
  * *Intent:* ;; Read the first input string with floating-point values
- `_read_second_float_vector` (@ `float/dot_product.asm`) -> DB Complexity: **9**
  * *Intent:* ;; Read the second input string with floating-point values
- `printResult` (@ `strings/reverse.asm`) -> DB Complexity: **9**
  * *Intent:* ;; Print the reversed string to the standard output.
- `_start` (@ `hello/hello.asm`) -> DB Complexity: **6**
  * *Intent:* ;; Entry point
- `printResult` (@ `stack/stack.asm`) -> DB Complexity: **6**
  * *Intent:* ;; Print the result to the standard output.
- `_error` (@ `float/dot_product.asm`) -> DB Complexity: **3**
  * *Intent:* ;; Print an error and exit.
- `_error_empty` (@ `float/dot_product.asm`) -> DB Complexity: **3**
  * *Intent:* ;; Print an error and exit.
- `_exit` (@ `float/dot_product.asm`) -> DB Complexity: **3**
  * *Intent:* ;; Exit from the program.
- `ERROR_MSG` (@ `float/dot_product.asm`) -> DB Complexity: **3**
  * *Intent:* ;; Error message to print if the number of items in the vectors is not the same. ;; `10` is the ASCII code of the new line symbol. `0` is the NUL term...
- `argcError` (@ `stack/stack.asm`) -> DB Complexity: **3**
  * *Intent:* ;; Print the error message if not enough command-line arguments.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `float` | 3 | 127.24 | 8.85% | 0.0% |
| `stack` | 3 | 86.18 | 11.36% | 0.0% |
| `strings` | 3 | 61.74 | 20.27% | 0.0% |
| `content` | 7 | 61.36 | 0.0% | 0.0% |
| `casm/casm3` | 3 | 44.16 | 5.0% | 66.67% |
| `sum` | 3 | 27.1 | 6.73% | 33.33% |
| `casm/casm1` | 2 | 24.46 | 5.0% | 0.0% |
| `casm/casm2` | 2 | 23.62 | 27.5% | 49.95% |
| `hello` | 3 | 19.86 | 3.33% | 0.0% |
| `__monolith__` | 6 | 8.66 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `casm/casm3/casm.asm` -> **100.0%** Exposure
- `casm/casm3/casm.c` -> **99.9985%** Exposure
- `sum/sum.asm` -> **99.9972%** Exposure
- `casm/casm2/casm.c` -> **99.8968%** Exposure
### Highest State Flux (Mutation/Volatility)
- `casm/casm3/casm.asm` -> **99.9851%** Exposure
- `casm/casm2/casm.c` -> **99.4622%** Exposure
- `strings/reverse.asm` -> **95.2862%** Exposure
- `stack/stack.asm` -> **44.816%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `casm/casm3/casm.asm` -> **2** Orphaned Functions | **0** Duplicates
- `sum/sum.asm` -> **2** Orphaned Functions | **0** Duplicates
- `casm/casm2/casm.c` -> **1** Orphaned Functions | **0** Duplicates
- `casm/casm3/casm.c` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`casm/casm2/casm.c`** -> AI Confidence: **98.96%**
2. **`casm/casm3/casm.c`** -> AI Confidence: **98.85%**
3. **`casm/casm1/Makefile`** -> AI Confidence: **98.84%**
4. **`casm/casm2/Makefile`** -> AI Confidence: **98.84%**
5. **`casm/casm3/Makefile`** -> AI Confidence: **98.84%**
6. **`float/Makefile`** -> AI Confidence: **98.84%**
7. **`hello/Makefile`** -> AI Confidence: **98.84%**
8. **`stack/Makefile`** -> AI Confidence: **98.84%**
9. **`strings/Makefile`** -> AI Confidence: **98.84%**
10. **`sum/Makefile`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `float/dot_product.asm` -> **20.0%** Exposure
- `stack/stack.asm` -> **20.0%** Exposure
- `strings/reverse.asm` -> **19.9566%** Exposure
### Weaponizable Injection Vectors
- `float/dot_product.asm` -> **100.0%** Exposure
- `strings/reverse.asm` -> **99.9997%** Exposure
- `stack/stack.asm` -> **99.998%** Exposure
### Algorithmic DoS Exposure
- `float/dot_product.asm` -> **100.0%** Exposure
- `strings/reverse.asm` -> **100.0%** Exposure
- `casm/casm2/casm.c` -> **100.0%** Exposure
- `stack/stack.asm` -> **99.992%** Exposure
- `hello/hello.asm` -> **98.7059%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `strings/reverse.asm` (ASSEMBLY) -> Cumulative Risk: **666.35**
- **Archetype:** `file_cluster_17` (Distance: 18.345 IQR)
- **Magnitude:** 46.14 | **LOC:** 104 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.9997%), State Flux (95.2862%)
- **Heaviest Functions:** `reverseStringAndPrint` (Impact: 13.5), `reverseString` (Impact: 13.5), `_start` (Impact: 4.7)

### 2. `stack/stack.asm` (ASSEMBLY) -> Cumulative Risk: **650.75**
- **Archetype:** `file_cluster_17` (Distance: 16.663 IQR)
- **Magnitude:** 70.58 | **LOC:** 164 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (99.998%), Algorithmic Dos (99.992%), Verification (80.0%)
- **Heaviest Functions:** `__repeat` (Impact: 22.1), `int_to_str` (Impact: 13.7), `_start` (Impact: 12.3)

### 3. `casm/casm2/casm.c` (C) -> Cumulative Risk: **612.76**
- **Archetype:** `file_cluster_13` (Distance: 15.508 IQR)
- **Magnitude:** 9.02 | **LOC:** 20 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.8968%)
- **Heaviest Functions:** `main` (Impact: 1.7)

### 4. `float/dot_product.asm` (ASSEMBLY) -> Cumulative Risk: **607.0**
- **Archetype:** `file_cluster_9` (Distance: 16.713 IQR)
- **Magnitude:** 111.64 | **LOC:** 333 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `_parse_first_float_vector` (Impact: 18.7), `_parse_second_float_vector` (Impact: 18.7), `_calculate_dot_product` (Impact: 14.2)

### 5. `sum/sum.asm` (ASSEMBLY) -> Cumulative Risk: **470.75**
- **Archetype:** `file_cluster_9` (Distance: 15.945 IQR)
- **Magnitude:** 11.5 | **LOC:** 54 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9972%), Documentation (77.2808%), Dead Code (58.257%)
- **Heaviest Functions:** `.correctSum` (Impact: 4.9), `.compare` (Impact: 3.2), `_start` (Impact: 1.9)

### 6. `casm/casm3/casm.asm` (ASSEMBLY) -> Cumulative Risk: **442.0**
- **Archetype:** `file_cluster_8` (Distance: 10.906 IQR)
- **Magnitude:** 20.12 | **LOC:** 23 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (99.9851%), Spec Match (73.3333%), Documentation (73.3333%)
- **Heaviest Functions:** `.loop` (Impact: 11.1), `.done` (Impact: 3.1), `my_strlen` (Impact: 1.7)

### 7. `hello/hello.asm` (ASSEMBLY) -> Cumulative Risk: **430.5**
- **Archetype:** `file_cluster_9` (Distance: 19.195 IQR)
- **Magnitude:** 4.26 | **LOC:** 31 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Algorithmic Dos (98.7059%), Spec Match (86.6667%), Documentation (86.6667%), Churn (82.71%)
- **Heaviest Functions:** `_start` (Impact: 3.0)

### 8. `casm/casm1/casm.asm` (ASSEMBLY) -> Cumulative Risk: **311.76**
- **Archetype:** `file_cluster_9` (Distance: 19.598 IQR)
- **Magnitude:** 9.34 | **LOC:** 30 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (80.0%), Documentation (80.0%), Churn (71.24%), Dead Code (64.5656%)
- **Heaviest Functions:** `_start` (Impact: 7.1)

### 9. `casm/casm3/casm.c` (C) -> Cumulative Risk: **286.34**
- **Archetype:** `file_cluster_8` (Distance: 8.666 IQR)
- **Magnitude:** 8.92 | **LOC:** 16 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (99.9985%), Spec Match (73.3333%), Documentation (73.3333%), Api Exposure (9.786%)
- **Heaviest Functions:** `main` (Impact: 5.7)

### 10. `casm/casm1/Makefile` (MAKEFILE) -> Cumulative Risk: **108.61**
- **Archetype:** `file_cluster_8` (Distance: 7.378 IQR)
- **Magnitude:** 15.12 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (40.0%), Documentation (40.0%), Api Exposure (9.1631%), Churn (9.03%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `float/dot_product.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 16.713 IQR)
- **Top Global Matches:** file_cluster_9: 16.713, file_cluster_17: 16.752, file_cluster_0: 16.754
- **Magnitude:** 111.64 | **LOC:** 333 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (21.5483%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_parse_first_float_vector` (Impact: 18.7 | O(2^N) | DB: 1)
    * *Intent:* ;; Parse the floating-point values from the input buffer.
  * `_parse_second_float_vector` (Impact: 18.7 | O(2^N) | DB: 1)
    * *Intent:* ;; Parse the floating-point values from the input buffer.
  * `_calculate_dot_product` (Impact: 14.2 | O(N^2))
    * *Intent:* ;; Prepare to calculate the dot product of the two vectors.
  * `_loop` (Impact: 13.6 | O(2^N))
    * *Intent:* ;; Calculate the the dot product in the loop.
  * `_error` (Impact: 4.9 | O(N^2) | DB: 3)
    * *Intent:* ;; Print an error and exit.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 58`, `args: 67`, `func_start: 22`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `dead_code: 11`
* *Architecture:* `io: 11`, `api: 2`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stack/stack.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.663 IQR)
- **Top Global Matches:** file_cluster_17: 16.663, file_cluster_9: 16.666, file_cluster_0: 16.694
- **Magnitude:** 70.58 | **LOC:** 164 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (29.072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__repeat` (Impact: 22.1 | O(2^N) | DB: 1)
  * `int_to_str` (Impact: 13.7 | O(2^N) | DB: 1)
    * *Intent:* ;; Convert the sum to a string and print it to the standard output.
  * `_start` (Impact: 12.3 | O(N^2))
    * *Intent:* ;; Entry point
  * `argcError` (Impact: 4.9 | O(N^2) | DB: 3)
    * *Intent:* ;; Print the error message if not enough command-line arguments.
  * `printResult` (Impact: 3.6 | O(N^2) | DB: 6)
    * *Intent:* ;; Print the result to the standard output.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 37`, `args: 30`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `dead_code: 6`
* *Architecture:* `io: 4`, `api: 1`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `strings/reverse.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 18.345 IQR)
- **Top Global Matches:** file_cluster_17: 18.345, file_cluster_9: 18.349, file_cluster_0: 18.372
- **Magnitude:** 46.14 | **LOC:** 104 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (55.8245%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `reverseStringAndPrint` (Impact: 13.5 | O(2^N) | DB: 1)
    * *Intent:* ;; Calculate the length of the input string and prepare to reverse it.
  * `reverseString` (Impact: 13.5 | O(2^N) | DB: 2)
    * *Intent:* ;; Reverse the string and store it in the output buffer.
  * `_start` (Impact: 4.7 | O(N^2))
    * *Intent:* ;; Entry point of the program.
  * `printResult` (Impact: 3.5 | O(N^2) | DB: 9)
    * *Intent:* ;; Print the reversed string to the standard output.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 18`, `args: 18`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 9`, `dead_code: 5`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm3/casm.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.906 IQR)
- **Top Global Matches:** file_cluster_8: 10.906, file_cluster_7: 11.526, file_cluster_13: 11.694
- **Magnitude:** 20.12 | **LOC:** 23 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `.loop` (Impact: 11.1 | O(N^2) | DB: 1)
  * `.done` (Impact: 3.1 | O(N^2))
  * `my_strlen` (Impact: 1.7 | O(N^2))
    * *Intent:* ;; Function that returns the length of the string passed in the first argument
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 1`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 2`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm1/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.378 IQR)
- **Top Global Matches:** file_cluster_8: 7.378, file_cluster_7: 8.405, file_cluster_1: 8.542
- **Magnitude:** 15.12 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm3/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.378 IQR)
- **Top Global Matches:** file_cluster_8: 7.378, file_cluster_7: 8.405, file_cluster_1: 8.542
- **Magnitude:** 15.12 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm2/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.608 IQR)
- **Top Global Matches:** file_cluster_8: 7.608, file_cluster_7: 8.6, file_cluster_1: 8.738
- **Magnitude:** 14.6 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `float/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.1 IQR)
- **Top Global Matches:** file_cluster_8: 7.1, file_cluster_7: 8.159, file_cluster_1: 8.32
- **Magnitude:** 14.6 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hello/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.098 IQR)
- **Top Global Matches:** file_cluster_8: 7.098, file_cluster_7: 8.157, file_cluster_1: 8.319
- **Magnitude:** 14.6 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stack/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.098 IQR)
- **Top Global Matches:** file_cluster_8: 7.098, file_cluster_7: 8.157, file_cluster_1: 8.319
- **Magnitude:** 14.6 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `strings/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.098 IQR)
- **Top Global Matches:** file_cluster_8: 7.098, file_cluster_7: 8.157, file_cluster_1: 8.319
- **Magnitude:** 14.6 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sum/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.098 IQR)
- **Top Global Matches:** file_cluster_8: 7.098, file_cluster_7: 8.157, file_cluster_1: 8.319
- **Magnitude:** 14.6 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_3.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 12.78 | **LOC:** 639 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_6.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 11.94 | **LOC:** 597 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sum/sum.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 15.945 IQR)
- **Top Global Matches:** file_cluster_9: 15.945, file_cluster_0: 15.998, file_cluster_17: 16.068
- **Magnitude:** 11.5 | **LOC:** 54 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (15.1871%), Tech Debt (99.9972%)
**Top Internal Functions/Classes:**
  * `.correctSum` (Impact: 4.9 | O(N^2) | DB: 3)
    * *Intent:* ;; Print a message that the sum is correct
  * `.compare` (Impact: 3.2 | O(N^2))
  * `_start` (Impact: 1.9 | O(N^2))
    * *Intent:* ;; Entry point
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 4`, `func_start: 4`
* *Risk/State:* `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_2.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 10.08 | **LOC:** 504 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm1/casm.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 19.598 IQR)
- **Top Global Matches:** file_cluster_9: 19.598, file_cluster_0: 19.677, file_cluster_6: 19.707
- **Magnitude:** 9.34 | **LOC:** 30 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_start` (Impact: 7.1 | O(N^2))
    * *Intent:* ;; Entry point
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 4`, `args: 4`, `func_start: 1`
* *Risk/State:* `dead_code: 2`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_5.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 9.04 | **LOC:** 452 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm2/casm.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.508 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.494 IQR)
- **Top Global Matches:** file_cluster_13: 15.508, file_cluster_0: 15.783, file_cluster_11: 15.815
- **Magnitude:** 9.02 | **LOC:** 20 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (99.8968%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 1.7 | O(N^2) | DB: 3)
    * *Intent:* #include <stdio.h> #include <string.h>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm3/casm.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.666 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.108 IQR)
- **Top Global Matches:** file_cluster_8: 8.666, file_cluster_13: 8.88, file_cluster_7: 9.523
- **Magnitude:** 8.92 | **LOC:** 16 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (99.9985%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 5.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `args: 2`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdlib.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_4.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 6.42 | **LOC:** 321 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_1.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.66 | **LOC:** 283 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_7.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.44 | **LOC:** 272 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hello/hello.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 19.195 IQR)
- **Top Global Matches:** file_cluster_9: 19.195, file_cluster_0: 19.294, file_cluster_6: 19.333
- **Magnitude:** 4.26 | **LOC:** 31 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_start` (Impact: 3.0 | O(N^2) | DB: 6)
    * *Intent:* ;; Entry point
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 4`, `func_start: 1`
* *Risk/State:* `dead_code: 2`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CODE_OF_CONDUCT.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.58 | **LOC:** 129 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `casm/casm2/casm.c` (C) | Magnitude: 9.02 | Delta: **0.275 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, branch: 4, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `stack/stack.asm` (ASSEMBLY) | Magnitude: 70.58 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 37, args: 30, branch: 12
- `strings/reverse.asm` (ASSEMBLY) | Magnitude: 46.14 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 18, args: 18, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `casm/casm3/casm.c` (C) | Magnitude: 8.92 | Delta: **0.214 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, api: 3, structural_boundaries: 2, args: 2
- `casm/casm3/casm.asm` (ASSEMBLY) | Magnitude: 20.12 | Delta: **0.62 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 7, branch: 5, func_start: 3, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `float/dot_product.asm` (ASSEMBLY) | Magnitude: 111.64 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 123, args: 67, structural_boundaries: 58, func_start: 22
- `sum/sum.asm` (ASSEMBLY) | Magnitude: 11.5 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 9, args: 4, func_start: 4
- `casm/casm1/casm.asm` (ASSEMBLY) | Magnitude: 9.34 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 4, args: 4, branch: 2
- `hello/hello.asm` (ASSEMBLY) | Magnitude: 4.26 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, args: 4, sec_high_risk_execution: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `sum/sum.asm` -> Churn: **56.46%** | Cog Load: 15.1871% | Debt: 99.9972%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `float/dot_product.asm` -> **Alex Kuleshov** (100.0% isolated ownership) | Magnitude: 111.64
- `stack/stack.asm` -> **Alex Kuleshov** (100.0% isolated ownership) | Magnitude: 70.58

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `casm/casm2/casm.c` -> **Severity: 2777.8** (Blast Radius: 27.778 * Doc Risk: 100.0%)
- `hello/hello.asm` -> **Severity: 2407.428** (Blast Radius: 27.778 * Doc Risk: 86.6667%)
- `casm/casm1/casm.asm` -> **Severity: 2222.24** (Blast Radius: 27.778 * Doc Risk: 80.0%)
- `sum/sum.asm` -> **Severity: 2146.706** (Blast Radius: 27.778 * Doc Risk: 77.2808%)
- `casm/casm3/casm.asm` -> **Severity: 2037.052** (Blast Radius: 27.778 * Doc Risk: 73.3333%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
