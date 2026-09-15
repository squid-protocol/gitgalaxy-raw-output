# ARCHITECTURAL_BRIEF: tcpip_historical
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/weiss/original-bsd.git` |
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
| Total Artifacts | 4910 |
| Analyzed Artifacts (Scanned) | 133 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4777 |
| Total LOC | 14876 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 2.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3474 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1447 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4569 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 130 | 14864 | 97.7% |
| MAKEFILE | 1 | 11 | 0.8% |
| MARKDOWN | 1 | 0 | 0.8% |
| PLAINTEXT | 1 | 1 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z +0.65; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 77%, Data / Markup / Trivial 7%, C Struct Operations Files 5%, Large Core Modules 5%, Many-Argument Workhorses Files 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 131 | 98.5% |
| Unknown | 1 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4777*

**Composition by Extension & Reason:**
- `.c`: 2094x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 585x Excluded: Neighborhood Micro-Mass Limit Exceeded, 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 331x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `no_extension`: 189x Excluded: Neighborhood Micro-Mass Limit Exceeded, 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.distribution')
- `.3`: 213x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.2`: 98x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.f`: 90x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.p`: 69x Excluded (Unsupported Extension: '.p')
- `.4`: 57x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.ms`: 46x Excluded (Unsupported Extension: '.ms')
- `.n`: 46x Excluded (Unsupported Extension: '.n')
- `.out`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.me`: 43x Excluded (Unsupported Extension: '.me')
- `.afm`: 36x Excluded (Unsupported Extension: '.afm')
- `.mod`: 29x Excluded (Unsupported Extension: '.mod')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 90.5 | 16.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 17.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.3 | 15.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 12.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 25.1 | 8.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 80.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4726 | 82 | 126 | `sys/netinet/tcp_input.c` |
| cleanup | 13 | 5 | 0 | `sys/netinet/ip_mroute.c` |
| guards | 197 | 31 | 4 | `sys/sys/vnode_if.h` |
| danger | 27 | 9 | 0 | `sys/netinet/in_cksum.c` |
| concurrency | 1 | 1 | 0 | `sys/sys/proc.h` |
| connectivity | 1089 | 111 | 19 | `sys/sys/vnode_if.h` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 115 | 32 | 2 | `sys/sys/socketvar.h` |
| time | 12 | 7 | 0 | `sys/sys/shm.h` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 10 | 6 | 0 | `sys/sys/syslog.h` |
| tests | 0 | 0 | 0 | - |
| docs | 3 | 3 | 0 | `sys/netinet/tcp_debug.c` |
| debt | 104 | 38 | 2 | `sys/netinet/tcp_debug.c` |
| mutation | 2802 | 27 | 85 | `sys/netinet/tcp_input.c` |
| dead_code | 168 | 44 | 4 | `sys/sys/sysctl.h` |
| credential | 0 | 0 | 0 | - |
| threat | 438 | 66 | 9 | `sys/netinet/ip_input.c` |
| ml_ai | 104 | 9 | 0 | `sys/netinet/in_pcb.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 0)
- `README` (Hits: 0)
- `sys/netinet/icmp_var.h` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **cdefs.h** (`sys/sys/cdefs.h`) — 21 inbound connections
2. **param.h** (`sys/sys/param.h`) — 18 inbound connections
3. **socket.h** (`sys/sys/socket.h`) — 18 inbound connections
4. **in.h** (`sys/netinet/in.h`) — 17 inbound connections
5. **in_systm.h** (`sys/netinet/in_systm.h`) — 17 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **in_proto.c** (`sys/netinet/in_proto.c`) — 26 outbound dependencies
2. **tcp_input.c** (`sys/netinet/tcp_input.c`) — 23 outbound dependencies
3. **tcp_subr.c** (`sys/netinet/tcp_subr.c`) — 23 outbound dependencies
4. **tcp_usrreq.c** (`sys/netinet/tcp_usrreq.c`) — 23 outbound dependencies
5. **tcp_timer.c** (`sys/netinet/tcp_timer.c`) — 22 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `tcp_input` **(Many-Argument Workhorses)** (@ `sys/netinet/tcp_input.c`) -> Impact: **464.7** | LOC: 1119
  * *Intent:* /* * TCP input routine, follows pages 65-76 of the * protocol specification dated September, 1981 very closely. */
- `tcp_output` **(Compute Cores)** (@ `sys/netinet/tcp_output.c`) -> Impact: **172.8** | LOC: 515
  * *Intent:* #endif #define MAX_TCPOPTLEN 32 /* max # bytes that go in options */ /* * Tcp output routine: figure out what should be sent and send it. */
- `tcp_usrreq` **(Many-Argument Workhorses)** (@ `sys/netinet/tcp_usrreq.c`) -> Impact: **155.8** | LOC: 274
  * *Intent:* /* * Process a TCP user request for TCP tb. If this is a send request * then m is the mbuf chain of send data. If this is a timer expiration * (called...
- `ip_output` **(Many-Argument Workhorses)** (@ `sys/netinet/ip_output.c`) -> Impact: **155.7** | LOC: 321
  * *Intent:* /* * IP output. The packet in mbuf chain m contains a skeletal IP * header (with len, off, ttl, proto, tos, src, dst). * The mbuf chain containing the...
- `ip_ctloutput` **(Many-Argument Workhorses)** (@ `sys/netinet/ip_output.c`) -> Impact: **147.0** | LOC: 147
  * *Intent:* /* * IP socket option processing. */
- `icmp_input` **(Many-Argument Workhorses)** (@ `sys/netinet/ip_icmp.c`) -> Impact: **122.6** | LOC: 234
  * *Intent:* /* * Process a received ICMP message. */
- `ip_setmoptions` **(Many-Argument Workhorses)** (@ `sys/netinet/ip_output.c`) -> Impact: **111.8** | LOC: 235
  * *Intent:* /* * Set the IP multicast options in response to user setsockopt(). */
- `rip_usrreq` **(Many-Argument Workhorses)** (@ `sys/netinet/raw_ip.c`) -> Impact: **110.7** | LOC: 156
  * *Intent:* /*ARGSUSED*/
- `udp_usrreq` **(Many-Argument Workhorses)** (@ `sys/netinet/udp_usrreq.c`) -> Impact: **92.5** | LOC: 136
  * *Intent:* /* 40 1K datagrams */ /*ARGSUSED*/
- `rip_ctloutput` **(Many-Argument Workhorses)** (@ `sys/netinet/raw_ip.c`) -> Impact: **92.1** | LOC: 78
  * *Intent:* /* * Raw IP socket option processing. */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `sys/netinet` | 41 | 9737.66 | 38.33% | 23.29% |
| `games/phantasia` | 1 | 5000.0 | 0.0% | 0.0% |
| `sys/sys` | 89 | 2555.72 | 5.76% | 10.59% |
| `__monolith__` | 2 | 15.0 | 3.49% | 36.55% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `sys/sys/signalvar.h` -> **99.2508%** Exposure
- `sys/sys/ttydefaults.h` -> **98.9013%** Exposure
- `sys/netinet/tcp_timer.c` -> **97.023%** Exposure
- `sys/netinet/igmp.c` -> **95.2456%** Exposure
- `sys/sys/conf.h` -> **90.8422%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `sys/netinet/if_ether.c` -> **100.0%** Exposure
- `sys/netinet/igmp.c` -> **100.0%** Exposure
- `sys/netinet/in.c` -> **100.0%** Exposure
- `sys/netinet/in_cksum.c` -> **100.0%** Exposure
- `sys/netinet/in_pcb.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sys/netinet/in_pcb.c` -> **7** Orphaned Functions | **0** Duplicates
- `sys/netinet/ip_input.c` -> **7** Orphaned Functions | **0** Duplicates
- `sys/netinet/tcp_subr.c` -> **7** Orphaned Functions | **0** Duplicates
- `sys/netinet/igmp.c` -> **5** Orphaned Functions | **0** Duplicates
- `sys/netinet/if_ether.c` -> **4** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `429` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `sys/netinet/tcp_timer.c` (C) -> Cumulative Risk: **663.88**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.59)
- **Magnitude:** 227.76 | **LOC:** 311 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.8368%)
- **Heaviest Functions:** `tcp_timers` (Many-Argument Workhorses, Impact: 46.5), `tcp_slowtimo` (I/O & Config Routines, Impact: 13.2), `tcp_fasttimo` (I/O & Config Routines, Impact: 6.0)

### 2. `sys/netinet/in_pcb.c` (C) -> Cumulative Risk: **650.95**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z +1.48)
- **Magnitude:** 478.02 | **LOC:** 472 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.0989%)
- **Heaviest Functions:** `in_pcbconnect` (Compute Cores, Impact: 61.3), `in_pcblookup` (Many-Argument Workhorses, Impact: 55.2), `in_pcbnotify` (Many-Argument Workhorses, Impact: 50.6)

### 3. `sys/netinet/igmp.c` (C) -> Cumulative Risk: **642.88**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z +1.67)
- **Magnitude:** 199.42 | **LOC:** 292 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.2958%)
- **Heaviest Functions:** `igmp_input` (Many-Argument Workhorses, Impact: 42.8), `igmp_fasttimo` (I/O & Config Routines, Impact: 8.4), `igmp_joingroup` (C Struct Operations, Impact: 6.5)

### 4. `sys/netinet/udp_usrreq.c` (C) -> Cumulative Risk: **642.68**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.12)
- **Magnitude:** 515.08 | **LOC:** 615 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.081%)
- **Heaviest Functions:** `udp_usrreq` (Many-Argument Workhorses, Impact: 92.5), `udp_input` (Many-Argument Workhorses, Impact: 81.0), `udp_output` (Many-Argument Workhorses, Impact: 28.9)

### 5. `sys/netinet/tcp_input.c` (C) -> Cumulative Risk: **636.98**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.18)
- **Magnitude:** 1564.42 | **LOC:** 1635 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.6121%)
- **Heaviest Functions:** `tcp_input` (Many-Argument Workhorses, Impact: 464.7), `tcp_mss` (Many-Argument Workhorses, Impact: 53.5), `tcp_dooptions` (Many-Argument Workhorses, Impact: 51.5)

### 6. `sys/netinet/ip_input.c` (C) -> Cumulative Risk: **630.23**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.30)
- **Magnitude:** 939.72 | **LOC:** 1141 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.9405%)
- **Heaviest Functions:** `ip_forward` (Many-Argument Workhorses, Impact: 67.8), `ip_dooptions` (Compute Cores, Impact: 63.1), `ipintr` (Compute Cores, Impact: 62.9)

### 7. `sys/netinet/raw_ip.c` (C) -> Cumulative Risk: **622.32**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.42)
- **Magnitude:** 405.68 | **LOC:** 386 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.2147%)
- **Heaviest Functions:** `rip_usrreq` (Many-Argument Workhorses, Impact: 110.7), `rip_ctloutput` (Many-Argument Workhorses, Impact: 92.1), `rip_input` (C Struct Operations, Impact: 24.8)

### 8. `sys/netinet/tcp_usrreq.c` (C) -> Cumulative Risk: **620.79**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.18)
- **Magnitude:** 484.34 | **LOC:** 504 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.4175%)
- **Heaviest Functions:** `tcp_usrreq` (Many-Argument Workhorses, Impact: 155.8), `tcp_ctloutput` (Many-Argument Workhorses, Impact: 67.6), `tcp_usrclosed` (Compute Cores, Impact: 15.5)

### 9. `sys/netinet/tcp_subr.c` (C) -> Cumulative Risk: **608.91**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z +1.46)
- **Magnitude:** 376.96 | **LOC:** 420 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.9864%)
- **Heaviest Functions:** `tcp_close` (Compute Cores, Impact: 36.0), `tcp_respond` (Many-Argument Workhorses, Impact: 24.3), `tcp_notify` (Compute Cores, Impact: 18.7)

### 10. `sys/netinet/if_ether.c` (C) -> Cumulative Risk: **603.59**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.44)
- **Magnitude:** 381.38 | **LOC:** 530 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.2519%)
- **Heaviest Functions:** `arpresolve` (Many-Argument Workhorses, Impact: 47.3), `arp_rtrequest` (Many-Argument Workhorses, Impact: 43.2), `in_arpinput` (C Struct Operations, Impact: 37.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `games/phantasia/monsters.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_input.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1564.42 | **LOC:** 1635 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.5439%), Tech Debt (56.6207%)
**Top Internal Functions/Classes:**
  * `tcp_input` **(Many-Argument Workhorses)** (Impact: 464.7)
    * *Intent:* /* * TCP input routine, follows pages 65-76 of the * protocol specification dated September, 1981 ve...
  * `tcp_mss` **(Many-Argument Workhorses)** (Impact: 53.5)
    * *Intent:* * Determine a reasonable value for maxseg size. * If the route is known, check route for mtu. * If n...
  * `tcp_dooptions` **(Many-Argument Workhorses)** (Impact: 51.5)
  * `tcp_reass` **(Many-Argument Workhorses)** (Impact: 45.1)
    * *Intent:* #ifndef TUBA_INCLUDE
  * `tcp_xmit_timer` **(Many-Argument Workhorses)** (Impact: 13.8)
    * *Intent:* /* * Collect new round-trip time estimate * and update averages and current timeout. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 297 instances
* *State Mutation (weighted view):* 899
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 134`, `args: 5`, `func_start: 6`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 305`, `dead_code: 2`, `fragile_debt: 11`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 23`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` cpu.h, if.h, route.h, in.h, in_pcb.h, in_systm.h, ip.h, ip_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/ip_output.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1193.14 | **LOC:** 1039 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.2753%), Tech Debt (18.3025%)
**Top Internal Functions/Classes:**
  * `ip_output` **(Many-Argument Workhorses)** (Impact: 155.7)
    * *Intent:* /* * IP output. The packet in mbuf chain m contains a skeletal IP * header (with len, off, ttl, prot...
  * `ip_ctloutput` **(Many-Argument Workhorses)** (Impact: 147.0)
    * *Intent:* /* * IP socket option processing. */
  * `ip_setmoptions` **(Many-Argument Workhorses)** (Impact: 111.8)
    * *Intent:* /* * Set the IP multicast options in response to user setsockopt(). */
  * `ip_pcbopts` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* /* * Set up IP options in pcb for insertion in output packets. * Store in mbuf with pointer in pcbop...
  * `ip_getmoptions` **(C Struct Operations)** (Impact: 26.2)
    * *Intent:* /* * Return the IP multicast options in response to user getsockopt(). */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 210 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 643
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 178`, `args: 9`, `func_start: 8`, `class_start: 23`
* *Risk/State:* `state_mutation: 223`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 16`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` mtpr.h, if.h, route.h, in.h, in_pcb.h, in_systm.h, in_var.h, ip.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/ip_input.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 939.72 | **LOC:** 1141 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.3766%), Tech Debt (51.0991%)
**Top Internal Functions/Classes:**
  * `ip_forward` **(Many-Argument Workhorses)** (Impact: 67.8)
    * *Intent:* /* * Forward a packet. If some error occurs return the sender * an icmp packet. Note we can't always...
  * `ip_dooptions` **(Compute Cores)** (Impact: 63.1)
    * *Intent:* /* * Do option processing on a datagram, * possibly discarding it if bad options are encountered, * ...
  * `ipintr` **(Compute Cores)** (Impact: 62.9)
    * *Intent:* /* * Ip input routine. Checksum and byte swap header. If fragmented * try to reassemble. Process opt...
  * `ip_reass` **(Many-Argument Workhorses)** (Impact: 36.2)
    * *Intent:* /* * Take incoming datagram fragment and try to * reassemble it into whole datagram. If a chain for ...
  * `ip_sysctl` **(Many-Argument Workhorses)** (Impact: 22.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 599
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 179`, `args: 3`, `func_start: 15`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 209`, `dead_code: 1`, `fragile_debt: 4`, `unreferenced_by_name: 7`
* *Architecture:* `api: 19`, `import: 19`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` if.h, route.h, in.h, in_pcb.h, in_systm.h, in_var.h, ip.h, ip_icmp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/ip_mroute.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 625.16 | **LOC:** 809 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.8977%), Tech Debt (20.365%)
**Top Internal Functions/Classes:**
  * `ip_mrouter_cmd` **(Compute Cores)** (Impact: 67.4)
    * *Intent:* /* * Handle DVMRP setsockopt commands to modify the multicast routing tables. */
  * `ip_mforward` **(Many-Argument Workhorses)** (Impact: 47.3)
    * *Intent:* /* * IP multicast forwarding function. This function assumes that the packet * pointed to by "ip" ha...
  * `add_lgrp` **(Compute Cores)** (Impact: 16.7)
    * *Intent:* /* * Add the multicast group in the lgrpctl to the list of local multicast * group memberships assoc...
  * `add_vif` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* /* * Add a vif to the vif table */
  * `del_vif` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* /* * Delete a vif from the vif table */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 116 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 373
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 144`, `args: 1`, `func_start: 15`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 141`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 21`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` if.h, raw_cb.h, route.h, igmp.h, igmp_var.h, in.h, in_pcb.h, in_systm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/ip_icmp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 555.16 | **LOC:** 566 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (15.6799%)
**Top Internal Functions/Classes:**
  * `icmp_input` **(Many-Argument Workhorses)** (Impact: 122.6)
    * *Intent:* /* * Process a received ICMP message. */
  * `icmp_error` **(Many-Argument Workhorses)** (Impact: 51.1)
    * *Intent:* /* * Generate an error packet of type error * in response to bad packet ip. */
  * `icmp_reflect` **(Compute Cores)** (Impact: 45.5)
    * *Intent:* /* * Reflect the ip packet back to the source */
  * `icmp_sysctl` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `icmp_send` **(C Struct Operations)** (Impact: 4.6)
    * *Intent:* /* * Send an icmp packet back to the ip level, * after supplying a checksum. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 96 instances
* *State Mutation (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 100`, `args: 4`, `func_start: 6`, `class_start: 9`
* *Risk/State:* `state_mutation: 107`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 16`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` if.h, route.h, icmp_var.h, in.h, in_systm.h, in_var.h, ip.h, ip_icmp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/udp_usrreq.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 515.08 | **LOC:** 615 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.8401%), Tech Debt (82.5498%)
**Top Internal Functions/Classes:**
  * `udp_usrreq` **(Many-Argument Workhorses)** (Impact: 92.5)
    * *Intent:* /* 40 1K datagrams */ /*ARGSUSED*/
  * `udp_input` **(Many-Argument Workhorses)** (Impact: 81.0)
  * `udp_output` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `udp_ctlinput` **(C Struct Operations)** (Impact: 13.0)
  * `udp_saveopt` **(C Struct Operations)** (Impact: 5.0)
    * *Intent:* /* * Create a "control" mbuf containing the specified data * with the specified type for presentatio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 119`, `args: 1`, `func_start: 8`, `class_start: 16`
* *Risk/State:* `state_mutation: 97`, `fragile_debt: 5`, `unreferenced_by_name: 4`
* *Architecture:* `api: 8`, `import: 18`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` if.h, route.h, in.h, in_pcb.h, in_systm.h, ip.h, ip_icmp.h, ip_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_usrreq.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 484.34 | **LOC:** 504 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.2512%), Tech Debt (54.2553%)
**Top Internal Functions/Classes:**
  * `tcp_usrreq` **(Many-Argument Workhorses)** (Impact: 155.8)
    * *Intent:* /* * Process a TCP user request for TCP tb. If this is a send request * then m is the mbuf chain of ...
  * `tcp_ctloutput` **(Many-Argument Workhorses)** (Impact: 67.6)
  * `tcp_usrclosed` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /* * User issued close, and wish to trail through shutdown states: * if never received SYN, just for...
  * `tcp_disconnect` **(C Struct Operations)** (Impact: 10.8)
    * *Intent:* /* * Initiate (or continue) disconnect. * If embryonic state, just send reset (once). * If in ``let ...
  * `tcp_attach` **(C Struct Operations)** (Impact: 9.9)
    * *Intent:* /* * Attach TCP protocol to socket, allocating * internet protocol control block, tcp control block,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 78`, `args: 2`, `func_start: 5`, `class_start: 10`
* *Risk/State:* `state_mutation: 72`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 6`, `import: 23`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` if.h, route.h, in.h, in_pcb.h, in_systm.h, ip.h, ip_var.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_output.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 478.46 | **LOC:** 578 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.5175%), Tech Debt (19.2643%)
**Top Internal Functions/Classes:**
  * `tcp_output` **(Compute Cores)** (Impact: 172.8)
    * *Intent:* #endif #define MAX_TCPOPTLEN 32 /* max # bytes that go in options */ /* * Tcp output routine: figure...
  * `tcp_setpersist` **(Compute Cores)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 23`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 97`, `fragile_debt: 2`
* *Architecture:* `api: 3`, `import: 21`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` route.h, in.h, in_pcb.h, in_systm.h, ip.h, ip_var.h, tcp.h, tcp_debug.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/in_pcb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 478.02 | **LOC:** 472 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.2603%), Tech Debt (87.2601%)
**Top Internal Functions/Classes:**
  * `in_pcbconnect` **(Compute Cores)** (Impact: 61.3)
    * *Intent:* /* * Connect from a socket to a specified address. * Both address and port must be specified in argu...
  * `in_pcblookup` **(Many-Argument Workhorses)** (Impact: 55.2)
  * `in_pcbnotify` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* /* * Pass some notification to all connections of a protocol * associated with address dst. The loca...
  * `in_pcbbind` **(Compute Cores)** (Impact: 47.0)
  * `in_losing` **(C Struct Operations)** (Impact: 7.0)
    * *Intent:* /* * Check for alternatives when higher level complains * about service problems. For now, invalidat...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 216
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 94`, `args: 2`, `func_start: 11`, `class_start: 26`
* *Risk/State:* `state_mutation: 80`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `import: 19`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` if.h, route.h, in.h, in_pcb.h, in_systm.h, in_var.h, ip.h, ip_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/sys/vnode_if.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 410.8 | **LOC:** 832 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `VOP_IOCTL` **(C Struct Operations)** (Impact: 3.6)
  * `VOP_RENAME` **(C Struct Operations)** (Impact: 3.6)
  * `VOP_SELECT` **(C Struct Operations)** (Impact: 3.3)
  * `VOP_SYMLINK` **(C Struct Operations)** (Impact: 3.3)
  * `VOP_ADVLOCK` **(C Struct Operations)** (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 402`, `func_start: 39`, `class_start: 323`
* *Risk/State:* `state_mutation: 170`
* *Architecture:* `api: 118`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.49
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.007576
  * `Imports (Out-Degree: 1):` buf.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sys/netinet/raw_ip.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 405.68 | **LOC:** 386 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.0897%), Tech Debt (62.4814%)
**Top Internal Functions/Classes:**
  * `rip_usrreq` **(Many-Argument Workhorses)** (Impact: 110.7)
    * *Intent:* /*ARGSUSED*/
  * `rip_ctloutput` **(Many-Argument Workhorses)** (Impact: 92.1)
    * *Intent:* /* * Raw IP socket option processing. */
  * `rip_input` **(C Struct Operations)** (Impact: 24.8)
    * *Intent:* /* * Setup generic address and protocol structures * for raw_input routine, then pass them along wit...
  * `rip_output` **(C Struct Operations)** (Impact: 9.8)
    * *Intent:* /* * Generate IP header and pass packet to ip_output. * Tack on options user may have setup with con...
  * `rip_init` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* /* * Nominal space allocated to a raw ip socket. */ #define RIPSNDQ 8192 #define RIPRCVQ 8192 /* * R...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 75`, `args: 1`, `func_start: 5`, `class_start: 12`
