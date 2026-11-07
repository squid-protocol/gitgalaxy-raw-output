# ARCHITECTURAL_BRIEF: cics-event-consumer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cicsdev/cics-event-consumer` |
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
- **Scope:** 50 analyzed artifact(s), 5397 LOC.
- **Load-bearing artifact:** `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` -- 9 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` -- pulls in 48 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` at magnitude 1997.2 (structural weight, not risk).
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
| Total Artifacts | 85 |
| Analyzed Artifacts (Scanned) | 50 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 35 |
| Total LOC | 5397 |
| Volatility Index | 0.02 |
| % Scanned of codebase = | 58.8% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4233 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4557 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3966 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 25 | 5096 | 50.0% |
| XML | 10 | 0 | 20.0% |
| PLAINTEXT | 5 | 0 | 10.0% |
| MARKDOWN | 4 | 0 | 8.0% |
| COBOL | 4 | 228 | 8.0% |
| SHELL | 1 | 22 | 2.0% |
| HTML | 1 | 51 | 2.0% |

## 4.1 SOURCE ENCODINGS
All 50 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Large Core Modules (3) 20%, Interface Declarations Files 10%, Large Core Modules (2) 8%, Many-Argument Workhorses Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 41 | 82.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 18.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 35*

**Composition by Extension & Reason:**
- `.md`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.java`: 1x Excluded (Machine-Generated Source Code Signature: 1042 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1170 LOC)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.mf`: 1x Excluded (Unsupported Extension: '.MF')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 77.9 | 15.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.2 | 43.1 | 53.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 29.1 | 17.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 44.7 | 4.6 | 2.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.4 | 3.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 56.0 | 2.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 24.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 40 | 7 | 2 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` |
| cleanup | 10 | 4 | 0 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| guards | 625 | 23 | 35 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| danger | 522 | 20 | 17 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| concurrency | 15 | 7 | 2 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Email.java` |
| connectivity | 330 | 29 | 17 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` |
| io | 38 | 8 | 2 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/ConvertFOP.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 18 | 4 | 0 | `examples/CA1YCOB3.cbl` |
| time | 1 | 1 | 0 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSHTTP.java` |
| serialization | 10 | 4 | 0 | `examples/CA1YCOB3.cbl` |
| regex | 21 | 5 | 0 | `examples/CA1YCOB3.cbl` |
| events | 51 | 11 | 3 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| tests | 0 | 0 | 0 | - |
| docs | 426 | 23 | 21 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` |
| debt | 54 | 12 | 2 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| mutation | 1652 | 28 | 55 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| dead_code | 187 | 26 | 8 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` |
| credential | 5 | 2 | 0 | `examples/ca1y.sh` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 10 | 4 | 0 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/ConvertFOP.java` (Hits: 19)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` (Hits: 6)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/MVSJob.java` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **EmitProperties.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java`) — 9 inbound connections
2. **Util.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Util.java`) — 3 inbound connections
3. **Epde_epde__item.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java`) — 2 inbound connections
4. **CHANGELOG.md** (`CHANGELOG.md`) — 1 inbound connections
5. **README.md** (`README.md`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Emit.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) — 48 outbound dependencies
2. **Event.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/Event.java`) — 22 outbound dependencies
3. **SUMMARY.md** (`SUMMARY.md`) — 20 outbound dependencies
4. **ConvertFOP.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/ConvertFOP.java`) — 19 outbound dependencies
5. **Email.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Email.java`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolveTokensInKey` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **406.8** | LOC: 727
  * *Intent:* * - The string to search for tokens * @param pattern * - The pattern to use to find tokens * @param props * - The properties to use as the lookup tabl...
