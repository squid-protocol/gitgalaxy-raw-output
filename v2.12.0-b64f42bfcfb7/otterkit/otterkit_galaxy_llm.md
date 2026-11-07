# ARCHITECTURAL_BRIEF: otterkit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/otterkit/otterkit.git` |
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
- **Scope:** 45 analyzed artifact(s), 14249 LOC.
- **Load-bearing artifact:** `Libraries/Otterkit.Native/decNumber/decContext.c` -- 13 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Libraries/Otterkit.Native/nativelib/decNumber.c` -- pulls in 7 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Libraries/Otterkit.Native/decNumber/decNumber.c` at magnitude 9222.0 (structural weight, not risk).
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
| Total Artifacts | 57 |
| Analyzed Artifacts (Scanned) | 45 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 12 |
| Total LOC | 14249 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 78.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3753 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1802 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3037 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 36 | 14077 | 80.0% |
| MARKDOWN | 6 | 0 | 13.3% |
| HTML | 1 | 38 | 2.2% |
| CPP | 1 | 134 | 2.2% |
| PLAINTEXT | 1 | 0 | 2.2% |

## 4.1 SOURCE ENCODINGS
All 45 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 33%, Compute Cores Files 18%, Data / Markup / Trivial 18%, Many-Argument Workhorses Files 16%, Large Core Modules (3) 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 38 | 84.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 15.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 12*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 3x Excluded (Unsupported Extension: '.patch')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.dll`: 1x Excluded (Explicitly Denied Extension: '.dll')
- `.dylib`: 1x Excluded (Explicitly Denied Extension: '.dylib')
- `.so`: 1x Excluded (Explicitly Denied Extension: '.so')
- `.h`: 1x Excluded (Embedded Array/Matrix Payload: 19650 commas in 1186 LOC)
- `.pdf`: 1x Excluded (Explicitly Denied Extension: '.pdf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.9 | 25.9 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.1 | 37.6 | 51.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.8 | 15.4 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 24.8 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.8 | 5.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.1 | 6.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 13.4 | 1.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.4 | 84.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 88 | 8 | 2 | `Libraries/Otterkit.Native/decNumber/decNumber.c` |
| cleanup | 43 | 1 | 0 | `Libraries/Otterkit.Native/decNumber/decNumber.c` |
| guards | 953 | 25 | 87 | `Libraries/Otterkit.Native/decNumber/decNumber.c` |
| danger | 86 | 14 | 5 | `Libraries/Otterkit.Native/decNumber/decNumber.c` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 560 | 29 | 64 | `Libraries/Otterkit.Native/nativelib/decNumber.c` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 1 | 0 | `Libraries/Otterkit.Native/nativelib/CASPAL.h` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 3 | 2 | 0 | `Libraries/Otterkit.Native/decNumber/example4.c` |
| tests | 0 | 0 | 0 | - |
| docs | 1 | 1 | 0 | `Libraries/Otterkit.Native/decNumber/ICU-license.html` |
| debt | 124 | 16 | 3 | `Libraries/Otterkit.Native/decNumber/decNumber.c` |
| mutation | 4892 | 19 | 190 | `Libraries/Otterkit.Native/decNumber/decNumber.c` |
| dead_code | 264 | 22 | 14 | `Libraries/Otterkit.Native/nativelib/decNumber.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 205 | 7 | 26 | `Libraries/Otterkit.Native/decNumber/decCommon.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.github/ISSUE_TEMPLATE/✨request-a-new-feature.md` (Hits: 0)
- `.github/ISSUE_TEMPLATE/🐛-report-a-bug.md` (Hits: 0)
- `.github/ISSUE_TEMPLATE/🔒-report-a-security-vulnerability.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **decContext.c** (`Libraries/Otterkit.Native/decNumber/decContext.c`) — 13 inbound connections
2. **decNumber.h** (`Libraries/Otterkit.Native/decNumber/decNumber.h`) — 13 inbound connections
3. **decNumber.c** (`Libraries/Otterkit.Native/decNumber/decNumber.c`) — 12 inbound connections
4. **decNumberLocal.h** (`Libraries/Otterkit.Native/decNumber/decNumberLocal.h`) — 9 inbound connections
5. **decContext.h** (`Libraries/Otterkit.Native/decNumber/decContext.h`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **decNumber.c** (`Libraries/Otterkit.Native/nativelib/decNumber.c`) — 7 outbound dependencies
2. **decNumber.c** (`Libraries/Otterkit.Native/decNumber/decNumber.c`) — 6 outbound dependencies
3. **decimal64.c** (`Libraries/Otterkit.Native/decNumber/decimal64.c`) — 6 outbound dependencies
4. **decDouble.c** (`Libraries/Otterkit.Native/decNumber/decDouble.c`) — 5 outbound dependencies
5. **decQuad.c** (`Libraries/Otterkit.Native/decNumber/decQuad.c`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `decLnOp` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decNumber.c`) -> Impact: **1218.7** | LOC: 2460
  * *Intent:* /* 3. Fastpaths are included for ln(10) and ln(2), up to length 40, */ /* as these are common requests. ln(10) is used by log10(x). */ /* */ /* 4. An ...
- `decDivideOp` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decNumber.c`) -> Impact: **365.1** | LOC: 582
  * *Intent:* /* exp=exp-1 */ /* end outer_loop */ /* exp=exp+1 -- set the proper exponent */ /* if have=0 then generate answer=0 */ /* Return (Result is defined by...
- `decDivide` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decBasic.c`) -> Impact: **301.6** | LOC: 497
  * *Intent:* /* */ /* result gets the result of dividing dfl by dfr: */ /* dfl is the first decFloat (lhs) */ /* dfr is the second decFloat (rhs) */ /* set is the ...
- `decAddOp` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decNumber.c`) -> Impact: **218.2** | LOC: 343
  * *Intent:* /* overlap the A or B coefficient */ /* then the result must be calculated into a temporary buffer. In */ /* this case a local (stack) buffer is used ...
- `decCompareOp` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decNumber.c`) -> Impact: **203.4** | LOC: 152
  * *Intent:* /* */ /* res is C, the result. C may be A and/or B (e.g., X=X?X) */ /* lhs is A */ /* rhs is B */ /* set is the context */ /* op is the operation flag...
- `decNumberPower` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decNumber.c`) -> Impact: **192.9** | LOC: 326
  * *Intent:* /* Mathematical function restrictions apply (see above); a NaN is */ /* returned with Invalid_operation if a restriction is violated. */ /* */ /* Howe...
- `decFloatFMA` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decBasic.c`) -> Impact: **187.3** | LOC: 268
  * *Intent:* /* ------------------------------------------------------------------ */ /* decFloatFMA -- multiply and add three decFloats, fused */ /* */ /* result ...
- `decFinalize` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decCommon.c`) -> Impact: **178.6** | LOC: 331
  * *Intent:* #endif
- `decNumberFromString` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decNumber.c`) -> Impact: **167.4** | LOC: 229
  * *Intent:* /* set -- the context used for processing any error, */ /* determining the maximum precision available */ /* (set.digits), determining the maximum and...
- `decFloatFromString` **(Many-Argument Workhorses)** (@ `Libraries/Otterkit.Native/decNumber/decCommon.c`) -> Impact: **151.3** | LOC: 227
  * *Intent:* /* coefficient it will be rounded. */ /* set is the context */ /* returns result */ /* */ /* The length of the coefficient and the size of the exponen...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Libraries/Otterkit.Native/decNumber` | 30 | 17493.96 | 25.28% | 18.26% |
| `Libraries/Otterkit.Native/nativelib` | 9 | 816.92 | 25.21% | 43.77% |
| `__monolith__` | 3 | 3.86 | 0.0% | 0.0% |
| `.github/ISSUE_TEMPLATE` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Libraries/Otterkit.Native/nativelib/decNumber.c` -> **99.9972%** Exposure
- `Libraries/Otterkit.Native/decNumber/decContext.c` -> **98.3255%** Exposure
- `Libraries/Otterkit.Native/nativelib/memory.c` -> **97.0688%** Exposure
- `Libraries/Otterkit.Native/nativelib/u8console.c` -> **97.0688%** Exposure
- `Libraries/Otterkit.Native/nativelib/CASPAL.h` -> **43.507%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Libraries/Otterkit.Native/decNumber/decBasic.c` -> **100.0%** Exposure
- `Libraries/Otterkit.Native/decNumber/decCommon.c` -> **100.0%** Exposure
- `Libraries/Otterkit.Native/decNumber/decNumber.c` -> **100.0%** Exposure
- `Libraries/Otterkit.Native/decNumber/decPacked.c` -> **100.0%** Exposure
- `Libraries/Otterkit.Native/decNumber/decimal128.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Libraries/Otterkit.Native/nativelib/decNumber.c` -> **88** Orphaned Functions | **0** Duplicates
- `Libraries/Otterkit.Native/decNumber/decNumber.c` -> **49** Orphaned Functions | **0** Duplicates
- `Libraries/Otterkit.Native/decNumber/decContext.c` -> **14** Orphaned Functions | **0** Duplicates
- `Libraries/Otterkit.Native/decNumber/decimal128.c` -> **5** Orphaned Functions | **0** Duplicates
- `Libraries/Otterkit.Native/decNumber/decimal32.c` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `94` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Libraries/Otterkit.Native/decNumber/decNumber.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.386)
- **Top Global Matches:** file_cluster_8: 7.386, file_cluster_6: 12.303, file_cluster_4: 20.653
- **Magnitude:** 9222.0 | **LOC:** 8142 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **6**; blast radius 40.026; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.9%), Guard Balance (formerly Safety Score) (86.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decLnOp` **(Many-Argument Workhorses)** (Impact: 1218.7)
    * *Intent:* /* 3. Fastpaths are included for ln(10) and ln(2), up to length 40, */ /* as these are common reques...
  * `decDivideOp` **(Many-Argument Workhorses)** (Impact: 365.1)
    * *Intent:* /* exp=exp-1 */ /* end outer_loop */ /* exp=exp+1 -- set the proper exponent */ /* if have=0 then ge...
  * `decAddOp` **(Many-Argument Workhorses)** (Impact: 218.2)
    * *Intent:* /* overlap the A or B coefficient */ /* then the result must be calculated into a temporary buffer. ...
  * `decCompareOp` **(Many-Argument Workhorses)** (Impact: 203.4)
    * *Intent:* /* */ /* res is C, the result. C may be A and/or B (e.g., X=X?X) */ /* lhs is A */ /* rhs is B */ /*...
  * `decNumberPower` **(Many-Argument Workhorses)** (Impact: 192.9)
    * *Intent:* /* Mathematical function restrictions apply (see above); a NaN is */ /* returned with Invalid_operat...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 49 instances
* *Amplified Cascading Flux:* 1396 instances
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 4310
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1396`, `structural_boundaries: 514`, `args: 169`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 1518`, `dead_code: 19`, `fragile_debt: 4`, `unreferenced_by_name: 49`
* *Architecture:* `api: 67`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 202`, `cleanup: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.026
  * `Choke Point (Betweenness):` 0.002881 | `Ripple Effect (Closeness):` 0.272727
  * `Imports (Out-Degree: 3):` ctype.h, decNumber.h, decNumberLocal.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decBasic.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.077)
- **Top Global Matches:** file_cluster_6: 6.077, file_cluster_4: 8.906, file_cluster_8: 16.429
- **Magnitude:** 3628.16 | **LOC:** 3909 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 14.674; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.7%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decDivide` **(Many-Argument Workhorses)** (Impact: 301.6)
    * *Intent:* /* */ /* result gets the result of dividing dfl by dfr: */ /* dfl is the first decFloat (lhs) */ /* ...
  * `decFloatFMA` **(Many-Argument Workhorses)** (Impact: 187.3)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decFloatFMA -- multiply ...
  * `decFloatAdd` **(Many-Argument Workhorses)** (Impact: 139.6)
    * *Intent:* #endif
  * `decFloatQuantize` **(Many-Argument Workhorses)** (Impact: 134.5)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decFloatQuantize -- quan...
  * `decNumCompare` **(Many-Argument Workhorses)** (Impact: 129.6)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decNumCompare -- numeric...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 564 instances
* *State Mutation (weighted view):* 1813
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 646`, `structural_boundaries: 325`, `args: 88`, `func_start: 72`, `class_start: 13`
* *Risk/State:* `state_mutation: 685`, `dead_code: 20`
* *Architecture:* `api: 64`
* *Defense:* `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.045455
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decCommon.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.954)
- **Top Global Matches:** file_cluster_8: 5.954, file_cluster_6: 12.458, file_cluster_4: 21.107
- **Magnitude:** 1695.78 | **LOC:** 1836 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 29.475; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decFinalize` **(Many-Argument Workhorses)** (Impact: 178.6)
    * *Intent:* #endif
  * `decFloatFromString` **(Many-Argument Workhorses)** (Impact: 151.3)
    * *Intent:* /* coefficient it will be rounded. */ /* set is the context */ /* returns result */ /* */ /* The len...
  * `decFloatToEngString` **(Many-Argument Workhorses)** (Impact: 80.2)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decFloatToEngString -- c...
  * `decFloatToString` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decFloatToString -- conv...
  * `decFloatFromPackedChecked` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* /* exp is the in-range unbiased exponent, q, or a special value in */ /* the form returned by decFlo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 309 instances
* *State Mutation (weighted view):* 994
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 92`, `args: 25`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 376`, `dead_code: 19`, `fragile_debt: 2`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.475
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.090909
  * `Imports (Out-Degree: 0):` decDPD.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decimal64.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.585)
- **Top Global Matches:** file_cluster_3: 6.585, file_cluster_8: 20.373, file_cluster_6: 33.229
- **Magnitude:** 935.7 | **LOC:** 840 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 17.611; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decimal64FromNumber` **(Many-Argument Workhorses)** (Impact: 66.0)
    * *Intent:* /* ds is the target decimal64 */ /* dn is the source number (assumed valid) */ /* set is the context...
  * `decDigitsFromDPD` **(Many-Argument Workhorses)** (Impact: 51.9)
    * *Intent:* /* caller may pre-process leading zero declets. */ /* */ /* When doing the 'extra declet' case care ...
  * `decimal64ToString` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `decDigitsToDPD` **(Many-Argument Workhorses)** (Impact: 39.1)
    * *Intent:* // QUOT10 -- macro to return the quotient of unit u divided by 10**n #define QUOT10(u, n) ((((uInt)(...
  * `decimal64ToNumber` **(Many-Argument Workhorses)** (Impact: 32.6)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decimal64ToNumber -- con...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 654
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 30`, `args: 13`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 222`, `dead_code: 6`, `unreferenced_by_name: 5`
* *Architecture:* `api: 18`, `import: 7`
* *Defense:* `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.611
  * `Choke Point (Betweenness):` 0.002176 | `Ripple Effect (Closeness):` 0.094697
  * `Imports (Out-Degree: 5):` decDPD.h, decNumber.h, decNumberLocal.h, decimal64.h, stdio.h, string.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decimal128.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.532)
- **Top Global Matches:** file_cluster_8: 9.532, file_cluster_3: 16.444, file_cluster_6: 21.144
- **Magnitude:** 515.4 | **LOC:** 554 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 13.659; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decimal128FromNumber` **(Many-Argument Workhorses)** (Impact: 55.4)
    * *Intent:* /* ds is the target decimal128 */ /* dn is the source number (assumed valid) */ /* set is the contex...
  * `decimal128ToString` **(Many-Argument Workhorses)** (Impact: 53.0)
  * `decimal128ToNumber` **(Many-Argument Workhorses)** (Impact: 37.9)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decimal128ToNumber -- co...
  * `decimal128Show` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decimal128Show -- displa...
  * `decimal128FromString` **(Many-Argument Workhorses)** (Impact: 4.8)
    * *Intent:* /* to-number -- conversion from numeric string */ /* */ /* decimal128FromString(result, string, set)...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 105 instances
* *State Mutation (weighted view):* 327
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 18`, `args: 11`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 117`, `dead_code: 7`, `unreferenced_by_name: 5`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.659
  * `Choke Point (Betweenness):` 0.001647 | `Ripple Effect (Closeness):` 0.045455
  * `Imports (Out-Degree: 6):` decNumber.h, decNumberLocal.h, decimal128.h, stdio.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decimal32.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.767)
- **Top Global Matches:** file_cluster_8: 8.767, file_cluster_6: 10.15, file_cluster_4: 18.165
- **Magnitude:** 426.22 | **LOC:** 477 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decimal32FromNumber` **(Many-Argument Workhorses)** (Impact: 60.9)
    * *Intent:* /* ds is the target decimal32 */ /* dn is the source number (assumed valid) */ /* set is the context...
  * `decimal32ToString` **(Many-Argument Workhorses)** (Impact: 38.7)
  * `decimal32ToNumber` **(Compute Cores)** (Impact: 23.1)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decimal32ToNumber -- con...
  * `decimal32Show` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decimal32Show -- display...
  * `decimal32FromString` **(Many-Argument Workhorses)** (Impact: 4.8)
    * *Intent:* /* to-number -- conversion from numeric string */ /* */ /* decimal32FromString(result, string, set);...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 19`, `args: 11`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 89`, `dead_code: 6`, `unreferenced_by_name: 5`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` decNumber.h, decNumberLocal.h, decimal32.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Libraries/Otterkit.Native/nativelib/decNumber.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.562)
- **Top Global Matches:** file_cluster_15: 5.562, file_cluster_11: 7.453, file_cluster_2: 7.505
- **Magnitude:** 289.04 | **LOC:** 1038 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 84.312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `d128Compare` **(Parameter Forwarders)** (Impact: 4.1)
    * *Intent:* /* decQuad Comparisons */
  * `d64Compare` **(Parameter Forwarders)** (Impact: 4.1)
    * *Intent:* /* decDouble Comparisons */
  * `d128Pow` **(Parameter Forwarders)** (Impact: 2.7)
  * `d64Pow` **(Parameter Forwarders)** (Impact: 2.7)
  * `d128FMA` **(Parameter Forwarders)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 92`, `args: 92`, `func_start: 88`
* *Risk/State:* `unreferenced_by_name: 88`
* *Architecture:* `api: 88`, `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` decDouble.h, decQuad.h, decimal128.h, decimal64.h, ..\decNumber\decDouble.h, ..\decNumber\decimal64.h, CASPAL.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Libraries/Otterkit.Native/decNumber/decContext.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.164)
- **Top Global Matches:** file_cluster_6: 6.164, file_cluster_4: 12.005, file_cluster_8: 13.309
- **Magnitude:** 228.76 | **LOC:** 438 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **4**; blast radius 53.199; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.3%), Complexity Load (formerly Cognitive Load) (92.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decContextSetStatusFromString` **(Compute Cores)** (Impact: 29.5)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decContextSetStatusFromS...
  * `decContextSetStatusFromStringQuiet` **(Compute Cores)** (Impact: 29.5)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decContextSetStatusFromS...
  * `decContextStatusToString` **(Compute Cores)** (Impact: 23.9)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decContextStatusToString...
  * `decContextDefault` **(Many-Argument Workhorses)** (Impact: 14.9)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decContextDefault -- ini...
  * `decContextTestEndian` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decContextTestEndian -- ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 67`, `args: 17`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `state_mutation: 39`, `unreferenced_by_name: 14`
* *Architecture:* `api: 16`, `import: 4`
* *Defense:* `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 53.199
  * `Choke Point (Betweenness):` 0.006122 | `Ripple Effect (Closeness):` 0.29697
  * `Imports (Out-Degree: 2):` decContext.h, decNumberLocal.h, stdio.h, string.h
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decPacked.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.573)
- **Top Global Matches:** file_cluster_3: 6.573, file_cluster_8: 20.967, file_cluster_6: 33.892
- **Magnitude:** 222.48 | **LOC:** 221 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 13.278; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decPackedToNumber` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* /* scale, is converted to a decNumber. The BCD array is assumed full */ /* of digits, and must be en...
  * `decPackedFromNumber` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* /* second parameter. The final 4-bit nibble in the array will be a */ /* sign nibble, C (1100) for +...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 49`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.278
  * `Choke Point (Betweenness):` 0.000352 | `Ripple Effect (Closeness):` 0.022727
  * `Imports (Out-Degree: 4):` decNumber.h, decNumberLocal.h, decPacked.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/nativelib/allocator.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.049)
