# ARCHITECTURAL_BRIEF: prokka
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tseemann/prokka.git` |
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
| Total Artifacts | 104 |
| Analyzed Artifacts (Scanned) | 23 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 81 |
| Total LOC | 2402 |
| Volatility Index | 0.043 |
| % Scanned of codebase = | 22.1% |
| Dominant Lang | PERL |

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
| PERL | 12 | 2223 | 52.2% |
| SQLITE | 3 | 63 | 13.0% |
| MARKDOWN | 2 | 0 | 8.7% |
| SHELL | 2 | 53 | 8.7% |
| PLAINTEXT | 2 | 0 | 8.7% |
| YAML | 1 | 16 | 4.3% |
| MAKEFILE | 1 | 47 | 4.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** I/O & Config Routines Files 39%, Declarative / Non-Code 35%, Data / Markup / Trivial 22%, Large Core Modules 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19 | 82.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 17.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 81*

**Composition by Extension & Reason:**
- `.pm`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 1x Excluded (File size exceeds 50MB limit without Intent Lock)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 88.1 | 43.7 | 39.2 | 5.1 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.9 | 64.4 | 83.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 73.1 | 5.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 6.5 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 49.9 | 5.2 | 4.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 20.9 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 68.1 | 99.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 45.3 | 7.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 52.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 67.4 | 10.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 52.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 13 | 2 | 0 | `bin/prokka` |
| cleanup | 5 | 3 | 1 | `bin/prokka` |
| guards | 24 | 11 | 2 | `bin/prokka` |
| danger | 99 | 12 | 13 | `bin/prokka` |
| concurrency | 5 | 3 | 1 | `bin/prokka` |
| connectivity | 50 | 10 | 3 | `bin/prokka` |
| io | 64 | 12 | 8 | `bin/prokka` |
| crypto | 0 | 0 | 0 | - |
| ipc | 26 | 6 | 4 | `bin/prokka` |
| time | 6 | 2 | 0 | `bin/prokka` |
| serialization | 0 | 0 | 0 | - |
| regex | 315 | 15 | 17 | `bin/prokka` |
| events | 0 | 0 | 0 | - |
| tests | 1 | 1 | 0 | `bin/prokka-make_tarball` |
| docs | 0 | 0 | 0 | - |
| debt | 128 | 13 | 15 | `bin/prokka` |
| mutation | 395 | 14 | 13 | `bin/prokka` |
| dead_code | 24 | 9 | 2 | `bin/prokka` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `bin/prokka-make_tarball` |
| ml_ai | 7 | 1 | 0 | `bin/prokka` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `bin/prokka` (Hits: 20)
- `update-dbs/Makefile` (Hits: 16)
- `bin/prokka-build_kingdom_dbs` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **prokka** (`bin/prokka`) — 33 outbound dependencies
2. **prokka-genbank_to_fasta_db** (`bin/prokka-genbank_to_fasta_db`) — 8 outbound dependencies
3. **UniProt-to-sprot.pl** (`update-dbs/UniProt-to-sprot.pl`) — 8 outbound dependencies
4. **prokka-biocyc_to_fasta_db** (`bin/prokka-biocyc_to_fasta_db`) — 7 outbound dependencies
5. **prokka-cdd_to_hmm** (`bin/prokka-cdd_to_hmm`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `setOptions` **(I/O & Config Routines)** (@ `bin/prokka`) -> Impact: **28.5** | LOC: 70
  * *Intent:* #---------------------------------------------------------------------- # Option setting routines
- `usage` **(Compute Cores)** (@ `bin/prokka`) -> Impact: **28.2** | LOC: 27
- `cleanup_product` **(Compute Cores)** (@ `bin/prokka`) -> Impact: **22.7** | LOC: 30
  * *Intent:* #EXIT #----------------------------------------------------------------------
- `setup_db` **(I/O & Config Routines)** (@ `bin/prokka`) -> Impact: **16.9** | LOC: 39
  * *Intent:* #----------------------------------------------------------------------
- `check_tool` **(Compute Cores)** (@ `bin/prokka`) -> Impact: **12.6** | LOC: 26
- `clean_db` **(Compute Cores)** (@ `bin/prokka`) -> Impact: **11.8** | LOC: 10
  * *Intent:* #----------------------------------------------------------------------
- `setOptions` **(I/O & Config Routines)** (@ `bin/prokka-genbank_to_fasta_db`) -> Impact: **10.3** | LOC: 27
  * *Intent:* #---------------------------------------------------------------------- # Option setting routines
- `show_citation` **(I/O & Config Routines)** (@ `bin/prokka`) -> Impact: **8.9** | LOC: 18
  * *Intent:* #----------------------------------------------------------------------
- `setOptions` **(I/O & Config Routines)** (@ `bin/prokka-hamap_to_hmm`) -> Impact: **8.4** | LOC: 28
  * *Intent:* #---------------------------------------------------------------------- # Option setting routines
- `setOptions` **(I/O & Config Routines)** (@ `bin/prokka-uniprot_to_fasta_db`) -> Impact: **8.3** | LOC: 27
  * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option setting routines

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `bin` | 12 | 1244.94 | 59.78% | 1.97% |
| `update-dbs` | 3 | 96.82 | 32.45% | 24.37% |
| `__monolith__` | 3 | 26.98 | 0.0% | 0.0% |
| `db/cm/__build` | 3 | 10.26 | 5.12% | 0.0% |
| `doc` | 2 | 4.88 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `update-dbs/Makefile` -> **73.1059%** Exposure
- `bin/prokka` -> **23.6646%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bin/prokka` -> **99.9999%** Exposure
- `bin/prokka-uniprot_to_fasta_db` -> **99.9998%** Exposure
- `update-dbs/UniProt-to-sprot.pl` -> **99.9997%** Exposure
- `bin/prokka-hamap_to_hmm` -> **99.9987%** Exposure
- `bin/prokka-tigrfams_to_hmm` -> **99.9982%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `update-dbs/Makefile` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `94` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `bin/prokka` (PERL) -> Cumulative Risk: **726.34**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.67)
- **Magnitude:** 827.32 | **LOC:** 1834 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 62.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (94.6238%)
- **Heaviest Functions:** `setOptions` (I/O & Config Routines, Impact: 28.5), `usage` (Compute Cores, Impact: 28.2), `cleanup_product` (Compute Cores, Impact: 22.7)

