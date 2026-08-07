# ARCHITECTURAL_BRIEF: jenkins
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/jenkins` |
| **Timestamp** | `2026-08-07T05:02:52.947020+00:00` |
| **Scan Duration** | `16.41s` |
| **Git Branch** | `master` |
| **Git Commit** | `bc6a2222ce5a9e104a4f5a96653f0e879461936b` |
| **Git Remote** | `https://github.com/jenkinsci/jenkins` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2103 malicious artifacts.

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
| Total Artifacts | 12361 |
| Analyzed Artifacts (Scanned) | 11977 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 384 |
| Total LOC | 216117 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.9% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1544 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 144 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 7512 | 0 | 62.7% |
| JAVA | 1906 | 171877 | 15.9% |
| XML | 1222 | 22 | 10.2% |
| HTML | 1019 | 21493 | 8.5% |
| JAVASCRIPT | 123 | 8476 | 1.0% |
| CSS | 88 | 10851 | 0.7% |
| GROOVY | 64 | 1155 | 0.5% |
| JSON | 28 | 1461 | 0.2% |
| MARKDOWN | 5 | 0 | 0.0% |
| SHELL | 4 | 102 | 0.0% |
| BATCH | 3 | 31 | 0.0% |
| RUBY | 1 | 525 | 0.0% |
| C | 1 | 15 | 0.0% |
| PYTHON | 1 | 109 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.548`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2763 | 23.1% |
| file_cluster_13 | 1464 | 12.2% |
| file_cluster_0 | 130 | 1.1% |
| file_cluster_4 | 41 | 0.3% |
| file_cluster_16 | 24 | 0.2% |
| file_cluster_2 | 15 | 0.1% |
| file_cluster_17 | 7 | 0.1% |
| file_cluster_9 | 2 | 0.0% |
| file_cluster_12 | 1 | 0.0% |
| file_cluster_6 | 1 | 0.0% |
| file_cluster_15 | 1 | 0.0% |
| file_cluster_7 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7517 | 62.8% |
| Static: Minified & Vendor Opaque Mass | 10 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 384*

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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 9.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 21.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.0 | 0.2 | 0.0 |
| API Exposure | 0.0 | 17.3 | 2.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 62.3 | 86.7 | 100.0 |
| Instability Exposure | 0.0 | 4.7 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 21.9 | 6.2 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 44.5 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/src/test/resources/hudson/model/hudson.tools.JDKInstaller.json.html` (Hits: 1074)
- `core/src/test/java/jenkins/util/io/PathRemoverTest.java` (Hits: 150)
- `core/src/main/java/hudson/FilePath.java` (Hits: 147)

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