- **Top Global Matches:** file_cluster_7: 7.049, file_cluster_12: 7.716, file_cluster_5: 9.614
- **Magnitude:** 181.5 | **LOC:** 315 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%), Complexity Load (formerly Cognitive Load) (67.4%)
- **Documentation Coverage:** 84.312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VirtualPoolCreate` **(Compute Cores)** (Impact: 11.5)
  * `SmallAlloc` **(Defensive Guards)** (Impact: 10.9)
  * `VirtualPoolDecommit` **(Compute Cores)** (Impact: 9.1)
  * `SmallDealloc` **(Compute Cores)** (Impact: 7.1)
  * `AlignLengthToSizeClass` **(I/O & Config Routines)** (Impact: 5.6)
    * *Intent:* // Apparently, GCC can't optimize this function properly and generates a bunch of branches. // This ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 33`, `args: 11`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 40`, `unreferenced_by_name: 3`
* *Architecture:* `api: 11`, `import: 1`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` allocator.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Libraries/Otterkit.Native/nativelib/u8range.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.568)
- **Top Global Matches:** file_cluster_9: 5.568, file_cluster_15: 10.196, file_cluster_16: 10.451
- **Magnitude:** 174.38 | **LOC:** 337 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.1%), Guard Balance (formerly Safety Score) (66.9%)
- **Documentation Coverage:** 84.312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `u8ScalarAlgorithm` **(Many-Argument Workhorses)** (Impact: 27.7)
    * *Intent:* // Return 0 on success or 1-based index of first error char
  * `IsValidThreeByteSequence` **(Compute Cores)** (Impact: 22.8)
  * `IsValidFourByteSequence` **(Compute Cores)** (Impact: 22.4)
  * `u8RangeAlgorithm` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* #if defined(AMD64) // Return 0 on success or -1 on error
  * `IsValidTwoByteSequence` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* // | U+D000..U+D7FF | ED | 80..9F | 80..BF | | // +--------------------+------------+-------------+-...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 9`, `args: 6`, `func_start: 5`
