# ARCHITECTURAL_BRIEF: prokka
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/prokka` |
| **Timestamp** | `2026-08-03T19:30:25.570498+00:00` |
| **Scan Duration** | `1.21s` |
| **Git Branch** | `master` |
| **Git Commit** | `045d3c5f8a1a54a873d76eb4b6c8f85d4fb82944` |
| **Git Remote** | `https://github.com/tseemann/prokka.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3 malicious artifacts.

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
| Total Artifacts | 104 |
| Analyzed Artifacts (Scanned) | 20 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 84 |
| Total LOC | 2339 |
| Volatility Index | 0.1 |
| % Scanned of codebase = | 19.2% |
| Dominant Lang | PERL |

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
| PERL | 12 | 2223 | 60.0% |
| MARKDOWN | 2 | 0 | 10.0% |
| SHELL | 2 | 53 | 10.0% |
| PLAINTEXT | 2 | 0 | 10.0% |
| YAML | 1 | 16 | 5.0% |
| MAKEFILE | 1 | 47 | 5.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.366`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 6 | 30.0% |
| file_cluster_8 | 5 | 25.0% |
| file_cluster_17 | 3 | 15.0% |
| file_cluster_13 | 2 | 10.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 20.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 84*

**Composition by Extension & Reason:**
- `.pm`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 1x Excluded (File size exceeds 50MB limit without Intent Lock)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sql`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.fna`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.hamap`: 1x Excluded (Unsupported Extension: '.HAMAP')
- `.pfam`: 1x Excluded (Unsupported Extension: '.Pfam')
- `.prokka`: 1x Excluded (Unsupported Extension: '.Prokka')
- `.rfam`: 1x Excluded (Unsupported Extension: '.Rfam')
- `.uniprot`: 1x Excluded (Unsupported Extension: '.UniProt')
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 7.3 | 98.1 | 81.8 | 92.2 | 98.1 |
| Error & Exception Exposure | 0.0 | 96.7 | 73.4 | 83.7 | 91.7 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Testing Exposure | 2.3 | 80.0 | 7.3 | 2.3 | 2.3 |
| API Exposure | 0.0 | 7.5 | 0.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 28.3 | 1.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 87.5 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 45.3 | 8.5 | 3.8 | 0.0 |
| Specification Exposure | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.6 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 80.8 | 13.7 | 0.0 | 0.0 |
| Documentation Exposure | 11.9 | 100.0 | 43.9 | 27.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 2.0 | 0.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 18.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 19.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `bin/prokka` (Hits: 23)
- `update-dbs/Makefile` (Hits: 16)
- `bin/prokka-build_kingdom_dbs` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **prokka** (`bin/prokka`) — 0 inbound connections
4. **prokka-abricate_to_fasta_db** (`bin/prokka-abricate_to_fasta_db`) — 0 inbound connections
5. **prokka-biocyc_to_fasta_db** (`bin/prokka-biocyc_to_fasta_db`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **prokka** (`bin/prokka`) — 33 outbound dependencies
2. **prokka-genbank_to_fasta_db** (`bin/prokka-genbank_to_fasta_db`) — 8 outbound dependencies
3. **UniProt-to-sprot.pl** (`update-dbs/UniProt-to-sprot.pl`) — 8 outbound dependencies
4. **prokka-biocyc_to_fasta_db** (`bin/prokka-biocyc_to_fasta_db`) — 7 outbound dependencies
5. **prokka-cdd_to_hmm** (`bin/prokka-cdd_to_hmm`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `kingdoms` (@ `bin/prokka`) -> Impact: **339.0** | LOC: 220
  * *Intent:* #----------------------------------------------------------------------
- `setOptions` (@ `bin/prokka-uniprot_to_fasta_db`) -> Impact: **22.8** | LOC: 36
  * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option setting routines
- `setOptions` (@ `update-dbs/UniProt-to-sprot.pl`) -> Impact: **22.8** | LOC: 36
  * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option setting routines
- `cleanup_product` (@ `bin/prokka`) -> Impact: **22.7** | LOC: 30
  * *Intent:* #EXIT #----------------------------------------------------------------------
- `find_exe` (@ `bin/prokka`) -> Impact: **10.3** | LOC: 8
  * *Intent:* #----------------------------------------------------------------------
- `setOptions` (@ `bin/prokka-clusters_to_hmm`) -> Impact: **10.1** | LOC: 22
  * *Intent:* #---------------------------------------------------------------------- # Option setting routines
- `usage` (@ `bin/prokka-clusters_to_hmm`) -> Impact: **9.4** | LOC: 8
- `usage` (@ `bin/prokka-genpept_to_fasta_db`) -> Impact: **9.4** | LOC: 8
- `setOptions` (@ `bin/prokka-genpept_to_fasta_db`) -> Impact: **9.3** | LOC: 26
  * *Intent:* #---------------------------------------------------------------------- # Option setting routines
- `show_citation` (@ `bin/prokka`) -> Impact: **7.9** | LOC: 18
  * *Intent:* #----------------------------------------------------------------------

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `kingdoms` (@ `bin/prokka`) -> **O(2^N) [Recursive]**
  * *Intent:* #----------------------------------------------------------------------

### Highest Data Gravity (Database Complexity)
- `kingdoms` (@ `bin/prokka`) -> DB Complexity: **37**
  * *Intent:* #----------------------------------------------------------------------
- `cleanup_product` (@ `bin/prokka`) -> DB Complexity: **21**
  * *Intent:* #EXIT #----------------------------------------------------------------------
- `Anonymous_Block` (@ `bin/prokka-build_kingdom_dbs`) -> DB Complexity: **21**
- `msg` (@ `bin/prokka`) -> DB Complexity: **4**
  * *Intent:* #----------------------------------------------------------------------
- `Anonymous_Block` (@ `bin/prokka-make_tarball`) -> DB Complexity: **3**
- `find_exe` (@ `bin/prokka`) -> DB Complexity: **2**
  * *Intent:* #----------------------------------------------------------------------
- `num_cpu` (@ `bin/prokka`) -> DB Complexity: **2**
  * *Intent:* #----------------------------------------------------------------------
- `num_digits` (@ `bin/prokka`) -> DB Complexity: **2**
  * *Intent:* #----------------------------------------------------------------------
- `setOptions` (@ `bin/prokka-uniprot_to_fasta_db`) -> DB Complexity: **2**
  * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option setting routines
- `setOptions` (@ `update-dbs/UniProt-to-sprot.pl`) -> DB Complexity: **2**
  * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option setting routines

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `bin` | 12 | 5160.56 | 93.2% | 18.69% |
| `update-dbs` | 3 | 141.12 | 60.05% | 0.0% |
| `__monolith__` | 3 | 26.98 | 3.45% | 0.0% |
| `doc` | 2 | 4.88 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bin/prokka-make_tarball` -> **100.0%** Exposure
- `bin/prokka-build_kingdom_dbs` -> **99.9912%** Exposure
- `bin/prokka` -> **24.3107%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/prokka` -> **100.0%** Exposure
- `bin/prokka-abricate_to_fasta_db` -> **100.0%** Exposure
- `bin/prokka-biocyc_to_fasta_db` -> **100.0%** Exposure
- `bin/prokka-cdd_to_hmm` -> **100.0%** Exposure
- `bin/prokka-clusters_to_hmm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `bin/prokka-make_tarball` -> **1** Orphaned Functions | **3** Duplicates
- `bin/prokka-build_kingdom_dbs` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bin/prokka-make_tarball`** -> AI Confidence: **98.96%**
2. **`bin/prokka-build_kingdom_dbs`** -> AI Confidence: **98.86%**
3. **`update-dbs/Makefile`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `bin/prokka-clusters_to_hmm` -> **100.0%** Exposure
- `bin/prokka-hamap_to_hmm` -> **100.0%** Exposure
- `bin/prokka` -> **99.9997%** Exposure
- `bin/prokka-biocyc_to_fasta_db` -> **0.336%** Exposure
- `bin/prokka-genbank_to_fasta_db` -> **0.0028%** Exposure
### Weaponizable Injection Vectors
- `bin/prokka-clusters_to_hmm` -> **100.0%** Exposure
- `bin/prokka-hamap_to_hmm` -> **100.0%** Exposure
- `update-dbs/Makefile` -> **99.9997%** Exposure
- `bin/prokka` -> **6.6635%** Exposure
### Algorithmic DoS Exposure
- `bin/prokka-uniprot_to_fasta_db` -> **1.9558%** Exposure
- `update-dbs/UniProt-to-sprot.pl` -> **1.9512%** Exposure
- `bin/prokka-genpept_to_fasta_db` -> **1.3563%** Exposure
- `bin/prokka-clusters_to_hmm` -> **1.3375%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `93` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `bin/prokka` (PERL) -> Cumulative Risk: **732.9**
- **Archetype:** `file_cluster_0` (Distance: 14.003 IQR)
- **Magnitude:** 1606.02 | **LOC:** 1834 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.9997%), Cognitive Load (98.1438%)
- **Heaviest Functions:** `kingdoms` (Impact: 339.0), `cleanup_product` (Impact: 22.7), `find_exe` (Impact: 10.3)

### 2. `bin/prokka-hamap_to_hmm` (PERL) -> Cumulative Risk: **650.06**
- **Archetype:** `file_cluster_17` (Distance: 12.972 IQR)
- **Magnitude:** 818.22 | **LOC:** 160 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)

