# ARCHITECTURAL_BRIEF: xv6-public
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/xv6-public` |
| **Timestamp** | `2026-08-03T19:27:43.796225+00:00` |
| **Scan Duration** | `0.35s` |
| **Git Branch** | `master` |
| **Git Commit** | `eeb7b415dbcb12cc362d0783e41c3d1f44066b17` |
| **Git Remote** | `https://github.com/mit-pdos/xv6-public.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 70 malicious artifacts.

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
| Total Artifacts | 102 |
| Analyzed Artifacts (Scanned) | 84 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 7076 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 82.4% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3008 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2051 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.244 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 65 | 6267 | 77.4% |
| ASSEMBLY | 7 | 203 | 8.3% |
| PERL | 4 | 174 | 4.8% |
| SHELL | 4 | 222 | 4.8% |
| PLAINTEXT | 2 | 0 | 2.4% |
| MAKEFILE | 1 | 210 | 1.2% |
| MARKDOWN | 1 | 0 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.719`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 44 | 52.4% |
| file_cluster_13 | 36 | 42.9% |
| file_cluster_11 | 1 | 1.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 3.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 18*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.c`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.el`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tmpl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ld`: 1x Excluded (Unsupported Extension: '.ld')
- `.h`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.list`: 1x Excluded (Unsupported Extension: '.list')
- `.spec`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.p`: 1x Excluded (Unsupported Extension: '.p')
- `.ftr`: 1x Excluded (Unsupported Extension: '.ftr')
- `.hdr`: 1x Excluded (Unsupported Extension: '.hdr')
- `.pl`: 1x Excluded (Machine-Generated Source Code Signature: 48 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 98.7 | 41.9 | 44.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 36.3 | 21.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 38.7 | 22.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 21.3 | 2.4 | 80.0 |
| API Exposure | 0.0 | 19.3 | 8.5 | 8.7 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 59.8 | 99.9 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 91.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.9 | 100.0 | 78.9 | 96.6 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `usertests.c` (Hits: 185)
- `runoff` (Hits: 65)
- `Makefile` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **types.h** (`types.h`) — 44 inbound connections
2. **param.h** (`param.h`) — 25 inbound connections
3. **defs.h** (`defs.h`) — 24 inbound connections
4. **mmu.h** (`mmu.h`) — 19 inbound connections
5. **x86.h** (`x86.h`) — 19 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **console.c** (`console.c`) — 12 outbound dependencies
2. **ide.c** (`ide.c`) — 12 outbound dependencies
3. **fs.c** (`fs.c`) — 11 outbound dependencies
4. **memide.c** (`memide.c`) — 11 outbound dependencies
5. **sysfile.c** (`sysfile.c`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `trap` (@ `trap.c`) -> Impact: **251.8** | LOC: 77
  * *Intent:* //PAGEBREAK: 41
- `exec` (@ `exec.c`) -> Impact: **130.0** | LOC: 105
  * *Intent:* #include "types.h" #include "param.h" #include "memlayout.h" #include "mmu.h" #include "proc.h" #include "defs.h" #include "x86.h" #include "elf.h"
- `createdelete` (@ `usertests.c`) -> Impact: **128.0** | LOC: 71
  * *Intent:* // four processes create and delete different files in same directory
- `concreate` (@ `usertests.c`) -> Impact: **127.5** | LOC: 90
  * *Intent:* // test concurrent create/link/unlink of the same file
- `subdir` (@ `usertests.c`) -> Impact: **119.4** | LOC: 182
- `scheduler` (@ `proc.c`) -> Impact: **111.4** | LOC: 107
- `Anonymous_Block_[Truncated]` (@ `runoff`) -> Impact: **99.5** | LOC: 237
- `runcmd` (@ `sh.c`) -> Impact: **87.8** | LOC: 75
  * *Intent:* // Execute cmd. Never returns.
- `sharedfd` (@ `usertests.c`) -> Impact: **78.9** | LOC: 50
  * *Intent:* // More file system tests // two processes write to the same file descriptor // is the offset shared? does inode locking work?
- `filewrite` (@ `file.c`) -> Impact: **68.0** | LOC: 40
  * *Intent:* //PAGEBREAK! // Write to file f.

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `trap` (@ `trap.c`) -> **O(2^N) [Recursive]**
  * *Intent:* //PAGEBREAK: 41
- `createdelete` (@ `usertests.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // four processes create and delete different files in same directory
- `insl` (@ `x86.h`) -> **O(2^N) [Recursive]**
- `outsl` (@ `x86.h`) -> **O(2^N) [Recursive]**
- `stosb` (@ `x86.h`) -> **O(2^N) [Recursive]**
- `stosl` (@ `x86.h`) -> **O(2^N) [Recursive]**
- `filewrite` (@ `file.c`) -> **O(2^N) [Recursive]**
  * *Intent:* //PAGEBREAK! // Write to file f.
- `balloc` (@ `fs.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // Blocks. // Allocate a zeroed disk block.
- `scheduler` (@ `proc.c`) -> **O(2^N) [Recursive]**
- `concreate` (@ `usertests.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // test concurrent create/link/unlink of the same file

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `runoff`) -> DB Complexity: **224**
- `subdir` (@ `usertests.c`) -> DB Complexity: **83**
- `concreate` (@ `usertests.c`) -> DB Complexity: **55**
  * *Intent:* // test concurrent create/link/unlink of the same file
- `bigfile` (@ `usertests.c`) -> DB Complexity: **45**
- `writetest` (@ `usertests.c`) -> DB Complexity: **44**
- `unlinkread` (@ `usertests.c`) -> DB Complexity: **42**
  * *Intent:* // can I unlink a file and still read it?
- `createdelete` (@ `usertests.c`) -> DB Complexity: **41**
  * *Intent:* // four processes create and delete different files in same directory
- `writetest1` (@ `usertests.c`) -> DB Complexity: **41**
- `sharedfd` (@ `usertests.c`) -> DB Complexity: **39**
  * *Intent:* // More file system tests // two processes write to the same file descriptor // is the offset shared? does inode locking work?
- `main` (@ `mkfs.c`) -> DB Complexity: **38**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 84 | 9384.02 | 40.43% | 37.3% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `printpcs` -> **100.0%** Exposure
- `show1` -> **100.0%** Exposure
- `spinp` -> **100.0%** Exposure
- `zombie.c` -> **99.9996%** Exposure
- `echo.c` -> **99.9985%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bio.c` -> **100.0%** Exposure
- `bootmain.c` -> **100.0%** Exposure
- `console.c` -> **100.0%** Exposure
- `echo.c` -> **100.0%** Exposure
- `exec.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sysfile.c` -> **13** Orphaned Functions | **0** Duplicates
- `sysproc.c` -> **8** Orphaned Functions | **0** Duplicates
- `pipe.c` -> **4** Orphaned Functions | **0** Duplicates
- `sleeplock.c` -> **4** Orphaned Functions | **0** Duplicates
- `file.c` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`console.c`** -> AI Confidence: **99.48%**
2. **`exec.c`** -> AI Confidence: **99.48%**
3. **`usertests.c`** -> AI Confidence: **99.48%**
4. **`trap.c`** -> AI Confidence: **99.39%**
5. **`stressfs.c`** -> AI Confidence: **99.34%**
6. **`cat.c`** -> AI Confidence: **99.32%**
7. **`echo.c`** -> AI Confidence: **99.32%**
8. **`kill.c`** -> AI Confidence: **99.32%**
9. **`ln.c`** -> AI Confidence: **99.32%**
10. **`mkdir.c`** -> AI Confidence: **99.32%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `cuth` -> **100.0%** Exposure
- `sign.pl` -> **96.2585%** Exposure
- `init.c` -> **20.0%** Exposure
- `syscall.c` -> **20.0%** Exposure
- `trap.c` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `init.c` -> **100.0%** Exposure
- `stressfs.c` -> **100.0%** Exposure
- `usertests.c` -> **100.0%** Exposure
- `cuth` -> **100.0%** Exposure
- `sign.pl` -> **100.0%** Exposure
### Raw Memory Manipulation
- `proc.c` -> **10.0%** Exposure
- `sysfile.c` -> **9.806%** Exposure
- `vm.c` -> **0.7846%** Exposure
- `log.c` -> **0.1988%** Exposure
- `trap.c` -> **0.0899%** Exposure
### Algorithmic DoS Exposure
- `console.c` -> **100.0%** Exposure
- `fs.c` -> **100.0%** Exposure
- `grep.c` -> **100.0%** Exposure
- `ls.c` -> **100.0%** Exposure
- `mkfs.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `281` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `usertests.c` (C) -> Cumulative Risk: **757.82**
- **Archetype:** `file_cluster_8` (Distance: 13.569 IQR)
- **Magnitude:** 2081.36 | **LOC:** 1804 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `createdelete` (Impact: 128.0), `concreate` (Impact: 127.5), `subdir` (Impact: 119.4)

### 2. `pipe.c` (C) -> Cumulative Risk: **702.59**
- **Archetype:** `file_cluster_13` (Distance: 13.363 IQR)
- **Magnitude:** 157.98 | **LOC:** 122 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.2761%), Tech Debt (83.5956%)
- **Heaviest Functions:** `pipealloc` (Impact: 17.4), `pipewrite` (Impact: 16.1), `piperead` (Impact: 15.1)

### 3. `printf.c` (C) -> Cumulative Risk: **683.79**
- **Archetype:** `file_cluster_13` (Distance: 12.828 IQR)
- **Magnitude:** 170.12 | **LOC:** 86 | **CtrlFlow:** 86.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (89.442%)
- **Heaviest Functions:** `printf` (Impact: 62.4), `printint` (Impact: 19.2), `putc` (Impact: 2.0)

### 4. `proc.c` (C) -> Cumulative Risk: **682.55**
- **Archetype:** `file_cluster_13` (Distance: 13.115 IQR)
- **Magnitude:** 313.82 | **LOC:** 535 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (95.4992%)
- **Heaviest Functions:** `scheduler` (Impact: 111.4), `mycpu` (Impact: 12.2), `userinit` (Impact: 10.2)

### 5. `vm.c` (C) -> Cumulative Risk: **668.77**
- **Archetype:** `file_cluster_13` (Distance: 13.289 IQR)
- **Magnitude:** 242.06 | **LOC:** 395 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.1276%)
- **Heaviest Functions:** `copyuvm` (Impact: 19.6), `loaduvm` (Impact: 15.1), `allocuvm` (Impact: 13.4)

### 6. `init.c` (C) -> Cumulative Risk: **662.87**
- **Archetype:** `file_cluster_13` (Distance: 10.943 IQR)
- **Magnitude:** 23.92 | **LOC:** 38 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), State Flux (99.9912%), Documentation (95.5672%)
- **Heaviest Functions:** `main` (Impact: 11.3)

### 7. `cuth` (PERL) -> Cumulative Risk: **661.25**
- **Archetype:** `file_cluster_8` (Distance: 12.413 IQR)
- **Magnitude:** 33.4 | **LOC:** 49 | **CtrlFlow:** 92.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `writefile` (Impact: 5.6)

### 8. `grep.c` (C) -> Cumulative Risk: **656.05**
- **Archetype:** `file_cluster_13` (Distance: 12.591 IQR)
- **Magnitude:** 149.56 | **LOC:** 108 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7582%)
- **Heaviest Functions:** `matchhere` (Impact: 28.3), `grep` (Impact: 16.9), `matchstar` (Impact: 12.4)

### 9. `file.c` (C) -> Cumulative Risk: **652.5**
- **Archetype:** `file_cluster_13` (Distance: 12.206 IQR)
- **Magnitude:** 210.78 | **LOC:** 158 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Algorithmic Dos (99.9999%), Documentation (99.6674%)
- **Heaviest Functions:** `filewrite` (Impact: 68.0), `fileclose` (Impact: 25.2), `fileread` (Impact: 20.9)

### 10. `console.c` (C) -> Cumulative Risk: **649.29**
- **Archetype:** `file_cluster_13` (Distance: 12.736 IQR)
- **Magnitude:** 357.96 | **LOC:** 300 | **CtrlFlow:** 79.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (96.6044%)
- **Heaviest Functions:** `cprintf` (Impact: 62.3), `consoleread` (Impact: 28.9), `printint` (Impact: 17.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `usertests.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.569 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.468 IQR)
- **Top Global Matches:** file_cluster_8: 13.569, file_cluster_13: 13.741, file_cluster_0: 13.746
- **Magnitude:** 2081.36 | **LOC:** 1804 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 83
- **Risk Profile:** Cognitive Load (78.2645%), Tech Debt (9.3495%)
**Top Internal Functions/Classes:**
  * `createdelete` (Impact: 128.0 | O(2^N) | DB: 41)
    * *Intent:* // four processes create and delete different files in same directory
  * `concreate` (Impact: 127.5 | O(2^N) | DB: 55)
    * *Intent:* // test concurrent create/link/unlink of the same file
  * `subdir` (Impact: 119.4 | O(2^N) | DB: 83)
  * `sharedfd` (Impact: 78.9 | O(2^N) | DB: 39)
    * *Intent:* // More file system tests // two processes write to the same file descriptor // is the offset shared...
  * `pipe1` (Impact: 61.9 | O(2^N) | DB: 32)
    * *Intent:* // simple fork and pipe read/write
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 79`, `args: 34`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 34`, `state_mutation: 794`, `dead_code: 4`, `orphaned_logic: 3`
* *Architecture:* `io: 185`, `api: 115`, `import: 9`
* *Defense:* `cleanup: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` param.h, memlayout.h, fs.h, stat.h, fcntl.h, syscall.h, user.h, types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sh.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.867 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.041 IQR)
- **Top Global Matches:** file_cluster_8: 12.867, file_cluster_13: 13.09, file_cluster_0: 13.208
- **Magnitude:** 653.76 | **LOC:** 494 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (73.3871%), Tech Debt (10.5161%)
**Top Internal Functions/Classes:**
  * `runcmd` (Impact: 87.8 | O(2^N) | DB: 38)
    * *Intent:* // Execute cmd. Never returns.
  * `nulterminate` (Impact: 58.2 | O(2^N) | DB: 9)
    * *Intent:* // NUL-terminate all the counted strings.
  * `gettoken` (Impact: 58.1 | O(N^1) | DB: 14)
  * `main` (Impact: 24.8 | O(N^2) | DB: 8)
  * `parseredirs` (Impact: 23.2 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 102`, `args: 26`, `func_start: 19`, `class_start: 50`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 200`, `orphaned_logic: 1`
* *Architecture:* `io: 13`, `api: 106`, `import: 3`
* *Defense:* `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` types.h, fcntl.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sysfile.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.663 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.632 IQR)
- **Top Global Matches:** file_cluster_8: 12.663, file_cluster_13: 12.682, file_cluster_11: 13.038
- **Magnitude:** 439.24 | **LOC:** 445 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (77.6%), Tech Debt (76.4673%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 46.9 | O(2^N) | DB: 7)
  * `sys_unlink` (Impact: 22.6 | O(N^1) | DB: 4)
    * *Intent:* //PAGEBREAK!
  * `sys_open` (Impact: 20.8 | O(N^1) | DB: 9)
  * `isdirempty` (Impact: 16.7 | O(2^N) | DB: 2)
    * *Intent:* // Is the directory dp empty except for "." and ".." ?
  * `sys_link` (Impact: 16.5 | O(N^1) | DB: 4)
    * *Intent:* // Create the path new as a link to the same inode as old.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 92`, `args: 17`, `func_start: 17`, `class_start: 20`
* *Risk/State:* `state_mutation: 147`, `dead_code: 1`, `orphaned_logic: 13`
* *Architecture:* `io: 2`, `api: 71`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` param.h, proc.h, spinlock.h, fs.h, stat.h, fcntl.h, sleeplock.h, mmu.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.94 IQR)
- **Top Global Matches:** file_cluster_8: 11.94, file_cluster_0: 12.013, file_cluster_17: 12.014
- **Magnitude:** 423.2 | **LOC:** 287 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.6227%), Tech Debt (15.8869%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 21`, `func_start: 25`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 12`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `io: 40`, `api: 2`, `import: 1`
* *Defense:* `safety: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` *.d
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `console.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.736 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.818 IQR)
- **Top Global Matches:** file_cluster_13: 12.736, file_cluster_8: 12.792, file_cluster_7: 13.205
- **Magnitude:** 357.96 | **LOC:** 300 | **CtrlFlow:** 79.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (78.4202%), Tech Debt (13.0657%)
**Top Internal Functions/Classes:**
  * `cprintf` (Impact: 62.3 | O(N^2) | DB: 13)
    * *Intent:* //PAGEBREAK: 50 // Print to the console. only understands %d, %x, %p, %s.
  * `consoleread` (Impact: 28.9 | O(N^2) | DB: 7)
  * `printint` (Impact: 17.2 | O(N^1) | DB: 11)
  * `cgaputc` (Impact: 17.2 | O(N^1) | DB: 8)
  * `panic` (Impact: 11.3 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 19`, `args: 10`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 167`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 33`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` param.h, proc.h, spinlock.h, memlayout.h, fs.h, x86.h, sleeplock.h, file.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.115 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.052 IQR)
- **Top Global Matches:** file_cluster_13: 13.115, file_cluster_8: 13.288, file_cluster_11: 13.519
- **Magnitude:** 313.82 | **LOC:** 535 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (90.4049%), Tech Debt (22.7147%)
**Top Internal Functions/Classes:**
  * `scheduler` (Impact: 111.4 | O(2^N) | DB: 19)
  * `mycpu` (Impact: 12.2 | O(2^N) | DB: 3)
    * *Intent:* // Must be called with interrupts disabled to avoid the caller being // rescheduled between reading ...
  * `userinit` (Impact: 10.2 | O(2^N) | DB: 13)
    * *Intent:* //PAGEBREAK: 32 // Set up first user process.
  * `allocproc` (Impact: 9.3 | O(N^1) | DB: 15)
    * *Intent:* //PAGEBREAK: 32 // Look in the process table for an UNUSED proc. // If found, change state to EMBRYO...
  * `myproc` (Impact: 1.9 | O(N^1) | DB: 2)
    * *Intent:* // Disable interrupts so that we are not rescheduled // while reading proc from the cpu structure
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 48`, `args: 13`, `func_start: 11`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 125`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 37`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` param.h, proc.h, spinlock.h, memlayout.h, x86.h, mmu.h, types.h, defs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `trap.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.113 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.373 IQR)
- **Top Global Matches:** file_cluster_13: 11.113, file_cluster_8: 11.239, file_cluster_7: 11.772
- **Magnitude:** 292.68 | **LOC:** 113 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (54.7608%), Tech Debt (57.6638%)
**Top Internal Functions/Classes:**
  * `trap` (Impact: 251.8 | O(2^N) | DB: 5)
    * *Intent:* //PAGEBREAK: 41
  * `tvinit` (Impact: 3.4 | O(N^1) | DB: 2)
  * `idtinit` (Impact: 1.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `state_mutation: 19`, `orphaned_logic: 2`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` param.h, proc.h, spinlock.h, memlayout.h, x86.h, mmu.h, types.h, traps.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mkfs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.044 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.379 IQR)
