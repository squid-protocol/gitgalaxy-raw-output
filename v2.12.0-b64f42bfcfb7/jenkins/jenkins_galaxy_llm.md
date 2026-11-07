# ARCHITECTURAL_BRIEF: jenkins
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jenkinsci/jenkins` |
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
- **Scope:** 11866 analyzed artifact(s), 250894 LOC.
- **Load-bearing artifact:** `core/src/main/java/jenkins/model/Jenkins.java` -- 544 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `core/src/main/java/jenkins/model/Jenkins.java` -- pulls in 317 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `core/src/main/java/jenkins/model/Jenkins.java` at magnitude 2332.74 (structural weight, not risk).
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
| Total Artifacts | 12362 |
| Analyzed Artifacts (Scanned) | 11866 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 496 |
| Total LOC | 250894 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.0% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4119 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1415 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5719 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 160 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 7511 | 0 | 63.3% |
| JAVA | 1906 | 203283 | 16.1% |
| XML | 1100 | 9 | 9.3% |
| HTML | 1019 | 21493 | 8.6% |
| JAVASCRIPT | 124 | 11233 | 1.0% |
| CSS | 88 | 10925 | 0.7% |
| GROOVY | 64 | 1209 | 0.5% |
| JSON | 29 | 1566 | 0.2% |
| YAML | 9 | 394 | 0.1% |
| MARKDOWN | 6 | 0 | 0.1% |
| SHELL | 4 | 102 | 0.0% |
| BATCH | 3 | 31 | 0.0% |
| RUBY | 1 | 525 | 0.0% |
| C | 1 | 15 | 0.0% |
| PYTHON | 1 | 109 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 7 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 11764 |
| utf-8 | bom | 95 |
| cp1252 | cp1252-fallback | 6 |
| latin-1 | latin-1-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 83%, Declarative / Non-Code 3%, Encapsulated Accessors Files 3%, Large Core Modules (3) 3%, Large Core Modules (2) 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4347 | 36.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7517 | 63.3% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 496*

**Composition by Extension & Reason:**
- `.svg`: 125x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 1787 commas in 521 LOC)
- `.gif`: 109x Excluded (Explicitly Denied Extension: '.gif')
- `.png`: 69x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 53x Unsupported Format (.undeterminable), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 33x Excluded (Explicitly Denied Extension: '.zip')
- `.hpi`: 18x Excluded (Binary Format Detected)
- `.hint`: 14x Unsupported Format (.hint)
- `.properties`: 9x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.xml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 61 exceeds 500 chars)
- `.jpi`: 5x Excluded (Binary Format Detected)
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.g4`: 4x Unsupported Format (.g4)
- `.04`: 4x Unsupported Format (.04)
- `.yml`: 1x Excluded (Machine-Generated Source Code Signature: 15 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.config`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 81.5 | 21.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.8 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 97.9 | 1.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 86.6 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1327 | 517 | 0 | `test/src/test/java/hudson/cli/DeleteBuildsCommandTest.java` |
| cleanup | 191 | 109 | 0 | `test/src/test/java/jenkins/security/stapler/Security400Test.java` |
| guards | 21993 | 1757 | 3 | `core/src/main/java/hudson/FilePath.java` |
| danger | 12033 | 1396 | 1 | `core/src/main/java/jenkins/model/Jenkins.java` |
| concurrency | 2596 | 369 | 0 | `core/src/main/java/jenkins/model/Jenkins.java` |
| connectivity | 18295 | 1699 | 3 | `core/src/main/java/jenkins/model/Jenkins.java` |
| io | 5537 | 744 | 0 | `core/src/main/java/hudson/FilePath.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 25 | 9 | 0 | `core/src/main/java/hudson/Proc.java` |
| time | 513 | 132 | 0 | `core/src/test/java/hudson/scheduler/CronTabDayOfWeekLocaleTest.java` |
| serialization | 33 | 17 | 0 | `core/src/main/java/jenkins/util/xml/XMLUtils.java` |
| regex | 258 | 106 | 0 | `war/src/main/webapp/scripts/hudson-behavior.js` |
| events | 2034 | 418 | 0 | `core/src/main/java/jenkins/model/Jenkins.java` |
| tests | 16724 | 624 | 0 | `core/src/test/java/jenkins/org/apache/commons/validator/routines/InetAddressValidatorTest.java` |
| docs | 8642 | 1542 | 1 | `core/src/main/java/jenkins/model/Jenkins.java` |
| debt | 1477 | 510 | 0 | `test/src/test/java/hudson/model/DirectoryBrowserSupportTest.java` |
| mutation | 41752 | 1943 | 5 | `core/src/main/java/jenkins/model/Jenkins.java` |
| dead_code | 5983 | 1080 | 0 | `test/src/test/java/jenkins/security/stapler/DoActionFilterTest.java` |
| credential | 49 | 23 | 0 | `test/src/test/resources/plugins/warnings-update-center-malformed.json` |
| threat | 12 | 6 | 0 | `core/src/test/java/jenkins/model/IdStrategyTest.java` |
| ml_ai | 192 | 78 | 0 | `core/src/main/java/hudson/slaves/NodeProvisioner.java` |
| ui | 1162 | 251 | 0 | `src/main/scss/pages/_dashboard.scss` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `core/src/main/java/hudson/FilePath.java` (Hits: 273)
- `core/src/test/java/jenkins/util/VirtualFileTest.java` (Hits: 255)
- `core/src/test/java/jenkins/util/io/PathRemoverTest.java` (Hits: 151)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Jenkins.java** (`core/src/main/java/jenkins/model/Jenkins.java`) — 544 inbound connections
2. **Extension.java** (`core/src/main/java/hudson/Extension.java`) — 429 inbound connections
3. **Util.java** (`core/src/main/java/hudson/Util.java`) — 239 inbound connections
4. **ExtensionList.java** (`core/src/main/java/hudson/ExtensionList.java`) — 217 inbound connections
5. **ExtensionPoint.java** (`core/src/main/java/hudson/ExtensionPoint.java`) — 163 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Jenkins.java** (`core/src/main/java/jenkins/model/Jenkins.java`) — 317 outbound dependencies
2. **Functions.java** (`core/src/main/java/hudson/Functions.java`) — 167 outbound dependencies
3. **PluginManager.java** (`core/src/main/java/hudson/PluginManager.java`) — 154 outbound dependencies
4. **Run.java** (`core/src/main/java/hudson/model/Run.java`) — 125 outbound dependencies
5. **FilePath.java** (`core/src/main/java/hudson/FilePath.java`) — 118 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createPluginSetupWizard` **(Compute Cores)** (@ `src/main/js/pluginSetupWizardGui.js`) -> Impact: **345.3** | LOC: 1419
  * *Intent:* // Setup the dialog, exported
- `Anonymous_Block_[Truncated]` **(Compute Cores)** (@ `core/report-l10n.rb`) -> Impact: **138.7** | LOC: 134
- `serveFile` **(Many-Argument Workhorses)** (@ `core/src/main/java/hudson/model/DirectoryBrowserSupport.java`) -> Impact: **108.8** | LOC: 217
- `_main` **(Compute Cores)** (@ `cli/src/main/java/hudson/cli/CLI.java`) -> Impact: **81.2** | LOC: 209
- `buildFormTree` **(Compute Cores)** (@ `core/src/main/resources/jenkins/formelementpath/form-element-path.js`) -> Impact: **80.1** | LOC: 188
  * *Intent:* // most of this is copied from hudson-behaviour.js
- `doXml` **(Many-Argument Workhorses)** (@ `core/src/main/java/hudson/model/Api.java`) -> Impact: **63.6** | LOC: 108
  * *Intent:* /** * Exposes the bean as XML. */
- `buildFormTree` **(Compute Cores)** (@ `war/src/main/webapp/scripts/hudson-behavior.js`) -> Impact: **62.2** | LOC: 169
  * *Intent:* // // structured form submission handling // see https://www.jenkins.io/redirect/developer/structured-form-submission
- `drawCategoryLabels` **(Many-Argument Workhorses)** (@ `core/src/main/java/hudson/util/NoOverlapCategoryAxis.java`) -> Impact: **61.3** | LOC: 115
- `installIfNecessaryFrom` **(Many-Argument Workhorses)** (@ `core/src/main/java/hudson/FilePath.java`) -> Impact: **58.9** | LOC: 104
- `maintain` **(I/O & Config Routines)** (@ `core/src/main/java/hudson/model/Queue.java`) -> Impact: **57.9** | LOC: 237
  * *Intent:* /** * Queue maintenance. * * <p> * Move projects between {@link #waitingList}, {@link #blockedProjects}, {@link #buildables}, and {@link #pendings} * ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `core/src/main/java/hudson/model` | 170 | 19249.3 | 11.79% | 19.99% |
| `core/src/main/java/hudson` | 50 | 8992.74 | 12.57% | 19.84% |
| `core/src/main/java/hudson/util` | 122 | 7694.08 | 12.94% | 23.13% |
| `test/src/test/java/hudson/model` | 84 | 6008.88 | 11.51% | 0.0% |
| `core/src/main/java/jenkins/model` | 69 | 4413.82 | 6.88% | 24.55% |
| `war/src/main/webapp/scripts` | 9 | 2615.1 | 32.2% | 46.28% |
| `core/src/main/java/hudson/security` | 45 | 2235.52 | 9.93% | 33.36% |
| `core/src/main/java/hudson/slaves` | 33 | 2124.0 | 9.75% | 27.02% |
| `core/src/main/java/jenkins/util` | 38 | 1853.18 | 14.63% | 8.09% |
| `core/src/main/java/hudson/tasks` | 22 | 1846.68 | 16.22% | 4.91% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `core/src/main/java/hudson/PluginStrategy.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/cli/declarative/MethodBinder.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/model/queue/QueueTaskFilter.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/search/SearchItems.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/jna/Advapi32.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `war/src/main/webapp/WEB-INF/hudson` -> **100.0%** Exposure
- `cli/src/main/java/hudson/util/QuotedStringTokenizer.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/ArgumentListBuilder.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/ByteArrayOutputStream2.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/ChartUtil.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/src/test/java/jenkins/security/stapler/DoActionFilterTest.java` -> **99** Orphaned Functions | **2** Duplicates
- `core/src/test/java/jenkins/util/VirtualFileTest.java` -> **89** Orphaned Functions | **4** Duplicates
- `test/src/test/java/jenkins/security/stapler/GetterMethodFilterTest.java` -> **81** Orphaned Functions | **4** Duplicates
- `test/src/test/java/hudson/model/DirectoryBrowserSupportTest.java` -> **24** Orphaned Functions | **48** Duplicates
- `test/src/test/java/hudson/model/ViewTest.java` -> **49** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `test/src/test/java/jenkins/install/SetupWizardTest.java` -> **86.6016%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `22` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `27664` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `core/src/main/java/jenkins/model/Jenkins.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.388)
- **Top Global Matches:** file_cluster_5: 7.388, file_cluster_12: 9.68, file_cluster_7: 10.441
- **Magnitude:** 2332.74 | **LOC:** 5991 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **544** in-repo importer(s); it depends on **317**; blast radius 15.62; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (92.8%), Guard Balance (formerly Safety Score) (68.5%), Concurrency Surface (formerly Concurrency) (53.4%)
- **Documentation Coverage:** 45.8667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Jenkins` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /** * @param pluginManager * If non-null, use existing plugin manager. create a new one. */
  * `loadTasks` **(I/O & Config Routines)** (Impact: 24.6)
  * `getItem` **(Defensive Guards)** (Impact: 22.9)
    * *Intent:* * Gets the item by its path name from the given context * * <p><strong>Path Names:</strong> * If the...
  * `executeReactor` **(Stateful Encapsulated Methods)** (Impact: 16.6)
    * *Intent:* /** * Executes a reactor. * * @param is * If non-null, this can be consulted for ignoring some tasks...
  * `refreshExtensions` **(Callbacks & Closures)** (Impact: 15.9)
    * *Intent:* /** * Refresh {@link ExtensionList}s by adding all the newly discovered extensions. * * Exposed only...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 128 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 140
* *State Mutation (weighted view):* 505
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 363`, `structural_boundaries: 1279`, `args: 441`, `func_start: 400`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 280`, `high_risk_execution: 3`, `state_mutation: 249`, `planned_debt: 17`, `fragile_debt: 8`
* *Architecture:* `io: 37`, `api: 404`, `concurrency: 65`, `import: 317`
* *Defense:* `safety: 208`, `doc: 286`, `sync_locks: 28`, `immutability_locks: 106`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.62
  * `Choke Point (Betweenness):` 0.005054 | `Ripple Effect (Closeness):` 0.071405
  * `Imports (Out-Degree: 190):` com.google.common.annotations.VisibleForTesting, com.google.inject.Inject, com.google.inject.Injector, com.thoughtworks.xstream.XStream, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings...
  * `Imported By (In-Degree: 544):` (Excluded from Brief to save tokens)

### `war/src/main/webapp/scripts/hudson-behavior.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.526)
- **Top Global Matches:** file_cluster_12: 8.526, file_cluster_7: 10.014, file_cluster_4: 10.552
- **Magnitude:** 1808.86 | **LOC:** 2761 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.2%), Complexity Load (formerly Cognitive Load) (69.8%), Concurrency Surface (formerly Concurrency) (66.8%)
- **Documentation Coverage:** 73.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildFormTree` **(Compute Cores)** (Impact: 62.2)
    * *Intent:* // // structured form submission handling // see https://www.jenkins.io/redirect/developer/structure...
  * `registerMinMaxValidator` **(Defensive Guards)** (Impact: 48.7)
    * *Intent:* /** * Add a validator for number fields which contains 'min', 'max' attribute */
  * `encode` **(Compute Cores)** (Impact: 33.7)
    * *Intent:* */ // eslint-disable-next-line no-unused-vars
  * `onchange` **(Defensive Guards)** (Impact: 32.8)
  * `findFormParent` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* /** * Finds the DOM node of the given DOM node that acts as a parent in the form submission. * * The...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 218 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 70
* *State Mutation (weighted view):* 731
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 361`, `args: 200`, `func_start: 122`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 17`, `state_mutation: 295`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 25`
* *Architecture:* `io: 9`, `concurrency: 15`
* *Defense:* `safety: 89`, `doc: 39`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/FilePath.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.9)
- **Top Global Matches:** file_cluster_5: 7.9, file_cluster_12: 8.904, file_cluster_7: 10.7
- **Magnitude:** 1586.3 | **LOC:** 3937 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **118** in-repo importer(s); it depends on **118**; blast radius 3.839; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (64.1%), Connectivity (formerly Api Exposure) (58.9%), Guard Balance (formerly Safety Score) (56.6%), Concurrency Surface (formerly Concurrency) (18.9%)
- **Documentation Coverage:** 51.1811% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `installIfNecessaryFrom` **(Many-Argument Workhorses)** (Impact: 58.9)
  * `invoke` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `readFromTar` **(Many-Argument Workhorses)** (Impact: 38.9)
    * *Intent:* /** * Reads from a tar stream and stores obtained files to the base dir. * Supports large files &gt;...
  * `normalize` **(Compute Cores)** (Impact: 36.8)
    * *Intent:* /** * {@link File#getParent()} etc cannot handle ".." and "." in the path component very well, * so ...
  * `validateRelativePath` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* * or {@link Jenkins#MANAGE} permission if no such ancestor is found. * * <p>Note that this permissio...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 64 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 987`, `args: 304`, `func_start: 293`, `class_start: 70`
* *Risk/State:* `safety_bypasses: 119`, `state_mutation: 160`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 273`, `api: 222`, `concurrency: 13`, `import: 118`
* *Defense:* `safety: 148`, `doc: 136`, `sync_locks: 1`, `immutability_locks: 219`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.839
  * `Choke Point (Betweenness):` 0.000405 | `Ripple Effect (Closeness):` 0.054026
  * `Imports (Out-Degree: 31):` com.google.common.annotations.VisibleForTesting, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.Launcher.LocalLauncher, hudson.Launcher.RemoteLauncher, hudson.Util.fileToPath, hudson.Util.fixEmpty...
  * `Imported By (In-Degree: 118):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/Functions.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.922)
- **Top Global Matches:** file_cluster_5: 6.922, file_cluster_7: 9.767, file_cluster_12: 9.886
- **Magnitude:** 1337.48 | **LOC:** 2743 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **155** in-repo importer(s); it depends on **167**; blast radius 5.168; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (97.2%), Guard Balance (formerly Safety Score) (80.0%), Concurrency Surface (formerly Concurrency) (54.9%)
- **Documentation Coverage:** 39.8458% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPasswordValue` **(Defensive Guards)** (Impact: 34.9)
    * *Intent:* /** * Used by {@code <f:password/>} so that we send an encrypted value to the client. */
  * `dumpThreadInfo` **(Compute Cores)** (Impact: 32.5)
    * *Intent:* // ThreadInfo.toString() truncates the stack trace by first 8, so needed my own version
  * `getRelativeNameFrom` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* /** * Gets the relative name or display name to the given item from the specified group. * * @since ...
  * `doPrintStackTrace` **(Many-Argument Workhorses)** (Impact: 31.7)
  * `htmlAttributeEscape` **(Compute Cores)** (Impact: 18.1)
    * *Intent:* /** * Escapes a string so it can be used in an HTML attribute value. * <pre> * Input example 1: &amp...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 79 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 595`, `args: 219`, `func_start: 199`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 184`, `state_mutation: 104`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 194`, `concurrency: 18`, `import: 167`
* *Defense:* `safety: 52`, `doc: 114`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.168
  * `Choke Point (Betweenness):` 0.001108 | `Ripple Effect (Closeness):` 0.055684
  * `Imports (Out-Degree: 88):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.cli.CLICommand, hudson.console.ConsoleAnnotationDescriptor, hudson.console.ConsoleAnnotatorFactory, hudson.init.InitMilestone...
  * `Imported By (In-Degree: 155):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Queue.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.372)
- **Top Global Matches:** file_cluster_5: 8.372, file_cluster_12: 10.811, file_cluster_7: 11.399
- **Magnitude:** 1274.06 | **LOC:** 3253 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **82** in-repo importer(s); it depends on **115**; blast radius 2.253; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.3%), Connectivity (formerly Api Exposure) (79.6%), Guard Balance (formerly Safety Score) (72.5%), Complexity Load (formerly Cognitive Load) (25.7%)
- **Documentation Coverage:** 42.8184% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maintain` **(I/O & Config Routines)** (Impact: 57.9)
    * *Intent:* /** * Queue maintenance. * * <p> * Move projects between {@link #waitingList}, {@link #blockedProjec...
  * `scheduleInternal` **(Many-Argument Workhorses)** (Impact: 27.3)
    * *Intent:* /** * Schedules an execution of a task. * * @since 1.311 * @return * {@link hudson.model.queue.Sched...
  * `makeFlyWeightTaskBuildable` **(Stateful Encapsulated Methods)** (Impact: 18.1)
    * *Intent:* /** * This method checks if the flyweight task can be run on any of the available executors * @param...
  * `load` **(Defensive Guards)** (Impact: 17.0)
    * *Intent:* /** * Loads the queue contents that was {@link #save() saved}. */
  * `getCauseOfBlockage` **(Compute Cores)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 611`, `args: 231`, `func_start: 212`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 162`, `state_mutation: 113`, `dead_code: 4`, `planned_debt: 16`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 186`, `concurrency: 29`, `import: 115`
* *Defense:* `safety: 101`, `doc: 145`, `sync_locks: 67`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.253
  * `Choke Point (Betweenness):` 0.000492 | `Ripple Effect (Closeness):` 0.050858
  * `Imports (Out-Degree: 68):` com.google.common.annotations.VisibleForTesting, com.google.common.cache.Cache, com.google.common.cache.CacheBuilder, com.infradna.tool.bridge_method_injector.WithBridgeMethods, com.thoughtworks.xstream.XStream, com.thoughtworks.xstream.converters.basic.AbstractSingleValueConverter, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull...
  * `Imported By (In-Degree: 82):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/PluginManager.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.291)
