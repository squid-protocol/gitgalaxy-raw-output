# ARCHITECTURAL_BRIEF: spamassassin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/spamassassin` |
| **Timestamp** | `2026-08-07T03:52:30.477502+00:00` |
| **Scan Duration** | `1.97s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `cd27d984b5eed731d8b4aae0dc654267fc7b9917` |
| **Git Remote** | `https://github.com/apache/spamassassin.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 104 malicious artifacts.

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
| Total Artifacts | 1882 |
| Analyzed Artifacts (Scanned) | 515 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1367 |
| Total LOC | 38852 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 27.4% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7483 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3685 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 335 | 33207 | 65.0% |
| SHELL | 57 | 1965 | 11.1% |
| PLAINTEXT | 45 | 4 | 8.7% |
| MARKDOWN | 25 | 0 | 4.9% |
| SQLITE | 22 | 354 | 4.3% |
| C | 15 | 2643 | 2.9% |
| MAKEFILE | 5 | 205 | 1.0% |
| YAML | 3 | 37 | 0.6% |
| PHP | 2 | 5 | 0.4% |
| M4 | 2 | 144 | 0.4% |
| CSS | 1 | 123 | 0.2% |
| JAVASCRIPT | 1 | 162 | 0.2% |
| XML | 1 | 0 | 0.2% |
| CSV | 1 | 3 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.165`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 230 | 44.7% |
| file_cluster_0 | 98 | 19.0% |
| file_cluster_13 | 90 | 17.5% |
| file_cluster_17 | 14 | 2.7% |
| file_cluster_9 | 5 | 1.0% |
| Unknown | 4 | 0.8% |
| file_cluster_11 | 3 | 0.6% |
| file_cluster_12 | 3 | 0.6% |
| file_cluster_4 | 2 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 66 | 12.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1367*

**Composition by Extension & Reason:**
- `no_extension`: 239x Unsupported Format (.undeterminable), 76x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.cf`: 234x Excluded (Unsupported Extension: '.cf'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lm`: 172x Excluded (Unsupported Extension: '.lm')
- `.pm`: 132x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.eml`: 44x Excluded (Unsupported Extension: '.eml')
- `.msg`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.8`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.1`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 161 LOC)
- `.3`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pre`: 16x Excluded (Unsupported Extension: '.pre'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.2`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.5`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC), 1x Excluded (Saturation: Line 23 exceeds 500 chars)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 50.3 | 58.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 65.3 | 82.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 31.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 14.3 | 0.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 67.9 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 1.9 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.7 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 37.9 | 1.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 38.2 | 35.0 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `masses/mass-check` (Hits: 118)
- `masses/rule-dev/sought/mkzone_remote_svn/run` (Hits: 55)
- `masses/rule-dev/sought/mkzone/run_part2` (Hits: 52)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **rules** (`debian/rules`) — 7 inbound connections
2. **utils.h** (`spamc/utils.h`) — 3 inbound connections
3. **date.t** (`t/date.t`) — 2 inbound connections
4. **utf8.t** (`t/utf8.t`) — 2 inbound connections
5. **spamassassin.install** (`debian/spamassassin.install`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mass-check** (`masses/mass-check`) — 45 outbound dependencies
2. **spamc.c** (`spamc/spamc.c`) — 28 outbound dependencies
3. **ruleqa.cgi** (`masses/rule-qa/automc/ruleqa.cgi`) — 24 outbound dependencies
4. **libspamc.c** (`spamc/libspamc.c`) — 24 outbound dependencies
5. **SIQ.pm** (`rulesrc/sandbox/dos/SIQ.pm`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `show_default_view` (@ `masses/rule-qa/automc/ruleqa.cgi`) -> Impact: **1065.3** | LOC: 1852
- `usage` (@ `masses/mass-check`) -> Impact: **792.0** | LOC: 1782
- `main` (@ `masses/garescorer.c`) -> Impact: **362.2** | LOC: 767
- `init` (@ `masses/rule-qa/corpus-hourly`) -> Impact: **352.1** | LOC: 442
- `set_freqs_templates` (@ `masses/rule-qa/automc/ruleqa.cgi`) -> Impact: **328.0** | LOC: 523
- `init` (@ `masses/rule-qa/reports-from-logs`) -> Impact: **273.1** | LOC: 319
  * *Intent:* # ---------------------------------------------------------------------------
- `tryone` (@ `t/cidrs.t`) -> Impact: **268.5** | LOC: 130
- `trynet` (@ `t/cidrs.t`) -> Impact: **261.9** | LOC: 118
- `_message_read_bsmtp` (@ `spamc/libspamc.c`) -> Impact: **226.6** | LOC: 479
- `evaluate_inner` (@ `masses/garescorer.c`) -> Impact: **187.2** | LOC: 623
  * *Intent:* #endif /* ! USE_VARIABLE_MUTATIONS */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 227 | 17640.11 | 45.15% | 17.47% |
| `spamd-apache2/t/certs` | 3 | 10017.04 | 0.0% | 0.0% |
| `masses` | 36 | 8847.85 | 71.51% | 18.76% |
| `debian` | 10 | 5201.1 | 7.99% | 9.01% |
| `t/data/etc` | 2 | 5001.0 | 0.0% | 0.0% |
| `masses/rule-qa/automc` | 6 | 3834.43 | 44.51% | 18.41% |
| `spamd-apache2/bin` | 3 | 3386.3 | 56.36% | 94.65% |
| `masses/rule-qa` | 14 | 2743.92 | 67.45% | 50.15% |
| `spamc` | 16 | 2727.98 | 33.08% | 27.39% |
| `masses/rule-dev` | 5 | 1121.08 | 62.57% | 11.25% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `t/perlcritic.t` -> **100.0%** Exposure
- `t/spamc_bug6176.t` -> **100.0%** Exposure
- `t/spamc_x_e.t` -> **100.0%** Exposure
- `t/spamc_y.t` -> **100.0%** Exposure
- `t/spamd_maxsize.t` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Makefile.PL` -> **100.0%** Exposure
- `contrib/mbox-to-check` -> **100.0%** Exposure
- `contrib/samailoffset` -> **100.0%** Exposure
- `debian/bin/genorig.pl` -> **100.0%** Exposure
- `masses/bayes-testing/bayes-static-thresholds` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `contrib/run-corpora` -> **1** Orphaned Functions | **14** Duplicates
- `sql/bayes_pg.sql` -> **2** Orphaned Functions | **11** Duplicates
- `spamc/libspamc.c` -> **12** Orphaned Functions | **0** Duplicates
- `masses/rule-qa/automc/sorttable.js` -> **6** Orphaned Functions | **4** Duplicates
- `sql/neural_pg.sql` -> **0** Orphaned Functions | **9** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`spamc/spamc.c`** -> AI Confidence: **99.48%**
2. **`masses/evolve_metarule/evolve_metarule.c`** -> AI Confidence: **99.39%**
3. **`spamc/libspamc.c`** -> AI Confidence: **99.39%**
4. **`masses/garescorer.c`** -> AI Confidence: **99.34%**
5. **`spamc/qmail-spamc.c`** -> AI Confidence: **99.32%**
6. **`masses/perceptron.c`** -> AI Confidence: **99.31%**
7. **`spamc/utils.c`** -> AI Confidence: **99.31%**
8. **`contrib/kill-spamd.sh`** -> AI Confidence: **99.29%**
9. **`contrib/run-corpora`** -> AI Confidence: **99.29%**
10. **`contrib/run-masses`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `91` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1734` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `masses/rule-qa/corpus-nightly` (SHELL) -> Cumulative Risk: **705.58**
- **Archetype:** `file_cluster_11` (Distance: 13.106 IQR)
- **Magnitude:** 77.22 | **LOC:** 100 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9991%), Safety Score (98.9133%), Tech Debt (98.6106%)
- **Heaviest Functions:** `__global_context__` (Impact: 53.0)

### 2. `masses/rule-qa/automc/sorttable.js` (JAVASCRIPT) -> Cumulative Risk: **655.35**
- **Archetype:** `file_cluster_17` (Distance: 15.104 IQR)
- **Magnitude:** 198.84 | **LOC:** 496 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9541%), Cognitive Load (92.0154%)
- **Heaviest Functions:** `forEach` (Impact: 19.0), `shaker_sort` (Impact: 15.4), `dean_addEvent` (Impact: 15.2)

### 3. `backend/nitemc/extract_to_rsync_dir` (SHELL) -> Cumulative Risk: **647.98**
- **Archetype:** `file_cluster_4` (Distance: 14.642 IQR)
- **Magnitude:** 57.28 | **LOC:** 63 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9905%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 18.3), `Anonymous_Block` (Impact: 5.2), `Anonymous_Block` (Impact: 5.2)

### 4. `t/data/Dumpheaders.pm` (PERL) -> Cumulative Risk: **632.6**
- **Archetype:** `file_cluster_0` (Distance: 14.494 IQR)
- **Magnitude:** 193.16 | **LOC:** 98 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9321%), Safety Score (99.273%)
- **Heaviest Functions:** `check_end` (Impact: 82.0), `new` (Impact: 3.8)

### 5. `masses/runGA` (SHELL) -> Cumulative Risk: **620.64**
- **Archetype:** `file_cluster_11` (Distance: 11.508 IQR)
- **Magnitude:** 121.58 | **LOC:** 184 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9995%), Safety Score (99.989%), Tech Debt (99.7764%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 70.1), `Anonymous_Block` (Impact: 5.2), `__global_context__` (Impact: 5.1)

### 6. `spamc/libspamc.c` (C) -> Cumulative Risk: **620.61**
- **Archetype:** `file_cluster_13` (Distance: 13.741 IQR)
- **Magnitude:** 1391.62 | **LOC:** 2465 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.0884%), Documentation (87.3077%)
- **Heaviest Functions:** `_message_read_bsmtp` (Impact: 226.6), `_opensocket` (Impact: 103.1), `_append_original_body` (Impact: 69.9)

### 7. `spamc/utils.c` (C) -> Cumulative Risk: **610.93**
- **Archetype:** `file_cluster_13` (Distance: 12.434 IQR)
- **Magnitude:** 199.18 | **LOC:** 271 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (98.486%), Safety Score (86.6471%)
- **Heaviest Functions:** `fd_timeout_read` (Impact: 26.7), `full_write` (Impact: 21.6), `full_read` (Impact: 18.4)

### 8. `masses/garescorer.c` (C) -> Cumulative Risk: **600.6**
- **Archetype:** `file_cluster_8` (Distance: 13.837 IQR)
- **Magnitude:** 1601.46 | **LOC:** 1314 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.3618%), Documentation (96.1374%)
- **Heaviest Functions:** `main` (Impact: 362.2), `evaluate_inner` (Impact: 187.2), `myMutation` (Impact: 88.5)

### 9. `spamd/netbsd-rc-script.sh` (SHELL) -> Cumulative Risk: **595.71**
- **Archetype:** `file_cluster_12` (Distance: 13.252 IQR)
- **Magnitude:** 131.1 | **LOC:** 151 | **CtrlFlow:** 83.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9921%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 24.9), `Anonymous_Block` (Impact: 10.3), `Anonymous_Block` (Impact: 6.5)

### 10. `contrib/run-corpora` (SHELL) -> Cumulative Risk: **591.5**
- **Archetype:** `file_cluster_8` (Distance: 13.114 IQR)
- **Magnitude:** 2.04 | **LOC:** 201 | **CtrlFlow:** 79.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9939%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 13.7), `Anonymous_Block` (Impact: 13.1), `Anonymous_Block` (Impact: 13.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `debian/GPG.KEY` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamd-apache2/t/certs/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamd-apache2/t/certs/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/data/etc/testhost.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dnsbl_subtests.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.955 IQR)
- **Top Global Matches:** file_cluster_0: 11.955, file_cluster_4: 12.383, file_cluster_13: 12.395
- **Magnitude:** 4183.43 | **LOC:** 390 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.8149%), Tech Debt (71.4362%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 55`, `args: 11`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 101`, `dead_code: 3`, `fragile_debt: 6`
* *Architecture:* `io: 5`, `concurrency: 12`, `import: 14`
* *Defense:* `safety: 5`, `test: 2`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, Mail::SpamAssassin, SPAMD_LOCALHOST, Errno, longer, constant, vars, SATest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/automc/ruleqa.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.112 IQR)
- **Top Global Matches:** file_cluster_0: 14.112, file_cluster_17: 14.112, file_cluster_8: 14.135
- **Magnitude:** 3450.74 | **LOC:** 2189 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.2028%), Tech Debt (10.5063%)
**Top Internal Functions/Classes:**
  * `show_default_view` (Impact: 1065.3)
  * `set_freqs_templates` (Impact: 328.0)
  * `get_daterev_html_table` (Impact: 178.8)
  * `read_automc_global_conf` (Impact: 156.1)
    * *Intent:* # ---------------------------------------------------------------------------
  * `ui_parse_url_base` (Impact: 151.1)
    * *Intent:* # ---------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 486`, `args: 64`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 1141`, `dead_code: 6`, `fragile_debt: 3`
* *Architecture:* `io: 34`, `api: 1`, `import: 18`
* *Defense:* `safety: 12`, `doc: 1`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` of, a, CGI::Carp, Time::Local, strict, info, the, Data::Dumper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamd-apache2/bin/apache-spamd.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.668 IQR)
- **Top Global Matches:** file_cluster_0: 13.668, file_cluster_13: 13.964, file_cluster_8: 13.993
- **Magnitude:** 3178.4 | **LOC:** 368 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.9651%), Tech Debt (99.5369%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 43`, `args: 3`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 258`, `planned_debt: 1`, `fragile_debt: 13`
* *Architecture:* `io: 7`, `import: 7`
* *Defense:* `safety: 1`, `doc: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` reasonable, Sys::Hostname, DESTROY, mod_perl, Apache2::BuildConfig, Mail::SpamAssassin::Spamd::Config, Cwd, point...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/mass-check` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.844 IQR)
- **Top Global Matches:** file_cluster_0: 14.844, file_cluster_11: 15.118, file_cluster_13: 15.22
- **Magnitude:** 2693.22 | **LOC:** 2679 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.0958%), Tech Debt (10.5525%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 792.0)
  * `client_mode` (Impact: 138.4)
    * *Intent:* # this is the function that implements client mode. generally, in a loop: # make a request of the se...
  * `server_mode` (Impact: 44.0)
    * *Intent:* ############################################################################ # this is the function ...
  * `deal_with_before_after` (Impact: 25.5)
  * `scan_client_cache` (Impact: 24.4)
    * *Intent:* # scan the client's cache and return a path to a gzip archive of AI output
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 742`, `structural_boundaries: 434`, `args: 27`, `func_start: 39`
* *Risk/State:* `high_risk_execution: 16`, `state_mutation: 1501`, `dead_code: 26`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 118`, `concurrency: 36`, `import: 39`
* *Defense:* `safety: 7`, `cleanup: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Socket, umask, it, server, strict, the, more, Mail::SpamAssassin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/bayessql.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.035 IQR)
- **Top Global Matches:** file_cluster_0: 13.035, file_cluster_13: 13.126, file_cluster_8: 13.199
- **Magnitude:** 2129.41 | **LOC:** 559 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.0222%), Tech Debt (14.429%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 94`, `args: 2`, `func_start: 4`
* *Risk/State:* `state_mutation: 268`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `io: 12`, `import: 13`
* *Defense:* `safety: 3`, `test: 54`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mail::SpamAssassin, File::Find, this, DBI, constant, biggie, SATest, DBD::SQLite...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mkrules.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.533 IQR)
- **Top Global Matches:** file_cluster_8: 11.533, file_cluster_0: 11.592, file_cluster_13: 11.903
- **Magnitude:** 1803.52 | **LOC:** 476 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.3931%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 50`, `args: 10`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 128`
* *Architecture:* `io: 2`, `import: 8`
* *Defense:* `test: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Copy, this, File::Path, Mail::SpamAssassin::Plugin, SATest, Test::More, lib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/garescorer.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.837 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.05 IQR)
- **Top Global Matches:** file_cluster_8: 13.837, file_cluster_13: 14.012, file_cluster_7: 14.097
- **Magnitude:** 1601.46 | **LOC:** 1314 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.7198%), Tech Debt (26.0257%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 362.2)
  * `evaluate_inner` (Impact: 187.2)
    * *Intent:* #endif /* ! USE_VARIABLE_MUTATIONS */
  * `myMutation` (Impact: 88.5)
  * `Crossover` (Impact: 43.1)
    * *Intent:* /* Did previous try go too far away? */ if (iters_same_passed) { /* in 2nd phase */
  * `showSummary` (Impact: 30.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 35`, `args: 2`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 713`, `fragile_debt: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 120`, `import: 6`
* *Defense:* `doc: 6`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time.h, scores.h, pgapack.h, tests.h, math.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamc/libspamc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.741 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.175 IQR)
- **Top Global Matches:** file_cluster_13: 13.741, file_cluster_8: 13.863, file_cluster_0: 14.012
- **Magnitude:** 1391.62 | **LOC:** 2465 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.553%), Tech Debt (68.9898%)
**Top Internal Functions/Classes:**
  * `_message_read_bsmtp` (Impact: 226.6)
  * `_opensocket` (Impact: 103.1)
    * *Intent:* #include <syslog.h> #include <unistd.h> #include <sys/types.h> #include <sys/socket.h> #include <net...
  * `_append_original_body` (Impact: 69.9)
    * *Intent:* /* Search for \nDATA\n which marks start of actual message */ while ((p_len = (m->raw_len - (p - m->...
  * `transport_setup` (Impact: 69.6)
  * `_try_to_connect_unix` (Impact: 53.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 87`, `args: 20`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 522`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 12`
* *Architecture:* `io: 12`, `api: 157`, `import: 24`
* *Defense:* `safety: 17`, `test: 7`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` time.h, un.h, string.h, socket.h, errno.h, in.h, io.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/header_utf8.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.097 IQR)
- **Top Global Matches:** file_cluster_8: 10.097, file_cluster_0: 10.137, file_cluster_13: 10.31
- **Magnitude:** 964.72 | **LOC:** 233 | **CtrlFlow:** 87.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.2561%), Tech Debt (79.931%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 12`, `func_start: 1`
* *Risk/State:* `state_mutation: 21`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `import: 9`
* *Defense:* `safety: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Net::LibIDN, constant, Net::LibIDN2, SATest, Test::More, Email::Address::XS, lib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-dev/seek-phrases-in-log` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.721 IQR)
- **Top Global Matches:** file_cluster_17: 13.721, file_cluster_0: 13.79, file_cluster_11: 13.909
- **Magnitude:** 849.34 | **LOC:** 710 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.4709%), Tech Debt (56.2563%)
**Top Internal Functions/Classes:**
  * `collapse_pats` (Impact: 116.5)
  * `assemble_regexps` (Impact: 51.2)
  * `subsume_with_dotstars` (Impact: 33.7)
  * `expand_with_dots` (Impact: 32.7)
  * `filter_into_message_subsets` (Impact: 25.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 133`, `args: 11`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 497`, `dead_code: 3`, `planned_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `import: 5`
* *Defense:* `safety: 2`, `doc: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dumper, Getopt::Long, this, longer, way, Digest::SHA, non, need...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/hit-frequencies` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.263 IQR)
- **Top Global Matches:** file_cluster_8: 13.263, file_cluster_17: 13.364, file_cluster_13: 13.383
- **Magnitude:** 846.78 | **LOC:** 1036 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.8737%), Tech Debt (11.3024%)
**Top Internal Functions/Classes:**
  * `compute_overlaps_for_rule` (Impact: 163.3)
  * `_print_overlap_ratios` (Impact: 60.6)
  * `_hmap_to_overlap_ratio` (Impact: 15.3)
  * `_prettify_overlap_rules` (Impact: 11.6)
  * `soratio` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 198`, `args: 8`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 563`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `import: 6`
* *Defense:* `safety: 5`, `doc: 18`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Getopt::Long, this, hits, FindBin, results, less, Pod::Usage, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile.PL` (PERL | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.187 IQR)
- **Top Global Matches:** file_cluster_0: 12.187, file_cluster_8: 12.471, file_cluster_13: 12.653
- **Magnitude:** 790.12 | **LOC:** 1141 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (65.3762%), Tech Debt (73.1482%)
**Top Internal Functions/Classes:**
  * `MY::constants` (Impact: 118.6)
    * *Intent:* # Now override the constants routine to add our own macros.
  * `parse_arg` (Impact: 101.3)
  * `MY::postamble` (Impact: 71.2)
  * `float_to_version` (Impact: 64.0)
    * *Intent:* # Converts a version represented as a float to a real three-part version, # eg.: # 5.006001 -> 5.6.1...
  * `MY::dist` (Impact: 12.5)
    * *Intent:* # Override some vars in the dist section.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 167`, `args: 8`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 322`, `planned_debt: 1`, `fragile_debt: 5`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `import: 11`
* *Defense:* `safety: 8`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExtUtils::MakeMaker, man1, this, Config, for, DBI, constant, a...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/reports-from-logs` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.383 IQR)
- **Top Global Matches:** file_cluster_17: 13.383, file_cluster_0: 13.415, file_cluster_13: 13.458
- **Magnitude:** 764.1 | **LOC:** 714 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.4479%), Tech Debt (17.5937%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 273.1)
    * *Intent:* # ---------------------------------------------------------------------------
  * `start_hit_frequencies_at_rev` (Impact: 85.3)
    * *Intent:* # ---------------------------------------------------------------------------
  * `configure` (Impact: 10.1)
    * *Intent:* # ---------------------------------------------------------------------------
  * `get_rulemetadata_for_revision` (Impact: 7.9)
    * *Intent:* # ---------------------------------------------------------------------------
  * `create_outputdir` (Impact: 7.5)
    * *Intent:* # ---------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 176`, `args: 14`, `func_start: 22`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 361`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 32`, `import: 14`