- **Top Global Matches:** file_cluster_13: 13.044, file_cluster_8: 13.201, file_cluster_0: 13.381
- **Magnitude:** 253.08 | **LOC:** 298 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (64.623%), Tech Debt (13.3266%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 25.9 | O(N^2) | DB: 38)
  * `iappend` (Impact: 12.7 | O(N^2) | DB: 16)
    * *Intent:* #define min(a, b) ((a) < (b) ? (a) : (b))
  * `balloc` (Impact: 7.7 | O(2^N) | DB: 6)
  * `wsect` (Impact: 3.6 | O(N^1) | DB: 6)
  * `rsect` (Impact: 3.6 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 36`, `args: 6`, `func_start: 10`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 132`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 55`, `import: 10`
* *Defense:* `safety: 11`, `test: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdlib.h, param.h, stdio.h, assert.h, fs.h, unistd.h, stat.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exec.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.459 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.074 IQR)
- **Top Global Matches:** file_cluster_13: 13.459, file_cluster_8: 13.749, file_cluster_12: 13.76
- **Magnitude:** 252.88 | **LOC:** 115 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (98.7137%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `exec` (Impact: 130.0 | O(2^N) | DB: 33)
    * *Intent:* #include "types.h" #include "param.h" #include "memlayout.h" #include "mmu.h" #include "proc.h" #inc...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`
* *Architecture:* `api: 22`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` param.h, proc.h, elf.h, memlayout.h, x86.h, mmu.h, types.h, defs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.289 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.803 IQR)
- **Top Global Matches:** file_cluster_13: 13.289, file_cluster_11: 13.583, file_cluster_8: 13.609
- **Magnitude:** 242.06 | **LOC:** 395 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (74.196%), Tech Debt (16.0124%)
**Top Internal Functions/Classes:**
  * `copyuvm` (Impact: 19.6 | O(2^N) | DB: 7)
  * `loaduvm` (Impact: 15.1 | O(2^N) | DB: 6)
  * `allocuvm` (Impact: 13.4 | O(2^N) | DB: 3)
  * `deallocuvm` (Impact: 11.8 | O(N^2) | DB: 7)
    * *Intent:* // 0..KERNBASE: user memory (text+data+stack+heap), mapped to // phys memory allocated by the kernel...
  * `freevm` (Impact: 8.8 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 24`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 114`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 38`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` param.h, proc.h, elf.h, memlayout.h, x86.h, mmu.h, types.h, defs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `log.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.274 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.469 IQR)