- **Top Global Matches:** file_cluster_5: 6.291, file_cluster_12: 8.946, file_cluster_7: 9.609
- **Magnitude:** 1255.76 | **LOC:** 2698 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **154**; blast radius 1.903; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Connectivity (formerly Api Exposure) (68.8%), Guard Balance (formerly Safety Score) (67.7%), Complexity Load (formerly Cognitive Load) (36.9%)
- **Documentation Coverage:** 54.8117% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `install` **(Many-Argument Workhorses)** (Impact: 36.3)
  * `doPluginsSearch` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `initTasks` **(Stateful Encapsulated Methods)** (Impact: 29.4)
    * *Intent:* /** * Called immediately after the construction. * This is a separate method so that code executed f...
  * `dynamicLoad` **(Many-Argument Workhorses)** (Impact: 29.4)
    * *Intent:* /** * Try the dynamicLoad, removeExisting to attempt to dynamic load disabled plugins */
  * `addDependencies` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* //TODO: Consider refactoring in order to avoid DMI_COLLECTION_OF_URLS
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 96 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 386
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 654`, `args: 161`, `func_start: 132`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 144`, `state_mutation: 194`, `planned_debt: 10`, `fragile_debt: 3`
* *Architecture:* `io: 57`, `api: 129`, `concurrency: 12`, `import: 154`
* *Defense:* `safety: 136`, `doc: 75`, `sync_locks: 2`, `immutability_locks: 52`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.903
  * `Choke Point (Betweenness):` 0.000347 | `Ripple Effect (Closeness):` 0.051137
  * `Imports (Out-Degree: 58):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.PluginWrapper.Dependency, hudson.init.InitMilestone, hudson.init.InitMilestone.COMPLETED, hudson.init.InitMilestone.PLUGINS_LISTED...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/UpdateCenter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.499)
- **Top Global Matches:** file_cluster_5: 7.499, file_cluster_12: 8.748, file_cluster_7: 9.252
- **Magnitude:** 1251.8 | **LOC:** 2956 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **111**; blast radius 0.591; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.1%), Debt Markers (formerly Tech Debt) (90.7%), Connectivity (formerly Api Exposure) (74.8%), Guard Balance (formerly Safety Score) (67.8%)
- **Documentation Coverage:** 51.4124% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verifyChecksums` **(Compute Cores)** (Impact: 42.6)
    * *Intent:* /** * Implements the checksum verification logic with fallback to weaker algorithm for {@link Downlo...
  * `download` **(Defensive Guards)** (Impact: 28.7)
    * *Intent:* /** * Download a plugin or core upgrade in preparation for installing it * into its final location. ...
  * `doConnectionStatusImpl` **(Stateful Encapsulated Methods)** (Impact: 22.2)
  * `getBadge` **(I/O & Config Routines)** (Impact: 15.2)
  * `verifyChecksums` **(Stateful Encapsulated Methods)** (Impact: 15.1)
    * *Intent:* /** * Compare the provided values and return the appropriate {@link VerificationResult}. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 80
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 635`, `args: 201`, `func_start: 190`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 147`, `state_mutation: 155`, `planned_debt: 4`, `duplicate_logic: 24`
* *Architecture:* `io: 80`, `api: 221`, `concurrency: 40`, `import: 111`
* *Defense:* `safety: 117`, `doc: 127`, `sync_locks: 22`, `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.591
  * `Choke Point (Betweenness):` 7.1e-05 | `Ripple Effect (Closeness):` 0.042307
  * `Imports (Out-Degree: 42):` com.google.common.annotations.VisibleForTesting, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.BulkChange, hudson.Extension, hudson.ExtensionPoint, hudson.Functions...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Run.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.846)
- **Top Global Matches:** file_cluster_5: 6.846, file_cluster_12: 8.598, file_cluster_7: 9.392
- **Magnitude:** 1113.66 | **LOC:** 2700 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **130** in-repo importer(s); it depends on **125**; blast radius 2.519; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Connectivity (formerly Api Exposure) (92.6%), Guard Balance (formerly Safety Score) (64.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.8%)
- **Documentation Coverage:** 32.8313% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addArtifacts` **(Many-Argument Workhorses)** (Impact: 36.3)
  * `execute` **(Defensive Guards)** (Impact: 18.3)
  * `getBuildStatusSummary` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* /** * Gets an object which represents the single line summary of the status of this build * (especia...
  * `getLog` **(Defensive Guards)** (Impact: 14.9)
    * *Intent:* /** * Gets the log of the build as a list of strings (one per log line). * The number of lines retur...
  * `waitForCheckpoint` **(Defensive Guards)** (Impact: 13.0)
    * *Intent:* /** * @see CheckPoint#block() */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 85 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 569`, `args: 177`, `func_start: 176`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 144`, `planned_debt: 6`
