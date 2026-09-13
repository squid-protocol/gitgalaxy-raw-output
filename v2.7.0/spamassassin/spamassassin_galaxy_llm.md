# ARCHITECTURAL_BRIEF: spamassassin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apache/spamassassin.git` |
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
| Total Artifacts | 1882 |
| Analyzed Artifacts (Scanned) | 518 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1364 |
| Total LOC | 43439 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 27.5% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7455 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3891 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 337 | 34955 | 65.1% |
| SHELL | 58 | 2010 | 11.2% |
| PLAINTEXT | 45 | 4 | 8.7% |
| MARKDOWN | 25 | 0 | 4.8% |
| SQLITE | 22 | 354 | 4.2% |
| C | 15 | 5255 | 2.9% |
| MAKEFILE | 5 | 210 | 1.0% |
| YAML | 3 | 37 | 0.6% |
| PHP | 2 | 5 | 0.4% |
| M4 | 2 | 144 | 0.4% |
| CSS | 1 | 123 | 0.2% |
| JAVASCRIPT | 1 | 339 | 0.2% |
| XML | 1 | 0 | 0.2% |
| CSV | 1 | 3 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 448 | 86.5% |
| Unknown | 4 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 66 | 12.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1364*

**Composition by Extension & Reason:**
- `no_extension`: 239x Unsupported Format (.undeterminable), 75x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.cf`: 236x Excluded (Unsupported Extension: '.cf'), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lm`: 172x Excluded (Unsupported Extension: '.lm')
- `.pm`: 131x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Packed Payload Guard (Impossible Density: 3.45 hits/line)
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
- `.pl`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC), 1x Excluded (Saturation: Line 23 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.3 | 35.7 | 26.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 68.3 | 73.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 1.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 69.3 | 98.2 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 39.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 37.9 | 1.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1313 | 82 | 2 | `spamc/libspamc.c` |
| cleanup | 548 | 157 | 3 | `masses/mass-check` |
| guards | 694 | 202 | 2 | `spamc/libspamc.c` |
| danger | 2088 | 196 | 9 | `masses/bayes-testing/bayes-10pcv-driver` |
| concurrency | 114 | 48 | 0 | `t/SATest.pm` |
| connectivity | 793 | 153 | 4 | `masses/rule-qa/automc/ruleqa.cgi` |
| io | 1478 | 214 | 7 | `masses/mass-check` |
| crypto | 0 | 0 | 0 | - |
| ipc | 98 | 39 | 0 | `spamc/spamc.c` |
| time | 273 | 67 | 1 | `tools/sa-stats.pl` |
| serialization | 4 | 2 | 0 | `tools/github/apply_pr.sh` |
| regex | 1841 | 191 | 8 | `masses/rule-qa/automc/ruleqa.cgi` |
| events | 42 | 18 | 0 | `masses/rule-qa/automc/sorttable.js` |
| tests | 1379 | 236 | 5 | `t/uri.t` |
| docs | 95 | 25 | 0 | `spamc/spamc.pod` |
| debt | 1792 | 271 | 10 | `masses/mass-check` |
| mutation | 9488 | 409 | 34 | `spamc/libspamc.c` |
| dead_code | 233 | 88 | 1 | `masses/mass-check` |
| credential | 8 | 2 | 0 | `t/uri.t` |
| threat | 136 | 47 | 0 | `spamc/libspamc.c` |
| ml_ai | 329 | 68 | 2 | `masses/mass-check` |
| ui | 81 | 6 | 0 | `masses/rule-qa/automc/ruleqa.cgi` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `masses/mass-check` (Hits: 80)
- `masses/rule-dev/sought/mkzone_remote_svn/run` (Hits: 57)
- `masses/rule-dev/sought/mkzone/run_part2` (Hits: 54)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **rules** (`debian/rules`) — 8 inbound connections
2. **utils.h** (`spamc/utils.h`) — 3 inbound connections
3. **date.t** (`t/date.t`) — 2 inbound connections
4. **utf8.t** (`t/utf8.t`) — 2 inbound connections
5. **spamassassin.install** (`debian/spamassassin.install`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mass-check** (`masses/mass-check`) — 45 outbound dependencies
2. **SATest.pm** (`t/SATest.pm`) — 35 outbound dependencies
3. **spamc.c** (`spamc/spamc.c`) — 28 outbound dependencies
4. **ruleqa.cgi** (`masses/rule-qa/automc/ruleqa.cgi`) — 24 outbound dependencies
5. **libspamc.c** (`spamc/libspamc.c`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_opensocket` (@ `spamc/libspamc.c`) -> Impact: **926.1** | LOC: 2243
  * *Intent:* /* * opensocket() * * Given a socket family (PF_INET or PF_INET6 or PF_UNIX), try to * create this socket and store the FD in the pointed-to place. * ...
- `set_config` (@ `rulesrc/sandbox/dos/SIQ.pm`) -> Impact: **342.0** | LOC: 214
- `generate_messages` (@ `masses/mass-check`) -> Impact: **243.6** | LOC: 267
  * *Intent:* # Input: # - Number of messages to generate (scalar) # - Hash of Arrays of outstanding requests (reference to hash of array refs) # timestamp# -> [ nu...
- `adapt` (@ `masses/garescorer.c`) -> Impact: **237.4** | LOC: 197
  * *Intent:* #ifdef LAMARCK
- `gen_class` (@ `masses/rule-qa/corpus-hourly`) -> Impact: **221.6** | LOC: 272
- `read_args` (@ `spamc/spamc.c`) -> Impact: **220.1** | LOC: 381
  * *Intent:* /** * Does the command line parsing for argv[]. * * Returns EX_OK or EX_TEMPFAIL if successful. EX_TEMPFAIL is a kludge for * the cases where we want ...
- `message_filter` (@ `spamc/libspamc.c`) -> Impact: **182.0** | LOC: 375
- `wanted` (@ `masses/mass-check`) -> Impact: **181.0** | LOC: 240
- `myMutation` (@ `masses/garescorer.c`) -> Impact: **179.2** | LOC: 230
  * *Intent:* * This mutation function tosses a weighted coin for each allele. * If the allele is to be mutated, then the way it's mutated is to regress it * toward...
- `client_mode` (@ `masses/mass-check`) -> Impact: **148.3** | LOC: 387
  * *Intent:* # this is the function that implements client mode. generally, in a loop: # make a request of the server for some max number of messages, and send our...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `spamd-apache2/t/certs` | 3 | 10012.22 | 0.0% | 0.0% |
| `t` | 230 | 9527.6 | 32.83% | 15.22% |
| `masses` | 36 | 8176.94 | 58.83% | 7.62% |
| `debian` | 10 | 5144.2 | 3.51% | 0.0% |
| `spamc` | 16 | 5031.36 | 31.35% | 24.36% |
| `t/data/etc` | 2 | 5001.0 | 0.0% | 0.0% |
| `masses/rule-qa/automc` | 6 | 2747.55 | 41.31% | 5.45% |
| `masses/rule-qa` | 14 | 2073.08 | 58.37% | 8.88% |
| `rulesrc/sandbox/dos` | 1 | 1190.18 | 61.53% | 12.73% |
| `masses/corpora` | 7 | 979.54 | 58.54% | 8.19% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `masses/plugins/HitFreqsRuleTiming.pm` -> **99.9976%** Exposure
- `t/spamd_maxsize.t` -> **99.9877%** Exposure
- `t/data/taintcheckplugin.pm` -> **99.9842%** Exposure
- `spamc/libspamc.h` -> **99.9295%** Exposure
- `tools/sysreport` -> **99.9245%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `contrib/mbox-to-check` -> **100.0%** Exposure
- `masses/bayes-testing/bayes-static-thresholds` -> **100.0%** Exposure
- `masses/bayes-testing/bayes-tcr-from-freqs` -> **100.0%** Exposure
- `masses/bayes-testing/bayes-thresholds` -> **100.0%** Exposure
- `masses/bayes-testing/draw-bayes-histogram` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `spamc/libspamc.c` -> **10** Orphaned Functions | **0** Duplicates
- `Makefile.PL` -> **7** Orphaned Functions | **0** Duplicates
- `tools/sysreport` -> **7** Orphaned Functions | **0** Duplicates
- `masses/plugins/HitFreqsRuleTiming.pm` -> **4** Orphaned Functions | **0** Duplicates
- `spamc/utils.c` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `86` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1770` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/SATest.pm` (PERL) -> Cumulative Risk: **718.35**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1219.32 | **LOC:** 1258 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `sa_t_init` (Impact: 106.8), `start_spamd` (Impact: 66.1), `patterns_run_cb` (Impact: 45.5)

### 2. `spamd-apache2/bin/apache-spamd.pl` (PERL) -> Cumulative Risk: **670.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 244.5 | **LOC:** 368 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.4432%)
- **Heaviest Functions:** `mpm_specific_config` (Impact: 26.0), `get_libexecdir_apxs` (Impact: 6.5), `apache_module_path` (Impact: 6.0)

### 3. `masses/rule-qa/automc/sorttable.js` (JAVASCRIPT) -> Cumulative Risk: **636.88**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 633.08 | **LOC:** 496 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.9599%)
- **Heaviest Functions:** `makeSortable` (Impact: 41.5), `getInnerText` (Impact: 33.4), `guessType` (Impact: 22.4)

### 4. `masses/mass-check` (PERL) -> Cumulative Risk: **633.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2349.06 | **LOC:** 2679 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.2329%)
- **Heaviest Functions:** `generate_messages` (Impact: 243.6), `wanted` (Impact: 181.0), `client_mode` (Impact: 148.3)

### 5. `spamd-apache2/bin/Bench-spamd.pl` (PERL) -> Cumulative Risk: **632.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 179.06 | **LOC:** 232 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7262%), Tech Debt (88.9708%)
- **Heaviest Functions:** `mux_input` (Impact: 28.2), `headers` (Impact: 25.7), `body` (Impact: 16.6)

### 6. `Makefile.PL` (PERL) -> Cumulative Risk: **626.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 498.12 | **LOC:** 1141 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9966%), Safety Score (86.2379%)
- **Heaviest Functions:** `MY::postamble` (Impact: 71.2), `MY::constants` (Impact: 37.6), `MY::dist` (Impact: 12.5)

### 7. `spamc/libspamc.c` (C) -> Cumulative Risk: **613.08**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3050.04 | **LOC:** 2465 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.993%)
- **Heaviest Functions:** `_opensocket` (Impact: 926.1), `message_filter` (Impact: 182.0), `message_tell` (Impact: 136.6)

### 8. `t/dnsbl_subtests.t` (PERL) -> Cumulative Risk: **604.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 207.54 | **LOC:** 390 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.846%), Safety Score (78.5521%)
- **Heaviest Functions:** `reply_handler` (Impact: 46.8), `find_free_port` (Impact: 30.7), `process_sample_urls` (Impact: 19.9)

### 9. `spamc/utils.c` (C) -> Cumulative Risk: **603.88**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 204.28 | **LOC:** 271 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (91.3168%)
- **Heaviest Functions:** `fd_timeout_read` (Impact: 26.7), `ssl_timeout_read` (Impact: 20.0), `full_write` (Impact: 19.3)

### 10. `masses/rule-qa/reports-from-logs` (PERL) -> Cumulative Risk: **595.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 631.3 | **LOC:** 714 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (93.1104%)
- **Heaviest Functions:** `gen_class` (Impact: 123.7), `gen_report_freqs_all` (Impact: 45.6), `locate_input` (Impact: 40.0)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamc/libspamc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3050.04 | **LOC:** 2465 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.3288%), Tech Debt (32.0999%)
**Top Internal Functions/Classes:**
  * `_opensocket` (Impact: 926.1)
    * *Intent:* /* * opensocket() * * Given a socket family (PF_INET or PF_INET6 or PF_UNIX), try to * create this s...
  * `message_filter` (Impact: 182.0)
  * `message_tell` (Impact: 136.6)
  * `transport_setup` (Impact: 113.0)
    * *Intent:* * transport_setup() * * Given a "transport" object that says how we're to connect to the * spam daem...
  * `_opensocket` (Impact: 89.5)
    * *Intent:* #else
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 16 instances
* *Amplified Cascading Flux:* 332 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1033
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 424`, `structural_boundaries: 208`, `args: 51`, `func_start: 37`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 1`, `state_mutation: 369`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 10`
* *Architecture:* `io: 12`, `api: 18`, `import: 24`
* *Defense:* `safety: 42`, `immutability_locks: 18`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` inet.h, assert.h, config.h, errno.h, io.h, libspamc.h, in.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/mass-check` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2349.06 | **LOC:** 2679 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.5295%), Tech Debt (10.2899%)
**Top Internal Functions/Classes:**
  * `generate_messages` (Impact: 243.6)
    * *Intent:* # Input: # - Number of messages to generate (scalar) # - Hash of Arrays of outstanding requests (ref...
  * `wanted` (Impact: 181.0)
  * `client_mode` (Impact: 148.3)
    * *Intent:* # this is the function that implements client mode. generally, in a loop: # make a request of the se...
  * `usage` (Impact: 75.4)
  * `http_make_request` (Impact: 59.6)
    * *Intent:* # the client needs to make a request to the server on a given socket.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 22 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 323 instances
* *Concurrency (weighted view):* 36
* *Memory Alloc (weighted view):* 9
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 1008
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 762`, `structural_boundaries: 434`, `args: 25`, `func_start: 38`
* *Risk/State:* `high_risk_execution: 15`, `state_mutation: 362`, `dead_code: 27`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 80`, `api: 39`, `concurrency: 6`, `import: 39`
* *Defense:* `safety: 7`, `cleanup: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Config, Fcntl, File::Copy, File::Spec, FindBin, Getopt::Long, IO::Select, IO::Socket...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/automc/ruleqa.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1971.72 | **LOC:** 2189 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0843%), Tech Debt (12.828%)
**Top Internal Functions/Classes:**
  * `show_default_view` (Impact: 124.6)
  * `read_freqs_file` (Impact: 116.7)
  * `get_freqs_for_rule` (Impact: 72.6)
  * `generate_scoremap_chart` (Impact: 61.0)
  * `assemble_url` (Impact: 49.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 233 instances
* *Memory Alloc (weighted view):* 8
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 733
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 529`, `structural_boundaries: 496`, `args: 64`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 267`, `dead_code: 6`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 25`, `api: 65`, `import: 18`
* *Defense:* `safety: 12`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CGI, CGI::Carp, Compress::LZ4, Data::Dumper, Date::Manip, POSIX, Storable, Time::Local...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/garescorer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1599.16 | **LOC:** 1314 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.7895%), Tech Debt (19.4445%)
**Top Internal Functions/Classes:**
  * `adapt` (Impact: 237.4)
    * *Intent:* #ifdef LAMARCK
  * `myMutation` (Impact: 179.2)
    * *Intent:* * This mutation function tosses a weighted coin for each allele. * If the allele is to be mutated, t...
  * `Crossover` (Impact: 110.9)
    * *Intent:* /***************************************************************************** * Crossover implement...
  * `main` (Impact: 54.1)
  * `showSummary` (Impact: 40.6)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 267 instances
* *State Mutation (weighted view):* 821
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 66`, `args: 42`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 287`, `dead_code: 1`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 34`, `import: 6`
* *Defense:* `doc: 6`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math.h, pgapack.h, time.h, scores.h, tests.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/SATest.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1219.32 | **LOC:** 1258 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.3121%), Tech Debt (22.247%)
**Top Internal Functions/Classes:**
  * `sa_t_init` (Impact: 106.8)
    * *Intent:* # Set up for testing. Exports (as global vars): # out: $home: $HOME env variable # out: $cwd: here #...
  * `start_spamd` (Impact: 66.1)
    * *Intent:* # out: $spamd_stderr
  * `patterns_run_cb` (Impact: 45.5)
    * *Intent:* # ---------------------------------------------------------------------------
  * `spamcrun` (Impact: 38.3)
  * `ok_all_patterns` (Impact: 34.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 180 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 559
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 251`, `args: 38`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 199`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 7`
* *Architecture:* `io: 30`, `api: 53`, `import: 22`
* *Defense:* `safety: 6`, `test: 6`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Config, Cwd, Exporter, File::Basename, File::Copy, File::Path, File::Spec, File::Temp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rulesrc/sandbox/dos/SIQ.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1190.18 | **LOC:** 1162 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.5304%), Tech Debt (12.7294%)
**Top Internal Functions/Classes:**
  * `set_config` (Impact: 342.0)
  * `_parse_eval_call` (Impact: 115.5)
  * `_send_siq_query` (Impact: 82.5)
  * `_harvest_siq_responses` (Impact: 55.9)
  * `parsed_metadata` (Impact: 46.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 415`, `structural_boundaries: 210`, `args: 24`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 70`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 20`, `api: 9`, `import: 23`
* *Defense:* `safety: 2`, `doc: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Fcntl, IO::Socket, Mail::SpamAssassin::Logger, Mail::SpamAssassin::Plugin, Outbound, SIQ, Socket, aggregated...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamc/spamc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1003.62 | **LOC:** 1117 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.6115%), Tech Debt (24.4552%)
**Top Internal Functions/Classes:**
  * `read_args` (Impact: 220.1)
    * *Intent:* /** * Does the command line parsing for argv[]. * * Returns EX_OK or EX_TEMPFAIL if successful. EX_T...
  * `main` (Impact: 133.6)
  * `combine_args` (Impact: 50.6)
    * *Intent:* /* combine_args() :: parses spamc.conf for options, and combines those * with options passed via com...
  * `print_usage` (Impact: 30.9)
  * `get_output_fd` (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 161 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 506
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 68`, `args: 23`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 184`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 7`
* *Architecture:* `io: 1`, `api: 11`, `import: 28`
* *Defense:* `doc: 3`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` inet.h, config.h, errno.h, fcntl.h, getopt.h, io.h, libspamc.h, netdb.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/corpora/mk-corpus-link-farm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 668.46 | **LOC:** 844 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.3181%), Tech Debt (12.4616%)
**Top Internal Functions/Classes:**
  * `_mbox_extract_all` (Impact: 72.2)
  * `parse_rfc822_date` (Impact: 72.2)
  * `_mklink` (Impact: 53.3)
  * `dist_across_dests` (Impact: 17.2)
  * `find_srcs` (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 102 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 203`, `args: 15`, `func_start: 22`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 111`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 21`, `import: 13`
* *Defense:* `safety: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cwd, Data::Dumper, Fcntl, File::Basename, File::Find, File::Path, Getopt::Long, RFC...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/automc/sorttable.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 633.08 | **LOC:** 496 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.386%), Tech Debt (19.8801%)
**Top Internal Functions/Classes:**
  * `makeSortable` (Impact: 41.5)
  * `getInnerText` (Impact: 33.4)
  * `guessType` (Impact: 22.4)
  * `innerSortFunction` (Impact: 19.1)
  * `forEach` (Impact: 19.0)
    * *Intent:* // globally resolve forEach enumeration
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 120 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 65`, `args: 25`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 3`, `state_mutation: 127`, `dead_code: 7`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/reports-from-logs` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 631.3 | **LOC:** 714 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (82.3065%), Tech Debt (10.3692%)
**Top Internal Functions/Classes:**
  * `gen_class` (Impact: 123.7)
  * `gen_report_freqs_all` (Impact: 45.6)
    * *Intent:* # ---------------------------------------------------------------------------
  * `locate_input` (Impact: 40.0)
    * *Intent:* # ---------------------------------------------------------------------------
  * `start_hit_frequencies_at_rev` (Impact: 30.4)
    * *Intent:* # ---------------------------------------------------------------------------
  * `time_filter_fileset` (Impact: 27.8)
    * *Intent:* # ---------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 69 instances
* *Memory Alloc (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 179`, `args: 14`, `func_start: 21`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 76`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `io: 18`, `api: 22`, `import: 14`
* *Defense:* `safety: 3`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cwd, File::Copy, File::Path, Getopt::Long, POSIX, Time::ParseDate, constant, data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/hit-frequencies` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 610.7 | **LOC:** 1036 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.8812%), Tech Debt (10.6369%)
**Top Internal Functions/Classes:**
  * `_print_overlap_ratios` (Impact: 68.7)
  * `readlogs` (Impact: 43.8)
  * `compute_overlaps_for_rule` (Impact: 29.7)
  * `_print_scoremap` (Impact: 21.0)
  * `_hmap_to_overlap_ratio` (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 123 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 198`, `args: 8`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 123`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `api: 6`, `import: 6`
* *Defense:* `safety: 5`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` FindBin, Getopt::Long, Pod::Usage, hits, less, results, rules, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-dev/seek-phrases-in-log` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 542.64 | **LOC:** 710 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.6887%), Tech Debt (13.9595%)
**Top Internal Functions/Classes:**
  * `assemble_regexps` (Impact: 39.0)
  * `expand_with_dots` (Impact: 37.0)
  * `subsume_with_dotstars` (Impact: 33.7)
  * `collapse_pats` (Impact: 32.5)
  * `usage` (Impact: 23.8)
    * *Intent:* # (the "License"); you may not use this file except in compliance with # the License. You may obtain...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 86 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 133`, `args: 10`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 104`, `dead_code: 3`, `planned_debt: 5`
* *Architecture:* `io: 9`, `api: 18`, `import: 5`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dumper, Digest::SHA, Getopt::Long, N, longer, need, non, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/corpus-hourly` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 519.34 | **LOC:** 524 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.6211%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gen_class` (Impact: 221.6)
  * `locate` (Impact: 31.9)
  * `sort_all` (Impact: 18.8)
  * `update_rsync` (Impact: 14.8)
  * `current` (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 8 instances
* *Amplified Cascading Flux:* 57 instances
* *Sec Tainted Injection (weighted view):* 8
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 124`, `args: 3`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 63`, `dead_code: 4`
* *Architecture:* `io: 25`, `api: 10`, `import: 11`
* *Defense:* `safety: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cwd, File::Copy, File::Path, Getopt::Long, POSIX, Time::ParseDate, age, constant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile.PL` (PERL | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 498.12 | **LOC:** 1141 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.4347%), Tech Debt (70.9797%)
**Top Internal Functions/Classes:**
  * `MY::postamble` (Impact: 71.2)
  * `MY::constants` (Impact: 37.6)
    * *Intent:* # Now override the constants routine to add our own macros.
  * `MY::dist` (Impact: 12.5)
    * *Intent:* # Override some vars in the dist section.
  * `_set_macro_SYSCONFDIR` (Impact: 12.3)
    * *Intent:* # repository. # # The first parameter must be one value from @REPOSITORIES. # # *SYSCONFDIR can be o...
  * `_set_macro_LOCALSTATEDIR` (Impact: 12.3)
    * *Intent:* # repository. # # The first parameter must be one value from @REPOSITORIES. # # *LOCALSTATEDIR can b...
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 70 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 170`, `args: 8`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 81`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 20`, `import: 12`
* *Defense:* `safety: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Config, DBI, ExtUtils::MakeMaker, Mail::SpamAssassin::Util::DependencyInfo, TEST_REQUIRES, a, constant, for...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/perceptron.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 465.64 | **LOC:** 481 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.1306%), Tech Debt (11.5663%)
**Top Internal Functions/Classes:**
  * `train` (Impact: 40.8)
    * *Intent:* /* Trains the perceptron using stochastic gradient descent. */
  * `main` (Impact: 28.2)
  * `write_weights` (Impact: 27.1)
    * *Intent:* /* Writes out the weights in SpamAssassin score space. */
  * `get_random_test` (Impact: 12.4)
    * *Intent:* /* Get a random test using roulette wheel selection. This is not used anymore. */
  * `usage` (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 96 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 33`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 97`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 23`, `import: 8`
* *Defense:* `safety: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, math.h, stdio.h, stdlib.h, time.h, scores.h, tests.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamc/getopt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 422.34 | **LOC:** 352 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.5136%), Tech Debt (14.0027%)
**Top Internal Functions/Classes:**
  * `spamc_getopt_long` (Impact: 125.5)
  * `spamc_getopt` (Impact: 46.0)
  * `main` (Impact: 30.4)
    * *Intent:* #ifdef TESTGETOPT
  * `optiserr` (Impact: 25.2)
  * `longoptiserr` (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 54 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 47`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 54`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 4`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, errno.h, getopt.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/bayes-testing/map-s-space/bayes-analyse-from-raw-counts` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 412.34 | **LOC:** 430 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.6188%), Tech Debt (12.5746%)
**Top Internal Functions/Classes:**
  * `compute_thresholds` (Impact: 27.1)
  * `brc_line_to_score` (Impact: 26.4)
  * `compute_prob_for_token` (Impact: 19.3)
  * `draw_hist` (Impact: 17.9)
  * `cached_compute_prob_for_token` (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 112`, `args: 7`, `func_start: 9`
* *Risk/State:* `state_mutation: 91`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 9`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, POSIX, Robinson, a, constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rewrite-cf-with-new-scores` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 411.76 | **LOC:** 522 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.4522%), Tech Debt (10.4253%)
**Top Internal Functions/Classes:**
  * `generate_scores` (Impact: 33.2)
  * `fixup_meta_predicates` (Impact: 31.2)
  * `build_new_scores` (Impact: 26.2)
  * `read_gascores` (Impact: 17.4)
  * `read_oldscores` (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 69 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 85`, `args: 6`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 69`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 14`, `import: 5`
* *Defense:* `safety: 2`, `doc: 1`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GA, Getopt::Long, Pod::Usage, new, options, strict, the, this...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/logs-to-c` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 365.64 | **LOC:** 595 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.8534%), Tech Debt (15.4434%)
**Top Internal Functions/Classes:**
  * `read_ranges` (Impact: 65.3)
  * `writetests_c` (Impact: 22.9)
  * `readlogs` (Impact: 21.1)
  * `writescores_c` (Impact: 15.7)
  * `readscores` (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 71 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 67`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 75`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`, `api: 8`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` C, Getopt::Long, default, hits, need, strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/lint-rules-from-freqs` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 362.66 | **LOC:** 339 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (14.254%)
**Top Internal Functions/Classes:**
  * `readrules` (Impact: 63.0)
    * *Intent:* # note: do not use parse-rules-for-masses here, we need to do linting instead # of your average pars...
  * `lintrules` (Impact: 61.1)
  * `usage` (Impact: 15.2)
  * `concat_rule_lang` (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 41`, `args: 2`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 69`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 4`, `import: 5`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` description, matches, parse, rule, score, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/rule-hits-over-time` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 344.44 | **LOC:** 530 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0266%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `plot_gp` (Impact: 35.5)
  * `read_logs` (Impact: 29.9)
  * `summarise` (Impact: 20.2)
  * `usage` (Impact: 11.8)
  * `collapse_periods` (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 66 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 109`, `args: 4`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 67`, `dead_code: 1`
* *Architecture:* `io: 9`, `api: 10`, `import: 10`
* *Defense:* `safety: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CGI, Fcntl, GD, Getopt::Long, POSIX, SDBM_File, Statistics::DEA, an...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/SATest.pm` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 1219.32
- `masses/rule-qa/reports-from-logs` -> **Bill Cole** (100.0% isolated ownership) | Magnitude: 631.3
- `t/cross_user_config_leak.t` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 220.66
- `masses/rule-qa/automc/gen_info_xml` -> **Bill Cole** (100.0% isolated ownership) | Magnitude: 139.88
- `t/uri.t` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 90.0

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `debian/rules` -> **Severity: 0.978** (Embedded: 0.0154 * Error Risk: 63.308%)
- `t/utf8.t` -> **Severity: 0.3** (Embedded: 0.0039 * Error Risk: 77.6735%)
- `t/header.t` -> **Severity: 0.138** (Embedded: 0.0019 * Error Risk: 71.2812%)
- `t/debug.t` -> **Severity: 0.126** (Embedded: 0.0019 * Error Risk: 65.2163%)
- `t/plugin.t` -> **Severity: 0.123** (Embedded: 0.0019 * Error Risk: 63.9091%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `debian/rules` -> **Severity: 1453.0** (Blast Radius: 14.53 * Doc Risk: 100.0%)
- `t/date.t` -> **Severity: 502.9** (Blast Radius: 5.029 * Doc Risk: 100.0%)
- `Makefile.PL` -> **Severity: 186.3** (Blast Radius: 1.863 * Doc Risk: 100.0%)
- `debian/bin/genorig.pl` -> **Severity: 186.3** (Blast Radius: 1.863 * Doc Risk: 100.0%)
- `masses/bayes-testing/bayes-static-thresholds` -> **Severity: 186.3** (Blast Radius: 1.863 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
