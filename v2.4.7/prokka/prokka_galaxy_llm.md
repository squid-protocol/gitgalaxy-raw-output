# ARCHITECTURAL_BRIEF: prokka
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/prokka` |
| **Timestamp** | `2026-08-07T03:52:26.540135+00:00` |
| **Scan Duration** | `1.15s` |
| **Git Branch** | `master` |
| **Git Commit** | `045d3c5f8a1a54a873d76eb4b6c8f85d4fb82944` |
| **Git Remote** | `https://github.com/tseemann/prokka.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3 malicious artifacts.

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
| Cognitive Load Exposure | 5.0 | 97.3 | 77.6 | 88.2 | 81.8 |
| Error & Exception Exposure | 0.0 | 99.2 | 89.1 | 96.8 | 98.2 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Testing Exposure | 2.3 | 80.0 | 7.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 7.5 | 0.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 28.3 | 1.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 87.5 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 45.3 | 8.5 | 3.8 | 0.0 |
| Specification Exposure | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.6 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 80.8 | 13.7 | 0.0 | 0.0 |
| Documentation Exposure | 11.9 | 100.0 | 34.0 | 26.0 | 18.1 |
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

- `kingdoms` (@ `bin/prokka`) -> Impact: **167.0** | LOC: 220
  * *Intent:* #----------------------------------------------------------------------
- `genera` (@ `bin/prokka`) -> Impact: **164.8** | LOC: 216
- `hmms` (@ `bin/prokka`) -> Impact: **162.6** | LOC: 212
- `cms` (@ `bin/prokka`) -> Impact: **162.4** | LOC: 208
- `setup_db` (@ `bin/prokka`) -> Impact: **55.1** | LOC: 63
  * *Intent:* #----------------------------------------------------------------------
- `usage` (@ `bin/prokka`) -> Impact: **39.4** | LOC: 27
- `setOptions` (@ `bin/prokka`) -> Impact: **28.5** | LOC: 70
  * *Intent:* #---------------------------------------------------------------------- # Option setting routines
- `cleanup_product` (@ `bin/prokka`) -> Impact: **22.7** | LOC: 30
  * *Intent:* #EXIT #----------------------------------------------------------------------
- `setOptions` (@ `bin/prokka-uniprot_to_fasta_db`) -> Impact: **13.8** | LOC: 36
  * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option setting routines
- `setOptions` (@ `update-dbs/UniProt-to-sprot.pl`) -> Impact: **13.8** | LOC: 36
  * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option setting routines

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `bin` | 12 | 4901.06 | 87.92% | 18.69% |
| `update-dbs` | 3 | 130.12 | 58.7% | 0.0% |
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

1. **`bin/prokka-make_tarball`** -> AI Confidence: **99.06%**
2. **`bin/prokka-build_kingdom_dbs`** -> AI Confidence: **98.86%**
3. **`update-dbs/Makefile`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `93` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `bin/prokka` (PERL) -> Cumulative Risk: **619.55**
- **Archetype:** `file_cluster_0` (Distance: 13.951 IQR)
- **Magnitude:** 2052.82 | **LOC:** 1834 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.2377%), Cognitive Load (81.7522%)
- **Heaviest Functions:** `kingdoms` (Impact: 167.0), `genera` (Impact: 164.8), `hmms` (Impact: 162.6)

### 2. `bin/prokka-build_kingdom_dbs` (SHELL) -> Cumulative Risk: **552.22**
- **Archetype:** `file_cluster_8` (Distance: 11.813 IQR)
- **Magnitude:** 17.18 | **LOC:** 42 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9912%), Safety Score (98.4539%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 4.3), `__global_context__` (Impact: 1.5)

### 3. `bin/prokka-make_tarball` (SHELL) -> Cumulative Risk: **537.96**
- **Archetype:** `file_cluster_8` (Distance: 10.884 IQR)
- **Magnitude:** 29.08 | **LOC:** 48 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9994%), Safety Score (99.1563%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 5.2), `Anonymous_Block` (Impact: 5.2), `Anonymous_Block` (Impact: 3.2)