* *Risk/State:* `state_mutation: 53`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` if.h, route.h, in.h, in_pcb.h, in_systm.h, ip.h, ip_mroute.h, ip_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/in.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 389.74 | **LOC:** 597 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.9326%), Tech Debt (34.2007%)
**Top Internal Functions/Classes:**
  * `in_netof` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* #include <sys/socketvar.h> #include <net/if.h> #include <net/route.h> #include <netinet/in_systm.h> ...
  * `in_addmulti` **(C Struct Operations)** (Impact: 15.3)
    * *Intent:* /* * Add an address to the list of IP multicast addresses for a given interface. */
  * `in_ifscrub` **(Type Conversions)** (Impact: 7.6)
    * *Intent:* /* * Delete any existing route for an interface. */
  * `in_delmulti` **(C Struct Operations)** (Impact: 6.0)
    * *Intent:* /* * Delete a multicast address record. */
  * `in_socktrim` **(C Struct Operations)** (Impact: 4.9)
    * *Intent:* /* * Trim a mask in a sockaddr */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 108 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 324
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 119`, `args: 2`, `func_start: 5`, `class_start: 17`
* *Risk/State:* `state_mutation: 108`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 6`, `import: 12`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` if.h, route.h, if_ether.h, in.h, in_systm.h, in_var.h, errno.h, ioctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/if_ether.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 381.38 | **LOC:** 530 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.5317%), Tech Debt (49.3655%)
**Top Internal Functions/Classes:**
  * `arpresolve` **(Many-Argument Workhorses)** (Impact: 47.3)
    * *Intent:* /* * Resolve an IP address into an ethernet address. If success, * desten is filled in. If there is ...
  * `arp_rtrequest` **(Many-Argument Workhorses)** (Impact: 43.2)
    * *Intent:* /* * Parallel to llc_rtrequest. */
  * `in_arpinput` **(C Struct Operations)** (Impact: 37.5)
    * *Intent:* /* * ARP for Internet protocols on 10 Mb/s Ethernet. * Algorithm is that given in RFC 826. * In addi...
  * `arplookup` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* /* * Lookup or enter a new address in arptab. */
  * `arpintr` **(I/O & Config Routines)** (Impact: 12.4)
    * *Intent:* /* * Common length and type checks are done here, * then the protocol-specific routine is called. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 104`, `args: 19`, `func_start: 10`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 74`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` if.h, if_dl.h, route.h, if_ether.h, in.h, in_systm.h, in_var.h, ip.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_subr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 376.96 | **LOC:** 420 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.6939%), Tech Debt (51.4927%)
**Top Internal Functions/Classes:**
  * `tcp_close` **(Compute Cores)** (Impact: 36.0)
    * *Intent:* /* * Close a TCP control block: * discard all space held by the tcp * discard internet protocol bloc...
  * `tcp_respond` **(Many-Argument Workhorses)** (Impact: 24.3)
    * *Intent:* /* * Send a single message to the TCP at address specified by * the given TCP/IP header. If m == 0, ...
  * `tcp_notify` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* /* * Notify a tcp user of an asynchronous error; * store error as soft error, but wake up user * (fo...
  * `tcp_ctlinput` **(C Struct Operations)** (Impact: 17.1)
  * `tcp_drop` **(C Struct Operations)** (Impact: 9.6)
    * *Intent:* /* * Drop a TCP connection, reporting * the specified error. If connection is synchronized, * then s...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 68 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 232
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 79`, `args: 4`, `func_start: 10`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 96`, `unreferenced_by_name: 7`
* *Architecture:* `api: 13`, `import: 23`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` if.h, route.h, in.h, in_pcb.h, in_systm.h, ip.h, ip_icmp.h, ip_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_timer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 227.76 | **LOC:** 311 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.5407%), Tech Debt (97.023%)
**Top Internal Functions/Classes:**
  * `tcp_timers` **(Many-Argument Workhorses)** (Impact: 46.5)
    * *Intent:* int tcp_totbackoff = 511; /* sum of tcp_backoff[] */ /* * TCP timer processing. */
  * `tcp_slowtimo` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* /* * Tcp protocol timeout routine called every 500 ms. * Updates the timers in all active tcb's and ...
  * `tcp_fasttimo` **(I/O & Config Routines)** (Impact: 6.0)
    * *Intent:* #endif /* TUBA_INCLUDE */ /* * Fast timeout routine for processing delayed acks */
  * `tcp_canceltimers` **(C Struct Operations)** (Impact: 3.3)
    * *Intent:* #ifndef TUBA_INCLUDE /* * Cancel all timers for TCP tp. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 30`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 50`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 5`, `import: 22`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` cpu.h, if.h, route.h, in.h, in_pcb.h, in_systm.h, ip.h, ip_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/in_cksum.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 209.1 | **LOC:** 124 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.2684%), Tech Debt (32.4034%)
