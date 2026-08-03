# ARCHITECTURAL_BRIEF: cli
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/cli` |
| **Timestamp** | `2026-08-03T19:54:04.024960+00:00` |
| **Scan Duration** | `4.44s` |
| **Git Branch** | `latest` |
| **Git Commit** | `63b9a7c1a65361eb2e082d5f4aff267df52ba817` |
| **Git Remote** | `https://github.com/npm/cli.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 148 malicious artifacts.

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
| Total Artifacts | 6752 |
| Analyzed Artifacts (Scanned) | 676 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6076 |
| Total LOC | 17949 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 10.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6285 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.425 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9286 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 488 | 1 | 72.2% |
| JAVASCRIPT | 136 | 16757 | 20.1% |
| MARKDOWN | 28 | 0 | 4.1% |
| HTML | 10 | 663 | 1.5% |
| SHELL | 7 | 259 | 1.0% |
| BATCH | 3 | 37 | 0.4% |
| JSON | 2 | 152 | 0.3% |
| POWERSHELL | 2 | 80 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.188`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 106 | 15.7% |
| file_cluster_4 | 22 | 3.3% |
| file_cluster_13 | 18 | 2.7% |
| file_cluster_17 | 9 | 1.3% |
| file_cluster_11 | 2 | 0.3% |
| file_cluster_15 | 2 | 0.3% |
| Unknown | 1 | 0.1% |
| file_cluster_9 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 515 | 76.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6076*

**Composition by Extension & Reason:**
- `.json`: 3468x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14810 LOC)
- `.js`: 1253x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tgz`: 783x Excluded (Explicitly Denied Extension: '.tgz')
- `.md`: 202x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 8 LOC), 1x Excluded (Machine-Generated Source Code Signature: 736 LOC)
- `no_extension`: 162x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1657 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3841 LOC)
- `.py`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmd`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 34.3 | 18.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 96.5 | 13.5 | 4.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.9 | 0.4 | 0.0 |
| API Exposure | 0.0 | 17.3 | 2.0 | 0.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 47.3 | 26.8 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 18.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 30.8 | 1.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.4 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 38.3 | 4.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 29.8 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `workspaces/config/test/index.js` (Hits: 188)
- `workspaces/libnpmfund/test/index.js` (Hits: 102)
- `test/lib/utils/get-workspaces.js` (Hits: 43)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **package-json.hbs** (`scripts/template-oss/package-json.hbs`) — 6 inbound connections
2. **format.js** (`lib/utils/format.js`) — 2 inbound connections
3. **cmd-list.js** (`lib/utils/cmd-list.js`) — 1 inbound connections
4. **util.js** (`scripts/util.js`) — 1 inbound connections
5. **logging.js** (`workspaces/arborist/bin/lib/logging.js`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`workspaces/arborist/lib/arborist/index.js`) — 17 outbound dependencies
2. **index.js** (`workspaces/libnpmexec/lib/index.js`) — 17 outbound dependencies
3. **index.js** (`workspaces/config/lib/index.js`) — 16 outbound dependencies
4. **create-node-pr.js** (`scripts/create-node-pr.js`) — 12 outbound dependencies
5. **error-message.js** (`lib/utils/error-message.js`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `hasOwnProperty` (@ `workspaces/config/lib/index.js`) -> Impact: **242.3** | LOC: 170
- `readTree` (@ `workspaces/libnpmfund/lib/index.js`) -> Impact: **170.5** | LOC: 154
- `errorMessage` (@ `lib/utils/error-message.js`) -> Impact: **149.9** | LOC: 88
- `repair` (@ `workspaces/config/lib/index.js`) -> Impact: **111.9** | LOC: 212
- `spawn` (@ `scripts/util.js`) -> Impact: **82.5** | LOC: 57
- `sortAlphabetically` (@ `lib/utils/verify-signatures.js`) -> Impact: **77.1** | LOC: 156
- `depth` (@ `lib/utils/reify-output.js`) -> Impact: **63.3** | LOC: 54
- `exec` (@ `workspaces/libnpmexec/lib/index.js`) -> Impact: **56.8** | LOC: 97
- `iterate` (@ `scripts/dependency-graph.js`) -> Impact: **54.5** | LOC: 16
- `Anonymous_Block` (@ `lib/utils/completion.sh`) -> Impact: **52.0** | LOC: 60
  * *Intent:* #!/bin/bash ###-begin-npm-completion-### # # npm command completion script # # Installation: npm completion >> ~/.bashrc (or ~/.zshrc) # Or, maybe: np...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `hasOwnProperty` (@ `workspaces/config/lib/index.js`) -> **O(2^N) [Recursive]**
- `normalizePath` (@ `workspaces/libnpmdiff/test/index.js`) -> **O(2^N) [Recursive]**
- `errorMessage` (@ `lib/utils/error-message.js`) -> **O(2^N) [Recursive]**
- `filter` (@ `lib/utils/format-search-stream.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // This module consumes package data in the following format: // // { // name: String, // description: String, // maintainers: [{ username: String, em...
- `parseKeys` (@ `lib/utils/queryable.js`) -> **O(2^N) [Recursive]**
- `query` (@ `lib/utils/queryable.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // empty-bracket-shortcut-syntax is not supported on getter
- `reset` (@ `mock-globals/test/index.js`) -> **O(2^N) [Recursive]**
- `exists` (@ `mock-registry/lib/index.js`) -> **O(2^N) [Recursive]**
- `iterate` (@ `scripts/dependency-graph.js`) -> **O(2^N) [Recursive]**
- `readFile` (@ `smoke-tests/test/index.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `sortAlphabetically` (@ `lib/utils/verify-signatures.js`) -> DB Complexity: **41**
- `Anonymous_Block` (@ `lib/utils/completion.sh`) -> DB Complexity: **38**
  * *Intent:* #!/bin/bash ###-begin-npm-completion-### # # npm command completion script # # Installation: npm completion >> ~/.bashrc (or ~/.zshrc) # Or, maybe: np...
- `getCases` (@ `test/lib/utils/explain-dep.js`) -> DB Complexity: **30**
- `depth` (@ `lib/utils/reify-output.js`) -> DB Complexity: **27**
- `getContents` (@ `lib/utils/tar.js`) -> DB Complexity: **27**
- `hasOwnProperty` (@ `workspaces/config/lib/index.js`) -> DB Complexity: **25**
- `repair` (@ `workspaces/config/lib/index.js`) -> DB Complexity: **23**
- `errorMessage` (@ `lib/utils/error-message.js`) -> DB Complexity: **20**
- `exec` (@ `workspaces/libnpmexec/lib/index.js`) -> DB Complexity: **20**
- `padZero` (@ `lib/utils/log-file.js`) -> DB Complexity: **18**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 10 | 5111.72 | 9.98% | 10.0% |
| `lib/utils` | 35 | 1934.22 | 48.08% | 28.81% |
| `test/lib/utils` | 21 | 873.58 | 32.78% | 0.0% |
| `scripts` | 13 | 681.55 | 60.37% | 29.48% |
| `workspaces/config/lib` | 1 | 575.58 | 67.97% | 13.32% |
| `mock-registry/lib` | 1 | 513.02 | 94.77% | 46.59% |
| `bin` | 9 | 437.54 | 53.5% | 29.71% |
| `workspaces/arborist/lib/arborist` | 1 | 261.8 | 98.74% | 67.39% |
| `workspaces/arborist/scripts` | 2 | 245.52 | 49.81% | 32.57% |
| `workspaces/config/test` | 1 | 243.62 | 19.39% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bin/node-gyp-bin/node-gyp` -> **100.0%** Exposure
- `bin/npm` -> **100.0%** Exposure
- `bin/npx` -> **100.0%** Exposure
- `configure` -> **100.0%** Exposure
- `lib/utils/ping.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/npm` -> **100.0%** Exposure
- `bin/npx` -> **100.0%** Exposure
- `configure` -> **100.0%** Exposure
- `lib/utils/completion.sh` -> **100.0%** Exposure
- `scripts/smoke-tests.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `workspaces/libnpmfund/test/index.js` -> **0** Orphaned Functions | **31** Duplicates
- `workspaces/libnpmteam/test/index.js` -> **0** Orphaned Functions | **22** Duplicates
- `mock-globals/test/index.js` -> **0** Orphaned Functions | **14** Duplicates
- `test/lib/utils/get-workspaces.js` -> **0** Orphaned Functions | **12** Duplicates
- `bin/npx` -> **1** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`lib/utils/error-message.js`** -> AI Confidence: **99.48%**
2. **`lib/utils/reify-output.js`** -> AI Confidence: **99.34%**
3. **`lib/utils/verify-signatures.js`** -> AI Confidence: **99.31%**
4. **`mock-registry/lib/index.js`** -> AI Confidence: **99.31%**
5. **`scripts/util.js`** -> AI Confidence: **99.31%**
6. **`workspaces/arborist/lib/arborist/index.js`** -> AI Confidence: **99.31%**
7. **`workspaces/arborist/test/index.js`** -> AI Confidence: **99.31%**
8. **`workspaces/config/lib/index.js`** -> AI Confidence: **99.31%**
9. **`workspaces/libnpmexec/lib/index.js`** -> AI Confidence: **99.31%**
10. **`bin/node-gyp-bin/node-gyp`** -> AI Confidence: **99.29%**
11. **`bin/npm`** -> AI Confidence: **99.29%**
12. **`bin/npx`** -> AI Confidence: **99.29%**
13. **`index.js`** -> AI Confidence: **99.29%**
14. **`lib/utils/is-windows.js`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `test/lib/utils/display.js` -> **0.0891%** Exposure
### Exploit Generation Surface
- `lib/utils/completion.sh` -> **100.0%** Exposure
- `lib/utils/reify-output.js` -> **100.0%** Exposure
- `lib/utils/verify-signatures.js` -> **100.0%** Exposure
- `mock-registry/lib/index.js` -> **100.0%** Exposure
- `scripts/util.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `scripts/util.js` -> **100.0%** Exposure
- `test/index.js` -> **100.0%** Exposure
- `workspaces/arborist/scripts/benchmark.js` -> **100.0%** Exposure
- `workspaces/arborist/scripts/benchmark/reify.js` -> **100.0%** Exposure
- `workspaces/config/lib/index.js` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `mock-registry/lib/index.js` -> **99.9995%** Exposure
- `workspaces/config/test/index.js` -> **14.6493%** Exposure
### Algorithmic DoS Exposure
- `lib/utils/completion.sh` -> **100.0%** Exposure
- `lib/utils/error-message.js` -> **100.0%** Exposure
- `lib/utils/log-file.js` -> **100.0%** Exposure
- `lib/utils/reify-output.js` -> **100.0%** Exposure
- `lib/utils/tar.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `309` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `mock-registry/lib/index.js` (JAVASCRIPT) -> Cumulative Risk: **941.06**
- **Archetype:** `file_cluster_8` (Distance: 12.389 IQR)
- **Magnitude:** 513.02 | **LOC:** 674 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.9997%)
- **Heaviest Functions:** `exists` (Impact: 48.1), `noMatch` (Impact: 37.3), `putPackagePayload` (Impact: 36.4)

