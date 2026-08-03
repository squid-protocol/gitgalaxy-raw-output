# ARCHITECTURAL_BRIEF: tcpip_historical
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/tcpip_historical` |
| **Timestamp** | `2026-08-03T21:38:25.834390+00:00` |
| **Scan Duration** | `1.76s` |
| **Git Branch** | `master` |
| **Git Commit** | `b44636d7febc9dcf553118bd320571864188351d` |
| **Git Remote** | `https://github.com/weiss/original-bsd.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 130 malicious artifacts.

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
| Total Artifacts | 6082 |
| Analyzed Artifacts (Scanned) | 132 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5950 |
| Total LOC | 11237 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 2.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.625 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 129 | 11225 | 97.7% |
| MAKEFILE | 1 | 11 | 0.8% |
| MARKDOWN | 1 | 0 | 0.8% |
| PLAINTEXT | 1 | 1 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.399`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 97 | 73.5% |
| file_cluster_13 | 20 | 15.2% |
| file_cluster_9 | 13 | 9.8% |
| Unknown | 1 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5950*

**Composition by Extension & Reason:**
- `.c`: 1627x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1023x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 530x Excluded: Neighborhood Micro-Mass Limit Exceeded, 121x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 586x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 42x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.3`: 251x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 39x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `no_extension`: 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 137x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (Unsupported Extension: '.distribution')
- `.f`: 79x Excluded: Neighborhood Micro-Mass Limit Exceeded, 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.2`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.p`: 47x Excluded (Unsupported Extension: '.p'), 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.4`: 56x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.out`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ms`: 45x Excluded (Unsupported Extension: '.ms'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.n`: 46x Excluded (Unsupported Extension: '.n')
- `.me`: 43x Excluded (Unsupported Extension: '.me')
- `.inc`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.afm`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 96.8 | 22.0 | 5.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Testing Exposure | 0.3 | 80.0 | 9.3 | 2.3 | 2.3 |
| API Exposure | 0.0 | 17.0 | 10.6 | 12.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 5.0 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 91.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 1.6 | 100.0 | 75.5 | 98.8 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 0.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.4 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `sys/sys/socketvar.h` (Hits: 38)
- `sys/netinet/tcp_output.c` (Hits: 12)
- `sys/netinet/raw_ip.c` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **dirent.h** (`sys/sys/dirent.h`) — 1 inbound connections
2. **errno.h** (`sys/sys/errno.h`) — 1 inbound connections
3. **user.h** (`sys/sys/user.h`) — 1 inbound connections
4. **vnode_if.h** (`sys/sys/vnode_if.h`) — 1 inbound connections
5. **Makefile** (`Makefile`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **in_proto.c** (`sys/netinet/in_proto.c`) — 26 outbound dependencies
2. **tcp_input.c** (`sys/netinet/tcp_input.c`) — 23 outbound dependencies
3. **tcp_subr.c** (`sys/netinet/tcp_subr.c`) — 23 outbound dependencies
4. **tcp_usrreq.c** (`sys/netinet/tcp_usrreq.c`) — 23 outbound dependencies
5. **tcp_timer.c** (`sys/netinet/tcp_timer.c`) — 22 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `tcp_output` (@ `sys/netinet/tcp_output.c`) -> Impact: **426.8** | LOC: 296
  * *Intent:* #include <netinet/in_systm.h> #include <netinet/ip.h> #include <netinet/in_pcb.h> #include <netinet/ip_var.h> #include <netinet/tcp.h> #define TCPOUTF...
- `ip_output` (@ `sys/netinet/ip_output.c`) -> Impact: **229.1** | LOC: 181
  * *Intent:* #include <sys/socketvar.h> #include <net/if.h> #include <net/route.h> #include <netinet/in.h> #include <netinet/in_systm.h> #include <netinet/ip.h> #i...
- `icmp_reflect` (@ `sys/netinet/ip_icmp.c`) -> Impact: **176.6** | LOC: 103
- `rip_usrreq` (@ `sys/netinet/raw_ip.c`) -> Impact: **131.3** | LOC: 147
  * *Intent:* #endif
- `tcp_trace` (@ `sys/netinet/tcp_debug.c`) -> Impact: **74.3** | LOC: 86
  * *Intent:* #include <net/route.h> #include <net/if.h> #include <netinet/in.h> #include <netinet/in_systm.h> #include <netinet/ip.h> #include <netinet/in_pcb.h> #...
- `rip_ctloutput` (@ `sys/netinet/raw_ip.c`) -> Impact: **66.3** | LOC: 78
- `arpintr` (@ `sys/netinet/if_ether.c`) -> Impact: **63.8** | LOC: 29
- `in_pcbconnect` (@ `sys/netinet/in_pcb.c`) -> Impact: **62.1** | LOC: 99
- `tcp_usrreq` (@ `sys/netinet/tcp_usrreq.c`) -> Impact: **57.5** | LOC: 131
  * *Intent:* #include <net/if.h> #include <net/route.h> #include <netinet/in.h> #include <netinet/in_systm.h> #include <netinet/ip.h> #include <netinet/in_pcb.h> #...
- `igmp_input` (@ `sys/netinet/igmp.c`) -> Impact: **42.8** | LOC: 105

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `arpintr` (@ `sys/netinet/if_ether.c`) -> **O(2^N) [Recursive]**
- `icmp_reflect` (@ `sys/netinet/ip_icmp.c`) -> **O(2^N) [Recursive]**
- `arpresolve` (@ `sys/netinet/if_ether.c`) -> **O(2^N) [Recursive]**
- `arplookup` (@ `sys/netinet/if_ether.c`) -> **O(2^N) [Recursive]**
- `arptfree` (@ `sys/netinet/if_ether.c`) -> **O(2^N) [Recursive]**
- `icmp_error` (@ `sys/netinet/ip_icmp.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #include <net/if.h> #include <net/route.h> #include <netinet/in.h> #include <netinet/in_systm.h> #include <netinet/in_var.h> #include <netinet/ip.h> #...
- `icmp_send` (@ `sys/netinet/ip_icmp.c`) -> **O(2^N) [Recursive]**
- `ip_output` (@ `sys/netinet/ip_output.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #include <sys/socketvar.h> #include <net/if.h> #include <net/route.h> #include <netinet/in.h> #include <netinet/in_systm.h> #include <netinet/ip.h> #i...
- `rip_usrreq` (@ `sys/netinet/raw_ip.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif
- `tcp_output` (@ `sys/netinet/tcp_output.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #include <netinet/in_systm.h> #include <netinet/ip.h> #include <netinet/in_pcb.h> #include <netinet/ip_var.h> #include <netinet/tcp.h> #define TCPOUTF...

### Highest Data Gravity (Database Complexity)
- `tcp_output` (@ `sys/netinet/tcp_output.c`) -> DB Complexity: **124**
  * *Intent:* #include <netinet/in_systm.h> #include <netinet/ip.h> #include <netinet/in_pcb.h> #include <netinet/ip_var.h> #include <netinet/tcp.h> #define TCPOUTF...
- `ip_output` (@ `sys/netinet/ip_output.c`) -> DB Complexity: **59**
  * *Intent:* #include <sys/socketvar.h> #include <net/if.h> #include <net/route.h> #include <netinet/in.h> #include <netinet/in_systm.h> #include <netinet/ip.h> #i...
- `in_cksum` (@ `sys/netinet/in_cksum.c`) -> DB Complexity: **54**
  * *Intent:* /* * Copyright (c) 1988, 1992, 1993 * The Regents of the University of California. All rights reserved. * * %sccs.include.redist.c% * * @(#)in_cksum.c...
- `tcp_respond` (@ `sys/netinet/tcp_subr.c`) -> DB Complexity: **38**
- `icmp_reflect` (@ `sys/netinet/ip_icmp.c`) -> DB Complexity: **36**
- `tcp_usrreq` (@ `sys/netinet/tcp_usrreq.c`) -> DB Complexity: **35**
  * *Intent:* #include <net/if.h> #include <net/route.h> #include <netinet/in.h> #include <netinet/in_systm.h> #include <netinet/ip.h> #include <netinet/in_pcb.h> #...
- `rip_usrreq` (@ `sys/netinet/raw_ip.c`) -> DB Complexity: **31**
  * *Intent:* #endif
- `tcp_input` (@ `sys/netinet/tcp_input.c`) -> DB Complexity: **31**
- `igmp_sendreport` (@ `sys/netinet/igmp.c`) -> DB Complexity: **28**
- `tcp_reass` (@ `sys/netinet/tcp_input.c`) -> DB Complexity: **26**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `sys/netinet` | 41 | 12918.34 | 44.7% | 20.24% |
| `games/phantasia` | 1 | 5000.0 | 0.0% | 0.0% |
| `sys/sys` | 88 | 4158.54 | 11.6% | 10.4% |
| `__monolith__` | 2 | 118.0 | 2.5% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `sys/sys/kernel.h` -> **99.9999%** Exposure
- `sys/sys/ttydefaults.h` -> **99.8783%** Exposure
- `sys/sys/signalvar.h` -> **99.2508%** Exposure
- `sys/netinet/tcp_timer.c` -> **97.3241%** Exposure
- `sys/sys/uio.h` -> **97.2364%** Exposure
### Highest State Flux (Mutation/Volatility)
- `sys/netinet/if_ether.c` -> **100.0%** Exposure
- `sys/netinet/igmp.c` -> **100.0%** Exposure
- `sys/netinet/in.c` -> **100.0%** Exposure
- `sys/netinet/in_cksum.c` -> **100.0%** Exposure
- `sys/netinet/in_local.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sys/netinet/in_pcb.c` -> **7** Orphaned Functions | **0** Duplicates
- `sys/netinet/tcp_subr.c` -> **6** Orphaned Functions | **0** Duplicates
- `sys/netinet/igmp.c` -> **5** Orphaned Functions | **0** Duplicates
- `sys/netinet/in.c` -> **3** Orphaned Functions | **0** Duplicates
- `sys/netinet/raw_ip.c` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`sys/netinet/ip_input.c`** -> AI Confidence: **99.48%**
2. **`sys/netinet/tcp_debug.c`** -> AI Confidence: **99.48%**
3. **`sys/netinet/tcp_output.c`** -> AI Confidence: **99.48%**
4. **`sys/netinet/tcp_input.c`** -> AI Confidence: **99.39%**
5. **`sys/netinet/tcp_usrreq.c`** -> AI Confidence: **99.39%**
6. **`sys/netinet/raw_ip.c`** -> AI Confidence: **99.35%**
7. **`sys/netinet/if_ether.c`** -> AI Confidence: **99.31%**
8. **`sys/netinet/in.c`** -> AI Confidence: **99.31%**
9. **`sys/netinet/in_pcb.c`** -> AI Confidence: **99.31%**
10. **`sys/netinet/ip_icmp.c`** -> AI Confidence: **99.31%**
11. **`sys/netinet/ip_mroute.c`** -> AI Confidence: **99.31%**
12. **`sys/netinet/ip_output.c`** -> AI Confidence: **99.31%**
13. **`sys/netinet/tcp_timer.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `sys/netinet/in.c` -> **20.0%** Exposure
### Raw Memory Manipulation
- `sys/sys/vnode.h` -> **9.9983%** Exposure
- `sys/sys/mount.h` -> **9.961%** Exposure
- `sys/sys/conf.h` -> **9.9603%** Exposure
- `sys/sys/tty.h` -> **9.9265%** Exposure
- `sys/sys/systm.h` -> **9.1219%** Exposure
### Algorithmic DoS Exposure
- `sys/netinet/igmp.c` -> **100.0%** Exposure
- `sys/netinet/in.c` -> **100.0%** Exposure
- `sys/netinet/ip_icmp.c` -> **100.0%** Exposure
- `sys/netinet/raw_ip.c` -> **100.0%** Exposure
- `sys/netinet/if_ether.c` -> **61.9742%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `429` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `sys/netinet/igmp.c` (C) -> Cumulative Risk: **719.61**
- **Archetype:** `file_cluster_13` (Distance: 12.646 IQR)
- **Magnitude:** 226.42 | **LOC:** 292 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (97.7273%)
- **Heaviest Functions:** `igmp_input` (Impact: 42.8), `igmp_fasttimo` (Impact: 8.3), `igmp_sendreport` (Impact: 6.1)

### 2. `sys/netinet/raw_ip.c` (C) -> Cumulative Risk: **696.08**
- **Archetype:** `file_cluster_13` (Distance: 13.199 IQR)
- **Magnitude:** 507.18 | **LOC:** 386 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9038%)
- **Heaviest Functions:** `rip_usrreq` (Impact: 131.3), `rip_ctloutput` (Impact: 66.3), `rip_input` (Impact: 30.7)

### 3. `sys/netinet/ip_icmp.c` (C) -> Cumulative Risk: **656.53**
- **Archetype:** `file_cluster_13` (Distance: 13.083 IQR)
- **Magnitude:** 433.38 | **LOC:** 566 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.4851%)
- **Heaviest Functions:** `icmp_reflect` (Impact: 176.6), `icmp_error` (Impact: 42.7), `icmp_send` (Impact: 8.1)

