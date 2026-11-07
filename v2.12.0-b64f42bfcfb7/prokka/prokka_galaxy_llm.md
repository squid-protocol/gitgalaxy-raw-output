# ARCHITECTURAL_BRIEF: prokka
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tseemann/prokka.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 77 analyzed artifact(s), 13584 LOC.
- **Load-bearing artifact:** `update-dbs/swissknife_1.81/lib/SWISS/TextFunc.pm` -- 43 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `bin/prokka` -- pulls in 30 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `update-dbs/swissknife_1.81/lib/SWISS/CCalt_prod.pm` at magnitude 1272.7 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 104 |
| Analyzed Artifacts (Scanned) | 77 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 27 |
| Total LOC | 13584 |
| Volatility Index | 0.013 |
| % Scanned of codebase = | 74.0% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2434 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4289 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2133 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 61 | 13295 | 79.2% |
| MARKDOWN | 3 | 0 | 3.9% |
| SHELL | 3 | 70 | 3.9% |
| PLAINTEXT | 3 | 0 | 3.9% |
| SQLITE | 3 | 63 | 3.9% |
| YAML | 2 | 61 | 2.6% |
| MAKEFILE | 1 | 47 | 1.3% |
| HTML | 1 | 48 | 1.3% |

## 4.1 SOURCE ENCODINGS
All 77 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 45%, Compute Cores Files 17%, Data / Markup / Trivial 12%, Declarative / Non-Code 12%, Parameter Forwarders Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 71 | 92.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 7.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 27*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 1x Excluded (File size exceeds 50MB limit without Intent Lock)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.fna`: 2x Excluded (Unsupported Extension: '.fna')
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.hamap`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pfam`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.prokka`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rfam`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.uniprot`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 90.4 | 54.7 | 62.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.9 | 59.4 | 63.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 72.9 | 11.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 29.7 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 49.9 | 8.0 | 9.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 20.9 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 86.8 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 45.3 | 2.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.7 | 0.5 | 0.6 | 0.6 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 67.4 | 15.8 | 17.4 | 17.4 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 83.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 449 | 50 | 15 | `update-dbs/swissknife_1.81/lib/SWISS/Entry.pm` |
| cleanup | 15 | 10 | 1 | `bin/prokka` |
| guards | 92 | 59 | 2 | `update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm` |
| danger | 125 | 20 | 5 | `bin/prokka` |
| concurrency | 5 | 3 | 0 | `bin/prokka` |
| connectivity | 700 | 61 | 17 | `update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm` |
| io | 109 | 21 | 2 | `update-dbs/swissknife_1.81/lib/SWISS/Stars/DR.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 27 | 7 | 0 | `bin/prokka` |
| time | 10 | 5 | 0 | `bin/prokka` |
| serialization | 0 | 0 | 0 | - |
| regex | 1118 | 63 | 38 | `bin/prokka` |
| events | 1 | 1 | 0 | `update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm` |
| tests | 4 | 4 | 0 | `update-dbs/swissknife_1.81/lib/SWISS/CCcatalytic_activity.pm` |
| docs | 56 | 50 | 1 | `update-dbs/swissknife_1.81/lib/SWISS/Stars/EV.pm` |
| debt | 171 | 33 | 5 | `bin/prokka` |
| mutation | 2142 | 65 | 59 | `bin/prokka` |
| dead_code | 74 | 38 | 3 | `update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm` |
| credential | 1 | 1 | 0 | `update-dbs/swissknife_1.81/lib/SWISS/FTs.pm` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 11 | 3 | 0 | `bin/prokka` |
| ui | 5 | 1 | 0 | `update-dbs/swissknife_1.81/lib/SWISS/Stars/DR.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `update-dbs/swissknife_1.81/lib/SWISS/Stars/DR.html` (Hits: 22)
- `bin/prokka` (Hits: 20)
- `update-dbs/Makefile` (Hits: 16)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TextFunc.pm** (`update-dbs/swissknife_1.81/lib/SWISS/TextFunc.pm`) — 43 inbound connections
2. **ListBase.pm** (`update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm`) — 24 inbound connections
3. **BaseClass.pm** (`update-dbs/swissknife_1.81/lib/SWISS/BaseClass.pm`) — 21 inbound connections
4. **CC.pm** (`update-dbs/swissknife_1.81/lib/SWISS/CC.pm`) — 3 inbound connections
5. **KW.pm** (`update-dbs/swissknife_1.81/lib/SWISS/KW.pm`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **prokka** (`bin/prokka`) — 30 outbound dependencies
2. **CCs.pm** (`update-dbs/swissknife_1.81/lib/SWISS/CCs.pm`) — 17 outbound dependencies
3. **prokka-genbank_to_fasta_db** (`bin/prokka-genbank_to_fasta_db`) — 8 outbound dependencies
4. **GNs.pm** (`update-dbs/swissknife_1.81/lib/SWISS/GNs.pm`) — 8 outbound dependencies
5. **ListBase.pm** (`update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `fromText` **(Many-Argument Workhorses)** (@ `update-dbs/swissknife_1.81/lib/SWISS/CCbpc_properties.pm`) -> Impact: **186.7** | LOC: 193
- `advancedParseNew` **(Many-Argument Workhorses)** (@ `update-dbs/swissknife_1.81/lib/SWISS/DEs.pm`) -> Impact: **150.9** | LOC: 140
- `_FTtoText` **(Many-Argument Workhorses)** (@ `update-dbs/swissknife_1.81/lib/SWISS/FTs.pm`) -> Impact: **146.1** | LOC: 81
- `toText` **(Many-Argument Workhorses)** (@ `update-dbs/swissknife_1.81/lib/SWISS/Stars.pm`) -> Impact: **136.5** | LOC: 209
- `toStringNew` **(Many-Argument Workhorses)** (@ `update-dbs/swissknife_1.81/lib/SWISS/DEs.pm`) -> Impact: **121.0** | LOC: 92
- `fromText` **(Many-Argument Workhorses)** (@ `update-dbs/swissknife_1.81/lib/SWISS/CCalt_prod.pm`) -> Impact: **115.4** | LOC: 195
- `fromText` **(Compute Cores)** (@ `update-dbs/swissknife_1.81/lib/SWISS/FTs.pm`) -> Impact: **97.7** | LOC: 84
- `wrapOn` **(Many-Argument Workhorses)** (@ `update-dbs/swissknife_1.81/lib/SWISS/TextFunc.pm`) -> Impact: **82.3** | LOC: 111
- `toString` **(Compute Cores)** (@ `update-dbs/swissknife_1.81/lib/SWISS/CCalt_prod.pm`) -> Impact: **80.0** | LOC: 328
- `toFasta` **(Compute Cores)** (@ `update-dbs/swissknife_1.81/lib/SWISS/Entry.pm`) -> Impact: **77.2** | LOC: 54

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `update-dbs/swissknife_1.81/lib/SWISS` | 45 | 10785.5 | 62.81% | 12.71% |
| `bin` | 12 | 1244.94 | 59.78% | 1.89% |
| `update-dbs/swissknife_1.81/lib/SWISS/Stars` | 5 | 304.6 | 42.73% | 29.19% |
| `update-dbs` | 3 | 96.82 | 32.45% | 12.58% |
| `db/cm/__build` | 7 | 50.12 | 3.43% | 0.0% |
| `__monolith__` | 3 | 26.98 | 0.0% | 0.0% |
| `.github/workflows` | 1 | 8.0 | 4.21% | 0.0% |
| `db/cm` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `update-dbs/swissknife_1.81/lib/SWISS/Stars/EV.pm` -> **72.8766%** Exposure
- `update-dbs/swissknife_1.81/lib/SWISS/CC.pm` -> **66.6298%** Exposure
- `update-dbs/swissknife_1.81/lib/SWISS/Refs.pm` -> **47.7425%** Exposure
- `update-dbs/swissknife_1.81/lib/SWISS/Ref.pm` -> **44.0608%** Exposure
- `update-dbs/swissknife_1.81/lib/SWISS/OSs.pm` -> **40.0808%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `update-dbs/swissknife_1.81/lib/SWISS/CC.pm` -> **100.0%** Exposure
- `update-dbs/swissknife_1.81/lib/SWISS/CCbpc_properties.pm` -> **100.0%** Exposure
- `update-dbs/swissknife_1.81/lib/SWISS/CCcatalytic_activity.pm` -> **100.0%** Exposure
- `update-dbs/swissknife_1.81/lib/SWISS/CCcofactor.pm` -> **100.0%** Exposure
- `update-dbs/swissknife_1.81/lib/SWISS/CCdisease.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm` -> **8** Orphaned Functions | **0** Duplicates
- `update-dbs/swissknife_1.81/lib/SWISS/Entry.pm` -> **3** Orphaned Functions | **0** Duplicates
- `update-dbs/swissknife_1.81/lib/SWISS/GNs.pm` -> **3** Orphaned Functions | **0** Duplicates
- `update-dbs/swissknife_1.81/lib/SWISS/OSs.pm` -> **3** Orphaned Functions | **0** Duplicates
- `update-dbs/swissknife_1.81/lib/SWISS/Ref.pm` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `398` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `update-dbs/swissknife_1.81/lib/SWISS/CCalt_prod.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.615)
- **Top Global Matches:** file_cluster_6: 8.615, file_cluster_8: 9.33, file_cluster_4: 16.373
- **Magnitude:** 1272.7 | **LOC:** 1709 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 8.19; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Many-Argument Workhorses)** (Impact: 115.4)
  * `toString` **(Compute Cores)** (Impact: 80.0)
  * `deleteEvidenceTags` **(Many-Argument Workhorses)** (Impact: 70.8)
  * `addEvidenceTag` **(Many-Argument Workhorses)** (Impact: 68.9)
  * `getEvidenceTagsString` **(Many-Argument Workhorses)** (Impact: 68.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 142 instances
* *State Mutation (weighted view):* 454
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 297`, `args: 33`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 170`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 37`, `import: 10`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.19
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 2):` Carp, Exporter, SWISS::BaseClass, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/DEs.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.257)
- **Top Global Matches:** file_cluster_8: 7.257, file_cluster_6: 12.663, file_cluster_4: 21.006
- **Magnitude:** 839.14 | **LOC:** 822 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.688; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `advancedParseNew` **(Many-Argument Workhorses)** (Impact: 150.9)
  * `toStringNew` **(Many-Argument Workhorses)** (Impact: 121.0)
  * `advancedParse` **(Compute Cores)** (Impact: 39.9)
  * `sort` **(Compute Cores)** (Impact: 34.2)
  * `to_old_format` **(Compute Cores)** (Impact: 33.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 307
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 208`, `args: 30`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 111`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 23`, `import: 8`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carp, Exporter, SWISS::DE, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/prokka` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.307)
- **Top Global Matches:** file_cluster_4: 7.307, file_cluster_15: 11.022, file_cluster_11: 11.71
- **Magnitude:** 827.32 | **LOC:** 1834 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 62.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 7.688; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 184 instances
* *High Risk Execution (weighted view):* 15
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 566
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 492`, `structural_boundaries: 347`, `args: 9`, `func_start: 26`
* *Risk/State:* `high_risk_execution: 16`, `state_mutation: 198`, `dead_code: 4`, `fragile_debt: 12`
* *Architecture:* `io: 20`, `api: 26`, `concurrency: 2`, `import: 32`
* *Defense:* `safety: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bio::Root::Version, Bio::SearchIO, Bio::Seq, Bio::SeqFeature::Generic, Bio::SeqIO, Bio::Tools::GFF, Bio::Tools::GuessSeqFormat, Cwd...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/swissknife_1.81/lib/SWISS/GNs.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.887)
- **Top Global Matches:** file_cluster_6: 5.887, file_cluster_4: 11.155, file_cluster_8: 14.232
- **Magnitude:** 730.8 | **LOC:** 990 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.688; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (71.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addAsNewGeneGroup` **(Many-Argument Workhorses)** (Impact: 70.0)
  * `addAsNewSynonym` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `delete` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `replaceGeneGroup` **(Many-Argument Workhorses)** (Impact: 30.7)
  * `text` **(Compute Cores)** (Impact: 29.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 193`, `args: 28`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 96`, `unreferenced_by_name: 3`
* *Architecture:* `api: 27`, `import: 9`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carp, Data::Dumper, Exporter, SWISS::GeneGroup, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/swissknife_1.81/lib/SWISS/FTs.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.353)
- **Top Global Matches:** file_cluster_3: 10.353, file_cluster_8: 30.413, file_cluster_1: 40.503
- **Magnitude:** 716.8 | **LOC:** 520 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 7.688; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_FTtoText` **(Many-Argument Workhorses)** (Impact: 146.1)
  * `fromText` **(Compute Cores)** (Impact: 97.7)
  * `sort` **(Compute Cores)** (Impact: 40.0)
    * *Intent:* #sorting based on annotation rule ANN027, #and additional instructions from Amos. #FTs should be sor...
  * `_wrapField` **(Many-Argument Workhorses)** (Impact: 39.7)
  * `_cleanDescription` **(Type Conversions)** (Impact: 31.4)
    * *Intent:* # remove wrongly inserted ' ' in description of CONFLICT, VARIANT, VAR_SEQ and VARSPLIC
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 286
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 88`, `args: 13`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 96`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 10`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Carp, Exporter, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/swissknife_1.81/lib/SWISS/TextFunc.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.324)
- **Top Global Matches:** file_cluster_6: 8.324, file_cluster_8: 9.479, file_cluster_4: 16.119
- **Magnitude:** 592.14 | **LOC:** 624 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **43** in-repo importer(s); it depends on **4**; blast radius 156.831; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrapOn` **(Many-Argument Workhorses)** (Impact: 82.3)
  * `toMixedCase` **(Compute Cores)** (Impact: 51.0)
  * `removeInternalComments` **(Compute Cores)** (Impact: 35.7)
    * *Intent:* # # Functions used to cleanup entries in annotators' jobs # #removes wild ** comments throughout an ...
  * `restoreInternalComments` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* #does the opposite... #returns an array with the internal comments that could not be restored at the...
  * `joinWith` **(Many-Argument Workhorses)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 101 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 307
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 127`, `args: 26`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 105`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 156.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.568206
  * `Imports (Out-Degree: 0):` Carp, Exporter, strict, vars
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/Entry.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.98)
- **Top Global Matches:** file_cluster_4: 5.98, file_cluster_15: 10.162, file_cluster_6: 11.174
- **Magnitude:** 458.52 | **LOC:** 755 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 14.223; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.8%), Guard Balance (formerly Safety Score) (62.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toFasta` **(Compute Cores)** (Impact: 77.2)
  * `isoFormSequence` **(Compute Cores)** (Impact: 33.6)
  * `AUTOLOAD` **(Compute Cores)** (Impact: 28.6)
  * `toFastaOld` **(Compute Cores)** (Impact: 15.9)
  * `isoIds` **(Compute Cores)** (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 46 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 211`, `args: 34`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `api: 30`, `import: 13`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.223
  * `Choke Point (Betweenness):` 0.000175 | `Ripple Effect (Closeness):` 0.026316
  * `Imports (Out-Degree: 1):` Carp, Exporter, SWISS::TextFunc, e, strict, vars
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.176)
- **Top Global Matches:** file_cluster_15: 6.176, file_cluster_11: 8.135, file_cluster_12: 8.288
- **Magnitude:** 454.12 | **LOC:** 858 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **8**; blast radius 74.296; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.1%), Guard Balance (formerly Safety Score) (61.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addEvidenceTag` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `deleteEvidenceTag` **(Defensive Guards)** (Impact: 19.1)
  * `del` **(Compute Cores)** (Impact: 18.7)
  * `get` **(Compute Cores)** (Impact: 17.4)
  * `setEvidenceTags` **(Defensive Guards)** (Impact: 14.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 208`, `args: 40`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 58`, `unreferenced_by_name: 8`
* *Architecture:* `api: 44`, `import: 11`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 74.296
  * `Choke Point (Betweenness):` 0.00309 | `Ripple Effect (Closeness):` 0.316296
  * `Imports (Out-Degree: 1):` Carp, Data::Dumper, Exporter, SWISS::BaseClass, del, get, strict, vars
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/Ref.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.847)
- **Top Global Matches:** file_cluster_6: 6.847, file_cluster_4: 12.382, file_cluster_8: 13.866
- **Magnitude:** 454.06 | **LOC:** 555 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 9.866; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.8%), Guard Balance (formerly Safety Score) (73.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `toText` **(Compute Cores)** (Impact: 66.9)
  * `pubtype` **(Compute Cores)** (Impact: 20.7)
  * `rc_sort` **(Compute Cores)** (Impact: 11.0)
  * `unpackRL` **(Compute Cores)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 69 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 120`, `args: 14`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 76`, `fragile_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 8`, `api: 16`, `import: 8`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.866
  * `Choke Point (Betweenness):` 0.000263 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 4):` Carp, Exporter, SWISS::BaseClass, SWISS::ListBase, SWISS::RCelement, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/Stars.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.923)