- `addPropertiesFromDFHEP_DESCRIPTOR` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **195.0** | LOC: 367
  * *Intent:* /** * Add name / value properties from contents of container DFHEP.DESCRIPTOR and business information items from * containers DFHEP.DATA.nnnnn * * @p...
- `getFileUsingFTP` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **159.5** | LOC: 170
  * *Intent:* * @param trustmgr * - * @param datatimeout * - * @param proxyserver * - * @param proxyusername * - * @param proxypassword * - * @param anonymouspasswo...
- `evaluateFormula` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPAPv1.java`) -> Impact: **62.0** | LOC: 96
  * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more arguments, and the first argument refers to a level...
- `evaluateFormula` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java`) -> Impact: **62.0** | LOC: 96
  * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more arguments, and the first argument refers to a level...
- `evaluateFormula` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java`) -> Impact: **62.0** | LOC: 96
  * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more arguments, and the first argument refers to a level...
- `callAdapters` **(Compute Cores)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **59.7** | LOC: 147
  * *Intent:* /** * Call a set of adapters in a pre-defined sequence providing the properties required by the adapter are present. * * @param props * - properties t...
- `emit` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **53.7** | LOC: 154
  * *Intent:* /** * Emit a message using configuration from a set of properties, and data from the CICS channel. * * @param props * - properties to use * @param cic...
- `send` **(I/O & Config Routines)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSHTTP.java`) -> Impact: **48.5** | LOC: 230
- `getHtmlTable` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **47.0** | LOC: 108
  * *Intent:* /** * Return an HTML document containing a table of properties and containers that match the provided regular * expressions. * * @param props * - prop...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y` | 15 | 3317.44 | 27.85% | 33.83% |
| `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface` | 3 | 1006.52 | 37.61% | 98.82% |
| `examples` | 10 | 106.52 | 5.4% | 0.0% |
| `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe` | 5 | 93.92 | 1.06% | 66.88% |
| `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web` | 3 | 69.54 | 8.35% | 18.93% |
| `examples/schemas` | 4 | 42.08 | 0.0% | 0.0% |
| `cics-event-consumer-ca1y/WebContent/WEB-INF` | 2 | 21.04 | 0.0% | 0.0% |
| `__monolith__` | 5 | 15.96 | 0.0% | 0.0% |
| `cics-event-consumer-bundle` | 1 | 10.52 | 0.0% | 0.0% |
| `cics-event-consumer-ca1y` | 1 | 10.52 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/ContextInfoType.java` -> **100.0%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` -> **99.9981%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPAPv1.java` -> **99.9257%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/Event.java` -> **99.593%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/ObjectFactory.java` -> **97.0688%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSHTTP.java` -> **99.9999%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Util.java` -> **99.9994%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSFile.java` -> **99.9992%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/Event.java` -> **99.9873%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java` -> **99.9801%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` -> **62** Orphaned Functions | **0** Duplicates
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPAPv1.java` -> **36** Orphaned Functions | **0** Duplicates
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java` -> **24** Orphaned Functions | **0** Duplicates
- `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/ContextInfoType.java` -> **14** Orphaned Functions | **0** Duplicates
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Util.java` -> **8** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `253` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 13.437)
- **Top Global Matches:** file_cluster_8: 13.437, file_cluster_6: 14.848, file_cluster_4: 21.586
- **Magnitude:** 1997.2 | **LOC:** 3009 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **48**; blast radius 18.54; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.9%), Connectivity (formerly Api Exposure) (6.6%)
- **Documentation Coverage:** 5.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveTokensInKey` **(Many-Argument Workhorses)** (Impact: 406.8)
    * *Intent:* * - The string to search for tokens * @param pattern * - The pattern to use to find tokens * @param ...
  * `addPropertiesFromDFHEP_DESCRIPTOR` **(Many-Argument Workhorses)** (Impact: 195.0)
    * *Intent:* /** * Add name / value properties from contents of container DFHEP.DESCRIPTOR and business informati...
  * `getFileUsingFTP` **(Many-Argument Workhorses)** (Impact: 159.5)
    * *Intent:* * @param trustmgr * - * @param datatimeout * - * @param proxyserver * - * @param proxyusername * - *...
  * `callAdapters` **(Compute Cores)** (Impact: 59.7)
    * *Intent:* /** * Call a set of adapters in a pre-defined sequence providing the properties required by the adap...
  * `emit` **(Many-Argument Workhorses)** (Impact: 53.7)
    * *Intent:* /** * Emit a message using configuration from a set of properties, and data from the CICS channel. *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 249 instances
* *State Mutation (weighted view):* 794
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 443`, `structural_boundaries: 219`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 207`, `high_risk_execution: 1`, `state_mutation: 296`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 11`, `import: 46`
* *Defense:* `safety: 117`, `doc: 42`, `immutability_locks: 46`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.54
  * `Choke Point (Betweenness):` 0.005315 | `Ripple Effect (Closeness):` 0.020408
  * `Imports (Out-Degree: 14):` com.fasterxml.jackson.databind.ObjectMapper, com.ibm.cics.ca1y.epadapterinterface.*, com.ibm.cics.server.*, com.ibm.cics.server.invocation.CICSProgram, com.ibm.etools.marshall.util.MarshallExternalDecimalUtils, com.ibm.etools.marshall.util.MarshallFloatUtils, com.ibm.etools.marshall.util.MarshallIntegerUtils, com.ibm.etools.marshall.util.MarshallPackedDecimalUtils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.636)
- **Top Global Matches:** file_cluster_12: 7.636, file_cluster_7: 7.931, file_cluster_5: 9.544
- **Magnitude:** 375.56 | **LOC:** 885 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 28.81; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluateFormula` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more a...
  * `wrappedGetNumber` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* /** * @generated * wrappedGetNumber */
  * `match` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * @generated */
  * `evaluateMap` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /** * @generated * evaluateMap */
  * `setEpde__dataname` **(Compute Cores)** (Impact: 4.8)
    * *Intent:* /** * @generated */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 111`, `args: 69`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 41`, `unreferenced_by_name: 62`