* *Architecture:* `io: 35`, `api: 191`, `concurrency: 14`, `import: 125`
* *Defense:* `safety: 138`, `doc: 153`, `sync_locks: 10`, `immutability_locks: 65`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.519
  * `Choke Point (Betweenness):` 0.0006 | `Ripple Effect (Closeness):` 0.046802
  * `Imports (Out-Degree: 76):` com.thoughtworks.xstream.XStream, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.AbortException, hudson.BulkChange, hudson.EnvVars, hudson.Extension...
  * `Imported By (In-Degree: 130):` (Excluded from Brief to save tokens)

### `src/main/js/pluginSetupWizardGui.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.837)
- **Top Global Matches:** file_cluster_4: 7.837, file_cluster_10: 10.251, file_cluster_15: 11.132
- **Magnitude:** 1095.24 | **LOC:** 1455 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.111; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.3%), Guard Balance (formerly Safety Score) (59.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPluginSetupWizard` **(Compute Cores)** (Impact: 345.3)
    * *Intent:* // Setup the dialog, exported
  * `setPanel` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* // call this to set the panel in the app, this performs some additional things & adds common transit...
  * `showInstallProgress` **(I/O & Config Routines)** (Impact: 46.8)
    * *Intent:* // Define actions
  * `updateStatus` **(I/O & Config Routines)** (Impact: 36.5)
    * *Intent:* // call to the installStatus, update progress bar & plugin details; transition on complete
  * `showInitialSetupWizard` **(I/O & Config Routines)** (Impact: 23.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 284`, `args: 134`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 108`, `planned_debt: 1`
* *Architecture:* `api: 9`, `concurrency: 7`, `import: 21`
* *Defense:* `safety: 32`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 8.4e-05
  * `Imports (Out-Degree: 18):` pluginManager, securityConfig, id, bootstrap-detached, configureInstance.hbs, errorPanel.hbs, firstUserPanel.hbs, incompleteInstallationPanel.hbs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/AbstractProject.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.994)
- **Top Global Matches:** file_cluster_5: 6.994, file_cluster_7: 10.297, file_cluster_12: 10.608
- **Magnitude:** 880.0 | **LOC:** 2164 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **88** in-repo importer(s); it depends on **98**; blast radius 1.621; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.6%), Connectivity (formerly Api Exposure) (93.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (24.2%)
- **Documentation Coverage:** 43.2526% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `submitImpl` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `_poll` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* /** * {@link #poll(TaskListener)} method without the try/catch block that does listener notification...
  * `poll` **(Defensive Guards)** (Impact: 17.2)
    * *Intent:* /** * Checks if there's any update in SCM, and returns true if any is found. * * <p> * The implement...
  * `checkout` **(Many-Argument Workhorses)** (Impact: 12.2)
  * `isAllSuitableNodesOffline` **(Stateful Encapsulated Methods)** (Impact: 11.1)
    * *Intent:* /** * Returns true if all suitable nodes for the job are offline. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 433`, `args: 146`, `func_start: 150`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 141`, `state_mutation: 79`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 158`, `concurrency: 15`, `import: 98`
* *Defense:* `safety: 49`, `doc: 99`, `sync_locks: 4`, `immutability_locks: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.621
  * `Choke Point (Betweenness):` 0.000617 | `Ripple Effect (Closeness):` 0.051717
  * `Imports (Out-Degree: 73):` com.infradna.tool.bridge_method_injector.WithBridgeMethods, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, hudson.AbortException, hudson.CopyOnWrite, hudson.EnvVars, hudson.ExtensionList, hudson.ExtensionPoint...
  * `Imported By (In-Degree: 88):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/util/ProcessTree.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.842)