### 4. `update-dbs/AMRprot-to-AMR.pl` (PERL) -> Cumulative Risk: **459.25**
- **Archetype:** `file_cluster_8` (Distance: 11.085 IQR)
- **Magnitude:** 24.44 | **LOC:** 40 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (86.5796%), Cognitive Load (81.0697%)

### 5. `bin/prokka-genpept_to_fasta_db` (PERL) -> Cumulative Risk: **456.76**
- **Archetype:** `file_cluster_0` (Distance: 16.265 IQR)
- **Magnitude:** 52.62 | **LOC:** 96 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.7679%), Cognitive Load (88.4197%)
- **Heaviest Functions:** `setOptions` (Impact: 7.3), `usage` (Impact: 6.4), `TAG` (Impact: 3.7)

### 6. `update-dbs/UniProt-to-sprot.pl` (PERL) -> Cumulative Risk: **453.9**
- **Archetype:** `file_cluster_0` (Distance: 14.121 IQR)
- **Magnitude:** 85.74 | **LOC:** 150 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.3086%), Cognitive Load (90.0804%)
- **Heaviest Functions:** `setOptions` (Impact: 13.8)

### 7. `bin/prokka-genbank_to_fasta_db` (PERL) -> Cumulative Risk: **445.89**
- **Archetype:** `file_cluster_17` (Distance: 13.245 IQR)
- **Magnitude:** 686.65 | **LOC:** 141 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.6514%), Cognitive Load (89.9391%)

### 8. `bin/prokka-hamap_to_hmm` (PERL) -> Cumulative Risk: **440.82**
- **Archetype:** `file_cluster_17` (Distance: 12.936 IQR)
- **Magnitude:** 705.09 | **LOC:** 160 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.5747%), Cognitive Load (81.255%)

### 9. `bin/prokka-abricate_to_fasta_db` (PERL) -> Cumulative Risk: **430.61**
- **Archetype:** `file_cluster_13` (Distance: 12.85 IQR)
- **Magnitude:** 42.46 | **LOC:** 45 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.961%), Cognitive Load (87.1361%)

### 10. `bin/prokka-tigrfams_to_hmm` (PERL) -> Cumulative Risk: **430.14**
- **Archetype:** `file_cluster_13` (Distance: 15.757 IQR)
- **Magnitude:** 67.08 | **LOC:** 101 | **CtrlFlow:** 81.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.1108%), Cognitive Load (88.0797%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `bin/prokka` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.951 IQR)
- **Top Global Matches:** file_cluster_0: 13.951, file_cluster_17: 14.083, file_cluster_13: 14.14
- **Magnitude:** 2052.82 | **LOC:** 1834 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (81.7522%), Tech Debt (24.3107%)
**Top Internal Functions/Classes:**
  * `kingdoms` (Impact: 167.0)
    * *Intent:* #----------------------------------------------------------------------
  * `genera` (Impact: 164.8)
  * `hmms` (Impact: 162.6)
  * `cms` (Impact: 162.4)
  * `setup_db` (Impact: 55.1)
    * *Intent:* #----------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 488`, `structural_boundaries: 347`, `args: 10`, `func_start: 26`