* *Architecture:* `io: 2`, `api: 70`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 13`, `doc: 76`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.81
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.045918
  * `Imports (Out-Degree: 0):` com.ibm.etools.marshall.util.*, java.beans.BeanInfo, java.beans.IntrospectionException, java.beans.Introspector, java.beans.PropertyDescriptor, java.lang.reflect.Method
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.794)
- **Top Global Matches:** file_cluster_12: 7.794, file_cluster_7: 7.88, file_cluster_5: 9.557
- **Magnitude:** 327.54 | **LOC:** 694 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 15.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluateFormula` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more a...
  * `setEpde__item` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* /** * @generated */
  * `wrappedGetNumber` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* /** * @generated * wrappedGetNumber */
  * `match` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * @generated */
  * `evaluateMap` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /** * @generated * evaluateMap */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 91`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 46`, `unreferenced_by_name: 24`
* *Architecture:* `io: 2`, `api: 40`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 13`, `doc: 46`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 1):` com.ibm.etools.marshall.util.*, java.beans.BeanInfo, java.beans.IntrospectionException, java.beans.Introspector, java.beans.PropertyDescriptor, java.lang.reflect.Method
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPAPv1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.883)
- **Top Global Matches:** file_cluster_7: 7.883, file_cluster_12: 8.24, file_cluster_5: 9.7
- **Magnitude:** 303.42 | **LOC:** 673 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 15.573; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluateFormula` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more a...
  * `wrappedGetNumber` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* /** * @generated * wrappedGetNumber */
  * `match` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * @generated */
  * `evaluateMap` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /** * @generated * evaluateMap */
  * `setEpap__strucid` **(Compute Cores)** (Impact: 4.8)
    * *Intent:* /** * @generated */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 82`, `args: 43`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 38`, `unreferenced_by_name: 36`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 13`, `doc: 50`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 0):` com.ibm.etools.marshall.util.*, java.beans.BeanInfo, java.beans.IntrospectionException, java.beans.Introspector, java.beans.PropertyDescriptor, java.lang.reflect.Method
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 9.707)
- **Top Global Matches:** file_cluster_14: 9.707, file_cluster_5: 9.85, file_cluster_7: 10.838
- **Magnitude:** 273.92 | **LOC:** 725 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **9**; blast radius 104.749; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (84.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (44.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPropertySummary` **(Compute Cores)** (Impact: 19.3)
    * *Intent:* /** * Summary of property. * * @param props * @param key * @return summary of the properties */
  * `setPropertyMimeDefault` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* /** * Associate the property with a MIME associated with the provided file name. * * @param key * - ...
  * `setPropertyAttachment` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* /** * Associate the property key with an attachment. * * @param key * - property key * @param attach...
  * `setPropertyAlternateName` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* /** * Associate the property key with an alternate name. * * @param key * - property key * @param at...
  * `setPropertyReturnContainer` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* /** * Associate the property key with the name of a container. * * @param key * - property key * @pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 84`, `args: 28`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 26`
* *Architecture:* `api: 33`, `concurrency: 1`, `import: 9`
* *Defense:* `doc: 46`, `sync_locks: 1`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 104.749
  * `Choke Point (Betweenness):` 0.002764 | `Ripple Effect (Closeness):` 0.183673
  * `Imports (Out-Degree: 1):` java.net.FileNameMap, java.net.URLConnection, java.util.Collections, java.util.Enumeration, java.util.Hashtable, java.util.LinkedHashMap, java.util.Map, java.util.Properties...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSHTTP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 13.343)
- **Top Global Matches:** file_cluster_8: 13.343, file_cluster_6: 14.271, file_cluster_4: 20.857
- **Magnitude:** 167.78 | **LOC:** 380 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 15.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.5%), Complexity Load (formerly Cognitive Load) (38.6%), Debt Markers (formerly Tech Debt) (17.3%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 48.5)
  * `getMessageSummary` **(I/O & Config Routines)** (Impact: 9.8)
    * *Intent:* /** * Return a short summary of the contents to be written to the queue. * * @return short summary o...
  * `CICSHTTP` **(State Mutators)** (Impact: 1.6)
  * `validForEmission` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit * * @return true if the entries in EmitProperties are...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 29`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 35`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 16`, `doc: 13`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.HttpClientRequest, com.ibm.cics.server.HttpClientResponse, com.ibm.cics.server.HttpSession, com.ibm.cics.server.IOErrorException, com.ibm.cics.server.TimedOutException, java.net.URI, java.util.logging.Level, java.util.logging.Logger...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Util.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.484)
- **Top Global Matches:** file_cluster_7: 7.484, file_cluster_12: 8.157, file_cluster_5: 9.674
- **Magnitude:** 154.58 | **LOC:** 357 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 111.237; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getHexDump` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* /** * Return a string of hexadecimal of byteArray with line separators suitable for trace. * * @para...
  * `getChunks` **(Defensive Guards)** (Impact: 13.9)
    * *Intent:* /** * Return an 2 dimensional array. The first ordinal is the number of chunks * the supplied string...
  * `getChunks` **(Defensive Guards)** (Impact: 13.9)
    * *Intent:* /** * Return an 2 dimensional array. The first ordinal is the number of chunks * the supplied byte a...
  * `loadProperties` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /* * Add name / value properties from the byte array. * * @param props - The properties to add to. *...
  * `getOptions` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* /** * Extract the command options from a string into an array. * * @param commandLine * - String in ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 44`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 20`, `unreferenced_by_name: 8`
* *Architecture:* `api: 12`, `import: 8`
* *Defense:* `safety: 10`, `doc: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 111.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.120048
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.IsCICS, com.ibm.jzos.RcException, java.io.StringReader, java.util.Arrays, java.util.Date, java.util.Properties, javax.xml.bind.DatatypeConverter, org.apache.commons.io.IOUtils
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Email.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.295)
- **Top Global Matches:** file_cluster_6: 12.295, file_cluster_4: 13.388, file_cluster_7: 16.624
- **Magnitude:** 124.16 | **LOC:** 367 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 15.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Concurrency Surface (formerly Concurrency) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 22.7)
    * *Intent:* /** * Send a mail using the information in properties. * * @return boolean - true if the mail was su...
  * `addAttachments` **(Stateful Encapsulated Methods)** (Impact: 13.4)
    * *Intent:* /** * Add attachments in the properties to the multipart message. * * @param multipart * - The multi...
  * `addBody` **(Stateful Encapsulated Methods)** (Impact: 8.1)
    * *Intent:* /** * Add property mail.content to to the multipart message. * * @param multipart * - The multipart ...
  * `getMessageSummary` **(Stateful Encapsulated Methods)** (Impact: 5.1)
    * *Intent:* /** * Return a short text summary of the mail. * * @return short summary of the mail. */
  * `Email` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * @author Mark Cocker <mark_cocker@uk.ibm.com> * @version 1.0 * @since 2012-02-10 * @param p * -...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 45`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 20`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 18`
* *Defense:* `safety: 6`, `doc: 21`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 2):` java.util.Date, java.util.Enumeration, java.util.logging.Level, java.util.logging.Logger, javax.activation.DataHandler, javax.mail.Authenticator, javax.mail.BodyPart, javax.mail.Message...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/MVSWriteToOperator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.778)
- **Top Global Matches:** file_cluster_8: 9.778, file_cluster_6: 18.315, file_cluster_3: 21.508
- **Magnitude:** 115.44 | **LOC:** 247 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 15.573; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.2%), Debt Markers (formerly Tech Debt) (27.2%)
- **Documentation Coverage:** 22.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDescriptorCode` **(Compute Cores)** (Impact: 42.3)
    * *Intent:* /** * Return an int representing the provided descriptor code. * * @param route * - number or string...
  * `getRouteCode` **(Compute Cores)** (Impact: 39.3)
    * *Intent:* /** * Return an int representing the provided route code. * * @param route * - number or string cons...
  * `send` **(I/O & Config Routines)** (Impact: 5.3)
  * `getMessageSummary` **(Stateful Encapsulated Methods)** (Impact: 3.6)
    * *Intent:* /** * Return a short summary of the WTO message. * * @return short summary of the WTO message. */
  * `MVSWriteToOperator` **(State Mutators)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 45`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 6`, `doc: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 0):` com.ibm.jzos.MvsConsole, com.ibm.jzos.WtoConstants, com.ibm.jzos.WtoMessage, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSQueue.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 14.56)
- **Top Global Matches:** file_cluster_8: 14.56, file_cluster_6: 15.557, file_cluster_4: 21.966
- **Magnitude:** 104.98 | **LOC:** 283 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 15.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (32.3%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 25.1)
  * `CICSQueue` **(Defensive Guards)** (Impact: 19.1)
  * `getMessageSummary` **(Stateful Encapsulated Methods)** (Impact: 7.2)
    * *Intent:* /** * Return a short summary of the contents to be written to the queue. * * @return short summary o...
  * `validForEmission` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit * * @return true if the entries in EmitProperties are...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 15`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 6`, `doc: 13`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.*, java.util.Arrays, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSFile.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 10.858)
- **Top Global Matches:** file_cluster_7: 10.858, file_cluster_12: 11.216, file_cluster_5: 12.015
- **Magnitude:** 86.44 | **LOC:** 209 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 14.447; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.1%), Debt Markers (formerly Tech Debt) (42.7%), Complexity Load (formerly Cognitive Load) (36.3%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 13.8)
  * `CICSFile` **(Defensive Guards)** (Impact: 13.0)
  * `getMessageSummary` **(Encapsulated Accessors)** (Impact: 1.6)
    * *Intent:* /** * Return a short summary of the contents to be written to the file. * * @return short summary of...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 14`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`, `import: 2`
* *Defense:* `safety: 6`, `doc: 12`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.*, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/JZOSFile.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 13.527)
- **Top Global Matches:** file_cluster_8: 13.527, file_cluster_6: 14.352, file_cluster_4: 20.892
- **Magnitude:** 74.92 | **LOC:** 257 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 15.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Guard Balance (formerly Safety Score) (70.4%), Debt Markers (formerly Tech Debt) (26.3%), Complexity Load (formerly Cognitive Load) (21.1%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 26.9)
  * `getMessageSummary` **(Stateful Encapsulated Methods)** (Impact: 7.1)
    * *Intent:* /** * Return a short summary of the contents to be written to the queue. * * @return short summary o...
  * `JZOSFile` **(State Mutators)** (Impact: 1.6)
  * `validForEmission` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit * * @return true if the entries in EmitProperties are...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 11`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 12`, `doc: 10`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 1):` com.ibm.jzos.ZFile, com.ibm.jzos.ZFileConstants, com.ibm.jzos.ZFileException, java.util.Arrays, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/ConvertFOP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.622)
