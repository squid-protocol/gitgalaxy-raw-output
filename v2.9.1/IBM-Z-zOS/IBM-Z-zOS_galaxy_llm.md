# ARCHITECTURAL_BRIEF: IBM-Z-zOS
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/IBM/IBM-Z-zOS.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 412 analyzed artifact(s), 39838 LOC.
- **Load-bearing artifact:** `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/SmfPrintStream.java` -- 57 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `zOS-WLM/WLM Documents.md` -- pulls in 33 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `zOS-Tools-and-Toys/wjsfsmon/wjsfsmon.rexx` at magnitude 2663.96 (structural weight, not risk).
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
| Total Artifacts | 1423 |
| Analyzed Artifacts (Scanned) | 412 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1011 |
| Total LOC | 39838 |
| Volatility Index | 0.345 |
| % Scanned of codebase = | 29.0% |
| Dominant Lang | REXX |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3906 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.227 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3447 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 117 | 0 | 28.4% |
| JAVA | 84 | 8767 | 20.4% |
| PLAINTEXT | 64 | 0 | 15.5% |
| REXX | 51 | 14702 | 12.4% |
| C | 20 | 6584 | 4.9% |
| COBOL | 18 | 4752 | 4.4% |
| XML | 11 | 0 | 2.7% |
| PYTHON | 10 | 1527 | 2.4% |
| MAKEFILE | 9 | 154 | 2.2% |
| SHELL | 7 | 304 | 1.7% |
| JCL | 5 | 152 | 1.2% |
| JSON | 4 | 1438 | 1.0% |
| HTML | 3 | 540 | 0.7% |
| DOCKERFILE | 2 | 15 | 0.5% |
| ASSEMBLY | 2 | 78 | 0.5% |
| CSV | 1 | 73 | 0.2% |
| CPP | 1 | 16 | 0.2% |
| PERL | 1 | 97 | 0.2% |
| HLASM | 1 | 638 | 0.2% |
| BINARY_THREAT | 1 | 1 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.509`
> **Composition Archetype:** `Mid Flat Project` (z +2.51; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 50%, Large Core Modules (3) 16%, Large Core Modules 9%, Declarative / Non-Code 7%, Compute Cores Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 229 | 55.6% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 181 | 43.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1011*

**Composition by Extension & Reason:**
- `.pdf`: 735x Excluded (Explicitly Denied Extension: '.pdf')
- `.woff`: 90x Excluded (Explicitly Denied Extension: '.woff')
- `.woff2`: 90x Excluded (Explicitly Denied Extension: '.woff2')
- `.xml`: 2x Excluded (Saturation: Line 41 exceeds 500 chars), 1x Excluded (Static Asset Blob without Intent: 2213 LOC), 1x Excluded (Static Asset Blob without Intent: 1082 LOC)
- `.listing`: 17x Excluded (Unsupported Extension: '.listing')
- `no_extension`: 5x Unsupported Format (.undeterminable), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: 'no_extension')
- `.json`: 1x Excluded (Static Asset Blob without Intent: 1990 LOC), 1x Excluded (Static Asset Blob without Intent: 2418 LOC), 1x Excluded (Massive Static Asset Blob: 4338 LOC)
- `.obj`: 4x Excluded (Explicitly Denied Extension: '.obj')
- `.jar`: 3x Excluded (Explicitly Denied Extension: '.jar')
- `.conf`: 3x Excluded (Unsupported Extension: '.conf')
- `.xmit`: 3x Excluded (Unsupported Extension: '.xmit')
- `.rex`: 2x Excluded (Unsupported Extension: '.rex')
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.pptx`: 2x Excluded (Explicitly Denied Extension: '.pptx')
- `.md`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2809 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.6 | 37.4 | 33.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 66.8 | 87.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.9 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.6 | 5.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 61.3 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 69.8 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 53.1 | 2.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 42.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.7 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 15.5 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3237 | 103 | 10 | `zOS-PKI/gencert.c` |
| cleanup | 99 | 57 | 1 | `zOS-PKI/gencert.c` |
| guards | 939 | 135 | 6 | `SMF-Tools/SMF84Formatter/smf84fmt.c` |
| danger | 1469 | 154 | 11 | `zOS-Tools-and-Toys/submit2/submit2.sh` |
| concurrency | 13 | 8 | 0 | `zOS-Tools-and-Toys/msglg610/stdjes3.jcl` |
| connectivity | 1455 | 140 | 12 | `zOS-Tools-and-Toys/ping/netinet/ip_var.h` |
| io | 539 | 95 | 3 | `zOS-Tools-and-Toys/msglg610/iplmerg4.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 540 | 64 | 3 | `zOS-Tools-and-Toys/wjsfsmon/wjsfsmon.rexx` |
| time | 46 | 20 | 0 | `zOS-Tools-and-Toys/wjsfsmon/wjsfsmon.rexx` |
| serialization | 2 | 2 | 0 | `zOS-Print/ACIF-User-Exit-samples/Cobol Source/ACIFOTX.COB` |
| regex | 14 | 7 | 0 | `zOS-Print/ACIF-User-Exit-samples/Cobol Source/APKINPTS.COB` |
| events | 60 | 38 | 0 | `zOS-Tools-and-Toys/ping/ping.c` |
| tests | 4 | 3 | 0 | `zOS-Print/ACIF-User-Exit-samples/Cobol Source/APKXPSEG.COB` |
| docs | 1047 | 125 | 8 | `SMF-Tools/SMF_WAS/src/com/ibm/smf/twas/request/ZosRequestInfoSection.java` |
| debt | 2086 | 123 | 13 | `zOS-Print/ACIF-User-Exit-samples/Cobol Source/STRFLDS.COB` |
| mutation | 18531 | 196 | 141 | `zOS-Tools-and-Toys/wjsfsmon/wjsfsmon.rexx` |
| dead_code | 416 | 107 | 5 | `zOS-Tools-and-Toys/wjsfsmon/wjsfsmon.rexx` |
| credential | 4 | 2 | 0 | `zOS-Workflow/Tailored Fit Pricing for IBM Z Workflow/workflow_tailoredfitpricing_colocated.xml` |
| threat | 337 | 54 | 2 | `zOS-Tools-and-Toys/fsq/fsq.rexx` |
| ml_ai | 99 | 24 | 0 | `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/ZCAPI.java` |
| ui | 53 | 11 | 0 | `zOS-Tools-and-Toys/msglg610/iplmerg4.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `zOS-Tools-and-Toys/msglg610/iplmerg4.html` (Hits: 78)
- `zOS-Tools-and-Toys/submit2/submit2.sh` (Hits: 58)
- `zOSMF/Zosmf-Python/SecurityAPITest.py` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **SmfPrintStream.java** (`SMF-Tools/SMF_CORE/src/com/ibm/smf/format/SmfPrintStream.java`) — 57 inbound connections
2. **UnsupportedVersionException.java** (`SMF-Tools/SMF_CORE/src/com/ibm/smf/format/UnsupportedVersionException.java`) — 39 inbound connections
3. **SmfRecord.java** (`SMF-Tools/SMF_CORE/src/com/ibm/smf/format/SmfRecord.java`) — 31 inbound connections
4. **SmfStream.java** (`SMF-Tools/SMF_CORE/src/com/ibm/smf/format/SmfStream.java`) — 29 inbound connections
5. **SmfEntity.java** (`SMF-Tools/SMF_CORE/src/com/ibm/smf/format/SmfEntity.java`) — 27 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **WLM Documents.md** (`zOS-WLM/WLM Documents.md`) — 33 outbound dependencies
2. **RestConnection.java** (`zOSMF/ZosmfRESTClient/src/com/ibm/zosmf/restclient/basic/RestConnection.java`) — 23 outbound dependencies
3. **ping.c** (`zOS-Tools-and-Toys/ping/ping.c`) — 21 outbound dependencies
4. **ResponseTimes.java** (`SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/ResponseTimes.java`) — 21 outbound dependencies
5. **readme.md** (`readme.md`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` **(Many-Argument Workhorses)** (@ `zOS-PKI/gencert.c`) -> Impact: **440.3** | LOC: 1220
  * *Intent:* /* * Start of program */
- `processRecord` **(Many-Argument Workhorses)** (@ `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/CSVExport.java`) -> Impact: **118.1** | LOC: 523
- `SMFType98SubType1` **(Compute Cores)** (@ `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/types/SMFType98SubType1.java`) -> Impact: **113.8** | LOC: 268
- `traverse` **(Many-Argument Workhorses)** (@ `zOS-Tools-and-Toys/dirsize/dirsize.c`) -> Impact: **112.5** | LOC: 130
- `main` **(Many-Argument Workhorses)** (@ `zOS-Tools-and-Toys/rexxc/rexx.c`) -> Impact: **109.2** | LOC: 279
  * *Intent:* /**********************************************************************/ /* main() */ /***************************************************************...
- `pager` **(Many-Argument Workhorses)** (@ `zOS-Tools-and-Toys/jes/jes.rexx`) -> Impact: **100.4** | LOC: 206
  * *Intent:* /************************************************************/ /************************************************************/
- `pager` **(Many-Argument Workhorses)** (@ `zOS-Tools-and-Toys/sdsfutil/jes.rexx`) -> Impact: **100.4** | LOC: 206
  * *Intent:* /************************************************************/ /************************************************************/
- `traverse` **(Many-Argument Workhorses)** (@ `zOS-Tools-and-Toys/ifind/ifind.c`) -> Impact: **97.6** | LOC: 90
- `main` **(Many-Argument Workhorses)** (@ `zOS-Tools-and-Toys/sparse/sparse.c`) -> Impact: **82.4** | LOC: 263
  * *Intent:* int fopt=0; /* filename option */ int vopt=0; /* keep option */ int ropt=0; /* repeat string */ int lopt=0; /* line numbers */ int sopt=0; /* keep opt...
- `process_cmd` **(Compute Cores)** (@ `zOS-Tools-and-Toys/view/view.c`) -> Impact: **81.1** | LOC: 67
  * *Intent:* /* processes a given character command */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `zOS-Tools-and-Toys/wjsip` | 10 | 4606.9 | 79.42% | 37.32% |
| `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins` | 21 | 4101.9 | 67.36% | 72.9% |
| `zOS-Tools-and-Toys/wjsfsmon` | 2 | 2664.96 | 37.99% | 10.26% |
| `zOS-Print/ACIF-User-Exit-samples/Cobol Source` | 18 | 1750.24 | 35.08% | 74.38% |
| `zOS-Tools-and-Toys/view` | 7 | 1392.8 | 20.25% | 7.42% |
| `zOS-Tools-and-Toys/wjssmf` | 3 | 1271.46 | 72.58% | 0.0% |
| `zOS-Tools-and-Toys/devinfo` | 2 | 1082.34 | 33.98% | 5.66% |
| `zOS-Tools-and-Toys/fsq` | 2 | 1067.6 | 42.94% | 5.13% |
| `zOS-PKI` | 3 | 1018.4 | 27.42% | 27.14% |
| `SMF-Tools/SMF_CORE/src/com/ibm/smf/format` | 16 | 961.06 | 21.73% | 19.92% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `zOS-Print/ACIF-User-Exit-samples/Cobol Source/STRFLDS.COB` -> **100.0%** Exposure
- `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/AffinityCreation.java` -> **99.9894%** Exposure
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/plugins/Type98CPU.java` -> **99.9447%** Exposure
- `zOS-Print/ACIF-User-Exit-samples/Cobol Source/APKINPXT.COB` -> **99.9106%** Exposure
- `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/ReWrite.java` -> **99.7464%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `SMF-Tools/SMF84Formatter/smf84fmt.c` -> **100.0%** Exposure
- `zOS-Tools-and-Toys/dirsize/dirsize.c` -> **100.0%** Exposure
- `zOS-Tools-and-Toys/getuids/getuids.c` -> **100.0%** Exposure
- `zOS-Tools-and-Toys/ifind/ifind.c` -> **100.0%** Exposure
- `zOS-Tools-and-Toys/ping/ping.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/AffinityCreation.java` -> **11** Orphaned Functions | **8** Duplicates
- `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/ThreadRequestDensity.java` -> **11** Orphaned Functions | **4** Duplicates
- `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/ThreadRequestDensity2.java` -> **11** Orphaned Functions | **4** Duplicates
- `zOS-Tools-and-Toys/wjsfsmon/wjsfsmon.rexx` -> **8** Orphaned Functions | **6** Duplicates
- `zOS-Tools-and-Toys/view/l_unix.c` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `zOS-PKI/gencert.c` -> **15.496%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `448` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `928` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `zOS-Tools-and-Toys/wjsfsmon/wjsfsmon.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2663.96 | **LOC:** 2797 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 92.772% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `details` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* /**********************************************************************/
  * `showbyfs` **(I/O & Config Routines)** (Impact: 33.4)
    * *Intent:* /**********************************************************************/
  * `cleanup` **(Many-Argument Workhorses)** (Impact: 24.5)
  * `setcolors` **(I/O & Config Routines)** (Impact: 21.9)
    * *Intent:* /**********************************************************************/
  * `showcontention` **(I/O & Config Routines)** (Impact: 21.9)
    * *Intent:* /**********************************************************************/
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 618 instances
* *High Risk Execution (weighted view):* 16
* *State Mutation (weighted view):* 1968
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 554`, `args: 33`, `func_start: 81`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 19`, `state_mutation: 732`, `dead_code: 9`, `duplicate_logic: 6`, `unreferenced_by_name: 8`
* *Architecture:* `io: 13`
* *Defense:* `safety: 16`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/devinfo/devinfo.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1081.34 | **LOC:** 896 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 81.478% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Getdev_Info` **(I/O & Config Routines)** (Impact: 43.7)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Parse the D M=DEV() comma...
  * `DEVINW` **(Compute Cores)** (Impact: 42.7)
    * *Intent:* ** BOTPRINT - This is an optional keyword which, if provided, will ** ** reformat the generated outp...
  * `GetPhysical_Chp` **(I/O & Config Routines)** (Impact: 24.6)
    * *Intent:* /*-------------------------------------------------------------------*/
  * `Initialize` **(I/O & Config Routines)** (Impact: 23.1)
    * *Intent:* /*------------------------ Subroutines ------------------------------*/ /*--------------------------...
  * `Channel_Summary` **(I/O & Config Routines)** (Impact: 22.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Write a summary of the ch...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 255 instances
* *State Mutation (weighted view):* 885
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 82`, `args: 1`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 375`, `dead_code: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`
* *Defense:* `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/fsq/fsq.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1066.6 | **LOC:** 1131 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (85.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.257% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printinfo` **(I/O & Config Routines)** (Impact: 53.4)
    * *Intent:* /**********************************************************************/
  * `halt` **(Compute Cores)** (Impact: 43.2)
  * `getlfsinfo` **(Compute Cores)** (Impact: 39.0)
  * `getopts` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* /* do */ /* if opt.lca<>'' then say 'Option a was specified' */ /* if opt.lcb<>'' then say 'Option b...
  * `loadtemplate` **(Compute Cores)** (Impact: 23.8)
    * *Intent:* /**********************************************************************/
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 234 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 729
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 250`, `args: 13`, `func_start: 24`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 261`, `dead_code: 9`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-PKI/gencert.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1010.78 | **LOC:** 1621 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 2.002; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.0%), Complexity Load (formerly Cognitive Load) (82.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 440.3)
    * *Intent:* /* * Start of program */
  * `usage` **(I/O & Config Routines)** (Impact: 14.3)
  * `updateCPL` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `displayCPL` **(Compute Cores)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 138 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 496
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 176`, `args: 15`, `func_start: 4`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 220`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 13`, `import: 12`
* *Defense:* `safety: 3`, `immutability_locks: 47`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, errno.h, stddef.h, stdio.h, stdlib.h, string.h, strings.h, stat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/view/l_unix.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 860.36 | **LOC:** 682 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 2.002; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_next_line` **(Compute Cores)** (Impact: 37.2)
    * *Intent:* /* reads in another line from the file, if any, else return NULL */
  * `rescreen` **(I/O & Config Routines)** (Impact: 25.1)
    * *Intent:* /* this is a refresh routine that prints out the current screen from topline it returns the next com...
  * `getcmd` **(Compute Cores)** (Impact: 23.1)
    * *Intent:* /* this function reads uses getchar() to read unbuffered input from the keyboard and processes the k...
  * `initialize` **(I/O & Config Routines)** (Impact: 19.0)
    * *Intent:* /* initializes the case globals for character formatting */
  * `strinstr` **(Compute Cores)** (Impact: 16.1)
    * *Intent:* /* this determines if global searchstr is in the param string str */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 155 instances