* *Defense:* `safety: 3`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` data, File::Copy, Getopt::Long, Time::ParseDate, log, this, files, File::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/corpus-hourly` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.756 IQR)
- **Top Global Matches:** file_cluster_17: 13.756, file_cluster_0: 13.839, file_cluster_13: 13.984
- **Magnitude:** 694.44 | **LOC:** 524 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.8979%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 352.1)
  * `configure` (Impact: 8.9)
  * `clean_up` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 122`, `args: 3`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 324`, `dead_code: 4`
* *Architecture:* `io: 40`, `import: 11`
* *Defense:* `safety: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Copy, Getopt::Long, Time::ParseDate, newer, longer, files, File::Path, POSIX...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rulesrc/sandbox/dos/SIQ.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.855 IQR)
- **Top Global Matches:** file_cluster_0: 12.855, file_cluster_13: 13.135, file_cluster_8: 13.265
- **Magnitude:** 634.78 | **LOC:** 1162 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.8079%), Tech Debt (13.4463%)
**Top Internal Functions/Classes:**
  * `set_config` (Impact: 142.3)
  * `siq_score` (Impact: 28.3)
  * `siq_ip_score` (Impact: 28.3)
  * `siq_domain_score` (Impact: 28.3)
  * `siq_relative_score` (Impact: 28.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 210`, `args: 25`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 327`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 22`, `api: 1`, `import: 23`