* *Risk/State:* `state_mutation: 31`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CASPAL.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Libraries/Otterkit.Native/decNumber/decNumberLocal.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.177)
- **Top Global Matches:** file_cluster_17: 3.177, file_cluster_2: 4.799, file_cluster_15: 6.692
- **Magnitude:** 107.92 | **LOC:** 758 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **2**; blast radius 60.253; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.6%), Connectivity (formerly Api Exposure) (58.1%), Guard Balance (formerly Safety Score) (56.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 70`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.272727
  * `Imports (Out-Degree: 0):` stdlib.h, string.h
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decDouble.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 5.705)
- **Top Global Matches:** file_cluster_17: 5.705, file_cluster_2: 7.95, file_cluster_15: 8.196
- **Magnitude:** 98.18 | **LOC:** 156 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 18.267; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 34`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 81`, `import: 2`
* *Defense:* `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.267
  * `Choke Point (Betweenness):` 0.000705 | `Ripple Effect (Closeness):` 0.072727
  * `Imports (Out-Degree: 2):` decContext.h, decQuad.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decQuad.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 5.63)
- **Top Global Matches:** file_cluster_17: 5.63, file_cluster_2: 7.941, file_cluster_15: 8.278
- **Magnitude:** 96.4 | **LOC:** 178 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 31.7; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 34`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 79`, `import: 1`
* *Defense:* `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.7
  * `Choke Point (Betweenness):` 0.000705 | `Ripple Effect (Closeness):` 0.145455
  * `Imports (Out-Degree: 1):` decContext.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/nativelib/u8casefold.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.373)
- **Top Global Matches:** file_cluster_15: 5.373, file_cluster_2: 6.838, file_cluster_16: 7.827
- **Magnitude:** 87.76 | **LOC:** 1847 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (12.0%), Debt Markers (formerly Tech Debt) (8.0%)
- **Documentation Coverage:** 84.312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MappingSearch` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* // Memory and thread safety notes: // The trie is static and read-only, so it should be safe to use ...
  * `RuneLength` **(Compute Cores)** (Impact: 7.7)
  * `Casefold` **(Many-Argument Workhorses)** (Impact: 7.3)
  * `AsciiCasefold` **(Parameter Forwarders)** (Impact: 3.7)
  * `PopulationCount` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CASPAL.h, allocator.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Libraries/Otterkit.Native/nativelib/memory.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.89)