- **Top Global Matches:** file_cluster_6: 6.923, file_cluster_8: 12.488, file_cluster_4: 13.226
- **Magnitude:** 376.98 | **LOC:** 471 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.688; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.3%), Guard Balance (formerly Safety Score) (69.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toText` **(Many-Argument Workhorses)** (Impact: 136.5)
  * `AUTOLOAD` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `update` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* # Stars is a master object like entry. Therefore it has to update itself # and its subobjects. The t...
  * `fromText` **(Compute Cores)** (Impact: 7.8)
  * `insertLineGroup` **(Compute Cores)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 45 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 80`, `args: 14`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 50`, `unreferenced_by_name: 2`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carp, Exporter, SWISS::Stars::DR, SWISS::Stars::EV, SWISS::Stars::aa, SWISS::Stars::default, strict, vars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/swissknife_1.81/lib/SWISS/CCs.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.48)
- **Top Global Matches:** file_cluster_6: 7.48, file_cluster_4: 9.148, file_cluster_15: 15.73
- **Magnitude:** 352.24 | **LOC:** 519 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 7.688; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.1%), Guard Balance (formerly Safety Score) (71.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_sort_cmp` **(Compute Cores)** (Impact: 41.4)
  * `_chooseType` **(Compute Cores)** (Impact: 26.7)
  * `del` **(Compute Cores)** (Impact: 17.4)
  * `fromText` **(Compute Cores)** (Impact: 17.3)
  * `sort` **(Compute Cores)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 121`, `args: 18`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 17`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` Carp, Exporter, SWISS::CC, SWISS::CCalt_prod, SWISS::CCbpc_properties, SWISS::CCcatalytic_activity, SWISS::CCcofactor, SWISS::CCcopyright...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/swissknife_1.81/lib/SWISS/CCbpc_properties.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.069)
- **Top Global Matches:** file_cluster_4: 7.069, file_cluster_6: 8.954, file_cluster_15: 13.143
- **Magnitude:** 332.08 | **LOC:** 230 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 8.19; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Many-Argument Workhorses)** (Impact: 186.7)
  * `comment` **(Compute Cores)** (Impact: 16.6)
  * `sort` **(Compute Cores)** (Impact: 12.0)
  * `toString` **(Compute Cores)** (Impact: 7.7)
  * `properties` **(Compute Cores)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 77`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`, `unreferenced_by_name: 1`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.19
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 2):` Carp, SWISS::BaseClass, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/CCcatalytic_activity.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.931)
- **Top Global Matches:** file_cluster_4: 7.931, file_cluster_9: 10.67, file_cluster_15: 11.87
- **Magnitude:** 329.34 | **LOC:** 361 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 8.19; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Compute Cores)** (Impact: 55.2)
  * `activity_reaction` **(Compute Cores)** (Impact: 20.9)
  * `_activity_to_text` **(Compute Cores)** (Impact: 20.0)
  * `activity_rhea` **(Compute Cores)** (Impact: 16.7)
  * `activity_ec` **(Compute Cores)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 95`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 44`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 13`, `import: 7`
* *Defense:* `safety: 1`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.19
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 3):` Carp, SWISS::BaseClass, SWISS::CC, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/CC.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.181)
- **Top Global Matches:** file_cluster_6: 8.181, file_cluster_8: 10.448, file_cluster_4: 15.585
- **Magnitude:** 288.86 | **LOC:** 283 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 12.832; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.8%), Guard Balance (formerly Safety Score) (75.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toString` **(Many-Argument Workhorses)** (Impact: 57.9)
  * `fromText` **(Compute Cores)** (Impact: 37.1)
  * `blocks2String` **(Compute Cores)** (Impact: 29.1)
  * `parse2Blocks` **(Compute Cores)** (Impact: 9.1)
  * `wrap` **(Parameter Forwarders)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 68`, `args: 13`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 42`, `planned_debt: 3`, `fragile_debt: 3`
* *Architecture:* `api: 14`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.832
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.039474
  * `Imports (Out-Degree: 2):` Carp, Exporter, SWISS::BaseClass, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/DRs.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.622)
- **Top Global Matches:** file_cluster_6: 7.622, file_cluster_8: 12.779, file_cluster_4: 13.705
- **Magnitude:** 285.46 | **LOC:** 416 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.688; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%), Guard Balance (formerly Safety Score) (71.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toText` **(Compute Cores)** (Impact: 38.9)
  * `sort` **(Compute Cores)** (Impact: 38.8)
    * *Intent:* # EMBL DR lines must never be sorted. The sort order stems from EMBL # join statements and merges be...
  * `fromText` **(Compute Cores)** (Impact: 28.4)
  * `_dbIndex` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* # * Private methods/functions
  * `pids` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* # The EMBL protein identifiers introduced in 1999 are of the form # xxxxx.yy, e.g. CAA33128.1 # If $...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 90`, `args: 15`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`
* *Architecture:* `io: 1`, `api: 14`, `import: 7`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Carp, Data::Dumper, Exporter, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/swissknife_1.81/lib/SWISS/CCinteraction.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.543)
- **Top Global Matches:** file_cluster_8: 8.543, file_cluster_6: 18.07, file_cluster_3: 20.633
- **Magnitude:** 258.64 | **LOC:** 185 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 8.19; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.5%), Guard Balance (formerly Safety Score) (80.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Compute Cores)** (Impact: 51.1)
  * `sort` **(Compute Cores)** (Impact: 45.4)
  * `comment` **(Compute Cores)** (Impact: 19.3)
  * `toString` **(Compute Cores)** (Impact: 4.6)
  * `new` **(Type Conversions)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 52`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `dead_code: 3`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 2):` Carp, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/CCcofactor.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.497)