- **Top Global Matches:** file_cluster_5: 6.842, file_cluster_12: 7.518, file_cluster_7: 9.979
- **Magnitude:** 875.5 | **LOC:** 2141 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **51**; blast radius 0.326; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (86.2%), Concurrency Surface (formerly Concurrency) (60.9%), Guard Balance (formerly Safety Score) (57.2%)
- **Documentation Coverage:** 70.5584% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AIXProcess` **(I/O & Config Routines)** (Impact: 16.7)
  * `parse` **(I/O & Config Routines)** (Impact: 15.5)
  * `FreeBSD` **(Compute Cores)** (Impact: 14.8)
  * `get` **(Defensive Guards)** (Impact: 14.3)
    * *Intent:* /* package */ static volatile Boolean vetoersExist; /** * Gets the {@link ProcessTree} of the curren...
  * `Darwin` **(Defensive Guards)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 60
* *State Mutation (weighted view):* 271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 434`, `args: 131`, `func_start: 124`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 109`, `dead_code: 8`, `planned_debt: 3`, `duplicate_logic: 15`
* *Architecture:* `io: 16`, `api: 80`, `concurrency: 15`, `import: 51`
* *Defense:* `safety: 98`, `doc: 45`, `sync_locks: 12`, `immutability_locks: 81`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.326
  * `Choke Point (Betweenness):` 6.3e-05 | `Ripple Effect (Closeness):` 0.040289
  * `Imports (Out-Degree: 12):` com.sun.jna.LastErrorException, com.sun.jna.Memory, com.sun.jna.Native, com.sun.jna.NativeLong, com.sun.jna.Pointer.NULL, com.sun.jna.ptr.IntByReference, com.sun.jna.ptr.NativeLongByReference, edu.umd.cs.findbugs.annotations.CheckForNull...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Job.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.501)
- **Top Global Matches:** file_cluster_5: 6.501, file_cluster_12: 9.356, file_cluster_7: 9.797
- **Magnitude:** 803.94 | **LOC:** 1732 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **77** in-repo importer(s); it depends on **114**; blast radius 1.36; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Connectivity (formerly Api Exposure) (96.9%), Guard Balance (formerly Safety Score) (69.7%), Concurrency Surface (formerly Concurrency) (49.7%)
- **Documentation Coverage:** 44.2553% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBuildStabilityHealthReport` **(I/O & Config Routines)** (Impact: 21.1)
  * `doRssChangelog` **(Generic / Templated Code)** (Impact: 17.6)
    * *Intent:* /** * RSS feed for changes in this project. * * @since 2.60 */
  * `onLoad` **(Defensive Guards)** (Impact: 15.9)
  * `getBuildHealthReports` **(I/O & Config Routines)** (Impact: 14.4)
  * `onLocationChanged` **(Defensive Guards)** (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 61 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 417`, `args: 122`, `func_start: 123`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 96`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 19`, `api: 124`, `concurrency: 13`, `import: 114`
* *Defense:* `safety: 34`, `doc: 74`, `sync_locks: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.36
  * `Choke Point (Betweenness):` 0.00059 | `Ripple Effect (Closeness):` 0.051567
  * `Imports (Out-Degree: 74):` com.infradna.tool.bridge_method_injector.WithBridgeMethods, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.BulkChange, hudson.EnvVars, hudson.Extension, hudson.ExtensionList...
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/Util.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.727)
- **Top Global Matches:** file_cluster_5: 6.727, file_cluster_12: 8.511, file_cluster_7: 9.83
- **Magnitude:** 776.84 | **LOC:** 1998 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **239** in-repo importer(s); it depends on **102**; blast radius 10.103; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.6%), Connectivity (formerly Api Exposure) (96.7%), Guard Balance (formerly Safety Score) (46.8%), Complexity Load (formerly Cognitive Load) (25.4%)
- **Documentation Coverage:** 18.2292% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `escape` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* /** * Escapes HTML unsafe characters like &lt;, &amp; to the respective character entities. */
  * `encode` **(Many-Argument Workhorses)** (Impact: 27.1)
  * `getTimeSpanString` **(Compute Cores)** (Impact: 25.9)
    * *Intent:* /** * Returns a human readable text of the time duration, for example "3 minutes 40 seconds". * This...
  * `getMethod` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `createDirectories` **(Defensive Guards)** (Impact: 23.1)
    * *Intent:* * * <p>If this method fails, * then it may do so after creating some, but not all, of the parent dir...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 55 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 395`, `args: 102`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 73`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 96`, `api: 97`, `concurrency: 3`, `import: 102`
* *Defense:* `safety: 205`, `doc: 87`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.103
  * `Choke Point (Betweenness):` 0.000587 | `Ripple Effect (Closeness):` 0.062205
  * `Imports (Out-Degree: 13):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.CheckReturnValue, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.model.TaskListener, hudson.util.QuotedStringTokenizer, hudson.util.VariableResolver...
  * `Imported By (In-Degree: 239):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/UpdateSite.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.013)
- **Top Global Matches:** file_cluster_5: 7.013, file_cluster_7: 9.191, file_cluster_12: 9.656
- **Magnitude:** 707.16 | **LOC:** 1768 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **66**; blast radius 0.413; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Connectivity (formerly Api Exposure) (83.7%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (30.6%)
- **Documentation Coverage:** 31.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Data` **(Defensive Guards)** (Impact: 26.1)
  * `deploy` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* * <p> * This is mainly intended to be called from the UI. The actual installation work happens * asy...
  * `Plugin` **(Defensive Guards)** (Impact: 23.6)
  * `getNeededDependencies` **(I/O & Config Routines)** (Impact: 16.4)
    * *Intent:* /** * Returns a list of dependent plugins which need to be installed or upgraded for this plugin to ...
  * `Entry` **(Many-Argument Workhorses)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 309`, `args: 103`, `func_start: 93`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 96`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 132`, `concurrency: 9`, `import: 66`
* *Defense:* `safety: 44`, `doc: 106`, `sync_locks: 1`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 7.5e-05 | `Ripple Effect (Closeness):` 0.040124
  * `Imports (Out-Degree: 23):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.ExtensionList, hudson.PluginManager, hudson.PluginWrapper, hudson.ProxyConfiguration...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Fingerprint.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.572)
- **Top Global Matches:** file_cluster_5: 6.572, file_cluster_12: 8.016, file_cluster_7: 9.499
- **Magnitude:** 697.32 | **LOC:** 1503 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **46**; blast radius 0.49; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Connectivity (formerly Api Exposure) (75.2%), Guard Balance (formerly Safety Score) (62.6%), Complexity Load (formerly Cognitive Load) (35.4%)
- **Documentation Coverage:** 44.898% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromString` **(Many-Argument Workhorses)** (Impact: 39.0)
    * *Intent:* /** * Parses a {@link RangeSet} from a string like "1-3,5,7-9" */
  * `removeAll` **(Compute Cores)** (Impact: 15.9)
    * *Intent:* /** * Updates this range set by removing all the values in the given range set. * * @return true if ...
  * `canDiscoverItem` **(Defensive Guards)** (Impact: 14.8)
    * *Intent:* /** * Checks if the current user can Discover the item. * If yes, it may be displayed as a text in F...
  * `retainAll` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* /** * Updates this range set by the intersection of this range and the given range. * * @return true...
  * `trim` **(I/O & Config Routines)** (Impact: 12.8)
    * *Intent:* /** * Trim off references to non-existent builds and jobs, thereby making the fingerprint smaller. *...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 283`, `args: 109`, `func_start: 105`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 79`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 101`, `concurrency: 19`, `import: 46`
* *Defense:* `safety: 47`, `doc: 63`, `sync_locks: 19`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 8e-05 | `Ripple Effect (Closeness):` 0.048469
  * `Imports (Out-Degree: 21):` com.infradna.tool.bridge_method_injector.WithBridgeMethods, com.thoughtworks.xstream.converters.Converter, com.thoughtworks.xstream.converters.MarshallingContext, com.thoughtworks.xstream.converters.UnmarshallingContext, com.thoughtworks.xstream.converters.basic.DateConverter, com.thoughtworks.xstream.converters.collections.CollectionConverter, com.thoughtworks.xstream.io.HierarchicalStreamReader, com.thoughtworks.xstream.io.HierarchicalStreamWriter...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `core/report-l10n.rb` (RUBY | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.382)
- **Top Global Matches:** file_cluster_1: 8.382, file_cluster_3: 48.619, file_cluster_8: 70.341
- **Magnitude:** 678.7 | **LOC:** 552 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.06; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.9%), Complexity Load (formerly Cognitive Load) (33.6%), Mutation Surface (formerly State Flux) (31.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` **(Compute Cores)** (Impact: 138.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 477`, `structural_boundaries: 2`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` set
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/model/Computer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.915)
- **Top Global Matches:** file_cluster_5: 5.915, file_cluster_12: 8.635, file_cluster_7: 8.848
- **Magnitude:** 630.68 | **LOC:** 1802 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **128** in-repo importer(s); it depends on **115**; blast radius 2.553; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (82.4%), Guard Balance (formerly Safety Score) (68.5%), Concurrency Surface (formerly Concurrency) (61.8%)
- **Documentation Coverage:** 26.7544% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doConfigSubmit` **(Compute Cores)** (Impact: 14.0)
    * *Intent:* /** * Accepts the update to the node configuration. */
  * `doConfigDotXml` **(Compute Cores)** (Impact: 12.0)
    * *Intent:* /** * Accepts {@code config.xml} submission, as well as serve it. */
  * `removeExecutor` **(Stateful Encapsulated Methods)** (Impact: 9.5)
    * *Intent:* /** * Called by {@link Executor} to kill excessive executors from this computer. */
  * `doRssLatest` **(Generic / Templated Code)** (Impact: 9.4)
    * *Intent:* /** * Retrieve the RSS feed for the last build for each project executed in this computer. * Only th...
  * `setNumExecutors` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* /** * Calling path, *means protected by Queue.withLock * * Computer.doConfigSubmit -> Computer.repla...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 404`, `args: 119`, `func_start: 116`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 80`, `state_mutation: 54`, `planned_debt: 9`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 132`, `concurrency: 17`, `import: 115`
* *Defense:* `safety: 27`, `doc: 90`, `sync_locks: 6`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.553
  * `Choke Point (Betweenness):` 0.000517 | `Ripple Effect (Closeness):` 0.053907
  * `Imports (Out-Degree: 64):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.OverrideMustInvoke, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.EnvVars, hudson.Extension, hudson.Launcher.ProcStarter...
  * `Imported By (In-Degree: 128):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Descriptor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.242)
- **Top Global Matches:** file_cluster_5: 6.242, file_cluster_7: 9.844, file_cluster_12: 9.97
- **Magnitude:** 595.54 | **LOC:** 1335 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **163** in-repo importer(s); it depends on **74**; blast radius 4.533; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Connectivity (formerly Api Exposure) (85.8%), Guard Balance (formerly Safety Score) (79.2%), Complexity Load (formerly Cognitive Load) (31.7%)
- **Documentation Coverage:** 26.4151% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newInstancesFromHeteroList` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* /** * @since 2.475 */
  * `getStaticHelpUrl` **(Generic / Templated Code)** (Impact: 15.2)
    * *Intent:* /** * @since 2.475 */
  * `getHelpFile` **(Defensive Guards)** (Impact: 13.4)
  * `buildFillDependencies` **(Stateful Encapsulated Methods)** (Impact: 13.3)
  * `doHelpImpl` **(Stateful Encapsulated Methods)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 308`, `args: 84`, `func_start: 88`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 61`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `api: 81`, `concurrency: 2`, `import: 74`