- **Top Global Matches:** file_cluster_7: 9.622, file_cluster_5: 10.483, file_cluster_12: 10.719
- **Magnitude:** 65.72 | **LOC:** 207 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 15.573; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (23.6%), Debt Markers (formerly Tech Debt) (15.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 14.6)
    * *Intent:* /** * Minimal test harness to convert a FO file to a PDF using the Java * command line. * * @param a...
  * `convertFOP` **(Many-Argument Workhorses)** (Impact: 12.7)
    * *Intent:* /** * Convert an XML or FO input stream to an output stream based on the specified xslt and target M...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 35`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 12`, `unreferenced_by_name: 1`
* *Architecture:* `io: 19`, `api: 4`, `import: 19`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 0):` java.io.BufferedOutputStream, java.io.File, java.io.FileInputStream, java.io.FileOutputStream, java.io.InputStream, java.io.OutputStream, java.util.Arrays, java.util.List...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/Event.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 12.898)
- **Top Global Matches:** file_cluster_5: 12.898, file_cluster_7: 13.17, file_cluster_9: 13.844
- **Magnitude:** 64.0 | **LOC:** 178 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 14.447; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (25.0%), Debt Markers (formerly Tech Debt) (19.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createEvent` **(Many-Argument Workhorses)** (Impact: 30.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 31`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 5`, `import: 22`
* *Defense:* `safety: 3`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.ibm.cics.ca1y.Emit, com.ibm.cics.ca1y.EmitProperties, java.io.StringReader, java.util.Iterator, java.util.List, java.util.ResourceBundle, java.util.logging.Level, java.util.logging.Logger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/JavaHTTP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.95)
- **Top Global Matches:** file_cluster_8: 12.95, file_cluster_6: 13.57, file_cluster_4: 20.127
- **Magnitude:** 58.3 | **LOC:** 269 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 15.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.8%), Guard Balance (formerly Safety Score) (58.0%), Debt Markers (formerly Tech Debt) (28.9%), Concurrency Surface (formerly Concurrency) (18.7%)
- **Documentation Coverage:** 37.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 21.8)
  * `getMessageSummary` **(Stateful Encapsulated Methods)** (Impact: 3.8)
    * *Intent:* /** * Return a short summary of the contents to be sent to the HTTP server. * * @return String */
  * `JavaHTTP` **(State Mutators)** (Impact: 1.6)
  * `validForEmission` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit using this class. * * @return boolean */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 23`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 8`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 10`, `doc: 17`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 1):` java.io.IOException, java.io.InputStream, java.nio.charset.StandardCharsets, java.util.Enumeration, java.util.logging.Level, java.util.logging.Logger, javax.ws.rs.client.Client, javax.ws.rs.client.ClientBuilder...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/ContextInfoType.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.434)