### 3. `bin/prokka-clusters_to_hmm` (PERL) -> Cumulative Risk: **621.37**
- **Archetype:** `file_cluster_0` (Distance: 12.725 IQR)
- **Magnitude:** 75.02 | **LOC:** 111 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `setOptions` (Impact: 10.1), `usage` (Impact: 9.4)

### 4. `bin/prokka-build_kingdom_dbs` (SHELL) -> Cumulative Risk: **584.41**
- **Archetype:** `file_cluster_8` (Distance: 11.813 IQR)
- **Magnitude:** 17.18 | **LOC:** 42 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9912%), Cognitive Load (97.2852%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 4.3), `__global_context__` (Impact: 1.5)

### 5. `bin/prokka-make_tarball` (SHELL) -> Cumulative Risk: **555.85**
- **Archetype:** `file_cluster_8` (Distance: 10.818 IQR)
- **Magnitude:** 24.98 | **LOC:** 48 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9994%), Safety Score (96.7003%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 3.2), `Anonymous_Block` (Impact: 3.2), `Anonymous_Block` (Impact: 3.1)

### 6. `bin/prokka-abricate_to_fasta_db` (PERL) -> Cumulative Risk: **463.97**
- **Archetype:** `file_cluster_13` (Distance: 12.899 IQR)
- **Magnitude:** 42.46 | **LOC:** 45 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (94.6321%), Safety Score (89.6858%)