- `testIPv6` (@ `core/src/test/java/jenkins/org/apache/commons/validator/routines/InetAddressValidatorTest.java`) -> Impact: **2289.8** | LOC: 155
- `__global_context__` (@ `core/report-l10n.rb`) -> Impact: **837.1** | LOC: 495
- `onInitMilestoneAttained` (@ `core/src/main/java/jenkins/model/Jenkins.java`) -> Impact: **717.3** | LOC: 1511
- `executeReactor` (@ `core/src/main/java/jenkins/model/Jenkins.java`) -> Impact: **536.2** | LOC: 1510
- `printThrowable` (@ `core/src/test/java/hudson/FunctionsTest.java`) -> Impact: **456.3** | LOC: 226
- `resetFilter` (@ `core/src/main/java/jenkins/model/Jenkins.java`) -> Impact: **449.9** | LOC: 1134
- `unzip` (@ `core/src/main/java/hudson/FilePath.java`) -> Impact: **429.0** | LOC: 1374
- `isUnix` (@ `core/src/main/java/hudson/FilePath.java`) -> Impact: **428.1** | LOC: 1391
  * *Intent:* /** * When this {@link FilePath} represents the remote path, * this field is always non-null on the controller (the field represents * the channel to ...
- `mkdirs` (@ `core/src/main/java/hudson/FilePath.java`) -> Impact: **424.1** | LOC: 1381
  * *Intent:* // shouldn't need this replace, but better safe than sorry
- `loadTasks` (@ `core/src/main/java/jenkins/model/Jenkins.java`) -> Impact: **365.2** | LOC: 729
  * *Intent:* /** * If usage statistics are being collected * * @return {@code true} if usage statistics should be collected. * Defaults to {@code true} when {@link...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `core/src/main/java/hudson/model` | 170 | 20773.98 | 10.26% | 65.98% |
| `core/src/main/java/hudson` | 50 | 10099.38 | 10.95% | 53.15% |
| `core/src/main/java/hudson/util` | 122 | 8699.0 | 12.91% | 64.74% |
| `core/src/main/java/jenkins/model` | 69 | 7935.72 | 9.0% | 51.83% |
| `test/src/test/java/hudson/model` | 84 | 7882.8 | 14.16% | 0.0% |
| `test/src/test/java/hudson/cli` | 48 | 3500.24 | 16.06% | 0.0% |
| `core/src/main/java/hudson/slaves` | 33 | 2932.64 | 10.17% | 72.4% |
| `core/src/main/java/hudson/security` | 45 | 2829.64 | 9.08% | 55.55% |
| `test/src/test/java/jenkins/security` | 45 | 2784.78 | 25.49% | 0.0% |
| `core/src/test/java/jenkins/org/apache/commons/validator/routines` | 4 | 2772.12 | 15.8% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Jenkinsfile` -> **100.0%** Exposure
- `core/move-l10n.groovy` -> **100.0%** Exposure
- `core/src/main/resources/hudson/model/AllView/noJob.groovy` -> **100.0%** Exposure
- `core/src/main/resources/hudson/security/GlobalSecurityConfiguration/index.groovy` -> **100.0%** Exposure
- `core/src/main/resources/hudson/tasks/ArtifactArchiver/help-defaultExcludes.groovy` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `war/src/main/webapp/WEB-INF/hudson` -> **100.0%** Exposure
- `core/src/main/java/hudson/logging/WeakLogHandler.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/search/SearchIndexBuilder.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/ArgumentListBuilder.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/ClasspathBuilder.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/src/test/java/hudson/model/DirectoryBrowserSupportTest.java` -> **24** Orphaned Functions | **71** Duplicates
- `test/src/test/java/jenkins/security/stapler/GetterMethodFilterTest.java` -> **81** Orphaned Functions | **5** Duplicates
- `core/src/main/java/hudson/util/TimeUnit2.java` -> **2** Orphaned Functions | **79** Duplicates
- `core/src/main/java/hudson/FilePath.java` -> **0** Orphaned Functions | **79** Duplicates
- `core/src/main/java/jenkins/model/Jenkins.java` -> **0** Orphaned Functions | **64** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`core/src/test/java/jenkins/model/JenkinsGetRootUrlTest.java`** -> AI Confidence: **99.39%**
2. **`core/src/test/java/jenkins/security/RedactSecretJsonInErrorMessageSanitizerTest.java`** -> AI Confidence: **99.34%**
3. **`core/src/main/java/hudson/cli/DisablePluginCommand.java`** -> AI Confidence: **99.31%**
4. **`core/src/main/java/hudson/cli/ListChangesCommand.java`** -> AI Confidence: **99.31%**
5. **`core/src/main/java/hudson/model/Executor.java`** -> AI Confidence: **99.31%**
6. **`core/src/main/java/hudson/model/ParametersAction.java`** -> AI Confidence: **99.31%**
7. **`core/src/main/java/hudson/scheduler/CronTabList.java`** -> AI Confidence: **99.31%**
8. **`core/src/main/java/hudson/util/NoOverlapCategoryAxis.java`** -> AI Confidence: **99.31%**
9. **`core/src/main/java/hudson/util/PrettyPrintWriter.java`** -> AI Confidence: **99.31%**
10. **`core/src/main/java/hudson/util/Service.java`** -> AI Confidence: **99.31%**
11. **`core/src/main/java/hudson/util/jelly/MorphTagLibrary.java`** -> AI Confidence: **99.31%**
12. **`core/src/main/java/jenkins/console/ConsoleUrlProvider.java`** -> AI Confidence: **99.31%**
13. **`core/src/main/java/jenkins/model/PeepholePermalink.java`** -> AI Confidence: **99.31%**
14. **`core/src/main/java/jenkins/model/queue/ItemDeletion.java`** -> AI Confidence: **99.31%**
15. **`core/src/main/java/jenkins/org/apache/commons/validator/routines/DomainValidator.java`** -> AI Confidence: **99.31%**
16. **`core/src/main/java/jenkins/util/DefaultScriptListener.java`** -> AI Confidence: **99.31%**
17. **`core/src/main/java/jenkins/widgets/HistoryPageFilter.java`** -> AI Confidence: **99.31%**
18. **`core/src/main/java/org/jenkins/ui/icon/Icon.java`** -> AI Confidence: **99.31%**
19. **`core/src/test/java/hudson/FunctionsTest.java`** -> AI Confidence: **99.31%**
20. **`core/src/test/java/hudson/model/BuildStatusSummaryTest.java`** -> AI Confidence: **99.31%**
21. **`core/src/test/java/jenkins/org/apache/commons/validator/routines/UrlValidatorTest.java`** -> AI Confidence: **99.31%**
22. **`test/src/test/java/hudson/cli/RunRangeCommandTest.java`** -> AI Confidence: **99.31%**
23. **`test/src/test/java/jenkins/security/csp/AvatarContributorTest.java`** -> AI Confidence: **99.31%**
24. **`test/src/test/java/lib/form/RepeatableTest.java`** -> AI Confidence: **99.31%**
25. **`test/src/test/resources/lib/form/OptionTest/UsingGroovyView/index.groovy`** -> AI Confidence: **99.29%**
26. **`core/src/test/java/hudson/console/UrlAnnotatorTest.java`** -> AI Confidence: **99.29%**
27. **`core/src/test/java/jenkins/org/apache/commons/validator/routines/InetAddressValidatorTest.java`** -> AI Confidence: **99.29%**
28. **`core/src/test/java/jenkins/util/UrlHelperTest.java`** -> AI Confidence: **99.29%**
29. **`core/report-l10n.rb`** -> AI Confidence: **99.29%**
30. **`core/src/main/resources/hudson/PluginManager/_updateSite.js`** -> AI Confidence: **99.29%**
31. **`core/src/main/resources/lib/layout/progressiveRendering/progressiveRendering.js`** -> AI Confidence: **99.29%**
32. **`src/main/js/components/header/actions-touch.js`** -> AI Confidence: **99.29%**
33. **`war/src/main/webapp/scripts/loading.js`** -> AI Confidence: **99.29%**
34. **`cli/src/main/java/hudson/cli/CLI.java`** -> AI Confidence: **99.24%**
35. **`core/src/main/java/hudson/ClassicPluginStrategy.java`** -> AI Confidence: **99.24%**
36. **`core/src/main/java/hudson/DependencyRunner.java`** -> AI Confidence: **99.24%**
37. **`core/src/main/java/hudson/ExtensionFinder.java`** -> AI Confidence: **99.24%**
38. **`core/src/main/java/hudson/TcpSlaveAgentListener.java`** -> AI Confidence: **99.24%**
39. **`core/src/main/java/hudson/cli/BuildCommand.java`** -> AI Confidence: **99.24%**
40. **`core/src/main/java/hudson/cli/ConsoleCommand.java`** -> AI Confidence: **99.24%**
41. **`core/src/main/java/hudson/cli/InstallPluginCommand.java`** -> AI Confidence: **99.24%**
42. **`core/src/main/java/hudson/cli/OfflineNodeCommand.java`** -> AI Confidence: **99.24%**
43. **`core/src/main/java/hudson/cli/ReloadJobCommand.java`** -> AI Confidence: **99.24%**
44. **`core/src/main/java/hudson/diagnosis/NullIdDescriptorMonitor.java`** -> AI Confidence: **99.24%**
45. **`core/src/main/java/hudson/model/AbstractBuild.java`** -> AI Confidence: **99.24%**
46. **`core/src/main/java/hudson/model/Actionable.java`** -> AI Confidence: **99.24%**
47. **`core/src/main/java/hudson/model/AsyncAperiodicWork.java`** -> AI Confidence: **99.24%**
48. **`core/src/main/java/hudson/model/AsyncPeriodicWork.java`** -> AI Confidence: **99.24%**
49. **`core/src/main/java/hudson/model/Fingerprint.java`** -> AI Confidence: **99.24%**
50. **`core/src/main/java/hudson/model/HealthReport.java`** -> AI Confidence: **99.24%**
51. **`core/src/main/java/hudson/model/queue/MappingWorksheet.java`** -> AI Confidence: **99.24%**
52. **`core/src/main/java/hudson/model/queue/WorkUnitContext.java`** -> AI Confidence: **99.24%**
53. **`core/src/main/java/hudson/scheduler/CronTab.java`** -> AI Confidence: **99.24%**
54. **`core/src/main/java/hudson/scm/ChangeLogSet.java`** -> AI Confidence: **99.24%**
55. **`core/src/main/java/hudson/security/ChainedServletFilter.java`** -> AI Confidence: **99.24%**
56. **`core/src/main/java/hudson/security/ChainedServletFilter2.java`** -> AI Confidence: **99.24%**
57. **`core/src/main/java/hudson/slaves/NodeProvisioner.java`** -> AI Confidence: **99.24%**
58. **`core/src/main/java/hudson/slaves/RetentionStrategy.java`** -> AI Confidence: **99.24%**
59. **`core/src/main/java/hudson/tasks/BuildStepCompatibilityLayer.java`** -> AI Confidence: **99.24%**
60. **`core/src/main/java/hudson/tasks/BuildStepDescriptor.java`** -> AI Confidence: **99.24%**
61. **`core/src/main/java/hudson/tasks/BuildWrappers.java`** -> AI Confidence: **99.24%**
62. **`core/src/main/java/hudson/tasks/LogRotator.java`** -> AI Confidence: **99.24%**
63. **`core/src/main/java/hudson/util/ProcessTree.java`** -> AI Confidence: **99.24%**
64. **`core/src/main/java/hudson/util/Retrier.java`** -> AI Confidence: **99.24%**
65. **`core/src/main/java/hudson/util/RobustReflectionConverter.java`** -> AI Confidence: **99.24%**
66. **`core/src/main/java/jenkins/ClassLoaderReflectionToolkit.java`** -> AI Confidence: **99.24%**
67. **`core/src/main/java/jenkins/cli/StopBuildsCommand.java`** -> AI Confidence: **99.24%**
68. **`core/src/main/java/jenkins/model/identity/InstanceIdentityProvider.java`** -> AI Confidence: **99.24%**
69. **`core/src/main/java/jenkins/security/ClassFilterImpl.java`** -> AI Confidence: **99.24%**
70. **`core/src/main/java/jenkins/security/RedactSecretJsonInErrorMessageSanitizer.java`** -> AI Confidence: **99.24%**
71. **`core/src/main/java/jenkins/security/SecurityListener.java`** -> AI Confidence: **99.24%**
72. **`core/src/main/java/jenkins/security/csp/AvatarContributor.java`** -> AI Confidence: **99.24%**
73. **`core/src/main/java/jenkins/security/stapler/DoActionFilter.java`** -> AI Confidence: **99.24%**
74. **`core/src/main/java/jenkins/security/stapler/StaplerDispatchValidator.java`** -> AI Confidence: **99.24%**
75. **`core/src/main/java/jenkins/security/stapler/TypedFilter.java`** -> AI Confidence: **99.24%**
76. **`core/src/main/java/jenkins/telemetry/impl/ContentSecurityPolicy.java`** -> AI Confidence: **99.24%**
77. **`core/src/main/java/jenkins/util/FullDuplexHttpService.java`** -> AI Confidence: **99.24%**
78. **`core/src/main/java/jenkins/util/JSONSignatureValidator.java`** -> AI Confidence: **99.24%**
79. **`core/src/main/java/jenkins/util/Listeners.java`** -> AI Confidence: **99.24%**
80. **`core/src/main/java/jenkins/widgets/BuildTimeTrend.java`** -> AI Confidence: **99.24%**
81. **`core/src/main/java/org/acegisecurity/GrantedAuthority.java`** -> AI Confidence: **99.24%**
82. **`core/src/test/java/jenkins/security/apitoken/ApiTokenStatsTest.java`** -> AI Confidence: **99.24%**
83. **`test/src/test/java/hudson/model/queue/BuildKeepsRunningWhenFaultySubTasksTest.java`** -> AI Confidence: **99.24%**
84. **`test/src/test/java/jenkins/security/LastGrantedAuthoritiesPropertyTest.java`** -> AI Confidence: **99.24%**
85. **`war/src/main/java/executable/Main.java`** -> AI Confidence: **99.24%**
86. **`src/main/js/components/command-palette/index.js`** -> AI Confidence: **99.24%**
87. **`src/main/js/pluginSetupWizardGui.js`** -> AI Confidence: **99.24%**
88. **`core/src/main/java/hudson/cli/ListPluginsCommand.java`** -> AI Confidence: **99.23%**
89. **`core/src/main/java/hudson/console/ConsoleAnnotator.java`** -> AI Confidence: **99.23%**
90. **`core/src/main/java/hudson/model/RunParameterValue.java`** -> AI Confidence: **99.23%**
91. **`core/src/main/java/hudson/model/ViewGroupMixIn.java`** -> AI Confidence: **99.23%**
92. **`core/src/main/java/hudson/search/ParsedQuickSilver.java`** -> AI Confidence: **99.23%**
93. **`core/src/main/java/hudson/security/AccessDeniedException3.java`** -> AI Confidence: **99.23%**
94. **`cli/src/main/java/hudson/cli/FullDuplexHttpStream.java`** -> AI Confidence: **99.18%**
95. **`cli/src/main/java/hudson/cli/PlainCLIProtocol.java`** -> AI Confidence: **99.18%**
96. **`cli/src/main/java/hudson/cli/PrivateKeyProvider.java`** -> AI Confidence: **99.18%**
97. **`cli/src/main/java/hudson/cli/SSHCLI.java`** -> AI Confidence: **99.18%**
98. **`core/src/main/java/hudson/ExtensionList.java`** -> AI Confidence: **99.18%**
99. **`core/src/main/java/hudson/LocalPluginManager.java`** -> AI Confidence: **99.18%**
100. **`core/src/main/java/hudson/WebAppMain.java`** -> AI Confidence: **99.18%**
101. **`core/src/main/java/hudson/cli/CLIAction.java`** -> AI Confidence: **99.18%**
102. **`core/src/main/java/hudson/cli/CopyJobCommand.java`** -> AI Confidence: **99.18%**
103. **`core/src/main/java/hudson/cli/HelpCommand.java`** -> AI Confidence: **99.18%**
104. **`core/src/main/java/hudson/cli/SetBuildDescriptionCommand.java`** -> AI Confidence: **99.18%**
105. **`core/src/main/java/hudson/cli/declarative/MethodBinder.java`** -> AI Confidence: **99.18%**
106. **`core/src/main/java/hudson/cli/handlers/GenericItemOptionHandler.java`** -> AI Confidence: **99.18%**
107. **`core/src/main/java/hudson/console/ConsoleAnnotationOutputStream.java`** -> AI Confidence: **99.18%**
108. **`core/src/main/java/hudson/console/ConsoleNote.java`** -> AI Confidence: **99.18%**
109. **`core/src/main/java/hudson/console/HyperlinkNote.java`** -> AI Confidence: **99.18%**
110. **`core/src/main/java/hudson/console/PlainTextConsoleOutputStream.java`** -> AI Confidence: **99.18%**
111. **`core/src/main/java/hudson/init/InitStrategy.java`** -> AI Confidence: **99.18%**
112. **`core/src/main/java/hudson/init/impl/InstallUncaughtExceptionHandler.java`** -> AI Confidence: **99.18%**
113. **`core/src/main/java/hudson/lifecycle/UnixLifecycle.java`** -> AI Confidence: **99.18%**
114. **`core/src/main/java/hudson/logging/LogRecorder.java`** -> AI Confidence: **99.18%**
115. **`core/src/main/java/hudson/logging/WeakLogHandler.java`** -> AI Confidence: **99.18%**
116. **`core/src/main/java/hudson/model/AbstractItem.java`** -> AI Confidence: **99.18%**
117. **`core/src/main/java/hudson/model/AbstractModelObject.java`** -> AI Confidence: **99.18%**
118. **`core/src/main/java/hudson/model/BuildAuthorizationToken.java`** -> AI Confidence: **99.18%**
119. **`core/src/main/java/hudson/model/BuildTimelineWidget.java`** -> AI Confidence: **99.18%**
120. **`core/src/main/java/hudson/model/ChoiceParameterDefinition.java`** -> AI Confidence: **99.18%**
121. **`core/src/main/java/hudson/model/ComputerPinger.java`** -> AI Confidence: **99.18%**
122. **`core/src/main/java/hudson/model/FileParameterDefinition.java`** -> AI Confidence: **99.18%**
123. **`core/src/main/java/hudson/model/FileParameterValue.java`** -> AI Confidence: **99.18%**
124. **`core/src/main/java/hudson/model/ItemGroup.java`** -> AI Confidence: **99.18%**
125. **`core/src/main/java/hudson/model/Label.java`** -> AI Confidence: **99.18%**
126. **`core/src/main/java/hudson/model/LoadStatistics.java`** -> AI Confidence: **99.18%**
127. **`core/src/main/java/hudson/model/ModifiableItemGroup.java`** -> AI Confidence: **99.18%**
128. **`core/src/main/java/hudson/model/MultiStageTimeSeries.java`** -> AI Confidence: **99.18%**
129. **`core/src/main/java/hudson/model/Project.java`** -> AI Confidence: **99.18%**
130. **`core/src/main/java/hudson/model/Result.java`** -> AI Confidence: **99.18%**
131. **`core/src/main/java/hudson/model/RunMap.java`** -> AI Confidence: **99.18%**
132. **`core/src/main/java/hudson/model/Slave.java`** -> AI Confidence: **99.18%**
133. **`core/src/main/java/hudson/model/StringParameterDefinition.java`** -> AI Confidence: **99.18%**
134. **`core/src/main/java/hudson/model/TaskListener.java`** -> AI Confidence: **99.18%**
135. **`core/src/main/java/hudson/model/UserIdMapper.java`** -> AI Confidence: **99.18%**
136. **`core/src/main/java/hudson/model/View.java`** -> AI Confidence: **99.18%**
137. **`core/src/main/java/hudson/model/ViewJob.java`** -> AI Confidence: **99.18%**
138. **`core/src/main/java/hudson/model/labels/LabelExpression.java`** -> AI Confidence: **99.18%**
139. **`core/src/main/java/hudson/model/listeners/ItemListener.java`** -> AI Confidence: **99.18%**
140. **`core/src/main/java/hudson/model/listeners/SCMListener.java`** -> AI Confidence: **99.18%**
141. **`core/src/main/java/hudson/model/queue/QueueSorter.java`** -> AI Confidence: **99.18%**
142. **`core/src/main/java/hudson/model/userproperty/UserPropertyCategoryAction.java`** -> AI Confidence: **99.18%**
143. **`core/src/main/java/hudson/node_monitors/ResponseTimeMonitor.java`** -> AI Confidence: **99.18%**
144. **`core/src/main/java/hudson/node_monitors/TemporarySpaceMonitor.java`** -> AI Confidence: **99.18%**
145. **`core/src/main/java/hudson/scm/NullSCM.java`** -> AI Confidence: **99.18%**
146. **`core/src/main/java/hudson/scm/SCMDescriptor.java`** -> AI Confidence: **99.18%**
147. **`core/src/main/java/hudson/security/AbstractPasswordBasedSecurityRealm.java`** -> AI Confidence: **99.18%**
148. **`core/src/main/java/hudson/security/FederatedLoginService.java`** -> AI Confidence: **99.18%**
149. **`core/src/main/java/hudson/security/HudsonFilter.java`** -> AI Confidence: **99.18%**
150. **`core/src/main/java/hudson/security/HudsonPrivateSecurityRealm.java`** -> AI Confidence: **99.18%**
151. **`core/src/main/java/hudson/security/PermissionGroup.java`** -> AI Confidence: **99.18%**
152. **`core/src/main/java/hudson/security/SecurityRealm.java`** -> AI Confidence: **99.18%**
153. **`core/src/main/java/hudson/security/SidACL.java`** -> AI Confidence: **99.18%**
154. **`core/src/main/java/hudson/security/UnwrapSecurityExceptionFilter.java`** -> AI Confidence: **99.18%**
155. **`core/src/main/java/hudson/slaves/CloudRetentionStrategy.java`** -> AI Confidence: **99.18%**
156. **`core/src/main/java/hudson/slaves/CloudSlaveRetentionStrategy.java`** -> AI Confidence: **99.18%**
157. **`core/src/main/java/hudson/slaves/ConnectionActivityMonitor.java`** -> AI Confidence: **99.18%**
158. **`core/src/main/java/hudson/slaves/DelegatingComputerLauncher.java`** -> AI Confidence: **99.18%**
159. **`core/src/main/java/hudson/slaves/WorkspaceList.java`** -> AI Confidence: **99.18%**
160. **`core/src/main/java/hudson/tasks/BuildTrigger.java`** -> AI Confidence: **99.18%**
161. **`core/src/main/java/hudson/tasks/Shell.java`** -> AI Confidence: **99.18%**
162. **`core/src/main/java/hudson/tools/AbstractCommandInstaller.java`** -> AI Confidence: **99.18%**
163. **`core/src/main/java/hudson/tools/DownloadFromUrlInstaller.java`** -> AI Confidence: **99.18%**
164. **`core/src/main/java/hudson/tools/ToolLocationNodeProperty.java`** -> AI Confidence: **99.18%**
165. **`core/src/main/java/hudson/tools/ZipExtractionInstaller.java`** -> AI Confidence: **99.18%**
166. **`core/src/main/java/hudson/triggers/SafeTimerTask.java`** -> AI Confidence: **99.18%**
167. **`core/src/main/java/hudson/triggers/TimerTrigger.java`** -> AI Confidence: **99.18%**
168. **`core/src/main/java/hudson/util/BootFailure.java`** -> AI Confidence: **99.18%**
169. **`core/src/main/java/hudson/util/CharacterEncodingFilter.java`** -> AI Confidence: **99.18%**
170. **`core/src/main/java/hudson/util/CompressedFile.java`** -> AI Confidence: **99.18%**
171. **`core/src/main/java/hudson/util/DirScanner.java`** -> AI Confidence: **99.18%**
172. **`core/src/main/java/hudson/util/Graph.java`** -> AI Confidence: **99.18%**
173. **`core/src/main/java/hudson/util/Iterators.java`** -> AI Confidence: **99.18%**
174. **`core/src/main/java/hudson/util/Protector.java`** -> AI Confidence: **99.18%**
175. **`core/src/main/java/hudson/util/ReflectionUtils.java`** -> AI Confidence: **99.18%**
176. **`core/src/main/java/hudson/util/RobustCollectionConverter.java`** -> AI Confidence: **99.18%**
177. **`core/src/main/java/hudson/util/RunList.java`** -> AI Confidence: **99.18%**
178. **`core/src/main/java/hudson/util/StreamTaskListener.java`** -> AI Confidence: **99.18%**
179. **`core/src/main/java/hudson/util/XStream2.java`** -> AI Confidence: **99.18%**
180. **`core/src/main/java/hudson/util/io/ReopenableRotatingFileOutputStream.java`** -> AI Confidence: **99.18%**
181. **`core/src/main/java/hudson/util/io/RewindableRotatingFileOutputStream.java`** -> AI Confidence: **99.18%**
182. **`core/src/main/java/hudson/util/xstream/ImmutableListConverter.java`** -> AI Confidence: **99.18%**
183. **`core/src/main/java/hudson/views/ListViewColumn.java`** -> AI Confidence: **99.18%**
184. **`core/src/main/java/hudson/widgets/RenderOnDemandClosure.java`** -> AI Confidence: **99.18%**
185. **`core/src/main/java/jenkins/MetaLocaleDrivenResourceProvider.java`** -> AI Confidence: **99.18%**
186. **`core/src/main/java/jenkins/PluginSubtypeMarker.java`** -> AI Confidence: **99.18%**
187. **`core/src/main/java/jenkins/agents/WebSocketAgents.java`** -> AI Confidence: **99.18%**
188. **`core/src/main/java/jenkins/cli/listeners/DefaultCLIListener.java`** -> AI Confidence: **99.18%**
189. **`core/src/main/java/jenkins/health/HealthCheckAction.java`** -> AI Confidence: **99.18%**
190. **`core/src/main/java/jenkins/management/AdministrativeMonitorsConfiguration.java`** -> AI Confidence: **99.18%**
191. **`core/src/main/java/jenkins/management/AsynchronousAdministrativeMonitor.java`** -> AI Confidence: **99.18%**
192. **`core/src/main/java/jenkins/model/AssetManager.java`** -> AI Confidence: **99.18%**
193. **`core/src/main/java/jenkins/model/BackgroundGlobalBuildDiscarder.java`** -> AI Confidence: **99.18%**
194. **`core/src/main/java/jenkins/model/GlobalBuildDiscarderStrategy.java`** -> AI Confidence: **99.18%**
195. **`core/src/main/java/jenkins/model/GlobalComputerRetentionCheckIntervalConfiguration.java`** -> AI Confidence: **99.18%**
196. **`core/src/main/java/jenkins/model/GlobalQuietPeriodConfiguration.java`** -> AI Confidence: **99.18%**
197. **`core/src/main/java/jenkins/model/IExecutor.java`** -> AI Confidence: **99.18%**
198. **`core/src/main/java/jenkins/model/JenkinsLocationConfiguration.java`** -> AI Confidence: **99.18%**
199. **`core/src/main/java/jenkins/model/SimpleGlobalBuildDiscarderStrategy.java`** -> AI Confidence: **99.18%**
200. **`core/src/main/java/jenkins/model/StandardArtifactManager.java`** -> AI Confidence: **99.18%**
201. **`core/src/main/java/jenkins/model/identity/IdentityRootAction.java`** -> AI Confidence: **99.18%**
202. **`core/src/main/java/jenkins/model/lazy/BuildReference.java`** -> AI Confidence: **99.18%**
203. **`core/src/main/java/jenkins/model/lazy/BuildReferenceMapAdapter.java`** -> AI Confidence: **99.18%**
204. **`core/src/main/java/jenkins/model/queue/CompositeCauseOfBlockage.java`** -> AI Confidence: **99.18%**
205. **`core/src/main/java/jenkins/model/queue/QueueIdStrategy.java`** -> AI Confidence: **99.18%**
206. **`core/src/main/java/jenkins/mvn/FilePathSettingsProvider.java`** -> AI Confidence: **99.18%**
207. **`core/src/main/java/jenkins/plugins/DetachedPluginsUtil.java`** -> AI Confidence: **99.18%**
208. **`core/src/main/java/jenkins/run/ChangesTabFactory.java`** -> AI Confidence: **99.18%**
209. **`core/src/main/java/jenkins/scm/SCMCheckoutStrategy.java`** -> AI Confidence: **99.18%**
210. **`core/src/main/java/jenkins/scm/SCMDecisionHandler.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `test/src/test/java/jenkins/install/SetupWizardTest.java` -> **44.4672%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `50` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `27645` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `core/src/main/java/hudson/model/AbstractCIBase.java` (JAVA) -> Cumulative Risk: **712.52**
- **Archetype:** `file_cluster_13` (Distance: 12.453 IQR)
- **Magnitude:** 192.32 | **LOC:** 278 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9816%), State Flux (99.9178%), Tech Debt (98.9971%)
- **Heaviest Functions:** `createNewComputerForNode` (Impact: 45.6), `updateComputerList` (Impact: 28.0), `updateComputer` (Impact: 14.2)

### 2. `src/main/js/components/dialogs/index.js` (JAVASCRIPT) -> Cumulative Risk: **700.01**
- **Archetype:** `file_cluster_4` (Distance: 13.585 IQR)
- **Magnitude:** 436.22 | **LOC:** 360 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `init` (Impact: 43.3), `appendButtons` (Impact: 19.2), `show` (Impact: 15.0)

### 3. `core/src/main/resources/jenkins/security/apitoken/LegacyApiTokenAdministrativeMonitor/resources.js` (JAVASCRIPT) -> Cumulative Risk: **668.89**
- **Archetype:** `file_cluster_4` (Distance: 12.51 IQR)
- **Magnitude:** 174.66 | **LOC:** 189 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9998%)
- **Heaviest Functions:** `checkTheDesiredOne` (Impact: 13.3), `confirmAndRevokeAllSelected` (Impact: 12.6), `onCheckChanged` (Impact: 5.6)

### 4. `core/src/main/java/hudson/util/SequentialExecutionQueue.java` (JAVA) -> Cumulative Risk: **666.38**
- **Archetype:** `file_cluster_4` (Distance: 11.235 IQR)
- **Magnitude:** 105.46 | **LOC:** 137 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8552%), Concurrency (99.0684%)
- **Heaviest Functions:** `run` (Impact: 12.2), `isStarving` (Impact: 10.1), `execute` (Impact: 9.0)

### 5. `src/main/js/pluginSetupWizardGui.js` (JAVASCRIPT) -> Cumulative Risk: **656.86**
- **Archetype:** `file_cluster_13` (Distance: 13.382 IQR)
- **Magnitude:** 1144.76 | **LOC:** 1455 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (93.4976%)
- **Heaviest Functions:** `createPluginSetupWizard` (Impact: 163.1), `searchForPlugins` (Impact: 67.8), `setPanel` (Impact: 54.0)

### 6. `src/main/js/add-item.js` (JAVASCRIPT) -> Cumulative Risk: **655.04**
- **Archetype:** `file_cluster_17` (Distance: 11.792 IQR)
- **Magnitude:** 275.94 | **LOC:** 302 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9946%), State Flux (99.928%), Concurrency (98.5105%)
- **Heaviest Functions:** `getItems` (Impact: 69.0), `drawIcon` (Impact: 18.0), `nameFieldEvent` (Impact: 11.7)

### 7. `core/src/main/java/jenkins/telemetry/impl/UserLanguages.java` (JAVA) -> Cumulative Risk: **650.78**
- **Archetype:** `file_cluster_4` (Distance: 12.159 IQR)
- **Magnitude:** 87.46 | **LOC:** 110 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9668%)
- **Heaviest Functions:** `createContent` (Impact: 9.6), `handle` (Impact: 7.6), `getId` (Impact: 2.7)

### 8. `core/src/main/resources/lib/hudson/progressive-text.js` (JAVASCRIPT) -> Cumulative Risk: **644.83**
- **Archetype:** `file_cluster_4` (Distance: 11.812 IQR)
- **Magnitude:** 1.75 | **LOC:** 115 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9985%), State Flux (99.871%), Concurrency (99.3536%)
- **Heaviest Functions:** `fetchNext` (Impact: 38.4), `fetchNext` (Impact: 4.5), `fetchNext` (Impact: 2.5)

### 9. `core/src/main/java/hudson/scm/SCMDescriptor.java` (JAVA) -> Cumulative Risk: **642.91**
- **Archetype:** `file_cluster_13` (Distance: 11.978 IQR)
- **Magnitude:** 94.88 | **LOC:** 173 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9996%), State Flux (89.9763%)
- **Heaviest Functions:** `load` (Impact: 13.0), `isApplicable` (Impact: 7.7), `isApplicable` (Impact: 7.1)

### 10. `core/src/main/java/jenkins/model/CoreEnvironmentContributor.java` (JAVA) -> Cumulative Risk: **642.41**
- **Archetype:** `file_cluster_4` (Distance: 12.348 IQR)
- **Magnitude:** 76.34 | **LOC:** 71 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9939%), Tech Debt (99.8115%)
- **Heaviest Functions:** `buildEnvironmentFor` (Impact: 17.4), `buildEnvironmentFor` (Impact: 6.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `core/src/main/java/jenkins/model/Jenkins.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.458 IQR)
- **Top Global Matches:** file_cluster_13: 13.458, file_cluster_0: 13.582, file_cluster_11: 13.864
- **Magnitude:** 4917.26 | **LOC:** 5991 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (22.4391%), Tech Debt (99.9817%)
**Top Internal Functions/Classes:**
  * `onInitMilestoneAttained` (Impact: 717.3)
  * `executeReactor` (Impact: 536.2)
  * `resetFilter` (Impact: 449.9)
  * `loadTasks` (Impact: 365.2)
    * *Intent:* /** * If usage statistics are being collected * * @return {@code true} if usage statistics should be...
  * `doSafeExit` (Impact: 322.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 859`, `args: 227`, `func_start: 274`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 149`, `state_mutation: 217`, `dead_code: 8`, `planned_debt: 9`, `fragile_debt: 3`, `duplicate_logic: 64`
* *Architecture:* `io: 22`, `api: 320`, `concurrency: 69`, `import: 317`
* *Defense:* `safety: 129`, `doc: 259`, `sync_locks: 15`, `immutability_locks: 72`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.768
  * `Choke Point (Betweenness):` 0.00242 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 187):` java.util.Map, hudson.PluginManager, hudson.security.ACLContext, hudson.slaves.NodeDescriptor, hudson.model.Job, hudson.security.HudsonFilter, hudson.model.DescriptorByNameOwner, jenkins.util.io.FileBoolean...
  * `Imported By (In-Degree: 511):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/FilePath.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.143 IQR)
- **Top Global Matches:** file_cluster_13: 12.143, file_cluster_0: 12.345, file_cluster_8: 12.614
- **Magnitude:** 3251.32 | **LOC:** 3937 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (13.4209%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `unzip` (Impact: 429.0)
  * `isUnix` (Impact: 428.1)
    * *Intent:* /** * When this {@link FilePath} represents the remote path, * this field is always non-null on the ...
  * `mkdirs` (Impact: 424.1)
    * *Intent:* // shouldn't need this replace, but better safe than sorry
  * `invoke` (Impact: 346.0)
  * `readFromTar` (Impact: 262.2)
    * *Intent:* /** * Executed after the actual FileCallable is invoked (even if this one failed). This code will ru...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 578`, `args: 164`, `func_start: 166`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 55`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 79`
* *Architecture:* `io: 147`, `api: 138`, `concurrency: 26`, `import: 118`
* *Defense:* `safety: 87`, `doc: 146`, `sync_locks: 1`, `immutability_locks: 114`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.502
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` java.net.HttpURLConnection, java.util.Map, jenkins.MasterToSlaveFileCallable, org.jenkinsci.remoting.RoleChecker, java.nio.charset.StandardCharsets, org.jenkinsci.remoting.RoleSensitive, java.net.URI, java.io.BufferedInputStream...
  * `Imported By (In-Degree: 101):` (Excluded from Brief to save tokens)

### `core/src/test/java/jenkins/org/apache/commons/validator/routines/InetAddressValidatorTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_15` (Drift: 11.117 IQR)
- **Top Global Matches:** file_cluster_15: 11.117, file_cluster_8: 11.417, file_cluster_7: 11.875
- **Magnitude:** 2568.08 | **LOC:** 656 | **CtrlFlow:** 98.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.0544%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testIPv6` (Impact: 2289.8)
  * `testVALIDATOR_445` (Impact: 179.2)
  * `testVALIDATOR_419` (Impact: 50.9)
  * `testVALIDATOR_335` (Impact: 30.2)
    * *Intent:* /** * Test cases for InetAddressValidator. * * @version $Revision$ */
  * `testInetAddressesByClass` (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1266`, `structural_boundaries: 26`, `args: 263`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `import: 4`
* *Defense:* `doc: 7`, `test: 185`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.junit.jupiter.api.BeforeEach, org.junit.jupiter.api.Assertions.assertFalse, org.junit.jupiter.api.Test, org.junit.jupiter.api.Assertions.assertTrue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/model/Queue.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.502 IQR)
- **Top Global Matches:** file_cluster_13: 11.502, file_cluster_0: 11.711, file_cluster_11: 12.177
- **Magnitude:** 1236.5 | **LOC:** 3253 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (14.4021%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `clear` (Impact: 287.5)
  * `maintain` (Impact: 240.3)
  * `toString` (Impact: 125.0)
  * `updateSnapshot` (Impact: 52.8)
  * `save` (Impact: 30.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 282`, `args: 77`, `func_start: 85`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 22`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 34`
* *Architecture:* `io: 4`, `api: 88`, `concurrency: 14`, `import: 115`
* *Defense:* `safety: 33`, `doc: 47`, `sync_locks: 24`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.881
  * `Choke Point (Betweenness):` 0.000232 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 51):` java.util.Map, java.time.Duration, org.jenkinsci.remoting.RoleChecker, hudson.model.queue.CauseOfBlockage.BecauseLabelIsOffline, com.google.common.cache.Cache, java.util.Collections, jenkins.util.SystemProperties, edu.umd.cs.findbugs.annotations.CheckForNull...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `src/main/js/pluginSetupWizardGui.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.382 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.517 IQR)
