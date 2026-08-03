# ARCHITECTURAL_BRIEF: jellyfin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/jellyfin` |
| **Timestamp** | `2026-08-03T20:59:00.821138+00:00` |
| **Scan Duration** | `6.03s` |
| **Git Branch** | `master` |
| **Git Commit** | `dbc42bb8e236f9ead33ddd47d500b7d00f52805d` |
| **Git Remote** | `https://github.com/jellyfin/jellyfin.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1836 malicious artifacts.

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
| Total Artifacts | 2334 |
| Analyzed Artifacts (Scanned) | 2010 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 324 |
| Total LOC | 146196 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 86.1% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4567 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1517 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9391 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 1834 | 130604 | 91.2% |
| JSON | 153 | 14969 | 7.6% |
| HTML | 7 | 607 | 0.3% |
| PLAINTEXT | 6 | 0 | 0.3% |
| MARKDOWN | 6 | 0 | 0.3% |
| XML | 2 | 0 | 0.1% |
| SHELL | 2 | 16 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.403`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 1121 | 55.8% |
| file_cluster_8 | 551 | 27.4% |
| file_cluster_7 | 114 | 5.7% |
| file_cluster_0 | 92 | 4.6% |
| file_cluster_16 | 72 | 3.6% |
| file_cluster_4 | 29 | 1.4% |
| file_cluster_17 | 7 | 0.3% |
| file_cluster_6 | 3 | 0.1% |
| file_cluster_15 | 3 | 0.1% |
| file_cluster_11 | 2 | 0.1% |
| file_cluster_1 | 2 | 0.1% |
| file_cluster_2 | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 0.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 324*