### 4. `sys/netinet/in_pcb.c` (C) -> Cumulative Risk: **632.87**
- **Archetype:** `file_cluster_13` (Distance: 13.655 IQR)
- **Magnitude:** 478.32 | **LOC:** 472 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.6245%), Tech Debt (87.2601%)
- **Heaviest Functions:** `in_pcbconnect` (Impact: 62.1), `in_pcbbind` (Impact: 28.2), `in_pcblookup` (Impact: 27.2)

### 5. `sys/netinet/tcp_subr.c` (C) -> Cumulative Risk: **607.59**
- **Archetype:** `file_cluster_13` (Distance: 13.802 IQR)
- **Magnitude:** 347.74 | **LOC:** 420 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (98.8081%), Safety Score (92.4821%)
- **Heaviest Functions:** `tcp_respond` (Impact: 19.1), `tcp_init` (Impact: 10.9), `tcp_ctlinput` (Impact: 9.2)

### 6. `sys/netinet/if_ether.c` (C) -> Cumulative Risk: **596.15**
- **Archetype:** `file_cluster_13` (Distance: 12.801 IQR)
- **Magnitude:** 335.96 | **LOC:** 530 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (91.0275%), Verification (80.0%)
- **Heaviest Functions:** `arpintr` (Impact: 63.8), `arpresolve` (Impact: 38.9), `arplookup` (Impact: 15.2)