- **Top Global Matches:** file_cluster_6: 8.497, file_cluster_4: 10.367, file_cluster_9: 16.476
- **Magnitude:** 253.92 | **LOC:** 233 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 8.19; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Compute Cores)** (Impact: 57.2)
  * `toString` **(Compute Cores)** (Impact: 22.7)
  * `comment` **(Compute Cores)** (Impact: 21.7)
  * `structured_names` **(Compute Cores)** (Impact: 18.2)
  * `new` **(Type Conversions)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 60`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 40`, `dead_code: 2`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 3):` Carp, SWISS::CC, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/GeneGroup.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.009)
- **Top Global Matches:** file_cluster_15: 7.009, file_cluster_4: 8.304, file_cluster_16: 9.004
- **Magnitude:** 252.6 | **LOC:** 377 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 9.866; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%), Guard Balance (formerly Safety Score) (61.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Compute Cores)** (Impact: 55.3)
  * `toText` **(Compute Cores)** (Impact: 9.5)
  * `_fromText_old` **(Compute Cores)** (Impact: 9.3)
  * `Synonyms` **(Compute Cores)** (Impact: 7.8)
  * `shift` **(Compute Cores)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 118`, `args: 33`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 28`, `import: 7`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.866
  * `Choke Point (Betweenness):` 0.000175 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 3):` Carp, Exporter, SWISS::GN, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/BaseClass.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.492)