- **Top Global Matches:** file_cluster_11: 5.434, file_cluster_13: 6.571, file_cluster_15: 6.778
- **Magnitude:** 49.42 | **LOC:** 241 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 20.587; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (78.3%), Guard Balance (formerly Safety Score) (52.1%), Connectivity (formerly Api Exposure) (8.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setEventname` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the eventname property. * * @param value * allowed object is * {@link String...
  * `setUsertag` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the usertag property. * * @param value * allowed object is * {@link String }...
  * `setNetworkapplid` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the networkapplid property. * * @param value * allowed object is * {@link St...
  * `setTimestamp` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the timestamp property. * * @param value * allowed object is * {@link XMLGre...
  * `setBindingname` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the bindingname property. * * @param value * allowed object is * {@link Stri...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 14`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.587
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020408
  * `Imports (Out-Degree: 0):` javax.xml.bind.annotation.XmlAccessType, javax.xml.bind.annotation.XmlAccessorType, javax.xml.bind.annotation.XmlElement, javax.xml.bind.annotation.XmlSchemaType, javax.xml.bind.annotation.XmlType, javax.xml.datatype.XMLGregorianCalendar
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/XMPP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.041)
- **Top Global Matches:** file_cluster_12: 7.041, file_cluster_11: 9.179, file_cluster_15: 9.206
- **Magnitude:** 47.68 | **LOC:** 158 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 14.447; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (66.6%), Dead Code Surface (formerly Dead Code) (56.0%), Guard Balance (formerly Safety Score) (53.7%), Mutation Surface (formerly State Flux) (48.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 9.0)
  * `XMPP` **(Defensive Guards)** (Impact: 3.3)
  * `destroy` **(Interface Declarations)** (Impact: 2.2)
  * `processMessage` **(Parameter Forwarders)** (Impact: 1.9)
  * `getMessageSummary` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 27`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `dead_code: 5`, `unreferenced_by_name: 3`
* *Architecture:* `api: 17`, `import: 11`
* *Defense:* `safety: 4`, `doc: 3`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.Properties, java.util.logging.Level, java.util.logging.Logger, org.jivesoftware.smack.Chat, org.jivesoftware.smack.ChatManager, org.jivesoftware.smack.ConnectionConfiguration, org.jivesoftware.smack.MessageListener, org.jivesoftware.smack.XMPPConnection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/MVSJob.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.569)
- **Top Global Matches:** file_cluster_12: 7.569, file_cluster_7: 8.62, file_cluster_5: 9.719
- **Magnitude:** 34.48 | **LOC:** 141 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 15.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Debt Markers (formerly Tech Debt) (59.8%), Guard Balance (formerly Safety Score) (57.9%), Complexity Load (formerly Cognitive Load) (25.7%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 9.8)
  * `MVSJob` **(State Mutators)** (Impact: 1.6)
  * `validForEmission` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit * * @return true if the entries in EmitProperties are...
  * `getMessageSummary` **(Encapsulated Accessors)** (Impact: 1.1)
    * *Intent:* /** * Return a short summary of the MVS job. * * @return short summary of the MVS job. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 4`, `import: 6`