- **Top Global Matches:** file_cluster_13: 13.274, file_cluster_8: 13.418, file_cluster_11: 13.634
- **Magnitude:** 212.38 | **LOC:** 235 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (64.7885%), Tech Debt (27.3764%)
**Top Internal Functions/Classes:**
  * `log_write` (Impact: 33.0 | O(2^N) | DB: 5)
    * *Intent:* // Caller has modified b->data and is done with the buffer. // Record the block number and pin in th...
  * `begin_op` (Impact: 10.7 | O(N^1) | DB: 1)
    * *Intent:* // called at the start of each FS system call.
  * `end_op` (Impact: 8.6 | O(N^1) | DB: 5)
    * *Intent:* // called at the end of each FS system call. // commits if this was the last outstanding operation.
  * `initlog` (Impact: 7.6 | O(2^N) | DB: 3)
  * `install_trans` (Impact: 3.5 | O(N^1) | DB: 4)
    * *Intent:* // Copy committed blocks from log to their home location
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 38`, `args: 11`, `func_start: 10`, `class_start: 14`
* *Risk/State:* `state_mutation: 100`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 31`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` param.h, spinlock.h, fs.h, buf.h, sleeplock.h, types.h, defs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `file.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.206 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.962 IQR)
- **Top Global Matches:** file_cluster_13: 12.206, file_cluster_8: 12.277, file_cluster_0: 12.732
- **Magnitude:** 210.78 | **LOC:** 158 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (69.1353%), Tech Debt (57.9953%)
**Top Internal Functions/Classes:**
  * `filewrite` (Impact: 68.0 | O(2^N) | DB: 7)
    * *Intent:* //PAGEBREAK! // Write to file f.
  * `fileclose` (Impact: 25.2 | O(2^N) | DB: 4)
    * *Intent:* // Close file f. (Decrement ref count, close when reaches 0.)
  * `fileread` (Impact: 20.9 | O(2^N) | DB: 2)
    * *Intent:* // Read from file f.
  * `filedup` (Impact: 8.5 | O(2^N) | DB: 1)
    * *Intent:* // Increment ref count for file f.
  * `filealloc` (Impact: 5.0 | O(N^1) | DB: 3)
    * *Intent:* // Allocate a file structure.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 30`, `args: 7`, `func_start: 7`, `class_start: 8`