### 2. `workspaces/arborist/lib/arborist/index.js` (JAVASCRIPT) -> Cumulative Risk: **870.05**
- **Archetype:** `file_cluster_4` (Distance: 12.967 IQR)
- **Magnitude:** 261.8 | **LOC:** 311 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `workspaceDependencySet` (Impact: 49.6), `excludeWorkspacesDependencySet` (Impact: 28.9), `lockfileVersion` (Impact: 21.3)

### 3. `workspaces/config/lib/index.js` (JAVASCRIPT) -> Cumulative Risk: **849.53**
- **Archetype:** `file_cluster_4` (Distance: 13.621 IQR)
- **Magnitude:** 575.58 | **LOC:** 1035 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `hasOwnProperty` (Impact: 242.3), `repair` (Impact: 111.9)

### 4. `workspaces/arborist/scripts/benchmark.js` (JAVASCRIPT) -> Cumulative Risk: **826.49**
- **Archetype:** `file_cluster_4` (Distance: 12.193 IQR)
- **Magnitude:** 244.52 | **LOC:** 209 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `usage` (Impact: 37.8), `onCycle` (Impact: 30.0), `onStart` (Impact: 19.4)

### 5. `lib/utils/verify-signatures.js` (JAVASCRIPT) -> Cumulative Risk: **804.32**
- **Archetype:** `file_cluster_4` (Distance: 12.498 IQR)
- **Magnitude:** 231.94 | **LOC:** 393 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 20.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `sortAlphabetically` (Impact: 77.1)

