# ARCHITECTURAL_BRIEF: cics-java-jcics-samples
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cicsdev/cics-java-jcics-samples.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 76 analyzed artifact(s), 2087 LOC.
- **Load-bearing artifact:** `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` -- 15 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java` -- pulls in 16 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` at magnitude 70.38 (structural weight, not risk).
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
| Total Artifacts | 207 |
| Analyzed Artifacts (Scanned) | 76 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 131 |
| Total LOC | 2087 |
| Volatility Index | 0.013 |
| % Scanned of codebase = | 36.7% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.345 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2965 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0476 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 37 | 1892 | 48.7% |
| MARKDOWN | 18 | 0 | 23.7% |
| XML | 12 | 0 | 15.8% |
| PLAINTEXT | 6 | 0 | 7.9% |
| COBOL | 2 | 164 | 2.6% |
| JCL | 1 | 31 | 1.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `2.241`
> **Composition Archetype:** `Small Flat Repo` (z +2.24; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Large Core Modules 24%, Large Core Modules (2) 12%, Encapsulated Accessors Files 8%, Parameter Forwarders Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 52 | 68.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 24 | 31.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 131*

**Composition by Extension & Reason:**
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.program`: 27x Excluded (Unsupported Extension: '.program')
- `.transaction`: 27x Excluded (Unsupported Extension: '.transaction')
- `.prefs`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.osgibundle`: 6x Excluded (Unsupported Extension: '.osgibundle')
- `.mf`: 6x Excluded (Unsupported Extension: '.MF')
- `.properties`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jar`: 4x Excluded (Explicitly Denied Extension: '.jar')
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 61.4 | 5.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 69.8 | 26.1 | 22.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 77.4 | 23.5 | 27.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.7 | 2.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 58.4 | 5.1 | 3.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.0 | 11.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.0 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1 | 1 | 0 | `projects/com.ibm.cicsdev.terminal/src/com/ibm/cicsdev/terminal/TerminalExample1.java` |
| cleanup | 0 | 0 | 0 | - |
| guards | 288 | 27 | 14 | `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` |
| danger | 93 | 22 | 4 | `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` |
| concurrency | 12 | 1 | 0 | `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize/SerializeExample1.java` |
| connectivity | 125 | 38 | 5 | `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` |
| io | 1 | 1 | 0 | `etc/VSAM/DEFVSAM.jcl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 6 | 2 | 0 | `src/Cobol/EDUCHAN.cbl` |
| time | 6 | 3 | 0 | `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` |
| serialization | 2 | 1 | 0 | `src/Cobol/EDUCHAN.cbl` |
| regex | 0 | 0 | 0 | - |
| events | 2 | 1 | 0 | `etc/VSAM/DEFVSAM.jcl` |
| tests | 0 | 0 | 0 | - |
| docs | 186 | 37 | 8 | `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` |
| debt | 3 | 2 | 0 | `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkServEduchan.java` |
| mutation | 503 | 39 | 22 | `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` |
| dead_code | 43 | 33 | 1 | `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` |
| credential | 0 | 0 | 0 | - |
| threat | 15 | 2 | 0 | `src/Cobol/EDUCHAN.cbl` |
| ml_ai | 2 | 1 | 0 | `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `etc/VSAM/DEFVSAM.jcl` (Hits: 1)
- `MAINTAINERS.md` (Hits: 0)
- `README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **StockPartHelper.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java`) — 15 inbound connections
2. **VsamExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/VsamExampleCommon.java`) — 3 inbound connections
3. **blog.md** (`blog/blog.md`) — 1 inbound connections
4. **KsdsExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java`) — 1 inbound connections
5. **MAINTAINERS.md** (`MAINTAINERS.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **KsdsExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java`) — 16 outbound dependencies
2. **EsdsExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java`) — 13 outbound dependencies
3. **RrdsExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java`) — 13 outbound dependencies
4. **README.md** (`README.md`) — 12 outbound dependencies
5. **LinkProg3.java** (`projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg3.java`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` **(Defensive Guards)** (@ `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkServEduchan.java`) -> Impact: **19.8** | LOC: 57
  * *Intent:* /** * Main entry point to a CICS OSGi program. * * The fully qualified name of this class should be added to the * CICS-MainClass entry in the parent ...
- `main` **(I/O & Config Routines)** (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExample5.java`) -> Impact: **11.7** | LOC: 64
  * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the CICS-MainClass entry in * the parent OSGi bundle's...
- `main` **(Defensive Guards)** (@ `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg3.java`) -> Impact: **11.3** | LOC: 84
  * *Intent:* /** * Main entry point to a CICS OSGi program. * This can be called via a LINK or a 3270 attach. * * The fully qualified name of this class should be ...
- `deleteRecord` **(Defensive Guards)** (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java`) -> Impact: **10.9** | LOC: 76
  * *Intent:* /** * Provides a simple example of deleting a single record from a VSAM KSDS file. * * @param partId the key of the record to locate in the VSAM file....
- `deleteRecord` **(Defensive Guards)** (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java`) -> Impact: **10.7** | LOC: 73
  * *Intent:* /** * Provides a simple example of deleting a single record from a VSAM RRDS file. * * @param rrn the RRN of the record to locate in the VSAM file. * ...
- `main` **(Defensive Guards)** (@ `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize/SerializeExample1.java`) -> Impact: **10.4** | LOC: 67
  * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the CICS-MainClass entry in * the parent OSGi bundle's...
- `MAIN-PROCESSING` **(I/O & Config Routines)** (@ `src/Cobol/EDUCHAN.cbl`) -> Impact: **10.4** | LOC: 87
  * *Intent:* * -----------------------------------------------------------
- `main` **(I/O & Config Routines)** (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExample5.java`) -> Impact: **10.0** | LOC: 58
  * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the CICS-MainClass entry in * the parent OSGi bundle's...
- `browse` **(Defensive Guards)** (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java`) -> Impact: **9.7** | LOC: 56
  * *Intent:* /** * Provides an example of browsing a VSAM KSDS dataset. * * @param partIdStart the part ID from which the browse should begin. * @param count the m...
- `browse` **(Defensive Guards)** (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java`) -> Impact: **9.5** | LOC: 52
  * *Intent:* /** * Provides an example of browsing a VSAM ESDS dataset. * * @param rbaStart the RBA from which the browse should begin. * @param count the maximum ...

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq` | 5 | 125.82 | 9.88% | 23.49% |
| `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link` | 6 | 118.86 | 5.12% | 25.67% |
| `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds` | 6 | 109.02 | 1.79% | 42.82% |
| `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds` | 6 | 106.62 | 2.31% | 31.46% |
| `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq` | 4 | 98.7 | 9.49% | 21.74% |
| `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds` | 6 | 88.4 | 3.01% | 42.6% |
| `src/Cobol` | 2 | 49.88 | 53.28% | 52.61% |
| `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam` | 2 | 46.12 | 0.0% | 0.0% |
| `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize` | 1 | 29.12 | 12.82% | 23.43% |
| `projects/com.ibm.cicsdev.terminal/src/com/ibm/cicsdev/terminal` | 1 | 24.48 | 8.74% | 34.34% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Cobol/EC01.cbl` -> **77.4054%** Exposure
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` -> **68.1542%** Exposure
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java` -> **66.8188%** Exposure
- `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg1.java` -> **37.7541%** Exposure
- `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg2.java` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample3.java` -> **99.9932%** Exposure
- `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample3.java` -> **99.9914%** Exposure
- `src/Cobol/EDUCHAN.cbl` -> **99.0149%** Exposure
- `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample4.java` -> **97.7726%** Exposure
- `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg2.java` -> **97.3403%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` -> **6** Orphaned Functions | **0** Duplicates
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java` -> **4** Orphaned Functions | **0** Duplicates
- `src/Cobol/EC01.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg1.java` -> **1** Orphaned Functions | **0** Duplicates
- `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg2.java` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `229` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 70.38 | **LOC:** 389 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 10.91; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (68.2%), Mutation Surface (formerly State Flux) (44.4%), Guard Balance (formerly Safety Score) (20.1%), Connectivity (formerly Api Exposure) (5.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deleteRecord` **(Defensive Guards)** (Impact: 10.7)
    * *Intent:* /** * Provides a simple example of deleting a single record from a VSAM RRDS file. * * @param rrn th...
  * `browse` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* /** * Provides an example of browsing a VSAM RRDS dataset. * * @param rrnStart the RRN from which th...
  * `updateRecord` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* /** * Provides a simple example of updating a single record in a VSAM RRDS file. * * This method use...
  * `addRecord` **(Defensive Guards)** (Impact: 6.9)
    * *Intent:* /** * Provides a simple example of adding a record to a VSAM RRDS file. * * @param rrn the RRN of th...
  * `readRecord` **(Defensive Guards)** (Impact: 6.0)
    * *Intent:* /** * Provides a simple example of reading a single record from a VSAM RRDS file. * * @param rrn the...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 54`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 6`
* *Architecture:* `api: 8`, `import: 13`
* *Defense:* `safety: 28`, `doc: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.DuplicateRecordException, com.ibm.cics.server.EndOfFileException, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.RRDS, com.ibm.cics.server.RRDS_Browse, com.ibm.cics.server.RecordHolder, com.ibm.cics.server.RecordNotFoundException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 60.22 | **LOC:** 362 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 15.546; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (31.8%), Connectivity (formerly Api Exposure) (31.2%), Guard Balance (formerly Safety Score) (21.2%), Complexity Load (formerly Cognitive Load) (4.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deleteRecord` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* /** * Provides a simple example of deleting a single record from a VSAM KSDS file. * * @param partId...
  * `browse` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* /** * Provides an example of browsing a VSAM KSDS dataset. * * @param partIdStart the part ID from w...
  * `updateRecord` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* /** * Provides a simple example of updating a single record in a VSAM KSDS file. * * This method use...
  * `readRecord` **(Defensive Guards)** (Impact: 6.2)
    * *Intent:* /** * Provides a simple example of reading a single record from a VSAM KSDS file. * * @param partId ...
  * `addRecord` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* /** * Provides a simple example of adding a record to a VSAM KSDS file. * * @param sp the {@link Sto...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 53`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 7`, `import: 16`
* *Defense:* `safety: 24`, `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.546
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.013333
  * `Imports (Out-Degree: 2):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.DuplicateRecordException, com.ibm.cics.server.EndOfFileException, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.KSDS, com.ibm.cics.server.KeyHolder, com.ibm.cics.server.KeyedFileBrowse, com.ibm.cics.server.RecordHolder...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 45.9 | **LOC:** 269 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 10.91; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (66.8%), Mutation Surface (formerly State Flux) (38.2%), Guard Balance (formerly Safety Score) (23.4%), Connectivity (formerly Api Exposure) (5.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `browse` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* /** * Provides an example of browsing a VSAM ESDS dataset. * * @param rbaStart the RBA from which th...
  * `updateRecord` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* /** * Provides a simple example of updating a single record in a VSAM ESDS file. * * This method use...
  * `addRecord` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* /** * Provides a simple example of adding a record to a VSAM ESDS file. * * @param sp the {@link Sto...
  * `readRecord` **(Defensive Guards)** (Impact: 6.0)
    * *Intent:* /** * Provides a simple example of reading a single record from a VSAM ESDS file. * * @param rba the...
  * `EsdsExampleCommon` **(Interface Declarations)** (Impact: 1.3)
    * *Intent:* /** * Constructor to initialise the reference to the sample file. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 42`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 13`
* *Defense:* `safety: 17`, `doc: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.DuplicateRecordException, com.ibm.cics.server.ESDS, com.ibm.cics.server.ESDS_Browse, com.ibm.cics.server.EndOfFileException, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.RecordHolder, com.ibm.cics.server.RecordNotFoundException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 41.84 | **LOC:** 235 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **4**; blast radius 142.702; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Guard Balance (formerly Safety Score) (68.2%), Connectivity (formerly Api Exposure) (58.4%), Test Surface (formerly Verification) (2.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* /** * Generate a StockPart object which contains random, but valid data. * * @return A newly-created...
  * `generateDescription` **(I/O & Config Routines)** (Impact: 2.1)
    * *Intent:* /** * Generates a description for a random part using the arrays of constants * {@link #SIZE}, {@lin...
  * `getKey` **(Parameter Forwarders)** (Impact: 2.0)
    * *Intent:* /** * Extracts the key from the supplied {@link StockPart} instance as * a byte array, suitable for ...
  * `getKey` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* /** * Extracts the key from the supplied part ID, which represents a * {@link StockPart} instance, a...
  * `generateKey` **(Interface Declarations)** (Impact: 1.7)
    * *Intent:* /** * Generates a random key. * * @return a byte array representing a random key value */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `doc: 15`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 142.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.2
  * `Imports (Out-Degree: 0):` com.ibm.cicsdev.bean.StockPart, java.math.BigDecimal, java.util.Calendar, java.util.concurrent.ThreadLocalRandom
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample3.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 41.2 | **LOC:** 161 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.8%), Debt Markers (formerly Tech Debt) (25.5%), Complexity Load (formerly Cognitive Load) (23.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readFromQueue` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /** * Read of byte[] data from a TSQ. */
  * `writeToQueue` **(I/O & Config Routines)** (Impact: 3.7)
    * *Intent:* /** * Write of byte[] data to a TSQ. */
  * `main` **(I/O & Config Routines)** (Impact: 2.7)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the ...
  * `TSQExample3` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param tsq - the temporary storag...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 29`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.ItemHolder, com.ibm.cics.server.TSQ, com.ibm.cics.server.TSQType, com.ibm.cics.server.Task, com.ibm.cicsdev.bean.TsqRecord, java.text.MessageFormat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample3.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 39.96 | **LOC:** 153 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.8%), Debt Markers (formerly Tech Debt) (26.3%), Complexity Load (formerly Cognitive Load) (22.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readFromQueue` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /** * Read of byte[] data from a TDQ. */
  * `writeToQueue` **(I/O & Config Routines)** (Impact: 3.7)
    * *Intent:* /** * Write of byte[] data to the instance TDQ. */
  * `main` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* /** * Main entry point to this CICS Java program. */
  * `TDQExample3` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param tdq - the transient data q...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 28`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.DataHolder, com.ibm.cics.server.TDQ, com.ibm.cics.server.Task, com.ibm.cicsdev.bean.TdqRecord, java.text.MessageFormat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg3.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 37.9 | **LOC:** 216 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.1%), Guard Balance (formerly Safety Score) (62.5%), Debt Markers (formerly Tech Debt) (19.0%), Complexity Load (formerly Cognitive Load) (17.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 11.3)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * This can be called via a LINK or a 3270 attach. * *...
  * `buildChannel` **(Stateful Encapsulated Methods)** (Impact: 2.2)
    * *Intent:* /** * Build channel and populate with simple char container with string data. * * @return a Channel ...
  * `linkProg` **(Encapsulated Accessors)** (Impact: 1.9)
    * *Intent:* /** * LINK to the CICS program. * * @param chan - the channel to send to the target CICS program. */
  * `LinkProg3` **(Encapsulated Accessors)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param prog - the program referen...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 21`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 10`, `doc: 11`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CCSIDErrorException, com.ibm.cics.server.Channel, com.ibm.cics.server.ChannelErrorException, com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.CodePageErrorException, com.ibm.cics.server.Container, com.ibm.cics.server.ContainerErrorException, com.ibm.cics.server.InvalidRequestException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkServEduchan.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 35.94 | **LOC:** 184 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (40.1%), Mutation Surface (formerly State Flux) (28.2%), Debt Markers (formerly Tech Debt) (21.7%), Complexity Load (formerly Cognitive Load) (10.4%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 19.8)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * * The fully qualified name of this class should be ...
  * `buildRcContainer` **(Defensive Guards)** (Impact: 2.8)
    * *Intent:* /** * Build a BIT container from an int and put into a CICS container in the channel. * * @param rc ...
  * `ReturnCode` **(Encapsulated Accessors)** (Impact: 1.6)
  * `getNumVal` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 23`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `safety: 8`, `doc: 9`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CCSIDErrorException, com.ibm.cics.server.Channel, com.ibm.cics.server.ChannelErrorException, com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.CodePageErrorException, com.ibm.cics.server.Container, com.ibm.cics.server.ContainerErrorException, com.ibm.cics.server.InvalidRequestException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cobol/EDUCHAN.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 31.94 | **LOC:** 173 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Guard Balance (formerly Safety Score) (66.1%), Complexity Load (formerly Cognitive Load) (61.4%), Debt Markers (formerly Tech Debt) (27.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCESSING` **(I/O & Config Routines)** (Impact: 10.4)
    * *Intent:* * -----------------------------------------------------------
  * `ABEND-ROUTINE` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* * ----------------------------------------------------------- * Abnormal end * ---------------------...
  * `RESP-ERROR` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* * -----------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize/SerializeExample1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 29.12 | **LOC:** 181 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.9%), Guard Balance (formerly Safety Score) (31.5%), Debt Markers (formerly Tech Debt) (23.4%), Complexity Load (formerly Cognitive Load) (12.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 10.4)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the ...
  * `acquireLock` **(Stateful Encapsulated Methods)** (Impact: 2.4)
    * *Intent:* /** * Attempts to acquire the shared resource lock. This method calls the * {@link NameResource#enqu...
  * `randomSleep` **(Encapsulated Accessors)** (Impact: 1.6)
    * *Intent:* /** * Sleep this thread for a random interval. */
  * `doUpdate` **(Encapsulated Accessors)** (Impact: 1.2)
    * *Intent:* /** * Provides a dummy method to represent an update of some shared application * resource. * * @thr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 10`, `doc: 7`, `sync_locks: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.LengthErrorException, com.ibm.cics.server.NameResource, com.ibm.cics.server.ResourceUnavailableException, com.ibm.cics.server.Task, java.util.concurrent.ThreadLocalRandom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample2.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 28.14 | **LOC:** 162 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.1%), Guard Balance (formerly Safety Score) (37.9%), Debt Markers (formerly Tech Debt) (24.8%), Complexity Load (formerly Cognitive Load) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readFromQueue` **(I/O & Config Routines)** (Impact: 3.9)
    * *Intent:* /** * Simple read of string data from a TSQ. */
  * `writeToQueue` **(Defensive Guards)** (Impact: 3.5)
    * *Intent:* /** * Write of Java string data to a TSQ. */
  * `main` **(I/O & Config Routines)** (Impact: 2.7)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the ...
  * `TSQExample2` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param tsq - the temporary storag...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 21`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 8`, `doc: 8`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.ItemHolder, com.ibm.cics.server.TSQ, com.ibm.cics.server.TSQType, com.ibm.cics.server.Task, java.io.UnsupportedEncodingException, java.text.MessageFormat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample2.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 26.8 | **LOC:** 154 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.8%), Guard Balance (formerly Safety Score) (36.0%), Debt Markers (formerly Tech Debt) (25.5%), Complexity Load (formerly Cognitive Load) (7.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readFromQueue` **(Defensive Guards)** (Impact: 3.8)
    * *Intent:* /** * Simple read of string data from a TDQ. */
  * `writeToQueue` **(Defensive Guards)** (Impact: 3.5)
    * *Intent:* /** * Write some sample data to the instance TDQ. */
  * `main` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* /** * Main entry point to this CICS Java program. */
  * `TDQExample2` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param tdq - the transient data q...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 20`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 8`, `doc: 8`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.DataHolder, com.ibm.cics.server.TDQ, com.ibm.cics.server.Task, java.io.UnsupportedEncodingException, java.text.MessageFormat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 24.7 | **LOC:** 134 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.6%), Guard Balance (formerly Safety Score) (47.2%), Debt Markers (formerly Tech Debt) (33.6%), Complexity Load (formerly Cognitive Load) (8.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readFromQueue` **(I/O & Config Routines)** (Impact: 3.3)
    * *Intent:* /** * Simple read of string data from a TSQ. */
  * `writeToQueue` **(Defensive Guards)** (Impact: 3.0)
    * *Intent:* /** * Write of Java string data to a TSQ. */
  * `main` **(I/O & Config Routines)** (Impact: 2.7)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the ...
  * `TSQExample1` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param tsq - the temporary storag...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 17`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.ItemHolder, com.ibm.cics.server.TSQ, com.ibm.cics.server.TSQType, com.ibm.cics.server.Task, java.text.MessageFormat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.terminal/src/com/ibm/cicsdev/terminal/TerminalExample1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 24.48 | **LOC:** 127 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.5%), Guard Balance (formerly Safety Score) (62.3%), Debt Markers (formerly Tech Debt) (34.3%), Complexity Load (formerly Cognitive Load) (8.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 7.0)
    * *Intent:* /** * Main entry point to a CICS OSGi program. */
  * `getTerminalString` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /** * Verifies the current task is associated with a terminal and then * receives the input data. Th...
  * `parseTerminalString` **(Stateful Encapsulated Methods)** (Impact: 3.6)
    * *Intent:* /** * Breaks down the input string into * @param strTerm * @return */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 20`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.DataHolder, com.ibm.cics.server.EndOfChainIndicatorException, com.ibm.cics.server.Task, com.ibm.cics.server.TerminalPrincipalFacility, java.util.ArrayList, java.util.List, java.util.StringTokenizer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample4.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 23.7 | **LOC:** 130 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Guard Balance (formerly Safety Score) (46.0%), Debt Markers (formerly Tech Debt) (33.6%), Complexity Load (formerly Cognitive Load) (9.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateQueue` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* /** * Browses through a queue created by {@link TSQExample3} and updates each record. * * Each item ...
  * `main` **(I/O & Config Routines)** (Impact: 2.8)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the ...
  * `TSQExample4` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param tsq - the temporary storag...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 25`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.ItemErrorException, com.ibm.cics.server.ItemHolder, com.ibm.cics.server.TSQ, com.ibm.cics.server.TSQType, com.ibm.cics.server.Task, com.ibm.cicsdev.bean.TsqRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 23.36 | **LOC:** 126 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.4%), Guard Balance (formerly Safety Score) (45.1%), Debt Markers (formerly Tech Debt) (35.1%), Complexity Load (formerly Cognitive Load) (7.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readFromQueue` **(I/O & Config Routines)** (Impact: 3.2)
    * *Intent:* /** * Simple read of string data from a TDQ. */
  * `writeToQueue` **(Defensive Guards)** (Impact: 3.0)
    * *Intent:* /** * Write some sample data to the instance TDQ. */
  * `main` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* /** * Main entry point to this CICS Java program. */
  * `TDQExample1` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param tdq - the transient data q...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.DataHolder, com.ibm.cics.server.TDQ, com.ibm.cics.server.Task, java.text.MessageFormat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExample5.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 20.32 | **LOC:** 103 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.91; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.1%), Guard Balance (formerly Safety Score) (61.4%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (8.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 11.7)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.Task, com.ibm.cicsdev.bean.StockPart, com.ibm.cicsdev.vsam.StockPartHelper, java.util.List
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg2.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 19.56 | **LOC:** 128 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.3%), Guard Balance (formerly Safety Score) (56.0%), Debt Markers (formerly Tech Debt) (37.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 3.3)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * This can be called via a LINK or a 3270 attach. * *...
  * `linkProg` **(Stateful Encapsulated Methods)** (Impact: 2.0)
    * *Intent:* /** * Link to the CICS COBOL program and catch any errors from CICS. * * @param commarea - byte arra...
  * `buildCommarea` **(Encapsulated Accessors)** (Impact: 1.7)
    * *Intent:* /** * Build the commarea using the supplied JZOS wrapper * and set the input fields as required. * *...
  * `LinkProg2` **(Encapsulated Accessors)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param prog - the program referen...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 2`, `doc: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.Program, com.ibm.cics.server.Task, com.ibm.cicsdev.bean.JZOSCommareaWrapper, java.text.MessageFormat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExample5.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 18.64 | **LOC:** 97 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.91; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.1%), Guard Balance (formerly Safety Score) (61.4%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (8.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 10.0)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.Task, com.ibm.cicsdev.bean.StockPart, com.ibm.cicsdev.vsam.StockPartHelper, java.util.List
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cobol/EC01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 17.94 | **LOC:** 119 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (77.4%), Mutation Surface (formerly State Flux) (76.5%), Guard Balance (formerly Safety Score) (63.5%), Complexity Load (formerly Cognitive Load) (45.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A-CONTROL` **(I/O & Config Routines)** (Impact: 4.7)
    * *Intent:* ********************
  * `ZZX-CICS-ERROR-ROUTINE` **(I/O & Config Routines)** (Impact: 3.8)
    * *Intent:* ********************************
  * `ZZX-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExample5.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 14.1 | **LOC:** 95 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.91; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.1%), Mutation Surface (formerly State Flux) (40.1%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (5.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 8.5)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * * The FQ name of this class should be added to the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.Task, com.ibm.cicsdev.bean.StockPart, com.ibm.cicsdev.vsam.StockPartHelper, java.util.List
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 13.04 | **LOC:** 123 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 10.91; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (37.8%), Guard Balance (formerly Safety Score) (32.7%), Mutation Surface (formerly State Flux) (23.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* /** * Main entry point to a CICS OSGi program. * This can be called via a LINK or a 3270 attach. * *...
  * `linkProg` **(Stateful Encapsulated Methods)** (Impact: 2.2)
    * *Intent:* /** * Link to the CICS COBOL program catching any errors from CICS * The invoked CICS progra will re...
  * `LinkProg1` **(Encapsulated Accessors)** (Impact: 1.6)
    * *Intent:* /** * Constructor used to pass data to superclass constructor. * * @param prog - the program referen...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 17`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 5`, `doc: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.Program, com.ibm.cics.server.Task, java.io.UnsupportedEncodingException, java.text.MessageFormat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link.cicsbundle/META-INF/cics.xml` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link.resources.cicsbundle/META-INF/cics.xml` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.serialize.cicsbundle/META-INF/cics.xml` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java` -> **Severity: 0.006** (Bridge: 0.0002 * Flux: 31.8088%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` -> **Severity: 13.648** (Embedded: 0.2 * Error Risk: 68.2375%)
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java` -> **Severity: 0.283** (Embedded: 0.0133 * Error Risk: 21.197%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Cobol/EC01.cbl` -> **Severity: 1091.0** (Blast Radius: 10.91 * Doc Risk: 100.0%)
- `src/Cobol/EDUCHAN.cbl` -> **Severity: 1091.0** (Blast Radius: 10.91 * Doc Risk: 100.0%)
- `etc/VSAM/DEFVSAM.jcl` -> **Severity: 1043.542** (Blast Radius: 10.91 * Doc Risk: 95.65%)
- `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkServEduchan.java` -> **Severity: 467.571** (Blast Radius: 10.91 * Doc Risk: 42.8571%)

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