**Composition by Extension & Reason:**
- `.cs`: 103x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 1596 LOC), 2x Excluded (Machine-Generated Source Code Signature: 1611 LOC)
- `.json`: 88x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csproj`: 32x Excluded (Unsupported Extension: '.csproj'), 10x Unsupported Format (.csproj)
- `.nfo`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace'), 1x Unsupported Format (.undeterminable)
- `.props`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.props'), 1x Unsupported Format (.props)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.srt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 96.5 | 14.1 | 5.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 43.1 | 49.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.7 | 2.3 | 80.0 |
| API Exposure | 0.0 | 17.0 | 6.0 | 5.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 48.2 | 39.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 76.2 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.7 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.6 | 12.2 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 50.5 | 56.4 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 36.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 97.7 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `MediaBrowser.Providers/Manager/ImageSaver.cs` (Hits: 31)
- `tests/Jellyfin.Server.Implementations.Tests/Plugins/PluginManagerTests.cs` (Hits: 31)
- `Jellyfin.Server/Migrations/Routines/MoveExtractedFiles.cs` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Library.cs** (`src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/Libraries/Library.cs`) — 252 inbound connections
2. **Extensions.cs** (`MediaBrowser.Controller/Entities/Extensions.cs`) — 220 inbound connections
3. **Audio.cs** (`MediaBrowser.Controller/Entities/Audio/Audio.cs`) — 88 inbound connections
4. **MediaInfo.cs** (`MediaBrowser.Model/MediaInfo/MediaInfo.cs`) — 60 inbound connections
5. **Constants.cs** (`MediaBrowser.Model/Cryptography/Constants.cs`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ApplicationHost.cs** (`Emby.Server.Implementations/ApplicationHost.cs`) — 102 outbound dependencies
2. **ProviderManager.cs** (`MediaBrowser.Providers/Manager/ProviderManager.cs`) — 41 outbound dependencies
3. **SessionManager.cs** (`Emby.Server.Implementations/Session/SessionManager.cs`) — 40 outbound dependencies
4. **LibraryController.cs** (`Jellyfin.Api/Controllers/LibraryController.cs`) — 39 outbound dependencies
5. **ApiServiceCollectionExtensions.cs** (`Jellyfin.Server/Extensions/ApiServiceCollectionExtensions.cs`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `GetPostedPlaybackInfo` (@ `Jellyfin.Api/Controllers/MediaInfoController.cs`) -> Impact: **2976.5** | LOC: 134
  * *Intent:* /// <param name="subtitleStreamIndex">The subtitle stream index.</param> /// <param name="maxAudioChannels">The maximum number of audio channels.</par...
- `GetChildCount` (@ `Emby.Server.Implementations/Dto/DtoService.cs`) -> Impact: **1227.8** | LOC: 914
- `GetAudioDirectPlayProfile` (@ `MediaBrowser.Model/Dlna/StreamBuilder.cs`) -> Impact: **1047.3** | LOC: 577
- `ParseParams` (@ `Jellyfin.Api/Helpers/StreamingHelpers.cs`) -> Impact: **944.4** | LOC: 198
- `GetVersionInfo` (@ `MediaBrowser.Controller/Entities/BaseItem.cs`) -> Impact: **881.1** | LOC: 962
- `Filter` (@ `MediaBrowser.Controller/Entities/UserViewBuilder.cs`) -> Impact: **863.4** | LOC: 464
- `FetchDataFromXmlNode` (@ `MediaBrowser.LocalMetadata/Parsers/BaseItemXmlParser.cs`) -> Impact: **849.9** | LOC: 387
  * *Intent:* /// <summary> /// Fetches metadata from one Xml Element. /// </summary> /// <param name="reader">The reader.</param> /// <param name="itemResult">The ...
- `Fetch` (@ `MediaBrowser.XbmcMetadata/Parsers/BaseNfoParser.cs`) -> Impact: **818.2** | LOC: 398
  * *Intent:* /// <summary> /// Fetches the specified item. /// </summary> /// <param name="item">The <see cref="MetadataResult{T}"/>.</param> /// <param name="meta...
- `GetProgramsAsync` (@ `src/Jellyfin.LiveTv/Listings/SchedulesDirect.cs`) -> Impact: **809.4** | LOC: 584
- `FetchFromItunesInfo` (@ `MediaBrowser.MediaEncoding/Probing/ProbeResultNormalizer.cs`) -> Impact: **803.5** | LOC: 551

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Resolve` (@ `Emby.Naming/Video/VideoListResolver.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Resolves alternative versions and extras from list of video files. /// </summary> /// <param name="videoInfos">List of related video...
- `Dispose` (@ `Emby.Server.Implementations/ApplicationHost.cs`) -> **O(2^N) [Recursive]**
- `WebSocketRequestHandler` (@ `Emby.Server.Implementations/HttpServer/WebSocketManager.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <inheritdoc />
- `GetDrives` (@ `Emby.Server.Implementations/IO/ManagedFileSystem.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* // Copying over will fail against hidden files
- `ChangePluginState` (@ `Emby.Server.Implementations/Plugins/PluginManager.cs`) -> **O(2^N) [Recursive]**
- `Dispose` (@ `Emby.Server.Implementations/ScheduledTasks/ScheduledTaskWorker.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Releases unmanaged and - optionally - managed resources. /// </summary> /// <param name="dispose"><c>true</c> to release both manage...
- `OnPlaybackStopped` (@ `Emby.Server.Implementations/Session/SessionManager.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Used to report that playback has ended for an item. /// </summary> /// <param name="info">The info.</param> /// <returns>Task.</retu...
- `TranslateItemForPlayback` (@ `Emby.Server.Implementations/Session/SessionManager.cs`) -> **O(2^N) [Recursive]**
- `HandleRequest` (@ `Emby.Server.Implementations/SyncPlay/SyncPlayManager.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <inheritdoc />
- `Dispose` (@ `Emby.Server.Implementations/Updates/InstallationManager.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Releases unmanaged and optionally managed resources. /// </summary> /// <param name="dispose"><c>true</c> to release both managed an...

### Highest Data Gravity (Database Complexity)
- `Up` (@ `src/Jellyfin.Database/Jellyfin.Database.Providers.Sqlite/Migrations/20241020103111_LibraryDbMigration.cs`) -> DB Complexity: **173**
  * *Intent:* /// <inheritdoc />
- `GetItem` (@ `Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs`) -> DB Complexity: **88**
- `Get_DisplayTitle_TestData` (@ `tests/Jellyfin.Model.Tests/Entities/MediaStreamTests.cs`) -> DB Complexity: **84**
- `LogEnvironmentInfo` (@ `Jellyfin.Server/Helpers/StartupHelpers.cs`) -> DB Complexity: **83**
  * *Intent:* /// <summary> /// Logs relevant environment variables and information about the host. /// </summary> /// <param name="logger">The logger to use.</para...
- `Perform` (@ `Jellyfin.Server/Migrations/Routines/MigrateUserDb.cs`) -> DB Complexity: **73**
  * *Intent:* /// <inheritdoc/>
- `Perform` (@ `Jellyfin.Server/Migrations/Routines/MigrateDisplayPreferencesDb.cs`) -> DB Complexity: **65**
  * *Intent:* /// <inheritdoc />
- `Perform` (@ `Jellyfin.Server/Migrations/PreStartupRoutines/MigrateEncodingOptions.cs`) -> DB Complexity: **64**
  * *Intent:* /// <inheritdoc />
- `ModelBinder` (@ `Jellyfin.Api/Controllers/UniversalAudioController.cs`) -> DB Complexity: **49**
  * *Intent:* /// <param name="startTimeTicks">Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.</param> /// <param name="transcodingContainer">Opti...
- `GetMediaStream` (@ `Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs`) -> DB Complexity: **49**
  * *Intent:* /// <summary> /// Gets the media stream. /// </summary> /// <param name="reader">The reader.</param> /// <returns>MediaStream.</returns>
- `Up` (@ `src/Jellyfin.Database/Jellyfin.Database.Providers.Sqlite/Migrations/20200613202153_AddUsers.cs`) -> DB Complexity: **48**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Jellyfin.Api/Controllers` | 59 | 20067.74 | 20.15% | 47.9% |
| `MediaBrowser.Controller/Entities` | 46 | 9068.08 | 16.88% | 43.73% |
| `MediaBrowser.Controller/MediaEncoding` | 16 | 8639.87 | 21.33% | 31.24% |
| `MediaBrowser.Model/Dlna` | 24 | 4959.4 | 21.5% | 29.5% |
| `Jellyfin.Server/Migrations/Routines` | 28 | 4921.0 | 18.77% | 39.66% |
| `Emby.Server.Implementations/Session` | 3 | 3830.7 | 34.96% | 43.8% |
| `MediaBrowser.Providers/Manager` | 5 | 3670.02 | 17.81% | 36.32% |
| `src/Jellyfin.LiveTv` | 4 | 3527.76 | 63.47% | 63.91% |
| `MediaBrowser.Providers/MediaInfo` | 12 | 3524.7 | 26.41% | 39.99% |
| `Jellyfin.Api/Helpers` | 8 | 3194.58 | 16.28% | 55.53% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Jellyfin.Api/BaseJellyfinApiController.cs` -> **100.0%** Exposure
- `Jellyfin.Api/Extensions/ClaimsPrincipalExtensions.cs` -> **100.0%** Exposure
- `Jellyfin.Api/Models/ConfigurationPageInfo.cs` -> **100.0%** Exposure
- `Jellyfin.Data/UserEntityExtensions.cs` -> **100.0%** Exposure
- `Jellyfin.Server.Implementations/Extensions/ExpressionExtensions.cs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Emby.Naming/AudioBook/AudioBookFileInfo.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookFilePathParserResult.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookInfo.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookNameParserResult.cs` -> **100.0%** Exposure
- `Emby.Naming/Book/BookFileNameParserResult.cs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Emby.Server.Implementations/Session/SessionManager.cs` -> **16** Orphaned Functions | **15** Duplicates
- `Emby.Server.Implementations/IO/ManagedFileSystem.cs` -> **15** Orphaned Functions | **12** Duplicates
- `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` -> **24** Orphaned Functions | **2** Duplicates
- `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` -> **14** Orphaned Functions | **11** Duplicates
- `tests/Jellyfin.Model.Tests/Entities/ProviderIdsExtensionsTests.cs` -> **22** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Jellyfin.Api/Controllers/AudioController.cs`** -> AI Confidence: **99.48%**
2. **`Jellyfin.Api/Controllers/TrailersController.cs`** -> AI Confidence: **99.48%**
3. **`MediaBrowser.Controller/Entities/InternalItemsQuery.cs`** -> AI Confidence: **99.48%**
4. **`MediaBrowser.Model/Dto/BaseItemDto.cs`** -> AI Confidence: **99.48%**
5. **`Jellyfin.Api/Controllers/MediaInfoController.cs`** -> AI Confidence: **99.39%**
6. **`Jellyfin.Api/Models/LiveTvDtos/GetProgramsDto.cs`** -> AI Confidence: **99.39%**
7. **`MediaBrowser.LocalMetadata/Parsers/BaseItemXmlParser.cs`** -> AI Confidence: **99.39%**
8. **`tests/Jellyfin.Model.Tests/Dlna/LegacyStreamInfo.cs`** -> AI Confidence: **99.39%**
9. **`Jellyfin.Api/Helpers/StreamingHelpers.cs`** -> AI Confidence: **99.35%**
10. **`Emby.Naming/Common/NamingOptions.cs`** -> AI Confidence: **99.34%**
11. **`MediaBrowser.Controller/MediaEncoding/TranscodingJob.cs`** -> AI Confidence: **99.34%**
12. **`Emby.Naming/ExternalFiles/ExternalPathParser.cs`** -> AI Confidence: **99.31%**
13. **`Emby.Server.Implementations/Dto/DtoService.cs`** -> AI Confidence: **99.31%**
14. **`Emby.Server.Implementations/IO/FileRefresher.cs`** -> AI Confidence: **99.31%**
15. **`Emby.Server.Implementations/IO/LibraryMonitor.cs`** -> AI Confidence: **99.31%**
16. **`Emby.Server.Implementations/ScheduledTasks/ScheduledTaskWorker.cs`** -> AI Confidence: **99.31%**
17. **`Emby.Server.Implementations/SyncPlay/SyncPlayManager.cs`** -> AI Confidence: **99.31%**
18. **`Emby.Server.Implementations/Updates/InstallationManager.cs`** -> AI Confidence: **99.31%**
19. **`Jellyfin.Api/Auth/SyncPlayAccessPolicy/SyncPlayAccessHandler.cs`** -> AI Confidence: **99.31%**
20. **`Jellyfin.Api/Controllers/ActivityLogController.cs`** -> AI Confidence: **99.31%**
21. **`Jellyfin.Api/Controllers/ArtistsController.cs`** -> AI Confidence: **99.31%**
22. **`Jellyfin.Api/Controllers/DynamicHlsController.cs`** -> AI Confidence: **99.31%**
23. **`Jellyfin.Api/Controllers/FilterController.cs`** -> AI Confidence: **99.31%**
24. **`Jellyfin.Api/Controllers/GenresController.cs`** -> AI Confidence: **99.31%**
25. **`Jellyfin.Api/Controllers/ImageController.cs`** -> AI Confidence: **99.31%**
26. **`Jellyfin.Api/Controllers/ItemUpdateController.cs`** -> AI Confidence: **99.31%**
27. **`Jellyfin.Api/Controllers/ItemsController.cs`** -> AI Confidence: **99.31%**
28. **`Jellyfin.Api/Controllers/PlaystateController.cs`** -> AI Confidence: **99.31%**
29. **`Jellyfin.Api/Controllers/SearchController.cs`** -> AI Confidence: **99.31%**
30. **`Jellyfin.Api/Controllers/TvShowsController.cs`** -> AI Confidence: **99.31%**
31. **`Jellyfin.Api/Controllers/UniversalAudioController.cs`** -> AI Confidence: **99.31%**
32. **`Jellyfin.Api/Controllers/VideosController.cs`** -> AI Confidence: **99.31%**
33. **`Jellyfin.Api/Helpers/DynamicHlsHelper.cs`** -> AI Confidence: **99.31%**
34. **`MediaBrowser.Common/Net/NetworkUtils.cs`** -> AI Confidence: **99.31%**
35. **`MediaBrowser.Controller/MediaEncoding/EncodingJobInfo.cs`** -> AI Confidence: **99.31%**
36. **`MediaBrowser.LocalMetadata/Parsers/PlaylistXmlParser.cs`** -> AI Confidence: **99.31%**
37. **`MediaBrowser.MediaEncoding/Probing/ProbeResultNormalizer.cs`** -> AI Confidence: **99.31%**
38. **`MediaBrowser.MediaEncoding/Transcoding/TranscodeManager.cs`** -> AI Confidence: **99.31%**
39. **`MediaBrowser.Model/Dlna/StreamBuilder.cs`** -> AI Confidence: **99.31%**
40. **`MediaBrowser.Model/Dlna/StreamInfo.cs`** -> AI Confidence: **99.31%**
41. **`MediaBrowser.Model/Dto/MediaSourceInfo.cs`** -> AI Confidence: **99.31%**
42. **`MediaBrowser.Model/Entities/MediaStream.cs`** -> AI Confidence: **99.31%**
43. **`MediaBrowser.Providers/Books/OpenPackagingFormat/OpfReader.cs`** -> AI Confidence: **99.31%**
44. **`MediaBrowser.Providers/Manager/ImageSaver.cs`** -> AI Confidence: **99.31%**
45. **`MediaBrowser.Providers/Manager/ItemImageProvider.cs`** -> AI Confidence: **99.31%**
46. **`MediaBrowser.Providers/Manager/MetadataService.cs`** -> AI Confidence: **99.31%**
47. **`MediaBrowser.Providers/MediaInfo/AudioFileProber.cs`** -> AI Confidence: **99.31%**
48. **`MediaBrowser.Providers/Plugins/Tmdb/Movies/TmdbMovieProvider.cs`** -> AI Confidence: **99.31%**
49. **`MediaBrowser.Providers/Plugins/Tmdb/TV/TmdbEpisodeProvider.cs`** -> AI Confidence: **99.31%**
50. **`MediaBrowser.Providers/Plugins/Tmdb/TV/TmdbSeriesProvider.cs`** -> AI Confidence: **99.31%**
51. **`MediaBrowser.Providers/Plugins/Tmdb/TmdbClientManager.cs`** -> AI Confidence: **99.31%**
52. **`MediaBrowser.Providers/Plugins/Tmdb/TmdbExternalUrlProvider.cs`** -> AI Confidence: **99.31%**
53. **`MediaBrowser.XbmcMetadata/Parsers/BaseNfoParser.cs`** -> AI Confidence: **99.31%**
54. **`MediaBrowser.XbmcMetadata/Parsers/EpisodeNfoParser.cs`** -> AI Confidence: **99.31%**
55. **`MediaBrowser.XbmcMetadata/Parsers/MovieNfoParser.cs`** -> AI Confidence: **99.31%**
56. **`MediaBrowser.XbmcMetadata/Parsers/SeriesNfoParser.cs`** -> AI Confidence: **99.31%**
57. **`src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/User.cs`** -> AI Confidence: **99.31%**
58. **`src/Jellyfin.Database/Jellyfin.Database.Implementations/QueryPartitionHelpers.cs`** -> AI Confidence: **99.31%**
59. **`src/Jellyfin.LiveTv/LiveTvDtoService.cs`** -> AI Confidence: **99.31%**
60. **`tests/Jellyfin.Model.Tests/Dlna/StreamBuilderTests.cs`** -> AI Confidence: **99.31%**
61. **`Emby.Naming/Book/BookFileNameParser.cs`** -> AI Confidence: **99.29%**
62. **`Emby.Naming/TV/EpisodeInfo.cs`** -> AI Confidence: **99.29%**
63. **`Jellyfin.Api/Models/MediaInfoDtos/PlaybackInfoDto.cs`** -> AI Confidence: **99.29%**
64. **`MediaBrowser.MediaEncoding/Probing/MediaFrameInfo.cs`** -> AI Confidence: **99.29%**
65. **`MediaBrowser.Model/Dto/UpdateUserItemDataDto.cs`** -> AI Confidence: **99.29%**
66. **`MediaBrowser.Model/Lyrics/LyricMetadata.cs`** -> AI Confidence: **99.29%**
67. **`MediaBrowser.Model/Search/SearchHint.cs`** -> AI Confidence: **99.29%**
68. **`src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/BaseItemEntity.cs`** -> AI Confidence: **99.29%**
69. **`src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/MediaStreamInfo.cs`** -> AI Confidence: **99.29%**
70. **`Emby.Photos/PhotoProvider.cs`** -> AI Confidence: **99.24%**
71. **`Emby.Server.Implementations/Collections/CollectionManager.cs`** -> AI Confidence: **99.24%**
72. **`Emby.Server.Implementations/Devices/DeviceId.cs`** -> AI Confidence: **99.24%**
73. **`Emby.Server.Implementations/EntryPoints/UserDataChangeNotifier.cs`** -> AI Confidence: **99.24%**
74. **`Emby.Server.Implementations/HttpServer/WebSocketConnection.cs`** -> AI Confidence: **99.24%**
75. **`Emby.Server.Implementations/IO/ManagedFileSystem.cs`** -> AI Confidence: **99.24%**
76. **`Emby.Server.Implementations/Images/CollectionFolderImageProvider.cs`** -> AI Confidence: **99.24%**
77. **`Emby.Server.Implementations/Localization/LocalizationManager.cs`** -> AI Confidence: **99.24%**
78. **`Emby.Server.Implementations/Playlists/PlaylistManager.cs`** -> AI Confidence: **99.24%**
79. **`Emby.Server.Implementations/Plugins/PluginManager.cs`** -> AI Confidence: **99.24%**
80. **`Emby.Server.Implementations/Session/SessionManager.cs`** -> AI Confidence: **99.24%**
81. **`Emby.Server.Implementations/Session/WebSocketController.cs`** -> AI Confidence: **99.24%**
82. **`Emby.Server.Implementations/TV/TVSeriesManager.cs`** -> AI Confidence: **99.24%**
83. **`Jellyfin.Api/Controllers/InstantMixController.cs`** -> AI Confidence: **99.24%**
84. **`Jellyfin.Api/Controllers/MusicGenresController.cs`** -> AI Confidence: **99.24%**
85. **`Jellyfin.Server.Implementations/Extensions/ServiceCollectionExtensions.cs`** -> AI Confidence: **99.24%**
86. **`Jellyfin.Server/Filters/CachingOpenApiProvider.cs`** -> AI Confidence: **99.24%**
87. **`Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs`** -> AI Confidence: **99.24%**
88. **`Jellyfin.Server/Migrations/Routines/MoveExtractedFiles.cs`** -> AI Confidence: **99.24%**
89. **`MediaBrowser.Controller/Entities/Folder.cs`** -> AI Confidence: **99.24%**
90. **`MediaBrowser.Controller/Entities/TV/Episode.cs`** -> AI Confidence: **99.24%**
91. **`MediaBrowser.Controller/Entities/UserViewBuilder.cs`** -> AI Confidence: **99.24%**
92. **`MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs`** -> AI Confidence: **99.24%**
93. **`MediaBrowser.Controller/MediaEncoding/IMediaEncoder.cs`** -> AI Confidence: **99.24%**
94. **`MediaBrowser.Controller/MediaEncoding/TranscodingSegmentCleaner.cs`** -> AI Confidence: **99.24%**
95. **`MediaBrowser.Controller/Session/SessionInfo.cs`** -> AI Confidence: **99.24%**
96. **`MediaBrowser.LocalMetadata/Images/LocalImageProvider.cs`** -> AI Confidence: **99.24%**
97. **`MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs`** -> AI Confidence: **99.24%**
98. **`MediaBrowser.MediaEncoding/Subtitles/SubtitleEncoder.cs`** -> AI Confidence: **99.24%**
99. **`MediaBrowser.Providers/MediaInfo/FFProbeVideoInfo.cs`** -> AI Confidence: **99.24%**
100. **`src/Jellyfin.Drawing.Skia/SkiaEncoder.cs`** -> AI Confidence: **99.24%**
101. **`src/Jellyfin.Drawing/ImageProcessor.cs`** -> AI Confidence: **99.24%**
102. **`src/Jellyfin.LiveTv/Channels/ChannelManager.cs`** -> AI Confidence: **99.24%**
103. **`src/Jellyfin.LiveTv/DefaultLiveTvService.cs`** -> AI Confidence: **99.24%**
104. **`src/Jellyfin.LiveTv/Guide/GuideManager.cs`** -> AI Confidence: **99.24%**
105. **`src/Jellyfin.LiveTv/IO/EncodedRecorder.cs`** -> AI Confidence: **99.24%**
106. **`src/Jellyfin.LiveTv/LiveTvMediaSourceProvider.cs`** -> AI Confidence: **99.24%**
107. **`src/Jellyfin.LiveTv/Recordings/RecordingsManager.cs`** -> AI Confidence: **99.24%**
108. **`src/Jellyfin.LiveTv/Timers/TimerManager.cs`** -> AI Confidence: **99.24%**
109. **`src/Jellyfin.LiveTv/TunerHosts/LiveStream.cs`** -> AI Confidence: **99.24%**
110. **`src/Jellyfin.Networking/Manager/NetworkManager.cs`** -> AI Confidence: **99.24%**
111. **`tests/Jellyfin.Providers.Tests/Manager/ProviderManagerTests.cs`** -> AI Confidence: **99.24%**
112. **`Jellyfin.Server/Filters/SecurityRequirementsOperationFilter.cs`** -> AI Confidence: **99.23%**
113. **`Jellyfin.Server/Migrations/Stages/CodeMigration.cs`** -> AI Confidence: **99.23%**
114. **`MediaBrowser.Controller/MediaEncoding/TranscodingThrottler.cs`** -> AI Confidence: **99.23%**
115. **`MediaBrowser.Controller/Streaming/ProgressiveFileStream.cs`** -> AI Confidence: **99.23%**
116. **`MediaBrowser.MediaEncoding/Encoder/EncoderValidator.cs`** -> AI Confidence: **99.23%**
117. **`MediaBrowser.XbmcMetadata/Parsers/SeasonNfoParser.cs`** -> AI Confidence: **99.23%**
118. **`src/Jellyfin.Database/Jellyfin.Database.Implementations/Locking/PessimisticLockBehavior.cs`** -> AI Confidence: **99.23%**
119. **`MediaBrowser.Model/LiveTv/LiveTvChannelQuery.cs`** -> AI Confidence: **99.2%**
120. **`MediaBrowser.Model/LiveTv/RecordingQuery.cs`** -> AI Confidence: **99.2%**
121. **`src/Jellyfin.LiveTv/Listings/SchedulesDirectDtos/ProgramDetailsDto.cs`** -> AI Confidence: **99.2%**
122. **`Emby.Server.Implementations/ApplicationHost.cs`** -> AI Confidence: **99.18%**
123. **`Emby.Server.Implementations/Collections/CollectionImageProvider.cs`** -> AI Confidence: **99.18%**
124. **`Emby.Server.Implementations/Configuration/ServerConfigurationManager.cs`** -> AI Confidence: **99.18%**
125. **`Emby.Server.Implementations/Data/CleanDatabaseScheduledTask.cs`** -> AI Confidence: **99.18%**
126. **`Emby.Server.Implementations/Images/BaseDynamicImageProvider.cs`** -> AI Confidence: **99.18%**
127. **`Emby.Server.Implementations/Images/DynamicImageProvider.cs`** -> AI Confidence: **99.18%**
128. **`Emby.Server.Implementations/Images/PlaylistImageProvider.cs`** -> AI Confidence: **99.18%**
129. **`Emby.Server.Implementations/ScheduledTasks/Tasks/ChapterImagesTask.cs`** -> AI Confidence: **99.18%**
130. **`Emby.Server.Implementations/ScheduledTasks/Tasks/CleanupCollectionAndPlaylistPathsTask.cs`** -> AI Confidence: **99.18%**
131. **`Emby.Server.Implementations/ScheduledTasks/Tasks/PluginUpdateTask.cs`** -> AI Confidence: **99.18%**
132. **`Jellyfin.Api/Auth/DefaultAuthorizationPolicy/DefaultAuthorizationHandler.cs`** -> AI Confidence: **99.18%**
133. **`Jellyfin.Api/Controllers/HlsSegmentController.cs`** -> AI Confidence: **99.18%**
134. **`Jellyfin.Api/Controllers/MoviesController.cs`** -> AI Confidence: **99.18%**
135. **`Jellyfin.Api/Controllers/PackageController.cs`** -> AI Confidence: **99.18%**
136. **`Jellyfin.Api/Controllers/PluginsController.cs`** -> AI Confidence: **99.18%**
137. **`Jellyfin.Api/Controllers/QuickConnectController.cs`** -> AI Confidence: **99.18%**
138. **`Jellyfin.Api/Controllers/RemoteImageController.cs`** -> AI Confidence: **99.18%**
139. **`Jellyfin.Api/Controllers/SessionController.cs`** -> AI Confidence: **99.18%**
140. **`Jellyfin.Api/Controllers/StartupController.cs`** -> AI Confidence: **99.18%**
141. **`Jellyfin.Api/Controllers/SuggestionsController.cs`** -> AI Confidence: **99.18%**
142. **`Jellyfin.Api/Controllers/TrickplayController.cs`** -> AI Confidence: **99.18%**
143. **`Jellyfin.Api/Controllers/UserViewsController.cs`** -> AI Confidence: **99.18%**
144. **`Jellyfin.Api/Helpers/RequestHelpers.cs`** -> AI Confidence: **99.18%**
145. **`Jellyfin.Api/Middleware/ExceptionMiddleware.cs`** -> AI Confidence: **99.18%**
146. **`Jellyfin.Server.Implementations/Devices/DeviceManager.cs`** -> AI Confidence: **99.18%**
147. **`Jellyfin.Server.Implementations/Item/BaseItemRepository.cs`** -> AI Confidence: **99.18%**
148. **`Jellyfin.Server.Implementations/Item/PeopleRepository.cs`** -> AI Confidence: **99.18%**
149. **`Jellyfin.Server.Implementations/Users/DefaultPasswordResetProvider.cs`** -> AI Confidence: **99.18%**
150. **`Jellyfin.Server/Extensions/ApiServiceCollectionExtensions.cs`** -> AI Confidence: **99.18%**
151. **`Jellyfin.Server/Migrations/PreStartupRoutines/MigrateEncodingOptions.cs`** -> AI Confidence: **99.18%**
152. **`Jellyfin.Server/Migrations/Routines/FixPlaylistOwner.cs`** -> AI Confidence: **99.18%**
153. **`Jellyfin.Server/Migrations/Routines/MigrateLibraryUserData.cs`** -> AI Confidence: **99.18%**
154. **`Jellyfin.Server/Migrations/Routines/MoveTrickplayFiles.cs`** -> AI Confidence: **99.18%**
155. **`Jellyfin.Server/Migrations/Routines/RefreshCleanNames.cs`** -> AI Confidence: **99.18%**
156. **`Jellyfin.Server/Migrations/Routines/RefreshInternalDateModified.cs`** -> AI Confidence: **99.18%**
157. **`Jellyfin.Server/Migrations/Routines/RemoveDuplicateExtras.cs`** -> AI Confidence: **99.18%**
158. **`Jellyfin.Server/Migrations/Routines/ReseedFolderFlag.cs`** -> AI Confidence: **99.18%**
159. **`Jellyfin.Server/Program.cs`** -> AI Confidence: **99.18%**
160. **`MediaBrowser.Common/Net/INetworkManager.cs`** -> AI Confidence: **99.18%**
161. **`MediaBrowser.Common/Plugins/BasePluginOfT.cs`** -> AI Confidence: **99.18%**
162. **`MediaBrowser.Controller/Devices/IDeviceManager.cs`** -> AI Confidence: **99.18%**
163. **`MediaBrowser.Controller/Entities/Audio/Audio.cs`** -> AI Confidence: **99.18%**
164. **`MediaBrowser.Controller/Entities/Audio/MusicAlbum.cs`** -> AI Confidence: **99.18%**
165. **`MediaBrowser.Controller/Entities/CollectionFolder.cs`** -> AI Confidence: **99.18%**
166. **`MediaBrowser.Controller/Entities/Movies/Movie.cs`** -> AI Confidence: **99.18%**
167. **`MediaBrowser.Controller/Entities/TV/Season.cs`** -> AI Confidence: **99.18%**
168. **`MediaBrowser.Controller/Entities/Trailer.cs`** -> AI Confidence: **99.18%**
169. **`MediaBrowser.Controller/Providers/IProviderManager.cs`** -> AI Confidence: **99.18%**
170. **`MediaBrowser.LocalMetadata/Images/EpisodeLocalImageProvider.cs`** -> AI Confidence: **99.18%**
171. **`MediaBrowser.Providers/Books/OpenPackagingFormat/EpubProvider.cs`** -> AI Confidence: **99.18%**
172. **`MediaBrowser.Providers/Lyric/LyricScheduledTask.cs`** -> AI Confidence: **99.18%**
173. **`MediaBrowser.Providers/MediaInfo/EmbeddedImageProvider.cs`** -> AI Confidence: **99.18%**
174. **`MediaBrowser.Providers/MediaInfo/ProbeProvider.cs`** -> AI Confidence: **99.18%**
175. **`MediaBrowser.Providers/MediaInfo/SubtitleScheduledTask.cs`** -> AI Confidence: **99.18%**
176. **`MediaBrowser.Providers/MediaInfo/VideoImageProvider.cs`** -> AI Confidence: **99.18%**
177. **`MediaBrowser.Providers/Music/AlbumMetadataService.cs`** -> AI Confidence: **99.18%**
178. **`MediaBrowser.Providers/Music/AudioMetadataService.cs`** -> AI Confidence: **99.18%**
179. **`MediaBrowser.Providers/Playlists/PlaylistItemsProvider.cs`** -> AI Confidence: **99.18%**
180. **`MediaBrowser.Providers/Plugins/AudioDb/AudioDbArtistImageProvider.cs`** -> AI Confidence: **99.18%**
181. **`MediaBrowser.Providers/Plugins/AudioDb/AudioDbArtistProvider.cs`** -> AI Confidence: **99.18%**
182. **`MediaBrowser.Providers/Plugins/Omdb/OmdbItemProvider.cs`** -> AI Confidence: **99.18%**
183. **`MediaBrowser.Providers/Plugins/Omdb/OmdbProvider.cs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `MediaBrowser.XbmcMetadata/Savers/BaseNfoSaver.cs` -> **0.0128%** Exposure
- `tests/Jellyfin.MediaEncoding.Tests/Probing/ProbeResultNormalizerTests.cs` -> **0.0002%** Exposure
- `tests/Jellyfin.Providers.Tests/MediaInfo/MediaInfoResolverTests.cs` -> **0.0002%** Exposure
### Exploit Generation Surface
- `Emby.Naming/Audio/AlbumParser.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookFileInfo.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookFilePathParser.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookInfo.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookListResolver.cs` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `Emby.Server.Implementations/Data/SqliteExtensions.cs` -> **100.0%** Exposure
- `Emby.Server.Implementations/ScheduledTasks/TaskManager.cs` -> **100.0%** Exposure
- `Jellyfin.Server/Helpers/StartupHelpers.cs` -> **100.0%** Exposure
- `MediaBrowser.Providers/Plugins/MusicBrainz/MusicBrainzAlbumProvider.cs` -> **100.0%** Exposure
- `MediaBrowser.Providers/Plugins/MusicBrainz/MusicBrainzArtistProvider.cs` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `MediaBrowser.Providers/Plugins/Tmdb/TmdbUtils.cs` -> **97.7174%** Exposure
### Algorithmic DoS Exposure
- `Emby.Naming/Audio/AlbumParser.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookFileInfo.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookFilePathParser.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookInfo.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookListResolver.cs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10367` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `MediaBrowser.Providers/Plugins/MusicBrainz/MusicBrainzArtistProvider.cs` (CSHARP) -> Cumulative Risk: **949.22**
- **Archetype:** `file_cluster_13` (Distance: 11.478 IQR)
- **Magnitude:** 196.52 | **LOC:** 187 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `GetMetadata` (Impact: 32.8), `GetResultsFromResponse` (Impact: 27.4), `GetSearchResults` (Impact: 23.2)

### 2. `MediaBrowser.Providers/Plugins/Omdb/OmdbItemProvider.cs` (CSHARP) -> Cumulative Risk: **947.13**
- **Archetype:** `file_cluster_13` (Distance: 12.078 IQR)
- **Magnitude:** 366.64 | **LOC:** 313 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `GetSearchResultsInternal` (Impact: 151.4), `ResultToMetadataResult` (Impact: 26.6), `GetResult` (Impact: 8.8)

### 3. `Emby.Server.Implementations/Data/SqliteExtensions.cs` (CSHARP) -> Cumulative Risk: **927.9**
- **Archetype:** `file_cluster_8` (Distance: 11.655 IQR)
- **Magnitude:** 343.84 | **LOC:** 272 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `TryReadDateTime` (Impact: 37.3), `TryBind` (Impact: 29.0), `TryGetGuid` (Impact: 25.9)

### 4. `src/Jellyfin.LiveTv/TunerHosts/LiveStream.cs` (CSHARP) -> Cumulative Risk: **927.55**
- **Archetype:** `file_cluster_4` (Distance: 11.579 IQR)
- **Magnitude:** 253.92 | **LOC:** 177 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `DeleteTempFiles` (Impact: 53.0), `Dispose` (Impact: 37.1), `TrySeek` (Impact: 27.1)

### 5. `MediaBrowser.Providers/Plugins/AudioDb/AudioDbArtistImageProvider.cs` (CSHARP) -> Cumulative Risk: **925.17**
- **Archetype:** `file_cluster_13` (Distance: 12.434 IQR)
- **Magnitude:** 224.64 | **LOC:** 156 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `GetImages` (Impact: 61.7), `GetImages` (Impact: 50.3), `GetSupportedImages` (Impact: 6.1)

### 6. `src/Jellyfin.LiveTv/LiveTvManager.cs` (CSHARP) -> Cumulative Risk: **923.43**
- **Archetype:** `file_cluster_17` (Distance: 12.956 IQR)
- **Magnitude:** 1605.0 | **LOC:** 1293 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `GetEmbyRecordingsAsync` (Impact: 107.3), `AddRecordingInfo` (Impact: 86.5), `GetTimers` (Impact: 82.0)

### 7. `MediaBrowser.Providers/Plugins/AudioDb/AudioDbAlbumProvider.cs` (CSHARP) -> Cumulative Risk: **921.07**
- **Archetype:** `file_cluster_13` (Distance: 11.631 IQR)
- **Magnitude:** 317.64 | **LOC:** 304 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `ProcessResult` (Impact: 98.1), `GetMetadata` (Impact: 31.7), `DownloadInfo` (Impact: 14.2)

### 8. `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` (CSHARP) -> Cumulative Risk: **912.06**
- **Archetype:** `file_cluster_13` (Distance: 12.814 IQR)
- **Magnitude:** 2103.46 | **LOC:** 1400 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `ExtractImageInternal` (Impact: 356.1), `ExtractVideoImagesOnIntervalAccelerated` (Impact: 317.8), `GetMediaInfoInternal` (Impact: 141.0)

### 9. `MediaBrowser.Providers/Plugins/AudioDb/AudioDbArtistProvider.cs` (CSHARP) -> Cumulative Risk: **907.63**
- **Archetype:** `file_cluster_13` (Distance: 12.185 IQR)
- **Magnitude:** 304.3 | **LOC:** 291 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `ProcessResult` (Impact: 82.3), `GetMetadata` (Impact: 31.7), `DownloadArtistInfo` (Impact: 9.6)

### 10. `Jellyfin.Server.Implementations/Activity/ActivityManager.cs` (CSHARP) -> Cumulative Risk: **905.42**
- **Archetype:** `file_cluster_13` (Distance: 13.143 IQR)
- **Magnitude:** 346.22 | **LOC:** 214 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `GetPagedResultAsync` (Impact: 158.5), `ApplyOrdering` (Impact: 49.5), `MapOrderBy` (Impact: 11.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.9 IQR)
- **Top Global Matches:** file_cluster_8: 12.9, file_cluster_13: 13.161, file_cluster_7: 13.214
- **Magnitude:** 5750.7 | **LOC:** 7852 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (24.4893%), Tech Debt (27.7337%)
**Top Internal Functions/Classes:**
  * `GetRkmppVidFiltersPrefered` (Impact: 489.0 | O(N^6) | DB: 24)
  * `GetVideoBitrateParam` (Impact: 346.7 | O(N^6) | DB: 6)
  * `GetVaapiLimitedVidFiltersPrefered` (Impact: 297.1 | O(N^6) | DB: 28)
  * `GetAmdDx11VidFiltersPrefered` (Impact: 275.6 | O(N^6) | DB: 31)
  * `GetNvidiaVidFiltersPrefered` (Impact: 274.8 | O(N^6) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 690`, `structural_boundaries: 801`, `args: 140`, `func_start: 335`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 610`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 24`
* *Architecture:* `io: 7`, `api: 59`, `import: 22`
* *Defense:* `safety: 131`, `doc: 110`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` System.Runtime.InteropServices, System.Collections.Generic, MediaBrowser.Model.Dlna, MediaBrowser.Model.Dto, System.IO, MediaBrowser.Controller.IO, Jellyfin.Extensions, MediaBrowser.Model.Configuration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Controllers/ImageController.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.359 IQR)
- **Top Global Matches:** file_cluster_0: 13.359, file_cluster_13: 13.752, file_cluster_4: 13.816
- **Magnitude:** 3666.96 | **LOC:** 2070 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (28.02%), Tech Debt (30.9554%)
**Top Internal Functions/Classes:**
  * `GetImageInternal` (Impact: 429.8 | O(N^4) | DB: 24)
    * *Intent:* /// <summary> /// Get user profile image. /// </summary> /// <param name="userId">User id.</param> /...
  * `GetItemImage` (Impact: 197.3 | O(N^4))
    * *Intent:* /// <summary> /// Delete the user's image. /// </summary> /// <param name="userId">User Id.</param> ...
  * `GetGenreImage` (Impact: 197.3 | O(N^4))
  * `GetMusicGenreImage` (Impact: 197.3 | O(N^4))
  * `GetPersonImage` (Impact: 197.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 171`, `args: 62`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `state_mutation: 182`, `dead_code: 2`, `orphaned_logic: 20`
* *Architecture:* `io: 8`, `api: 27`, `concurrency: 95`, `import: 35`
* *Defense:* `safety: 43`, `doc: 430`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.IO, System.Threading.Tasks, System.Collections.Immutable, Microsoft.AspNetCore.Authorization, MediaBrowser.Model.Drawing, MediaBrowser.Model.Dto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Controllers/MediaInfoController.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.494 IQR)
- **Top Global Matches:** file_cluster_0: 15.494, file_cluster_13: 15.575, file_cluster_4: 15.69
- **Magnitude:** 3518.9 | **LOC:** 345 | **CtrlFlow:** 72.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (48.34%), Tech Debt (27.5003%)
**Top Internal Functions/Classes:**
  * `GetPostedPlaybackInfo` (Impact: 2976.5 | O(2^N) | DB: 16)
    * *Intent:* /// <param name="subtitleStreamIndex">The subtitle stream index.</param> /// <param name="maxAudioCh...
  * `OpenLiveStream` (Impact: 338.6 | O(N^3) | DB: 15)
    * *Intent:* /// <param name="userId">The user id.</param> /// <param name="playSessionId">The play session id.</...
  * `GetPlaybackInfo` (Impact: 32.9 | O(2^N) | DB: 1)
    * *Intent:* /// <summary> /// Gets live playback media info for an item. /// </summary> /// <param name="itemId"...
  * `GetBitrateTestBytes` (Impact: 24.8 | O(N^3))
    * *Intent:* /// <summary> /// Tests the network with a request with the size of the bitrate. /// </summary> /// ...
  * `MediaInfoController` (Impact: 8.7 | O(2^N) | DB: 6)
    * *Intent:* /// <summary> /// Initializes a new instance of the <see cref="MediaInfoController"/> class. /// </s...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 48`, `args: 11`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 92`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 7`, `concurrency: 28`, `import: 21`
* *Defense:* `safety: 86`, `doc: 76`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Microsoft.AspNetCore.Mvc.ModelBinding, System.Threading.Tasks, Microsoft.AspNetCore.Authorization, Microsoft.AspNetCore.Http, Jellyfin.Extensions, MediaBrowser.Controller.Library, MediaBrowser.Controller.Devices, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Emby.Server.Implementations/Session/SessionManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.793 IQR)
- **Top Global Matches:** file_cluster_4: 13.793, file_cluster_13: 13.804, file_cluster_8: 13.844
- **Magnitude:** 3257.9 | **LOC:** 2155 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (35.3013%), Tech Debt (69.2683%)
**Top Internal Functions/Classes:**
  * `OnPlaybackStopped` (Impact: 313.8 | O(2^N) | DB: 13)
    * *Intent:* /// <summary> /// Used to report that playback has ended for an item. /// </summary> /// <param name...
  * `GetSessions` (Impact: 257.8 | O(N^6) | DB: 16)
    * *Intent:* /// <inheritdoc/>
  * `SendPlayCommand` (Impact: 137.2 | O(N^6) | DB: 3)
    * *Intent:* /// <inheritdoc />
  * `OnPlaybackStart` (Impact: 135.9 | O(2^N) | DB: 10)
    * *Intent:* /// <summary> /// Used to report that playback has started for an item. /// </summary> /// <param na...
  * `UpdateNowPlayingItem` (Impact: 129.4 | O(N^6) | DB: 2)
    * *Intent:* /// <summary> /// Updates the now playing item id. /// </summary> /// <returns>Task.</returns>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 301`, `args: 138`, `func_start: 271`, `class_start: 1`
* *Risk/State:* `state_mutation: 373`, `duplicate_logic: 15`, `orphaned_logic: 16`
* *Architecture:* `api: 52`, `concurrency: 189`, `import: 39`
* *Defense:* `safety: 111`, `doc: 165`, `immutability_locks: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Controller.Net, MediaBrowser.Model.Querying, MediaBrowser.Model.SyncPlay, MediaBrowser.Controller.Entities.TV.Episode, MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.Library, Jellyfin.Data.Events...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.814 IQR)
- **Top Global Matches:** file_cluster_13: 12.814, file_cluster_8: 12.911, file_cluster_11: 13.111
- **Magnitude:** 2103.46 | **LOC:** 1400 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (35.649%), Tech Debt (97.9921%)
**Top Internal Functions/Classes:**
  * `ExtractImageInternal` (Impact: 356.1 | O(N^6) | DB: 31)
  * `ExtractVideoImagesOnIntervalAccelerated` (Impact: 317.8 | O(N^6) | DB: 10)
    * *Intent:* /// <inheritdoc />
  * `GetMediaInfoInternal` (Impact: 141.0 | O(N^6) | DB: 11)
    * *Intent:* /// <summary> /// Gets the media info internal. /// </summary> /// <returns>Task{MediaInfoResult}.</...
  * `SetFFmpegPath` (Impact: 138.3 | O(N^6) | DB: 16)
    * *Intent:* /// <summary> /// Run at startup to validate ffmpeg. /// Sets global variables FFmpegPath. /// Prece...
  * `ExtractImage` (Impact: 91.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 199`, `args: 104`, `func_start: 140`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 220`, `planned_debt: 2`, `duplicate_logic: 11`, `orphaned_logic: 14`
* *Architecture:* `io: 8`, `api: 55`, `concurrency: 34`, `import: 32`
* *Defense:* `safety: 45`, `doc: 58`, `sync_locks: 4`, `immutability_locks: 16`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.MediaEncoding.Probing, MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.Dlna, MediaBrowser.Model.IO, System.Threading.Tasks, MediaBrowser.Controller.MediaEncoding, MediaBrowser.Model.Drawing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Model/Dlna/StreamBuilder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.698 IQR)
- **Top Global Matches:** file_cluster_8: 12.698, file_cluster_13: 12.879, file_cluster_17: 12.891
- **Magnitude:** 2092.72 | **LOC:** 2400 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (30.1339%), Tech Debt (26.5395%)
**Top Internal Functions/Classes:**
  * `GetAudioDirectPlayProfile` (Impact: 1047.3 | O(N^6) | DB: 21)
  * `GetTranscodeReasonForFailedCondition` (Impact: 210.2 | O(N^5))
  * `GetOptimalAudioStream` (Impact: 199.0 | O(N^6) | DB: 9)
  * `CheckVideoConditions` (Impact: 137.2 | O(N^3))
    * *Intent:* // Reverse codec profiles for backward compatibility - first codec profile has higher priority
  * `GetOptimalAudioStream` (Impact: 135.4 | O(2^N) | DB: 1)
    * *Intent:* /// <summary> /// Gets the optimal audio stream. /// </summary> /// <param name="options">The <see c...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 184`, `args: 64`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 105`, `planned_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 11`, `import: 12`
* *Defense:* `safety: 105`, `doc: 76`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Model.Dto, MediaBrowser.Model.MediaInfo, System, Jellyfin.Data.Enums, MediaBrowser.Model.Entities, MediaBrowser.Model.Session, System.Collections.Generic, MediaBrowser.Model.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Emby.Server.Implementations/Dto/DtoService.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.741 IQR)
- **Top Global Matches:** file_cluster_17: 12.741, file_cluster_8: 12.806, file_cluster_13: 12.83
- **Magnitude:** 2071.78 | **LOC:** 1512 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (19.7821%), Tech Debt (22.4815%)
**Top Internal Functions/Classes:**
  * `GetChildCount` (Impact: 1227.8 | O(N^6) | DB: 28)
  * `GetBaseItemDtoInternal` (Impact: 159.1 | O(N^5) | DB: 1)
  * `GetBaseItemDtos` (Impact: 116.1 | O(N^5) | DB: 2)
    * *Intent:* /// <inheritdoc />
  * `AttachUserSpecificInfo` (Impact: 112.3 | O(N^6))
    * *Intent:* /// <summary> /// Attaches the user specific info. /// </summary>
  * `NormalizeMediaSourceContainers` (Impact: 104.9 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 183`, `args: 83`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 107`, `dead_code: 5`, `planned_debt: 3`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 19`, `import: 25`
* *Defense:* `safety: 128`, `doc: 28`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MediaBrowser.Model.Querying, MediaBrowser.Controller.Entities.TV.Episode, MediaBrowser.Controller.Entities.TV.Series, System.Collections.Generic, MediaBrowser.Controller.Entities.Photo, MediaBrowser.Controller.Entities.Movies.Movie, MediaBrowser.Controller.Entities.Person, MediaBrowser.Model.Dto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.129 IQR)
- **Top Global Matches:** file_cluster_8: 13.129, file_cluster_13: 13.173, file_cluster_17: 13.385
- **Magnitude:** 1837.64 | **LOC:** 1483 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 54.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (68.3417%), Tech Debt (19.6849%)
**Top Internal Functions/Classes:**
  * `GetItem` (Impact: 420.7 | O(N^5) | DB: 88)
  * `Perform` (Impact: 405.9 | O(N^6) | DB: 44)
    * *Intent:* /// <inheritdoc/>
  * `GetMediaStream` (Impact: 176.1 | O(N^3) | DB: 49)
    * *Intent:* /// <summary> /// Gets the media stream. /// </summary> /// <param name="reader">The reader.</param>...
  * `GetUserData` (Impact: 37.6 | O(N^3) | DB: 15)
  * `GetMediaAttachment` (Impact: 28.6 | O(N^3) | DB: 8)
    * *Intent:* /// <summary> /// Gets the attachment. /// </summary> /// <param name="reader">The reader.</param> /...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 272`, `args: 38`, `func_start: 114`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 616`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 11`, `import: 21`
* *Defense:* `safety: 7`, `doc: 26`, `immutability_locks: 15`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Data, System.Collections.Generic, Jellyfin.Server.ServerSetupApp, Jellyfin.Database.Implementations, System.Collections.Immutable, Microsoft.Data.Sqlite, System.IO, Jellyfin.Database.Implementations.Entities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Controller/Entities/BaseItem.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.225 IQR)
- **Top Global Matches:** file_cluster_0: 13.225, file_cluster_13: 13.305, file_cluster_11: 13.451
- **Magnitude:** 1740.54 | **LOC:** 2689 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (24.7842%), Tech Debt (57.5612%)
**Top Internal Functions/Classes:**
  * `GetVersionInfo` (Impact: 881.1 | O(N^6) | DB: 46)
  * `GetCustomRatingForComparision` (Impact: 67.1 | O(2^N) | DB: 1)
    * *Intent:* /// <summary> /// Gets or sets the run time ticks.
  * `GetMediaSources` (Impact: 61.8 | O(N^6))
  * `CreateSortName` (Impact: 55.9 | O(N^5) | DB: 7)
    * *Intent:* /// <summary>
  * `ModifySortChunks` (Impact: 46.2 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 312`, `args: 153`, `func_start: 165`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 192`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 7`, `orphaned_logic: 7`
* *Architecture:* `io: 9`, `api: 163`, `concurrency: 41`, `import: 34`
* *Defense:* `safety: 67`, `doc: 231`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.472
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.Library, MediaBrowser.Model.IO, System.Threading.Tasks, System.Collections.Immutable, MediaBrowser.Model.Dto, MediaBrowser.Controller.Persistence...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `MediaBrowser.LocalMetadata/Parsers/BaseItemXmlParser.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.977 IQR)
- **Top Global Matches:** file_cluster_8: 10.977, file_cluster_13: 11.255, file_cluster_7: 11.283
- **Magnitude:** 1668.88 | **LOC:** 873 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (14.1134%), Tech Debt (16.3944%)
**Top Internal Functions/Classes:**
  * `FetchDataFromXmlNode` (Impact: 849.9 | O(N^6) | DB: 11)
    * *Intent:* /// <summary> /// Fetches metadata from one Xml Element. /// </summary> /// <param name="reader">The...
  * `GetShare` (Impact: 111.5 | O(N^6) | DB: 3)
    * *Intent:* /// <summary> /// Get share. /// </summary> /// <param name="reader">The xml reader.</param> /// <re...
  * `GetLinkedChild` (Impact: 103.7 | O(N^6))
    * *Intent:* /// <summary> /// Get linked child. /// </summary> /// <param name="reader">The xml reader.</param> ...
  * `FetchFromSharesNode` (Impact: 81.3 | O(N^6) | DB: 1)
  * `FetchDataFromPersonsNode` (Impact: 74.3 | O(N^6))
    * *Intent:* /// <summary> /// Fetches the data from persons node. /// </summary> /// <param name="reader">The re...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 93`, `args: 20`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 61`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 3`, `import: 16`