- **Top Global Matches:** file_cluster_12: 7.492, file_cluster_15: 7.582, file_cluster_16: 9.39
- **Magnitude:** 220.9 | **LOC:** 386 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **6**; blast radius 145.707; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.0%), Guard Balance (formerly Safety Score) (62.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addEvidenceTag` **(Compute Cores)** (Impact: 21.6)
  * `AUTOLOAD` **(Defensive Guards)** (Impact: 14.9)
    * *Intent:* # makes it appear that there are functions # of the same names as the member variables # which get a...
  * `_containsFields` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* # helper function for checkClashes # less said about this the better #
  * `deleteEvidenceTag` **(Compute Cores)** (Impact: 12.7)
  * `setEvidenceTags` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* # Evidence tag handling
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 161`, `args: 27`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 31`, `unreferenced_by_name: 2`
* *Architecture:* `api: 25`, `import: 14`
* *Defense:* `safety: 6`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 145.707
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.386696
  * `Imports (Out-Degree: 0):` Carp, Data::Dumper, Exporter, strict, the, vars
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/CCdisease.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.891)
- **Top Global Matches:** file_cluster_4: 6.891, file_cluster_15: 10.852, file_cluster_6: 11.019
- **Magnitude:** 195.48 | **LOC:** 266 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 8.19; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.1%), Guard Balance (formerly Safety Score) (70.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Compute Cores)** (Impact: 36.6)
  * `comment` **(Compute Cores)** (Impact: 16.6)
  * `disease` **(Compute Cores)** (Impact: 8.5)
  * `_parse_txt_ev` **(Compute Cores)** (Impact: 6.3)
  * `toString` **(Compute Cores)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 70`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 1`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.19
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 2):` Carp, SWISS::BaseClass, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/CCsubcell_location.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.338)
- **Top Global Matches:** file_cluster_4: 7.338, file_cluster_6: 9.258, file_cluster_15: 12.856
- **Magnitude:** 189.42 | **LOC:** 250 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 8.19; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.9%), Guard Balance (formerly Safety Score) (69.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Compute Cores)** (Impact: 34.7)
  * `comment` **(Compute Cores)** (Impact: 24.2)
  * `toString` **(Compute Cores)** (Impact: 10.6)
  * `note` **(Compute Cores)** (Impact: 8.5)
  * `_parse_txt_ev` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 66`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `planned_debt: 2`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 1`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.19
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 2):` Carp, SWISS::BaseClass, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/OSs.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.402)
- **Top Global Matches:** file_cluster_6: 7.402, file_cluster_4: 11.2, file_cluster_8: 15.695
- **Magnitude:** 185.46 | **LOC:** 219 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.688; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Complexity Load (formerly Cognitive Load) (71.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scientific2rc` **(Compute Cores)** (Impact: 39.0)
    * *Intent:* # convert scientific name to the abbreviated form as it is used # in the RC SPECIES line # $superreg...
  * `fromText` **(Compute Cores)** (Impact: 13.5)
  * `toText` **(Compute Cores)** (Impact: 10.7)
  * `new` **(Type Conversions)** (Impact: 3.2)
  * `initialize` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 46`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 35`, `unreferenced_by_name: 3`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carp, Exporter, SWISS::ListBase, SWISS::OS, SWISS::TextFunc, input, strict, vars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/swissknife_1.81/lib/SWISS/CCseq_caution.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.17)