### 2. `update-dbs/UniProt-to-sprot.pl` (PERL) -> Cumulative Risk: **518.77**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.58)
- **Magnitude:** 55.64 | **LOC:** 150 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Safety Score (91.7606%)
- **Heaviest Functions:** `setOptions` (I/O & Config Routines, Impact: 8.3), `usage` (I/O & Config Routines, Impact: 6.4)

### 3. `bin/prokka-hamap_to_hmm` (PERL) -> Cumulative Risk: **505.73**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.69)
- **Magnitude:** 66.9 | **LOC:** 160 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9987%), Safety Score (98.016%)
- **Heaviest Functions:** `setOptions` (I/O & Config Routines, Impact: 8.4), `usage` (I/O & Config Routines, Impact: 6.4), `get_file` (Compute Cores, Impact: 5.7)

### 4. `bin/prokka-cdd_to_hmm` (PERL) -> Cumulative Risk: **502.64**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.54)
- **Magnitude:** 48.38 | **LOC:** 136 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9979%), Safety Score (96.8356%)
- **Heaviest Functions:** `setOptions` (I/O & Config Routines, Impact: 7.1), `usage` (I/O & Config Routines, Impact: 6.4)

### 5. `bin/prokka-uniprot_to_fasta_db` (PERL) -> Cumulative Risk: **500.98**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.55)
- **Magnitude:** 55.62 | **LOC:** 150 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Safety Score (91.9163%)
- **Heaviest Functions:** `setOptions` (I/O & Config Routines, Impact: 8.3), `usage` (I/O & Config Routines, Impact: 6.4)

### 6. `bin/prokka-clusters_to_hmm` (PERL) -> Cumulative Risk: **480.29**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.44)
- **Magnitude:** 40.02 | **LOC:** 111 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9897%), Safety Score (97.0688%)
- **Heaviest Functions:** `setOptions` (I/O & Config Routines, Impact: 8.1), `usage` (I/O & Config Routines, Impact: 6.4)