- **Top Global Matches:** file_cluster_13: 13.382, file_cluster_8: 13.456, file_cluster_4: 13.464
- **Magnitude:** 1144.76 | **LOC:** 1455 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.4976%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `createPluginSetupWizard` (Impact: 163.1)
  * `searchForPlugins` (Impact: 67.8)
  * `setPanel` (Impact: 54.0)
  * `getAllDependencies` (Impact: 52.8)
  * `resumeInstallation` (Impact: 21.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 197`, `args: 78`, `func_start: 97`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 401`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 43`
* *Architecture:* `api: 22`, `concurrency: 25`, `import: 21`
* *Defense:* `safety: 26`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` incompleteInstallationPanel.hbs, jenkins, pluginManager, proxyConfigPanel.hbs, id, progressPanel.hbs, pluginSelectionPanel.hbs, pluginSetupWizard.hbs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/PluginManager.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.851 IQR)
- **Top Global Matches:** file_cluster_13: 12.851, file_cluster_0: 13.081, file_cluster_11: 13.227
- **Magnitude:** 984.7 | **LOC:** 2698 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (25.9996%), Tech Debt (99.9885%)
**Top Internal Functions/Classes:**
  * `parseRequestedPlugins` (Impact: 141.1)
  * `initTasks` (Impact: 40.8)
    * *Intent:* /**
  * `run` (Impact: 36.8)
    * *Intent:* /** * {@link ClassLoader} that can load all the publicly visible classes from plugins * (and includi...
  * `run` (Impact: 36.5)
    * *Intent:* /** * {@link ClassLoader} that can load all the publicly visible classes from plugins * (and includi...
  * `TaskGraphBuilder` (Impact: 32.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 379`, `args: 72`, `func_start: 67`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 122`, `planned_debt: 5`, `duplicate_logic: 28`
* *Architecture:* `io: 32`, `api: 101`, `concurrency: 3`, `import: 154`
* *Defense:* `safety: 69`, `doc: 89`, `sync_locks: 1`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` java.util.Map, hudson.util.Retrier, hudson.security.ACLContext, java.time.Duration, jenkins.util.io.OnMaster, org.kohsuke.stapler.verb.POST, hudson.init.InitMilestone.PLUGINS_LISTED, org.kohsuke.stapler.StaplerRequest...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/Functions.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.252 IQR)
- **Top Global Matches:** file_cluster_13: 12.252, file_cluster_0: 12.658, file_cluster_16: 12.814
- **Magnitude:** 969.98 | **LOC:** 2743 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (18.3673%), Tech Debt (99.9019%)
**Top Internal Functions/Classes:**
  * `dumpThreadInfo` (Impact: 49.8)
    * *Intent:* /** * @deprecated use {@link #getCookie(HttpServletRequest, String)} */
  * `getPageDecorators` (Impact: 40.7)
  * `getRelativeNameFrom` (Impact: 38.0)
  * `doPrintStackTrace` (Impact: 31.8)
    * *Intent:* /** * Finds the given object in the ancestor list and returns its URL. * This is used to determine t...
  * `htmlAttributeEscape` (Impact: 30.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 407`, `args: 128`, `func_start: 119`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 107`, `state_mutation: 52`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 27`
* *Architecture:* `io: 3`, `api: 178`, `concurrency: 33`, `import: 167`
* *Defense:* `safety: 38`, `doc: 138`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.221
  * `Choke Point (Betweenness):` 0.000451 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 83):` java.util.Map, hudson.tasks.Publisher, org.kohsuke.stapler.StaplerRequest, hudson.cli.CLICommand, hudson.model.ItemGroup, hudson.model.Job, java.nio.charset.StandardCharsets, java.net.URI...
  * `Imported By (In-Degree: 136):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Run.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.626 IQR)
- **Top Global Matches:** file_cluster_13: 12.626, file_cluster_0: 12.825, file_cluster_11: 13.182
- **Magnitude:** 945.82 | **LOC:** 2700 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (13.4759%), Tech Debt (99.7304%)
**Top Internal Functions/Classes:**
  * `computeDisplayName` (Impact: 264.4)
    * *Intent:* /** * Returns the {@link Cause}s that triggered a build. * * <p> * If a build sits in the queue for ...
  * `execute` (Impact: 77.0)
  * `onStartBuilding` (Impact: 25.7)
  * `onLoad` (Impact: 21.0)
  * `setResult` (Impact: 17.7)
    * *Intent:* /** * If the build is in progress, remember {@link RunExecution} that's running it.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 376`, `args: 66`, `func_start: 90`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 61`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 20`
* *Architecture:* `io: 11`, `api: 138`, `concurrency: 6`, `import: 125`
* *Defense:* `safety: 81`, `doc: 137`, `sync_locks: 1`, `immutability_locks: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.083
  * `Choke Point (Betweenness):` 0.000432 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 58):` java.util.Map, jenkins.util.io.OnMaster, org.kohsuke.stapler.verb.POST, hudson.console.ConsoleNote, org.kohsuke.stapler.StaplerRequest, org.kohsuke.stapler.StaplerProxy, java.util.Comparator, java.util.Collections...
  * `Imported By (In-Degree: 108):` (Excluded from Brief to save tokens)

### `test/src/test/java/hudson/model/DirectoryBrowserSupportTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.147 IQR)
- **Top Global Matches:** file_cluster_0: 11.147, file_cluster_13: 11.273, file_cluster_8: 11.537
- **Magnitude:** 895.42 | **LOC:** 1538 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (14.8999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doubleDots` (Impact: 217.4)
  * `root` (Impact: 23.3)
  * `root` (Impact: 23.0)
  * `contentSecurityPolicy` (Impact: 17.0)
    * *Intent:* // when there was a file leak, the number of open file handle was always // greater or equal to the ...
  * `getListOfEntriesInDownloadedZip` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 313`, `args: 105`, `func_start: 106`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 96`, `planned_debt: 2`, `duplicate_logic: 71`, `orphaned_logic: 24`
* *Architecture:* `io: 67`, `api: 81`, `import: 77`
* *Defense:* `safety: 21`, `doc: 13`, `test: 131`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` java.net.HttpURLConnection, java.util.Map, org.junit.jupiter.api.Assertions.assertEquals, org.junit.jupiter.api.Assumptions.assumeTrue, hudson.util.StreamTaskListener, java.nio.charset.StandardCharsets, org.hamcrest.Matchers.containsInAnyOrder, java.io.FileNotFoundException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/test/java/hudson/FunctionsTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.864 IQR)
- **Top Global Matches:** file_cluster_8: 10.864, file_cluster_13: 10.929, file_cluster_0: 10.967
- **Magnitude:** 888.32 | **LOC:** 800 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.2985%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `printThrowable` (Impact: 456.3)
  * `testGetRelativeLinkTo_JobNotContainedInV` (Impact: 23.2)
  * `assertPrintThrowable` (Impact: 20.6)
  * `testGetRelativeLinkTo_JobContainedInView` (Impact: 19.1)
  * `getRelativeLinkTo_MavenModules` (Impact: 18.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 168`, `args: 60`, `func_start: 77`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 19`, `planned_debt: 1`, `duplicate_logic: 12`, `orphaned_logic: 28`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 43`
* *Defense:* `safety: 12`, `test: 162`, `sync_locks: 2`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` org.junit.jupiter.params.ParameterizedTest, org.junit.jupiter.api.Assertions.assertEquals, java.util.Arrays, hudson.console.ConsoleAnnotatorFactory.RootAction, org.hamcrest.Matchers.emptyString, org.hamcrest.Matchers.is, hudson.model.ItemGroup, org.kohsuke.stapler.StaplerRequest2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/report-l10n.rb` (RUBY | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.244 IQR)
- **Top Global Matches:** file_cluster_8: 8.244, file_cluster_7: 9.069, file_cluster_1: 9.311
- **Magnitude:** 884.1 | **LOC:** 552 | **CtrlFlow:** 99.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.0422%), Tech Debt (16.2077%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 837.1)
  * `ISO639` (Impact: 24.9)
    * *Intent:* # from https://github.com/ged/linguistics/blob/master/lib/linguistics/iso639.rb # Hash of ISO639 2- ...
  * `Anonymous_Block` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 2`, `args: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` set
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/model/UpdateCenter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.502 IQR)
- **Top Global Matches:** file_cluster_13: 11.502, file_cluster_0: 11.754, file_cluster_4: 12.038
- **Magnitude:** 843.68 | **LOC:** 2956 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.9834%), Tech Debt (99.9753%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 281.9)
  * `verifyChecksums` (Impact: 64.9)
  * `run` (Impact: 28.8)
    * *Intent:* /** * Gets a job by its ID.
  * `getComputedSHA512` (Impact: 28.2)
  * `_run` (Impact: 19.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 278`, `args: 68`, `func_start: 84`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 13`, `dead_code: 1`, `duplicate_logic: 30`
* *Architecture:* `io: 28`, `api: 96`, `concurrency: 36`, `import: 111`
* *Defense:* `safety: 40`, `doc: 71`, `sync_locks: 9`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` java.net.HttpURLConnection, hudson.PluginManager, java.util.Map, hudson.security.ACLContext, jenkins.util.io.OnMaster, java.util.Vector, org.kohsuke.stapler.StaplerRequest, jenkins.management.Badge...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/model/Fingerprint.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.236 IQR)
- **Top Global Matches:** file_cluster_0: 12.236, file_cluster_13: 12.259, file_cluster_4: 12.537
- **Magnitude:** 829.28 | **LOC:** 1503 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.044%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `fromString` (Impact: 52.8)
    * *Intent:* /**
  * `canDiscoverItem` (Impact: 38.9)
  * `removeAll` (Impact: 32.6)
  * `trim` (Impact: 29.4)
  * `retainAll` (Impact: 26.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 259`, `args: 87`, `func_start: 96`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 95`, `dead_code: 4`, `planned_debt: 3`, `duplicate_logic: 39`
* *Architecture:* `io: 3`, `api: 111`, `concurrency: 39`, `import: 46`
* *Defense:* `safety: 43`, `doc: 91`, `sync_locks: 19`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.274
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` java.util.Date, java.util.Map, hudson.security.ACLContext, hudson.util.PersistedList, jenkins.fingerprints.FingerprintStorage, jenkins.model.FingerprintFacet, com.thoughtworks.xstream.converters.UnmarshallingContext, com.thoughtworks.xstream.converters.Converter...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/security/HudsonPrivateSecurityRealm.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.454 IQR)
- **Top Global Matches:** file_cluster_13: 10.454, file_cluster_0: 10.674, file_cluster_8: 11.0
- **Magnitude:** 791.84 | **LOC:** 1189 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (6.7453%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `HudsonPrivateSecurityRealm` (Impact: 155.1)
  * `setCaptchaSupport` (Impact: 137.7)
    * *Intent:* /**
  * `_doCreateAccount` (Impact: 131.2)
    * *Intent:* /** * Computes if this Hudson has some user accounts configured. *
  * `newInstance` (Impact: 18.1)
    * *Intent:* // form field validation // this pattern needs to be generalized and moved to stapler
  * `load` (Impact: 15.2)
    * *Intent:* /** * Default REGEX for the user ID check in case the ID_REGEX is not set
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 209`, `args: 68`, `func_start: 69`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 9`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 26`
* *Architecture:* `api: 77`, `concurrency: 1`, `import: 77`
* *Defense:* `safety: 12`, `doc: 25`, `sync_locks: 1`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.184
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` java.nio.charset.StandardCharsets, jakarta.servlet.FilterConfig, java.util.Collections, jenkins.util.SystemProperties, org.springframework.security.crypto.password.PasswordEncoder, java.util.regex.Pattern, hudson.security.captcha.CaptchaSupport, org.springframework.security.core.userdetails.UsernameNotFoundException...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/slaves/SlaveComputer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.491 IQR)
- **Top Global Matches:** file_cluster_13: 11.491, file_cluster_0: 11.6, file_cluster_11: 12.073
- **Magnitude:** 778.0 | **LOC:** 1207 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (15.9386%), Tech Debt (99.9991%)
**Top Internal Functions/Classes:**
  * `_connect` (Impact: 145.4)
  * `disconnect` (Impact: 85.7)
  * `closeChannel` (Impact: 85.5)
  * `setChannel` (Impact: 60.7)
  * `onClosed` (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 224`, `args: 56`, `func_start: 65`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 36`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 20`
* *Architecture:* `io: 10`, `api: 72`, `concurrency: 13`, `import: 78`
* *Defense:* `safety: 27`, `doc: 40`, `sync_locks: 3`, `immutability_locks: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 8.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` hudson.model.Executor, java.util.Map, hudson.model.Queue, hudson.security.ACLContext, hudson.util.StreamTaskListener, java.nio.channels.ClosedChannelException, java.util.Collections, jenkins.util.SystemProperties...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Job.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.1 IQR)
- **Top Global Matches:** file_cluster_13: 12.1, file_cluster_0: 12.26, file_cluster_11: 12.668
- **Magnitude:** 774.68 | **LOC:** 1732 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (18.6922%), Tech Debt (99.602%)
**Top Internal Functions/Classes:**
  * `getBuildStabilityHealthReport` (Impact: 56.6)
    * *Intent:* /** * Directory for storing {@link Run} records. * <p> * Some {@link Job}s may not have backing data...
  * `doRssChangelog` (Impact: 33.1)
    * *Intent:* /** * Gets the read-only view of the recent builds.
  * `onLocationChanged` (Impact: 23.4)
  * `getEstimatedDurationCandidates` (Impact: 21.7)
  * `getDynamic` (Impact: 19.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 331`, `args: 89`, `func_start: 100`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 71`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `io: 16`, `api: 139`, `concurrency: 14`, `import: 114`
* *Defense:* `safety: 24`, `doc: 101`, `sync_locks: 9`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.979
  * `Choke Point (Betweenness):` 0.000414 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 55):` java.util.Map, org.kohsuke.stapler.verb.POST, org.kohsuke.stapler.StaplerRequest, jenkins.model.PeepholePermalink, hudson.widgets.HistoryWidget, java.util.Collections, jenkins.model.HistoricalBuild, edu.umd.cs.findbugs.annotations.CheckForNull...
  * `Imported By (In-Degree: 61):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/View.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.911 IQR)
- **Top Global Matches:** file_cluster_13: 11.911, file_cluster_0: 12.137, file_cluster_11: 12.624
- **Magnitude:** 743.58 | **LOC:** 1286 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.008%), Tech Debt (99.6128%)
**Top Internal Functions/Classes:**
  * `getProperties` (Impact: 187.3)
    * *Intent:* /**
  * `writeXml` (Impact: 40.8)
  * `updateByXml` (Impact: 40.6)
    * *Intent:* /** * Returns the page to redirect the user to, after the view is created. * * The returned string i...
  * `doItemCategories` (Impact: 19.9)
  * `doCheckJobName` (Impact: 17.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 261`, `args: 64`, `func_start: 77`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 40`, `dead_code: 3`, `duplicate_logic: 18`
* *Architecture:* `io: 6`, `api: 91`, `concurrency: 11`, `import: 97`
* *Defense:* `safety: 25`, `doc: 68`, `sync_locks: 6`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.046
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` java.util.Map, org.kohsuke.stapler.verb.POST, org.kohsuke.stapler.StaplerRequest, javax.xml.transform.stream.StreamResult, java.nio.charset.StandardCharsets, java.io.BufferedInputStream, java.util.Comparator, java.util.Collections...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/AbstractProject.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.057 IQR)
- **Top Global Matches:** file_cluster_13: 12.057, file_cluster_0: 12.191, file_cluster_11: 12.544
- **Magnitude:** 736.3 | **LOC:** 2164 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.1932%), Tech Debt (88.3932%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 37.0)
  * `getCauseOfBlockage` (Impact: 28.1)
    * *Intent:* /**
  * `workspaceOffline` (Impact: 26.2)
    * *Intent:* /** * Schedules a build of this project, and returns a {@link Future} object * to wait for the compl...
  * `doDoWipeOutWorkspace` (Impact: 20.9)
  * `isAllSuitableNodesOffline` (Impact: 19.1)
    * *Intent:* /** * Schedules a build. * * Important: the actions should be persistable without outside references...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 295`, `args: 86`, `func_start: 95`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 85`, `state_mutation: 50`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 7`
* *Architecture:* `io: 3`, `api: 138`, `concurrency: 18`, `import: 98`
* *Defense:* `safety: 23`, `doc: 110`, `sync_locks: 1`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.325
  * `Choke Point (Betweenness):` 0.000322 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` java.util.Map, hudson.tasks.Publisher, hudson.CopyOnWrite, java.util.Vector, org.kohsuke.stapler.verb.POST, org.kohsuke.stapler.StaplerRequest, java.util.Comparator, hudson.model.listeners.SCMPollListener...
  * `Imported By (In-Degree: 74):` (Excluded from Brief to save tokens)

### `war/src/main/webapp/scripts/hudson-behavior.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.123 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.226 IQR)
- **Top Global Matches:** file_cluster_0: 13.123, file_cluster_17: 13.128, file_cluster_11: 13.178
- **Magnitude:** 709.58 | **LOC:** 2761 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (57.6202%), Tech Debt (98.1271%)
**Top Internal Functions/Classes:**
  * `delayedCheck` (Impact: 217.7)
  * `findFollowingTR` (Impact: 61.4)
    * *Intent:* /** * Schedules a form field check. Executions are serialized to reduce the bandwidth impact.
  * `registerValidator` (Impact: 38.5)
    * *Intent:* // https://stackoverflow.com/a/37562814/4951015 // Code could be simplified if support for HTMLUnit ...
  * `findFormParent` (Impact: 30.5)
  * `findNearBy` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 80`, `args: 41`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 2`, `state_mutation: 134`, `dead_code: 4`, `duplicate_logic: 5`, `orphaned_logic: 16`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 24`, `doc: 21`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/util/ProcessTree.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.336 IQR)
- **Top Global Matches:** file_cluster_13: 11.336, file_cluster_0: 11.401, file_cluster_8: 11.736
- **Magnitude:** 670.96 | **LOC:** 2141 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.1739%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getEnvironmentVariables` (Impact: 117.3)
  * `getEnvironmentVariables` (Impact: 55.5)
  * `super` (Impact: 45.4)
    * *Intent:* /** * Kills this process and all the descendants. * <p>
  * `getArguments` (Impact: 35.1)
  * `createProcess` (Impact: 32.7)
    * *Intent:* /** * Serialized form of {@link OSProcess} is the PID and {@link ProcessTree} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 182`, `args: 54`, `func_start: 67`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 14`, `planned_debt: 2`, `duplicate_logic: 32`
* *Architecture:* `io: 11`, `api: 40`, `concurrency: 4`, `import: 51`
* *Defense:* `safety: 44`, `doc: 32`, `sync_locks: 3`, `immutability_locks: 25`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.258
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` java.util.Map, jenkins.agents.AgentComputerUtil, java.util.concurrent.TimeUnit, java.util.Arrays, hudson.util.ProcessTreeRemoting.IProcessTree, java.io.RandomAccessFile, java.nio.charset.StandardCharsets, hudson.util.ProcessTreeRemoting.IOSProcess...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `test/src/test/java/hudson/cli/RunRangeCommandTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.025 IQR)
- **Top Global Matches:** file_cluster_8: 12.025, file_cluster_0: 12.281, file_cluster_13: 12.372
- **Magnitude:** 660.28 | **LOC:** 1040 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.0242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dummyRangeRangeSingleShouldSuccess` (Impact: 34.1)
  * `dummyRangeRangeSingleShouldFailIfBuildRa` (Impact: 30.3)
  * `dummyRangeRangeSingleShouldFailIfBuildRa` (Impact: 25.6)
  * `dummyRangeNumberSingleShouldSuccess` (Impact: 16.3)
  * `dummyRangeNumberMultiShouldFailIfBuildNu` (Impact: 16.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 63`, `args: 39`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 244`, `duplicate_logic: 25`, `orphaned_logic: 13`
* *Architecture:* `api: 3`, `import: 16`
* *Defense:* `doc: 1`, `test: 362`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` hudson.model.Run, org.jvnet.hudson.test.junit.jupiter.WithJenkins, hudson.model.Item, hudson.cli.CLICommandInvoker.Matcher.failedWith, hudson.Extension, hudson.cli.CLICommandInvoker.Matcher.hasNoStandardOutput, org.hamcrest.Matchers.containsString, org.junit.jupiter.api.Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/test/java/lib/form/RepeatableTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.623 IQR)
- **Top Global Matches:** file_cluster_0: 11.623, file_cluster_13: 11.682, file_cluster_8: 11.946
- **Magnitude:** 620.18 | **LOC:** 681 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (25.2855%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testNested` (Impact: 29.4)
  * `testNestedEnabledTopButton` (Impact: 29.4)
    * *Intent:* /** Tests nested repeatable and use of @DataBoundConstructor to process formData */
  * `testNestedEnabledTopButtonInner` (Impact: 29.4)
    * *Intent:* /** Tests nested repeatable and use of @DataBoundConstructor to process formData */
  * `testNestedEnabledTopButtonOuter` (Impact: 29.4)
    * *Intent:* /** Tests nested repeatable and use of @DataBoundConstructor to process formData */
  * `testNestedRadio` (Impact: 23.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 143`, `args: 50`, `func_start: 104`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 74`, `duplicate_logic: 16`, `orphaned_logic: 19`
* *Architecture:* `io: 26`, `api: 36`, `concurrency: 2`, `import: 31`
* *Defense:* `safety: 12`, `doc: 16`, `test: 59`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` org.junit.jupiter.api.Assertions.assertEquals, org.junit.jupiter.api.Assertions.assertThrows, org.htmlunit.html.HtmlButton, org.kohsuke.stapler.StaplerRequest2, org.junit.jupiter.api.Assertions.assertNotNull, java.util.ArrayList, org.htmlunit.html.HtmlForm, org.htmlunit.WebClientUtil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/model/Computer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.835 IQR)
- **Top Global Matches:** file_cluster_13: 11.835, file_cluster_0: 12.032, file_cluster_11: 12.392
- **Magnitude:** 610.88 | **LOC:** 1802 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (9.9515%), Tech Debt (99.2681%)
**Top Internal Functions/Classes:**
  * `getHostName` (Impact: 21.6)
    * *Intent:* /** * Equivalent to {@code disconnect(null)}
  * `doRssLatest` (Impact: 17.7)
  * `setNumExecutors` (Impact: 17.1)
    * *Intent:* // TODO implement addOrReplaceAction, removeAction, removeActions, replaceActions /**
  * `addNewExecutorIfNecessary` (Impact: 17.0)
  * `relocateOldLogs` (Impact: 16.7)
    * *Intent:* /** * Called by {@link Jenkins#updateComputerList(boolean, Collection)} to notify {@link Computer} t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 296`, `args: 71`, `func_start: 87`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 72`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 14`
* *Architecture:* `io: 9`, `api: 122`, `concurrency: 4`, `import: 115`
* *Defense:* `safety: 19`, `doc: 90`, `sync_locks: 3`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.225
  * `Choke Point (Betweenness):` 0.000366 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` java.util.Map, org.kohsuke.stapler.verb.POST, java.nio.charset.StandardCharsets, hudson.slaves.ComputerListener, org.kohsuke.stapler.StaplerProxy, java.util.Collections, java.util.LinkedHashMap, jenkins.util.SystemProperties...
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/ClassicPluginStrategy.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.164 IQR)
- **Top Global Matches:** file_cluster_13: 12.164, file_cluster_0: 12.384, file_cluster_11: 12.454
- **Magnitude:** 590.18 | **LOC:** 700 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.4763%), Tech Debt (99.5991%)
**Top Internal Functions/Classes:**
  * `createPluginWrapper` (Impact: 61.0)
  * `findClass` (Impact: 33.1)
  * `load` (Impact: 31.3)
  * `findComponents` (Impact: 29.6)
    * *Intent:* /** * Creates a classloader that can load all the specified jar files and delegate to the given pare...
  * `loadLinkedManifest` (Impact: 25.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 174`, `args: 35`, `func_start: 41`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 87`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `io: 57`, `api: 28`, `concurrency: 19`, `import: 51`
* *Defense:* `safety: 33`, `doc: 17`, `sync_locks: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.145
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` java.util.Set, org.apache.tools.ant.types.FileSet, java.util.Arrays, java.io.OutputStream, java.util.jar.JarFile, hudson.model.Hudson, org.apache.tools.ant.types.Resource, org.apache.tools.ant.types.resources.MappedResourceCollection...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Executor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.885 IQR)
- **Top Global Matches:** file_cluster_13: 11.885, file_cluster_0: 12.104, file_cluster_8: 12.506
- **Magnitude:** 577.26 | **LOC:** 993 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (16.1393%), Tech Debt (99.9969%)
**Top Internal Functions/Classes:**
  * `finish1` (Impact: 128.3)
  * `run` (Impact: 115.0)
    * *Intent:* // worth recording who did it
  * `interrupt` (Impact: 27.4)
  * `resetWorkUnit` (Impact: 23.6)
    * *Intent:* // we abort the build. // but that causes JENKINS-28690 style deadlocks when the correctly written c...
  * `of` (Impact: 19.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 139`, `args: 34`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 28`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `api: 47`, `concurrency: 4`, `import: 57`
* *Defense:* `safety: 60`, `doc: 45`, `sync_locks: 59`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.483
  * `Choke Point (Betweenness):` 0.000131 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` jenkins.model.CauseOfInterruption.UserInterruption, jenkins.model.queue.AsynchronousExecution, java.util.logging.Level.WARNING, hudson.security.ACLContext, java.util.concurrent.TimeUnit, jenkins.model.IExecutor, java.util.Arrays, org.kohsuke.stapler.HttpResponse...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `core/src/main/java/hudson/Proc.java` (JAVA) | Magnitude: 258.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 93, branch: 49, io: 45
- `core/src/main/java/hudson/model/queue/AbstractSubTask.java` (JAVA) | Magnitude: 13.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 2, class_start: 1, api: 1
- `core/src/main/java/org/acegisecurity/userdetails/UserDetails.java` (JAVA) | Magnitude: 29.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 24, args: 14, func_start: 14
- `core/src/main/java/hudson/model/PermalinkProjectAction.java` (JAVA) | Magnitude: 62.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, doc: 23, api: 16, structural_boundaries: 13
- `test/src/test/java/jenkins/security/stapler/StaplerRoutableFieldTest.java` (JAVA) | Magnitude: 53.98 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 108, func_start: 45, test: 45, structural_boundaries: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `war/src/main/webapp/WEB-INF/hudson` (SHELL) | Magnitude: 44.84 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 27, branch: 12, structural_boundaries: 9, indent_spaces: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/src/test/java/hudson/model/ParametersAction2Test.java` (JAVA) | Magnitude: 139.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 285, structural_boundaries: 181, test: 63, state_mutation: 28
- `test/src/test/java/hudson/tasks/ArtifactArchiverTest.java` (JAVA) | Magnitude: 340.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 443, structural_boundaries: 163, test: 101, func_start: 53
- `test/src/test/java/org/kohsuke/stapler/beanutils/BeanUtilsTagLibrary.java` (JAVA) | Magnitude: 10.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 12, func_start: 5, import: 5
- `core/src/main/java/hudson/model/ResultTrend.java` (JAVA) | Magnitude: 11.86 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, doc: 11, structural_boundaries: 7, branch: 6
- `core/src/main/java/jenkins/model/details/DurationDetail.java` (JAVA) | Magnitude: 6.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, branch: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `core/src/test/java/jenkins/org/apache/commons/validator/routines/InetAddressValidatorTest.java` (JAVA) | Magnitude: 2568.08 | Delta: **0.3 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1266, args: 263, closures: 254, indent_spaces: 232

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `core/src/main/java/hudson/model/ItemGroup.java` (JAVA) | Magnitude: 52.36 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 37, doc: 33, generics: 23
- `core/src/main/java/hudson/util/TagCloud.java` (JAVA) | Magnitude: 34.3 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 15, api: 12, args: 7
- `core/src/main/java/jenkins/model/RunAction2.java` (JAVA) | Magnitude: 91.24 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, branch: 4, doc: 4, args: 2
- `core/src/main/java/jenkins/util/InterceptingExecutorService.java` (JAVA) | Magnitude: 103.68 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 39, generics: 25, args: 19
- `core/src/main/java/jenkins/model/details/KeptForeverDetail.java` (JAVA) | Magnitude: 11.14 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, branch: 8, structural_boundaries: 7, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `war/src/main/webapp/scripts/behavior.js` (JAVASCRIPT) | Magnitude: 119.16 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 111, state_mutation: 36, branch: 26, args: 17
- `core/src/main/resources/lib/form/repeatable/repeatable.js` (JAVASCRIPT) | Magnitude: 2.91 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, state_mutation: 106, branch: 28, structural_boundaries: 23
- `core/src/main/resources/lib/form/select/select.js` (JAVASCRIPT) | Magnitude: 2.5 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 86, state_mutation: 30, branch: 24, structural_boundaries: 14
- `src/main/js/add-item.js` (JAVASCRIPT) | Magnitude: 275.94 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 216, state_mutation: 60, structural_boundaries: 55, func_start: 46
- `core/src/main/resources/lib/hudson/newFromList/validation.js` (JAVASCRIPT) | Magnitude: 1.12 | Delta: **0.175 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 42, state_mutation: 14, structural_boundaries: 10, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `core/src/main/resources/hudson/model/LoadStatistics/resources.js` (JAVASCRIPT) | Magnitude: 15.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, immutability_locks: 13, globals: 5, ui_framework: 4
- `core/src/main/resources/hudson/model/DirectoryBrowserSupport/pattern.js` (JAVASCRIPT) | Magnitude: 25.32 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 10, structural_boundaries: 4, globals: 3
- `core/src/main/resources/lib/hudson/editable-description.js` (JAVASCRIPT) | Magnitude: 0.1 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, ui_framework: 6, globals: 6, args: 5
- `src/main/js/util/i18n.js` (JAVASCRIPT) | Magnitude: 2.98 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, args: 1, func_start: 1
- `core/src/main/resources/lib/layout/progressiveRendering/progressiveRendering.js` (JAVASCRIPT) | Magnitude: 0.87 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, func_start: 9, args: 7, globals: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `core/src/main/java/jenkins/util/URLClassLoader2.java` (JAVA) | Magnitude: 58.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 19, concurrency: 18, doc: 17
- `core/src/main/java/hudson/util/ConsistentHash.java` (JAVA) | Magnitude: 213.9 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 56, concurrency: 43, func_start: 41
- `core/src/test/java/jenkins/model/lazy/AbstractLazyLoadRunMapTest.java` (JAVA) | Magnitude: 155.52 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 74, test: 57, concurrency: 56
- `test/src/test/java/hudson/model/HelpLinkTest.java` (JAVA) | Magnitude: 33.0 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, import: 19, indent_spaces: 18, concurrency: 13
- `core/src/test/java/hudson/util/AtomicFileWriterTest.java` (JAVA) | Magnitude: 94.94 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 66, concurrency: 42, io: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `core/src/main/java/hudson/scheduler/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, doc: 1, planned_debt: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/main/js/components/dropdowns/types.js` (JAVASCRIPT) | Magnitude: 10.52 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: doc: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `test/src/test/java/hudson/model/FileParameterValueTest.java` (JAVA) | Magnitude: 94.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 290, structural_boundaries: 132, io: 63, test: 58
- `test/src/test/java/hudson/model/UpdateCenterMigrationTest.java` (JAVA) | Magnitude: 37.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 29, args: 13, import: 11
- `core/src/main/java/hudson/AbortException.java` (JAVA) | Magnitude: 7.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, func_start: 3, api: 3
- `test/src/test/java/hudson/util/SecretCompatTest.java` (JAVA) | Magnitude: 12.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 34, import: 18, test: 13
- `core/src/test/java/hudson/triggers/SCMTriggerTest.java` (JAVA) | Magnitude: 1.36 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, decorators: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `core/src/main/java/jenkins/util/io/OnMaster.java` (JAVA) | Magnitude: 12.56 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 11, structural_boundaries: 2, doc: 2, class_start: 1
- `core/src/main/java/jenkins/model/lazy/Boundary.java` (JAVA) | Magnitude: 8.04 | Delta: **0.46 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 4, func_start: 3, args: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ath.sh` -> Churn: **67.71%** | Cog Load: 94.4594% | Debt: 99.9999%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/src/main/java/hudson/model/UpdateCenter.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 843.68
- `core/src/main/java/hudson/model/Fingerprint.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 829.28
- `core/src/main/java/hudson/model/View.java` -> **Jan Faracik** (100.0% isolated ownership) | Magnitude: 743.58
- `core/src/main/java/hudson/util/ProcessTree.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 670.96
- `core/src/main/java/hudson/ClassicPluginStrategy.java` -> **Dmitriy Ukhlov** (100.0% isolated ownership) | Magnitude: 590.18

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/src/main/java/jenkins/model/Jenkins.java` -> **Severity: 0.165** (Bridge: 0.0024 * Flux: 68.3795%)
- `core/src/main/java/hudson/model/Job.java` -> **Severity: 0.029** (Bridge: 0.0004 * Flux: 70.7564%)
- `core/src/main/java/hudson/model/Computer.java` -> **Severity: 0.025** (Bridge: 0.0004 * Flux: 69.6561%)
- `core/src/main/java/hudson/model/Run.java` -> **Severity: 0.017** (Bridge: 0.0004 * Flux: 38.8041%)
- `core/src/main/java/hudson/Functions.java` -> **Severity: 0.016** (Bridge: 0.0005 * Flux: 34.5117%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/src/main/java/jenkins/YesNoMaybe.java` -> **Severity: 409.478** (Blast Radius: 9.666 * Doc Risk: 42.3627%)
- `core/src/main/java/jenkins/model/Jenkins.java` -> **Severity: 374.84** (Blast Radius: 14.768 * Doc Risk: 25.3819%)
- `core/src/main/java/org/acegisecurity/Authentication.java` -> **Severity: 252.326** (Blast Radius: 3.117 * Doc Risk: 80.9517%)
- `core/src/main/java/hudson/Functions.java` -> **Severity: 187.429** (Blast Radius: 5.221 * Doc Risk: 35.8991%)
- `core/src/main/java/org/acegisecurity/userdetails/UsernameNotFoundException.java` -> **Severity: 156.578** (Blast Radius: 1.85 * Doc Risk: 84.6367%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