### 7. `sys/netinet/tcp_output.c` (C) -> Cumulative Risk: **593.05**
- **Archetype:** `file_cluster_13` (Distance: 14.063 IQR)
- **Magnitude:** 750.3 | **LOC:** 578 | **CtrlFlow:** 83.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (92.6923%), Safety Score (92.6073%)
- **Heaviest Functions:** `tcp_output` (Impact: 426.8), `tcp_setpersist` (Impact: 3.8)

### 8. `sys/netinet/in.c` (C) -> Cumulative Risk: **590.78**
- **Archetype:** `file_cluster_13` (Distance: 13.029 IQR)
- **Magnitude:** 215.78 | **LOC:** 597 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (77.1446%)
- **Heaviest Functions:** `in_netof` (Impact: 12.2), `in_delmulti` (Impact: 9.3), `in_socktrim` (Impact: 6.7)

### 9. `sys/netinet/tcp_timer.c` (C) -> Cumulative Risk: **574.54**
- **Archetype:** `file_cluster_13` (Distance: 13.506 IQR)
- **Magnitude:** 204.6 | **LOC:** 311 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (97.3241%), Documentation (89.9743%)
- **Heaviest Functions:** `tcp_timers` (Impact: 25.9), `tcp_fasttimo` (Impact: 6.0), `tcp_canceltimers` (Impact: 2.5)