* *Defense:* `safety: 43`, `doc: 63`, `sync_locks: 2`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.533
  * `Choke Point (Betweenness):` 0.000176 | `Ripple Effect (Closeness):` 0.055385
  * `Imports (Out-Degree: 21):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.BulkChange, hudson.DescriptorExtensionList, hudson.ExtensionList, hudson.PluginWrapper...
  * `Imported By (In-Degree: 163):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/AbstractBuild.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.804)
- **Top Global Matches:** file_cluster_5: 6.804, file_cluster_7: 10.318, file_cluster_12: 10.453
- **Magnitude:** 575.98 | **LOC:** 1419 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **90** in-repo importer(s); it depends on **69**; blast radius 1.118; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (75.2%), Concurrency Surface (formerly Concurrency) (31.9%)
- **Documentation Coverage:** 38.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Defensive Guards)** (Impact: 25.3)
  * `reportError` **(Stateful Encapsulated Methods)** (Impact: 14.5)
  * `createLauncher` **(Stateful Encapsulated Methods)** (Impact: 14.4)
    * *Intent:* /** * Creates a {@link Launcher} that this build will use. This can be overridden by derived types *...
  * `tearDownBuildEnvironments` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* /** * Tear down all build environments (in reverse order). * <p> * Returns a failure {@link Result} ...
  * `getUpstreamRelationship` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* /** * Gets the dependency relationship from this build (as the sink) * and that project (as the sour...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 48 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 263`, `args: 66`, `func_start: 75`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 65`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `api: 85`, `concurrency: 6`, `import: 69`
* *Defense:* `safety: 56`, `doc: 60`, `sync_locks: 2`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.118
  * `Choke Point (Betweenness):` 0.000256 | `Ripple Effect (Closeness):` 0.04381
  * `Imports (Out-Degree: 52):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, hudson.AbortException, hudson.EnvVars, hudson.FilePath, hudson.Functions, hudson.Launcher, hudson.Util...
  * `Imported By (In-Degree: 90):` (Excluded from Brief to save tokens)

### `test/src/test/java/hudson/model/QueueTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.853)
- **Top Global Matches:** file_cluster_5: 6.853, file_cluster_12: 7.412, file_cluster_7: 9.05
- **Magnitude:** 560.28 | **LOC:** 1562 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **114**; blast radius 0.125; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.6%), Connectivity (formerly Api Exposure) (58.7%), Guard Balance (formerly Safety Score) (51.3%), Complexity Load (formerly Cognitive Load) (46.9%)
- **Documentation Coverage:** 92.1348% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pendingsConsistenceAfterErrorDuringMaintain` **(Annotated & Test Methods)** (Impact: 11.9)
  * `queueApiOutputShouldBeFilteredByUserPermission` **(I/O & Config Routines)** (Impact: 10.2)
  * `waitUntilWaitingListIsEmpty` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `flyweightTasks` **(Annotated & Test Methods)** (Impact: 6.2)
  * `checkCancelOperationUsingUrl` **(Stateful Encapsulated Methods)** (Impact: 5.9)
    * *Intent:* /** * * @param urlProvider the endpoint to query * @param legacyRedirect whether the endpoint has th...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 94
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 444`, `args: 118`, `func_start: 98`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 99`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 11`, `api: 92`, `concurrency: 44`, `import: 114`
* *Defense:* `safety: 22`, `doc: 9`, `test: 181`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.125
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.000444
  * `Imports (Out-Degree: 41):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, hudson.ExtensionList, hudson.Functions, hudson.Launcher, hudson.XmlFile, hudson.matrix.AxisList, hudson.matrix.MatrixBuild...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/Launcher.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.765)
- **Top Global Matches:** file_cluster_5: 6.765, file_cluster_12: 8.853, file_cluster_7: 9.829
- **Magnitude:** 555.2 | **LOC:** 1500 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **100** in-repo importer(s); it depends on **41**; blast radius 2.401; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (96.3%), Guard Balance (formerly Safety Score) (59.0%), Mutation Surface (formerly State Flux) (54.5%), Debt Markers (formerly Tech Debt) (40.9%)
- **Documentation Coverage:** 50.4132% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printCommandLine` **(Stateful Encapsulated Methods)** (Impact: 16.8)
    * *Intent:* /** * Prints out the command line to the listener so that users know what we are doing. */
  * `call` **(Annotated & Test Methods)** (Impact: 12.9)
  * `launch` **(Compute Cores)** (Impact: 11.1)
  * `maskedPrintCommandLine` **(Stateful Encapsulated Methods)** (Impact: 10.8)
    * *Intent:* /** * Prints out the command line to the listener with some portions masked to prevent sensitive inf...
  * `launch` **(Defensive Guards)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 296`, `args: 128`, `func_start: 127`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 1`, `state_mutation: 59`, `planned_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `io: 67`, `api: 136`, `concurrency: 4`, `import: 41`
* *Defense:* `safety: 68`, `doc: 64`, `sync_locks: 2`, `immutability_locks: 57`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.401
  * `Choke Point (Betweenness):` 0.000253 | `Ripple Effect (Closeness):` 0.052577
  * `Imports (Out-Degree: 22):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.Proc.LocalProc, hudson.Proc.ProcWithJenkins23271Patch, hudson.model.Computer, hudson.model.Node, hudson.model.Run...
  * `Imported By (In-Degree: 100):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/View.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.868)
- **Top Global Matches:** file_cluster_5: 5.868, file_cluster_12: 8.244, file_cluster_7: 9.567
- **Magnitude:** 529.22 | **LOC:** 1286 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **53** in-repo importer(s); it depends on **97**; blast radius 1.283; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.1%), Connectivity (formerly Api Exposure) (91.1%), Guard Balance (formerly Safety Score) (60.0%), Concurrency Surface (formerly Concurrency) (20.3%)
- **Documentation Coverage:** 31.3187% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doItemCategories` **(Many-Argument Workhorses)** (Impact: 24.9)
    * *Intent:* /** * An API REST method to get the allowed {$link TopLevelItem}s and its categories. * * @return A ...
  * `create` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* /** * @since 2.475 */
  * `filterQueueItemTest` **(Stateful Encapsulated Methods)** (Impact: 13.6)
  * `isRelevant` **(Stateful Encapsulated Methods)** (Impact: 9.2)
  * `copy` **(Stateful Encapsulated Methods)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 335`, `args: 93`, `func_start: 95`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 49`