**Top Internal Functions/Classes:**
  * `in_cksum` **(Many-Argument Workhorses)** (Impact: 41.4)
    * *Intent:* #include <sys/param.h> #include <sys/mbuf.h> /* * Checksum routine for Internet Protocol family head...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 6`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 55`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mbuf.h, param.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/igmp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 199.42 | **LOC:** 292 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.6833%), Tech Debt (95.2456%)
**Top Internal Functions/Classes:**
  * `igmp_input` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `igmp_fasttimo` **(I/O & Config Routines)** (Impact: 8.4)
  * `igmp_joingroup` **(C Struct Operations)** (Impact: 6.5)
  * `igmp_sendreport` **(C Struct Operations)** (Impact: 5.7)
  * `igmp_leavegroup` **(C Struct Operations)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 50`, `args: 1`, `func_start: 6`, `class_start: 5`
* *Risk/State:* `state_mutation: 56`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 7`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` if.h, route.h, igmp.h, igmp_var.h, in.h, in_systm.h, in_var.h, ip.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_debug.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 142.94 | **LOC:** 134 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.8935%), Tech Debt (23.8538%)
**Top Internal Functions/Classes:**
  * `tcp_trace` **(Many-Argument Workhorses)** (Impact: 82.7)
    * *Intent:* #endif /* * Tcp debug routines */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 10`, `args: 6`, `func_start: 1`, `class_start: 3`