* *Defense:* `safety: 2`, `doc: 39`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` of, Socket, whatever, strict, the, suitable, bytes, first...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cidrs.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.085 IQR)
- **Top Global Matches:** file_cluster_0: 10.085, file_cluster_13: 10.437, file_cluster_8: 10.488
- **Magnitude:** 550.82 | **LOC:** 152 | **CtrlFlow:** 87.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.792%), Tech Debt (73.3489%)
**Top Internal Functions/Classes:**
  * `tryone` (Impact: 268.5)
  * `trynet` (Impact: 261.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 19`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 18`, `fragile_debt: 2`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mail::SpamAssassin, Mail::SpamAssassin::NetSet, Net::CIDR::Lite, constant, SATest, Test::More, strict, lib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/rule-hits-over-time` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.276 IQR)
- **Top Global Matches:** file_cluster_13: 13.276, file_cluster_0: 13.305, file_cluster_8: 13.329
- **Magnitude:** 535.78 | **LOC:** 530 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.0301%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_gp` (Impact: 59.9)
  * `plot_gp` (Impact: 36.0)
  * `read_logs` (Impact: 29.9)
  * `summarise` (Impact: 20.2)
  * `usage` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 109`, `args: 4`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 351`, `dead_code: 1`
* *Architecture:* `io: 15`, `import: 10`
* *Defense:* `safety: 3`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` data, scaling, Getopt::Long, Statistics::DEA, this, SDBM_File, POSIX, Fcntl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamc/getopt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.046 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.109 IQR)
- **Top Global Matches:** file_cluster_13: 13.046, file_cluster_8: 13.119, file_cluster_11: 13.286
- **Magnitude:** 531.54 | **LOC:** 352 | **CtrlFlow:** 76.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.4617%), Tech Debt (14.0027%)
**Top Internal Functions/Classes:**
  * `spamc_getopt_long` (Impact: 125.5)
  * `spamc_getopt` (Impact: 45.9)
  * `main` (Impact: 37.2)
  * `optiserr` (Impact: 35.8)
    * *Intent:* * </@LICENSE> */ #include <stdio.h> #include <string.h> #include <assert.h> #include <stdlib.h> #inc...
  * `longoptiserr` (Impact: 30.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 35`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 215`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 36`, `import: 6`
* *Defense:* `safety: 4`, `test: 3`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` getopt.h, stdlib.h, assert.h, string.h, errno.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/corpora/mk-corpus-link-farm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.04 IQR)
- **Top Global Matches:** file_cluster_0: 13.04, file_cluster_8: 13.052, file_cluster_13: 13.158
- **Magnitude:** 529.52 | **LOC:** 844 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1752%), Tech Debt (13.885%)
**Top Internal Functions/Classes:**
  * `parse_rfc822_date` (Impact: 98.3)
  * `usage` (Impact: 7.8)
  * `time_to_rfc822_date` (Impact: 4.5)
  * `dbg` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 202`, `args: 17`, `func_start: 23`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 404`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 12`, `import: 13`
* *Defense:* `safety: 3`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dumper, Time::ParseDate, Getopt::Long, File::Find, this, File::Basename, SDBM_File, longer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rewrite-cf-with-new-scores` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.103 IQR)
- **Top Global Matches:** file_cluster_0: 13.103, file_cluster_13: 13.207, file_cluster_8: 13.258
- **Magnitude:** 456.36 | **LOC:** 522 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.4209%), Tech Debt (11.8035%)
**Top Internal Functions/Classes:**
  * `new_score_line` (Impact: 131.9)
  * `read_gascores` (Impact: 17.4)
  * `read_oldscores` (Impact: 14.0)
  * `readline_gen` (Impact: 7.1)
  * `readline_gen2` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 85`, `args: 6`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 252`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 11`, `import: 5`
* *Defense:* `safety: 2`, `doc: 6`, `test: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, GA, this, the, new, Pod::Usage, warnings, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/20_saw_ampersand.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.545 IQR)
- **Top Global Matches:** file_cluster_0: 10.545, file_cluster_8: 11.409, file_cluster_13: 11.445
- **Magnitude:** 455.01 | **LOC:** 230 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.4977%), Tech Debt (18.594%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 23`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 37`, `planned_debt: 1`
* *Architecture:* `io: 11`, `import: 7`
* *Defense:* `safety: 3`, `test: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Mail::SpamAssassin, of, longer, Devel::SawAmpersand, debug, Carp, SATest, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `masses/rule-qa/automc/ruleqa.cgi` (PERL) | Magnitude: 3450.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1427, state_mutation: 1141, branch: 506, structural_boundaries: 486
- `masses/corpora/mk-corpus-link-farm` (PERL) | Magnitude: 529.52 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 460, state_mutation: 404, structural_boundaries: 202, branch: 189
- `masses/rule-qa/import-logs` (PERL) | Magnitude: 118.38 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 55, structural_boundaries: 35, branch: 33
- `tools/mboxsplit` (PERL) | Magnitude: 0.05 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 42, branch: 20, indent_spaces: 11, structural_boundaries: 8
- `masses/enable-all-evolved-rules` (PERL) | Magnitude: 39.56 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 23, branch: 14, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `contrib/run-masses` (SHELL) | Magnitude: 0.61 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 31, branch: 17, safety_bypasses: 14, indent_spaces: 7
- `masses/runGA` (SHELL) | Magnitude: 121.58 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 67, branch: 50, state_mutation: 39, indent_spaces: 35
- `masses/rule-qa/corpus-nightly` (SHELL) | Magnitude: 77.22 | Delta: **0.305 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 33, io: 21, state_mutation: 21, indent_spaces: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `masses/contrib/automasscheck-minimal/automasscheck-minimal.sh` (SHELL) | Magnitude: 1.59 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 72, branch: 64, state_mutation: 58, io: 39
- `tools/github/apply_pr.sh` (SHELL) | Magnitude: 0.03 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 25, branch: 12, state_mutation: 12, structural_boundaries: 11
- `spamd/netbsd-rc-script.sh` (SHELL) | Magnitude: 131.1 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 62, indent_tabs: 50, branch: 46, reflection_metaprogramming: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/spamd_prefork_stress_2.t` (PERL) | Magnitude: 33.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 18, branch: 13, indent_spaces: 9, structural_boundaries: 7
- `t/idn_dots.t` (PERL) | Magnitude: 71.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 51, state_mutation: 40, branch: 35, structural_boundaries: 29
- `t/spamd_plugin.t` (PERL) | Magnitude: 21.74 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 6, state_mutation: 6, bitwise_ops: 6, structural_boundaries: 5
- `t/dcc.t` (PERL) | Magnitude: 18.76 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, bitwise_ops: 8, branch: 7, import: 5
- `t/db_awl_path_welcome_block.t` (PERL) | Magnitude: 22.66 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 8, state_mutation: 7, decorators: 7, indent_spaces: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `masses/freqdiff` (PERL) | Magnitude: 127.92 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 111, branch: 74, indent_tabs: 46, indent_spaces: 44
- `masses/evolve_metarule/preproc.pl` (PERL) | Magnitude: 82.46 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 66, branch: 38, indent_tabs: 30, structural_boundaries: 26
- `masses/mboxget` (PERL) | Magnitude: 141.24 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 66, branch: 56, structural_boundaries: 20
- `masses/rule-qa/reports-from-logs` (PERL) | Magnitude: 764.1 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 424, state_mutation: 361, structural_boundaries: 176, branch: 173
- `masses/cpucount` (PERL) | Magnitude: 31.04 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 34, branch: 33, io: 21, bitwise_ops: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `t/spamd_prefork_stress_4.t` (PERL) | Magnitude: 46.92 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 41, state_mutation: 30, branch: 22, structural_boundaries: 19
- `backend/nitemc/extract_to_rsync_dir` (SHELL) | Magnitude: 57.28 | Delta: **0.208 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: safety_bypasses: 25, branch: 24, state_mutation: 22, io: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `masses/bayes-testing/map-s-space/bayes-analyse-from-raw-counts` (PERL) | Magnitude: 55.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 387, indent_spaces: 238, structural_boundaries: 112, encapsulation: 87
- `masses/lint-rules-from-freqs` (PERL) | Magnitude: 329.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 196, state_mutation: 195, branch: 172, bitwise_ops: 49
- `t/spamd_hup.t` (PERL) | Magnitude: 24.84 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, test: 10, branch: 9, state_mutation: 9
- `t/spamd_prefork_stress.t` (PERL) | Magnitude: 30.74 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 15, branch: 13, indent_spaces: 9, structural_boundaries: 7
- `masses/model-statistics` (PERL) | Magnitude: 66.62 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 57, indent_tabs: 26, structural_boundaries: 14, encapsulation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sql/neural_pg.sql` (SQLITE) | Magnitude: 10.96 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, duplicate_logic: 9, func_start: 7, class_start: 2
- `sql/decodeshorturl_mysql.sql` (SQLITE) | Magnitude: 1.56 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 5, class_start: 1, safety: 1, dead_code: 1
- `sql/decodeshorturl_pg.sql` (SQLITE) | Magnitude: 1.56 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, class_start: 1, safety: 1, dead_code: 1
- `sql/redirectors_mysql.sql` (SQLITE) | Magnitude: 1.56 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 5, class_start: 1, safety: 1, dead_code: 1
- `sql/redirectors_pg.sql` (SQLITE) | Magnitude: 1.56 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, class_start: 1, safety: 1, dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/bayessql.t` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 2129.41
- `masses/rule-qa/reports-from-logs` -> **Bill Cole** (100.0% isolated ownership) | Magnitude: 764.1
- `t/cross_user_config_leak.t` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 256.24
- `masses/rule-qa/automc/gen_info_xml` -> **Bill Cole** (100.0% isolated ownership) | Magnitude: 181.98
- `debian/bin/genorig.pl` -> **Bill Cole** (100.0% isolated ownership) | Magnitude: 140.26

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `debian/rules` -> **Severity: 0.986** (Embedded: 0.0136 * Error Risk: 72.3979%)
- `t/utf8.t` -> **Severity: 0.249** (Embedded: 0.0039 * Error Risk: 63.9916%)
- `t/debug.t` -> **Severity: 0.163** (Embedded: 0.0019 * Error Risk: 83.9854%)
- `t/date.t` -> **Severity: 0.043** (Embedded: 0.0039 * Error Risk: 11.0202%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `spamc/getopt.h` -> **Severity: 374.397** (Blast Radius: 3.744 * Doc Risk: 99.9991%)
- `spamc/utils.h` -> **Severity: 353.233** (Blast Radius: 4.276 * Doc Risk: 82.6083%)
- `debian/rules` -> **Severity: 302.921** (Blast Radius: 13.064 * Doc Risk: 23.1875%)
- `spamc/libspamc.h` -> **Severity: 264.777** (Blast Radius: 2.679 * Doc Risk: 98.8344%)
- `t/date.t` -> **Severity: 229.977** (Blast Radius: 5.075 * Doc Risk: 45.3157%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