### 10. `sys/netinet/tcp_usrreq.c` (C) -> Cumulative Risk: **561.82**
- **Archetype:** `file_cluster_13` (Distance: 12.972 IQR)
- **Magnitude:** 229.3 | **LOC:** 504 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (83.5189%), Verification (80.0%)
- **Heaviest Functions:** `tcp_usrreq` (Impact: 57.5), `tcp_usrclosed` (Impact: 14.3), `tcp_disconnect` (Impact: 8.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `games/phantasia/monsters.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/ip_mroute.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.335 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.196 IQR)
- **Top Global Matches:** file_cluster_13: 13.335, file_cluster_8: 13.597, file_cluster_11: 13.694
- **Magnitude:** 3631.64 | **LOC:** 809 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (75.0398%), Tech Debt (11.8303%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 109`, `args: 8`, `func_start: 11`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 309`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 81`, `import: 21`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ioctl.h, param.h, protosw.h, ip.h, malloc.h, in_systm.h, socket.h, in_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/ip_input.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.358 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.821 IQR)
- **Top Global Matches:** file_cluster_13: 13.358, file_cluster_11: 13.654, file_cluster_8: 13.738
- **Magnitude:** 2886.42 | **LOC:** 1141 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (96.7732%), Tech Debt (16.5351%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 27`, `args: 6`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 165`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 37`, `import: 19`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, protosw.h, ip.h, malloc.h, kernel.h, in_systm.h, socket.h, in_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_output.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.063 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.28 IQR)
- **Top Global Matches:** file_cluster_13: 14.063, file_cluster_8: 14.359, file_cluster_11: 14.397
- **Magnitude:** 750.3 | **LOC:** 578 | **CtrlFlow:** 83.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 124
- **Risk Profile:** Cognitive Load (92.6923%), Tech Debt (46.7153%)
**Top Internal Functions/Classes:**
  * `tcp_output` (Impact: 426.8 | O(2^N) | DB: 124)
    * *Intent:* #include <netinet/in_systm.h> #include <netinet/ip.h> #include <netinet/in_pcb.h> #include <netinet/...
  * `tcp_setpersist` (Impact: 3.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 20`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 277`, `fragile_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 12`, `api: 37`, `import: 21`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, protosw.h, ip.h, malloc.h, in_systm.h, socket.h, route.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/sys/vnode_if.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.537 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.037 IQR)
- **Top Global Matches:** file_cluster_8: 10.537, file_cluster_7: 11.138, file_cluster_13: 11.326
- **Magnitude:** 709.9 | **LOC:** 832 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `VOP_IOCTL` (Impact: 2.0 | O(N^1) | DB: 7)
  * `VOP_RENAME` (Impact: 2.0 | O(N^1) | DB: 7)
  * `VOP_SELECT` (Impact: 1.9 | O(N^1) | DB: 6)
  * `VOP_SYMLINK` (Impact: 1.9 | O(N^1) | DB: 6)
  * `VOP_ADVLOCK` (Impact: 1.9 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 402`, `func_start: 39`, `class_start: 323`
* *Risk/State:* `state_mutation: 170`
* *Architecture:* `api: 458`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.591
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 0):` buf.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sys/netinet/tcp_input.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.378 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.912 IQR)
- **Top Global Matches:** file_cluster_13: 14.378, file_cluster_8: 14.554, file_cluster_11: 14.562
- **Magnitude:** 689.5 | **LOC:** 1635 | **CtrlFlow:** 73.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (92.0697%), Tech Debt (39.7315%)
**Top Internal Functions/Classes:**
  * `tcp_reass` (Impact: 28.3 | O(N^1) | DB: 26)
  * `tcp_input` (Impact: 27.4 | O(N^1) | DB: 31)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 69`, `args: 13`, `func_start: 2`, `class_start: 7`