### 7. `bin/prokka-biocyc_to_fasta_db` (PERL) -> Cumulative Risk: **466.18**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.70)
- **Magnitude:** 49.0 | **LOC:** 118 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9946%), Safety Score (88.6667%)
- **Heaviest Functions:** `usage` (I/O & Config Routines, Impact: 6.4), `setOptions` (I/O & Config Routines, Impact: 6.2), `get_file` (Compute Cores, Impact: 5.7)

### 8. `bin/prokka-genbank_to_fasta_db` (PERL) -> Cumulative Risk: **464.29**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.74)
- **Magnitude:** 38.28 | **LOC:** 141 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (97.7914%), Safety Score (77.0571%)
- **Heaviest Functions:** `setOptions` (I/O & Config Routines, Impact: 10.3), `usage` (I/O & Config Routines, Impact: 6.4), `TAG` (Parameter Forwarders, Impact: 3.9)

### 9. `bin/prokka-genpept_to_fasta_db` (PERL) -> Cumulative Risk: **414.93**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.62)
- **Magnitude:** 25.62 | **LOC:** 96 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (73.8278%), State Flux (55.5508%)
- **Heaviest Functions:** `setOptions` (I/O & Config Routines, Impact: 7.3), `usage` (I/O & Config Routines, Impact: 6.4), `TAG` (Parameter Forwarders, Impact: 3.7)