* *State Mutation (weighted view):* 667
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 34`, `args: 21`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 3`, `state_mutation: 357`, `dead_code: 6`, `unreferenced_by_name: 10`
* *Architecture:* `io: 1`, `api: 15`, `import: 9`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ctype.h, curses.h, l_unix.h, memory.h, signal.h, stdio.h, string.h, types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjsip/wjsipuse.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 797.68 | **LOC:** 791 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatcb` **(Many-Argument Workhorses)** (Impact: 31.1)
    * *Intent:* /**********************************************************************/ /* this formats or dumps a ...
  * `$fetch$` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /**********************************************************************/
  * `findlatch` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `start` **(I/O & Config Routines)** (Impact: 15.8)
  * `parseoptshelp` **(I/O & Config Routines)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 136`, `args: 13`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 5`, `state_mutation: 209`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/fscp/fscp.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 730.32 | **LOC:** 930 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compfs` **(I/O & Config Routines)** (Impact: 60.2)
    * *Intent:* /* compare two file systems */
  * `docopy` **(I/O & Config Routines)** (Impact: 19.1)
    * *Intent:* /* copy one file system to another using pax or copytree */
  * `compfile` **(I/O & Config Routines)** (Impact: 12.6)
    * *Intent:* /* compare two files */
  * `mkzfs` **(I/O & Config Routines)** (Impact: 12.2)
  * `compspace` **(I/O & Config Routines)** (Impact: 11.9)
    * *Intent:* /* compare space attributes between file systems */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 492
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 192`, `args: 3`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 180`, `dead_code: 2`
* *Architecture:* `io: 1`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjsip/wjsigmmp.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 710.44 | **LOC:** 677 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatcb` **(Many-Argument Workhorses)** (Impact: 31.1)
    * *Intent:* /**********************************************************************/ /* this formats or dumps a ...
  * `$fetch$` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /**********************************************************************/
  * `rungyac` **(Compute Cores)** (Impact: 14.9)
  * `parseoptshelp` **(I/O & Config Routines)** (Impact: 14.2)
  * `wjsidstart` **(I/O & Config Routines)** (Impact: 13.4)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 500
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 110`, `args: 12`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 4`, `state_mutation: 200`, `unreferenced_by_name: 9`
* *Architecture:* `io: 2`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/jes/jes.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 665.16 | **LOC:** 614 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (92.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pager` **(Many-Argument Workhorses)** (Impact: 100.4)
    * *Intent:* /************************************************************/ /************************************...
  * `getline` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* /************************************************************/ /************************************...
  * `find` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* /************************************************************/
  * `set` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /************************************************************/
  * `canon` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /************************************************************/
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 128 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 466
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 91`, `args: 7`, `func_start: 17`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 210`
* *Architecture:* `io: 6`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/sdsfutil/jes.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 665.16 | **LOC:** 614 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (92.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.191% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pager` **(Many-Argument Workhorses)** (Impact: 100.4)
    * *Intent:* /************************************************************/ /************************************...
  * `getline` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* /************************************************************/ /************************************...
  * `find` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* /************************************************************/
  * `set` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /************************************************************/
  * `canon` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /************************************************************/
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 128 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 466
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 91`, `args: 7`, `func_start: 17`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 210`
* *Architecture:* `io: 6`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjssmf/wjssmfr.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 630.88 | **LOC:** 673 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (84.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getargs` **(I/O & Config Routines)** (Impact: 33.8)
    * *Intent:* /* parse command line arguments */
  * `checksel` **(Compute Cores)** (Impact: 18.8)
  * `formatsec` **(I/O & Config Routines)** (Impact: 18.4)
  * `dump` **(Type Conversions)** (Impact: 11.4)
    * *Intent:* /**********************************************************************/ /* formatted dump utility *...
  * `getsrc` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 453
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 131`, `args: 6`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 151`
* *Architecture:* `io: 6`
* *Defense:* `safety: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `SMF-Tools/SMF84Formatter/smf84fmt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 628.46 | **LOC:** 1418 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.002; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (89.1%), Complexity Load (formerly Cognitive Load) (64.9%)
- **Documentation Coverage:** 30.9524% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_parm` **(Compute Cores)** (Impact: 38.4)
  * `format_records_json` **(I/O & Config Routines)** (Impact: 23.0)
    * *Intent:* /*********************************************************************/ /* Record formatting - JSON ...
  * `format_headings_csv` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `format_records_csv` **(I/O & Config Routines)** (Impact: 20.0)
    * *Intent:* /*********************************************************************/ /* Record formatting - CSV *...
  * `main` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* /*********************************************************************/ /* smf84fmt mainline */ /***...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 33`, `args: 17`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 184`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 49`, `doc: 21`, `immutability_locks: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ctype.h, smf84fmt.h, stdarg.h, stdint.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/ping/ping.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 539.86 | **LOC:** 1117 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 2.002; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Complexity Load (formerly Cognitive Load) (73.1%), Debt Markers (formerly Tech Debt) (22.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finish` **(Type Conversions)** (Impact: 13.0)
    * *Intent:* /* * finish -- * Print out statistics, and give up. */
  * `catcher` **(Type Conversions)** (Impact: 8.0)
    * *Intent:* /* * catcher -- * This routine causes another PING to be transmitted, and then * schedules another S...
  * `pr_addr` **(C Struct Operations)** (Impact: 6.5)
    * *Intent:* /* * pr_addr -- * Return an ascii host address as a dotted quad and optionally with * a hostname. */
  * `status` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /* * status -- * Print out statistics when SIGINFO is received. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 159 instances
* *High Risk Execution (weighted view):* 15
* *State Mutation (weighted view):* 480
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 238`, `args: 21`, `func_start: 4`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 18`, `state_mutation: 162`, `fragile_debt: 7`
* *Architecture:* `io: 4`, `api: 10`, `import: 22`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` inet.h, ctype.h, errno.h, netdb.h, in.h, in_systm.h, ip.h, ip_icmp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjsip/wjsigshm.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 518.88 | **LOC:** 463 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (93.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `halt` **(Compute Cores)** (Impact: 54.6)
  * `$fetch$` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /**********************************************************************/
  * `getstor` **(Many-Argument Workhorses)** (Impact: 12.2)
    * *Intent:* /**********************************************************************/
  * `dump` **(Type Conversions)** (Impact: 8.1)
    * *Intent:* /**********************************************************************/ /* formatted dump utility *...
  * `getpprp` **(Type Conversions)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 119 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 73`, `args: 11`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 142`, `dead_code: 2`, `unreferenced_by_name: 6`
* *Architecture:* `io: 3`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-WLM/Samples/wlmsamp.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 3.704; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002427
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zOS-Tools-and-Toys/where/where.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 496.68 | **LOC:** 498 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (61.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 72.22% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ismember` **(Compute Cores)** (Impact: 20.7)
  * `findem` **(Compute Cores)** (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 46`, `args: 3`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 295`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/CSVExport.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 451.5 | **LOC:** 602 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 2.002; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Complexity Load (formerly Cognitive Load) (95.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processRecord` **(Many-Argument Workhorses)** (Impact: 118.1)
  * `preParse` **(Compute Cores)** (Impact: 4.6)
  * `initialize` **(Compute Cores)** (Impact: 3.2)
  * `parse` **(Parameter Forwarders)** (Impact: 1.6)
  * `processingComplete` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 308
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 44`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 170`, `unreferenced_by_name: 5`
* *Architecture:* `api: 7`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` com.ibm.smf.format.DefaultFilter, com.ibm.smf.format.SMFFilter, com.ibm.smf.format.SmfPrintStream, com.ibm.smf.format.SmfRecord, com.ibm.smf.format.Triplet, com.ibm.smf.twas.request.NetworkDataSection, com.ibm.smf.twas.request.PlatformNeutralRequestInfoSection, com.ibm.smf.twas.request.RequestActivitySmfRecord...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjsip/wjsigref.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 447.4 | **LOC:** 455 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `halt` **(Compute Cores)** (Impact: 46.9)
  * `$fetch$` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /**********************************************************************/
  * `getstor` **(Many-Argument Workhorses)** (Impact: 12.2)
    * *Intent:* /**********************************************************************/
  * `dump` **(Type Conversions)** (Impact: 8.1)
    * *Intent:* /**********************************************************************/ /* formatted dump utility *...
  * `getstor64` **(Compute Cores)** (Impact: 6.7)
    * *Intent:* /**********************************************************************/
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 95 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 307
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 76`, `args: 11`, `func_start: 16`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 117`, `unreferenced_by_name: 7`
* *Architecture:* `io: 3`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjsip/wjsipndc.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 443.1 | **LOC:** 478 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `halt` **(Compute Cores)** (Impact: 27.9)
  * `$fetch$` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /**********************************************************************/
  * `zfspfsctl` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* /**********************************************************************/ /* pfsctl: issue the pfsctl...
  * `getstor` **(Many-Argument Workhorses)** (Impact: 12.2)
    * *Intent:* /**********************************************************************/
  * `dump` **(Type Conversions)** (Impact: 8.1)
    * *Intent:* /**********************************************************************/ /* formatted dump utility *...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 94 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 318
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 75`, `args: 10`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 130`, `unreferenced_by_name: 5`
* *Architecture:* `io: 3`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjsftp/iftp.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 436.96 | **LOC:** 658 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Complexity Load (formerly Cognitive Load) (84.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `localfile` **(Compute Cores)** (Impact: 39.6)
  * `hostfile` **(Compute Cores)** (Impact: 39.6)
  * `sortstem` **(Compute Cores)** (Impact: 13.3)
  * `runcmds` **(Defensive Guards)** (Impact: 12.6)
  * `showdirs` **(I/O & Config Routines)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 117`, `args: 7`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 85`
* *Architecture:* None
* *Defense:* `safety: 6`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/view/view.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 435.94 | **LOC:** 326 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.002; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.4%)
- **Documentation Coverage:** 42.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_cmd` **(Compute Cores)** (Impact: 81.1)
    * *Intent:* /* processes a given character command */
  * `main` **(Compute Cores)** (Impact: 31.6)
    * *Intent:* * heim@us.ibm.com * * This file contains the main function definitions * that [supposedly] comply wi...
  * `process_arg` **(Compute Cores)** (Impact: 20.6)
    * *Intent:* /*************************************************************** functions */ /* this processes comm...
  * `search` **(Compute Cores)** (Impact: 12.5)
    * *Intent:* /* this is the linear search algorithm, starting from the given line_t *search */
  * `pipeout` **(Compute Cores)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 21`, `args: 19`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 81`, `dead_code: 7`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 13`, `import: 4`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdio.h, string.h, stat.h, view.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjsip/wjsigrfi.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 433.2 | **LOC:** 423 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `$fetch$` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /**********************************************************************/
  * `halt` **(Compute Cores)** (Impact: 22.4)
  * `setflags` **(Compute Cores)** (Impact: 14.9)
  * `getstor` **(Many-Argument Workhorses)** (Impact: 12.2)
    * *Intent:* /**********************************************************************/
  * `dump` **(Type Conversions)** (Impact: 8.1)
    * *Intent:* /**********************************************************************/ /* formatted dump utility *...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 93 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 72`, `args: 11`, `func_start: 17`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 119`, `unreferenced_by_name: 7`
* *Architecture:* `io: 3`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjsip/wjsigstl.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 424.96 | **LOC:** 415 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `$fetch$` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /**********************************************************************/
  * `halt` **(Compute Cores)** (Impact: 19.3)
  * `setflags` **(Compute Cores)** (Impact: 14.9)
  * `getstor` **(Many-Argument Workhorses)** (Impact: 12.2)
    * *Intent:* /**********************************************************************/
  * `dump` **(Type Conversions)** (Impact: 8.1)
    * *Intent:* /**********************************************************************/ /* formatted dump utility *...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 91 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 300
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 70`, `args: 10`, `func_start: 17`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 118`, `dead_code: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 3`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/rexxc/rexx.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 420.06 | **LOC:** 516 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.002; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (44.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 109.2)
    * *Intent:* /**********************************************************************/ /* main() */ /*************...
  * `newline` **(Type Conversions)** (Impact: 7.5)
    * *Intent:* /**********************************************************************/
  * `catline` **(Type Conversions)** (Impact: 4.9)
    * *Intent:* /**********************************************************************/
  * `cknull` **(Parameter Forwarders)** (Impact: 3.2)
    * *Intent:* /**********************************************************************/
  * `usage` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* /**********************************************************************/
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 87 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 25`, `args: 7`, `func_start: 5`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 9`, `state_mutation: 99`, `dead_code: 5`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 14`, `import: 5`
* *Defense:* `doc: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, fcntl.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zOS-Tools-and-Toys/wjsigshl/wjsigshl.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 396.0 | **LOC:** 438 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 90.55% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `$fetch$` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /**********************************************************************/
  * `runshlm` **(Type Conversions)** (Impact: 13.0)
  * `getstor` **(Many-Argument Workhorses)** (Impact: 12.2)
    * *Intent:* /**********************************************************************/
  * `halt` **(Compute Cores)** (Impact: 11.9)
  * `dump` **(Type Conversions)** (Impact: 8.1)
    * *Intent:* /**********************************************************************/ /* formatted dump utility *...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 83 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 75`, `args: 11`, `func_start: 17`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 112`, `unreferenced_by_name: 7`
* *Architecture:* `io: 3`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `SMF-Tools/SMF84Formatter/Makefile` -> Churn: **100.0%** | Cog Load: 0.0% | Debt: 95.2574%
- `SMF-Tools/SMF84Formatter/smf84fmt.c` -> Churn: **100.0%** | Cog Load: 64.9404% | Debt: 8.8209%
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/ISmfFile.java` -> Churn: **100.0%** | Cog Load: 0.0% | Debt: 97.0688%
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/JclSmf.java` -> Churn: **100.0%** | Cog Load: 77.227% | Debt: 21.2567%
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/JzOSSmfFile.java` -> Churn: **100.0%** | Cog Load: 18.4944% | Debt: 99.593%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `SMF-Tools/SMF84Formatter/smf84fmt.c` -> **Kevin Grigorenko** (100.0% isolated ownership) | Magnitude: 628.46
- `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/CSVExport.java` -> **Kevin Grigorenko** (100.0% isolated ownership) | Magnitude: 451.5
- `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/RequestDensity2.java` -> **Kevin Grigorenko** (100.0% isolated ownership) | Magnitude: 378.92
- `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/ResponseTimes.java` -> **Kevin Grigorenko** (100.0% isolated ownership) | Magnitude: 373.3
- `SMF-Tools/SMF_WAS_PLUGINS/src/com/ibm/smf/was/plugins/RequestsPerServer.java` -> **Kevin Grigorenko** (100.0% isolated ownership) | Magnitude: 367.78

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `SMF-Tools/SMF_WAS/src/com/ibm/smf/twas/request/RequestActivitySmfRecord.java` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 100.0%)
- `SMF-Tools/SMF_WAS/src/com/ibm/smf/liberty/request/LibertyRequestRecord.java` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 100.0%)
- `SMF-Tools/SMF_WAS/src/com/ibm/smf/twas/request/ZosRequestInfoSection.java` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 99.9982%)
- `SMF-Tools/SMF_WAS/src/com/ibm/smf/was/common/PlatformNeutralSection.java` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 100.0%)
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/SmfRecord.java` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/SmfPrintStream.java` -> **Severity: 12.896** (Embedded: 0.1385 * Error Risk: 93.1055%)
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/SmfStream.java` -> **Severity: 8.072** (Embedded: 0.0886 * Error Risk: 91.0989%)
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/SmfRecord.java` -> **Severity: 7.076** (Embedded: 0.0753 * Error Risk: 93.9509%)
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/utilities/ConversionUtilities.java` -> **Severity: 5.1** (Embedded: 0.0575 * Error Risk: 88.7582%)
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/DefaultFilter.java` -> **Severity: 4.346** (Embedded: 0.051 * Error Risk: 85.2629%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `zOS-Container-Platform/multi-architecture-images/basic-image-building/src/java/ExampleTool.java` -> **Severity: 515.0** (Blast Radius: 5.15 * Doc Risk: 100.0%)
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/utilities/ConversionUtilities.java` -> **Severity: 277.18** (Blast Radius: 13.859 * Doc Risk: 20.0%)
- `zOSMF/ZosmfRESTClient/src/com/ibm/zosmf/restclient/basic/RestConnection.java` -> **Severity: 264.572** (Blast Radius: 3.704 * Doc Risk: 71.4286%)
- `SMF-Tools/SMF_CORE/src/com/ibm/smf/format/types/SMFType98SubType1.java` -> **Severity: 228.6** (Blast Radius: 2.286 * Doc Risk: 100.0%)
- `zOS-PKI/makefile` -> **Severity: 200.2** (Blast Radius: 2.002 * Doc Risk: 100.0%)

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