* *Risk/State:* `state_mutation: 548`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 75`, `import: 23`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, protosw.h, ip.h, malloc.h, in_systm.h, socket.h, route.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/ip_output.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.82 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.822 IQR)
- **Top Global Matches:** file_cluster_13: 13.82, file_cluster_8: 14.071, file_cluster_11: 14.19
- **Magnitude:** 538.26 | **LOC:** 1039 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (88.1659%), Tech Debt (34.3407%)
**Top Internal Functions/Classes:**
  * `ip_output` (Impact: 229.1 | O(2^N) | DB: 59)
    * *Intent:* #include <sys/socketvar.h> #include <net/if.h> #include <net/route.h> #include <netinet/in.h> #inclu...
  * `ip_insertoptions` (Impact: 14.1 | O(N^1) | DB: 17)
    * *Intent:* #endif /* * Multicasts with a time-to-live of zero may be looped- * back, above, but must not be tra...
  * `ip_optcopy` (Impact: 11.2 | O(N^1) | DB: 11)
    * *Intent:* /*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 54`, `args: 8`, `func_start: 3`, `class_start: 11`
* *Risk/State:* `state_mutation: 240`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 39`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` if.h, in_pcb.h, param.h, protosw.h, ip.h, in.h, in_var.h, route.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/raw_ip.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.199 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.798 IQR)
- **Top Global Matches:** file_cluster_13: 13.199, file_cluster_8: 13.388, file_cluster_11: 13.632
- **Magnitude:** 507.18 | **LOC:** 386 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (83.2765%), Tech Debt (50.209%)
**Top Internal Functions/Classes:**
  * `rip_usrreq` (Impact: 131.3 | O(2^N) | DB: 31)
    * *Intent:* #endif
  * `rip_ctloutput` (Impact: 66.3 | O(N^1) | DB: 16)
  * `rip_input` (Impact: 30.7 | O(N^2) | DB: 12)
    * *Intent:* /* * Nominal space allocated to a raw ip socket. */ #define RIPSNDQ 8192 #define RIPRCVQ 8192 /* * R...
  * `rip_output` (Impact: 8.6 | O(N^1) | DB: 20)
  * `rip_init` (Impact: 1.3 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 52`, `args: 3`, `func_start: 5`, `class_start: 12`
* *Risk/State:* `state_mutation: 197`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 6`, `api: 66`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` if.h, in_pcb.h, param.h, protosw.h, systm.h, errno.h, in.h, ip.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/in_pcb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.655 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.483 IQR)
- **Top Global Matches:** file_cluster_13: 13.655, file_cluster_8: 13.829, file_cluster_11: 13.968
- **Magnitude:** 478.32 | **LOC:** 472 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (79.9316%), Tech Debt (87.2601%)
**Top Internal Functions/Classes:**
  * `in_pcbconnect` (Impact: 62.1 | O(N^1) | DB: 24)
  * `in_pcbbind` (Impact: 28.2 | O(N^1) | DB: 21)
  * `in_pcblookup` (Impact: 27.2 | O(N^1) | DB: 13)
  * `in_pcbnotify` (Impact: 20.2 | O(N^1) | DB: 12)
  * `in_losing` (Impact: 5.2 | O(N^1) | DB: 5)
    * *Intent:* /* * Pass some notification to all connections of a protocol * associated with address dst. The loca...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 87`, `args: 1`, `func_start: 11`, `class_start: 26`
* *Risk/State:* `state_mutation: 244`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `io: 4`, `api: 69`, `import: 19`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ioctl.h, param.h, protosw.h, ip.h, malloc.h, in_systm.h, socket.h, in_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/ip_icmp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.083 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.033 IQR)
- **Top Global Matches:** file_cluster_13: 13.083, file_cluster_8: 13.368, file_cluster_11: 13.542
- **Magnitude:** 433.38 | **LOC:** 566 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (79.4391%), Tech Debt (20.4493%)
**Top Internal Functions/Classes:**
  * `icmp_reflect` (Impact: 176.6 | O(2^N) | DB: 36)
  * `icmp_error` (Impact: 42.7 | O(2^N) | DB: 7)
    * *Intent:* #include <net/if.h> #include <net/route.h> #include <netinet/in.h> #include <netinet/in_systm.h> #in...
  * `icmp_send` (Impact: 8.1 | O(2^N) | DB: 9)
  * `icmp_sysctl` (Impact: 6.1 | O(N^1))
  * `iptime` (Impact: 1.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 49`, `args: 6`, `func_start: 5`, `class_start: 7`
* *Risk/State:* `state_mutation: 145`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 49`, `import: 16`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` if.h, param.h, protosw.h, systm.h, in.h, in_var.h, ip.h, icmp_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_subr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.802 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.126 IQR)
- **Top Global Matches:** file_cluster_13: 13.802, file_cluster_8: 14.144, file_cluster_11: 14.33
- **Magnitude:** 347.74 | **LOC:** 420 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (67.3869%), Tech Debt (56.0358%)
**Top Internal Functions/Classes:**
  * `tcp_respond` (Impact: 19.1 | O(N^1) | DB: 38)
  * `tcp_init` (Impact: 10.9 | O(2^N) | DB: 4)
    * *Intent:* #include <netinet/in.h> #include <netinet/in_systm.h> #include <netinet/ip.h> #include <netinet/in_p...
  * `tcp_ctlinput` (Impact: 9.2 | O(N^1) | DB: 3)
    * *Intent:* /* * Close a TCP control block: * discard all space held by the tcp
  * `tcp_template` (Impact: 7.7 | O(N^1) | DB: 22)
  * `tcp_newtcpcb` (Impact: 6.6 | O(N^1) | DB: 13)
    * *Intent:* #undef xchg
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 68`, `args: 11`, `func_start: 9`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 229`, `orphaned_logic: 6`
* *Architecture:* `io: 3`, `api: 48`, `import: 23`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, protosw.h, ip.h, malloc.h, in_systm.h, socket.h, route.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/if_ether.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.801 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.915 IQR)
- **Top Global Matches:** file_cluster_13: 12.801, file_cluster_8: 12.949, file_cluster_11: 13.194
- **Magnitude:** 335.96 | **LOC:** 530 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (79.5254%), Tech Debt (19.1556%)
**Top Internal Functions/Classes:**
  * `arpintr` (Impact: 63.8 | O(2^N) | DB: 2)
  * `arpresolve` (Impact: 38.9 | O(2^N) | DB: 11)
  * `arplookup` (Impact: 15.2 | O(2^N) | DB: 5)
  * `arptfree` (Impact: 10.9 | O(2^N) | DB: 5)
  * `arprequest` (Impact: 3.7 | O(N^1) | DB: 13)
    * *Intent:* /*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 55`, `args: 2`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `state_mutation: 155`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 40`, `import: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ioctl.h, if.h, param.h, systm.h, in_var.h, errno.h, in.h, ip.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_usrreq.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.972 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.584 IQR)