* *Risk/State:* `high_risk_execution: 16`, `state_mutation: 1147`, `dead_code: 10`, `fragile_debt: 12`
* *Architecture:* `io: 23`, `api: 1`, `concurrency: 12`, `import: 32`
* *Defense:* `safety: 4`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::SeqIO, CDS, Bio::Tools::GFF, that, suitable, this, Bio::Seq, File::Copy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-hamap_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.936 IQR)
- **Top Global Matches:** file_cluster_17: 12.936, file_cluster_0: 13.09, file_cluster_13: 13.117
- **Magnitude:** 705.09 | **LOC:** 160 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.255%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 26`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 77`, `dead_code: 1`
* *Architecture:* `io: 1`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, File::Temp, Bio::SeqIO, strict, warnings, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-genbank_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.245 IQR)
- **Top Global Matches:** file_cluster_17: 13.245, file_cluster_0: 13.253, file_cluster_13: 13.308
- **Magnitude:** 686.65 | **LOC:** 141 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.9391%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 30`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 49`, `dead_code: 1`
* *Architecture:* `import: 8`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, as, Bio::SeqIO, strict, warnings, first, Bio::Tools::CodonTable, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-cdd_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.443 IQR)
- **Top Global Matches:** file_cluster_0: 14.443, file_cluster_13: 14.658, file_cluster_17: 14.723
- **Magnitude:** 574.88 | **LOC:** 136 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.9447%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 25`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 76`, `dead_code: 2`
* *Architecture:* `io: 2`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, File::Temp, Bio::SeqIO, strict, warnings, Bio::AlignIO, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-biocyc_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.547 IQR)
- **Top Global Matches:** file_cluster_17: 12.547, file_cluster_13: 12.554, file_cluster_0: 12.592
- **Magnitude:** 519.46 | **LOC:** 118 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.2018%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 30`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 51`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, Text::Unidecode, Bio::SeqIO, strict, HTML::Entities, warnings, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/UniProt-to-sprot.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.121 IQR)
- **Top Global Matches:** file_cluster_0: 14.121, file_cluster_13: 14.192, file_cluster_17: 14.219
- **Magnitude:** 85.74 | **LOC:** 150 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (90.0804%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` (Impact: 13.8)
    * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 23`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 70`, `dead_code: 2`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, SWISS::Entry, strict, SWISS::KW, warnings, lib, SWISS::OC, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-uniprot_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.125 IQR)
- **Top Global Matches:** file_cluster_0: 14.125, file_cluster_17: 14.225, file_cluster_13: 14.231
- **Magnitude:** 85.72 | **LOC:** 150 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.0995%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` (Impact: 13.8)
    * *Intent:* #print STDERR "\n"; #---------------------------------------------------------------------- # Option...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 22`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 70`, `dead_code: 2`
* *Architecture:* `io: 1`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, SWISS::Entry, strict, SWISS::KW, warnings, SWISS::OC, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-clusters_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.643 IQR)
- **Top Global Matches:** file_cluster_0: 12.643, file_cluster_13: 12.854, file_cluster_17: 13.08
- **Magnitude:** 68.02 | **LOC:** 111 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.1414%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` (Impact: 8.1)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `usage` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 22`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 52`
* *Architecture:* `io: 4`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, File::Temp, strict, warnings, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-tigrfams_to_hmm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.757 IQR)
- **Top Global Matches:** file_cluster_13: 15.757, file_cluster_0: 15.836, file_cluster_17: 15.945
- **Magnitude:** 67.08 | **LOC:** 101 | **CtrlFlow:** 81.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 5`
* *Risk/State:* `state_mutation: 51`, `dead_code: 2`
* *Architecture:* `io: 1`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MAP, CS, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-genpept_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.265 IQR)
- **Top Global Matches:** file_cluster_0: 16.265, file_cluster_17: 16.369, file_cluster_13: 16.475
- **Magnitude:** 52.62 | **LOC:** 96 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.4197%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setOptions` (Impact: 7.3)
    * *Intent:* #---------------------------------------------------------------------- # Option setting routines
  * `usage` (Impact: 6.4)
  * `TAG` (Impact: 3.7)
    * *Intent:* #----------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 21`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 34`, `dead_code: 3`
* *Architecture:* `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, as, Bio::SeqIO, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-abricate_to_fasta_db` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.85 IQR)
- **Top Global Matches:** file_cluster_13: 12.85, file_cluster_0: 12.861, file_cluster_8: 13.023
- **Magnitude:** 42.46 | **LOC:** 45 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.1361%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dumper, Bio::SeqIO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka-make_tarball` (SHELL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.884 IQR)
- **Top Global Matches:** file_cluster_8: 10.884, file_cluster_13: 11.432, file_cluster_0: 11.437
- **Magnitude:** 29.08 | **LOC:** 48 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.8117%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 5.2)
  * `Anonymous_Block` (Impact: 5.2)
  * `Anonymous_Block` (Impact: 3.2)
  * `__global_context__` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 9`
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
- **Risk Profile:** Cognitive Load (4.956%), Tech Debt (0.0%)
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
- **Risk Profile:** Cognitive Load (97.2852%), Tech Debt (99.9912%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 4.3)
  * `__global_context__` (Impact: 1.5)
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
- `update-dbs/UniProt-to-sprot.pl` (PERL) | Magnitude: 85.74 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 70, branch: 51, structural_boundaries: 23
- `bin/prokka-uniprot_to_fasta_db` (PERL) | Magnitude: 85.72 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 70, branch: 51, structural_boundaries: 22
- `bin/prokka-genpept_to_fasta_db` (PERL) | Magnitude: 52.62 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 34, branch: 26, structural_boundaries: 21
- `bin/prokka` (PERL) | Magnitude: 2052.82 | Delta: **0.132 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 1147, indent_spaces: 1054, branch: 488, structural_boundaries: 347
- `bin/prokka-clusters_to_hmm` (PERL) | Magnitude: 68.02 | Delta: **0.211 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 52, branch: 35, indent_spaces: 35, structural_boundaries: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `bin/prokka-abricate_to_fasta_db` (PERL) | Magnitude: 42.46 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 27, indent_spaces: 14, structural_boundaries: 10, encapsulation: 7
- `bin/prokka-tigrfams_to_hmm` (PERL) | Magnitude: 67.08 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 51, branch: 22, regex_execution: 21, indent_spaces: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `bin/prokka-biocyc_to_fasta_db` (PERL) | Magnitude: 519.46 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 51, indent_spaces: 50, structural_boundaries: 30, branch: 29
- `bin/prokka-genbank_to_fasta_db` (PERL) | Magnitude: 686.65 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 62, state_mutation: 49, branch: 41, structural_boundaries: 30
- `bin/prokka-hamap_to_hmm` (PERL) | Magnitude: 705.09 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 78, state_mutation: 77, branch: 39, structural_boundaries: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `update-dbs/AMRprot-to-AMR.pl` (PERL) | Magnitude: 24.44 | Delta: **0.2 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 9, bitwise_ops: 5, regex_execution: 4
- `bin/prokka-build_kingdom_dbs` (SHELL) | Magnitude: 17.18 | Delta: **0.308 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 11, indent_spaces: 10, io: 8, structural_boundaries: 5
- `bin/prokka-make_tarball` (SHELL) | Magnitude: 29.08 | Delta: **0.548 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: debug_prints: 13, safety_bypasses: 12, state_mutation: 12, branch: 10

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bin/prokka` -> Churn: **80.85%** | Cog Load: 81.7522% | Debt: 24.3107%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `bin/prokka-hamap_to_hmm` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 705.09
- `bin/prokka-genbank_to_fasta_db` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 686.65
- `update-dbs/UniProt-to-sprot.pl` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 85.74

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `update-dbs/Makefile` -> **Severity: 5000.0** (Blast Radius: 50.0 * Doc Risk: 100.0%)
- `update-dbs/AMRprot-to-AMR.pl` -> **Severity: 3230.155** (Blast Radius: 50.0 * Doc Risk: 64.6031%)
- `bin/prokka-build_kingdom_dbs` -> **Severity: 2697.025** (Blast Radius: 50.0 * Doc Risk: 53.9405%)
- `bin/prokka-make_tarball` -> **Severity: 2315.155** (Blast Radius: 50.0 * Doc Risk: 46.3031%)
- `bin/prokka-abricate_to_fasta_db` -> **Severity: 2160.825** (Blast Radius: 50.0 * Doc Risk: 43.2165%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