### 7. `update-dbs/AMRprot-to-AMR.pl` (PERL) -> Cumulative Risk: **446.84**
- **Archetype:** `file_cluster_8` (Distance: 11.085 IQR)
- **Magnitude:** 24.44 | **LOC:** 40 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Cognitive Load (81.0697%)

### 8. `bin/prokka-genpept_to_fasta_db` (PERL) -> Cumulative Risk: **445.72**
- **Archetype:** `file_cluster_0` (Distance: 16.361 IQR)
- **Magnitude:** 59.62 | **LOC:** 96 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (93.4364%), Safety Score (69.4708%)
- **Heaviest Functions:** `usage` (Impact: 9.4), `setOptions` (Impact: 9.3), `TAG` (Impact: 3.7)

### 9. `update-dbs/UniProt-to-sprot.pl` (PERL) -> Cumulative Risk: **445.02**
- **Archetype:** `file_cluster_0` (Distance: 14.181 IQR)
- **Magnitude:** 96.74 | **LOC:** 150 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (91.7766%), Safety Score (81.6424%)
- **Heaviest Functions:** `setOptions` (Impact: 22.8)

### 10. `bin/prokka-cdd_to_hmm` (PERL) -> Cumulative Risk: **430.48**
- **Archetype:** `file_cluster_0` (Distance: 14.506 IQR)
- **Magnitude:** 716.88 | **LOC:** 136 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.0436%), Cognitive Load (95.5376%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `bin/prokka` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.003 IQR)
- **Top Global Matches:** file_cluster_0: 14.003, file_cluster_17: 14.136, file_cluster_13: 14.191
- **Magnitude:** 1606.02 | **LOC:** 1834 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (98.1438%), Tech Debt (24.3107%)
**Top Internal Functions/Classes:**
  * `kingdoms` (Impact: 339.0 | O(2^N) | DB: 37)
    * *Intent:* #----------------------------------------------------------------------
  * `cleanup_product` (Impact: 22.7 | O(N^1) | DB: 21)
    * *Intent:* #EXIT #----------------------------------------------------------------------
  * `find_exe` (Impact: 10.3 | O(N^1) | DB: 2)
    * *Intent:* #----------------------------------------------------------------------
  * `show_citation` (Impact: 7.9 | O(N^1))
    * *Intent:* #----------------------------------------------------------------------
  * `num_cpu` (Impact: 6.5 | O(N^1) | DB: 2)
    * *Intent:* #----------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 618`, `structural_boundaries: 321`, `args: 10`, `func_start: 26`