- **Top Global Matches:** file_cluster_13: 12.972, file_cluster_11: 13.509, file_cluster_8: 13.551
- **Magnitude:** 229.3 | **LOC:** 504 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (83.5189%), Tech Debt (51.785%)
**Top Internal Functions/Classes:**
  * `tcp_usrreq` (Impact: 57.5 | O(N^1) | DB: 35)
    * *Intent:* #include <net/if.h> #include <net/route.h> #include <netinet/in.h> #include <netinet/in_systm.h> #in...
  * `tcp_usrclosed` (Impact: 14.3 | O(N^1) | DB: 4)
  * `tcp_disconnect` (Impact: 8.0 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 20`, `func_start: 3`, `class_start: 5`
* *Risk/State:* `state_mutation: 116`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 30`, `import: 23`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, protosw.h, ip.h, malloc.h, in_systm.h, socket.h, route.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/igmp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.646 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.712 IQR)
- **Top Global Matches:** file_cluster_13: 12.646, file_cluster_8: 12.857, file_cluster_0: 13.201
- **Magnitude:** 226.42 | **LOC:** 292 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (68.4573%), Tech Debt (95.2456%)
**Top Internal Functions/Classes:**
  * `igmp_input` (Impact: 42.8 | O(N^2) | DB: 24)
  * `igmp_fasttimo` (Impact: 8.3 | O(N^1) | DB: 4)
  * `igmp_sendreport` (Impact: 6.1 | O(N^1) | DB: 28)
  * `igmp_joingroup` (Impact: 4.8 | O(N^1) | DB: 4)
  * `igmp_init` (Impact: 1.3 | O(N^1) | DB: 1)
    * *Intent:* #include <sys/param.h> #include <sys/mbuf.h> #include <sys/socket.h> #include <sys/protosw.h> #inclu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 46`, `args: 7`, `func_start: 6`, `class_start: 5`