* *Defense:* `safety: 10`, `doc: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System, System.IO, Jellyfin.Data.Enums, MediaBrowser.Model.Entities, System.Threading, MediaBrowser.Controller.Extensions, System.Collections.Generic, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.LiveTv/LiveTvManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.956 IQR)
- **Top Global Matches:** file_cluster_17: 12.956, file_cluster_4: 12.971, file_cluster_13: 13.057
- **Magnitude:** 1605.0 | **LOC:** 1293 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (64.5917%), Tech Debt (81.8297%)
**Top Internal Functions/Classes:**
  * `GetEmbyRecordingsAsync` (Impact: 107.3 | O(N^5) | DB: 22)
  * `AddRecordingInfo` (Impact: 86.5 | O(N^6) | DB: 1)
  * `GetTimers` (Impact: 82.0 | O(N^5) | DB: 8)
  * `CreateTimer` (Impact: 74.3 | O(2^N) | DB: 3)
  * `GetTimersInternal` (Impact: 65.8 | O(N^5) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 311`, `args: 116`, `func_start: 108`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 278`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 12`
* *Architecture:* `api: 33`, `concurrency: 119`, `import: 26`
* *Defense:* `safety: 47`, `doc: 14`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MediaBrowser.Model.Querying, MediaBrowser.Controller.Configuration, System.Collections.Generic, Jellyfin.Data.Events, System.Threading.Tasks, MediaBrowser.Model.Dto, Jellyfin.LiveTv.Configuration, Jellyfin.Database.Implementations.Entities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Controller/Entities/UserViewBuilder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.007 IQR)
- **Top Global Matches:** file_cluster_8: 11.007, file_cluster_17: 11.175, file_cluster_13: 11.283
- **Magnitude:** 1503.6 | **LOC:** 1028 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (21.3478%), Tech Debt (20.844%)
**Top Internal Functions/Classes:**
  * `Filter` (Impact: 863.4 | O(N^6) | DB: 4)
  * `GetUserItems` (Impact: 184.1 | O(N^6))
  * `GetMediaFolders` (Impact: 73.8 | O(2^N))
  * `SortAndPage` (Impact: 46.1 | O(N^4) | DB: 3)
  * `GetMovieGenres` (Impact: 29.4 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 209`, `args: 85`, `func_start: 111`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `dead_code: 3`, `duplicate_logic: 3`, `orphaned_logic: 2`
* *Architecture:* `api: 8`, `import: 14`
* *Defense:* `safety: 37`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Model.Querying, MediaBrowser.Controller.Entities.TV.Episode, System, Jellyfin.Data.Enums, MediaBrowser.Model.Entities.MetadataProvider, Jellyfin.Extensions, MediaBrowser.Model.Entities, MediaBrowser.Controller.Entities.TV.Series...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Probing/ProbeResultNormalizer.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.247 IQR)
- **Top Global Matches:** file_cluster_8: 12.247, file_cluster_13: 12.379, file_cluster_17: 12.5
- **Magnitude:** 1421.88 | **LOC:** 1761 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 18.2%
- **Algorithmic:** O(N^6) | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (29.3072%), Tech Debt (15.0997%)
**Top Internal Functions/Classes:**
  * `FetchFromItunesInfo` (Impact: 803.5 | O(N^6) | DB: 40)
  * `GetMediaInfo` (Impact: 288.6 | O(N^6) | DB: 5)
    * *Intent:* /// <summary> /// Transforms a FFprobe response into its <see cref="MediaInfo"/> equivalent. /// </s...
  * `GetEstimatedAudioBitrate` (Impact: 99.3 | O(N^6))
  * `NormalizeFormat` (Impact: 87.2 | O(N^6))
  * `ProbeResultNormalizer` (Impact: 3.7 | O(N^3) | DB: 2)
    * *Intent:* /// <summary> /// Initializes a new instance of the <see cref="ProbeResultNormalizer"/> class. /// <...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 127`, `args: 41`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `state_mutation: 123`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 3`, `import: 17`
* *Defense:* `safety: 43`, `doc: 17`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MediaBrowser.Model.Dto, MediaBrowser.Model.MediaInfo, System, System.IO, Jellyfin.Data.Enums, System.Text.RegularExpressions, MediaBrowser.Model.Entities, MediaBrowser.Controller.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Helpers/StreamingHelpers.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.232 IQR)
- **Top Global Matches:** file_cluster_8: 11.232, file_cluster_13: 11.254, file_cluster_7: 11.56
- **Magnitude:** 1421.04 | **LOC:** 608 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (16.1024%), Tech Debt (12.4131%)
**Top Internal Functions/Classes:**
  * `ParseParams` (Impact: 944.4 | O(N^6) | DB: 1)
  * `GetStreamingState` (Impact: 309.5 | O(N^6) | DB: 13)
    * *Intent:* /// Gets the current streaming state. /// </summary> /// <param name="streamingRequest">The <see cre...
  * `GetOutputFileExtension` (Impact: 77.4 | O(N^4) | DB: 3)
  * `GetContainerFileExtension` (Impact: 25.2 | O(N^3))
  * `ParseStreamOptions` (Impact: 15.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 71`, `args: 8`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 9`, `import: 23`
* *Defense:* `safety: 31`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Controller.Streaming, MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.Dlna, System.Threading.Tasks, MediaBrowser.Controller.MediaEncoding, MediaBrowser.Model.Dto, Microsoft.AspNetCore.Http...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Providers/Plugins/Tmdb/TmdbClientManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.184 IQR)
- **Top Global Matches:** file_cluster_4: 14.184, file_cluster_13: 14.279, file_cluster_16: 14.495
- **Magnitude:** 1400.12 | **LOC:** 719 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (49.1106%), Tech Debt (84.7288%)
**Top Internal Functions/Classes:**
  * `GetSeriesGroupAsync` (Impact: 154.4 | O(N^4) | DB: 2)
    * *Intent:* /// <summary> /// Gets a tv show episode group from the TMDb API based on the show id and the displa...
  * `GetEpisodeAsync` (Impact: 145.9 | O(N^5) | DB: 4)
    * *Intent:* /// <summary> /// Gets a tv season from the TMDb API based on the tv show's TMDb id. /// </summary> ...
  * `GetMovieAsync` (Impact: 136.2 | O(2^N) | DB: 2)
    * *Intent:* /// <summary> /// Gets a movie from the TMDb API based on its TMDb id. /// </summary> /// <param nam...
  * `SearchCollectionAsync` (Impact: 112.9 | O(2^N) | DB: 1)
  * `GetCollectionAsync` (Impact: 111.4 | O(2^N) | DB: 2)
    * *Intent:* /// <summary> /// Gets a collection from the TMDb API based on its TMDb id. /// </summary> /// <para...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 100`, `args: 39`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `state_mutation: 84`, `duplicate_logic: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 19`, `concurrency: 111`, `import: 17`
* *Defense:* `safety: 37`, `doc: 142`, `immutability_locks: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` MediaBrowser.Model.Dto, System, MediaBrowser.Model.Entities, System.Threading, TMDbLib.Objects.People, System.Collections.Generic, TMDbLib.Objects.Movies, TMDbLib.Objects.Search...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Subtitles/SubtitleEncoder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.886 IQR)
- **Top Global Matches:** file_cluster_13: 12.886, file_cluster_4: 12.899, file_cluster_8: 12.923
- **Magnitude:** 1309.0 | **LOC:** 1054 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (31.2034%), Tech Debt (12.4329%)
**Top Internal Functions/Classes:**
  * `ConvertTextSubtitleToSrtInternal` (Impact: 185.8 | O(N^6) | DB: 26)
  * `ExtractSubtitlesForFile` (Impact: 177.7 | O(N^6) | DB: 15)
  * `ExtractTextSubtitleInternal` (Impact: 160.1 | O(N^5) | DB: 21)
  * `ExtractAllExtractableSubtitlesMKS` (Impact: 115.2 | O(N^6) | DB: 14)
  * `ExtractAllExtractableSubtitlesInternal` (Impact: 74.4 | O(N^5) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 149`, `args: 41`, `func_start: 110`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 129`, `orphaned_logic: 4`
* *Architecture:* `io: 19`, `api: 11`, `concurrency: 85`, `import: 27`
* *Defense:* `safety: 49`, `doc: 41`, `immutability_locks: 14`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.IO, System.Threading.Tasks, UtfUnknown, System.Net.Http, MediaBrowser.Controller.MediaEncoding, MediaBrowser.Model.Dto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Controllers/DynamicHlsController.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.581 IQR)
- **Top Global Matches:** file_cluster_0: 13.581, file_cluster_13: 13.608, file_cluster_4: 13.881
- **Magnitude:** 1281.86 | **LOC:** 2082 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (34.8155%), Tech Debt (31.211%)
**Top Internal Functions/Classes:**
  * `GetSegmentResult` (Impact: 379.9 | O(2^N) | DB: 13)
    * *Intent:* /// <param name="playSessionId">The play session id.</param> /// <param name="segmentContainer">The ...
  * `GetVideoArguments` (Impact: 185.9 | O(N^6) | DB: 1)
  * `GetAudioArguments` (Impact: 180.2 | O(N^5) | DB: 1)
  * `GetCommandLineArguments` (Impact: 93.4 | O(N^4) | DB: 18)
    * *Intent:* /// <param name="enableAutoStreamCopy">Whether or not to allow automatic stream copy if requested va...
  * `_transcodeManager.LockAsync` (Impact: 56.7 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 141`, `args: 30`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `state_mutation: 187`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 19`, `api: 4`, `concurrency: 27`, `import: 32`
* *Defense:* `safety: 61`, `doc: 88`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MediaBrowser.Controller.Streaming, MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.Dlna, MediaBrowser.Model.IO, System.Threading.Tasks, Jellyfin.Api.Models.StreamingDtos, Microsoft.AspNetCore.Authorization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Providers/Manager/ImageSaver.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.852 IQR)
- **Top Global Matches:** file_cluster_13: 12.852, file_cluster_8: 12.948, file_cluster_4: 13.034
- **Magnitude:** 1267.64 | **LOC:** 719 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (34.5991%), Tech Debt (50.3773%)
**Top Internal Functions/Classes:**
  * `GetStandardSavePath` (Impact: 437.2 | O(N^6) | DB: 47)
    * *Intent:* /// <summary> /// Gets the save path. /// </summary> /// <param name="item">The item.</param> /// <p...
  * `SaveImage` (Impact: 283.9 | O(N^6) | DB: 18)
  * `GetCompatibleSavePaths` (Impact: 146.0 | O(N^6) | DB: 31)
    * *Intent:* /// <summary> /// Gets the compatible save paths. /// </summary> /// <param name="item">The item.</p...
  * `SaveImageToLocation` (Impact: 109.3 | O(2^N))
  * `SaveImageToLocation` (Impact: 32.0 | O(N^5) | DB: 9)
    * *Intent:* /// <summary> /// Saves the image to location. /// </summary> /// <param name="source">The source.</...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 120`, `args: 25`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 75`, `duplicate_logic: 5`
