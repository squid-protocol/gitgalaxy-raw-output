# ARCHITECTURAL_BRIEF: jenkins
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jenkinsci/jenkins` |
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
| Total Artifacts | 12362 |
| Analyzed Artifacts (Scanned) | 11977 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 385 |
| Total LOC | 249769 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.9% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1542 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 146 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 7512 | 0 | 62.7% |
| JAVA | 1905 | 202718 | 15.9% |
| XML | 1223 | 22 | 10.2% |
| HTML | 1019 | 21493 | 8.5% |
| JAVASCRIPT | 123 | 11159 | 1.0% |
| CSS | 88 | 10925 | 0.7% |
| GROOVY | 64 | 1209 | 0.5% |
| JSON | 28 | 1461 | 0.2% |
| MARKDOWN | 5 | 0 | 0.0% |
| SHELL | 4 | 102 | 0.0% |
| BATCH | 3 | 31 | 0.0% |
| RUBY | 1 | 525 | 0.0% |
| C | 1 | 15 | 0.0% |
| PYTHON | 1 | 109 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4450 | 37.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7517 | 62.8% |
| Static: Minified & Vendor Opaque Mass | 10 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 385*

**Composition by Extension & Reason:**
- `.gif`: 109x Excluded (Explicitly Denied Extension: '.gif')
- `.png`: 69x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 53x Unsupported Format (.undeterminable), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 33x Excluded (Explicitly Denied Extension: '.zip')
- `.hpi`: 18x Excluded (Binary Format Detected)
- `.hint`: 14x Unsupported Format (.hint)
- `.yml`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 9x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.xml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 61 exceeds 500 chars)
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.jpi`: 5x Excluded (Binary Format Detected)
- `.g4`: 4x Unsupported Format (.g4)
- `.04`: 4x Unsupported Format (.04)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 1787 commas in 521 LOC)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 5925 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.1 | 22.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 46.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.9 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 29.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 86.6 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1328 | 518 | 0 | `test/src/test/java/hudson/cli/DeleteBuildsCommandTest.java` |
| cleanup | 191 | 109 | 0 | `test/src/test/java/jenkins/security/stapler/Security400Test.java` |
| guards | 21969 | 1748 | 3 | `core/src/main/java/hudson/FilePath.java` |
| danger | 12033 | 1396 | 1 | `core/src/main/java/jenkins/model/Jenkins.java` |
| concurrency | 2596 | 369 | 0 | `core/src/main/java/jenkins/model/Jenkins.java` |
| connectivity | 18155 | 1696 | 3 | `core/src/main/java/jenkins/model/Jenkins.java` |
| io | 5506 | 742 | 0 | `core/src/main/java/hudson/FilePath.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 25 | 9 | 0 | `core/src/main/java/hudson/Proc.java` |
| time | 513 | 132 | 0 | `core/src/test/java/hudson/scheduler/CronTabDayOfWeekLocaleTest.java` |
| serialization | 33 | 17 | 0 | `core/src/main/java/jenkins/util/xml/XMLUtils.java` |
| regex | 166 | 85 | 0 | `war/src/main/webapp/scripts/hudson-behavior.js` |
| events | 2029 | 416 | 0 | `core/src/main/java/jenkins/model/Jenkins.java` |
| tests | 16213 | 623 | 0 | `test/src/test/java/hudson/cli/RunRangeCommandTest.java` |
| docs | 8626 | 1533 | 1 | `core/src/main/java/jenkins/model/Jenkins.java` |
| debt | 1461 | 506 | 0 | `test/src/test/java/hudson/model/DirectoryBrowserSupportTest.java` |
| mutation | 41675 | 1936 | 5 | `core/src/main/java/jenkins/model/Jenkins.java` |
| dead_code | 6169 | 1168 | 0 | `test/src/test/java/jenkins/security/stapler/DoActionFilterTest.java` |
| credential | 38 | 21 | 0 | `test/src/test/resources/hudson/model/hudson.tools.JDKInstaller.json.html` |
| threat | 319 | 143 | 0 | `core/src/main/java/hudson/ClassicPluginStrategy.java` |
| ml_ai | 192 | 78 | 0 | `core/src/main/java/hudson/slaves/NodeProvisioner.java` |
| ui | 1155 | 250 | 0 | `src/main/scss/pages/_dashboard.scss` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `core/src/main/java/hudson/FilePath.java` (Hits: 271)
- `core/src/test/java/jenkins/util/VirtualFileTest.java` (Hits: 251)
- `core/src/test/java/jenkins/util/io/PathRemoverTest.java` (Hits: 150)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Jenkins.java** (`core/src/main/java/jenkins/model/Jenkins.java`) — 511 inbound connections
2. **Extension.java** (`core/src/main/java/hudson/Extension.java`) — 429 inbound connections
3. **Util.java** (`core/src/main/java/hudson/Util.java`) — 217 inbound connections
4. **ExtensionList.java** (`core/src/main/java/hudson/ExtensionList.java`) — 205 inbound connections
5. **Symbol.java** (`core/src/main/java/org/jenkins/ui/symbol/Symbol.java`) — 188 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Jenkins.java** (`core/src/main/java/jenkins/model/Jenkins.java`) — 317 outbound dependencies
2. **Functions.java** (`core/src/main/java/hudson/Functions.java`) — 167 outbound dependencies
3. **PluginManager.java** (`core/src/main/java/hudson/PluginManager.java`) — 154 outbound dependencies
4. **Run.java** (`core/src/main/java/hudson/model/Run.java`) — 125 outbound dependencies
5. **FilePath.java** (`core/src/main/java/hudson/FilePath.java`) — 118 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__global_context__` (@ `core/report-l10n.rb`) -> Impact: **496.2** | LOC: 363
- `createPluginSetupWizard` (@ `src/main/js/pluginSetupWizardGui.js`) -> Impact: **348.1** | LOC: 1419
  * *Intent:* // Setup the dialog, exported