- **Top Global Matches:** file_cluster_7: 6.89, file_cluster_12: 8.884, file_cluster_5: 9.649
- **Magnitude:** 35.0 | **LOC:** 74 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Debt Markers (formerly Tech Debt) (97.1%), Complexity Load (formerly Cognitive Load) (73.1%), Guard Balance (formerly Safety Score) (64.6%)
- **Documentation Coverage:** 84.312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ottrkAlignedMove` **(Compute Cores)** (Impact: 10.2)
  * `ottrkAlignedFill` **(Compute Cores)** (Impact: 4.4)
  * `ottrkAlignedZeroFill` **(Compute Cores)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 6`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CASPAL.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Libraries/Otterkit.Native/decNumber/decContext.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 2.58)
- **Top Global Matches:** file_cluster_17: 2.58, file_cluster_2: 4.961, file_cluster_15: 6.667
- **Magnitude:** 34.54 | **LOC:** 255 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **3**; blast radius 160.392; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (73.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 16`, `class_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 160.392
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.349174
  * `Imports (Out-Degree: 0):` signal.h, stdint.h, stdio.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decSingle.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.804)
- **Top Global Matches:** file_cluster_17: 4.804, file_cluster_2: 7.561, file_cluster_15: 7.783
- **Magnitude:** 33.88 | **LOC:** 87 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 13.278; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 12`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 18`, `import: 3`
* *Defense:* `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.278
  * `Choke Point (Betweenness):` 0.001057 | `Ripple Effect (Closeness):` 0.022727
  * `Imports (Out-Degree: 3):` decContext.h, decDouble.h, decQuad.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/example6.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.29)
- **Top Global Matches:** file_cluster_12: 7.29, file_cluster_7: 8.644, file_cluster_2: 9.415
- **Magnitude:** 22.42 | **LOC:** 62 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (61.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 7.6)
    * *Intent:* /* ------------------------------------------------------------------ */ /* Decimal Number Library D...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` decPacked.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Libraries/Otterkit.Native/nativelib/allocator.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 2.802)