* *Architecture:* `io: 31`, `api: 5`, `concurrency: 28`, `import: 19`
* *Defense:* `safety: 46`, `doc: 97`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MediaBrowser.Controller.Entities.TV.Episode, MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.IO, System.Threading.Tasks, MediaBrowser.Controller.Entities.Person, System.IO, MediaBrowser.Controller.Entities.TV.Season...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.LiveTv/Channels/ChannelManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.407 IQR)
- **Top Global Matches:** file_cluster_13: 13.407, file_cluster_4: 13.476, file_cluster_17: 13.539
- **Magnitude:** 1240.9 | **LOC:** 1216 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (44.9854%), Tech Debt (92.9248%)
**Top Internal Functions/Classes:**
  * `GetChannelItemEntityAsync` (Impact: 334.1 | O(N^5) | DB: 27)
  * `GetChannelsInternalAsync` (Impact: 202.6 | O(N^6) | DB: 6)
    * *Intent:* /// <inheritdoc />
  * `Dispose` (Impact: 49.7 | O(2^N) | DB: 1)
  * `DeleteItem` (Impact: 45.6 | O(2^N))
    * *Intent:* /// <inheritdoc />
  * `GetChannel` (Impact: 39.9 | O(N^5) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 166`, `args: 72`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `state_mutation: 147`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 5`, `orphaned_logic: 8`
* *Architecture:* `io: 6`, `api: 18`, `concurrency: 76`, `import: 29`
* *Defense:* `safety: 59`, `doc: 53`, `immutability_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MediaBrowser.Model.Querying, MediaBrowser.Controller.Entities.TV.Episode, MediaBrowser.Controller.Entities.TV.Series, MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.Channels, MediaBrowser.Controller.Entities.Movies.Movie, MediaBrowser.Model.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Model/Dlna/ConditionProcessor.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.673 IQR)
- **Top Global Matches:** file_cluster_8: 10.673, file_cluster_7: 10.905, file_cluster_13: 11.082
- **Magnitude:** 1213.62 | **LOC:** 386 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (15.6752%), Tech Debt (98.0524%)
**Top Internal Functions/Classes:**
  * `IsVideoConditionSatisfied` (Impact: 513.0 | O(N^5))
    * *Intent:* /// <param name="videoRangeType">The <see cref="VideoRangeType"/>.</param> /// <param name="videoLev...
  * `IsVideoAudioConditionSatisfied` (Impact: 128.6 | O(N^5))
    * *Intent:* /// <summary> /// Checks if an audio condition is satisfied for a video. /// </summary> /// <param n...
  * `IsConditionSatisfied` (Impact: 123.4 | O(2^N) | DB: 3)
  * `IsAudioConditionSatisfied` (Impact: 81.6 | O(N^5))
    * *Intent:* /// <summary> /// Checks if an audio condition is satisfied. /// </summary> /// <param name="conditi...
  * `IsConditionSatisfied` (Impact: 80.9 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 84`, `args: 43`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `duplicate_logic: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Model.MediaInfo, System, Jellyfin.Data.Enums, System.Globalization, Jellyfin.Extensions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Controller/Entities/Folder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.768 IQR)
- **Top Global Matches:** file_cluster_13: 12.768, file_cluster_8: 12.892, file_cluster_0: 12.987
- **Magnitude:** 1171.7 | **LOC:** 1882 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 46.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (18.0214%), Tech Debt (31.472%)
**Top Internal Functions/Classes:**
  * `RequiresPostFiltering` (Impact: 132.6 | O(N^5))
  * `IsLibraryFolderAccessible` (Impact: 86.6 | O(N^6) | DB: 1)
  * `IsVisible` (Impact: 86.1 | O(2^N))
  * `FillUserDataDtoValues` (Impact: 79.3 | O(N^6) | DB: 8)
  * `QueryRecursive` (Impact: 56.1 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 170`, `args: 74`, `func_start: 107`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 111`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `api: 42`, `concurrency: 40`, `import: 28`
* *Defense:* `safety: 34`, `doc: 103`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MediaBrowser.Model.Querying, MediaBrowser.Controller.Entities.TV.Episode, MediaBrowser.Controller.LibraryTaskScheduler, MediaBrowser.Controller.Entities.TV.Series, MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.IO, System.Threading.Tasks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Emby.Server.Implementations/Playlists/PlaylistManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.622 IQR)
- **Top Global Matches:** file_cluster_4: 12.622, file_cluster_13: 12.628, file_cluster_17: 12.663
- **Magnitude:** 1120.92 | **LOC:** 689 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (59.0348%), Tech Debt (44.9379%)
**Top Internal Functions/Classes:**
  * `SavePlaylistFile` (Impact: 258.4 | O(N^6) | DB: 39)
    * *Intent:* /// <inheritdoc />
  * `CreatePlaylist` (Impact: 184.6 | O(N^6) | DB: 15)
  * `AddToPlaylistInternal` (Impact: 97.9 | O(N^6) | DB: 2)
  * `UpdatePlaylist` (Impact: 67.9 | O(N^5) | DB: 2)
  * `MoveItemAsync` (Impact: 63.9 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 141`, `args: 66`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 117`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 14`, `api: 16`, `concurrency: 56`, `import: 24`
* *Defense:* `safety: 39`, `doc: 4`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` System.Collections.Generic, MediaBrowser.Controller.Entities.Genre, MediaBrowser.Model.IO, System.Threading.Tasks, MediaBrowser.Model.Playlists, System.IO, MediaBrowser.Controller.Entities.Audio, Jellyfin.Database.Implementations.Entities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Providers/Manager/ItemImageProvider.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.066 IQR)
- **Top Global Matches:** file_cluster_13: 12.066, file_cluster_8: 12.093, file_cluster_4: 12.347
- **Magnitude:** 1118.08 | **LOC:** 750 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (16.9347%), Tech Debt (47.2454%)
**Top Internal Functions/Classes:**
  * `DownloadMultiImages` (Impact: 247.6 | O(N^6) | DB: 1)
  * `RefreshFromProvider` (Impact: 162.0 | O(N^6) | DB: 3)
    * *Intent:* /// <summary> /// Refreshes from a dynamic provider. /// </summary>
  * `RefreshFromProvider` (Impact: 140.1 | O(N^6) | DB: 5)
    * *Intent:* /// <summary> /// Refreshes from a remote provider. /// </summary> /// <param name="item">The item.<...
  * `DownloadImage` (Impact: 122.3 | O(N^6) | DB: 1)
  * `PruneImages` (Impact: 75.4 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 124`, `args: 29`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`, `duplicate_logic: 4`, `orphaned_logic: 3`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 31`, `import: 23`
* *Defense:* `safety: 36`, `doc: 57`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` System.Collections.Generic, MediaBrowser.Model.IO, System.Threading.Tasks, System.Net.Http, MediaBrowser.Model.Drawing, System.IO, MediaBrowser.Controller.Entities.Audio, MediaBrowser.Controller.Library...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.Networking/Manager/NetworkManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.468 IQR)
- **Top Global Matches:** file_cluster_13: 13.468, file_cluster_17: 13.558, file_cluster_8: 13.619
- **Magnitude:** 1086.38 | **LOC:** 1178 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (27.9402%), Tech Debt (63.4517%)
**Top Internal Functions/Classes:**
  * `InitializeOverrides` (Impact: 138.7 | O(N^6) | DB: 14)
    * *Intent:* /// <summary> /// Parses the user defined overrides into the dictionary object. /// Overrides are th...
  * `GetInterfacesCore` (Impact: 94.8 | O(N^6) | DB: 10)
    * *Intent:* /// <summary> /// Generate a list of all the interface ip addresses and submasks where that are in t...
  * `FilterBindSettings` (Impact: 89.0 | O(N^6) | DB: 4)
    * *Intent:* /// <summary> /// Filters a list of bind addresses and exclusions on available interfaces. /// </sum...
  * `GetBindAddress` (Impact: 73.5 | O(N^4) | DB: 8)
    * *Intent:* /// <inheritdoc/>
  * `GetAllBindInterfaces` (Impact: 68.1 | O(N^5) | DB: 3)
    * *Intent:* /// <summary> /// Reads the jellyfin configuration of the configuration manager and produces a list ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 150`, `args: 80`, `func_start: 110`, `class_start: 1`
* *Risk/State:* `state_mutation: 203`, `duplicate_logic: 7`, `orphaned_logic: 2`
* *Architecture:* `api: 22`, `concurrency: 1`, `import: 17`
* *Defense:* `safety: 29`, `doc: 124`, `sync_locks: 8`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` J2N.Collections.Generic.Extensions, System, Microsoft.AspNetCore.Http, Microsoft.Extensions.Configuration, System.Diagnostics.CodeAnalysis, MediaBrowser.Common.Net, System.Threading, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Transcoding/TranscodeManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.017 IQR)
- **Top Global Matches:** file_cluster_13: 12.017, file_cluster_8: 12.187, file_cluster_4: 12.429
- **Magnitude:** 1072.06 | **LOC:** 758 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (18.5223%), Tech Debt (23.6089%)
**Top Internal Functions/Classes:**
  * `StartFfMpeg` (Impact: 416.8 | O(2^N) | DB: 35)
  * `ReportTranscodingProgress` (Impact: 80.1 | O(N^4) | DB: 13)
  * `DeletePartialStreamFiles` (Impact: 79.9 | O(2^N))
  * `DeleteHlsPartialStreamFiles` (Impact: 71.9 | O(N^6) | DB: 7)
  * `PingTranscodingJob` (Impact: 35.9 | O(2^N) | DB: 1)
    * *Intent:* /// <inheritdoc />
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 89`, `args: 35`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `state_mutation: 82`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 11`, `api: 11`, `concurrency: 25`, `import: 29`
* *Defense:* `safety: 27`, `doc: 28`, `sync_locks: 6`, `immutability_locks: 14`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MediaBrowser.Controller.Streaming, MediaBrowser.Controller.Configuration, System.Collections.Generic, MediaBrowser.Model.Dlna, MediaBrowser.Model.IO, System.Threading.Tasks, MediaBrowser.Controller.MediaEncoding, System.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Jellyfin.LiveTv/Listings/SchedulesDirectDtos/MetadataDto.cs` (CSHARP) | Magnitude: 28.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 12, state_mutation: 9, indent_spaces: 9, api: 4
- `tests/Jellyfin.Providers.Tests/MediaInfo/EmbeddedImageProviderTests.cs` (CSHARP) | Magnitude: 290.6 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 56, func_start: 26, generics: 26
- `Jellyfin.Api/Controllers/PluginsController.cs` (CSHARP) | Magnitude: 172.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 136, doc: 70, structural_boundaries: 55, func_start: 31
- `tests/Jellyfin.Providers.Tests/Manager/MetadataServiceTests.cs` (CSHARP) | Magnitude: 352.82 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 282, state_mutation: 110, func_start: 71, sec_high_risk_execution: 60
- `tests/Jellyfin.Extensions.Tests/Json/Converters/JsonStringConverterTests.cs` (CSHARP) | Magnitude: 20.2 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 7, decorators: 7, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `MediaBrowser.Model/Tasks/ITaskTrigger.cs` (CSHARP) | Magnitude: 59.2 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 19, indent_spaces: 7, structural_boundaries: 5, branch: 2
- `src/Jellyfin.Drawing.Skia/UnplayedCountIndicator.cs` (CSHARP) | Magnitude: 26.68 | Delta: **0.127 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, doc: 15, structural_boundaries: 12, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Emby.Naming/Video/VideoFileInfo.cs` (CSHARP) | Magnitude: 179.1 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 66, state_mutation: 54, indent_spaces: 35, branch: 21
- `src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/BaseItemEntity.cs` (CSHARP) | Magnitude: 357.86 | Delta: **0.255 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 255, api: 86, indent_spaces: 85, branch: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Jellyfin.Api/Controllers/ScheduledTasksController.cs` (CSHARP) | Magnitude: 100.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 85, doc: 43, structural_boundaries: 32, func_start: 21
- `MediaBrowser.Providers/Lyric/LyricManager.cs` (CSHARP) | Magnitude: 564.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 347, structural_boundaries: 137, func_start: 65, branch: 59
- `src/Jellyfin.LiveTv/Listings/SchedulesDirectDtos/StationDto.cs` (CSHARP) | Magnitude: 50.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 30, state_mutation: 25, indent_spaces: 21, api: 10
- `src/Jellyfin.LiveTv/Listings/SchedulesDirectDtos/TokenDto.cs` (CSHARP) | Magnitude: 40.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 21, state_mutation: 18, indent_spaces: 15, api: 7
- `MediaBrowser.Model/Extensions/LibraryOptionsExtension.cs` (CSHARP) | Magnitude: 35.74 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 14, doc: 8, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `MediaBrowser.Model/IO/AsyncFile.cs` (CSHARP) | Magnitude: 31.38 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 20, structural_boundaries: 8, api: 6
- `MediaBrowser.Model/Drawing/ImageFormatExtensions.cs` (CSHARP) | Magnitude: 27.76 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 20, args: 16, closures: 16
- `Jellyfin.Server.Implementations/Item/OrderMapper.cs` (CSHARP) | Magnitude: 68.54 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 99, args: 83, closures: 82, indent_spaces: 58

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `MediaBrowser.Controller/Resolvers/ItemResolver.cs` (CSHARP) | Magnitude: 40.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 23, indent_spaces: 21, structural_boundaries: 8, branch: 4
- `Jellyfin.Api/Models/LibraryDtos/LibraryTypeOptionsDto.cs` (CSHARP) | Magnitude: 30.26 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 18, state_mutation: 9, generics: 8, structural_boundaries: 6
- `Jellyfin.Data/Events/Users/UserCreatedEventArgs.cs` (CSHARP) | Magnitude: 5.3 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, indent_spaces: 6, structural_boundaries: 3, api: 2
- `Jellyfin.Data/Events/Users/UserDeletedEventArgs.cs` (CSHARP) | Magnitude: 5.3 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, indent_spaces: 6, structural_boundaries: 3, api: 2
- `Jellyfin.Data/Events/Users/UserLockedOutEventArgs.cs` (CSHARP) | Magnitude: 5.3 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, indent_spaces: 6, structural_boundaries: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Jellyfin.LiveTv/LiveTvManager.cs` (CSHARP) | Magnitude: 1605.0 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 999, structural_boundaries: 311, state_mutation: 278, branch: 139
- `MediaBrowser.Providers/Plugins/Tmdb/Configuration/config.html` (HTML) | Magnitude: 81.58 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 42, ui_framework: 42, args: 30
- `Emby.Naming/AudioBook/AudioBookListResolver.cs` (CSHARP) | Magnitude: 239.02 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 45, branch: 22, state_mutation: 22
- `Emby.Server.Implementations/Dto/DtoService.cs` (CSHARP) | Magnitude: 2071.78 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1092, branch: 285, structural_boundaries: 183, safety: 128
- `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` (CSHARP) | Magnitude: 645.38 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 485, structural_boundaries: 241, args: 155, state_mutation: 124

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `MediaBrowser.Providers/Plugins/StudioImages/Configuration/config.html` (HTML) | Magnitude: 30.06 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 14, args: 9, concurrency: 8
- `MediaBrowser.Providers/Plugins/MusicBrainz/Configuration/config.html` (HTML) | Magnitude: 33.4 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 18, args: 14, ui_framework: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Emby.Server.Implementations/Playlists/PlaylistManager.cs` (CSHARP) | Magnitude: 1120.92 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 535, structural_boundaries: 141, state_mutation: 117, branch: 101
- `Emby.Server.Implementations/Session/SessionManager.cs` (CSHARP) | Magnitude: 3257.9 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1571, state_mutation: 373, structural_boundaries: 301, func_start: 271
- `src/Jellyfin.LiveTv/LiveTvMediaSourceProvider.cs` (CSHARP) | Magnitude: 425.52 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 237, structural_boundaries: 59, concurrency: 48, branch: 39
- `tests/Jellyfin.Server.Integration.Tests/Controllers/PluginsControllerTests.cs` (CSHARP) | Magnitude: 44.32 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 18, concurrency: 13, sec_high_risk_execution: 9
- `tests/Jellyfin.Server.Integration.Tests/Middleware/RobotsRedirectionMiddlewareTests.cs` (CSHARP) | Magnitude: 33.14 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 9, concurrency: 8, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `MediaBrowser.Model/Providers/ExternalIdInfo.cs` (CSHARP) | Magnitude: 29.6 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 24, state_mutation: 16, indent_spaces: 12, api: 5
- `Emby.Naming/TV/EpisodeInfo.cs` (CSHARP) | Magnitude: 63.68 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 56, state_mutation: 43, indent_spaces: 21, api: 16
- `Emby.Naming/Video/StubTypeRule.cs` (CSHARP) | Magnitude: 11.96 | Delta: **0.146 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 16, indent_spaces: 10, api: 4, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Jellyfin.Api/Constants/UserRoles.cs` (CSHARP) | Magnitude: 17.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, api: 4, immutability_locks: 3, indent_spaces: 3
- `Jellyfin.Api/Models/SyncPlayDtos/NewGroupRequestDto.cs` (CSHARP) | Magnitude: 7.98 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, indent_spaces: 5, api: 3, structural_boundaries: 2
- `MediaBrowser.Model/Lyrics/RemoteLyricInfoDto.cs` (CSHARP) | Magnitude: 18.64 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 7, api: 4, safety: 3
- `MediaBrowser.Model/Configuration/PathSubstitution.cs` (CSHARP) | Magnitude: 19.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, indent_spaces: 5, api: 3, structural_boundaries: 2
- `MediaBrowser.Model/SyncPlay/GroupStateUpdate.cs` (CSHARP) | Magnitude: 10.96 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 16, indent_spaces: 10, api: 4, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `MediaBrowser.Providers/Books/OpenPackagingFormat/OpfReader.cs` (CSHARP) | Magnitude: 566.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 242, structural_boundaries: 86, branch: 82, func_start: 38
- `Emby.Naming/Common/MediaType.cs` (CSHARP) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 12, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2
- `MediaBrowser.Controller/IServerApplicationPaths.cs` (CSHARP) | Magnitude: 16.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 47, indent_spaces: 15, structural_boundaries: 7, import: 5
- `MediaBrowser.Controller/Providers/RefreshPriority.cs` (CSHARP) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 12, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2
- `MediaBrowser.Model/SyncPlay/GroupRepeatMode.cs` (CSHARP) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 12, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` -> Churn: **100.0%** | Cog Load: 20.1467% | Debt: 98.1306%
- `MediaBrowser.Controller/Entities/BaseItem.cs` -> Churn: **75.17%** | Cog Load: 24.7842% | Debt: 57.5612%
- `Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs` -> Churn: **74.1%** | Cog Load: 68.3417% | Debt: 19.6849%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Jellyfin.LiveTv/LiveTvManager.cs` -> **evan314159** (100.0% isolated ownership) | Magnitude: 1605.0
- `src/Jellyfin.LiveTv/Channels/ChannelManager.cs` -> **evan314159** (100.0% isolated ownership) | Magnitude: 1240.9
- `MediaBrowser.Model/Dlna/ConditionProcessor.cs` -> **jaxx2104** (100.0% isolated ownership) | Magnitude: 1213.62
- `MediaBrowser.Providers/Manager/ItemImageProvider.cs` -> **theguymadmax** (100.0% isolated ownership) | Magnitude: 1118.08
- `Jellyfin.Server/Migrations/JellyfinMigrationService.cs` -> **Bond-009** (100.0% isolated ownership) | Magnitude: 883.24

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `MediaBrowser.Controller/Entities/Audio/Audio.cs` -> **Severity: 2094.4** (Blast Radius: 20.944 * Doc Risk: 100.0%)
- `MediaBrowser.Model/MediaInfo/MediaInfo.cs` -> **Severity: 1356.889** (Blast Radius: 13.569 * Doc Risk: 99.9992%)
- `src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/Libraries/Library.cs` -> **Severity: 704.68** (Blast Radius: 59.116 * Doc Risk: 11.9203%)
- `MediaBrowser.Controller/Entities/Extensions.cs` -> **Severity: 669.468** (Blast Radius: 56.162 * Doc Risk: 11.9203%)
- `src/Jellyfin.LiveTv/TunerHosts/HdHomerun/Channels.cs` -> **Severity: 519.6** (Blast Radius: 5.196 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