* *Risk/State:* `high_risk_execution: 16`, `state_mutation: 1155`, `dead_code: 10`, `fragile_debt: 12`
* *Architecture:* `io: 23`, `api: 1`, `concurrency: 12`, `import: 32`
* *Defense:* `safety: 4`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, odd, Data::Dumper, RNAmmer, this, FindBin, Time::Seconds, Bio::Seq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-genbank_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.342 IQR)
- **Top Global Matches:** file_cluster_17: 13.342, file_cluster_0: 13.348, file_cluster_13: 13.403
- **Magnitude:** 886.64 | **LOC:** 141 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (92.2456%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 27`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 51`, `dead_code: 1`
* *Architecture:* `import: 8`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, as, Data::Dumper, Bio::Tools::CodonTable, Getopt::Long, first, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-hamap_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.972 IQR)
- **Top Global Matches:** file_cluster_17: 12.972, file_cluster_0: 13.121, file_cluster_13: 13.148
- **Magnitude:** 818.22 | **LOC:** 160 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (93.8965%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 23`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 77`, `dead_code: 1`
* *Architecture:* `io: 1`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, Data::Dumper, Getopt::Long, File::Temp, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-biocyc_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.721 IQR)
- **Top Global Matches:** file_cluster_17: 12.721, file_cluster_13: 12.728, file_cluster_0: 12.763
- **Magnitude:** 749.74 | **LOC:** 118 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (92.2054%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 27`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 55`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, Data::Dumper, Getopt::Long, strict, warnings, HTML::Entities, Text::Unidecode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-cdd_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.506 IQR)
- **Top Global Matches:** file_cluster_0: 14.506, file_cluster_13: 14.721, file_cluster_17: 14.786
- **Magnitude:** 716.88 | **LOC:** 136 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (95.5376%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 23`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 78`, `dead_code: 2`
* *Architecture:* `io: 2`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, Data::Dumper, Getopt::Long, File::Temp, strict, warnings, Bio::AlignIO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/UniProt-to-sprot.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.181 IQR)
- **Top Global Matches:** file_cluster_0: 14.181, file_cluster_13: 14.252, file_cluster_17: 14.281
- **Magnitude:** 96.74 | **LOC:** 150 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (91.7766%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` (Impact: 22.8 | O(N^2) | DB: 2)
    * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 21`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 72`, `dead_code: 2`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SWISS::KW, Data::Dumper, Getopt::Long, lib, SWISS::OC, strict, warnings, SWISS::Entry
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-uniprot_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.185 IQR)
- **Top Global Matches:** file_cluster_0: 14.185, file_cluster_17: 14.287, file_cluster_13: 14.291
- **Magnitude:** 96.72 | **LOC:** 150 | **CtrlFlow:** 75.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (91.8089%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` (Impact: 22.8 | O(N^2) | DB: 2)
    * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 20`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 72`, `dead_code: 2`
* *Architecture:* `io: 1`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SWISS::KW, Data::Dumper, Getopt::Long, SWISS::OC, strict, warnings, SWISS::Entry
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-clusters_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.725 IQR)
- **Top Global Matches:** file_cluster_0: 12.725, file_cluster_13: 12.933, file_cluster_17: 13.161
- **Magnitude:** 75.02 | **LOC:** 111 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (96.4967%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` (Impact: 10.1 | O(N^1) | DB: 1)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `usage` (Impact: 9.4 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 20`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 54`
* *Architecture:* `io: 4`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dumper, Getopt::Long, File::Temp, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-tigrfams_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.757 IQR)
- **Top Global Matches:** file_cluster_13: 15.757, file_cluster_0: 15.836, file_cluster_17: 15.945
- **Magnitude:** 67.08 | **LOC:** 101 | **CtrlFlow:** 81.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 5`
* *Risk/State:* `state_mutation: 51`, `dead_code: 2`
* *Architecture:* `io: 1`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MAP, strict, warnings, CS
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-genpept_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.361 IQR)
- **Top Global Matches:** file_cluster_0: 16.361, file_cluster_17: 16.467, file_cluster_13: 16.569
- **Magnitude:** 59.62 | **LOC:** 96 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (93.4364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 9.4 | O(N^2) | DB: 1)
  * `setOptions` (Impact: 9.3 | O(N^1) | DB: 1)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `TAG` (Impact: 3.7 | O(N^1))
    * *Intent:* #----------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 18`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 36`, `dead_code: 3`