* *Risk/State:* `state_mutation: 127`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `io: 2`, `api: 31`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` igmp_var.h, if.h, igmp.h, param.h, protosw.h, in_var.h, in.h, ip.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/in.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.029 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.834 IQR)
- **Top Global Matches:** file_cluster_13: 13.029, file_cluster_8: 13.231, file_cluster_11: 13.526
- **Magnitude:** 215.78 | **LOC:** 597 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (77.1446%), Tech Debt (33.2727%)
**Top Internal Functions/Classes:**
  * `in_netof` (Impact: 12.2 | O(N^1) | DB: 7)
    * *Intent:* * * @(#)in.c 8.4 (Berkeley) 01/09/95 */ #include <sys/param.h> #include <sys/ioctl.h> #include <sys/...
  * `in_delmulti` (Impact: 9.3 | O(N^3) | DB: 7)
  * `in_socktrim` (Impact: 6.7 | O(N^2) | DB: 5)
    * *Intent:* /*
  * `in_ifscrub` (Impact: 4.7 | O(N^1) | DB: 1)
    * *Intent:* /* * Find address for this interface, if it exists. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 40`, `func_start: 4`, `class_start: 5`
* *Risk/State:* `state_mutation: 145`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 34`, `import: 12`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ioctl.h, if.h, param.h, in_var.h, errno.h, in.h, route.h, malloc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/in_cksum.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.282 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.485 IQR)
- **Top Global Matches:** file_cluster_13: 14.282, file_cluster_8: 14.344, file_cluster_11: 14.523
- **Magnitude:** 211.1 | **LOC:** 124 | **CtrlFlow:** 85.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (80.4044%), Tech Debt (32.4034%)
**Top Internal Functions/Classes:**
  * `in_cksum` (Impact: 27.4 | O(N^1) | DB: 54)
    * *Intent:* /* * Copyright (c) 1988, 1992, 1993 * The Regents of the University of California. All rights reserv...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 4`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 171`, `orphaned_logic: 1`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, mbuf.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_timer.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.506 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.994 IQR)
- **Top Global Matches:** file_cluster_13: 13.506, file_cluster_11: 13.963, file_cluster_8: 14.104
- **Magnitude:** 204.6 | **LOC:** 311 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (80.6121%), Tech Debt (97.3241%)
**Top Internal Functions/Classes:**
  * `tcp_timers` (Impact: 25.9 | O(N^1) | DB: 20)
    * *Intent:* tcp_iss += TCP_ISSINCR/PR_SLOWHZ; /* increment iss */ #ifdef TCP_COMPAT_42
  * `tcp_fasttimo` (Impact: 6.0 | O(N^1) | DB: 7)
    * *Intent:* int tcp_keepcnt = TCPTV_KEEPCNT; /* max idle probes */ int tcp_maxpersistidle = TCPTV_KEEP_IDLE; /* ...
  * `tcp_canceltimers` (Impact: 2.5 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 19`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `state_mutation: 142`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 25`, `import: 22`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, protosw.h, ip.h, malloc.h, in_systm.h, socket.h, route.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/sys/queue.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.968 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.077 IQR)
- **Top Global Matches:** file_cluster_8: 13.968, file_cluster_12: 14.133, file_cluster_11: 14.389
- **Magnitude:** 204.08 | **LOC:** 234 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (82.7047%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 27`, `class_start: 17`
* *Risk/State:* `state_mutation: 172`
* *Architecture:* `api: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/sys/mbuf.h` (C | Tier 0 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.46 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.399 IQR)
- **Top Global Matches:** file_cluster_8: 12.46, file_cluster_12: 12.851, file_cluster_13: 12.921
- **Magnitude:** 190.96 | **LOC:** 379 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (74.5763%), Tech Debt (38.1338%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 54`, `args: 4`, `class_start: 27`
* *Risk/State:* `state_mutation: 115`, `fragile_debt: 3`
* *Architecture:* `api: 56`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` malloc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_debug.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.825 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.103 IQR)
- **Top Global Matches:** file_cluster_13: 12.825, file_cluster_8: 13.329, file_cluster_11: 13.551
- **Magnitude:** 158.54 | **LOC:** 134 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (75.5526%), Tech Debt (23.8538%)
**Top Internal Functions/Classes:**
  * `tcp_trace` (Impact: 74.3 | O(N^1) | DB: 21)
    * *Intent:* #include <net/route.h> #include <net/if.h> #include <netinet/in.h> #include <netinet/in_systm.h> #in...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 3`
