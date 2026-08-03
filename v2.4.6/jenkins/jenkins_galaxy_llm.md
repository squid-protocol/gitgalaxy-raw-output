# ARCHITECTURAL_BRIEF: jenkins
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/jenkins` |
| **Timestamp** | `2026-08-03T20:59:21.743059+00:00` |
| **Scan Duration** | `16.99s` |
| **Git Branch** | `master` |
| **Git Commit** | `bc6a2222ce5a9e104a4f5a96653f0e879461936b` |
| **Git Remote** | `https://github.com/jenkinsci/jenkins` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2103 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
> **Architectural Drift Z-Score:** `2.549`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2766 | 23.1% |
| file_cluster_13 | 1464 | 12.2% |
| file_cluster_0 | 127 | 1.1% |
| file_cluster_4 | 39 | 0.3% |
| file_cluster_16 | 24 | 0.2% |
| file_cluster_2 | 15 | 0.1% |
| file_cluster_17 | 9 | 0.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 9.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.1 | 19.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.9 | 0.2 | 0.0 |
| API Exposure | 0.0 | 17.3 | 2.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 62.3 | 86.7 | 100.0 |
| Instability Exposure | 0.0 | 4.8 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 31.7 | 6.7 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 28.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 72.9 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 18.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `executeReactor` (@ `core/src/main/java/jenkins/model/Jenkins.java`) -> Impact: **3300.6** | LOC: 1510
- `testIPv6` (@ `core/src/test/java/jenkins/org/apache/commons/validator/routines/InetAddressValidatorTest.java`) -> Impact: **2972.1** | LOC: 154
- `isUnix` (@ `core/src/main/java/hudson/FilePath.java`) -> Impact: **2579.3** | LOC: 1391
  * *Intent:* /** * When this {@link FilePath} represents the remote path, * this field is always non-null on the controller (the field represents * the channel to ...
- `clear` (@ `core/src/main/java/hudson/model/Queue.java`) -> Impact: **1823.5** | LOC: 630
- `load` (@ `core/src/main/java/hudson/model/UpdateCenter.java`) -> Impact: **1641.8** | LOC: 592
- `isOptional` (@ `core/src/main/java/hudson/ExtensionFinder.java`) -> Impact: **1611.8** | LOC: 344
  * *Intent:* /** * Rebuilds the internal index, if any, so that future {@link #find(Class, Hudson)} calls * will discover components newly added to {@link PluginMa...
- `printThrowable` (@ `core/src/test/java/hudson/FunctionsTest.java`) -> Impact: **1217.6** | LOC: 224
- `getProperties` (@ `core/src/main/java/hudson/model/View.java`) -> Impact: **1159.3** | LOC: 507
  * *Intent:* /**
- `delayedCheck` (@ `war/src/main/webapp/scripts/hudson-behavior.js`) -> Impact: **985.6** | LOC: 513
- `HudsonPrivateSecurityRealm` (@ `core/src/main/java/hudson/security/HudsonPrivateSecurityRealm.java`) -> Impact: **923.0** | LOC: 540

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `println` (@ `core/move-l10n.groovy`) -> **O(2^N) [Recursive]**
- `set` (@ `core/src/main/resources/hudson/security/GlobalSecurityConfiguration/index.groovy`) -> **O(2^N) [Recursive]**
- `div` (@ `core/src/main/resources/jenkins/management/AdministrativeMonitorsConfiguration/config.groovy`) -> **O(2^N) [Recursive]**
  * *Intent:* /* * The MIT License * * Copyright (c) 2016, CloudBees, Inc. * * Permission is hereby granted, free of charge, to any person obtaining a copy * of thi...
- `option` (@ `test/src/test/resources/lib/form/OptionTest/UsingGroovyView/index.groovy`) -> **O(2^N) [Recursive]**
- `start` (@ `cli/src/main/java/hudson/cli/CLI.java`) -> **O(2^N) [Recursive]**
- `load` (@ `core/src/main/java/hudson/ClassicPluginStrategy.java`) -> **O(2^N) [Recursive]**
- `isOptional` (@ `core/src/main/java/hudson/ExtensionFinder.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Rebuilds the internal index, if any, so that future {@link #find(Class, Hudson)} calls * will discover components newly added to {@link PluginMa...
- `isUnix` (@ `core/src/main/java/hudson/FilePath.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * When this {@link FilePath} represents the remote path, * this field is always non-null on the controller (the field represents * the channel to ...
- `join` (@ `core/src/main/java/hudson/Launcher.java`) -> **O(2^N) [Recursive]**
- `envs` (@ `core/src/main/java/hudson/Launcher.java`) -> **O(2^N) [Recursive]**
  * *Intent:* * * <p> * This hides the difference between running programs locally vs remotely. * * * <h2>'env' parameter</h2> * <p> * To allow important environmen...

### Highest Data Gravity (Database Complexity)
- `onload` (@ `test/src/test/resources/hudson/model/hudson.tools.JDKInstaller.json.html`) -> DB Complexity: **551**
- `isUnix` (@ `core/src/main/java/hudson/FilePath.java`) -> DB Complexity: **364**
  * *Intent:* /** * When this {@link FilePath} represents the remote path, * this field is always non-null on the controller (the field represents * the channel to ...
- `doubleDots` (@ `test/src/test/java/hudson/model/DirectoryBrowserSupportTest.java`) -> DB Complexity: **226**
- `executeReactor` (@ `core/src/main/java/jenkins/model/Jenkins.java`) -> DB Complexity: **112**
- `onload` (@ `test/src/test/resources/hudson/model/hudson.tasks.Maven.MavenInstaller.json.html`) -> DB Complexity: **89**
- `createPluginSetupWizard` (@ `src/main/js/pluginSetupWizardGui.js`) -> DB Complexity: **81**
- `exports` (@ `webpack.config.js`) -> DB Complexity: **78**
- `testIsDescendant` (@ `core/src/test/java/hudson/UtilTest.java`) -> DB Complexity: **75**
  * *Intent:* // Malformed input is replaced without throwing an exception
- `load` (@ `core/src/main/java/hudson/model/UpdateCenter.java`) -> DB Complexity: **73**
- `createPluginWrapper` (@ `core/src/main/java/hudson/ClassicPluginStrategy.java`) -> DB Complexity: **58**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `core/src/main/java/hudson/model` | 170 | 41146.38 | 10.37% | 58.42% |
| `core/src/main/java/hudson` | 50 | 17668.74 | 10.77% | 44.63% |
| `core/src/main/java/hudson/util` | 122 | 16940.8 | 12.96% | 60.43% |
| `core/src/main/java/jenkins/model` | 69 | 10957.52 | 8.91% | 47.81% |
| `test/src/test/java/hudson/model` | 84 | 10767.9 | 14.36% | 0.0% |
| `test/src/test/java/hudson/cli` | 48 | 5597.84 | 16.0% | 0.0% |
| `core/src/main/java/jenkins/security` | 52 | 5539.6 | 8.77% | 40.43% |
| `core/src/main/java/hudson/security` | 45 | 5302.04 | 9.07% | 52.28% |
| `core/src/main/java/hudson/slaves` | 33 | 5122.34 | 10.24% | 68.28% |
| `core/src/main/java/jenkins/util` | 38 | 4847.6 | 15.7% | 47.23% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `core/src/main/resources/hudson/tasks/ArtifactArchiver/help-defaultExcludes.groovy` -> **100.0%** Exposure
- `core/src/main/resources/hudson/tasks/Fingerprinter/help-defaultExcludes.groovy` -> **100.0%** Exposure
- `licenseCompleter.groovy` -> **100.0%** Exposure
- `war/src/main/webapp/WEB-INF/hudson` -> **100.0%** Exposure
- `cli/src/main/java/hudson/cli/CLIConnectionFactory.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `war/src/main/webapp/WEB-INF/hudson` -> **100.0%** Exposure
- `core/src/main/java/hudson/logging/WeakLogHandler.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/search/SearchIndexBuilder.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/ArgumentListBuilder.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/util/ClasspathBuilder.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `core/src/main/java/hudson/util/TimeUnit2.java` -> **2** Orphaned Functions | **79** Duplicates
- `test/src/test/java/jenkins/security/stapler/GetterMethodFilterTest.java` -> **79** Orphaned Functions | **0** Duplicates
- `core/src/test/java/jenkins/util/VirtualFileTest.java` -> **49** Orphaned Functions | **4** Duplicates
- `core/src/main/java/hudson/util/IOUtils.java` -> **0** Orphaned Functions | **50** Duplicates
- `test/src/test/java/hudson/model/ViewTest.java` -> **42** Orphaned Functions | **6** Duplicates

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
25. **`Jenkinsfile`** -> AI Confidence: **99.29%**
26. **`core/src/main/resources/hudson/tasks/Shell/config.groovy`** -> AI Confidence: **99.29%**
27. **`core/src/main/resources/jenkins/management/AdministrativeMonitorsConfiguration/config.groovy`** -> AI Confidence: **99.29%**
28. **`core/src/main/resources/jenkins/management/ShutdownLink/index.groovy`** -> AI Confidence: **99.29%**
29. **`core/src/main/resources/jenkins/model/ArtifactManagerConfiguration/config.groovy`** -> AI Confidence: **99.29%**
30. **`core/src/main/resources/jenkins/security/UpdateSiteWarningsMonitor/message.groovy`** -> AI Confidence: **99.29%**
31. **`core/src/main/resources/lib/form/serverTcpPort.groovy`** -> AI Confidence: **99.29%**
32. **`licenseCompleter.groovy`** -> AI Confidence: **99.29%**
33. **`test/src/test/resources/lib/form/OptionTest/UsingGroovyView/index.groovy`** -> AI Confidence: **99.29%**
34. **`core/src/test/java/hudson/console/UrlAnnotatorTest.java`** -> AI Confidence: **99.29%**
35. **`core/src/test/java/jenkins/org/apache/commons/validator/routines/InetAddressValidatorTest.java`** -> AI Confidence: **99.29%**
36. **`core/src/test/java/jenkins/util/UrlHelperTest.java`** -> AI Confidence: **99.29%**
37. **`core/report-l10n.rb`** -> AI Confidence: **99.29%**
38. **`core/src/main/resources/hudson/PluginManager/_updateSite.js`** -> AI Confidence: **99.29%**
39. **`core/src/main/resources/lib/layout/progressiveRendering/progressiveRendering.js`** -> AI Confidence: **99.29%**
40. **`src/main/js/components/header/actions-touch.js`** -> AI Confidence: **99.29%**
41. **`war/src/main/webapp/scripts/loading.js`** -> AI Confidence: **99.29%**
42. **`cli/src/main/java/hudson/cli/CLI.java`** -> AI Confidence: **99.24%**
43. **`core/src/main/java/hudson/ClassicPluginStrategy.java`** -> AI Confidence: **99.24%**
44. **`core/src/main/java/hudson/DependencyRunner.java`** -> AI Confidence: **99.24%**
45. **`core/src/main/java/hudson/ExtensionFinder.java`** -> AI Confidence: **99.24%**
46. **`core/src/main/java/hudson/TcpSlaveAgentListener.java`** -> AI Confidence: **99.24%**
47. **`core/src/main/java/hudson/cli/BuildCommand.java`** -> AI Confidence: **99.24%**
48. **`core/src/main/java/hudson/cli/ConsoleCommand.java`** -> AI Confidence: **99.24%**
49. **`core/src/main/java/hudson/cli/InstallPluginCommand.java`** -> AI Confidence: **99.24%**
50. **`core/src/main/java/hudson/cli/OfflineNodeCommand.java`** -> AI Confidence: **99.24%**
51. **`core/src/main/java/hudson/cli/ReloadJobCommand.java`** -> AI Confidence: **99.24%**
52. **`core/src/main/java/hudson/diagnosis/NullIdDescriptorMonitor.java`** -> AI Confidence: **99.24%**
53. **`core/src/main/java/hudson/model/AbstractBuild.java`** -> AI Confidence: **99.24%**
54. **`core/src/main/java/hudson/model/Actionable.java`** -> AI Confidence: **99.24%**
55. **`core/src/main/java/hudson/model/AsyncAperiodicWork.java`** -> AI Confidence: **99.24%**
56. **`core/src/main/java/hudson/model/AsyncPeriodicWork.java`** -> AI Confidence: **99.24%**
57. **`core/src/main/java/hudson/model/Fingerprint.java`** -> AI Confidence: **99.24%**
58. **`core/src/main/java/hudson/model/HealthReport.java`** -> AI Confidence: **99.24%**
59. **`core/src/main/java/hudson/model/queue/MappingWorksheet.java`** -> AI Confidence: **99.24%**
60. **`core/src/main/java/hudson/model/queue/WorkUnitContext.java`** -> AI Confidence: **99.24%**
61. **`core/src/main/java/hudson/scheduler/CronTab.java`** -> AI Confidence: **99.24%**
62. **`core/src/main/java/hudson/scm/ChangeLogSet.java`** -> AI Confidence: **99.24%**
63. **`core/src/main/java/hudson/security/ChainedServletFilter.java`** -> AI Confidence: **99.24%**
64. **`core/src/main/java/hudson/security/ChainedServletFilter2.java`** -> AI Confidence: **99.24%**
65. **`core/src/main/java/hudson/slaves/NodeProvisioner.java`** -> AI Confidence: **99.24%**
66. **`core/src/main/java/hudson/slaves/RetentionStrategy.java`** -> AI Confidence: **99.24%**
67. **`core/src/main/java/hudson/tasks/BuildStepCompatibilityLayer.java`** -> AI Confidence: **99.24%**
68. **`core/src/main/java/hudson/tasks/BuildStepDescriptor.java`** -> AI Confidence: **99.24%**
69. **`core/src/main/java/hudson/tasks/BuildWrappers.java`** -> AI Confidence: **99.24%**
70. **`core/src/main/java/hudson/tasks/LogRotator.java`** -> AI Confidence: **99.24%**
71. **`core/src/main/java/hudson/util/ProcessTree.java`** -> AI Confidence: **99.24%**
72. **`core/src/main/java/hudson/util/Retrier.java`** -> AI Confidence: **99.24%**
73. **`core/src/main/java/hudson/util/RobustReflectionConverter.java`** -> AI Confidence: **99.24%**
74. **`core/src/main/java/jenkins/ClassLoaderReflectionToolkit.java`** -> AI Confidence: **99.24%**
75. **`core/src/main/java/jenkins/cli/StopBuildsCommand.java`** -> AI Confidence: **99.24%**
76. **`core/src/main/java/jenkins/model/identity/InstanceIdentityProvider.java`** -> AI Confidence: **99.24%**
77. **`core/src/main/java/jenkins/security/ClassFilterImpl.java`** -> AI Confidence: **99.24%**
78. **`core/src/main/java/jenkins/security/RedactSecretJsonInErrorMessageSanitizer.java`** -> AI Confidence: **99.24%**
79. **`core/src/main/java/jenkins/security/SecurityListener.java`** -> AI Confidence: **99.24%**
80. **`core/src/main/java/jenkins/security/csp/AvatarContributor.java`** -> AI Confidence: **99.24%**
81. **`core/src/main/java/jenkins/security/stapler/DoActionFilter.java`** -> AI Confidence: **99.24%**
82. **`core/src/main/java/jenkins/security/stapler/StaplerDispatchValidator.java`** -> AI Confidence: **99.24%**
83. **`core/src/main/java/jenkins/security/stapler/TypedFilter.java`** -> AI Confidence: **99.24%**
84. **`core/src/main/java/jenkins/telemetry/impl/ContentSecurityPolicy.java`** -> AI Confidence: **99.24%**
85. **`core/src/main/java/jenkins/util/FullDuplexHttpService.java`** -> AI Confidence: **99.24%**
86. **`core/src/main/java/jenkins/util/JSONSignatureValidator.java`** -> AI Confidence: **99.24%**
87. **`core/src/main/java/jenkins/util/Listeners.java`** -> AI Confidence: **99.24%**
88. **`core/src/main/java/jenkins/widgets/BuildTimeTrend.java`** -> AI Confidence: **99.24%**
89. **`core/src/main/java/org/acegisecurity/GrantedAuthority.java`** -> AI Confidence: **99.24%**
90. **`core/src/test/java/jenkins/security/apitoken/ApiTokenStatsTest.java`** -> AI Confidence: **99.24%**
91. **`test/src/test/java/hudson/model/queue/BuildKeepsRunningWhenFaultySubTasksTest.java`** -> AI Confidence: **99.24%**
92. **`test/src/test/java/jenkins/security/LastGrantedAuthoritiesPropertyTest.java`** -> AI Confidence: **99.24%**
93. **`war/src/main/java/executable/Main.java`** -> AI Confidence: **99.24%**
94. **`src/main/js/components/command-palette/index.js`** -> AI Confidence: **99.24%**
95. **`src/main/js/pluginSetupWizardGui.js`** -> AI Confidence: **99.24%**
96. **`core/src/main/resources/hudson/security/GlobalSecurityConfiguration/index.groovy`** -> AI Confidence: **99.23%**
97. **`core/src/main/java/hudson/cli/ListPluginsCommand.java`** -> AI Confidence: **99.23%**
98. **`core/src/main/java/hudson/console/ConsoleAnnotator.java`** -> AI Confidence: **99.23%**
99. **`core/src/main/java/hudson/model/RunParameterValue.java`** -> AI Confidence: **99.23%**
100. **`core/src/main/java/hudson/model/ViewGroupMixIn.java`** -> AI Confidence: **99.23%**
101. **`core/src/main/java/hudson/search/ParsedQuickSilver.java`** -> AI Confidence: **99.23%**
102. **`core/src/main/java/hudson/security/AccessDeniedException3.java`** -> AI Confidence: **99.23%**
103. **`cli/src/main/java/hudson/cli/FullDuplexHttpStream.java`** -> AI Confidence: **99.18%**
104. **`cli/src/main/java/hudson/cli/PlainCLIProtocol.java`** -> AI Confidence: **99.18%**
105. **`cli/src/main/java/hudson/cli/PrivateKeyProvider.java`** -> AI Confidence: **99.18%**
106. **`cli/src/main/java/hudson/cli/SSHCLI.java`** -> AI Confidence: **99.18%**
107. **`core/src/main/java/hudson/ExtensionList.java`** -> AI Confidence: **99.18%**
108. **`core/src/main/java/hudson/LocalPluginManager.java`** -> AI Confidence: **99.18%**
109. **`core/src/main/java/hudson/WebAppMain.java`** -> AI Confidence: **99.18%**
110. **`core/src/main/java/hudson/cli/CLIAction.java`** -> AI Confidence: **99.18%**
111. **`core/src/main/java/hudson/cli/CopyJobCommand.java`** -> AI Confidence: **99.18%**
112. **`core/src/main/java/hudson/cli/HelpCommand.java`** -> AI Confidence: **99.18%**
113. **`core/src/main/java/hudson/cli/SetBuildDescriptionCommand.java`** -> AI Confidence: **99.18%**
114. **`core/src/main/java/hudson/cli/declarative/MethodBinder.java`** -> AI Confidence: **99.18%**
115. **`core/src/main/java/hudson/cli/handlers/GenericItemOptionHandler.java`** -> AI Confidence: **99.18%**
116. **`core/src/main/java/hudson/console/ConsoleAnnotationOutputStream.java`** -> AI Confidence: **99.18%**
117. **`core/src/main/java/hudson/console/ConsoleNote.java`** -> AI Confidence: **99.18%**
118. **`core/src/main/java/hudson/console/HyperlinkNote.java`** -> AI Confidence: **99.18%**
119. **`core/src/main/java/hudson/console/PlainTextConsoleOutputStream.java`** -> AI Confidence: **99.18%**
120. **`core/src/main/java/hudson/init/InitStrategy.java`** -> AI Confidence: **99.18%**
121. **`core/src/main/java/hudson/init/impl/InstallUncaughtExceptionHandler.java`** -> AI Confidence: **99.18%**
122. **`core/src/main/java/hudson/lifecycle/UnixLifecycle.java`** -> AI Confidence: **99.18%**
123. **`core/src/main/java/hudson/logging/LogRecorder.java`** -> AI Confidence: **99.18%**
124. **`core/src/main/java/hudson/logging/WeakLogHandler.java`** -> AI Confidence: **99.18%**
125. **`core/src/main/java/hudson/model/AbstractItem.java`** -> AI Confidence: **99.18%**
126. **`core/src/main/java/hudson/model/AbstractModelObject.java`** -> AI Confidence: **99.18%**
127. **`core/src/main/java/hudson/model/BuildAuthorizationToken.java`** -> AI Confidence: **99.18%**
128. **`core/src/main/java/hudson/model/BuildTimelineWidget.java`** -> AI Confidence: **99.18%**
129. **`core/src/main/java/hudson/model/ChoiceParameterDefinition.java`** -> AI Confidence: **99.18%**
130. **`core/src/main/java/hudson/model/ComputerPinger.java`** -> AI Confidence: **99.18%**
131. **`core/src/main/java/hudson/model/FileParameterDefinition.java`** -> AI Confidence: **99.18%**
132. **`core/src/main/java/hudson/model/FileParameterValue.java`** -> AI Confidence: **99.18%**
133. **`core/src/main/java/hudson/model/ItemGroup.java`** -> AI Confidence: **99.18%**
134. **`core/src/main/java/hudson/model/Label.java`** -> AI Confidence: **99.18%**
135. **`core/src/main/java/hudson/model/LoadStatistics.java`** -> AI Confidence: **99.18%**
136. **`core/src/main/java/hudson/model/ModifiableItemGroup.java`** -> AI Confidence: **99.18%**
137. **`core/src/main/java/hudson/model/MultiStageTimeSeries.java`** -> AI Confidence: **99.18%**
138. **`core/src/main/java/hudson/model/Project.java`** -> AI Confidence: **99.18%**
139. **`core/src/main/java/hudson/model/Result.java`** -> AI Confidence: **99.18%**
140. **`core/src/main/java/hudson/model/RunMap.java`** -> AI Confidence: **99.18%**
141. **`core/src/main/java/hudson/model/Slave.java`** -> AI Confidence: **99.18%**
142. **`core/src/main/java/hudson/model/StringParameterDefinition.java`** -> AI Confidence: **99.18%**
143. **`core/src/main/java/hudson/model/TaskListener.java`** -> AI Confidence: **99.18%**
144. **`core/src/main/java/hudson/model/UserIdMapper.java`** -> AI Confidence: **99.18%**
145. **`core/src/main/java/hudson/model/View.java`** -> AI Confidence: **99.18%**
146. **`core/src/main/java/hudson/model/ViewJob.java`** -> AI Confidence: **99.18%**
147. **`core/src/main/java/hudson/model/labels/LabelExpression.java`** -> AI Confidence: **99.18%**
148. **`core/src/main/java/hudson/model/listeners/ItemListener.java`** -> AI Confidence: **99.18%**
149. **`core/src/main/java/hudson/model/listeners/SCMListener.java`** -> AI Confidence: **99.18%**
150. **`core/src/main/java/hudson/model/queue/QueueSorter.java`** -> AI Confidence: **99.18%**
151. **`core/src/main/java/hudson/model/userproperty/UserPropertyCategoryAction.java`** -> AI Confidence: **99.18%**
152. **`core/src/main/java/hudson/node_monitors/ResponseTimeMonitor.java`** -> AI Confidence: **99.18%**
153. **`core/src/main/java/hudson/node_monitors/TemporarySpaceMonitor.java`** -> AI Confidence: **99.18%**
154. **`core/src/main/java/hudson/scm/NullSCM.java`** -> AI Confidence: **99.18%**
155. **`core/src/main/java/hudson/scm/SCMDescriptor.java`** -> AI Confidence: **99.18%**
156. **`core/src/main/java/hudson/security/AbstractPasswordBasedSecurityRealm.java`** -> AI Confidence: **99.18%**
157. **`core/src/main/java/hudson/security/FederatedLoginService.java`** -> AI Confidence: **99.18%**
158. **`core/src/main/java/hudson/security/HudsonFilter.java`** -> AI Confidence: **99.18%**
159. **`core/src/main/java/hudson/security/HudsonPrivateSecurityRealm.java`** -> AI Confidence: **99.18%**
160. **`core/src/main/java/hudson/security/PermissionGroup.java`** -> AI Confidence: **99.18%**
161. **`core/src/main/java/hudson/security/SecurityRealm.java`** -> AI Confidence: **99.18%**
162. **`core/src/main/java/hudson/security/SidACL.java`** -> AI Confidence: **99.18%**
163. **`core/src/main/java/hudson/security/UnwrapSecurityExceptionFilter.java`** -> AI Confidence: **99.18%**
164. **`core/src/main/java/hudson/slaves/CloudRetentionStrategy.java`** -> AI Confidence: **99.18%**
165. **`core/src/main/java/hudson/slaves/CloudSlaveRetentionStrategy.java`** -> AI Confidence: **99.18%**
166. **`core/src/main/java/hudson/slaves/ConnectionActivityMonitor.java`** -> AI Confidence: **99.18%**
167. **`core/src/main/java/hudson/slaves/DelegatingComputerLauncher.java`** -> AI Confidence: **99.18%**
168. **`core/src/main/java/hudson/slaves/WorkspaceList.java`** -> AI Confidence: **99.18%**
169. **`core/src/main/java/hudson/tasks/BuildTrigger.java`** -> AI Confidence: **99.18%**
170. **`core/src/main/java/hudson/tasks/Shell.java`** -> AI Confidence: **99.18%**
171. **`core/src/main/java/hudson/tools/AbstractCommandInstaller.java`** -> AI Confidence: **99.18%**
172. **`core/src/main/java/hudson/tools/DownloadFromUrlInstaller.java`** -> AI Confidence: **99.18%**
173. **`core/src/main/java/hudson/tools/ToolLocationNodeProperty.java`** -> AI Confidence: **99.18%**
174. **`core/src/main/java/hudson/tools/ZipExtractionInstaller.java`** -> AI Confidence: **99.18%**
175. **`core/src/main/java/hudson/triggers/SafeTimerTask.java`** -> AI Confidence: **99.18%**
176. **`core/src/main/java/hudson/triggers/TimerTrigger.java`** -> AI Confidence: **99.18%**
177. **`core/src/main/java/hudson/util/BootFailure.java`** -> AI Confidence: **99.18%**
178. **`core/src/main/java/hudson/util/CharacterEncodingFilter.java`** -> AI Confidence: **99.18%**
179. **`core/src/main/java/hudson/util/CompressedFile.java`** -> AI Confidence: **99.18%**
180. **`core/src/main/java/hudson/util/DirScanner.java`** -> AI Confidence: **99.18%**
181. **`core/src/main/java/hudson/util/Graph.java`** -> AI Confidence: **99.18%**
182. **`core/src/main/java/hudson/util/Iterators.java`** -> AI Confidence: **99.18%**
183. **`core/src/main/java/hudson/util/Protector.java`** -> AI Confidence: **99.18%**
184. **`core/src/main/java/hudson/util/ReflectionUtils.java`** -> AI Confidence: **99.18%**
185. **`core/src/main/java/hudson/util/RobustCollectionConverter.java`** -> AI Confidence: **99.18%**
186. **`core/src/main/java/hudson/util/RunList.java`** -> AI Confidence: **99.18%**
187. **`core/src/main/java/hudson/util/StreamTaskListener.java`** -> AI Confidence: **99.18%**
188. **`core/src/main/java/hudson/util/XStream2.java`** -> AI Confidence: **99.18%**
189. **`core/src/main/java/hudson/util/io/ReopenableRotatingFileOutputStream.java`** -> AI Confidence: **99.18%**
190. **`core/src/main/java/hudson/util/io/RewindableRotatingFileOutputStream.java`** -> AI Confidence: **99.18%**
191. **`core/src/main/java/hudson/util/xstream/ImmutableListConverter.java`** -> AI Confidence: **99.18%**
192. **`core/src/main/java/hudson/views/ListViewColumn.java`** -> AI Confidence: **99.18%**
193. **`core/src/main/java/hudson/widgets/RenderOnDemandClosure.java`** -> AI Confidence: **99.18%**
194. **`core/src/main/java/jenkins/MetaLocaleDrivenResourceProvider.java`** -> AI Confidence: **99.18%**
195. **`core/src/main/java/jenkins/PluginSubtypeMarker.java`** -> AI Confidence: **99.18%**
196. **`core/src/main/java/jenkins/agents/WebSocketAgents.java`** -> AI Confidence: **99.18%**
197. **`core/src/main/java/jenkins/cli/listeners/DefaultCLIListener.java`** -> AI Confidence: **99.18%**
198. **`core/src/main/java/jenkins/health/HealthCheckAction.java`** -> AI Confidence: **99.18%**
199. **`core/src/main/java/jenkins/management/AdministrativeMonitorsConfiguration.java`** -> AI Confidence: **99.18%**
200. **`core/src/main/java/jenkins/management/AsynchronousAdministrativeMonitor.java`** -> AI Confidence: **99.18%**
201. **`core/src/main/java/jenkins/model/AssetManager.java`** -> AI Confidence: **99.18%**
202. **`core/src/main/java/jenkins/model/BackgroundGlobalBuildDiscarder.java`** -> AI Confidence: **99.18%**
203. **`core/src/main/java/jenkins/model/GlobalBuildDiscarderStrategy.java`** -> AI Confidence: **99.18%**
204. **`core/src/main/java/jenkins/model/GlobalComputerRetentionCheckIntervalConfiguration.java`** -> AI Confidence: **99.18%**
205. **`core/src/main/java/jenkins/model/GlobalQuietPeriodConfiguration.java`** -> AI Confidence: **99.18%**
206. **`core/src/main/java/jenkins/model/IExecutor.java`** -> AI Confidence: **99.18%**
207. **`core/src/main/java/jenkins/model/JenkinsLocationConfiguration.java`** -> AI Confidence: **99.18%**
208. **`core/src/main/java/jenkins/model/SimpleGlobalBuildDiscarderStrategy.java`** -> AI Confidence: **99.18%**
209. **`core/src/main/java/jenkins/model/StandardArtifactManager.java`** -> AI Confidence: **99.18%**
210. **`core/src/main/java/jenkins/model/identity/IdentityRootAction.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `core/src/test/java/hudson/security/HudsonPrivateSecurityRealmTest.java` -> **72.8557%** Exposure
- `core/src/test/java/jenkins/org/apache/commons/validator/routines/DomainValidatorTest.java` -> **33.3724%** Exposure
- `core/src/test/java/jenkins/org/apache/commons/validator/routines/UrlValidatorTest.java` -> **12.3938%** Exposure
### Exploit Generation Surface
- `Jenkinsfile` -> **100.0%** Exposure
- `core/move-l10n.groovy` -> **100.0%** Exposure
- `core/src/main/resources/jenkins/management/AdministrativeMonitorsConfiguration/config.groovy` -> **100.0%** Exposure
- `core/src/main/resources/jenkins/security/UpdateSiteWarningsConfiguration/config.groovy` -> **100.0%** Exposure
- `test/src/test/resources/lib/form/OptionTest/UsingGroovyView/index.groovy` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `core/src/main/java/hudson/Launcher.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/Proc.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/init/impl/InitialUserContent.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/model/AsyncPeriodicWork.java` -> **100.0%** Exposure
- `core/src/main/java/hudson/model/Build.java` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `test/src/test/java/jenkins/install/SetupWizardTest.java` -> **44.4672%** Exposure
### Algorithmic DoS Exposure
- `cli/src/main/java/hudson/cli/CLI.java` -> **100.0%** Exposure
- `cli/src/main/java/hudson/cli/FullDuplexHttpStream.java` -> **100.0%** Exposure
- `cli/src/main/java/hudson/cli/PlainCLIProtocol.java` -> **100.0%** Exposure
- `cli/src/main/java/hudson/cli/PrivateKeyProvider.java` -> **100.0%** Exposure
- `cli/src/main/java/hudson/util/QuotedStringTokenizer.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `50` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `27645` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `core/src/main/java/jenkins/telemetry/impl/UserLanguages.java` (JAVA) -> Cumulative Risk: **963.23**
- **Archetype:** `file_cluster_4` (Distance: 12.119 IQR)
- **Magnitude:** 113.26 | **LOC:** 110 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `handle` (Impact: 24.8), `createContent` (Impact: 16.6), `getId` (Impact: 3.1)

### 2. `core/src/main/java/jenkins/util/InterceptingExecutorService.java` (JAVA) -> Cumulative Risk: **931.4**
- **Archetype:** `file_cluster_16` (Distance: 10.524 IQR)
- **Magnitude:** 220.68 | **LOC:** 113 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `wrap` (Impact: 45.6), `invokeAll` (Impact: 17.1), `invokeAny` (Impact: 17.1)

### 3. `core/src/main/resources/hudson/model/UpdateCenter/update-center.js` (JAVASCRIPT) -> Cumulative Risk: **929.89**
- **Archetype:** `file_cluster_4` (Distance: 11.815 IQR)
- **Magnitude:** 92.76 | **LOC:** 54 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `refresh` (Impact: 53.8)

### 4. `core/src/main/java/hudson/util/PluginServletFilter.java` (JAVA) -> Cumulative Risk: **910.26**
- **Archetype:** `file_cluster_13` (Distance: 12.095 IQR)
- **Magnitude:** 352.58 | **LOC:** 248 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `cleanUp` (Impact: 87.6), `doFilter` (Impact: 36.8), `addFilter` (Impact: 29.7)

### 5. `core/src/main/java/jenkins/model/CoreEnvironmentContributor.java` (JAVA) -> Cumulative Risk: **898.82**
- **Archetype:** `file_cluster_4` (Distance: 12.348 IQR)
- **Magnitude:** 106.24 | **LOC:** 71 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `buildEnvironmentFor` (Impact: 41.4), `buildEnvironmentFor` (Impact: 12.7)

### 6. `core/src/main/java/hudson/util/SequentialExecutionQueue.java` (JAVA) -> Cumulative Risk: **896.77**
- **Archetype:** `file_cluster_4` (Distance: 11.441 IQR)
- **Magnitude:** 202.76 | **LOC:** 137 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run` (Impact: 71.0), `isStarving` (Impact: 24.8), `execute` (Impact: 16.4)

### 7. `core/src/main/java/hudson/scm/SCMDescriptor.java` (JAVA) -> Cumulative Risk: **894.71**
- **Archetype:** `file_cluster_13` (Distance: 11.993 IQR)
- **Magnitude:** 180.48 | **LOC:** 173 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9996%), Algorithmic Dos (99.9969%)
- **Heaviest Functions:** `load` (Impact: 50.6), `isApplicable` (Impact: 27.2), `isApplicable` (Impact: 27.2)

### 8. `src/main/js/components/dialogs/index.js` (JAVASCRIPT) -> Cumulative Risk: **875.5**
- **Archetype:** `file_cluster_4` (Distance: 13.618 IQR)
- **Magnitude:** 473.92 | **LOC:** 360 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `init` (Impact: 81.4), `appendButtons` (Impact: 27.9), `show` (Impact: 27.1)

### 9. `core/src/main/java/hudson/model/Build.java` (JAVA) -> Cumulative Risk: **874.78**
- **Archetype:** `file_cluster_13` (Distance: 11.627 IQR)
- **Magnitude:** 254.3 | **LOC:** 216 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `doRun` (Impact: 121.7), `cleanUp` (Impact: 37.2), `build` (Impact: 31.9)

### 10. `core/src/main/java/jenkins/widgets/RunListProgressiveRendering.java` (JAVA) -> Cumulative Risk: **871.41**
- **Archetype:** `file_cluster_13` (Distance: 10.844 IQR)
- **Magnitude:** 77.06 | **LOC:** 84 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `compute` (Impact: 39.8), `setBuilds` (Impact: 10.5), `data` (Impact: 3.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `core/src/main/java/jenkins/model/Jenkins.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.523 IQR)
- **Top Global Matches:** file_cluster_13: 13.523, file_cluster_0: 13.656, file_cluster_11: 13.921
- **Magnitude:** 4963.56 | **LOC:** 5991 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 112
- **Risk Profile:** Cognitive Load (23.8674%), Tech Debt (22.2416%)
**Top Internal Functions/Classes:**
  * `executeReactor` (Impact: 3300.6 | O(2^N) | DB: 112)
  * `doSafeExit` (Impact: 781.2 | O(N^6) | DB: 32)
  * `restart` (Impact: 85.2 | O(2^N) | DB: 1)
  * `safeRestart` (Impact: 40.0 | O(N^6) | DB: 1)
    * *Intent:* /** * Gets all the active labels in the current system.
  * `doExit` (Impact: 37.7 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 859`, `args: 256`, `func_start: 307`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 149`, `state_mutation: 223`, `dead_code: 8`, `planned_debt: 9`, `fragile_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 22`, `api: 225`, `concurrency: 79`, `import: 317`
* *Defense:* `safety: 129`, `doc: 259`, `sync_locks: 15`, `immutability_locks: 72`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.768
  * `Choke Point (Betweenness):` 0.00242 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 187):` hudson.security.HudsonFilter, jenkins.security.ClassFilterImpl, hudson.model.Fingerprint, hudson.remoting.LocalChannel, hudson.views.ViewsTabBar, org.kohsuke.stapler.WebMethod, io.jenkins.servlet.ServletContextWrapper, io.jenkins.servlet.RequestDispatcherWrapper...
  * `Imported By (In-Degree: 511):` (Excluded from Brief to save tokens)

### `core/src/test/java/jenkins/org/apache/commons/validator/routines/InetAddressValidatorTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_15` (Drift: 11.808 IQR)
- **Top Global Matches:** file_cluster_15: 11.808, file_cluster_8: 12.093, file_cluster_7: 12.525
- **Magnitude:** 3407.08 | **LOC:** 656 | **CtrlFlow:** 98.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (37.0544%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testIPv6` (Impact: 2972.1 | O(N^2))
  * `testVALIDATOR_445` (Impact: 309.5 | O(N^3))
  * `testVALIDATOR_419` (Impact: 65.8 | O(N^2))
  * `testVALIDATOR_335` (Impact: 39.1 | O(N^2))
  * `testInetAddressesByClass` (Impact: 3.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1266`, `structural_boundaries: 26`, `args: 263`, `func_start: 185`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `import: 4`
* *Defense:* `doc: 7`, `test: 185`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.junit.jupiter.api.Test, org.junit.jupiter.api.BeforeEach, org.junit.jupiter.api.Assertions.assertTrue, org.junit.jupiter.api.Assertions.assertFalse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/FilePath.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.245 IQR)
- **Top Global Matches:** file_cluster_13: 12.245, file_cluster_0: 12.452, file_cluster_8: 12.688
- **Magnitude:** 3260.82 | **LOC:** 3937 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 364
- **Risk Profile:** Cognitive Load (13.4242%), Tech Debt (23.3308%)
**Top Internal Functions/Classes:**
  * `isUnix` (Impact: 2579.3 | O(2^N) | DB: 364)
    * *Intent:* /** * When this {@link FilePath} represents the remote path, * this field is always non-null on the ...
  * `normalize` (Impact: 209.2 | O(N^5) | DB: 7)
    * *Intent:* * move the data to the computation. For example, if you are just computing a MD5 * digest of a file,...
  * `invoke` (Impact: 106.4 | O(N^6) | DB: 36)
  * `validatingVisitor` (Impact: 26.7 | O(N^6) | DB: 3)
  * `ignoringSymlinks` (Impact: 15.2 | O(N^4))
    * *Intent:* * @param suffix * The suffix string to be used in generating the file's name; may be * null, in whic...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 578`, `args: 199`, `func_start: 187`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 57`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 147`, `api: 113`, `concurrency: 26`, `import: 118`
* *Defense:* `safety: 87`, `doc: 146`, `sync_locks: 1`, `immutability_locks: 114`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.502
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` hudson.remoting.RemoteOutputStream, org.apache.tools.ant.BuildException, java.io.Serializable, hudson.remoting.LocalChannel, java.util.Objects, org.kohsuke.accmod.restrictions.NoExternalUse, jenkins.util.ContextResettingExecutorService, java.util.concurrent.ExecutorService...
  * `Imported By (In-Degree: 101):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Queue.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.552 IQR)
- **Top Global Matches:** file_cluster_13: 11.552, file_cluster_0: 11.769, file_cluster_11: 12.213
- **Magnitude:** 2124.1 | **LOC:** 3253 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (14.7743%), Tech Debt (23.4615%)
**Top Internal Functions/Classes:**
  * `clear` (Impact: 1823.5 | O(2^N) | DB: 6)
  * `save` (Impact: 66.4 | O(N^4) | DB: 1)
  * `schedule` (Impact: 61.3 | O(N^6))
  * `getNode` (Impact: 8.2 | O(2^N))
    * *Intent:* /** * {@link Task}s that can be built immediately * but blocked because another build is in progress...
  * `Queue` (Impact: 7.1 | O(N^5) | DB: 1)
    * *Intent:* /** * Data structure created for each idle {@link Executor}. * This is a job offer from the queue to...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 282`, `args: 86`, `func_start: 88`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 24`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 66`, `concurrency: 14`, `import: 115`
* *Defense:* `safety: 33`, `doc: 47`, `sync_locks: 24`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.881
  * `Choke Point (Betweenness):` 0.000232 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 51):` org.kohsuke.stapler.HttpResponse, java.util.Objects, org.kohsuke.accmod.restrictions.NoExternalUse, jenkins.model.queue.QueueIdStrategy, com.google.common.cache.Cache, java.util.GregorianCalendar, hudson.util.XStream2, java.util.List...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/Functions.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.273 IQR)
- **Top Global Matches:** file_cluster_13: 12.273, file_cluster_0: 12.679, file_cluster_16: 12.833
- **Magnitude:** 2037.78 | **LOC:** 2743 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.6384%), Tech Debt (99.474%)
**Top Internal Functions/Classes:**
  * `doPrintStackTrace` (Impact: 252.1 | O(2^N) | DB: 1)
    * *Intent:* /** * Finds the given object in the ancestor list and returns its URL. * This is used to determine t...
  * `dumpThreadInfo` (Impact: 166.7 | O(N^6))
    * *Intent:* /** * @deprecated use {@link #getCookie(HttpServletRequest, String)} */
  * `getRelativeNameFrom` (Impact: 109.9 | O(N^5) | DB: 1)
  * `getPageDecorators` (Impact: 97.7 | O(N^4))
  * `htmlAttributeEscape` (Impact: 74.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 407`, `args: 135`, `func_start: 129`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 107`, `state_mutation: 52`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 3`, `api: 173`, `concurrency: 33`, `import: 167`
* *Defense:* `safety: 38`, `doc: 138`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.221
  * `Choke Point (Betweenness):` 0.000451 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 83):` java.io.Serializable, java.util.Date, org.jenkins.ui.icon.Icon, hudson.security.AuthorizationStrategy, java.util.Objects, org.kohsuke.accmod.restrictions.NoExternalUse, hudson.model.ModelObject, hudson.views.ViewsTabBar...
  * `Imported By (In-Degree: 136):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Fingerprint.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.235 IQR)
- **Top Global Matches:** file_cluster_0: 12.235, file_cluster_13: 12.258, file_cluster_4: 12.538
- **Magnitude:** 1975.28 | **LOC:** 1503 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (26.8075%), Tech Debt (99.9985%)
**Top Internal Functions/Classes:**
  * `fromString` (Impact: 174.1 | O(N^6) | DB: 2)
    * *Intent:* /**
  * `canDiscoverItem` (Impact: 130.8 | O(N^6))
  * `add` (Impact: 104.6 | O(2^N) | DB: 4)
    * *Intent:* /** * Set of {@link Range}s. Mutable.
  * `isAlive` (Impact: 101.6 | O(2^N))
  * `removeAll` (Impact: 91.4 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 259`, `args: 92`, `func_start: 101`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 93`, `dead_code: 4`, `planned_debt: 3`, `duplicate_logic: 32`
* *Architecture:* `io: 3`, `api: 111`, `concurrency: 39`, `import: 46`
* *Defense:* `safety: 43`, `doc: 91`, `sync_locks: 19`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.274
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` java.util.logging.Level, java.util.Collections, org.kohsuke.stapler.export.ExportedBean, java.io.IOException, java.util.Date, edu.umd.cs.findbugs.annotations.CheckForNull, hudson.security.ACLContext, com.thoughtworks.xstream.converters.UnmarshallingContext...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/UpdateCenter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.543 IQR)
- **Top Global Matches:** file_cluster_13: 11.543, file_cluster_0: 11.8, file_cluster_4: 12.092
- **Magnitude:** 1941.38 | **LOC:** 2956 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (16.8199%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 1641.8 | O(2^N) | DB: 73)
  * `save` (Impact: 36.2 | O(2^N))
  * `isRestartScheduled` (Impact: 35.6 | O(N^6))
    * *Intent:* /** * Controls update center capability. * * <p> * The main job of this class is to keep track of th...
  * `getBackupVersion` (Impact: 25.7 | O(N^4) | DB: 3)
  * `synchronized` (Impact: 12.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 278`, `args: 73`, `func_start: 91`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 13`, `dead_code: 1`
* *Architecture:* `io: 28`, `api: 88`, `concurrency: 36`, `import: 111`
* *Defense:* `safety: 40`, `doc: 71`, `sync_locks: 9`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` org.kohsuke.stapler.HttpResponse, java.util.Objects, org.kohsuke.accmod.restrictions.NoExternalUse, java.nio.file.AtomicMoveNotSupportedException, java.util.concurrent.ExecutorService, hudson.util.XStream2, java.util.List, hudson.lifecycle.Lifecycle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/test/java/hudson/FunctionsTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.08 IQR)
- **Top Global Matches:** file_cluster_8: 11.08, file_cluster_13: 11.147, file_cluster_0: 11.187
- **Magnitude:** 1883.92 | **LOC:** 800 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (51.363%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `printThrowable` (Impact: 1217.6 | O(N^6) | DB: 2)
  * `testGetRelativeLinkTo_JobContainedInView` (Impact: 40.0 | O(N^4))
  * `testGetRelativeLinkTo_JobContainedInView` (Impact: 35.6 | O(N^4))
  * `getRelativeLinkTo_MavenModules` (Impact: 35.5 | O(N^4))
  * `suppressed` (Impact: 33.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 168`, `args: 62`, `func_start: 188`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 19`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 28`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 43`
* *Defense:* `safety: 12`, `test: 162`, `sync_locks: 2`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` java.util.logging.Level, org.mockito.Mockito.when, hudson.util.VersionNumber, java.util.Collections, org.junit.jupiter.api.Assertions.assertFalse, java.util.regex.Matcher, hudson.model.TopLevelItem, java.util.Arrays...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/ExtensionFinder.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.961 IQR)
- **Top Global Matches:** file_cluster_13: 11.961, file_cluster_16: 12.246, file_cluster_0: 12.257
- **Magnitude:** 1761.22 | **LOC:** 802 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (33.8952%), Tech Debt (48.9756%)
**Top Internal Functions/Classes:**
  * `isOptional` (Impact: 1611.8 | O(2^N) | DB: 15)
    * *Intent:* /** * Rebuilds the internal index, if any, so that future {@link #find(Class, Hudson)} calls * will ...
  * `getClassFromIndex` (Impact: 31.7 | O(N^3))
  * `isRefreshable` (Impact: 12.3 | O(N^3))
  * `isOptional` (Impact: 4.6 | O(N^3))
    * *Intent:* /** * Discovers the implementations of an extension point. * * <p> * This extension point allows you...
  * `getOrdinal` (Impact: 4.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 141`, `args: 43`, `func_start: 50`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 39`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 31`, `concurrency: 2`, `import: 44`
* *Defense:* `safety: 18`, `doc: 23`, `sync_locks: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.472
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` com.google.inject.Provider, java.util.logging.Level, java.lang.reflect.Constructor, java.util.Collections, com.google.inject.name.Names, java.lang.reflect.Method, org.kohsuke.accmod.restrictions.NoExternalUse, com.google.inject.spi.ProvisionListener...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/PluginManager.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.864 IQR)
- **Top Global Matches:** file_cluster_13: 12.864, file_cluster_0: 13.098, file_cluster_11: 13.237
- **Magnitude:** 1692.9 | **LOC:** 2698 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (16.2609%), Tech Debt (90.7814%)
**Top Internal Functions/Classes:**
  * `parseRequestedPlugins` (Impact: 454.1 | O(N^6) | DB: 14)
  * `TaskGraphBuilder` (Impact: 208.8 | O(2^N) | DB: 16)
  * `addDependencies` (Impact: 170.4 | O(2^N) | DB: 1)
  * `initTasks` (Impact: 132.7 | O(N^6) | DB: 11)
    * *Intent:* /**
  * `getBundledJpiManifestStream` (Impact: 95.8 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 379`, `args: 76`, `func_start: 79`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 122`, `planned_debt: 5`, `duplicate_logic: 11`
* *Architecture:* `io: 32`, `api: 85`, `concurrency: 3`, `import: 154`
* *Defense:* `safety: 69`, `doc: 89`, `sync_locks: 1`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` jenkins.InitReactorRunner, org.kohsuke.stapler.HttpResponse, org.kohsuke.stapler.HttpRedirect, hudson.util.CachingClassLoader, java.util.Objects, org.kohsuke.accmod.restrictions.NoExternalUse, io.jenkins.servlet.ServletContextWrapper, org.jvnet.hudson.reactor.Reactor...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Job.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.117 IQR)
- **Top Global Matches:** file_cluster_13: 12.117, file_cluster_0: 12.28, file_cluster_11: 12.684
- **Magnitude:** 1565.38 | **LOC:** 1732 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (18.2035%), Tech Debt (97.4833%)
**Top Internal Functions/Classes:**
  * `getBuildStabilityHealthReport` (Impact: 186.6 | O(N^6))
    * *Intent:* /** * Directory for storing {@link Run} records. * <p> * Some {@link Job}s may not have backing data...
  * `getDynamic` (Impact: 127.0 | O(2^N))
  * `doRssChangelog` (Impact: 106.8 | O(N^6) | DB: 2)
    * *Intent:* /** * Gets the read-only view of the recent builds.
  * `onLocationChanged` (Impact: 78.3 | O(N^6) | DB: 9)
  * `makeSearchIndex` (Impact: 71.2 | O(2^N) | DB: 2)
    * *Intent:* /** * Returns whether the name of this job can be changed by user. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 331`, `args: 99`, `func_start: 105`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 71`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 13`
* *Architecture:* `io: 16`, `api: 128`, `concurrency: 14`, `import: 114`
* *Defense:* `safety: 24`, `doc: 101`, `sync_locks: 9`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.979
  * `Choke Point (Betweenness):` 0.000414 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 55):` jenkins.scm.RunWithSCM, jenkins.model.ProjectNamingStrategy, org.kohsuke.accmod.restrictions.NoExternalUse, java.util.GregorianCalendar, hudson.PermalinkList, java.util.List, org.jfree.chart.renderer.category.StackedAreaRenderer, org.kohsuke.args4j.Argument...
  * `Imported By (In-Degree: 61):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Executor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.071 IQR)
- **Top Global Matches:** file_cluster_13: 12.071, file_cluster_0: 12.296, file_cluster_11: 12.679
- **Magnitude:** 1507.96 | **LOC:** 993 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (11.5555%), Tech Debt (72.6096%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 679.6 | O(2^N) | DB: 8)
    * *Intent:* // worth recording who did it // avoid using User.get() to avoid deadlock.
  * `finish1` (Impact: 416.1 | O(N^6))
  * `interrupt` (Impact: 157.3 | O(2^N) | DB: 1)
  * `resetWorkUnit` (Impact: 68.3 | O(N^5) | DB: 1)
    * *Intent:* // we abort the build. // but that causes JENKINS-28690 style deadlocks when the correctly written c...
  * `recordCauseOfInterruption` (Impact: 41.2 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 139`, `args: 35`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 36`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 34`, `concurrency: 4`, `import: 57`
* *Defense:* `safety: 60`, `doc: 45`, `sync_locks: 59`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.483
  * `Choke Point (Betweenness):` 0.000131 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` java.util.logging.Level.FINE, java.util.logging.Level, org.kohsuke.stapler.StaplerRequest, org.kohsuke.stapler.interceptor.RequirePOST, java.util.Collections, org.kohsuke.stapler.HttpResponse, java.io.IOException, org.kohsuke.stapler.export.ExportedBean...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/AbstractProject.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.081 IQR)
- **Top Global Matches:** file_cluster_13: 12.081, file_cluster_0: 12.214, file_cluster_11: 12.566
- **Magnitude:** 1495.7 | **LOC:** 2164 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.2319%), Tech Debt (88.3932%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 104.1 | O(N^5))
  * `checkout` (Impact: 68.1 | O(2^N) | DB: 3)
  * `isAllSuitableNodesOffline` (Impact: 63.9 | O(N^6))
    * *Intent:* /** * Schedules a build. * * Important: the actions should be persistable without outside references...
  * `workspaceOffline` (Impact: 63.1 | O(N^4))
    * *Intent:* /** * Schedules a build of this project, and returns a {@link Future} object * to wait for the compl...
  * `getCauseOfBlockage` (Impact: 61.2 | O(N^4))
    * *Intent:* /** * Gets a workspace for some build of this project.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 295`, `args: 98`, `func_start: 97`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 85`, `state_mutation: 50`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 7`
* *Architecture:* `io: 3`, `api: 138`, `concurrency: 18`, `import: 98`
* *Defense:* `safety: 23`, `doc: 110`, `sync_locks: 1`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.325
  * `Choke Point (Betweenness):` 0.000322 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` hudson.triggers.TriggerDescriptor, org.kohsuke.stapler.HttpResponse, org.kohsuke.stapler.HttpRedirect, org.kohsuke.accmod.restrictions.NoExternalUse, hudson.scm.PollingResult.BUILD_NOW, jenkins.scm.DefaultSCMCheckoutStrategyImpl, hudson.Launcher, hudson.slaves.Cloud...
  * `Imported By (In-Degree: 74):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/util/ProcessTree.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.354 IQR)
- **Top Global Matches:** file_cluster_13: 11.354, file_cluster_0: 11.421, file_cluster_8: 11.743
- **Magnitude:** 1488.76 | **LOC:** 2141 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (11.0981%), Tech Debt (99.2508%)
**Top Internal Functions/Classes:**
  * `getEnvironmentVariables` (Impact: 650.5 | O(2^N))
  * `createProcess` (Impact: 91.5 | O(N^5) | DB: 12)
    * *Intent:* /** * Serialized form of {@link OSProcess} is the PID and {@link ProcessTree} */
  * `killRecursively` (Impact: 87.4 | O(N^6))
    * *Intent:* /** * Lazily obtained {@link ProcessKiller}s to be applied on this process tree.
  * `killAll` (Impact: 80.1 | O(N^6))
  * `ProcfsUnix` (Impact: 67.2 | O(N^5) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 182`, `args: 58`, `func_start: 70`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 14`, `planned_debt: 2`, `duplicate_logic: 10`
* *Architecture:* `io: 11`, `api: 40`, `concurrency: 4`, `import: 51`
* *Defense:* `safety: 44`, `doc: 32`, `sync_locks: 3`, `immutability_locks: 25`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.258
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` java.util.logging.Level, java.util.Collections, java.io.Serializable, com.sun.jna.ptr.IntByReference, java.io.IOException, hudson.util.ProcessTreeRemoting.IProcessTree, edu.umd.cs.findbugs.annotations.CheckForNull, com.sun.jna.NativeLong...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/Run.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.674 IQR)
- **Top Global Matches:** file_cluster_13: 12.674, file_cluster_0: 12.878, file_cluster_11: 13.224
- **Magnitude:** 1410.32 | **LOC:** 2700 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (13.8995%), Tech Debt (37.8294%)
**Top Internal Functions/Classes:**
  * `computeDisplayName` (Impact: 844.5 | O(N^6) | DB: 33)
    * *Intent:* /** * Returns the {@link Cause}s that triggered a build. * * <p> * If a build sits in the queue for ...
  * `onLoad` (Impact: 108.8 | O(2^N))
    * *Intent:* /**
  * `getTransientActions` (Impact: 42.6 | O(N^5) | DB: 1)
    * *Intent:* /** * Human-readable description which is used on the main build page. * It can also be quite long, ...
  * `addAction` (Impact: 39.6 | O(2^N))
    * *Intent:* /**
  * `updateFrom` (Impact: 36.9 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 376`, `args: 77`, `func_start: 102`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 61`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 4`
* *Architecture:* `io: 11`, `api: 118`, `concurrency: 6`, `import: 125`
* *Defense:* `safety: 81`, `doc: 137`, `sync_locks: 1`, `immutability_locks: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.083
  * `Choke Point (Betweenness):` 0.000432 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 58):` java.io.Serializable, org.kohsuke.stapler.HttpResponse, java.util.Date, java.util.Objects, org.kohsuke.accmod.restrictions.NoExternalUse, java.util.GregorianCalendar, java.util.Comparator, hudson.util.XStream2...
  * `Imported By (In-Degree: 108):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/UpdateSite.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.744 IQR)
- **Top Global Matches:** file_cluster_13: 11.744, file_cluster_0: 11.804, file_cluster_8: 12.235
- **Magnitude:** 1405.56 | **LOC:** 1768 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (11.4666%), Tech Debt (99.5614%)
**Top Internal Functions/Classes:**
  * `deploy` (Impact: 220.8 | O(2^N) | DB: 3)
  * `Plugin` (Impact: 178.6 | O(N^6) | DB: 2)
  * `isRelevant` (Impact: 85.2 | O(N^6))
    * *Intent:* /** * Gets the raw update center JSON data. */
  * `getDependenciesIncompatibleWithInstalled` (Impact: 78.8 | O(2^N) | DB: 1)
  * `isFixable` (Impact: 78.3 | O(N^6))
    * *Intent:* /** * Returns a list of plugins that should be shown in the "available" tab. * These are "all plugin...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 218`, `args: 75`, `func_start: 61`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 23`, `planned_debt: 4`, `duplicate_logic: 13`
* *Architecture:* `io: 3`, `api: 115`, `concurrency: 8`, `import: 66`
* *Defense:* `safety: 30`, `doc: 131`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.245
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` java.util.logging.Level, org.kohsuke.stapler.DataBoundConstructor, org.kohsuke.stapler.interceptor.RequirePOST, hudson.util.VersionNumber, java.util.Collections, org.kohsuke.stapler.HttpResponse, java.io.IOException, java.util.UUID...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/model/View.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.978 IQR)
- **Top Global Matches:** file_cluster_13: 11.978, file_cluster_0: 12.211, file_cluster_11: 12.682
- **Magnitude:** 1398.38 | **LOC:** 1286 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (15.7024%), Tech Debt (16.7208%)
**Top Internal Functions/Classes:**
  * `getProperties` (Impact: 1159.3 | O(2^N) | DB: 31)
    * *Intent:* /**
  * `getAllItems` (Impact: 50.6 | O(2^N) | DB: 1)
    * *Intent:* /** * Encapsulates the rendering of the list of {@link TopLevelItem}s * that {@link Jenkins} owns. *...
  * `rename` (Impact: 13.9 | O(N^3))
  * `getItem` (Impact: 6.9 | O(2^N))
  * `getJob` (Impact: 3.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 261`, `args: 76`, `func_start: 92`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 40`, `dead_code: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 73`, `concurrency: 11`, `import: 97`
* *Defense:* `safety: 25`, `doc: 68`, `sync_locks: 6`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.046
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` hudson.DescriptorExtensionList, jenkins.model.Badgeable, java.io.Serializable, org.kohsuke.stapler.HttpResponse, org.jenkins.ui.icon.Icon, java.util.Objects, org.kohsuke.stapler.WebMethod, jenkins.model.ModelObjectWithContextMenu...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/ClassicPluginStrategy.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.207 IQR)
- **Top Global Matches:** file_cluster_13: 12.207, file_cluster_0: 12.429, file_cluster_11: 12.491
- **Magnitude:** 1355.18 | **LOC:** 700 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (43.4763%), Tech Debt (44.7711%)
**Top Internal Functions/Classes:**
  * `createPluginWrapper` (Impact: 201.8 | O(N^6) | DB: 58)
  * `load` (Impact: 189.7 | O(2^N) | DB: 5)
  * `findClass` (Impact: 102.9 | O(N^6))
  * `findComponents` (Impact: 84.9 | O(N^5) | DB: 3)
    * *Intent:* /** * Creates a classloader that can load all the specified jar files and delegate to the given pare...
  * `findResources` (Impact: 79.4 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 174`, `args: 37`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 87`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 57`, `api: 26`, `concurrency: 19`, `import: 51`
* *Defense:* `safety: 33`, `doc: 17`, `sync_locks: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.145
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` java.util.logging.Level, hudson.PluginWrapper.Dependency, org.apache.tools.ant.types.Resource, java.util.Collections, org.apache.tools.ant.BuildException, java.io.IOException, java.util.UUID, hudson.Plugin.DummyImpl...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/main/js/pluginSetupWizardGui.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.428 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.77 IQR)
- **Top Global Matches:** file_cluster_13: 13.428, file_cluster_8: 13.443, file_cluster_11: 13.505
- **Magnitude:** 1350.16 | **LOC:** 1455 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (93.4425%), Tech Debt (21.3362%)
**Top Internal Functions/Classes:**
  * `searchForPlugins` (Impact: 390.0 | O(2^N) | DB: 44)
  * `createPluginSetupWizard` (Impact: 376.1 | O(N^4) | DB: 81)
  * `walk` (Impact: 47.9 | O(2^N) | DB: 2)
  * `scrollPlugin` (Impact: 25.5 | O(N^3) | DB: 3)
  * `loadPluginCategories` (Impact: 22.3 | O(N^3) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 197`, `args: 78`, `func_start: 97`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 403`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `concurrency: 25`, `import: 21`
* *Defense:* `safety: 26`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` offlinePanel.hbs, securityConfig, pluginSelectList.hbs, id, welcomePanel.hbs, incompleteInstallationPanel.hbs, setupCompletePanel.hbs, bootstrap-detached...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/src/test/java/lib/form/RepeatableTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.694 IQR)
- **Top Global Matches:** file_cluster_0: 11.694, file_cluster_13: 11.75, file_cluster_8: 12.005
- **Magnitude:** 1253.88 | **LOC:** 681 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (40.1521%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testNested` (Impact: 146.8 | O(2^N) | DB: 8)
  * `testRadioBlock` (Impact: 104.8 | O(2^N) | DB: 8)
  * `testNestedRadio` (Impact: 96.6 | O(2^N) | DB: 3)
  * `testNestedEnabledTopButton` (Impact: 74.0 | O(N^5) | DB: 8)
  * `testNestedEnabledTopButtonInner` (Impact: 74.0 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 143`, `args: 50`, `func_start: 134`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 74`, `duplicate_logic: 5`, `orphaned_logic: 19`
* *Architecture:* `io: 26`, `api: 36`, `concurrency: 2`, `import: 31`
* *Defense:* `safety: 12`, `doc: 16`, `test: 59`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` hudson.DescriptorExtensionList, org.kohsuke.stapler.DataBoundConstructor, org.htmlunit.html.HtmlSelect, java.io.IOException, org.htmlunit.WebClientUtil, org.htmlunit.html.HtmlButton, org.htmlunit.html.HtmlForm, net.sf.json.JSONObject...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/model/ListView.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.983 IQR)
- **Top Global Matches:** file_cluster_13: 11.983, file_cluster_0: 12.102, file_cluster_4: 12.197
- **Magnitude:** 1243.0 | **LOC:** 654 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (25.9934%), Tech Debt (94.6665%)
**Top Internal Functions/Classes:**
  * `getItems` (Impact: 284.5 | O(2^N) | DB: 3)
  * `submitImpl` (Impact: 88.9 | O(N^5) | DB: 3)
  * `doCreateItem` (Impact: 73.5 | O(2^N) | DB: 1)
  * `locationChanged` (Impact: 60.5 | O(2^N))
  * `submit` (Impact: 56.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 155`, `args: 46`, `func_start: 82`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 54`, `dead_code: 1`, `duplicate_logic: 10`
* *Architecture:* `api: 59`, `concurrency: 47`, `import: 48`
* *Defense:* `safety: 24`, `doc: 32`, `sync_locks: 12`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.44
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` java.util.logging.Level, org.kohsuke.stapler.StaplerRequest, org.kohsuke.stapler.DataBoundConstructor, org.kohsuke.stapler.interceptor.RequirePOST, java.util.Collections, org.jenkinsci.Symbol, org.kohsuke.stapler.HttpResponse, java.io.IOException...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/slaves/SlaveComputer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.516 IQR)
- **Top Global Matches:** file_cluster_13: 11.516, file_cluster_0: 11.631, file_cluster_11: 12.088
- **Magnitude:** 1238.4 | **LOC:** 1207 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (16.1626%), Tech Debt (14.1323%)
**Top Internal Functions/Classes:**
  * `disconnect` (Impact: 481.7 | O(2^N) | DB: 9)
  * `_connect` (Impact: 441.0 | O(N^6) | DB: 14)
  * `getDelegatedLauncher` (Impact: 35.6 | O(N^4))
    * *Intent:* /** * Allows suspension of tasks being accepted by the agent computer. While this could be called by...
  * `decorate` (Impact: 28.5 | O(N^4) | DB: 6)
    * *Intent:* /** * Effective {@link ComputerLauncher} that hides the details of
  * `getNode` (Impact: 24.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 224`, `args: 57`, `func_start: 68`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 36`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 10`, `api: 62`, `concurrency: 13`, `import: 78`
* *Defense:* `safety: 27`, `doc: 40`, `sync_locks: 3`, `immutability_locks: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 8.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` edu.umd.cs.findbugs.annotations.OverrideMustInvoke, hudson.remoting.ChannelBuilder, org.kohsuke.stapler.HttpResponse, org.kohsuke.stapler.HttpRedirect, org.kohsuke.accmod.restrictions.NoExternalUse, hudson.Main, org.kohsuke.stapler.WebMethod, jenkins.slaves.RemotingVersionInfo...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `core/src/main/java/hudson/Launcher.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.291 IQR)
- **Top Global Matches:** file_cluster_0: 11.291, file_cluster_13: 11.352, file_cluster_8: 11.564
- **Magnitude:** 1154.3 | **LOC:** 1500 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (6.7795%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `join` (Impact: 113.4 | O(2^N))
  * `launch` (Impact: 87.6 | O(N^6) | DB: 9)
    * *Intent:* /** * Launch a command with optional censoring of arguments from the listener (Note: <strong>The cen...
  * `envs` (Impact: 86.3 | O(2^N))
    * *Intent:* * * <p> * This hides the difference between running programs locally vs remotely. * * * <h2>'env' pa...
  * `join` (Impact: 70.7 | O(2^N))
  * `launch` (Impact: 68.3 | O(N^5))
    * *Intent:* /** * Indicates that the caller will directly write to the child process {@link #stdin()} via {@link...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 201`, `args: 82`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 3`, `state_mutation: 3`, `planned_debt: 2`, `duplicate_logic: 36`
* *Architecture:* `io: 37`, `api: 86`, `concurrency: 4`, `import: 41`
* *Defense:* `safety: 43`, `doc: 104`, `sync_locks: 2`, `immutability_locks: 39`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.277
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` hudson.Proc.ProcWithJenkins23271Patch, java.util.logging.Level, hudson.remoting.RemoteOutputStream, java.io.Serializable, java.io.IOException, org.kohsuke.accmod.restrictions.NoExternalUse, edu.umd.cs.findbugs.annotations.CheckForNull, hudson.model.TaskListener...
  * `Imported By (In-Degree: 87):` (Excluded from Brief to save tokens)

### `war/src/main/webapp/scripts/hudson-behavior.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.154 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.911 IQR)
- **Top Global Matches:** file_cluster_17: 13.154, file_cluster_0: 13.157, file_cluster_11: 13.188
- **Magnitude:** 1149.38 | **LOC:** 2761 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (58.7712%), Tech Debt (12.5296%)
**Top Internal Functions/Classes:**
  * `delayedCheck` (Impact: 985.6 | O(2^N) | DB: 41)
  * `TryEach` (Impact: 5.6 | O(N^1))
    * *Intent:* * of this software and associated documentation files (the "Software"), to deal * in the Software wi...
  * `creator` (Impact: 4.3 | O(N^1) | DB: 6)
  * `object` (Impact: 2.0 | O(N^1))
    * *Intent:* * The MIT License * * Copyright (c) 2004-2010, Sun Microsystems, Inc., Kohsuke Kawaguchi, * Daniel D...
  * `onVisibilityChange` (Impact: 1.9 | O(N^1))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 80`, `args: 41`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 140`, `dead_code: 4`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 24`, `doc: 21`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/hudson/model/Computer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.897 IQR)
- **Top Global Matches:** file_cluster_13: 11.897, file_cluster_0: 12.094, file_cluster_11: 12.447
- **Magnitude:** 1139.68 | **LOC:** 1802 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (14.9605%), Tech Debt (47.582%)
**Top Internal Functions/Classes:**
  * `doRssLatest` (Impact: 73.4 | O(N^6) | DB: 1)
  * `getHostName` (Impact: 61.6 | O(N^5) | DB: 2)
    * *Intent:* /** * Equivalent to {@code disconnect(null)}
  * `relocateOldLogs` (Impact: 61.4 | O(N^5) | DB: 18)
  * `setNumExecutors` (Impact: 48.1 | O(N^6) | DB: 1)
    * *Intent:* // TODO implement addOrReplaceAction, removeAction, removeActions, replaceActions /** * This is wher...
  * `doConfigSubmit` (Impact: 43.4 | O(N^5) | DB: 1)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 296`, `args: 86`, `func_start: 96`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 72`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `io: 9`, `api: 123`, `concurrency: 4`, `import: 115`
* *Defense:* `safety: 19`, `doc: 90`, `sync_locks: 3`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.225
  * `Choke Point (Betweenness):` 0.000366 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` edu.umd.cs.findbugs.annotations.OverrideMustInvoke, org.kohsuke.stapler.HttpResponse, org.kohsuke.stapler.HttpRedirect, java.util.Date, org.kohsuke.accmod.restrictions.NoExternalUse, org.kohsuke.stapler.WebMethod, jenkins.util.ContextResettingExecutorService, java.util.concurrent.ExecutorService...
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `core/src/main/java/hudson/Proc.java` (JAVA) | Magnitude: 628.92 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 93, branch: 49, func_start: 48
- `core/src/main/java/hudson/model/queue/AbstractSubTask.java` (JAVA) | Magnitude: 13.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 2, class_start: 1, api: 1
- `core/src/main/java/org/acegisecurity/userdetails/UserDetails.java` (JAVA) | Magnitude: 86.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 24, args: 15, func_start: 14
- `test/src/test/java/jenkins/security/stapler/StaplerRoutableFieldTest.java` (JAVA) | Magnitude: 62.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 108, func_start: 45, test: 45, structural_boundaries: 41
- `core/src/main/java/hudson/views/LastDurationColumn.java` (JAVA) | Magnitude: 10.36 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, api: 4, decorators: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `war/src/main/webapp/WEB-INF/hudson` (SHELL) | Magnitude: 43.84 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 27, structural_boundaries: 9, indent_spaces: 9, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/src/test/java/org/kohsuke/stapler/beanutils/BeanUtilsTagLibrary.java` (JAVA) | Magnitude: 17.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 12, func_start: 5, import: 5
- `core/src/main/java/hudson/model/PermalinkProjectAction.java` (JAVA) | Magnitude: 59.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 36, doc: 23, api: 16, structural_boundaries: 13
- `cli/src/main/java/hudson/cli/NoCheckTrustManager.java` (JAVA) | Magnitude: 11.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 13, decorators: 6, api: 4
- `test/src/test/java/hudson/model/FileParameterValueTest.java` (JAVA) | Magnitude: 131.68 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 290, structural_boundaries: 132, func_start: 71, io: 63
- `test/src/test/java/jenkins/security/ApiTokenPropertyTest.java` (JAVA) | Magnitude: 252.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 485, func_start: 154, structural_boundaries: 140, test: 74

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `core/src/test/java/jenkins/org/apache/commons/validator/routines/InetAddressValidatorTest.java` (JAVA) | Magnitude: 3407.08 | Delta: **0.285 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1266, args: 263, closures: 254, indent_spaces: 232

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `core/src/main/java/hudson/util/TagCloud.java` (JAVA) | Magnitude: 55.2 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 15, api: 12, args: 7
- `core/src/main/java/hudson/model/ItemGroup.java` (JAVA) | Magnitude: 128.66 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 37, doc: 33, generics: 23
- `core/src/main/java/jenkins/model/details/KeptForeverDetail.java` (JAVA) | Magnitude: 12.24 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, branch: 8, structural_boundaries: 7, api: 4
- `core/src/main/java/jenkins/model/RunAction2.java` (JAVA) | Magnitude: 91.24 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, branch: 4, doc: 4, args: 2
- `core/src/main/java/jenkins/util/InterceptingExecutorService.java` (JAVA) | Magnitude: 220.68 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 39, args: 31, generics: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `war/src/main/webapp/scripts/hudson-behavior.js` (JAVASCRIPT) | Magnitude: 1149.38 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 386, state_mutation: 140, branch: 108, structural_boundaries: 80
- `war/src/main/webapp/scripts/behavior.js` (JAVASCRIPT) | Magnitude: 190.76 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 111, state_mutation: 36, branch: 26, args: 17
- `core/src/main/resources/lib/form/select/select.js` (JAVASCRIPT) | Magnitude: 2.5 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 86, state_mutation: 30, branch: 24, structural_boundaries: 14
- `core/src/main/resources/lib/form/repeatable/repeatable.js` (JAVASCRIPT) | Magnitude: 3.32 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, state_mutation: 106, branch: 28, structural_boundaries: 23
- `src/main/js/add-item.js` (JAVASCRIPT) | Magnitude: 239.44 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 216, state_mutation: 60, structural_boundaries: 55, func_start: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `core/src/main/resources/hudson/model/LoadStatistics/resources.js` (JAVASCRIPT) | Magnitude: 15.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, immutability_locks: 13, globals: 5, ui_framework: 4
- `core/src/main/resources/hudson/model/DirectoryBrowserSupport/pattern.js` (JAVASCRIPT) | Magnitude: 25.32 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 10, structural_boundaries: 4, globals: 3
- `core/src/main/resources/lib/hudson/editable-description.js` (JAVASCRIPT) | Magnitude: 0.12 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, ui_framework: 6, globals: 6, args: 5
- `core/src/main/resources/lib/layout/progressiveRendering/progressiveRendering.js` (JAVASCRIPT) | Magnitude: 0.55 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, func_start: 9, args: 7, globals: 7
- `src/main/js/util/i18n.js` (JAVASCRIPT) | Magnitude: 2.98 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `core/src/main/java/jenkins/util/URLClassLoader2.java` (JAVA) | Magnitude: 77.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 19, concurrency: 18, doc: 17
- `core/src/main/java/hudson/util/ConsistentHash.java` (JAVA) | Magnitude: 363.0 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 56, func_start: 44, concurrency: 43
- `core/src/test/java/jenkins/model/lazy/AbstractLazyLoadRunMapTest.java` (JAVA) | Magnitude: 191.52 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 74, test: 57, concurrency: 56
- `test/src/test/java/hudson/model/HelpLinkTest.java` (JAVA) | Magnitude: 34.1 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, import: 19, indent_spaces: 18, concurrency: 13
- `test/src/test/java/hudson/bugs/DateConversionTest.java` (JAVA) | Magnitude: 56.08 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 15, concurrency: 10, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `core/src/main/java/hudson/scheduler/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, doc: 1, planned_debt: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/main/js/components/dropdowns/types.js` (JAVASCRIPT) | Magnitude: 10.52 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: doc: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `test/src/test/java/hudson/model/UpdateCenterMigrationTest.java` (JAVA) | Magnitude: 128.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 29, args: 13, import: 11
- `test/src/test/java/jenkins/tasks/filters/impl/RetainVariablesLocalRuleTest.java` (JAVA) | Magnitude: 283.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 266, structural_boundaries: 123, state_mutation: 50, test: 50
- `core/src/main/java/hudson/AbortException.java` (JAVA) | Magnitude: 8.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, func_start: 3, api: 3
- `test/src/test/java/hudson/util/SecretCompatTest.java` (JAVA) | Magnitude: 13.0 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 34, import: 18, func_start: 13
- `core/src/test/java/hudson/util/DirScannerTest.java` (JAVA) | Magnitude: 40.26 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 28, func_start: 8, io: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `core/src/main/java/jenkins/util/io/OnMaster.java` (JAVA) | Magnitude: 12.56 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 11, structural_boundaries: 2, doc: 2, class_start: 1
- `core/src/main/java/jenkins/model/lazy/Boundary.java` (JAVA) | Magnitude: 11.14 | Delta: **0.455 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, func_start: 6, structural_boundaries: 4, args: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ath.sh` -> Churn: **68.03%** | Cog Load: 94.4594% | Debt: 99.9999%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/src/main/java/hudson/model/Fingerprint.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 1975.28
- `core/src/main/java/hudson/model/UpdateCenter.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 1941.38
- `core/src/main/java/hudson/util/ProcessTree.java` -> **strangelookingnerd** (100.0% isolated ownership) | Magnitude: 1488.76
- `core/src/main/java/hudson/model/View.java` -> **Jan Faracik** (100.0% isolated ownership) | Magnitude: 1398.38
- `core/src/main/java/hudson/ClassicPluginStrategy.java` -> **Dmitriy Ukhlov** (100.0% isolated ownership) | Magnitude: 1355.18

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/src/main/java/jenkins/model/Jenkins.java` -> **Severity: 0.171** (Bridge: 0.0024 * Flux: 70.6074%)
- `core/src/main/java/hudson/model/Job.java` -> **Severity: 0.029** (Bridge: 0.0004 * Flux: 70.7564%)
- `core/src/main/java/hudson/model/Computer.java` -> **Severity: 0.025** (Bridge: 0.0004 * Flux: 69.6561%)
- `core/src/main/java/hudson/model/Run.java` -> **Severity: 0.017** (Bridge: 0.0004 * Flux: 38.8041%)
- `core/src/main/java/hudson/Functions.java` -> **Severity: 0.016** (Bridge: 0.0005 * Flux: 34.5117%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/src/main/java/jenkins/YesNoMaybe.java` -> **Severity: 773.81** (Blast Radius: 9.666 * Doc Risk: 80.0548%)
- `core/src/main/java/hudson/Functions.java` -> **Severity: 522.1** (Blast Radius: 5.221 * Doc Risk: 100.0%)
- `core/src/main/java/org/jenkins/ui/symbol/Symbol.java` -> **Severity: 318.042** (Blast Radius: 3.533 * Doc Risk: 90.0204%)
- `core/src/main/java/org/acegisecurity/Authentication.java` -> **Severity: 311.368** (Blast Radius: 3.117 * Doc Risk: 99.8934%)
- `core/src/main/java/hudson/util/IOUtils.java` -> **Severity: 256.863** (Blast Radius: 2.856 * Doc Risk: 89.9382%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