* *Architecture:* `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, as, Getopt::Long, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-abricate_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.899 IQR)
- **Top Global Matches:** file_cluster_13: 12.899, file_cluster_0: 12.906, file_cluster_8: 13.091
- **Magnitude:** 42.46 | **LOC:** 45 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (94.6321%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 10`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-make_tarball` (SHELL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.818 IQR)
- **Top Global Matches:** file_cluster_8: 10.818, file_cluster_13: 11.394, file_cluster_0: 11.397
- **Magnitude:** 24.98 | **LOC:** 48 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (84.6301%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 3.2 | O(N^1))
  * `Anonymous_Block` (Impact: 3.2 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 3.1 | O(N^1))
  * `__global_context__` (Impact: 2.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 9`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 12`, `duplicate_logic: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 8`
* *Defense:* `test: 1`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/AMRprot-to-AMR.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.085 IQR)
- **Top Global Matches:** file_cluster_8: 11.085, file_cluster_13: 11.285, file_cluster_17: 11.763
- **Magnitude:** 24.44 | **LOC:** 40 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (81.0697%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.224 IQR)
- **Top Global Matches:** file_cluster_8: 7.224, file_cluster_7: 8.268, file_cluster_1: 8.39
- **Magnitude:** 19.94 | **LOC:** 71 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.3101%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `func_start: 16`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 16`, `api: 4`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-build_kingdom_dbs` (SHELL | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.813 IQR)
- **Top Global Matches:** file_cluster_8: 11.813, file_cluster_12: 12.121, file_cluster_0: 12.331
- **Magnitude:** 17.18 | **LOC:** 42 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (97.2852%), Tech Debt (99.9912%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 4.3 | O(N^1) | DB: 21)
  * `__global_context__` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 11`, `orphaned_logic: 1`