* *Architecture:* `io: 6`, `api: 102`, `concurrency: 7`, `import: 97`
* *Defense:* `safety: 29`, `doc: 65`, `sync_locks: 7`, `immutability_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.283
  * `Choke Point (Betweenness):` 0.000257 | `Ripple Effect (Closeness):` 0.048649
  * `Imports (Out-Degree: 58):` com.thoughtworks.xstream.converters.ConversionException, com.thoughtworks.xstream.io.StreamException, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.DescriptorExtensionList, hudson.Extension, hudson.ExtensionPoint, hudson.Functions...
  * `Imported By (In-Degree: 53):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/PluginWrapper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.796)
- **Top Global Matches:** file_cluster_5: 6.796, file_cluster_12: 9.19, file_cluster_7: 9.76
- **Magnitude:** 528.36 | **LOC:** 1441 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); it depends on **59**; blast radius 1.663; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.3%), Connectivity (formerly Api Exposure) (86.1%), Guard Balance (formerly Safety Score) (66.8%), Complexity Load (formerly Cognitive Load) (17.4%)
- **Documentation Coverage:** 47.8873% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolvePluginDependencies` **(I/O & Config Routines)** (Impact: 25.1)
    * *Intent:* /** * Makes sure that all the dependencies exist, and then accept optional dependencies * as real de...
  * `disable` **(Defensive Guards)** (Impact: 22.1)
    * *Intent:* /** * Disable this plugin using a strategy. * @param strategy strategy to use * @return an object re...
  * `Dependency` **(Compute Cores)** (Impact: 9.6)
  * `getDeprecations` **(Generic / Templated Code)** (Impact: 7.0)
  * `PluginWrapper` **(Many-Argument Workhorses)** (Impact: 6.8)
    * *Intent:* /** * @param archive * A .jpi archive file jar file, or a .jpl linked plugin. * @param manifest * Th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 267`, `args: 126`, `func_start: 111`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 52`, `fragile_debt: 1`
* *Architecture:* `io: 15`, `api: 115`, `import: 59`
* *Defense:* `safety: 34`, `doc: 75`, `immutability_locks: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.663
  * `Choke Point (Betweenness):` 9.1e-05 | `Ripple Effect (Closeness):` 0.050284
  * `Imports (Out-Degree: 17):` com.google.common.collect.Sets, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, hudson.PluginManager.PluginInstanceStore, hudson.PluginWrapper.PluginDisableStatus.ALREADY_DISABLED, hudson.PluginWrapper.PluginDisableStatus.DISABLED, hudson.PluginWrapper.PluginDisableStatus.ERROR_DISABLING, hudson.PluginWrapper.PluginDisableStatus.NOT_DISABLED_DEPENDANTS...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/security/HudsonPrivateSecurityRealm.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.444)