### 10. `update-dbs/Makefile` (MAKEFILE) -> Cumulative Risk: **322.66**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.26)
- **Magnitude:** 22.74 | **LOC:** 71 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (73.1059%), Churn (38.9%)
- **Heaviest Functions:** `install` (I/O & Config Routines, Impact: 1.3), `all` (I/O & Config Routines, Impact: 1.1), `HAMAP.hmm.gz` (I/O & Config Routines, Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `bin/prokka` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 827.32 | **LOC:** 1834 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (81.7098%), Tech Debt (23.6646%)
**Top Internal Functions/Classes:**
  * `setOptions` **(I/O & Config Routines)** (Impact: 28.5)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `usage` **(Compute Cores)** (Impact: 28.2)
  * `cleanup_product` **(Compute Cores)** (Impact: 22.7)
    * *Intent:* #EXIT #----------------------------------------------------------------------
  * `setup_db` **(I/O & Config Routines)** (Impact: 16.9)
    * *Intent:* #----------------------------------------------------------------------
  * `check_tool` **(Compute Cores)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 184 instances
* *High Risk Execution (weighted view):* 15
* *Concurrency (weighted view):* 12
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 566
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 492`, `structural_boundaries: 347`, `args: 9`, `func_start: 26`
* *Risk/State:* `high_risk_execution: 16`, `state_mutation: 198`, `dead_code: 10`, `fragile_debt: 12`
* *Architecture:* `io: 20`, `api: 26`, `concurrency: 2`, `import: 32`
* *Defense:* `safety: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::Root::Version, Bio::SearchIO, Bio::Seq, Bio::SeqFeature::Generic, Bio::SeqIO, Bio::Tools::GFF, Bio::Tools::GuessSeqFormat, CDS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-hamap_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 66.9 | **LOC:** 160 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.7562%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` **(I/O & Config Routines)** (Impact: 8.4)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `usage` **(I/O & Config Routines)** (Impact: 6.4)
  * `get_file` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* #----------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 26`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 17`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 3`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, Data::Dumper, File::Temp, Getopt::Long, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/UniProt-to-sprot.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 55.64 | **LOC:** 150 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option...
  * `usage` **(I/O & Config Routines)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 23`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 13`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dumper, Getopt::Long, SWISS::Entry, SWISS::KW, SWISS::OC, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-uniprot_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 55.62 | **LOC:** 150 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option...
  * `usage` **(I/O & Config Routines)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 22`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 13`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dumper, Getopt::Long, SWISS::Entry, SWISS::KW, SWISS::OC, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-biocyc_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 49.0 | **LOC:** 118 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.2485%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` **(I/O & Config Routines)** (Impact: 6.4)
  * `setOptions` **(I/O & Config Routines)** (Impact: 6.2)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `get_file` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* #----------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 30`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 3`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, Data::Dumper, Getopt::Long, HTML::Entities, Text::Unidecode, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-cdd_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 48.38 | **LOC:** 136 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.1423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` **(I/O & Config Routines)** (Impact: 7.1)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `usage` **(I/O & Config Routines)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 25`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 11`, `dead_code: 2`
* *Architecture:* `io: 2`, `api: 2`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::AlignIO, Bio::SeqIO, Data::Dumper, File::Temp, Getopt::Long, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-clusters_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 40.02 | **LOC:** 111 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.095%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` **(I/O & Config Routines)** (Impact: 8.1)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `usage` **(I/O & Config Routines)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 4
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 22`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 8`
* *Architecture:* `io: 4`, `api: 2`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dumper, File::Temp, Getopt::Long, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-genbank_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 38.28 | **LOC:** 141 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.7476%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` **(I/O & Config Routines)** (Impact: 10.3)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `usage` **(I/O & Config Routines)** (Impact: 6.4)
  * `TAG` **(Parameter Forwarders)** (Impact: 3.9)
    * *Intent:* #----------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 30`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`, `dead_code: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, Bio::Tools::CodonTable, Data::Dumper, Getopt::Long, as, first, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-tigrfams_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 34.08 | **LOC:** 101 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.5211%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 5`
* *Risk/State:* `state_mutation: 6`, `dead_code: 2`
* *Architecture:* `io: 1`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CS, MAP, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-genpept_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 25.62 | **LOC:** 96 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.6373%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `usage` **(I/O & Config Routines)** (Impact: 6.4)
  * `TAG` **(Parameter Forwarders)** (Impact: 3.7)
    * *Intent:* #----------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 21`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `dead_code: 3`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, Getopt::Long, as, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 22.74 | **LOC:** 71 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (73.1059%)
**Top Internal Functions/Classes:**
  * `install` **(I/O & Config Routines)** (Impact: 1.3)
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `HAMAP.hmm.gz` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* # $(CP) sprot_m $(DIR_M)/sprot
  * `HAMAP.hmm` **(I/O & Config Routines)** (Impact: 1.1)
  * `hamap_rules.dat` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `func_start: 16`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `io: 16`, `api: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-make_tarball` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 21.98 | **LOC:** 48 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.1741%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__global_context__` **(Unclassified)** (Impact: 2.8)
  * `Anonymous_Block` **(Unclassified)** (Impact: 2.2)
  * `Anonymous_Block` **(Unclassified)** (Impact: 2.2)
  * `Anonymous_Block` **(Unclassified)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 19`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 4`
* *Architecture:* `io: 8`
* *Defense:* `test: 1`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-abricate_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 21.46 | **LOC:** 45 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.3647%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/AMRprot-to-AMR.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 18.44 | **LOC:** 40 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.2793%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-build_kingdom_dbs` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 16.28 | **LOC:** 42 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.8667%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 3.4)
  * `__global_context__` **(Unclassified)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 5`
* *Architecture:* `io: 8`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `environment.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.32 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 10.12 | **LOC:** 506 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CITATION.cff
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/ChangeLog.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 3.88 | **LOC:** 194 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `db/cm/__build/archaea.sql` (SQLITE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3.42 | **LOC:** 22 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SELECT_Statement` **(Unclassified)** (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `db/cm/__build/bacteria.sql` (SQLITE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3.42 | **LOC:** 22 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SELECT_Statement` **(Unclassified)** (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `db/cm/__build/viruses.sql` (SQLITE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3.42 | **LOC:** 22 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SELECT_Statement` **(Unclassified)** (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CODE_OF_CONDUCT.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.54 | **LOC:** 77 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/ToDoList.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bin/prokka` -> Churn: **67.44%** | Cog Load: 81.7098% | Debt: 23.6646%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `bin/prokka-hamap_to_hmm` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 66.9
- `update-dbs/UniProt-to-sprot.pl` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 55.64

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `bin/prokka` -> **Severity: 4347.8** (Blast Radius: 43.478 * Doc Risk: 100.0%)
- `bin/prokka-biocyc_to_fasta_db` -> **Severity: 4347.8** (Blast Radius: 43.478 * Doc Risk: 100.0%)
- `bin/prokka-cdd_to_hmm` -> **Severity: 4347.8** (Blast Radius: 43.478 * Doc Risk: 100.0%)
- `bin/prokka-clusters_to_hmm` -> **Severity: 4347.8** (Blast Radius: 43.478 * Doc Risk: 100.0%)
- `bin/prokka-genbank_to_fasta_db` -> **Severity: 4347.8** (Blast Radius: 43.478 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