* *Architecture:* `io: 8`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `environment.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.32 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.3633%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 10.12 | **LOC:** 506 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/ChangeLog.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 3.88 | **LOC:** 194 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CODE_OF_CONDUCT.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.54 | **LOC:** 77 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/ToDoList.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `update-dbs/UniProt-to-sprot.pl` (PERL) | Magnitude: 96.74 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 72, indent_spaces: 71, branch: 61, structural_boundaries: 21
- `bin/prokka-uniprot_to_fasta_db` (PERL) | Magnitude: 96.72 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 72, indent_spaces: 71, branch: 61, structural_boundaries: 20
- `bin/prokka-genpept_to_fasta_db` (PERL) | Magnitude: 59.62 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 36, branch: 34, structural_boundaries: 18
- `bin/prokka` (PERL) | Magnitude: 1606.02 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 1155, indent_spaces: 1054, branch: 618, structural_boundaries: 321
- `bin/prokka-clusters_to_hmm` (PERL) | Magnitude: 75.02 | Delta: **0.208 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 54, branch: 41, indent_spaces: 35, structural_boundaries: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `bin/prokka-abricate_to_fasta_db` (PERL) | Magnitude: 42.46 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 27, branch: 14, indent_spaces: 14, structural_boundaries: 10
- `bin/prokka-tigrfams_to_hmm` (PERL) | Magnitude: 67.08 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 51, branch: 22, regex_execution: 21, indent_spaces: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `bin/prokka-genbank_to_fasta_db` (PERL) | Magnitude: 886.64 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 62, branch: 55, state_mutation: 51, structural_boundaries: 27
- `bin/prokka-biocyc_to_fasta_db` (PERL) | Magnitude: 749.74 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 55, indent_spaces: 50, branch: 45, structural_boundaries: 27
- `bin/prokka-hamap_to_hmm` (PERL) | Magnitude: 818.22 | Delta: **0.149 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 78, state_mutation: 77, branch: 47, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `update-dbs/AMRprot-to-AMR.pl` (PERL) | Magnitude: 24.44 | Delta: **0.2 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 9, bitwise_ops: 5, regex_execution: 4
- `bin/prokka-build_kingdom_dbs` (SHELL) | Magnitude: 17.18 | Delta: **0.308 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 11, indent_spaces: 10, io: 8, structural_boundaries: 5
- `bin/prokka-make_tarball` (SHELL) | Magnitude: 24.98 | Delta: **0.576 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: debug_prints: 13, safety_bypasses: 12, state_mutation: 12, structural_boundaries: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bin/prokka` -> Churn: **80.85%** | Cog Load: 98.1438% | Debt: 24.3107%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `bin/prokka-genbank_to_fasta_db` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 886.64
- `bin/prokka-hamap_to_hmm` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 818.22
- `update-dbs/UniProt-to-sprot.pl` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 96.74

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `update-dbs/AMRprot-to-AMR.pl` -> **Severity: 5000.0** (Blast Radius: 50.0 * Doc Risk: 100.0%)
- `update-dbs/Makefile` -> **Severity: 5000.0** (Blast Radius: 50.0 * Doc Risk: 100.0%)
- `bin/prokka-build_kingdom_dbs` -> **Severity: 4595.235** (Blast Radius: 50.0 * Doc Risk: 91.9047%)
- `bin/prokka-abricate_to_fasta_db` -> **Severity: 3867.95** (Blast Radius: 50.0 * Doc Risk: 77.359%)
- `bin/prokka-make_tarball` -> **Severity: 3596.685** (Blast Radius: 50.0 * Doc Risk: 71.9337%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