- **Top Global Matches:** file_cluster_5: 7.444, file_cluster_12: 8.373, file_cluster_7: 9.099
- **Magnitude:** 464.62 | **LOC:** 1189 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **77**; blast radius 0.254; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.6%), Guard Balance (formerly Safety Score) (63.9%), Connectivity (formerly Api Exposure) (56.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.7%)
- **Documentation Coverage:** 69.0909% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateAccountCreationForm` **(Many-Argument Workhorses)** (Impact: 30.7)
    * *Intent:* /** * @param req the request to process * @param validateCaptcha whether to attempt to validate a ca...
  * `newInstance` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `createAccountWithHashedPassword` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* /** * Creates a new user account by registering a Hashed password with the user. * * @param userName...
  * `doFilter` **(Type Conversions)** (Impact: 10.8)
  * `isPasswordHashed` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /** * Returns true if the supplied password starts with a prefix indicating it is already hashed. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 285`, `args: 96`, `func_start: 94`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 39`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 81`, `concurrency: 2`, `import: 77`
* *Defense:* `safety: 27`, `doc: 38`, `sync_locks: 2`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.254
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.034201
  * `Imports (Out-Degree: 24):` edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.Extension, hudson.ExtensionList, hudson.Util, hudson.model.Descriptor, hudson.model.ManagementLink, hudson.model.ModelObject...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `test/src/test/java/hudson/model/DirectoryBrowserSupportTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.813)
- **Top Global Matches:** file_cluster_5: 6.813, file_cluster_7: 8.602, file_cluster_12: 8.958
- **Magnitude:** 453.48 | **LOC:** 1538 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **77**; blast radius 0.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.6%), Complexity Load (formerly Cognitive Load) (13.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.4%), Connectivity (formerly Api Exposure) (10.9%)
- **Documentation Coverage:** 98.8764% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `root` **(Annotated & Test Methods)** (Impact: 12.6)
  * `root` **(Annotated & Test Methods)** (Impact: 12.3)
  * `zipDownloadFileLeakMx` **(I/O & Config Routines)** (Impact: 10.8)
  * `child` **(Defensive Guards)** (Impact: 7.6)
  * `child` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 313`, `args: 105`, `func_start: 103`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 66`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 48`, `unreferenced_by_name: 24`