- **Top Global Matches:** file_cluster_6: 8.17, file_cluster_4: 9.603, file_cluster_15: 16.052
- **Magnitude:** 176.88 | **LOC:** 176 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 8.19; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Compute Cores)** (Impact: 64.2)
  * `comment` **(Compute Cores)** (Impact: 9.2)
  * `toString` **(Compute Cores)** (Impact: 7.7)
  * `sort` **(Compute Cores)** (Impact: 6.3)
  * `new` **(Type Conversions)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 43`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.19
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 3):` Carp, SWISS::BaseClass, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `update-dbs/swissknife_1.81/lib/SWISS/IDs.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.81)
- **Top Global Matches:** file_cluster_15: 6.81, file_cluster_11: 8.057, file_cluster_9: 8.332
- **Magnitude:** 149.38 | **LOC:** 196 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 7.688; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (66.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromText` **(Compute Cores)** (Impact: 17.7)
  * `toText` **(Compute Cores)** (Impact: 17.0)
  * `new` **(Type Conversions)** (Impact: 3.2)
  * `initialize` **(Parameter Forwarders)** (Impact: 1.8)
  * `sort` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* # IDs must never be sorted, overwrite the inherited sort method.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 37`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `unreferenced_by_name: 1`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Carp, Exporter, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-dbs/swissknife_1.81/lib/SWISS/Stars/EV.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.298)