- `printThrowable` (@ `core/src/test/java/hudson/FunctionsTest.java`) -> Impact: **210.3** | LOC: 226
- `Anonymous_Block_[Truncated]` (@ `core/report-l10n.rb`) -> Impact: **138.7** | LOC: 134
- `serveFile` (@ `core/src/main/java/hudson/model/DirectoryBrowserSupport.java`) -> Impact: **118.6** | LOC: 217
- `_main` (@ `cli/src/main/java/hudson/cli/CLI.java`) -> Impact: **92.5** | LOC: 209
- `doXml` (@ `core/src/main/java/hudson/model/Api.java`) -> Impact: **84.8** | LOC: 108
  * *Intent:* /** * Exposes the bean as XML. */
- `buildFormTree` (@ `core/src/main/resources/jenkins/formelementpath/form-element-path.js`) -> Impact: **80.1** | LOC: 188
  * *Intent:* // most of this is copied from hudson-behaviour.js
- `maintain` (@ `core/src/main/java/hudson/model/Queue.java`) -> Impact: **78.8** | LOC: 237
  * *Intent:* /** * Queue maintenance. * * <p> * Move projects between {@link #waitingList}, {@link #blockedProjects}, {@link #buildables}, and {@link #pendings} * ...
- `verifyChecksums` (@ `core/src/main/java/hudson/model/UpdateCenter.java`) -> Impact: **78.7** | LOC: 53
  * *Intent:* /** * Implements the checksum verification logic with fallback to weaker algorithm for {@link DownloadJob}. * @param job The job downloading the file ...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `core/src/main/java/hudson/model` | 170 | 21507.6 | 13.41% | 20.57% |
| `core/src/main/java/hudson` | 50 | 9991.14 | 15.27% | 19.84% |
| `core/src/main/java/hudson/util` | 122 | 8330.18 | 14.41% | 23.38% |
| `test/src/test/java/hudson/model` | 84 | 6958.68 | 17.2% | 0.0% |
| `core/src/main/java/jenkins/model` | 69 | 4970.22 | 7.96% | 24.55% |
| `war/src/main/webapp/scripts` | 9 | 2652.6 | 31.35% | 55.27% |
| `core/src/main/java/hudson/security` | 45 | 2430.62 | 11.57% | 33.36% |
| `test/src/test/java/hudson/cli` | 48 | 2425.76 | 12.8% | 0.0% |
| `core/src/main/java/hudson/slaves` | 33 | 2359.9 | 11.02% | 27.02% |
| `test/src/test/java/jenkins/security` | 45 | 2122.56 | 21.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `core/src/main/java/hudson/PluginStrategy.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/cli/declarative/MethodBinder.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/model/ResourceController.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/model/queue/QueueTaskFilter.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/search/SearchItems.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `war/src/main/webapp/WEB-INF/hudson` -> **100.0%** Exposure
- `cli/src/main/java/hudson/util/QuotedStringTokenizer.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/model/RSS.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/ArgumentListBuilder.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/ByteArrayOutputStream2.java` -> **100.0%** Exposure
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
- **Binary Anomalies (X-Ray):** `29` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `27645` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `core/src/main/resources/lib/form/select/select.js` (JAVASCRIPT) -> Cumulative Risk: **695.39**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3.53 | **LOC:** 191 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (97.9682%), Cognitive Load (96.5807%)
- **Heaviest Functions:** `updateListBox` (Impact: 47.5), `onSuccess` (Impact: 13.1), `hasChanged` (Impact: 12.9)

### 2. `src/main/js/components/notifications/index.js` (JAVASCRIPT) -> Cumulative Risk: **676.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 76.96 | **LOC:** 79 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `init` (Impact: 11.7), `show` (Impact: 9.7), `init` (Impact: 3.6)

### 3. `src/main/js/components/dropdowns/autocomplete.js` (JAVASCRIPT) -> Cumulative Risk: **663.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 84.06 | **LOC:** 117 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `init` (Impact: 19.6), `updateSuggestions` (Impact: 14.6), `convertSuggestionToItem` (Impact: 6.2)

### 4. `core/src/main/java/jenkins/telemetry/impl/UserLanguages.java` (JAVA) -> Cumulative Risk: **657.93**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 56.56 | **LOC:** 110 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%), Tech Debt (99.6728%)
- **Heaviest Functions:** `handle` (Impact: 7.6), `createContent` (Impact: 4.7), `getId` (Impact: 1.2)

### 5. `core/src/main/java/hudson/slaves/SimpleScheduledRetentionStrategy.java` (JAVA) -> Cumulative Risk: **648.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 158.96 | **LOC:** 289 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9912%), Documentation (85.7143%), Cognitive Load (83.73%)
- **Heaviest Functions:** `check` (Impact: 32.9), `updateStartStopWindow` (Impact: 9.7), `doCheck` (Impact: 3.3)

### 6. `core/src/main/java/hudson/model/AbstractCIBase.java` (JAVA) -> Cumulative Risk: **633.76**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 149.02 | **LOC:** 278 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.4062%), State Flux (98.8654%), Safety Score (86.5822%)
- **Heaviest Functions:** `updateComputerList` (Impact: 24.6), `createNewComputerForNode` (Impact: 19.6), `updateComputer` (Impact: 9.7)

### 7. `core/src/main/resources/hudson/PluginManager/_table.js` (JAVASCRIPT) -> Cumulative Risk: **628.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 315.52 | **LOC:** 545 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9988%), Documentation (94.4444%), Safety Score (90.4341%)
- **Heaviest Functions:** `populateEnableDisableInfo` (Impact: 23.1), `initPluginRowHandling` (Impact: 17.5), `applyFilter` (Impact: 15.5)

### 8. `core/src/main/java/hudson/util/io/ReopenableFileOutputStream.java` (JAVA) -> Cumulative Risk: **614.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 55.42 | **LOC:** 105 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9988%), Documentation (86.6667%)
- **Heaviest Functions:** `current` (Impact: 4.5), `close` (Impact: 2.4), `write` (Impact: 2.2)

### 9. `websocket/jetty12-ee9/src/main/java/jenkins/websocket/Jetty12EE9Provider.java` (JAVA) -> Cumulative Risk: **610.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 95.6 | **LOC:** 181 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9988%)
- **Heaviest Functions:** `handle` (Impact: 10.8), `createWebSocket` (Impact: 5.1), `init` (Impact: 3.1)

### 10. `src/main/js/components/dialogs/index.js` (JAVASCRIPT) -> Cumulative Risk: **609.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 187.62 | **LOC:** 360 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (99.5989%)
- **Heaviest Functions:** `init` (Impact: 27.2), `appendButtons` (Impact: 11.9), `show` (Impact: 9.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `core/src/main/java/jenkins/model/Jenkins.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2597.64 | **LOC:** 5991 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (28.5838%), Tech Debt (12.5879%)
**Top Internal Functions/Classes:**
  * `Jenkins` (Impact: 50.0)
    * *Intent:* /** * @param pluginManager * If non-null, use existing plugin manager. create a new one. */
  * `loadTasks` (Impact: 29.6)
  * `_cleanUpAwaitDisconnects` (Impact: 24.1)
  * `refreshExtensions` (Impact: 22.9)
    * *Intent:* /** * Refresh {@link ExtensionList}s by adding all the newly discovered extensions. * * Exposed only...
  * `getItem` (Impact: 22.9)
    * *Intent:* * Gets the item by its path name from the given context * * <p><strong>Path Names:</strong> * If the...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 142 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 140
* *State Mutation (weighted view):* 533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 524`, `structural_boundaries: 1279`, `args: 441`, `func_start: 409`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 280`, `high_risk_execution: 3`, `state_mutation: 249`, `dead_code: 22`, `planned_debt: 17`, `fragile_debt: 8`
* *Architecture:* `io: 37`, `api: 404`, `concurrency: 65`, `import: 317`
* *Defense:* `safety: 208`, `doc: 286`, `sync_locks: 28`, `immutability_locks: 106`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.763
  * `Choke Point (Betweenness):` 0.00242 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 187):` com.google.common.annotations.VisibleForTesting, com.google.inject.Inject, com.google.inject.Injector, com.thoughtworks.xstream.XStream, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings...
  * `Imported By (In-Degree: 511):` (Excluded from Brief to save tokens)

### `war/src/main/webapp/scripts/hudson-behavior.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1838.36 | **LOC:** 2761 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (68.857%), Tech Debt (44.74%)
**Top Internal Functions/Classes:**
  * `buildFormTree` (Impact: 62.2)
    * *Intent:* // // structured form submission handling // see https://www.jenkins.io/redirect/developer/structure...
  * `registerMinMaxValidator` (Impact: 50.2)
    * *Intent:* /** * Add a validator for number fields which contains 'min', 'max' attribute * @param e Input eleme...
  * `encode` (Impact: 33.7)
    * *Intent:* */ // eslint-disable-next-line no-unused-vars
  * `onchange` (Impact: 32.8)
  * `registerValidator` (Impact: 32.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 219 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 70
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 733
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 361`, `args: 200`, `func_start: 122`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 17`, `state_mutation: 295`, `dead_code: 10`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 25`
* *Architecture:* `io: 9`, `concurrency: 15`
* *Defense:* `safety: 89`, `doc: 39`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/FilePath.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1696.7 | **LOC:** 3937 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (18.8455%), Tech Debt (9.9059%)
**Top Internal Functions/Classes:**
  * `installIfNecessaryFrom` (Impact: 67.8)
  * `invoke` (Impact: 48.5)
  * `readFromTar` (Impact: 47.8)
    * *Intent:* /** * Reads from a tar stream and stores obtained files to the base dir. * Supports large files &gt;...
  * `normalize` (Impact: 39.6)
    * *Intent:* /** * {@link File#getParent()} etc cannot handle ".." and "." in the path component very well, * so ...
  * `validateRelativePath` (Impact: 31.9)
    * *Intent:* * or {@link Jenkins#MANAGE} permission if no such ancestor is found. * * <p>Note that this permissio...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 69 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 987`, `args: 304`, `func_start: 295`, `class_start: 70`
* *Risk/State:* `safety_bypasses: 119`, `state_mutation: 160`, `dead_code: 3`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 271`, `api: 222`, `concurrency: 13`, `import: 118`
* *Defense:* `safety: 148`, `doc: 136`, `sync_locks: 1`, `immutability_locks: 219`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.501
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` com.google.common.annotations.VisibleForTesting, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.Launcher.LocalLauncher, hudson.Launcher.RemoteLauncher, hudson.Util.fileToPath, hudson.Util.fixEmpty...
  * `Imported By (In-Degree: 101):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/Functions.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1479.08 | **LOC:** 2743 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (32.5608%), Tech Debt (8.8994%)
**Top Internal Functions/Classes:**
  * `dumpThreadInfo` (Impact: 46.4)
    * *Intent:* // ThreadInfo.toString() truncates the stack trace by first 8, so needed my own version
  * `getPasswordValue` (Impact: 43.4)
    * *Intent:* /** * Used by {@code <f:password/>} so that we send an encrypted value to the client. */
  * `doPrintStackTrace` (Impact: 41.5)
  * `getRelativeNameFrom` (Impact: 38.0)
    * *Intent:* /** * Gets the relative name or display name to the given item from the specified group. * * @since ...
  * `guessIcon` (Impact: 18.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 79 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 595`, `args: 219`, `func_start: 199`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 184`, `state_mutation: 104`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 194`, `concurrency: 18`, `import: 167`
* *Defense:* `safety: 52`, `doc: 114`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.219
  * `Choke Point (Betweenness):` 0.000451 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 83):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.cli.CLICommand, hudson.console.ConsoleAnnotationDescriptor, hudson.console.ConsoleAnnotatorFactory, hudson.init.InitMilestone...
  * `Imported By (In-Degree: 136):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/UpdateCenter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1458.1 | **LOC:** 2956 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.3134%), Tech Debt (90.7332%)
**Top Internal Functions/Classes:**
  * `verifyChecksums` (Impact: 78.7)
    * *Intent:* /** * Implements the checksum verification logic with fallback to weaker algorithm for {@link Downlo...
  * `download` (Impact: 40.9)
    * *Intent:* /** * Download a plugin or core upgrade in preparation for installing it * into its final location. ...
  * `doConnectionStatusImpl` (Impact: 27.9)
  * `createUpdateCenter` (Impact: 27.1)
    * *Intent:* /** * Creates an update center. * @param config Requested configuration. May be {@code null} if defa...
  * `getBadge` (Impact: 21.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 75 instances
* *Concurrency (weighted view):* 80
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 635`, `args: 201`, `func_start: 201`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 147`, `state_mutation: 155`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 24`
* *Architecture:* `io: 79`, `api: 221`, `concurrency: 40`, `import: 111`
* *Defense:* `safety: 117`, `doc: 127`, `sync_locks: 22`, `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` com.google.common.annotations.VisibleForTesting, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.BulkChange, hudson.Extension, hudson.ExtensionPoint, hudson.Functions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/PluginManager.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1448.06 | **LOC:** 2698 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (42.6926%), Tech Debt (11.8983%)
**Top Internal Functions/Classes:**
  * `install` (Impact: 50.3)
  * `doPluginsSearch` (Impact: 41.8)
  * `initTasks` (Impact: 40.8)
    * *Intent:* /** * Called immediately after the construction. * This is a separate method so that code executed f...
  * `dynamicLoad` (Impact: 35.5)
    * *Intent:* /** * Try the dynamicLoad, removeExisting to attempt to dynamic load disabled plugins */
  * `addDependencies` (Impact: 26.4)
    * *Intent:* //TODO: Consider refactoring in order to avoid DMI_COLLECTION_OF_URLS
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 102 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 398
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 654`, `args: 161`, `func_start: 132`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 144`, `state_mutation: 194`, `planned_debt: 10`, `fragile_debt: 3`
* *Architecture:* `io: 57`, `api: 129`, `concurrency: 12`, `import: 154`
* *Defense:* `safety: 136`, `doc: 75`, `sync_locks: 2`, `immutability_locks: 52`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.PluginWrapper.Dependency, hudson.init.InitMilestone, hudson.init.InitMilestone.COMPLETED, hudson.init.InitMilestone.PLUGINS_LISTED...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Queue.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1442.96 | **LOC:** 3253 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (30.7081%), Tech Debt (11.8983%)
**Top Internal Functions/Classes:**
  * `maintain` (Impact: 78.8)
    * *Intent:* /** * Queue maintenance. * * <p> * Move projects between {@link #waitingList}, {@link #blockedProjec...
  * `scheduleInternal` (Impact: 39.3)
    * *Intent:* /** * Schedules an execution of a task. * * @since 1.311 * @return * {@link hudson.model.queue.Sched...
  * `makeFlyWeightTaskBuildable` (Impact: 20.9)
    * *Intent:* /** * This method checks if the flyweight task can be run on any of the available executors * @param...
  * `getItems` (Impact: 19.6)
    * *Intent:* /** * Gets the information about the queue item for the given project. * * @return empty if the proj...
  * `getItem` (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 611`, `args: 231`, `func_start: 215`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 162`, `state_mutation: 113`, `dead_code: 8`, `planned_debt: 16`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 186`, `concurrency: 29`, `import: 115`
* *Defense:* `safety: 101`, `doc: 145`, `sync_locks: 67`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.881
  * `Choke Point (Betweenness):` 0.000232 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 51):` com.google.common.annotations.VisibleForTesting, com.google.common.cache.Cache, com.google.common.cache.CacheBuilder, com.infradna.tool.bridge_method_injector.WithBridgeMethods, com.thoughtworks.xstream.XStream, com.thoughtworks.xstream.converters.basic.AbstractSingleValueConverter, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Run.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1225.76 | **LOC:** 2700 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (35.2737%), Tech Debt (9.0161%)
**Top Internal Functions/Classes:**
  * `addArtifacts` (Impact: 52.2)
  * `getBuildStatusSummary` (Impact: 29.2)
    * *Intent:* /** * Gets an object which represents the single line summary of the status of this build * (especia...
  * `execute` (Impact: 21.2)
  * `waitForCheckpoint` (Impact: 17.0)
    * *Intent:* /** * @see CheckPoint#block() */
  * `getLog` (Impact: 14.9)
    * *Intent:* /** * Gets the log of the build as a list of strings (one per log line). * The number of lines retur...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 88 instances
* *Amplified Sql Injection:* 2 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 320
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 569`, `args: 177`, `func_start: 179`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 144`, `dead_code: 3`, `planned_debt: 6`
* *Architecture:* `io: 34`, `api: 191`, `concurrency: 14`, `import: 125`
* *Defense:* `safety: 138`, `doc: 153`, `sync_locks: 10`, `immutability_locks: 65`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 0.000432 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 58):` com.thoughtworks.xstream.XStream, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.AbortException, hudson.BulkChange, hudson.EnvVars, hudson.Extension...
  * `Imported By (In-Degree: 108):` (Excluded from Brief to save tokens)

### `src/main/js/pluginSetupWizardGui.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1100.04 | **LOC:** 1455 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4889%), Tech Debt (8.3445%)
**Top Internal Functions/Classes:**
  * `createPluginSetupWizard` (Impact: 348.1)
    * *Intent:* // Setup the dialog, exported
  * `setPanel` (Impact: 48.0)
    * *Intent:* // call this to set the panel in the app, this performs some additional things & adds common transit...
  * `showInstallProgress` (Impact: 46.8)
    * *Intent:* // Define actions
  * `updateStatus` (Impact: 36.5)
    * *Intent:* // call to the installStatus, update progress bar & plugin details; transition on complete
  * `showInitialSetupWizard` (Impact: 23.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 284`, `args: 134`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 108`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 9`, `concurrency: 7`, `import: 21`
* *Defense:* `safety: 32`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` pluginManager, securityConfig, id, bootstrap-detached, configureInstance.hbs, errorPanel.hbs, firstUserPanel.hbs, incompleteInstallationPanel.hbs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/AbstractProject.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 985.2 | **LOC:** 2164 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.9608%), Tech Debt (11.3046%)
**Top Internal Functions/Classes:**
  * `submitImpl` (Impact: 36.1)
  * `_poll` (Impact: 31.4)
    * *Intent:* /** * {@link #poll(TaskListener)} method without the try/catch block that does listener notification...
  * `poll` (Impact: 18.6)
    * *Intent:* /** * Checks if there's any update in SCM, and returns true if any is found. * * <p> * The implement...
  * `onLoad` (Impact: 15.0)
  * `workspaceOffline` (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 433`, `args: 146`, `func_start: 150`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 141`, `state_mutation: 79`, `dead_code: 7`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 158`, `concurrency: 15`, `import: 98`
* *Defense:* `safety: 49`, `doc: 99`, `sync_locks: 4`, `immutability_locks: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.324
  * `Choke Point (Betweenness):` 0.000322 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` com.infradna.tool.bridge_method_injector.WithBridgeMethods, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, hudson.AbortException, hudson.CopyOnWrite, hudson.EnvVars, hudson.ExtensionList, hudson.ExtensionPoint...
  * `Imported By (In-Degree: 74):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/util/ProcessTree.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 935.4 | **LOC:** 2141 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.0615%), Tech Debt (86.2158%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 20.5)
  * `get` (Impact: 20.3)
    * *Intent:* /* package */ static volatile Boolean vetoersExist; /** * Gets the {@link ProcessTree} of the curren...
  * `FreeBSD` (Impact: 17.6)
  * `AIXProcess` (Impact: 16.7)
  * `Darwin` (Impact: 16.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 83 instances
* *Concurrency (weighted view):* 60
* *State Mutation (weighted view):* 275
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 434`, `args: 131`, `func_start: 124`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 109`, `dead_code: 4`, `planned_debt: 3`, `duplicate_logic: 15`
* *Architecture:* `io: 13`, `api: 80`, `concurrency: 15`, `import: 51`
* *Defense:* `safety: 98`, `doc: 45`, `sync_locks: 12`, `immutability_locks: 81`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.258
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.sun.jna.LastErrorException, com.sun.jna.Memory, com.sun.jna.Native, com.sun.jna.NativeLong, com.sun.jna.Pointer.NULL, com.sun.jna.ptr.IntByReference, com.sun.jna.ptr.NativeLongByReference, edu.umd.cs.findbugs.annotations.CheckForNull...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Job.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 906.24 | **LOC:** 1732 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (38.1824%), Tech Debt (9.303%)
**Top Internal Functions/Classes:**
  * `doRssChangelog` (Impact: 33.1)
    * *Intent:* /** * RSS feed for changes in this project. * * @since 2.60 */
  * `onLoad` (Impact: 26.2)
  * `getBuildStabilityHealthReport` (Impact: 26.1)
  * `onLocationChanged` (Impact: 15.4)
  * `getBuildHealthReports` (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 63 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 417`, `args: 122`, `func_start: 128`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 96`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 19`, `api: 124`, `concurrency: 13`, `import: 114`
* *Defense:* `safety: 34`, `doc: 74`, `sync_locks: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.979
  * `Choke Point (Betweenness):` 0.000414 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 55):` com.infradna.tool.bridge_method_injector.WithBridgeMethods, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.BulkChange, hudson.EnvVars, hudson.Extension, hudson.ExtensionList...
  * `Imported By (In-Degree: 61):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/Util.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 867.64 | **LOC:** 1998 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.1007%), Tech Debt (9.3115%)