* *Architecture:* `io: 67`, `api: 80`, `import: 77`
* *Defense:* `safety: 21`, `doc: 13`, `test: 131`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` com.sun.management.UnixOperatingSystemMXBean, edu.umd.cs.findbugs.annotations.NonNull, hudson.ExtensionList, hudson.FilePath, hudson.Functions, hudson.Launcher, hudson.Util, hudson.model.WindowsUtil.isWindowsSymlinkSupported...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `core/src/main/java/hudson/model/FreeStyleBuild.java` (JAVA) | Magnitude: 9.0 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 9, api: 4, args: 3
- `core/src/main/java/jenkins/widgets/HistoryPageEntry.java` (JAVA) | Magnitude: 19.32 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 9, args: 8, branch: 5
- `core/src/main/java/jenkins/model/item_category/Category.java` (JAVA) | Magnitude: 25.22 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 18, api: 8, decorators: 8
- `test/src/test/java/jenkins/bugs/Jenkins19124Test.java` (JAVA) | Magnitude: 32.54 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 42, import: 23, api: 9
- `core/src/main/java/jenkins/SlaveToMasterFileCallable.java` (JAVA) | Magnitude: 9.64 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 15, import: 7, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `core/src/main/resources/jenkins/management/AsynchronousAdministrativeMonitor/log.groovy` (GROOVY) | Magnitude: 15.38 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 3, branch: 2, core_var_decl: 2
- `core/src/main/java/jenkins/security/s2m/JarURLValidatorImpl.java` (JAVA) | Magnitude: 24.86 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 37, import: 18, args: 11
- `core/src/main/resources/hudson/diagnosis/ReverseProxySetupMonitor/resources.js` (JAVASCRIPT) | Magnitude: 16.74 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 11, core_var_decl: 9, branch: 8
- `src/main/scss/components/_breadcrumbs.scss` (CSS) | Magnitude: 1.14 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 208, closures: 29, ui_framework: 17, immutability_locks: 14
- `src/main/js/components/notifications/index.js` (JAVASCRIPT) | Magnitude: 76.96 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 63, state_mutation: 17, branch: 8, globals: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `core/src/main/java/hudson/scm/EditType.java` (JAVA) | Magnitude: 16.8 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 11, api: 9, immutability_locks: 5
- `src/main/scss/components/_notifications.scss` (CSS) | Magnitude: 0.44 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 89, closures: 8, class_start: 6, func_start: 4
- `src/main/scss/pages/_about.scss` (CSS) | Magnitude: 0.36 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 103, ui_framework: 7, closures: 6, class_start: 4
- `core/src/main/java/hudson/util/CompressedFile.java` (JAVA) | Magnitude: 45.92 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 43, io: 24, import: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `core/src/main/java/hudson/cli/CLICommand.java` (JAVA) | Magnitude: 160.08 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 106, import: 41, args: 36
- `core/src/main/java/jenkins/mvn/GlobalMavenConfig.java` (JAVA) | Magnitude: 19.38 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 21, api: 7, import: 7
- `test/src/test/java/jenkins/model/NodeListenerTest.java` (JAVA) | Magnitude: 11.58 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 42, indent_spaces: 31, import: 19, test: 7
- `core/src/main/java/hudson/security/UnwrapSecurityExceptionFilter.java` (JAVA) | Magnitude: 26.64 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 20, import: 11, safety: 7
- `core/src/test/java/jenkins/org/apache/commons/validator/routines/UrlValidatorTest.java` (JAVA) | Magnitude: 205.46 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 548, test: 185, structural_boundaries: 178, core_var_decl: 87

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `core/src/main/java/hudson/cli/CliCrumbExclusion.java` (JAVA) | Magnitude: 6.96 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 16, import: 9, indent_spaces: 9, ssr_boundaries: 4
- `test/src/test/java/hudson/model/ListViewTest.java` (JAVA) | Magnitude: 130.84 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 314, structural_boundaries: 168, core_var_decl: 77, design_snake_case: 73
- `core/src/main/java/hudson/util/HudsonIsRestarting.java` (JAVA) | Magnitude: 14.28 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, import: 6, api: 5
- `test/src/test/java/jenkins/model/ContextMenuTest.java` (JAVA) | Magnitude: 27.68 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 41, import: 22, decorators: 12
- `core/src/test/java/hudson/util/io/RewindableRotatingFileOutputStreamTest.java` (JAVA) | Magnitude: 17.04 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 37, io: 15, import: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `war/src/main/webapp/help/system-config/systemMessage.html` (HTML) | Magnitude: 13.12 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, io: 2, args: 1
- `core/src/main/java/jenkins/I18n.java` (JAVA) | Magnitude: 43.76 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 22, safety_bypasses: 12, core_var_decl: 12
- `war/src/main/webapp/help/system-config/systemMessage_it.html` (HTML) | Magnitude: 13.12 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, io: 2, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `core/src/main/java/hudson/util/ChunkedOutputStream.java` (JAVA) | Magnitude: 55.36 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 29, api: 12, doc: 12
- `core/src/main/resources/jenkins/security/apitoken/LegacyApiTokenAdministrativeMonitor/resources.js` (JAVASCRIPT) | Magnitude: 92.46 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 46, core_var_decl: 43, design_camel_case: 26
- `core/src/main/java/jenkins/security/stapler/StaplerFilteredActionListener.java` (JAVA) | Magnitude: 16.82 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 24, import: 12, args: 5
- `core/src/main/java/hudson/model/labels/LabelAssignmentAction.java` (JAVA) | Magnitude: 3.74 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 11, import: 8, api: 2, doc: 2
- `core/src/main/java/jenkins/model/ModelObjectWithChildren.java` (JAVA) | Magnitude: 16.28 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 27, indent_spaces: 18, import: 8, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `core/src/main/java/hudson/scheduler/BaseParser.java` (JAVA) | Magnitude: 80.32 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 24, branch: 15, api: 12
- `core/src/main/java/hudson/tasks/_maven/MavenConsoleAnnotator.java` (JAVA) | Magnitude: 28.64 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 15, import: 6, core_var_decl: 6
- `core/src/main/java/hudson/console/PlainTextConsoleOutputStream.java` (JAVA) | Magnitude: 18.98 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 17, import: 8, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/main/js/app.js` (JAVASCRIPT) | Magnitude: 15.4 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, import: 10
- `.github/workflows/label-conflicting-pr.yml` (YAML) | Magnitude: 16.38 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, args: 4, branch: 2, structural_boundaries: 2
- `core/src/main/java/hudson/util/NoHomeDir.java` (JAVA) | Magnitude: 5.76 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, io: 3, api: 3
- `core/src/main/java/jenkins/util/xstream/CriticalXStreamException.java` (JAVA) | Magnitude: 3.78 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, api: 2, import: 2
- `core/src/main/java/hudson/AbortException.java` (JAVA) | Magnitude: 5.9 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, api: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/main/scss/form/_select.scss` (CSS) | Magnitude: 0.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 61, closures: 8, ui_framework: 3, class_start: 2
- `src/main/js/pages/cloud-set/index.scss` (CSS) | Magnitude: 0.83 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 23, ui_framework: 5, closures: 3, class_start: 2
- `core/src/main/resources/hudson/PluginWrapper/uninstall.groovy` (GROOVY) | Magnitude: 15.34 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 5, core_var_decl: 3, design_snake_case: 3
- `core/src/main/java/hudson/security/UserMayOrMayNotExistException2.java` (JAVA) | Magnitude: 6.72 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, api: 3, args: 2
- `src/main/scss/form/_input.scss` (CSS) | Magnitude: 0.79 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, closures: 5, branch: 1, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `core/src/main/java/jenkins/model/queue/ItemDeletion.java` (JAVA) | Magnitude: 87.7 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 58, branch: 29, import: 28
- `core/src/main/resources/lib/form/confirm.js` (JAVASCRIPT) | Magnitude: 1.69 | Delta: **0.208** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 120, branch: 31, structural_boundaries: 28, core_var_decl: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `core/src/main/java/hudson/slaves/CloudRetentionStrategy.java` (JAVA) | Magnitude: 15.08 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 15, import: 8, api: 5
- `core/src/main/java/jenkins/agents/WebSocketAgents.java` (JAVA) | Magnitude: 70.86 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 71, import: 36, args: 26
- `core/src/test/java/jenkins/model/JenkinsLocationConfigurationTest.java` (JAVA) | Magnitude: 13.78 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 13, test: 11, import: 7
- `test/src/test/java/hudson/PluginManagerTest.java` (JAVA) | Magnitude: 217.14 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 634, structural_boundaries: 250, test: 112, core_var_decl: 110
- `core/src/main/java/jenkins/websocket/WebSockets.java` (JAVA) | Magnitude: 54.48 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 37, import: 15, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `core/src/main/java/jenkins/security/ResourceDomainRootAction.java` (JAVA) | Magnitude: 99.58 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 185, structural_boundaries: 79, core_var_decl: 42, import: 34
- `test/src/test/java/lib/form/ExpandableTextboxTest.java` (JAVA) | Magnitude: 44.68 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 68, import: 32, core_var_decl: 27
- `core/src/main/java/hudson/init/impl/InstallUncaughtExceptionHandler.java` (JAVA) | Magnitude: 57.18 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 43, import: 20, branch: 9
- `src/main/scss/components/_details.scss` (CSS) | Magnitude: 0.92 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 65, ui_framework: 10, immutability_locks: 4, class_start: 3
- `test/src/test/java/lib/layout/StopButtonTest.java` (JAVA) | Magnitude: 41.24 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 42, import: 20, core_var_decl: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `cli/src/main/java/hudson/cli/HexDump.java` (JAVA) | Magnitude: 35.0 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, branch: 9, core_var_decl: 7, structural_boundaries: 5
- `core/src/main/java/jenkins/security/BasicApiTokenHelper.java` (JAVA) | Magnitude: 14.4 | Delta: **0.232** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 17, import: 9, branch: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/src/main/java/hudson/model/Queue.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 1274.06
- `core/src/main/java/hudson/PluginManager.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 1255.76
- `core/src/main/java/hudson/model/UpdateCenter.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 1251.8
- `core/src/main/java/hudson/util/ProcessTree.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 875.5
- `core/src/main/java/hudson/model/Fingerprint.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 697.32

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/src/main/java/jenkins/model/Jenkins.java` -> **Severity: 0.469** (Bridge: 0.0051 * Flux: 92.8076%)
- `core/src/main/java/hudson/Functions.java` -> **Severity: 0.108** (Bridge: 0.0011 * Flux: 97.1796%)
- `core/src/main/java/hudson/model/AbstractProject.java` -> **Severity: 0.06** (Bridge: 0.0006 * Flux: 97.5779%)
- `core/src/main/java/hudson/model/Job.java` -> **Severity: 0.059** (Bridge: 0.0006 * Flux: 99.3408%)
- `core/src/main/java/hudson/model/Run.java` -> **Severity: 0.059** (Bridge: 0.0006 * Flux: 99.07%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `core/src/main/java/jenkins/model/Jenkins.java` -> **Severity: 4.893** (Embedded: 0.0714 * Error Risk: 68.5248%)
- `core/src/main/java/hudson/Functions.java` -> **Severity: 4.455** (Embedded: 0.0557 * Error Risk: 80.0%)
- `core/src/main/java/hudson/model/Descriptor.java` -> **Severity: 4.386** (Embedded: 0.0554 * Error Risk: 79.1914%)
- `core/src/main/java/jenkins/util/SystemProperties.java` -> **Severity: 4.37** (Embedded: 0.0579 * Error Risk: 75.4545%)
- `core/src/main/java/hudson/model/AbstractProject.java` -> **Severity: 4.137** (Embedded: 0.0517 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/src/main/java/jenkins/YesNoMaybe.java` -> **Severity: 973.4** (Blast Radius: 9.734 * Doc Risk: 100.0%)
- `core/src/main/java/jenkins/model/Jenkins.java` -> **Severity: 716.438** (Blast Radius: 15.62 * Doc Risk: 45.8667%)
- `core/src/main/java/org/acegisecurity/Authentication.java` -> **Severity: 221.947** (Blast Radius: 2.296 * Doc Risk: 96.6667%)
- `core/src/main/java/hudson/ExtensionList.java` -> **Severity: 216.097** (Blast Radius: 5.818 * Doc Risk: 37.1429%)
- `core/src/main/java/hudson/Functions.java` -> **Severity: 205.923** (Blast Radius: 5.168 * Doc Risk: 39.8458%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 291 literal sites + 19 sites through wrappers = 310
- **`panics_and_aborts`:** 1664 literal sites + 69 sites through wrappers = 1733

- `fileToPath` (function, panics_and_aborts, primitive): 32 call sites in 4 files -- `core/src/main/java/hudson/Util.java`
- `assertPrintThrowable` (function, debug_prints, primitive): 10 call sites in 1 files -- `core/src/test/java/hudson/FunctionsTest.java`
- `check` (function, debug_prints, primitive): 7 call sites in 1 files -- `cli/src/test/java/hudson/util/QuotedStringTokenizerTest.java`
- `error` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `core/src/main/java/hudson/scheduler/BaseParser.java`
- `assertReachableWithoutOk` (function, panics_and_aborts, primitive): 4 call sites in 2 files -- `test/src/test/java/jenkins/security/stapler/StaplerAbstractTest.java`
- `_onModified` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `core/src/main/java/hudson/util/PersistedList.java`
- `checkChannel` (function, panics_and_aborts, primitive): 3 call sites in 2 files -- `core/src/main/java/hudson/cli/CLICommand.java`
- `throwVerificationFailure` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `core/src/main/java/hudson/model/UpdateCenter.java`
- `_swap` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `core/src/main/java/jenkins/slaves/StandardOutputSwapper.java`
- `asPath` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `core/src/main/java/hudson/util/StreamTaskListener.java`
- `doBuild` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `core/src/main/java/hudson/model/AbstractProject.java`
- `doBuildWithParameters` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `core/src/main/java/hudson/model/AbstractProject.java`
*(+11 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 74887 call pairs -- scoped 31.3%, unique 0.7%, ambiguous 25.7%, external 42.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 72605 | 31.8% | 0.7% | 26.4% | 41.1% |
| javascript | 2138 | 18.6% | 0.0% | 1.4% | 80.0% |
| groovy | 69 | 1.4% | 1.4% | 15.9% | 81.2% |
| python | 29 | 17.2% | 0.0% | 0.0% | 82.8% |
| ruby | 26 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 18 | 0.0% | 0.0% | 0.0% | 100.0% |
| c | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