- **Top Global Matches:** file_cluster_15: 6.298, file_cluster_13: 8.349, file_cluster_16: 8.483
- **Magnitude:** 131.74 | **LOC:** 262 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 9.866; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (72.9%), Guard Balance (formerly Safety Score) (62.9%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_addEvidence` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* # if $update is set, the evidence date will be updated if the entry already # exists.
  * `sort` **(Compute Cores)** (Impact: 8.2)
  * `fromText` **(Compute Cores)** (Impact: 6.6)
  * `max` **(Parameter Forwarders)** (Impact: 5.6)
  * `addEvidence` **(Parameter Forwarders)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 50`, `args: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 2`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.866
  * `Choke Point (Betweenness):` 0.000175 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 2):` Carp, Exporter, SWISS::ListBase, SWISS::TextFunc, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `update-dbs/swissknife_1.81/lib/SWISS/OGs.pm` (PERL) | Magnitude: 120.16 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 39, state_mutation: 25, branch: 17
- `update-dbs/swissknife_1.81/lib/SWISS/OCs.pm` (PERL) | Magnitude: 66.86 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 30, state_mutation: 14, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `update-dbs/swissknife_1.81/lib/SWISS/BaseClass.pm` (PERL) | Magnitude: 220.9 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 161, indent_spaces: 132, branch: 63, state_mutation: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `update-dbs/swissknife_1.81/lib/SWISS/CCcopyright.pm` (PERL) | Magnitude: 32.04 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 31, indent_spaces: 24, api: 10, state_mutation: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bin/prokka` -> Churn: **67.44%** | Cog Load: 81.7098% | Debt: 22.7179%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `update-dbs/swissknife_1.81/lib/SWISS/CCalt_prod.pm` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 1272.7
- `update-dbs/swissknife_1.81/lib/SWISS/DEs.pm` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 839.14
- `update-dbs/swissknife_1.81/lib/SWISS/GNs.pm` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 730.8
- `update-dbs/swissknife_1.81/lib/SWISS/FTs.pm` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 716.8
- `update-dbs/swissknife_1.81/lib/SWISS/TextFunc.pm` -> **Torsten Seemann** (100.0% isolated ownership) | Magnitude: 592.14

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm` -> **Severity: 0.309** (Bridge: 0.0031 * Flux: 99.9696%)
- `update-dbs/swissknife_1.81/lib/SWISS/KW.pm` -> **Severity: 0.061** (Bridge: 0.0006 * Flux: 99.8979%)
- `update-dbs/swissknife_1.81/lib/SWISS/Ref.pm` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 100.0%)
- `update-dbs/swissknife_1.81/lib/SWISS/Entry.pm` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 99.9791%)
- `update-dbs/swissknife_1.81/lib/SWISS/GeneGroup.pm` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 99.9624%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `update-dbs/swissknife_1.81/lib/SWISS/TextFunc.pm` -> **Severity: 44.44** (Embedded: 0.5682 * Error Risk: 78.2107%)
- `update-dbs/swissknife_1.81/lib/SWISS/BaseClass.pm` -> **Severity: 24.232** (Embedded: 0.3867 * Error Risk: 62.6655%)
- `update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm` -> **Severity: 19.33** (Embedded: 0.3163 * Error Risk: 61.1127%)
- `update-dbs/swissknife_1.81/lib/SWISS/CC.pm` -> **Severity: 2.986** (Embedded: 0.0395 * Error Risk: 75.6335%)
- `update-dbs/swissknife_1.81/lib/SWISS/KW.pm` -> **Severity: 2.252** (Embedded: 0.0395 * Error Risk: 57.0578%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `update-dbs/swissknife_1.81/lib/SWISS/TextFunc.pm` -> **Severity: 15683.1** (Blast Radius: 156.831 * Doc Risk: 100.0%)
- `update-dbs/swissknife_1.81/lib/SWISS/BaseClass.pm` -> **Severity: 14570.7** (Blast Radius: 145.707 * Doc Risk: 100.0%)
- `update-dbs/swissknife_1.81/lib/SWISS/ListBase.pm` -> **Severity: 7429.6** (Blast Radius: 74.296 * Doc Risk: 100.0%)
- `update-dbs/swissknife_1.81/lib/SWISS/KW.pm` -> **Severity: 1640.1** (Blast Radius: 16.401 * Doc Risk: 100.0%)
- `update-dbs/swissknife_1.81/lib/SWISS/Entry.pm` -> **Severity: 1422.3** (Blast Radius: 14.223 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 134 literal sites + 2 sites through wrappers = 136
- **`panics_and_aborts`:** 68 literal sites + 7 sites through wrappers = 75

- `err` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `bin/prokka`
- `version` (function, debug_prints, primitive): 2 call sites in 1 files -- `bin/prokka`
- `version` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `bin/prokka`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1783 call pairs -- scoped 11.9%, unique 0.0%, ambiguous 0.1%, external 88.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 1754 | 12.1% | 0.0% | 0.1% | 87.8% |
| shell | 29 | 0.0% | 0.0% | 0.0% | 100.0% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