* *Risk/State:* `state_mutation: 19`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 21`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` if.h, route.h, in.h, in_pcb.h, in_systm.h, ip.h, ip_var.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/sys/systm.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 81.58 | **LOC:** 145 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.5564%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 65`, `import: 1`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` libkern.h
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `sys/sys/mbuf.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 77.96 | **LOC:** 379 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.1854%), Tech Debt (38.1338%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 54`, `args: 5`, `class_start: 27`
* *Risk/State:* `state_mutation: 12`, `fragile_debt: 3`
* *Architecture:* `api: 24`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.339
  * `Choke Point (Betweenness):` 0.000231 | `Ripple Effect (Closeness):` 0.128788
  * `Imports (Out-Degree: 1):` malloc.h
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `sys/sys/socketvar.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 68.14 | **LOC:** 236 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.673%), Tech Debt (22.6862%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 114`, `args: 1`, `class_start: 19`
* *Risk/State:* `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 50`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.177
  * `Choke Point (Betweenness):` 0.000636 | `Ripple Effect (Closeness):` 0.090909
  * `Imports (Out-Degree: 1):` select.h
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `sys/sys/vnode.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 63.3 | **LOC:** 412 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.5952%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `holdrele` **(C Struct Operations)** (Impact: 1.8)
    * *Intent:* #else #define VATTR_NULL(vap) (*(vap) = va_null) /* initialize a vattr */ #define HOLDRELE(vp) holdr...
  * `vhold` **(C Struct Operations)** (Impact: 1.8)
    * *Intent:* #define VHOLD(vp) vhold(vp) /* increase buf or page ref */
  * `vref` **(C Struct Operations)** (Impact: 1.8)
    * *Intent:* #define VREF(vp) vref(vp) /* increase reference */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 125`, `args: 7`, `func_start: 3`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `dead_code: 2`
