# ARCHITECTURAL_BRIEF: cobol-dialect-template
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/BroadcomMFD/cobol-dialect-template.git` |
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
- **Scope:** 33 analyzed artifact(s), 1177 LOC.
- **Load-bearing artifact:** `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` -- 4 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -- pulls in 28 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `client/example-dialect-support/.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 49 |
| Analyzed Artifacts (Scanned) | 33 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 1177 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.3% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2769 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3337 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 21.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0909 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 15 | 1018 | 45.5% |
| MARKDOWN | 6 | 0 | 18.2% |
| PLAINTEXT | 4 | 1 | 12.1% |
| JSON | 3 | 79 | 9.1% |
| XML | 2 | 0 | 6.1% |
| YAML | 1 | 34 | 3.0% |
| SHELL | 1 | 12 | 3.0% |
| TYPESCRIPT | 1 | 33 | 3.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 32 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 48%, State Mutators Files 15%, Encapsulated Accessors Files 12%, Large Core Modules (3) 12%, Declarative / Non-Code 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 23 | 69.7% |
| Unknown | 1 | 3.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 27.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16*

**Composition by Extension & Reason:**
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 6105 LOC)
- `.g4`: 3x Unsupported Format (.g4)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 20.1 | 3.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 69.6 | 39.2 | 51.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.5 | 2.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 56.2 | 12.0 | 4.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 76.9 | 3.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 96.6 | 17.7 | 11.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4 | 2 | 0 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` |
| cleanup | 0 | 0 | 0 | - |
| guards | 102 | 14 | 12 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` |
| danger | 23 | 9 | 2 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` |
| concurrency | 3 | 1 | 0 | `client/example-dialect-support/src/extension.ts` |
| connectivity | 76 | 17 | 6 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 2 | 2 | 0 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` |
| tests | 1 | 1 | 0 | `build.sh` |
| docs | 21 | 5 | 2 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` |
| debt | 7 | 2 | 0 | `build.sh` |
| mutation | 135 | 16 | 11 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` |
| dead_code | 23 | 7 | 2 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.github/workflows/maven.yml` (Hits: 0)
- `README.md` (Hits: 0)
- `client/example-dialect-support/CHANGELOG.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Level100Node.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java`) — 4 inbound connections
2. **RpcNode.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java`) — 3 inbound connections
3. **UnsetNode.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java`) — 3 inbound connections
4. **CobolErrorStrategy.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java`) — 2 inbound connections
5. **ExampleDialect.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ExampleDialect.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java`) — 28 outbound dependencies
2. **ExampleVisitor.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`) — 24 outbound dependencies
3. **ProcessLevel100Node.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) — 15 outbound dependencies
4. **ErrorMessageHelper.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) — 14 outbound dependencies
5. **FindInjectsCommand.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `accept` **(Many-Argument Workhorses)** (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **15.0** | LOC: 58
- `reportError` **(Defensive Guards)** (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java`) -> Impact: **14.8** | LOC: 19
- `visitRpcParseStatement` **(Callbacks & Closures)** (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`) -> Impact: **9.8** | LOC: 54
- `accept` **(Type Conversions)** (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) -> Impact: **8.2** | LOC: 25
- `accept` **(Callbacks & Closures)** (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java`) -> Impact: **7.8** | LOC: 52
- `checkSubordinatesIdentifier2` **(Stateful Encapsulated Methods)** (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **7.6** | LOC: 17
- `injectCopybook` **(Many-Argument Workhorses)** (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java`) -> Impact: **7.2** | LOC: 46
- `activate` **(Compute Cores)** (@ `client/example-dialect-support/src/extension.ts`) -> Impact: **5.6** | LOC: 28
  * *Intent:* // This method is called when your extension is activated // Your extension is activated the very first time the command is executed
- `getInputMismatchMessage` **(Parameter Forwarders)** (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> Impact: **4.8** | LOC: 7
  * *Intent:* /** * Returns an input mismatch error message for a {@link InputMismatchException} * * @param recognizer parser reference * @param e {@link InputMisma...
- `RpcNode` **(Many-Argument Workhorses)** (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java`) -> Impact: **4.1** | LOC: 18

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Parameter Forwarders**: thin, many-argument glue that forwards to other code
  * **Stateful Encapsulated Methods**: n/a
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `client/example-dialect-support` | 6 | 5019.62 | 0.0% | 0.0% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample` | 7 | 227.88 | 4.05% | 53.41% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor` | 4 | 90.5 | 9.09% | 8.04% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes` | 3 | 24.58 | 0.0% | 0.0% |
| `server/dialect-example` | 2 | 21.04 | 0.0% | 0.0% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility` | 1 | 19.5 | 0.0% | 0.0% |
| `client/example-dialect-support/snippets` | 1 | 15.96 | 0.0% | 0.0% |
| `client/example-dialect-support/src` | 1 | 15.36 | 16.25% | 81.76% |
| `client/example-dialect-support/syntaxes` | 1 | 15.34 | 0.0% | 0.0% |
| `.github/workflows` | 1 | 6.08 | 3.07% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` -> **99.9834%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **97.0688%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **90.5672%** Exposure
- `client/example-dialect-support/src/extension.ts` -> **81.7574%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` -> **48.4761%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` -> **96.5861%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -> **56.062%** Exposure
- `client/example-dialect-support/src/extension.ts` -> **50.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` -> **50.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java` -> **40.1312%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` -> **10** Orphaned Functions | **0** Duplicates
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **4** Orphaned Functions | **0** Duplicates
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **3** Orphaned Functions | **0** Duplicates
- `client/example-dialect-support/src/extension.ts` -> **2** Orphaned Functions | **0** Duplicates
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` -> **2** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `185` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `client/example-dialect-support/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.721)
- **Top Global Matches:** file_cluster_0: 7.721, file_cluster_5: 7.737, file_cluster_12: 8.89
- **Magnitude:** 62.08 | **LOC:** 299 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 74.289; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (56.1%), Guard Balance (formerly Safety Score) (53.6%), Connectivity (formerly Api Exposure) (41.5%), Complexity Load (formerly Cognitive Load) (6.4%)
- **Documentation Coverage:** 16.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `injectCopybook` **(Many-Argument Workhorses)** (Impact: 7.2)
  * `parseMyRule` **(Stateful Encapsulated Methods)** (Impact: 2.8)
  * `extend` **(Generic / Templated Code)** (Impact: 2.7)
    * *Intent:* /** * This implementation is specific to copybooks. * Use this when an external source content needs...
  * `processText` **(Generic / Templated Code)** (Impact: 2.4)
    * *Intent:* /** * Processing the text * * @param context is a DialectProcessingContext class with all needed dat...
  * `getKeywords` **(Callbacks & Closures)** (Impact: 2.2)
    * *Intent:* /** * Returns dialect keywords map where key is a keyword and a value is a description * * @return k...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 74`, `args: 17`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`
* *Architecture:* `api: 15`, `import: 25`
* *Defense:* `safety: 2`, `doc: 11`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 74.289
  * `Choke Point (Betweenness):` 0.047379 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 11):` com.google.common.collect.ImmutableList, com.google.common.collect.ImmutableMap, java.io.IOException, java.util.*, java.util.stream.Collectors, lombok.extern.slf4j.Slf4j, org.antlr.v4.runtime.CharStreams, org.antlr.v4.runtime.CommonTokenStream...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.443)
- **Top Global Matches:** file_cluster_0: 7.443, file_cluster_10: 9.335, file_cluster_5: 9.549
- **Magnitude:** 49.38 | **LOC:** 220 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 22.211; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (51.0%), Connectivity (formerly Api Exposure) (6.0%), Complexity Load (formerly Cognitive Load) (5.6%)
- **Documentation Coverage:** 84.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitRpcParseStatement` **(Callbacks & Closures)** (Impact: 9.8)
  * `visitUnsetStatement` **(Callbacks & Closures)** (Impact: 2.3)
  * `visitDataDescriptionEntry100` **(Callbacks & Closures)** (Impact: 2.2)
  * `visitBitwiseShiftstatement` **(Generic / Templated Code)** (Impact: 2.0)
  * `addTreeNode` **(Encapsulated Accessors)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 51`, `args: 33`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 3`, `unreferenced_by_name: 10`
* *Architecture:* `api: 12`, `import: 24`
* *Defense:* `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.211
  * `Choke Point (Betweenness):` 0.002016 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 4):` com.google.common.collect.ImmutableList, java.util.ArrayList, java.util.LinkedList, java.util.List, java.util.Objects, java.util.Optional.ofNullable, java.util.function.Function, java.util.stream.Collectors.toList...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.44)
- **Top Global Matches:** file_cluster_5: 7.44, file_cluster_7: 8.926, file_cluster_12: 9.28
- **Magnitude:** 46.52 | **LOC:** 116 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 22.211; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.6%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (20.1%), Connectivity (formerly Api Exposure) (16.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `accept` **(Many-Argument Workhorses)** (Impact: 15.0)
  * `checkSubordinatesIdentifier2` **(Stateful Encapsulated Methods)** (Impact: 7.6)
  * `getVariableUsageNode` **(Encapsulated Accessors)** (Impact: 2.3)
  * `ProcessRpcNode` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 24`, `args: 10`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 7`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.211
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071023
  * `Imports (Out-Degree: 1):` java.util.Objects, java.util.Optional, java.util.Optional.ofNullable, org.broadcom.cobol.dialects.cobolExample.nodes.RpcNode, org.eclipse.lsp.cobol.common.error.ErrorSeverity.ERROR, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.message.MessageService...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.07)
- **Top Global Matches:** file_cluster_0: 8.07, file_cluster_16: 8.591, file_cluster_15: 8.784
- **Magnitude:** 41.68 | **LOC:** 150 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 127.341; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (90.6%), Guard Balance (formerly Safety Score) (51.4%), Complexity Load (formerly Cognitive Load) (4.5%), Connectivity (formerly Api Exposure) (2.9%)
- **Documentation Coverage:** 41.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getInputMismatchMessage` **(Parameter Forwarders)** (Impact: 4.8)
    * *Intent:* /** * Returns an input mismatch error message for a {@link InputMismatchException} * * @param recogn...
  * `getExpectedText` **(Encapsulated Accessors)** (Impact: 3.8)
  * `getUnwantedTokenMessage` **(Parameter Forwarders)** (Impact: 3.7)
    * *Intent:* /** * Returns a message in case unwanted token found while parsing. * * @param recognizer Parser ref...
  * `removeIdentifierTokens` **(Encapsulated Accessors)** (Impact: 3.1)
  * `collectErrorTokens` **(Encapsulated Accessors)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 27`, `args: 15`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 14`
* *Defense:* `doc: 5`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 127.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066176
  * `Imports (Out-Degree: 1):` com.google.common.collect.ImmutableSet, java.util.Arrays, java.util.List, java.util.Optional, java.util.Set, java.util.stream.Collectors.joining, java.util.stream.Collectors.toList, org.antlr.v4.runtime.InputMismatchException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.663)
- **Top Global Matches:** file_cluster_12: 7.663, file_cluster_7: 7.729, file_cluster_5: 8.615
- **Magnitude:** 40.44 | **LOC:** 111 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 130.443; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.5%), Debt Markers (formerly Tech Debt) (48.5%), Mutation Surface (formerly State Flux) (12.9%), Complexity Load (formerly Cognitive Load) (11.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reportError` **(Defensive Guards)** (Impact: 14.8)
  * `reportMissingToken` **(Stateful Encapsulated Methods)** (Impact: 3.5)
  * `reportUnwantedToken` **(Encapsulated Accessors)** (Impact: 3.3)
  * `reportInputMismatch` **(Encapsulated Accessors)** (Impact: 2.1)
  * `reportNoViableAlternative` **(Encapsulated Accessors)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 22`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 130.443
  * `Choke Point (Betweenness):` 0.00504 | `Ripple Effect (Closeness):` 0.09375
  * `Imports (Out-Degree: 1):` lombok.Getter, lombok.NoArgsConstructor, lombok.Setter, lombok.extern.slf4j.Slf4j, org.antlr.v4.runtime.*, org.eclipse.lsp.cobol.common.message.MessageService, org.eclipse.lsp.cobol.common.message.MessageServiceProvider
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.639)
- **Top Global Matches:** file_cluster_12: 7.639, file_cluster_5: 8.399, file_cluster_16: 8.645
- **Magnitude:** 20.8 | **LOC:** 73 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 22.211; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.9%), Mutation Surface (formerly State Flux) (18.6%), Connectivity (formerly Api Exposure) (18.3%), Complexity Load (formerly Cognitive Load) (9.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `accept` **(Type Conversions)** (Impact: 8.2)
  * `registerVariable` **(Encapsulated Accessors)** (Impact: 2.4)
  * `addError` **(Stateful Encapsulated Methods)** (Impact: 2.3)
  * `ProcessLevel100Node` **(State Mutators)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 24`, `args: 8`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 3`, `import: 15`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.211
  * `Choke Point (Betweenness):` 0.00504 | `Ripple Effect (Closeness):` 0.071023
  * `Imports (Out-Degree: 2):` java.util.Optional, org.broadcom.cobol.dialects.cobolExample.nodes.Level100Node, org.eclipse.lsp.cobol.common.error.ErrorSeverity.ERROR, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.message.MessageService, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.SectionType...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.66)
- **Top Global Matches:** file_cluster_15: 4.66, file_cluster_2: 5.756, file_cluster_13: 5.922
- **Magnitude:** 19.5 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 40.069; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (56.2%), Guard Balance (formerly Safety Score) (51.2%), Mutation Surface (formerly State Flux) (25.6%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addReplacementContext` **(Parameter Forwarders)** (Impact: 2.2)
  * `addReplacementContext` **(Parameter Forwarders)** (Impact: 2.2)
  * `constructLocality` **(Parameter Forwarders)** (Impact: 2.1)
  * `constructRange` **(Parameter Forwarders)** (Impact: 1.9)
  * `constructRange` **(Parameter Forwarders)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.080357
  * `Imports (Out-Degree: 0):` lombok.experimental.UtilityClass, org.antlr.v4.runtime.ParserRuleContext, org.antlr.v4.runtime.tree.TerminalNode, org.eclipse.lsp.cobol.common.dialects.CobolDialect, org.eclipse.lsp.cobol.common.dialects.DialectProcessingContext, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp4j.Location, org.eclipse.lsp4j.Position...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `client/example-dialect-support/snippets/example-snippets.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.994)
- **Top Global Matches:** file_cluster_2: 1.994, file_cluster_17: 4.88, file_cluster_13: 6.235
- **Magnitude:** 15.96 | **LOC:** 48 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.273)
- **Top Global Matches:** file_cluster_0: 6.273, file_cluster_13: 9.432, file_cluster_10: 10.183
- **Magnitude:** 15.84 | **LOC:** 57 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 22.211; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.1%), Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (11.9%), Connectivity (formerly Api Exposure) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitInjectStatement` **(Generic / Templated Code)** (Impact: 2.2)
  * `addTreeNode` **(Encapsulated Accessors)** (Impact: 2.0)
  * `aggregateResult` **(Encapsulated Accessors)** (Impact: 1.9)
  * `InjectRuleVisitor` **(State Mutators)** (Impact: 1.6)
  * `defaultResult` **(Encapsulated Accessors)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.211
  * `Choke Point (Betweenness):` 0.002016 | `Ripple Effect (Closeness):` 0.071023
  * `Imports (Out-Degree: 1):` com.google.common.collect.ImmutableList, java.util.ArrayList, java.util.List, java.util.function.Function, java.util.stream.Collectors.toList, java.util.stream.Stream, org.antlr.v4.runtime.ParserRuleContext, org.broadcom.cobol.dialects.cobolExample.utility.VisitorUtility...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.809)
- **Top Global Matches:** file_cluster_10: 7.809, file_cluster_12: 8.403, file_cluster_0: 8.406
- **Magnitude:** 15.84 | **LOC:** 80 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 22.211; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.7%), Connectivity (formerly Api Exposure) (26.9%), Mutation Surface (formerly State Flux) (21.6%), Complexity Load (formerly Cognitive Load) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `accept` **(Callbacks & Closures)** (Impact: 7.8)
  * `ProcessUnsetNode` **(State Mutators)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 21`, `args: 10`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.211
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 1):` java.util.List, java.util.Optional, org.broadcom.cobol.dialects.cobolExample.nodes.UnsetNode, org.eclipse.lsp.cobol.common.error.ErrorSeverity.ERROR, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.message.MessageService, org.eclipse.lsp.cobol.common.model.NodeType...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `client/example-dialect-support/src/extension.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.844)
- **Top Global Matches:** file_cluster_10: 6.844, file_cluster_13: 6.891, file_cluster_15: 6.933
- **Magnitude:** 15.36 | **LOC:** 44 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 16.47; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Concurrency Surface (formerly Concurrency) (76.9%), Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `activate` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* // This method is called when your extension is activated // Your extension is activated the very fi...
  * `deactivate` **(State Mutators)** (Impact: 1.1)
    * *Intent:* // This method is called when your extension is deactivated
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `concurrency: 3`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cobol-dialect-api, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/syntaxes/example.injection.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.052)
- **Top Global Matches:** file_cluster_2: 2.052, file_cluster_17: 4.908, file_cluster_13: 6.249
- **Magnitude:** 15.34 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.078)
- **Top Global Matches:** file_cluster_2: 2.078, file_cluster_17: 4.919, file_cluster_13: 6.256
- **Magnitude:** 15.28 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.621)
- **Top Global Matches:** file_cluster_5: 7.621, file_cluster_12: 9.019, file_cluster_0: 9.033
- **Magnitude:** 14.58 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 22.211; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (41.4%), Mutation Surface (formerly State Flux) (40.1%), Debt Markers (formerly Tech Debt) (37.8%), Connectivity (formerly Api Exposure) (3.3%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createCommand` **(Encapsulated Accessors)** (Impact: 2.1)
  * `collectCommandsOrActions` **(Generic / Templated Code)** (Impact: 1.9)
    * *Intent:* /** * Create a list of commands or code actions according to the diagnostic's type. May be empty if ...
  * `toCodeAction` **(Encapsulated Accessors)** (Impact: 1.9)
  * `retrieveInjects` **(Encapsulated Accessors)** (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 24`, `args: 7`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.211
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 1):` java.util.Arrays.asList, java.util.Collections.singletonList, java.util.List, java.util.function.Function, java.util.stream.Collectors.toList, lombok.NonNull, org.broadcom.cobol.dialects.cobolExample.ExampleDialect.MISSING_INJECTS, org.eclipse.lsp.cobol.common.action.CodeActionProvider...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.633)
- **Top Global Matches:** file_cluster_13: 7.633, file_cluster_15: 7.763, file_cluster_17: 7.783
- **Magnitude:** 12.76 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 45.81; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.3%), Mutation Surface (formerly State Flux) (50.0%), Connectivity (formerly Api Exposure) (8.9%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RpcNode` **(Many-Argument Workhorses)** (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 45.81
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.1125
  * `Imports (Out-Degree: 0):` lombok.Getter, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNameAndLocality
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `server/dialect-example/lombok.config` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/pom.xml` (XML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 102 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/Level100Transformer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.414)
- **Top Global Matches:** file_cluster_7: 5.414, file_cluster_12: 7.062, file_cluster_5: 8.698
- **Magnitude:** 7.34 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 25.91; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.3%), Debt Markers (formerly Tech Debt) (32.2%), Connectivity (formerly Api Exposure) (6.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate` **(I/O & Config Routines)** (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066176
  * `Imports (Out-Degree: 1):` lombok.AllArgsConstructor, lombok.Getter, org.broadcom.cobol.dialects.cobolExample.nodes.Level100Node, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.tree.variable.ElementaryItemNode, org.eclipse.lsp.cobol.common.model.tree.variable.GroupItemNode, org.eclipse.lsp.cobol.common.model.tree.variable.UsageFormat, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNode...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.519)
- **Top Global Matches:** file_cluster_13: 5.519, file_cluster_17: 7.02, file_cluster_2: 7.189
- **Magnitude:** 6.18 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 45.81; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Connectivity (formerly Api Exposure) (45.0%), Mutation Surface (formerly State Flux) (11.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UnsetNode` **(State Mutators)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 45.81
  * `Choke Point (Betweenness):` 0.023185 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` lombok.Getter, org.broadcom.cobol.dialects.cobolExample.ExampleDialect, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNameAndLocality
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `.github/workflows/maven.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.875)
- **Top Global Matches:** file_cluster_2: 4.875, file_cluster_17: 6.26, file_cluster_11: 6.621
- **Magnitude:** 6.08 | **LOC:** 55 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 16.47; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (3.4%), Complexity Load (formerly Cognitive Load) (3.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Build with Maven` **(I/O & Config Routines)** (Impact: 1.1)
  * `Build vsix` **(I/O & Config Routines)** (Impact: 1.1)
  * `Copy vsix` **(I/O & Config Routines)** (Impact: 1.1)
  * `Package vsix` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v3, setup-java@v3, upload-artifact@v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.978)
- **Top Global Matches:** file_cluster_13: 5.978, file_cluster_17: 7.559, file_cluster_11: 7.646
- **Magnitude:** 5.64 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 58.394; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Connectivity (formerly Api Exposure) (24.6%), Mutation Surface (formerly State Flux) (11.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Level100Node` **(State Mutators)** (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.139205
  * `Imports (Out-Degree: 0):` lombok.Getter, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/DialectParserListener.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.958)
- **Top Global Matches:** file_cluster_0: 6.958, file_cluster_13: 7.632, file_cluster_11: 9.187
- **Magnitude:** 3.88 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 22.211; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Test Surface (formerly Verification) (2.3%), Connectivity (formerly Api Exposure) (1.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DialectParserListener` **(State Mutators)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.211
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071023
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, lombok.Getter, org.antlr.v4.runtime.BaseErrorListener, org.eclipse.lsp.cobol.common.error.SyntaxError
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `build.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.568)
- **Top Global Matches:** file_cluster_7: 5.568, file_cluster_12: 8.921, file_cluster_14: 9.533
- **Magnitude:** 2.14 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* None
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 2.1 | **LOC:** 105 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` (JAVA) | Magnitude: 62.08 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 142, structural_boundaries: 74, import: 25, core_var_decl: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `client/example-dialect-support/src/extension.ts` (TYPESCRIPT) | Magnitude: 15.36 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 10, core_var_decl: 7, design_camel_case: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA) | Magnitude: 40.44 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 22, decorators: 10, encapsulation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` (JAVA) | Magnitude: 12.76 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 8, state_mutation: 6, immutability_locks: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -> **Severity: 2.656** (Bridge: 0.0474 * Flux: 56.062%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 0.276** (Bridge: 0.0232 * Flux: 11.9203%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` -> **Severity: 0.094** (Bridge: 0.005 * Flux: 18.5893%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` -> **Severity: 0.065** (Bridge: 0.005 * Flux: 12.8734%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **Severity: 0.024** (Bridge: 0.002 * Flux: 11.9203%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` -> **Severity: 7.06** (Embedded: 0.1392 * Error Risk: 50.7142%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` -> **Severity: 6.106** (Embedded: 0.1125 * Error Risk: 54.2752%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` -> **Severity: 5.671** (Embedded: 0.0938 * Error Risk: 60.4878%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 5.071** (Embedded: 0.1 * Error Risk: 50.7142%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` -> **Severity: 4.943** (Embedded: 0.071 * Error Risk: 69.604%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` -> **Severity: 13044.3** (Blast Radius: 130.443 * Doc Risk: 100.0%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` -> **Severity: 5839.4** (Blast Radius: 58.394 * Doc Risk: 100.0%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **Severity: 5243.457** (Blast Radius: 127.341 * Doc Risk: 41.1765%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` -> **Severity: 4581.0** (Blast Radius: 45.81 * Doc Risk: 100.0%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 4581.0** (Blast Radius: 45.81 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 474 call pairs -- scoped 10.3%, unique 1.5%, ambiguous 4.0%, external 84.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 464 | 10.6% | 1.5% | 4.1% | 83.8% |
| typescript | 6 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