- **Top Global Matches:** file_cluster_17: 2.802, file_cluster_2: 3.402, file_cluster_13: 5.32
- **Magnitude:** 20.9 | **LOC:** 83 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 24.914; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (49.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 1`, `class_start: 5`
* *Risk/State:* None
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.914
  * `Choke Point (Betweenness):` 0.000529 | `Ripple Effect (Closeness):` 0.045455
  * `Imports (Out-Degree: 1):` CASPAL.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/example4.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.493)
- **Top Global Matches:** file_cluster_15: 5.493, file_cluster_17: 7.73, file_cluster_16: 7.97
- **Magnitude:** 19.22 | **LOC:** 62 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (60.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* // ...snip]
  * `signalHandler` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`, `args: 5`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` decNumber.h, setjmp.h, signal.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Libraries/Otterkit.Native/nativelib/CASPAL.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 5.423)
- **Top Global Matches:** file_cluster_17: 5.423, file_cluster_2: 6.889, file_cluster_11: 8.413
- **Magnitude:** 18.68 | **LOC:** 283 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 65.553; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (43.5%), Connectivity (formerly Api Exposure) (17.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`
* *Risk/State:* `safety_bypasses: 1`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 65.553
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.139205
  * `Imports (Out-Degree: 0):` arm_neon.h, immintrin.h, memoryapi.h, mman.h, windows.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decNumber.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 5.32)