### 6. `lib/utils/completion.sh` (SHELL) -> Cumulative Risk: **786.18**
- **Archetype:** `file_cluster_8` (Distance: 12.632 IQR)
- **Magnitude:** 94.58 | **LOC:** 71 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 52.0), `__global_context__` (Impact: 1.4)

### 7. `lib/utils/reify-output.js` (JAVASCRIPT) -> Cumulative Risk: **741.77**
- **Archetype:** `file_cluster_8` (Distance: 12.02 IQR)
- **Magnitude:** 142.94 | **LOC:** 221 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `depth` (Impact: 63.3), `getAuditReport` (Impact: 16.8), `printAuditReport` (Impact: 5.5)

### 8. `workspaces/arborist/scripts/benchmark/reify.js` (JAVASCRIPT) -> Cumulative Risk: **709.45**
- **Archetype:** `file_cluster_4` (Distance: 9.698 IQR)
- **Magnitude:** 54.28 | **LOC:** 115 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setup` (Impact: 10.9), `fn` (Impact: 6.4), `writeFileSync` (Impact: 3.7)

### 9. `workspaces/arborist/bin/funding.js` (JAVASCRIPT) -> Cumulative Risk: **632.45**
- **Archetype:** `file_cluster_4` (Distance: 10.31 IQR)
- **Magnitude:** 17.82 | **LOC:** 39 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (99.9942%), Tech Debt (99.8968%)
- **Heaviest Functions:** `exports` (Impact: 7.5)

### 10. `lib/utils/error-message.js` (JAVASCRIPT) -> Cumulative Risk: **622.68**
- **Archetype:** `file_cluster_17` (Distance: 12.291 IQR)
- **Magnitude:** 185.4 | **LOC:** 454 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (89.7216%)
- **Heaviest Functions:** `errorMessage` (Impact: 149.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/config/lib/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.621 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.612 IQR)
- **Top Global Matches:** file_cluster_4: 13.621, file_cluster_13: 13.909, file_cluster_11: 13.994
- **Magnitude:** 575.58 | **LOC:** 1035 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (67.9699%), Tech Debt (13.319%)
**Top Internal Functions/Classes:**
  * `hasOwnProperty` (Impact: 242.3 | O(2^N) | DB: 25)
  * `repair` (Impact: 111.9 | O(N^2) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 56`, `args: 35`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `state_mutation: 145`, `dead_code: 4`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 67`, `import: 15`
* *Defense:* `safety: 18`, `immutability_locks: 54`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` parse-field.js, ini, env-replace.js, promises, package-json, walk-up-path, node:path, type-defs.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mock-registry/lib/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.389 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.691 IQR)
- **Top Global Matches:** file_cluster_8: 12.389, file_cluster_4: 12.421, file_cluster_13: 12.498
- **Magnitude:** 513.02 | **LOC:** 674 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (94.7741%), Tech Debt (46.5914%)
**Top Internal Functions/Classes:**
  * `exists` (Impact: 48.1 | O(2^N) | DB: 14)
  * `noMatch` (Impact: 37.3 | O(N^2) | DB: 9)
  * `putPackagePayload` (Impact: 36.4 | O(N^3) | DB: 6)
  * `setup` (Impact: 29.9 | O(N^3) | DB: 4)
  * `startNock` (Impact: 9.9 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 59`, `args: 55`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 212`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 15`, `api: 24`, `concurrency: 30`, `import: 8`
* *Defense:* `safety: 12`, `doc: 1`, `test: 1`, `immutability_locks: 63`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nock, arborist, promises, npm-package-arg, json-stringify-safe, node:path, node:fs, pacote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/arborist/lib/arborist/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.967 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_4: 12.967, file_cluster_11: 13.438, file_cluster_17: 13.54
- **Magnitude:** 261.8 | **LOC:** 311 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (98.7399%), Tech Debt (67.3884%)
**Top Internal Functions/Classes:**
  * `workspaceDependencySet` (Impact: 49.6 | O(N^3) | DB: 6)
  * `excludeWorkspacesDependencySet` (Impact: 28.9 | O(N^3) | DB: 1)
  * `lockfileVersion` (Impact: 21.3 | O(2^N))
    * *Intent:* // The arborist manages three trees: // - actual // - virtual // - ideal // // The actual tree is wh...
  * `workspaceNodes` (Impact: 19.6 | O(N^2) | DB: 10)
  * `constructor` (Impact: 1.1 | O(N^1))
    * *Intent:* // // The virtual tree is loaded from metadata (package.json and lock files). // // The ideal tree i...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 26`, `args: 12`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 93`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 3`, `concurrency: 40`
* *Defense:* `safety: 8`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` reify.js, node:events, load-actual.js, load-virtual.js, tracker.js, node:path, add-rm-pkg-deps.js, audit-report.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/arborist/scripts/benchmark.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.193 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 6.073 IQR)
- **Top Global Matches:** file_cluster_4: 12.193, file_cluster_13: 12.648, file_cluster_17: 12.742
- **Magnitude:** 244.52 | **LOC:** 209 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (99.611%), Tech Debt (65.1355%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 37.8 | O(N^5) | DB: 3)
  * `onCycle` (Impact: 30.0 | O(N^2) | DB: 2)
  * `onStart` (Impact: 19.4 | O(N^2) | DB: 10)
  * `main` (Impact: 6.2 | O(N^1) | DB: 2)
  * `onComplete` (Impact: 5.2 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 21`, `args: 14`, `func_start: 16`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 66`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 3`, `concurrency: 64`, `import: 8`
* *Defense:* `safety: 5`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:child_process, node:path, benchmark, node:fs, server.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/config/test/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.415 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.698 IQR)
- **Top Global Matches:** file_cluster_8: 9.415, file_cluster_4: 10.022, file_cluster_17: 10.177
- **Magnitude:** 243.62 | **LOC:** 1871 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (19.3936%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `readFileSync` (Impact: 7.3 | O(2^N) | DB: 12)
  * `readFile` (Impact: 7.3 | O(2^N) | DB: 12)
  * `logHandler` (Impact: 5.3 | O(2^N) | DB: 14)
  * `logHandler` (Impact: 5.2 | O(2^N) | DB: 14)
  * `logHandler` (Impact: 4.8 | O(2^N) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 219`, `args: 138`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 16`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 188`, `concurrency: 141`, `import: 6`
* *Defense:* `safety: 27`, `test: 5`, `sync_locks: 1`, `immutability_locks: 192`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:path, .., type-defs.js, definition.js, node:fs, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/libnpmfund/lib/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.337 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.596 IQR)
- **Top Global Matches:** file_cluster_17: 11.337, file_cluster_8: 11.607, file_cluster_0: 11.622
- **Magnitude:** 236.7 | **LOC:** 211 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (37.1684%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `readTree` (Impact: 170.5 | O(N^3) | DB: 6)
  * `isValidFunding` (Impact: 37.2 | O(2^N) | DB: 7)
    * *Intent:* // Is the value of a `funding` property of a `package.json` // a valid type+url for `npm fund` to di...
  * `normalizeFunding` (Impact: 8.3 | O(N^1))
    * *Intent:* // supports object funding and string shorthand, or an array of these // if original was an array, r...
  * `read` (Impact: 2.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 31`, `args: 14`, `func_start: 16`
* *Risk/State:* `state_mutation: 12`, `dead_code: 2`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 10`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:url, arborist
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/verify-signatures.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.498 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.454 IQR)
- **Top Global Matches:** file_cluster_4: 12.498, file_cluster_13: 12.997, file_cluster_8: 13.101
- **Magnitude:** 231.94 | **LOC:** 393 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (19.0979%)
**Top Internal Functions/Classes:**
  * `sortAlphabetically` (Impact: 77.1 | O(N^3) | DB: 41)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 17`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 91`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 60`, `import: 7`
* *Defense:* `safety: 5`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tuf, npm-package-arg, +, string-locale-compare, proc-log, npm-registry-fetch, pacote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/error-message.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.291 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.404 IQR)
- **Top Global Matches:** file_cluster_17: 12.291, file_cluster_13: 12.339, file_cluster_0: 12.626
- **Magnitude:** 185.4 | **LOC:** 454 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (86.5653%), Tech Debt (89.7216%)
**Top Internal Functions/Classes:**
  * `errorMessage` (Impact: 149.9 | O(2^N) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 7`, `args: 5`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 33`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `api: 1`, `import: 5`
* *Defense:* `safety: 7`, `sync_locks: 1`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` parse-conflict-json, did-you-mean.js, node:path, proc-log, redact, node:fs, explain-eresolve.js, node:util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/util.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.49 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.629 IQR)
- **Top Global Matches:** file_cluster_4: 11.49, file_cluster_13: 11.779, file_cluster_17: 11.793
- **Magnitude:** 175.6 | **LOC:** 219 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (96.8144%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `spawn` (Impact: 82.5 | O(2^N) | DB: 1)
  * `json` (Impact: 7.4 | O(2^N) | DB: 4)
  * `getArgs` (Impact: 4.1 | O(N^1) | DB: 2)
    * *Intent:* // for spawn, allow a flat array of arguments where the // the last arg can optionally be an options...
  * `writeFile` (Impact: 3.7 | O(2^N))
  * `query` (Impact: 3.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 43`, `args: 20`, `func_start: 13`
* *Risk/State:* `state_mutation: 27`, `dead_code: 1`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 33`, `import: 10`
* *Defense:* `safety: 13`, `immutability_locks: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001481
  * `Imports (Out-Degree: 0):` promises, node:path, map-workspaces, proc-log, promise-spawn, git, node:util, nopt
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mock-globals/test/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.964 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.813 IQR)
- **Top Global Matches:** file_cluster_8: 8.964, file_cluster_4: 9.139, file_cluster_1: 9.696
- **Magnitude:** 143.36 | **LOC:** 332 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (49.0529%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `reset` (Impact: 12.2 | O(2^N))
  * `callback` (Impact: 4.0 | O(N^1))
  * `mockGlobals` (Impact: 2.0 | O(N^2))
  * `mockGlobals` (Impact: 1.9 | O(N^1) | DB: 1)
  * `mockGlobals` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 74`, `args: 43`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `duplicate_logic: 14`
* *Architecture:* `concurrency: 95`, `import: 2`
* *Defense:* `safety: 3`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/reify-output.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.02 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.199 IQR)
- **Top Global Matches:** file_cluster_8: 12.02, file_cluster_0: 12.245, file_cluster_17: 12.262
- **Magnitude:** 142.94 | **LOC:** 221 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^4) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (64.6912%), Tech Debt (90.808%)
**Top Internal Functions/Classes:**
  * `depth` (Impact: 63.3 | O(N^4) | DB: 27)
  * `getAuditReport` (Impact: 16.8 | O(N^1))
  * `printAuditReport` (Impact: 5.5 | O(N^1))
  * `getAuditReport` (Impact: 5.0 | O(N^2))
  * `getAuditReport` (Impact: 3.8 | O(N^1))
    * *Intent:* // pass in an arborist object, and it'll output the data about what // was done, what was audited, e...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 13`, `args: 6`, `func_start: 12`
* *Risk/State:* `state_mutation: 41`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 8`, `api: 2`
* *Defense:* `safety: 13`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ms, npm-audit-report, audit-error.js, libnpmfund, proc-log, treeverse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smoke-tests/test/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.769 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.437 IQR)
- **Top Global Matches:** file_cluster_8: 7.769, file_cluster_4: 8.185, file_cluster_7: 8.776
- **Magnitude:** 141.34 | **LOC:** 408 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (38.7555%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `readFile` (Impact: 7.4 | O(2^N))
  * `readFile` (Impact: 2.2 | O(N^1))
  * `readFile` (Impact: 2.2 | O(N^1))
  * `abbrevManifest` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 118`, `args: 29`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 2`, `api: 5`, `concurrency: 115`, `import: 3`
* *Defense:* `safety: 4`, `sync_locks: 13`, `immutability_locks: 39`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` setup.js, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/utils/open-url.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.551 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.321 IQR)
- **Top Global Matches:** file_cluster_4: 9.551, file_cluster_8: 9.587, file_cluster_13: 10.129
- **Magnitude:** 140.52 | **LOC:** 313 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (78.3148%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createInterface` (Impact: 27.1 | O(N^5))
  * `openUrl` (Impact: 7.9 | O(2^N))
  * `openWithNpm` (Impact: 7.2 | O(2^N))
  * `open` (Impact: 5.5 | O(N^2))
  * `openUrl` (Impact: 4.3 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 74`, `args: 36`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 11`, `fragile_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `io: 18`, `api: 1`, `concurrency: 65`, `import: 4`
* *Defense:* `safety: 3`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:events, mock-npm, tmock, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/display.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.32 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 6.087 IQR)
- **Top Global Matches:** file_cluster_8: 10.32, file_cluster_13: 10.693, file_cluster_17: 10.749
- **Magnitude:** 129.2 | **LOC:** 554 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (22.8644%), Tech Debt (99.9928%)
**Top Internal Functions/Classes:**
  * `setBlocking` (Impact: 14.3 | O(2^N))
  * `write` (Impact: 10.8 | O(2^N))
  * `write` (Impact: 8.2 | O(2^N))
  * `getArrayOrObject` (Impact: 7.7 | O(N^1))
  * `renderFrame` (Impact: 7.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 37`, `args: 33`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 5`, `import: 5`
* *Defense:* `safety: 22`, `immutability_locks: 25`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` supports-color, format, proc-log, chalk, explain-eresolve.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/npx-cli.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.269 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 6.126 IQR)
- **Top Global Matches:** file_cluster_17: 10.269, file_cluster_13: 10.273, file_cluster_8: 10.289
- **Magnitude:** 124.04 | **LOC:** 131 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.6447%), Tech Debt (67.3884%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 2`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cli.js, definitions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/queryable.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.673 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.595 IQR)
- **Top Global Matches:** file_cluster_17: 12.673, file_cluster_13: 12.844, file_cluster_11: 12.846
- **Magnitude:** 123.06 | **LOC:** 288 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (45.5763%), Tech Debt (38.7179%)
**Top Internal Functions/Classes:**
  * `parseKeys` (Impact: 49.9 | O(2^N) | DB: 5)
  * `query` (Impact: 27.1 | O(2^N) | DB: 1)
    * *Intent:* // empty-bracket-shortcut-syntax is not supported on getter
  * `replaceAppendSymbols` (Impact: 10.9 | O(2^N))
    * *Intent:* // replaces any occurrence of an empty-brackets (e.g: []) with a special Symbol(append) to represent...
  * `get` (Impact: 3.8 | O(N^1) | DB: 1)
  * `delete` (Impact: 2.1 | O(N^1))
    * *Intent:* // handles array indexes, converting valid integers to numbers // note that occurrences of Symbol(ap...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 21`, `args: 11`, `func_start: 14`
* *Risk/State:* `state_mutation: 22`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 3`, `immutability_locks: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/libnpmexec/lib/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.691 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.547 IQR)
- **Top Global Matches:** file_cluster_4: 11.691, file_cluster_13: 11.895, file_cluster_8: 12.334
- **Magnitude:** 122.26 | **LOC:** 316 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (96.9867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `exec` (Impact: 56.8 | O(N^2) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 27`, `args: 5`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`
* *Architecture:* `io: 8`, `api: 1`, `concurrency: 38`, `import: 17`
* *Defense:* `safety: 13`, `sync_locks: 1`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` with-lock.js, run-script.js, is-windows.js, package-json, promises, npm-package-arg, semver, pacote...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/utils/log-file.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.512 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.532 IQR)
- **Top Global Matches:** file_cluster_8: 8.512, file_cluster_4: 8.837, file_cluster_13: 9.191
- **Magnitude:** 121.3 | **LOC:** 362 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (86.7646%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `makeOldLogs` (Impact: 7.8 | O(N^1))
  * `constructor` (Impact: 7.3 | O(N^3))
  * `rm` (Impact: 7.3 | O(N^3) | DB: 3)
  * `log` (Impact: 3.7 | O(2^N) | DB: 6)
    * *Intent:* // Create a fake public method since there is not one on logFile anymore
  * `constructor` (Impact: 3.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 83`, `args: 37`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 18`, `concurrency: 77`, `import: 8`
* *Defense:* `safety: 2`, `immutability_locks: 80`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tmock, node:path, clean-snapshot, node:os, fs-minipass, log-file.js, node:fs, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/bundle-and-gitignore-deps.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.227 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.081 IQR)
- **Top Global Matches:** file_cluster_4: 11.227, file_cluster_17: 11.513, file_cluster_13: 11.583
- **Magnitude:** 118.58 | **LOC:** 263 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (75.3049%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAllowedPaths` (Impact: 31.3 | O(N^2) | DB: 11)
  * `main` (Impact: 9.7 | O(N^1) | DB: 7)
    * *Intent:* /*
  * `lsAndRmIgnored` (Impact: 4.8 | O(N^1))
  * `setBundleDeps` (Impact: 2.3 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 36`, `args: 19`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`, `dead_code: 2`
* *Architecture:* `io: 4`, `concurrency: 30`, `import: 7`
* *Defense:* `safety: 1`, `sync_locks: 1`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` npm-packlist, package-json, node:path, util, string-locale-compare, git, arborist
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/read-user-info.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.107 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.549 IQR)
- **Top Global Matches:** file_cluster_8: 8.107, file_cluster_13: 8.71, file_cluster_4: 8.965
- **Magnitude:** 116.14 | **LOC:** 70 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (45.6317%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `readUsername` (Impact: 28.6 | O(2^N))
  * `readEmail` (Impact: 28.6 | O(2^N))
  * `readOTP` (Impact: 24.4 | O(2^N))
  * `readPassword` (Impact: 20.4 | O(2^N))
  * `read` (Impact: 7.0 | O(2^N))
    * *Intent:* // Pass options through so we can differentiate between regular and silent prompts
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 14`, `args: 10`, `func_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` npm-user-validate, read, proc-log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mock-globals/lib/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.266 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 6.086 IQR)
- **Top Global Matches:** file_cluster_17: 11.266, file_cluster_8: 11.291, file_cluster_11: 11.767
- **Magnitude:** 115.06 | **LOC:** 237 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (55.447%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `splitLastSep` (Impact: 34.9 | O(N^2) | DB: 2)
  * `get` (Impact: 20.7 | O(2^N))
    * *Intent:* // A weird getter that can look up keys on nested objects but also // match keys with dots in their ...
  * `getKeys` (Impact: 12.2 | O(2^N))
    * *Intent:* // Map an object to an array of nested keys separated by dots // { a: 1, b: { c: 2, d: [1] } } => ['...
  * `protoDescriptor` (Impact: 6.1 | O(N^2) | DB: 3)
    * *Intent:* // Walk prototype chain to get first available descriptor. This is necessary // to get the current p...
  * `exports` (Impact: 4.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 44`, `args: 27`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`
* *Architecture:* `api: 3`
* *Defense:* `safety: 9`, `immutability_locks: 28`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/publish.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.685 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.531 IQR)
- **Top Global Matches:** file_cluster_4: 11.685, file_cluster_13: 12.285, file_cluster_17: 12.383
- **Magnitude:** 114.8 | **LOC:** 205 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (99.9604%), Tech Debt (86.9892%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 27.4 | O(N^1) | DB: 2)
  * `updatePkg` (Impact: 2.8 | O(N^2) | DB: 5)
  * `updatePkg` (Impact: 2.0 | O(N^1) | DB: 10)
  * `op` (Impact: 1.8 | O(N^1))
  * `getWorkspaceTag` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 41`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 15`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `concurrency: 60`, `import: 7`
* *Defense:* `safety: 5`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cli-table3, semver, fs, read, proc-log, pacote, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/libnpmteam/test/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.054 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.756 IQR)
- **Top Global Matches:** file_cluster_8: 9.054, file_cluster_4: 9.42, file_cluster_0: 9.634
- **Magnitude:** 110.22 | **LOC:** 221 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (27.8386%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 4.1 | O(N^1) | DB: 3)
  * `test` (Impact: 4.0 | O(N^1) | DB: 3)
  * `test` (Impact: 4.0 | O(N^1) | DB: 3)
  * `test` (Impact: 4.0 | O(N^1) | DB: 3)
  * `test` (Impact: 3.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 49`, `args: 22`, `func_start: 41`
* *Risk/State:* `duplicate_logic: 22`
* *Architecture:* `io: 9`, `concurrency: 42`, `import: 3`
* *Defense:* `test: 22`, `immutability_locks: 17`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, tap, tnock.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/libnpmfund/test/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.494 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.768 IQR)
- **Top Global Matches:** file_cluster_8: 7.494, file_cluster_7: 8.57, file_cluster_1: 8.756
- **Magnitude:** 104.68 | **LOC:** 1362 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (2.6749%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `normalizeFunding` (Impact: 4.3 | O(2^N) | DB: 6)
  * `readTree` (Impact: 4.0 | O(N^6) | DB: 18)
  * `readTree` (Impact: 4.0 | O(N^6) | DB: 9)
  * `readTree` (Impact: 4.0 | O(N^6) | DB: 12)
  * `readTree` (Impact: 4.0 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 65`, `args: 29`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 7`, `duplicate_logic: 31`
* *Architecture:* `io: 102`, `concurrency: 9`, `import: 3`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `bin/npx` (SHELL) | Magnitude: 74.74 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 39, branch: 21, indent_spaces: 13, duplicate_logic: 8
- `bin/npm` (SHELL) | Magnitude: 75.74 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 39, branch: 21, indent_spaces: 13, duplicate_logic: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `lib/commands/trust/index.js` (JAVASCRIPT) | Magnitude: 7.22 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, import: 6, structural_boundaries: 4, immutability_locks: 2
- `scripts/fish-completion.js` (JAVASCRIPT) | Magnitude: 31.38 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 25, immutability_locks: 11, structural_boundaries: 7, branch: 6
- `test/lib/utils/reify-output.js` (JAVASCRIPT) | Magnitude: 4.3 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: immutability_locks: 5, indent_spaces: 4, structural_boundaries: 3, import: 3
- `test/bin/windows-shims.js` (JAVASCRIPT) | Magnitude: 34.78 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 90, immutability_locks: 27, structural_boundaries: 19, args: 15
- `lib/utils/format.js` (JAVASCRIPT) | Magnitude: 33.0 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 25, sec_reflection_metaprogramming: 19, branch: 13, immutability_locks: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `bin/npm.ps1` (POWERSHELL) | Magnitude: 55.8 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 34, indent_spaces: 20, branch: 13, closures: 8
- `bin/npx.ps1` (POWERSHELL) | Magnitude: 55.8 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 34, indent_spaces: 20, branch: 13, closures: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `bin/npx-cli.js` (JAVASCRIPT) | Magnitude: 124.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, immutability_locks: 6, branch: 5, state_mutation: 4
- `mock-globals/lib/index.js` (JAVASCRIPT) | Magnitude: 115.06 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 44, branch: 32, immutability_locks: 28
- `lib/utils/error-message.js` (JAVASCRIPT) | Magnitude: 185.4 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, state_mutation: 33, branch: 27, immutability_locks: 14
- `lib/utils/npm-usage.js` (JAVASCRIPT) | Magnitude: 35.04 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, immutability_locks: 18, structural_boundaries: 12, branch: 9
- `lib/utils/sbom-spdx.js` (JAVASCRIPT) | Magnitude: 58.74 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 136, branch: 40, immutability_locks: 39, structural_boundaries: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `test/lib/utils/open-url.js` (JAVASCRIPT) | Magnitude: 140.52 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 248, structural_boundaries: 74, concurrency: 65, args: 36
- `workspaces/arborist/bin/license.js` (JAVASCRIPT) | Magnitude: 10.42 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 6, indent_spaces: 6, immutability_locks: 5, structural_boundaries: 3
- `lib/utils/installed-shallow.js` (JAVASCRIPT) | Magnitude: 15.72 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 10, immutability_locks: 8, concurrency: 5
- `workspaces/arborist/scripts/benchmark/reify.js` (JAVASCRIPT) | Magnitude: 54.28 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, io: 29, dependency_injection: 21, sec_io: 20
- `workspaces/arborist/bin/funding.js` (JAVASCRIPT) | Magnitude: 17.82 | Delta: **0.184 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, concurrency: 6, structural_boundaries: 4, immutability_locks: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `mock-registry/lib/index.js` (JAVASCRIPT) | Magnitude: 513.02 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 460, state_mutation: 212, branch: 75, immutability_locks: 63
- `lib/utils/explain-eresolve.js` (JAVASCRIPT) | Magnitude: 75.44 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 21, branch: 19, immutability_locks: 11
- `tap-snapshots/test/lib/utils/explain-eresolve.js.test.cjs` (JAVASCRIPT) | Magnitude: 25.0 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 336, indent_spaces: 186, bitwise_ops: 121, safety_bypasses: 49
- `lib/utils/tar.js` (JAVASCRIPT) | Magnitude: 42.52 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 85, immutability_locks: 19, structural_boundaries: 14, state_mutation: 14
- `workspaces/arborist/bin/lib/logging.js` (JAVASCRIPT) | Magnitude: 36.32 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 42, immutability_locks: 21, branch: 18, structural_boundaries: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `lib/utils/validate-lockfile.js` (JAVASCRIPT) | Magnitude: 17.02 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 13, sync_locks: 7, state_mutation: 6, branch: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `workspaces/arborist/lib/arborist/index.js` -> **Gar** (100.0% isolated ownership) | Magnitude: 261.8
- `mock-globals/test/index.js` -> **Josh Soref** (100.0% isolated ownership) | Magnitude: 143.36
- `test/lib/utils/open-url.js` -> **Josh Soref** (100.0% isolated ownership) | Magnitude: 140.52
- `scripts/bundle-and-gitignore-deps.js` -> **Josh Soref** (100.0% isolated ownership) | Magnitude: 118.58
- `lib/utils/read-user-info.js` -> **Marc Bernard** (100.0% isolated ownership) | Magnitude: 116.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/utils/format.js` -> **Severity: 0.057** (Embedded: 0.003 * Error Risk: 19.1545%)
- `workspaces/arborist/bin/lib/options.js` -> **Severity: 0.01** (Embedded: 0.0015 * Error Risk: 6.7352%)
- `lib/utils/cmd-list.js` -> **Severity: 0.009** (Embedded: 0.0015 * Error Risk: 6.2136%)
- `scripts/util.js` -> **Severity: 0.009** (Embedded: 0.0015 * Error Risk: 6.1054%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/utils/format.js` -> **Severity: 178.851** (Blast Radius: 3.944 * Doc Risk: 45.3476%)
- `lib/commands/trust/index.js` -> **Severity: 146.1** (Blast Radius: 1.461 * Doc Risk: 100.0%)
- `lib/utils/get-identity.js` -> **Severity: 146.1** (Blast Radius: 1.461 * Doc Risk: 100.0%)
- `lib/utils/output-error.js` -> **Severity: 146.1** (Blast Radius: 1.461 * Doc Risk: 100.0%)
- `lib/utils/reify-finish.js` -> **Severity: 146.1** (Blast Radius: 1.461 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