* *Risk/State:* `state_mutation: 64`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 18`, `import: 21`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, protosw.h, ip.h, in_systm.h, socket.h, route.h, tcp.h, tcp_seq.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/sys/socketvar.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.12 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 7.025 IQR)
- **Top Global Matches:** file_cluster_8: 12.12, file_cluster_0: 12.202, file_cluster_13: 12.289
- **Magnitude:** 134.12 | **LOC:** 236 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (46.3039%), Tech Debt (22.8298%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 114`, `class_start: 19`
* *Risk/State:* `state_mutation: 27`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 38`, `api: 89`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` select.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/udp_usrreq.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.27 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.47 IQR)
- **Top Global Matches:** file_cluster_13: 12.27, file_cluster_8: 12.678, file_cluster_11: 12.875
- **Magnitude:** 124.58 | **LOC:** 615 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (80.9947%), Tech Debt (82.1544%)
**Top Internal Functions/Classes:**
  * `udp_input` (Impact: 3.9 | O(N^1) | DB: 2)
  * `udp_detach` (Impact: 2.5 | O(N^1) | DB: 2)
  * `udp_init` (Impact: 1.2 | O(N^1) | DB: 2)
    * *Intent:* #else
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 32`, `args: 2`, `func_start: 3`, `class_start: 6`
* *Risk/State:* `state_mutation: 80`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 34`, `import: 18`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` if.h, in_pcb.h, param.h, protosw.h, ip.h, errno.h, in.h, udp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.926 IQR)
- **Top Global Matches:** file_cluster_8: 5.926, file_cluster_7: 7.222, file_cluster_1: 7.491
- **Magnitude:** 116.72 | **LOC:** 17 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 1`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/sys/mount.h` (C | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.854 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.415 IQR)
- **Top Global Matches:** file_cluster_8: 11.854, file_cluster_13: 11.919, file_cluster_9: 12.049
- **Magnitude:** 110.48 | **LOC:** 291 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.2489%), Tech Debt (20.5776%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 90`, `class_start: 40`
* *Risk/State:* `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 92`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ucred.h, cdefs.h, lock.h, queue.h, radix.h, socket.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_var.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.917 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.196 IQR)
- **Top Global Matches:** file_cluster_8: 8.917, file_cluster_9: 9.625, file_cluster_7: 9.652
- **Magnitude:** 102.14 | **LOC:** 255 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 71`, `class_start: 15`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `io: 4`, `api: 85`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `sys/sys/user.h` (C) | Magnitude: 21.66 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 14, import: 10, structural_boundaries: 6, class_start: 6
- `sys/netinet/in_cksum.c` (C) | Magnitude: 211.1 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 171, indent_tabs: 77, branch: 23, api: 11
- `sys/netinet/if_ether.c` (C) | Magnitude: 335.96 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 194, pointers: 163, state_mutation: 155, branch: 64
- `sys/netinet/in_proto.c` (C) | Magnitude: 44.52 | Delta: **0.173 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, import: 26, api: 15, pointers: 15
- `sys/netinet/in_pcb.c` (C) | Magnitude: 478.32 | Delta: **0.174 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 263, state_mutation: 244, pointers: 205, branch: 106

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `sys/sys/ioctl.h` (C) | Magnitude: 21.48 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 7, api: 6, import: 6, indent_tabs: 4
- `sys/netinet/tcp_seq.h` (C) | Magnitude: 22.36 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: macros: 12, pointers: 8, reflection_metaprogramming: 7, state_mutation: 6
- `sys/sys/mount.h` (C) | Magnitude: 110.48 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 92, structural_boundaries: 90, pointers: 71, indent_tabs: 63
- `sys/sys/socketvar.h` (C) | Magnitude: 134.12 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: pointers: 126, structural_boundaries: 114, api: 89, indent_tabs: 50
- `sys/sys/namei.h` (C) | Magnitude: 57.34 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: api: 41, indent_tabs: 36, structural_boundaries: 18, macros: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sys/sys/ptrace.h` (C) | Magnitude: 17.44 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 14, structural_boundaries: 3, api: 2, import: 2
- `sys/netinet/in_var.h` (C) | Magnitude: 100.24 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 49, state_mutation: 45, structural_boundaries: 40, api: 38
- `sys/netinet/if_ether.h` (C) | Magnitude: 88.32 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 50, indent_tabs: 43, structural_boundaries: 38, class_start: 23
- `sys/sys/signalvar.h` (C) | Magnitude: 45.76 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 44, api: 25, structural_boundaries: 24, macros: 21
- `sys/netinet/ip_icmp.h` (C) | Magnitude: 42.94 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 56, indent_tabs: 33, api: 26, structural_boundaries: 22

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `sys/sys/vnode_if.h` -> **Severity: 0.118** (Embedded: 0.0076 * Error Risk: 15.406%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `sys/sys/vnode_if.h` -> **Severity: 1359.1** (Blast Radius: 13.591 * Doc Risk: 100.0%)
- `sys/sys/dirent.h` -> **Severity: 1358.895** (Blast Radius: 13.591 * Doc Risk: 99.9849%)
- `sys/sys/user.h` -> **Severity: 1341.192** (Blast Radius: 13.591 * Doc Risk: 98.6824%)
- `sys/netinet/icmp_var.h` -> **Severity: 734.6** (Blast Radius: 7.346 * Doc Risk: 100.0%)
- `sys/netinet/igmp_var.h` -> **Severity: 734.6** (Blast Radius: 7.346 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