* *Risk/State:* `state_mutation: 51`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 24`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` param.h, spinlock.h, fs.h, sleeplock.h, file.h, types.h, defs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `string.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.033 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.401 IQR)
- **Top Global Matches:** file_cluster_13: 14.033, file_cluster_8: 14.054, file_cluster_0: 14.32
- **Magnitude:** 207.34 | **LOC:** 106 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (74.2207%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `memmove` (Impact: 12.9 | O(N^1) | DB: 12)
  * `strncmp` (Impact: 10.4 | O(N^1) | DB: 4)
  * `safestrcpy` (Impact: 8.7 | O(N^1) | DB: 6)
    * *Intent:* // Like strncpy but guaranteed to NUL-terminate.
  * `strncpy` (Impact: 8.6 | O(N^1) | DB: 8)
  * `memset` (Impact: 8.5 | O(N^1) | DB: 1)
    * *Intent:* #include "types.h" #include "x86.h"
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 21`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 114`
* *Architecture:* `api: 29`, `import: 2`
* *Defense:* `safety: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` types.h, x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `printf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.828 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.157 IQR)
- **Top Global Matches:** file_cluster_13: 12.828, file_cluster_8: 12.855, file_cluster_7: 13.272
- **Magnitude:** 170.12 | **LOC:** 86 | **CtrlFlow:** 86.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (81.3617%), Tech Debt (37.1377%)
**Top Internal Functions/Classes:**
  * `printf` (Impact: 62.4 | O(N^2) | DB: 14)
    * *Intent:* // Print to the given fd. Only understands %d, %x, %p, %s.
  * `printint` (Impact: 19.2 | O(N^1) | DB: 12)
  * `putc` (Impact: 2.0 | O(N^1) | DB: 3)
    * *Intent:* #include "types.h" #include "stat.h" #include "user.h"
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 4`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 78`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 7`, `import: 3`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` types.h, stat.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pipe.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.363 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.818 IQR)
- **Top Global Matches:** file_cluster_13: 13.363, file_cluster_8: 13.575, file_cluster_11: 13.883
- **Magnitude:** 157.98 | **LOC:** 122 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (78.3198%), Tech Debt (83.5956%)
**Top Internal Functions/Classes:**
  * `pipealloc` (Impact: 17.4 | O(N^1) | DB: 18)
  * `pipewrite` (Impact: 16.1 | O(N^2) | DB: 4)
    * *Intent:* //PAGEBREAK: 40
  * `piperead` (Impact: 15.1 | O(N^1) | DB: 4)
  * `pipeclose` (Impact: 11.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 78`, `orphaned_logic: 4`
* *Architecture:* `api: 18`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` param.h, proc.h, spinlock.h, fs.h, sleeplock.h, mmu.h, file.h, types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `defs.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.577 IQR)
- **Local Micro-Species:** `Cluster 1: Algorithmic Bitwise & Encapsulated Core` (Drift: 4.752 IQR)
- **Top Global Matches:** file_cluster_8: 8.577, file_cluster_7: 9.39, file_cluster_1: 9.649
- **Magnitude:** 155.78 | **LOC:** 191 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 191`, `args: 105`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`
* *Architecture:* `io: 3`, `api: 138`
* *Defense:* `safety: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.285714
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `ide.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.08 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.772 IQR)
- **Top Global Matches:** file_cluster_13: 12.08, file_cluster_8: 12.232, file_cluster_7: 12.703
- **Magnitude:** 155.06 | **LOC:** 169 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (71.4074%), Tech Debt (40.58%)
**Top Internal Functions/Classes:**
  * `iderw` (Impact: 37.6 | O(2^N) | DB: 4)
    * *Intent:* //PAGEBREAK! // Sync buf with disk. // If B_DIRTY is set, write buf to disk, clear B_DIRTY, set B_VA...
  * `idestart` (Impact: 33.4 | O(2^N) | DB: 4)
    * *Intent:* // Start the request for b. Caller must hold idelock.
  * `ideintr` (Impact: 8.5 | O(N^1) | DB: 4)
    * *Intent:* // Interrupt handler.
  * `idewait` (Impact: 7.5 | O(N^1) | DB: 1)
    * *Intent:* // Wait for IDE disk to become ready.
  * `ideinit` (Impact: 6.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 17`, `args: 6`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 48`, `orphaned_logic: 2`
* *Architecture:* `api: 11`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` param.h, proc.h, spinlock.h, memlayout.h, fs.h, x86.h, buf.h, sleeplock.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `grep.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.591 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.906 IQR)
- **Top Global Matches:** file_cluster_13: 12.591, file_cluster_8: 12.603, file_cluster_0: 12.996
- **Magnitude:** 149.56 | **LOC:** 108 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (77.3341%), Tech Debt (31.0999%)
**Top Internal Functions/Classes:**
  * `matchhere` (Impact: 28.3 | O(2^N) | DB: 1)
    * *Intent:* // matchhere: search for re at beginning of text
  * `grep` (Impact: 16.9 | O(N^2) | DB: 17)
  * `matchstar` (Impact: 12.4 | O(N^1) | DB: 1)
    * *Intent:* // matchstar: search for c*re at beginning of text
  * `main` (Impact: 10.0 | O(N^1) | DB: 13)
  * `match` (Impact: 9.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 11`, `args: 8`, `func_start: 5`
* *Risk/State:* `state_mutation: 54`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `api: 17`, `import: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` types.h, stat.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x86.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.932 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.839 IQR)
- **Top Global Matches:** file_cluster_8: 8.932, file_cluster_7: 9.559, file_cluster_1: 9.811
- **Magnitude:** 145.3 | **LOC:** 184 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `insl` (Impact: 8.4 | O(2^N) | DB: 2)
  * `outsl` (Impact: 8.4 | O(2^N) | DB: 2)
  * `stosb` (Impact: 8.4 | O(2^N) | DB: 2)
  * `stosl` (Impact: 8.4 | O(2^N) | DB: 2)
  * `lgdt` (Impact: 4.0 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 30`, `args: 10`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 62`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.362
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.22619
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `umalloc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.233 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.363 IQR)
- **Top Global Matches:** file_cluster_13: 13.233, file_cluster_8: 13.432, file_cluster_11: 13.748
- **Magnitude:** 139.84 | **LOC:** 91 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (74.8553%), Tech Debt (36.5413%)
**Top Internal Functions/Classes:**
  * `free` (Impact: 20.1 | O(N^1) | DB: 10)
  * `malloc` (Impact: 13.4 | O(N^2) | DB: 15)
  * `morecore` (Impact: 3.8 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 15`, `args: 1`, `func_start: 3`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 87`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 14`, `import: 4`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` types.h, stat.h, param.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runoff` (SHELL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 11.976 IQR)
- **Top Global Matches:** file_cluster_11: 11.976, file_cluster_6: 12.152, file_cluster_8: 12.166
- **Magnitude:** 137.88 | **LOC:** 247 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 224
- **Risk Profile:** Cognitive Load (63.5941%), Tech Debt (90.1238%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 99.5 | O(N^1) | DB: 224)
  * `__global_context__` (Impact: 1.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 40`, `args: 29`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 90`, `state_mutation: 33`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 65`
* *Defense:* `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runoff1` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.036 IQR)
- **Top Global Matches:** file_cluster_8: 13.036, file_cluster_0: 13.584, file_cluster_7: 13.606
- **Magnitude:** 136.78 | **LOC:** 109 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (86.8486%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `args: 3`
* *Risk/State:* `state_mutation: 120`
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` the
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bio.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.969 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.89 IQR)
- **Top Global Matches:** file_cluster_13: 12.969, file_cluster_8: 13.113, file_cluster_7: 13.579
- **Magnitude:** 128.28 | **LOC:** 145 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (64.2049%), Tech Debt (57.6638%)
**Top Internal Functions/Classes:**
  * `bget` (Impact: 15.7 | O(2^N) | DB: 9)
    * *Intent:* // Look through buffer cache for block on device dev. // If not found, allocate a buffer. // In eith...
  * `brelse` (Impact: 13.1 | O(2^N) | DB: 7)
    * *Intent:* // Release a locked buffer. // Move to the head of the MRU list.
  * `bwrite` (Impact: 8.4 | O(2^N) | DB: 1)
    * *Intent:* // Write b's contents to disk. Must be locked.
  * `binit` (Impact: 3.8 | O(N^1) | DB: 8)
  * `bread` (Impact: 2.5 | O(N^1) | DB: 1)
    * *Intent:* // Return a locked buf with the contents of the indicated block.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 18`, `args: 3`, `func_start: 5`, `class_start: 8`
* *Risk/State:* `state_mutation: 70`, `orphaned_logic: 2`
* *Architecture:* `api: 13`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` param.h, spinlock.h, fs.h, buf.h, sleeplock.h, types.h, defs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spinlock.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.203 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.626 IQR)
- **Top Global Matches:** file_cluster_13: 12.203, file_cluster_8: 12.498, file_cluster_11: 12.945
- **Magnitude:** 102.8 | **LOC:** 127 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (71.3876%), Tech Debt (74.4868%)
**Top Internal Functions/Classes:**
  * `popcli` (Impact: 14.6 | O(2^N) | DB: 1)
    * *Intent:* // Check whether this cpu is holding the lock.
  * `acquire` (Impact: 12.9 | O(2^N))
    * *Intent:* // Acquire the lock. // Loops (spins) until the lock is acquired. // Holding a lock for a long time ...
  * `getcallerpcs` (Impact: 12.9 | O(N^1) | DB: 7)
  * `holding` (Impact: 4.5 | O(N^1) | DB: 1)
  * `pushcli` (Impact: 3.4 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 12`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 39`, `orphaned_logic: 2`
* *Architecture:* `api: 12`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` param.h, proc.h, spinlock.h, memlayout.h, x86.h, mmu.h, types.h, defs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ls.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.738 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.343 IQR)
- **Top Global Matches:** file_cluster_13: 11.738, file_cluster_8: 11.86, file_cluster_0: 12.285
- **Magnitude:** 99.36 | **LOC:** 86 | **CtrlFlow:** 73.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (75.9636%), Tech Debt (39.0501%)
**Top Internal Functions/Classes:**
  * `ls` (Impact: 41.3 | O(N^2) | DB: 32)
  * `fmtname` (Impact: 7.8 | O(N^1) | DB: 3)
    * *Intent:* #include "types.h" #include "stat.h" #include "user.h" #include "fs.h"
  * `main` (Impact: 5.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 7`, `args: 3`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `api: 13`, `import: 4`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.17
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` types.h, fs.h, stat.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `runoff` (SHELL) | Magnitude: 137.88 | Delta: **0.176 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 145, safety_bypasses: 90, io: 65, branch: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `grep.c` (C) | Magnitude: 149.56 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, state_mutation: 54, branch: 25, pointers: 19
- `string.c` (C) | Magnitude: 207.34 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 114, indent_spaces: 53, pointers: 35, api: 29
- `printf.c` (C) | Magnitude: 170.12 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 78, indent_spaces: 61, branch: 26, pointers: 9
- `console.c` (C) | Magnitude: 357.96 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 189, state_mutation: 167, branch: 73, api: 33
- `file.c` (C) | Magnitude: 210.78 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 86, state_mutation: 51, pointers: 49, structural_boundaries: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `sysfile.c` (C) | Magnitude: 439.24 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 286, state_mutation: 147, pointers: 103, structural_boundaries: 92
- `ioapic.c` (C) | Magnitude: 43.58 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, state_mutation: 18, api: 9, structural_boundaries: 8
- `Makefile` (MAKEFILE) | Magnitude: 423.2 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 147, io: 40, branch: 29, func_start: 25
- `cuth` (PERL) | Magnitude: 33.4 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 34, state_mutation: 27, branch: 13, io: 7
- `usertests.c` (C) | Magnitude: 2081.36 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1363, state_mutation: 794, branch: 319, debug_prints: 251

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `user.h` -> **Severity: 13.878** (Embedded: 0.1905 * Error Risk: 72.8571%)
- `mmu.h` -> **Severity: 3.329** (Embedded: 0.2262 * Error Risk: 14.7197%)
- `x86.h` -> **Severity: 2.256** (Embedded: 0.2262 * Error Risk: 9.975%)
- `defs.h` -> **Severity: 2.171** (Embedded: 0.2857 * Error Risk: 7.5991%)
- `kbd.h` -> **Severity: 0.092** (Embedded: 0.0119 * Error Risk: 7.7076%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `user.h` -> **Severity: 4109.7** (Blast Radius: 41.097 * Doc Risk: 100.0%)
- `defs.h` -> **Severity: 3197.4** (Blast Radius: 31.974 * Doc Risk: 100.0%)
- `x86.h` -> **Severity: 3136.2** (Blast Radius: 31.362 * Doc Risk: 100.0%)
- `stat.h` -> **Severity: 2762.201** (Blast Radius: 41.433 * Doc Risk: 66.6667%)
- `mmu.h` -> **Severity: 2494.8** (Blast Radius: 24.948 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