- **Top Global Matches:** file_cluster_17: 5.32, file_cluster_2: 7.704, file_cluster_15: 8.188
- **Magnitude:** 17.12 | **LOC:** 183 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **1**; blast radius 96.841; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 14`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 87`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 96.841
  * `Choke Point (Betweenness):` 0.004757 | `Ripple Effect (Closeness):` 0.312771
  * `Imports (Out-Degree: 1):` decContext.h
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `Libraries/Otterkit.Native/decNumber/decDouble.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.244)
- **Top Global Matches:** file_cluster_17: 4.244, file_cluster_2: 5.332, file_cluster_15: 7.601
- **Magnitude:** 17.04 | **LOC:** 141 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` decBasic.c, decCommon.c, decContext.h, decDouble.h, decNumberLocal.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Libraries/Otterkit.Native/decNumber/decQuad.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.276)
- **Top Global Matches:** file_cluster_17: 4.276, file_cluster_2: 5.374, file_cluster_15: 7.618
- **Magnitude:** 16.94 | **LOC:** 136 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.951; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` decBasic.c, decCommon.c, decContext.h, decNumberLocal.h, decQuad.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Libraries/Otterkit.Native/decNumber/example3.c` (C) | Magnitude: 16.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, pointers: 37, structural_boundaries: 4, debug_prints: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Libraries/Otterkit.Native/decNumber/example5.c` (C) | Magnitude: 13.86 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 20, pointers: 8, branch: 2, structural_boundaries: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Libraries/Otterkit.Native/decNumber/decContext.c` -> **Severity: 0.612** (Bridge: 0.0061 * Flux: 99.999%)
- `Libraries/Otterkit.Native/decNumber/decNumber.c` -> **Severity: 0.288** (Bridge: 0.0029 * Flux: 100.0%)
- `Libraries/Otterkit.Native/decNumber/decimal64.c` -> **Severity: 0.218** (Bridge: 0.0022 * Flux: 100.0%)
- `Libraries/Otterkit.Native/decNumber/decimal128.c` -> **Severity: 0.165** (Bridge: 0.0016 * Flux: 100.0%)
- `Libraries/Otterkit.Native/decNumber/decPacked.c` -> **Severity: 0.035** (Bridge: 0.0004 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Libraries/Otterkit.Native/decNumber/decNumber.c` -> **Severity: 23.543** (Embedded: 0.2727 * Error Risk: 86.3235%)
- `Libraries/Otterkit.Native/decNumber/decContext.c` -> **Severity: 19.699** (Embedded: 0.297 * Error Risk: 66.3317%)
- `Libraries/Otterkit.Native/decNumber/decNumberLocal.h` -> **Severity: 15.475** (Embedded: 0.2727 * Error Risk: 56.7416%)
- `Libraries/Otterkit.Native/decNumber/decimal64.c` -> **Severity: 8.721** (Embedded: 0.0947 * Error Risk: 92.093%)
- `Libraries/Otterkit.Native/decNumber/decCommon.c` -> **Severity: 7.75** (Embedded: 0.0909 * Error Risk: 85.2494%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Libraries/Otterkit.Native/decNumber/decContext.c` -> **Severity: 5319.9** (Blast Radius: 53.199 * Doc Risk: 100.0%)
- `Libraries/Otterkit.Native/decNumber/decNumber.c` -> **Severity: 4002.6** (Blast Radius: 40.026 * Doc Risk: 100.0%)
- `Libraries/Otterkit.Native/decNumber/decCommon.c` -> **Severity: 2947.5** (Blast Radius: 29.475 * Doc Risk: 100.0%)
- `Libraries/Otterkit.Native/decNumber/decimal64.c` -> **Severity: 1761.1** (Blast Radius: 17.611 * Doc Risk: 100.0%)
- `Libraries/Otterkit.Native/decNumber/decBasic.c` -> **Severity: 1467.4** (Blast Radius: 14.674 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 78 literal sites + 5 sites through wrappers = 83

- `SystemAlloc` (macro, memory_alloc, primitive): 3 call sites in 1 files -- `Libraries/Otterkit.Native/nativelib/CASPAL.h`
- `SystemCommit` (macro, memory_alloc, primitive): 1 call sites in 1 files -- `Libraries/Otterkit.Native/nativelib/CASPAL.h`
- `SystemDecommit` (macro, memory_alloc, primitive): 1 call sites in 1 files -- `Libraries/Otterkit.Native/nativelib/CASPAL.h`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1531 call pairs -- scoped 35.6%, unique 14.9%, ambiguous 0.5%, external 49.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 1531 | 35.6% | 14.9% | 0.5% | 49.1% |

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