* *Defense:* `safety: 4`, `doc: 9`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 1):` com.ibm.jzos.MvsJobSubmitter, java.io.IOException, java.util.Scanner, java.util.StringTokenizer, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/ca1y.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 3.918)
- **Top Global Matches:** file_cluster_7: 3.918, file_cluster_12: 8.136, file_cluster_14: 8.463
- **Magnitude:** 32.54 | **LOC:** 68 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (54.0%), Connectivity (formerly Api Exposure) (7.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/CA1YCOB3.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.439)
- **Top Global Matches:** file_cluster_11: 6.439, file_cluster_2: 7.016, file_cluster_17: 8.145
- **Magnitude:** 20.88 | **LOC:** 141 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.8%), Connectivity (formerly Api Exposure) (1.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Main-program` **(I/O & Config Routines)** (Impact: 2.0)
  * `Main-program-exit` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/emailTemplate.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.903)
- **Top Global Matches:** file_cluster_13: 4.903, file_cluster_2: 5.634, file_cluster_17: 6.258
- **Magnitude:** 16.02 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 3`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/Event.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.465)
- **Top Global Matches:** file_cluster_11: 5.465, file_cluster_13: 6.421, file_cluster_15: 6.851
- **Magnitude:** 15.0 | **LOC:** 100 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 18.54; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.6%), Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (31.0%), Connectivity (formerly Api Exposure) (7.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setContextInfo` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the contextInfo property. * * @param value * allowed object is * {@link Cont...
  * `setPayloadData` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the payloadData property. * * @param value * allowed object is * {@link Payl...
  * `getContextInfo` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* /** * Gets the value of the contextInfo property. * * @return * possible object is * {@link ContextI...
  * `getPayloadData` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* /** * Gets the value of the payloadData property. * * @return * possible object is * {@link PayloadD...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.54
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020408
  * `Imports (Out-Degree: 0):` javax.xml.bind.annotation.XmlAccessType, javax.xml.bind.annotation.XmlAccessorType, javax.xml.bind.annotation.XmlElement, javax.xml.bind.annotation.XmlRootElement, javax.xml.bind.annotation.XmlType
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/package-info.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.673)
- **Top Global Matches:** file_cluster_13: 4.673, file_cluster_2: 6.019, file_cluster_17: 7.113
- **Magnitude:** 11.04 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-bundle/pom.xml` (XML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 19.758; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.758
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027211
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/WebContent/WEB-INF/ibm-web-ext.xml` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java` (JAVA) | Magnitude: 327.54 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 402, core_var_decl: 110, structural_boundaries: 91, design_snake_case: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitAdapter.java` (JAVA) | Magnitude: 3.18 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` (JAVA) | Magnitude: 273.92 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 284, structural_boundaries: 84, safety_bypasses: 65, branch: 57

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` -> **Severity: 0.276** (Bridge: 0.0028 * Flux: 99.925%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` -> **Severity: 15.457** (Embedded: 0.1837 * Error Risk: 84.1525%)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Util.java` -> **Severity: 8.887** (Embedded: 0.12 * Error Risk: 74.0252%)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` -> **Severity: 2.999** (Embedded: 0.0459 * Error Risk: 65.3104%)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSQueue.java` -> **Severity: 2.177** (Embedded: 0.0272 * Error Risk: 80.0%)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/ConvertFOP.java` -> **Severity: 2.177** (Embedded: 0.0272 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/XMPP.java` -> **Severity: 1444.7** (Blast Radius: 14.447 * Doc Risk: 100.0%)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/Event.java` -> **Severity: 1444.7** (Blast Radius: 14.447 * Doc Risk: 100.0%)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/EventConfig.java` -> **Severity: 1444.7** (Blast Radius: 14.447 * Doc Risk: 100.0%)
- `examples/CA1YCOB1.cbl` -> **Severity: 1444.7** (Blast Radius: 14.447 * Doc Risk: 100.0%)
- `examples/CA1YCOB2.cbl` -> **Severity: 1444.7** (Blast Radius: 14.447 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `7` files carry mainframe facts -- `6` call sites, `0` dataset bindings, `44` record items.

- **CICS operations:** `40` EXEC CICS operations naming a resource (`4` CHANNEL, `26` CONTAINER, `4` FILE, `6` QUEUE); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

### `examples/CA1YCOB3.cbl` (COBOL)
- **Calls:** `LINK CA1Y`
- **Record layouts (11 items):** `CONFIG (7)`, `WORKAREA (3)`, `CR (1)`
- **CICS operations:** `CONTAINER CA1Y (write)`, `CONTAINER TO (write)`, `CONTAINER SUBJECT (write)`, `CONTAINER CONTENT (write)`, `CONTAINER ATTACH1 (write)`, `CHANNEL CA1Y (pass)`
- **Compiler options:** `arith(extend)`, `trunc(bin)`
- **Data moves:** 41 (MOVE 5, STRING 36); most-fed items `WORKAREA-DATA`

### `examples/CA1YCOB4.cbl` (COBOL)
- **Calls:** `LINK CA1Y`
- **Record layouts (14 items):** `CONFIG (5)`, `PDF-DOC (4)`, `RESPONSE (4)`, `CR (1)`
- **CICS operations:** `CONTAINER CA1Y (write)`, `CHANNEL MyChannel (pass)`, `CONTAINER CA1YRESPONSE (read)`, `CONTAINER PDF (read)`
- **Compiler options:** `arith(extend)`, `trunc(bin)`
- **Data moves:** 14 (STRING 14); most-fed items `CONFIG-DATA`

### `examples/CA1YCOB2.cbl` (COBOL)
- **Calls:** `LINK CA1Y`
- **Record layouts (6 items):** `CONFIG (5)`, `CR (1)`
- **CICS operations:** `CONTAINER CA1Y (write)`, `CHANNEL MyChannel (pass)`
- **Compiler options:** `arith(extend)`, `trunc(bin)`
- **Data moves:** 20 (STRING 20); most-fed items `CONFIG-DATA`

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` (JAVA)
- **Calls:** `LINK onfailure`, `LINK "DFHJSON"`, `LINK options[0]`
- **CICS operations:** `CHANNEL CA1Y (pass)`, `CONTAINER entry.getValue()? (write)`, `CONTAINER CA1Y (write)`, `CONTAINER CA1YRESPONSE (write)`, `CONTAINER DFHEP.ADAPTER (write)`, `CONTAINER DFHEP.DESCRIPTOR (write)`, `CONTAINER DFHEP.DATA.* (write)`, `CONTAINER DFHEP.ADAPTPARM (write)`, `CONTAINER DFHEP.CONTEXT (write)`, `CONTAINER CA1Y-TRANSFORM-I (write)`, `CONTAINER CA1Y-TRANSFORM-O (write)`, `CONTAINER DFHJSON-DATA (write)` … (+3 more)

### `examples/CA1YCOB1.cbl` (COBOL)
- **Record layouts (13 items):** `CHANNEL-INFO (4)`, `CUSTOMER (4)`, `ORDER-PLACED (4)`, `EVENT (1)`
- **CICS operations:** `CONTAINER Customer (write)`, `CONTAINER Order (write)`
- **Compiler options:** `arith(extend)`, `trunc(bin)`

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSQueue.java` (JAVA)
- **CICS operations:** `QUEUE props.getProperty(QUEUE)? (write)`

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSFile.java` (JAVA)
- **CICS operations:** `FILE props.getProperty(FILE)? (write)`

- **Mainframe skeleton completeness:** 33% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: CSD extract (DFHCSDUP LIST / CICSPlex SM), or the web / API layer that LINKs it (4 gaps); application programs (source or load-module list) (3 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1305 call pairs -- scoped 17.2%, unique 1.1%, ambiguous 5.8%, external 75.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 1304 | 17.2% | 1.1% | 5.8% | 75.9% |
| shell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