* *Architecture:* `api: 50`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` lock.h, queue.h, vnode_if.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/sys/tty.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 59.74 | **LOC:** 192 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.611%), Tech Debt (26.1122%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 74`, `args: 1`, `class_start: 12`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `api: 42`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` select.h, termios.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/sys/proc.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 55.2 | **LOC:** 257 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.6945%), Tech Debt (82.6712%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 63`, `class_start: 32`
* *Risk/State:* `state_mutation: 2`, `fragile_debt: 4`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.801
  * `Choke Point (Betweenness):` 0.00052 | `Ripple Effect (Closeness):` 0.023674
  * `Imports (Out-Degree: 2):` proc.h, queue.h, select.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `sys/sys/mbuf.h` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 95.6223%)
- `sys/sys/proc.h` -> **Severity: 0.015** (Bridge: 0.0005 * Flux: 28.905%)
- `sys/sys/vnode_if.h` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 99.8097%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `sys/sys/mbuf.h` -> **Severity: 9.024** (Embedded: 0.1288 * Error Risk: 70.0724%)
- `sys/sys/malloc.h` -> **Severity: 7.007** (Embedded: 0.1189 * Error Risk: 58.9259%)
- `sys/sys/ucred.h` -> **Severity: 5.778** (Embedded: 0.0954 * Error Risk: 60.5532%)
- `sys/sys/systm.h` -> **Severity: 5.037** (Embedded: 0.0833 * Error Risk: 60.4498%)
- `sys/netinet/in_var.h` -> **Severity: 3.707** (Embedded: 0.0606 * Error Risk: 61.1719%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `sys/sys/vnode_if.h` -> **Severity: 649.0** (Blast Radius: 6.49 * Doc Risk: 100.0%)
- `Makefile` -> **Severity: 505.7** (Blast Radius: 5.057 * Doc Risk: 100.0%)
- `sys/netinet/if_ether.c` -> **Severity: 505.7** (Blast Radius: 5.057 * Doc Risk: 100.0%)
- `sys/netinet/igmp.c` -> **Severity: 505.7** (Blast Radius: 5.057 * Doc Risk: 100.0%)
- `sys/netinet/in.c` -> **Severity: 505.7** (Blast Radius: 5.057 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