**Top Internal Functions/Classes:**
  * `getMethod` (Impact: 38.0)
  * `escape` (Impact: 31.5)
    * *Intent:* /** * Escapes HTML unsafe characters like &lt;, &amp; to the respective character entities. */
  * `encode` (Impact: 30.6)
  * `createDirectories` (Impact: 26.5)
    * *Intent:* * * <p>If this method fails, * then it may do so after creating some, but not all, of the parent dir...
  * `getTimeSpanString` (Impact: 25.9)
    * *Intent:* /** * Returns a human readable text of the time duration, for example "3 minutes 40 seconds". * This...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 395`, `args: 102`, `func_start: 105`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 73`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 96`, `api: 97`, `concurrency: 3`, `import: 102`
* *Defense:* `safety: 205`, `doc: 87`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.756
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.CheckReturnValue, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.model.TaskListener, hudson.util.QuotedStringTokenizer, hudson.util.VariableResolver...
  * `Imported By (In-Degree: 217):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/UpdateSite.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 777.16 | **LOC:** 1768 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (34.9411%), Tech Debt (18.7161%)
**Top Internal Functions/Classes:**
  * `Plugin` (Impact: 35.8)
  * `deploy` (Impact: 33.0)
    * *Intent:* * <p> * This is mainly intended to be called from the UI. The actual installation work happens * asy...
  * `Data` (Impact: 31.8)
  * `getNeededDependencies` (Impact: 21.4)
    * *Intent:* /** * Returns a list of dependent plugins which need to be installed or upgraded for this plugin to ...
  * `isRelevant` (Impact: 13.2)
    * *Intent:* /** * Returns true if this warning is relevant to the current configuration * @return true if this w...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 58 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 309`, `args: 103`, `func_start: 93`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 96`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 132`, `concurrency: 9`, `import: 66`
* *Defense:* `safety: 44`, `doc: 106`, `sync_locks: 1`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.245
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.ExtensionList, hudson.PluginManager, hudson.PluginWrapper, hudson.ProxyConfiguration...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Fingerprint.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 731.12 | **LOC:** 1503 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.2644%), Tech Debt (8.8023%)
**Top Internal Functions/Classes:**
  * `fromString` (Impact: 40.7)
    * *Intent:* /** * Parses a {@link RangeSet} from a string like "1-3,5,7-9" */
  * `locationChanged` (Impact: 18.9)
  * `canDiscoverItem` (Impact: 16.2)
    * *Intent:* /** * Checks if the current user can Discover the item. * If yes, it may be displayed as a text in F...
  * `removeAll` (Impact: 15.9)
    * *Intent:* /** * Updates this range set by removing all the values in the given range set. * * @return true if ...
  * `trim` (Impact: 13.8)
    * *Intent:* /** * Trim off references to non-existent builds and jobs, thereby making the fingerprint smaller. *...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 283`, `args: 109`, `func_start: 106`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 79`, `dead_code: 4`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 101`, `concurrency: 19`, `import: 46`
* *Defense:* `safety: 47`, `doc: 63`, `sync_locks: 19`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.274
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` com.infradna.tool.bridge_method_injector.WithBridgeMethods, com.thoughtworks.xstream.converters.Converter, com.thoughtworks.xstream.converters.MarshallingContext, com.thoughtworks.xstream.converters.UnmarshallingContext, com.thoughtworks.xstream.converters.basic.DateConverter, com.thoughtworks.xstream.converters.collections.CollectionConverter, com.thoughtworks.xstream.io.HierarchicalStreamReader, com.thoughtworks.xstream.io.HierarchicalStreamWriter...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Computer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 708.58 | **LOC:** 1802 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (24.9996%), Tech Debt (12.7581%)
**Top Internal Functions/Classes:**
  * `doRssLatest` (Impact: 19.8)
    * *Intent:* /** * Retrieve the RSS feed for the last build for each project executed in this computer. * Only th...
  * `doConfigSubmit` (Impact: 15.8)
    * *Intent:* /** * Accepts the update to the node configuration. */
  * `doConfigDotXml` (Impact: 12.0)
    * *Intent:* /** * Accepts {@code config.xml} submission, as well as serve it. */
  * `buildEnvironment` (Impact: 11.0)
    * *Intent:* /** * Creates an environment variable override to be used for launching processes on this node. * * ...
  * `relocateOldLogs` (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 404`, `args: 119`, `func_start: 121`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 80`, `state_mutation: 54`, `dead_code: 3`, `planned_debt: 9`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 132`, `concurrency: 17`, `import: 115`
* *Defense:* `safety: 27`, `doc: 90`, `sync_locks: 6`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.224
  * `Choke Point (Betweenness):` 0.000366 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.OverrideMustInvoke, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.EnvVars, hudson.Extension, hudson.Launcher.ProcStarter...
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/AbstractBuild.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 692.48 | **LOC:** 1419 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.196%), Tech Debt (12.4862%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 28.1)
  * `reportError` (Impact: 21.2)
  * `getWhyKeepLog` (Impact: 20.4)
    * *Intent:* // // // fingerprint related stuff // //
  * `createLauncher` (Impact: 20.0)
    * *Intent:* /** * Creates a {@link Launcher} that this build will use. This can be overridden by derived types *...
  * `performAllBuildSteps` (Impact: 16.9)
    * *Intent:* /** * Runs all the given build steps, even if one of them fail. * * @param phase * true for the post...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 52 instances
* *Amplified Sql Injection:* 1 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 263`, `args: 66`, `func_start: 76`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 65`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `api: 85`, `concurrency: 6`, `import: 69`
* *Defense:* `safety: 56`, `doc: 60`, `sync_locks: 2`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.911
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, hudson.AbortException, hudson.EnvVars, hudson.FilePath, hudson.Functions, hudson.Launcher, hudson.Util...
  * `Imported By (In-Degree: 73):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Descriptor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 685.64 | **LOC:** 1335 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.7298%), Tech Debt (15.5595%)
**Top Internal Functions/Classes:**
  * `newInstancesFromHeteroList` (Impact: 26.2)
    * *Intent:* /** * @since 2.475 */
  * `getHelpFile` (Impact: 18.6)
  * `getStaticHelpUrl` (Impact: 17.2)
    * *Intent:* /** * @since 2.475 */
  * `doHelpImpl` (Impact: 15.6)
  * `buildFillDependencies` (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 308`, `args: 84`, `func_start: 88`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 61`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `api: 81`, `concurrency: 2`, `import: 74`
* *Defense:* `safety: 43`, `doc: 63`, `sync_locks: 2`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.669
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.Nullable, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.BulkChange, hudson.DescriptorExtensionList, hudson.ExtensionList, hudson.PluginWrapper...
  * `Imported By (In-Degree: 130):` (Excluded from Brief to save tokens)

### `core/report-l10n.rb` (RUBY | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 678.7 | **LOC:** 552 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.6261%), Tech Debt (10.7259%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 496.2)
  * `Anonymous_Block_[Truncated]` (Impact: 138.7)
  * `Anonymous_Block` (Impact: 7.7)
  * `Anonymous_Block` (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 477`, `structural_boundaries: 2`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` set
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/test/java/hudson/model/QueueTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 622.78 | **LOC:** 1562 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (52.0469%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `foldableCauseAction` (Impact: 16.6)
  * `pendingsConsistenceAfterErrorDuringMaintain` (Impact: 15.9)
  * `queueApiOutputShouldBeFilteredByUserPermission` (Impact: 12.2)
  * `waitUntilWaitingListIsEmpty` (Impact: 7.7)
  * `flyweightTasks` (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 22 instances
* *Amplified Sql Injection:* 1 instances
* *Concurrency (weighted view):* 94
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 444`, `args: 118`, `func_start: 98`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 99`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 11`, `api: 92`, `concurrency: 44`, `import: 114`
* *Defense:* `safety: 22`, `doc: 9`, `test: 181`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, hudson.ExtensionList, hudson.Functions, hudson.Launcher, hudson.XmlFile, hudson.matrix.AxisList, hudson.matrix.MatrixBuild...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/Launcher.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 590.7 | **LOC:** 1500 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.557%), Tech Debt (40.8584%)
**Top Internal Functions/Classes:**
  * `printCommandLine` (Impact: 18.5)
    * *Intent:* /** * Prints out the command line to the listener so that users know what we are doing. */
  * `launch` (Impact: 15.4)
  * `launch` (Impact: 14.3)
  * `call` (Impact: 12.9)
  * `maskedPrintCommandLine` (Impact: 10.8)
    * *Intent:* /** * Prints out the command line to the listener with some portions masked to prevent sensitive inf...
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 9
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 296`, `args: 128`, `func_start: 127`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 1`, `state_mutation: 59`, `planned_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `io: 67`, `api: 136`, `concurrency: 4`, `import: 41`
* *Defense:* `safety: 68`, `doc: 64`, `sync_locks: 2`, `immutability_locks: 57`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.276
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.Proc.LocalProc, hudson.Proc.ProcWithJenkins23271Patch, hudson.model.Computer, hudson.model.Node, hudson.model.Run...
  * `Imported By (In-Degree: 87):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/View.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 576.52 | **LOC:** 1286 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.6461%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doItemCategories` (Impact: 26.9)
    * *Intent:* /** * An API REST method to get the allowed {$link TopLevelItem}s and its categories. * * @return A ...
  * `filterQueueItemTest` (Impact: 20.6)
  * `create` (Impact: 20.6)
    * *Intent:* /** * @since 2.475 */
  * `getComputers` (Impact: 13.1)
  * `isRelevant` (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 335`, `args: 93`, `func_start: 96`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 49`, `dead_code: 3`
* *Architecture:* `io: 6`, `api: 102`, `concurrency: 7`, `import: 97`
* *Defense:* `safety: 29`, `doc: 65`, `sync_locks: 7`, `immutability_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` com.thoughtworks.xstream.converters.ConversionException, com.thoughtworks.xstream.io.StreamException, edu.umd.cs.findbugs.annotations.NonNull, edu.umd.cs.findbugs.annotations.SuppressFBWarnings, hudson.DescriptorExtensionList, hudson.Extension, hudson.ExtensionPoint, hudson.Functions...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `test/src/test/java/hudson/cli/RunRangeCommandTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 571.98 | **LOC:** 1040 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.0789%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dummyRangeRangeSingleShouldSuccess` (Impact: 19.1)
  * `dummyRangeRangeSingleShouldFailIfBuildRangeContainsZeroAndNegative` (Impact: 17.3)
  * `act` (Impact: 14.9)
  * `dummyRangeRangeSingleShouldFailIfBuildRangeContainsANegativeNumber` (Impact: 14.6)
  * `dummyRangeNumberSingleShouldSuccess` (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 103 instances
* *State Mutation (weighted view):* 322
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 63`, `args: 39`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 116`, `unreferenced_by_name: 39`
* *Architecture:* `api: 3`, `import: 16`
* *Defense:* `doc: 1`, `test: 362`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` hudson.Extension, hudson.cli.CLICommandInvoker.Matcher.failedWith, hudson.cli.CLICommandInvoker.Matcher.hasNoStandardOutput, hudson.cli.CLICommandInvoker.Matcher.succeeded, hudson.model.FreeStyleProject, hudson.model.Item, hudson.model.Run, java.util.List...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/PluginWrapper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 567.36 | **LOC:** 1441 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (20.0117%), Tech Debt (8.9312%)
**Top Internal Functions/Classes:**
  * `resolvePluginDependencies` (Impact: 27.1)
    * *Intent:* /** * Makes sure that all the dependencies exist, and then accept optional dependencies * as real de...
  * `disable` (Impact: 23.5)
    * *Intent:* /** * Disable this plugin using a strategy. * @param strategy strategy to use * @return an object re...
  * `PluginWrapper` (Impact: 12.8)
    * *Intent:* /** * @param archive * A .jpi archive file jar file, or a .jpl linked plugin. * @param manifest * Th...
  * `Dependency` (Impact: 12.5)
  * `getVersionOf` (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 267`, `args: 126`, `func_start: 111`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 52`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `io: 15`, `api: 115`, `import: 59`
* *Defense:* `safety: 34`, `doc: 75`, `immutability_locks: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` com.google.common.collect.Sets, edu.umd.cs.findbugs.annotations.CheckForNull, edu.umd.cs.findbugs.annotations.NonNull, hudson.PluginManager.PluginInstanceStore, hudson.PluginWrapper.PluginDisableStatus.ALREADY_DISABLED, hudson.PluginWrapper.PluginDisableStatus.DISABLED, hudson.PluginWrapper.PluginDisableStatus.ERROR_DISABLING, hudson.PluginWrapper.PluginDisableStatus.NOT_DISABLED_DEPENDANTS...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `core/src/test/java/jenkins/org/apache/commons/validator/routines/UrlValidatorTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 566.16 | **LOC:** 724 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.9861%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testValidator276` (Impact: 58.6)
  * `testValidator290` (Impact: 35.9)
  * `main` (Impact: 28.3)
    * *Intent:* /** * Validator for checking URL parsing * @param args - URLs to validate */
  * `testIsValid` (Impact: 26.3)
    * *Intent:* /** * Create set of tests by taking the testUrlXXX arrays and * running through all possible permuta...
  * `testValidator353` (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 178`, `args: 43`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 60`, `planned_debt: 1`, `unreferenced_by_name: 33`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 2`, `doc: 4`, `test: 185`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.net.URI, java.net.URISyntaxException, java.util.ArrayList, java.util.List, jenkins.org.apache.commons.validator.ResultPair, org.junit.jupiter.api.Assertions.assertEquals, org.junit.jupiter.api.Assertions.assertFalse, org.junit.jupiter.api.Assertions.assertThrows...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/src/main/java/hudson/model/UpdateCenter.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 1458.1
- `core/src/main/java/hudson/PluginManager.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 1448.06
- `core/src/main/java/hudson/util/ProcessTree.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 935.4
- `core/src/main/java/hudson/model/Fingerprint.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 731.12
- `core/src/main/java/hudson/model/AbstractBuild.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 692.48

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/src/main/java/jenkins/model/Jenkins.java` -> **Severity: 0.229** (Bridge: 0.0024 * Flux: 94.6069%)
- `core/src/main/java/hudson/Functions.java` -> **Severity: 0.044** (Bridge: 0.0005 * Flux: 97.1796%)
- `core/src/main/java/hudson/model/Run.java` -> **Severity: 0.043** (Bridge: 0.0004 * Flux: 99.199%)
- `core/src/main/java/hudson/model/Job.java` -> **Severity: 0.041** (Bridge: 0.0004 * Flux: 99.4279%)
- `core/src/main/java/hudson/model/AbstractProject.java` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 97.8627%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/src/main/java/jenkins/YesNoMaybe.java` -> **Severity: 966.2** (Blast Radius: 9.662 * Doc Risk: 100.0%)
- `core/src/main/java/jenkins/model/Jenkins.java` -> **Severity: 684.661** (Blast Radius: 14.763 * Doc Risk: 46.3768%)
- `core/src/main/java/org/acegisecurity/Authentication.java` -> **Severity: 301.213** (Blast Radius: 3.116 * Doc Risk: 96.6667%)
- `core/src/main/java/org/acegisecurity/GrantedAuthority.java` -> **Severity: 245.0** (Blast Radius: 2.695 * Doc Risk: 90.9091%)
- `core/src/main/java/hudson/Functions.java` -> **Severity: 207.955** (Blast Radius: 5.219 * Doc Risk: 39.8458%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
