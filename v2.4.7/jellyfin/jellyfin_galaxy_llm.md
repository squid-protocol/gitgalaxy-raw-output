# ARCHITECTURAL_BRIEF: jellyfin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/jellyfin` |
| **Timestamp** | `2026-08-07T05:02:32.950149+00:00` |
| **Scan Duration** | `5.62s` |
| **Git Branch** | `master` |
| **Git Commit** | `dbc42bb8e236f9ead33ddd47d500b7d00f52805d` |
| **Git Remote** | `https://github.com/jellyfin/jellyfin.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1836 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.369`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 1108 | 55.1% |
| file_cluster_8 | 564 | 28.1% |
| file_cluster_7 | 117 | 5.8% |
| file_cluster_0 | 86 | 4.3% |
| file_cluster_16 | 78 | 3.9% |
| file_cluster_4 | 29 | 1.4% |
| file_cluster_17 | 7 | 0.3% |
| file_cluster_15 | 3 | 0.1% |
| file_cluster_1 | 2 | 0.1% |
| file_cluster_2 | 2 | 0.1% |
| file_cluster_6 | 1 | 0.0% |
| file_cluster_11 | 1 | 0.0% |

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
| Cognitive Load Exposure | 0.0 | 91.5 | 12.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 40.6 | 48.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.0 | 2.3 | 2.3 |
| API Exposure | 0.0 | 17.0 | 6.0 | 5.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 16.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 47.9 | 37.9 | 0.0 |
| Commented Logic Exposure | 0.0 | 76.2 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.5 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 21.4 | 11.9 | 11.9 |
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

- `GetChildCount` (@ `Emby.Server.Implementations/Dto/DtoService.cs`) -> Impact: **360.9** | LOC: 914
- `GetAudioDirectPlayProfile` (@ `MediaBrowser.Model/Dlna/StreamBuilder.cs`) -> Impact: **286.9** | LOC: 577
- `GetVersionInfo` (@ `MediaBrowser.Controller/Entities/BaseItem.cs`) -> Impact: **282.1** | LOC: 962
- `GetBlockUnratedValue` (@ `MediaBrowser.Controller/Entities/BaseItem.cs`) -> Impact: **281.3** | LOC: 826
- `ParseParams` (@ `Jellyfin.Api/Helpers/StreamingHelpers.cs`) -> Impact: **276.9** | LOC: 198
- `Filter` (@ `MediaBrowser.Controller/Entities/UserViewBuilder.cs`) -> Impact: **263.2** | LOC: 464
- `AttachBasicFields` (@ `Emby.Server.Implementations/Dto/DtoService.cs`) -> Impact: **254.3** | LOC: 524
- `FetchDataFromXmlNode` (@ `MediaBrowser.LocalMetadata/Parsers/BaseItemXmlParser.cs`) -> Impact: **253.2** | LOC: 387
  * *Intent:* /// <summary> /// Fetches metadata from one Xml Element. /// </summary> /// <param name="reader">The reader.</param> /// <param name="itemResult">The ...
- `Fetch` (@ `MediaBrowser.XbmcMetadata/Parsers/BaseNfoParser.cs`) -> Impact: **245.7** | LOC: 398
  * *Intent:* /// <summary> /// Fetches the specified item. /// </summary> /// <param name="item">The <see cref="MetadataResult{T}"/>.</param> /// <param name="meta...
- `GetLinkedChild` (@ `MediaBrowser.Controller/Entities/BaseItem.cs`) -> Impact: **244.9** | LOC: 783

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Jellyfin.Api/Controllers` | 59 | 6808.94 | 17.14% | 51.62% |
| `MediaBrowser.Controller/Entities` | 46 | 5001.86 | 14.11% | 46.1% |
| `MediaBrowser.Controller/MediaEncoding` | 16 | 3325.91 | 17.95% | 31.43% |
| `Jellyfin.Server/Migrations/Routines` | 28 | 2702.1 | 18.49% | 48.08% |
| `MediaBrowser.Model/Dlna` | 24 | 2136.7 | 15.33% | 29.86% |
| `Emby.Server.Implementations/Localization/Core` | 102 | 1734.98 | 1.22% | 0.0% |
| `Emby.Server.Implementations/Session` | 3 | 1705.1 | 34.15% | 48.24% |
| `src/Jellyfin.LiveTv` | 4 | 1693.36 | 63.38% | 66.04% |
| `MediaBrowser.Providers/MediaInfo` | 12 | 1598.3 | 24.69% | 42.23% |
| `Jellyfin.Api/Helpers` | 8 | 1482.78 | 15.52% | 58.52% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Jellyfin.Api/BaseJellyfinApiController.cs` -> **100.0%** Exposure
- `Jellyfin.Api/Extensions/ClaimsPrincipalExtensions.cs` -> **100.0%** Exposure
- `Jellyfin.Api/Models/ConfigurationPageInfo.cs` -> **100.0%** Exposure
- `Jellyfin.Data/UserEntityExtensions.cs` -> **100.0%** Exposure
- `Jellyfin.Server.Implementations/Extensions/ExpressionExtensions.cs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Emby.Naming/AudioBook/AudioBookFileInfo.cs` -> **100.0%** Exposure
- `Emby.Naming/AudioBook/AudioBookInfo.cs` -> **100.0%** Exposure
- `Emby.Naming/Book/BookFileNameParserResult.cs` -> **100.0%** Exposure
- `Emby.Naming/Common/EpisodeExpression.cs` -> **100.0%** Exposure
- `Emby.Naming/Common/MediaType.cs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `MediaBrowser.Controller/Entities/BaseItem.cs` -> **41** Orphaned Functions | **22** Duplicates
- `Emby.Server.Implementations/Session/SessionManager.cs` -> **18** Orphaned Functions | **19** Duplicates
- `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` -> **28** Orphaned Functions | **4** Duplicates
- `Emby.Server.Implementations/IO/ManagedFileSystem.cs` -> **17** Orphaned Functions | **12** Duplicates
- `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` -> **27** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`MediaBrowser.LocalMetadata/Parsers/BaseItemXmlParser.cs`** -> AI Confidence: **99.39%**
2. **`tests/Jellyfin.Model.Tests/Dlna/LegacyStreamInfo.cs`** -> AI Confidence: **99.39%**
3. **`Emby.Naming/ExternalFiles/ExternalPathParser.cs`** -> AI Confidence: **99.31%**
4. **`Emby.Server.Implementations/Dto/DtoService.cs`** -> AI Confidence: **99.31%**
5. **`Emby.Server.Implementations/IO/FileRefresher.cs`** -> AI Confidence: **99.31%**
6. **`Emby.Server.Implementations/SyncPlay/SyncPlayManager.cs`** -> AI Confidence: **99.31%**
7. **`Jellyfin.Api/Auth/SyncPlayAccessPolicy/SyncPlayAccessHandler.cs`** -> AI Confidence: **99.31%**
8. **`Jellyfin.Api/Controllers/AudioController.cs`** -> AI Confidence: **99.31%**
9. **`Jellyfin.Api/Controllers/ItemUpdateController.cs`** -> AI Confidence: **99.31%**
10. **`Jellyfin.Api/Controllers/MediaInfoController.cs`** -> AI Confidence: **99.31%**
11. **`Jellyfin.Api/Controllers/SearchController.cs`** -> AI Confidence: **99.31%**
12. **`Jellyfin.Api/Helpers/DynamicHlsHelper.cs`** -> AI Confidence: **99.31%**
13. **`Jellyfin.Api/Helpers/StreamingHelpers.cs`** -> AI Confidence: **99.31%**
14. **`MediaBrowser.Controller/Entities/InternalItemsQuery.cs`** -> AI Confidence: **99.31%**
15. **`MediaBrowser.LocalMetadata/Parsers/PlaylistXmlParser.cs`** -> AI Confidence: **99.31%**
16. **`MediaBrowser.MediaEncoding/Probing/ProbeResultNormalizer.cs`** -> AI Confidence: **99.31%**
17. **`MediaBrowser.Model/Dlna/StreamBuilder.cs`** -> AI Confidence: **99.31%**
18. **`MediaBrowser.Model/Dlna/StreamInfo.cs`** -> AI Confidence: **99.31%**
19. **`MediaBrowser.Providers/Manager/ImageSaver.cs`** -> AI Confidence: **99.31%**
20. **`MediaBrowser.Providers/Manager/ItemImageProvider.cs`** -> AI Confidence: **99.31%**
21. **`MediaBrowser.Providers/Manager/MetadataService.cs`** -> AI Confidence: **99.31%**
22. **`MediaBrowser.Providers/MediaInfo/AudioFileProber.cs`** -> AI Confidence: **99.31%**
23. **`MediaBrowser.Providers/Plugins/Tmdb/Movies/TmdbMovieProvider.cs`** -> AI Confidence: **99.31%**
24. **`MediaBrowser.Providers/Plugins/Tmdb/TV/TmdbSeriesProvider.cs`** -> AI Confidence: **99.31%**
25. **`MediaBrowser.Providers/Plugins/Tmdb/TmdbExternalUrlProvider.cs`** -> AI Confidence: **99.31%**
26. **`MediaBrowser.XbmcMetadata/Parsers/BaseNfoParser.cs`** -> AI Confidence: **99.31%**
27. **`MediaBrowser.XbmcMetadata/Parsers/EpisodeNfoParser.cs`** -> AI Confidence: **99.31%**
28. **`MediaBrowser.XbmcMetadata/Parsers/MovieNfoParser.cs`** -> AI Confidence: **99.31%**
29. **`MediaBrowser.XbmcMetadata/Parsers/SeriesNfoParser.cs`** -> AI Confidence: **99.31%**
30. **`src/Jellyfin.LiveTv/LiveTvDtoService.cs`** -> AI Confidence: **99.31%**
31. **`tests/Jellyfin.Model.Tests/Dlna/StreamBuilderTests.cs`** -> AI Confidence: **99.31%**
32. **`Emby.Photos/PhotoProvider.cs`** -> AI Confidence: **99.24%**
33. **`Emby.Server.Implementations/IO/LibraryMonitor.cs`** -> AI Confidence: **99.24%**
34. **`Emby.Server.Implementations/IO/ManagedFileSystem.cs`** -> AI Confidence: **99.24%**
35. **`Emby.Server.Implementations/Images/CollectionFolderImageProvider.cs`** -> AI Confidence: **99.24%**
36. **`Emby.Server.Implementations/Playlists/PlaylistManager.cs`** -> AI Confidence: **99.24%**
37. **`Emby.Server.Implementations/Plugins/PluginManager.cs`** -> AI Confidence: **99.24%**
38. **`Emby.Server.Implementations/ScheduledTasks/ScheduledTaskWorker.cs`** -> AI Confidence: **99.24%**
39. **`Emby.Server.Implementations/Session/SessionManager.cs`** -> AI Confidence: **99.24%**
40. **`Emby.Server.Implementations/Session/WebSocketController.cs`** -> AI Confidence: **99.24%**
41. **`Emby.Server.Implementations/TV/TVSeriesManager.cs`** -> AI Confidence: **99.24%**
42. **`Emby.Server.Implementations/Updates/InstallationManager.cs`** -> AI Confidence: **99.24%**
43. **`Jellyfin.Api/Controllers/DynamicHlsController.cs`** -> AI Confidence: **99.24%**
44. **`Jellyfin.Api/Controllers/ItemsController.cs`** -> AI Confidence: **99.24%**
45. **`Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs`** -> AI Confidence: **99.24%**
46. **`Jellyfin.Server/Migrations/Routines/MoveExtractedFiles.cs`** -> AI Confidence: **99.24%**
47. **`MediaBrowser.Controller/Entities/Folder.cs`** -> AI Confidence: **99.24%**
48. **`MediaBrowser.Controller/Entities/UserViewBuilder.cs`** -> AI Confidence: **99.24%**
49. **`MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs`** -> AI Confidence: **99.24%**
50. **`MediaBrowser.Controller/MediaEncoding/EncodingJobInfo.cs`** -> AI Confidence: **99.24%**
51. **`MediaBrowser.Controller/MediaEncoding/TranscodingSegmentCleaner.cs`** -> AI Confidence: **99.24%**
52. **`MediaBrowser.Controller/Session/SessionInfo.cs`** -> AI Confidence: **99.24%**
53. **`MediaBrowser.LocalMetadata/Images/LocalImageProvider.cs`** -> AI Confidence: **99.24%**
54. **`MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs`** -> AI Confidence: **99.24%**
55. **`MediaBrowser.MediaEncoding/Subtitles/SubtitleEncoder.cs`** -> AI Confidence: **99.24%**
56. **`MediaBrowser.MediaEncoding/Transcoding/TranscodeManager.cs`** -> AI Confidence: **99.24%**
57. **`MediaBrowser.Model/Dto/MediaSourceInfo.cs`** -> AI Confidence: **99.24%**
58. **`MediaBrowser.Model/Entities/MediaStream.cs`** -> AI Confidence: **99.24%**
59. **`MediaBrowser.Providers/Books/OpenPackagingFormat/OpfReader.cs`** -> AI Confidence: **99.24%**
60. **`MediaBrowser.Providers/MediaInfo/FFProbeVideoInfo.cs`** -> AI Confidence: **99.24%**
61. **`MediaBrowser.Providers/Plugins/Tmdb/TV/TmdbEpisodeProvider.cs`** -> AI Confidence: **99.24%**
62. **`MediaBrowser.Providers/Plugins/Tmdb/TmdbClientManager.cs`** -> AI Confidence: **99.24%**
63. **`src/Jellyfin.Drawing.Skia/SkiaEncoder.cs`** -> AI Confidence: **99.24%**
64. **`src/Jellyfin.LiveTv/DefaultLiveTvService.cs`** -> AI Confidence: **99.24%**
65. **`src/Jellyfin.LiveTv/Guide/GuideManager.cs`** -> AI Confidence: **99.24%**
66. **`src/Jellyfin.LiveTv/IO/EncodedRecorder.cs`** -> AI Confidence: **99.24%**
67. **`src/Jellyfin.LiveTv/LiveTvMediaSourceProvider.cs`** -> AI Confidence: **99.24%**
68. **`src/Jellyfin.LiveTv/TunerHosts/LiveStream.cs`** -> AI Confidence: **99.24%**
69. **`src/Jellyfin.Networking/Manager/NetworkManager.cs`** -> AI Confidence: **99.24%**
70. **`Jellyfin.Server/Filters/SecurityRequirementsOperationFilter.cs`** -> AI Confidence: **99.23%**
71. **`Jellyfin.Server/Migrations/Stages/CodeMigration.cs`** -> AI Confidence: **99.23%**
72. **`MediaBrowser.Common/Net/NetworkUtils.cs`** -> AI Confidence: **99.23%**
73. **`MediaBrowser.Controller/MediaEncoding/TranscodingThrottler.cs`** -> AI Confidence: **99.23%**
74. **`MediaBrowser.XbmcMetadata/Parsers/SeasonNfoParser.cs`** -> AI Confidence: **99.23%**
75. **`src/Jellyfin.Database/Jellyfin.Database.Implementations/QueryPartitionHelpers.cs`** -> AI Confidence: **99.23%**
76. **`Emby.Server.Implementations/ApplicationHost.cs`** -> AI Confidence: **99.18%**
77. **`Emby.Server.Implementations/Collections/CollectionImageProvider.cs`** -> AI Confidence: **99.18%**
78. **`Emby.Server.Implementations/Data/CleanDatabaseScheduledTask.cs`** -> AI Confidence: **99.18%**
79. **`Emby.Server.Implementations/Images/BaseDynamicImageProvider.cs`** -> AI Confidence: **99.18%**
80. **`Emby.Server.Implementations/Images/DynamicImageProvider.cs`** -> AI Confidence: **99.18%**
81. **`Emby.Server.Implementations/Images/PlaylistImageProvider.cs`** -> AI Confidence: **99.18%**
82. **`Emby.Server.Implementations/QuickConnect/QuickConnectManager.cs`** -> AI Confidence: **99.18%**
83. **`Emby.Server.Implementations/ScheduledTasks/Tasks/ChapterImagesTask.cs`** -> AI Confidence: **99.18%**
84. **`Emby.Server.Implementations/ScheduledTasks/Tasks/CleanupCollectionAndPlaylistPathsTask.cs`** -> AI Confidence: **99.18%**
85. **`Emby.Server.Implementations/ScheduledTasks/Tasks/PluginUpdateTask.cs`** -> AI Confidence: **99.18%**
86. **`Jellyfin.Api/Auth/DefaultAuthorizationPolicy/DefaultAuthorizationHandler.cs`** -> AI Confidence: **99.18%**
87. **`Jellyfin.Api/Controllers/ArtistsController.cs`** -> AI Confidence: **99.18%**
88. **`Jellyfin.Api/Controllers/GenresController.cs`** -> AI Confidence: **99.18%**
89. **`Jellyfin.Api/Controllers/HlsSegmentController.cs`** -> AI Confidence: **99.18%**
90. **`Jellyfin.Api/Controllers/MoviesController.cs`** -> AI Confidence: **99.18%**
91. **`Jellyfin.Api/Controllers/MusicGenresController.cs`** -> AI Confidence: **99.18%**
92. **`Jellyfin.Api/Controllers/PlaystateController.cs`** -> AI Confidence: **99.18%**
93. **`Jellyfin.Api/Controllers/PluginsController.cs`** -> AI Confidence: **99.18%**
94. **`Jellyfin.Api/Controllers/QuickConnectController.cs`** -> AI Confidence: **99.18%**
95. **`Jellyfin.Api/Controllers/ScheduledTasksController.cs`** -> AI Confidence: **99.18%**
96. **`Jellyfin.Api/Controllers/StartupController.cs`** -> AI Confidence: **99.18%**
97. **`Jellyfin.Api/Controllers/SubtitleController.cs`** -> AI Confidence: **99.18%**
98. **`Jellyfin.Api/Controllers/UserController.cs`** -> AI Confidence: **99.18%**
99. **`Jellyfin.Api/Controllers/UserLibraryController.cs`** -> AI Confidence: **99.18%**
100. **`Jellyfin.Api/Controllers/YearsController.cs`** -> AI Confidence: **99.18%**
101. **`Jellyfin.Api/Helpers/RequestHelpers.cs`** -> AI Confidence: **99.18%**
102. **`Jellyfin.Api/Middleware/ExceptionMiddleware.cs`** -> AI Confidence: **99.18%**
103. **`Jellyfin.Api/Middleware/UrlDecodeQueryFeature.cs`** -> AI Confidence: **99.18%**
104. **`Jellyfin.Server.Implementations/Activity/ActivityManager.cs`** -> AI Confidence: **99.18%**
105. **`Jellyfin.Server.Implementations/Events/Consumers/Session/PlaybackStopLogger.cs`** -> AI Confidence: **99.18%**
106. **`Jellyfin.Server.Implementations/Item/BaseItemRepository.cs`** -> AI Confidence: **99.18%**
107. **`Jellyfin.Server.Implementations/Item/MediaStreamRepository.cs`** -> AI Confidence: **99.18%**
108. **`Jellyfin.Server.Implementations/Item/PeopleRepository.cs`** -> AI Confidence: **99.18%**
109. **`Jellyfin.Server.Implementations/Security/AuthorizationContext.cs`** -> AI Confidence: **99.18%**
110. **`Jellyfin.Server.Implementations/Users/DefaultPasswordResetProvider.cs`** -> AI Confidence: **99.18%**
111. **`Jellyfin.Server/Extensions/ApiServiceCollectionExtensions.cs`** -> AI Confidence: **99.18%**
112. **`Jellyfin.Server/Migrations/PreStartupRoutines/MigrateEncodingOptions.cs`** -> AI Confidence: **99.18%**
113. **`Jellyfin.Server/Migrations/Routines/FixPlaylistOwner.cs`** -> AI Confidence: **99.18%**
114. **`Jellyfin.Server/Migrations/Routines/MigrateLibraryUserData.cs`** -> AI Confidence: **99.18%**
115. **`Jellyfin.Server/Migrations/Routines/MoveTrickplayFiles.cs`** -> AI Confidence: **99.18%**
116. **`Jellyfin.Server/Migrations/Routines/RefreshCleanNames.cs`** -> AI Confidence: **99.18%**
117. **`Jellyfin.Server/Migrations/Routines/RefreshInternalDateModified.cs`** -> AI Confidence: **99.18%**
118. **`Jellyfin.Server/Migrations/Routines/RemoveDuplicateExtras.cs`** -> AI Confidence: **99.18%**
119. **`Jellyfin.Server/Migrations/Routines/ReseedFolderFlag.cs`** -> AI Confidence: **99.18%**
120. **`Jellyfin.Server/Program.cs`** -> AI Confidence: **99.18%**
121. **`Jellyfin.Server/ServerSetupApp/SetupServer.cs`** -> AI Confidence: **99.18%**
122. **`MediaBrowser.Common/Plugins/BasePluginOfT.cs`** -> AI Confidence: **99.18%**
123. **`MediaBrowser.Controller/Entities/Audio/Audio.cs`** -> AI Confidence: **99.18%**
124. **`MediaBrowser.Controller/Entities/Audio/MusicAlbum.cs`** -> AI Confidence: **99.18%**
125. **`MediaBrowser.Controller/Entities/CollectionFolder.cs`** -> AI Confidence: **99.18%**
126. **`MediaBrowser.Controller/Entities/Movies/Movie.cs`** -> AI Confidence: **99.18%**
127. **`MediaBrowser.Controller/Entities/TV/Season.cs`** -> AI Confidence: **99.18%**
128. **`MediaBrowser.Controller/Entities/Trailer.cs`** -> AI Confidence: **99.18%**
129. **`MediaBrowser.Controller/Entities/UserView.cs`** -> AI Confidence: **99.18%**
130. **`MediaBrowser.LocalMetadata/Images/EpisodeLocalImageProvider.cs`** -> AI Confidence: **99.18%**
131. **`MediaBrowser.Providers/Lyric/LyricManager.cs`** -> AI Confidence: **99.18%**
132. **`MediaBrowser.Providers/Lyric/LyricScheduledTask.cs`** -> AI Confidence: **99.18%**
133. **`MediaBrowser.Providers/MediaInfo/EmbeddedImageProvider.cs`** -> AI Confidence: **99.18%**
134. **`MediaBrowser.Providers/MediaInfo/ProbeProvider.cs`** -> AI Confidence: **99.18%**
135. **`MediaBrowser.Providers/MediaInfo/SubtitleScheduledTask.cs`** -> AI Confidence: **99.18%**
136. **`MediaBrowser.Providers/MediaInfo/VideoImageProvider.cs`** -> AI Confidence: **99.18%**
137. **`MediaBrowser.Providers/Music/AlbumMetadataService.cs`** -> AI Confidence: **99.18%**
138. **`MediaBrowser.Providers/Music/AudioMetadataService.cs`** -> AI Confidence: **99.18%**
139. **`MediaBrowser.Providers/Playlists/PlaylistItemsProvider.cs`** -> AI Confidence: **99.18%**
140. **`MediaBrowser.Providers/Plugins/AudioDb/AudioDbArtistImageProvider.cs`** -> AI Confidence: **99.18%**
141. **`MediaBrowser.Providers/Plugins/AudioDb/AudioDbArtistProvider.cs`** -> AI Confidence: **99.18%**
142. **`MediaBrowser.Providers/Plugins/Omdb/OmdbItemProvider.cs`** -> AI Confidence: **99.18%**
143. **`MediaBrowser.Providers/Plugins/Omdb/OmdbProvider.cs`** -> AI Confidence: **99.18%**
144. **`MediaBrowser.Providers/Plugins/Tmdb/BoxSets/TmdbBoxSetImageProvider.cs`** -> AI Confidence: **99.18%**
145. **`MediaBrowser.Providers/Plugins/Tmdb/BoxSets/TmdbBoxSetProvider.cs`** -> AI Confidence: **99.18%**
146. **`MediaBrowser.Providers/TV/SeriesMetadataService.cs`** -> AI Confidence: **99.18%**
147. **`MediaBrowser.Providers/Trickplay/TrickplayMoveImagesTask.cs`** -> AI Confidence: **99.18%**
148. **`MediaBrowser.Providers/Trickplay/TrickplayProvider.cs`** -> AI Confidence: **99.18%**
149. **`MediaBrowser.XbmcMetadata/Providers/BaseNfoProvider.cs`** -> AI Confidence: **99.18%**
150. **`MediaBrowser.XbmcMetadata/Providers/SeriesNfoSeasonProvider.cs`** -> AI Confidence: **99.18%**
151. **`MediaBrowser.XbmcMetadata/Savers/AlbumNfoSaver.cs`** -> AI Confidence: **99.18%**
152. **`MediaBrowser.XbmcMetadata/Savers/ArtistNfoSaver.cs`** -> AI Confidence: **99.18%**
153. **`MediaBrowser.XbmcMetadata/Savers/SeasonNfoSaver.cs`** -> AI Confidence: **99.18%**
154. **`MediaBrowser.XbmcMetadata/Savers/SeriesNfoSaver.cs`** -> AI Confidence: **99.18%**
155. **`src/Jellyfin.CodeAnalysis/AsyncDisposalPatternAnalyzer.cs`** -> AI Confidence: **99.18%**
156. **`src/Jellyfin.Drawing.Skia/StripCollageBuilder.cs`** -> AI Confidence: **99.18%**
157. **`src/Jellyfin.LiveTv/TunerHosts/BaseTunerHost.cs`** -> AI Confidence: **99.18%**
158. **`src/Jellyfin.LiveTv/TunerHosts/HdHomerun/HdHomerunHost.cs`** -> AI Confidence: **99.18%**
159. **`src/Jellyfin.LiveTv/TunerHosts/HdHomerun/HdHomerunManager.cs`** -> AI Confidence: **99.18%**
160. **`src/Jellyfin.LiveTv/TunerHosts/HdHomerun/HdHomerunUdpStream.cs`** -> AI Confidence: **99.18%**
161. **`src/Jellyfin.LiveTv/TunerHosts/TunerHostManager.cs`** -> AI Confidence: **99.18%**
162. **`tests/Jellyfin.Extensions.Tests/Json/Converters/JsonCommaDelimitedCollectionTests.cs`** -> AI Confidence: **99.18%**
163. **`tests/Jellyfin.Naming.Tests/ExternalFiles/ExternalPathParserTests.cs`** -> AI Confidence: **99.18%**
164. **`tests/Jellyfin.Providers.Tests/Manager/MetadataServiceTests.cs`** -> AI Confidence: **99.18%**
165. **`tests/Jellyfin.Providers.Tests/Manager/ProviderManagerTests.cs`** -> AI Confidence: **99.18%**
166. **`Emby.Server.Implementations/AppBase/BaseConfigurationManager.cs`** -> AI Confidence: **99.16%**
167. **`Emby.Server.Implementations/Chapters/ChapterManager.cs`** -> AI Confidence: **99.16%**
168. **`Emby.Server.Implementations/Collections/CollectionManager.cs`** -> AI Confidence: **99.16%**
169. **`Emby.Server.Implementations/EntryPoints/LibraryChangedNotifier.cs`** -> AI Confidence: **99.16%**
170. **`Emby.Server.Implementations/EntryPoints/UserDataChangeNotifier.cs`** -> AI Confidence: **99.16%**
171. **`Emby.Server.Implementations/HttpServer/WebSocketConnection.cs`** -> AI Confidence: **99.16%**
172. **`Emby.Server.Implementations/Localization/LocalizationManager.cs`** -> AI Confidence: **99.16%**
173. **`Emby.Server.Implementations/Session/SessionWebSocketListener.cs`** -> AI Confidence: **99.16%**
174. **`Jellyfin.Api/Auth/CustomAuthenticationHandler.cs`** -> AI Confidence: **99.16%**
175. **`Jellyfin.Api/Controllers/DisplayPreferencesController.cs`** -> AI Confidence: **99.16%**
176. **`Jellyfin.Api/Controllers/EnvironmentController.cs`** -> AI Confidence: **99.16%**
177. **`Jellyfin.Api/Controllers/FilterController.cs`** -> AI Confidence: **99.16%**
178. **`Jellyfin.Api/Controllers/ImageController.cs`** -> AI Confidence: **99.16%**
179. **`Jellyfin.Api/Controllers/LibraryController.cs`** -> AI Confidence: **99.16%**
180. **`Jellyfin.Api/Controllers/LibraryStructureController.cs`** -> AI Confidence: **99.16%**
181. **`Jellyfin.Api/Controllers/PlaylistsController.cs`** -> AI Confidence: **99.16%**
182. **`Jellyfin.Api/Controllers/TvShowsController.cs`** -> AI Confidence: **99.16%**
183. **`Jellyfin.Api/Controllers/UniversalAudioController.cs`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `MediaBrowser.Providers/Plugins/Tmdb/TmdbUtils.cs` -> **97.7174%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10367` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `MediaBrowser.Providers/Plugins/Omdb/OmdbItemProvider.cs` (CSHARP) -> Cumulative Risk: **740.43**
- **Archetype:** `file_cluster_13` (Distance: 11.963 IQR)
- **Magnitude:** 216.14 | **LOC:** 313 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9798%), Concurrency (99.5892%), Tech Debt (99.4203%)
- **Heaviest Functions:** `GetSearchResultsInternal` (Impact: 46.5), `ResultToMetadataResult` (Impact: 9.6), `GetResult` (Impact: 4.3)

### 2. `MediaBrowser.Providers/Plugins/AudioDb/AudioDbAlbumProvider.cs` (CSHARP) -> Cumulative Risk: **717.31**
- **Archetype:** `file_cluster_13` (Distance: 11.581 IQR)
- **Magnitude:** 209.14 | **LOC:** 304 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.988%), Documentation (99.8471%), Concurrency (96.4058%)
- **Heaviest Functions:** `ProcessResult` (Impact: 41.1), `GetMetadata` (Impact: 10.0), `DownloadInfo` (Impact: 4.7)

### 3. `src/Jellyfin.LiveTv/TunerHosts/LiveStream.cs` (CSHARP) -> Cumulative Risk: **707.7**
- **Archetype:** `file_cluster_4` (Distance: 11.579 IQR)
- **Magnitude:** 134.72 | **LOC:** 177 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.7449%), Tech Debt (92.1618%)
- **Heaviest Functions:** `TrySeek` (Impact: 11.5), `DeleteTempFiles` (Impact: 9.7), `LiveStream` (Impact: 9.2)

### 4. `MediaBrowser.Providers/Plugins/AudioDb/AudioDbArtistProvider.cs` (CSHARP) -> Cumulative Risk: **705.48**
- **Archetype:** `file_cluster_13` (Distance: 12.129 IQR)
- **Magnitude:** 207.5 | **LOC:** 291 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9982%), Documentation (99.9388%), Concurrency (97.8505%)
- **Heaviest Functions:** `ProcessResult` (Impact: 34.3), `GetMetadata` (Impact: 10.0), `EnsureArtistInfo` (Impact: 4.2)

### 5. `src/Jellyfin.LiveTv/LiveTvManager.cs` (CSHARP) -> Cumulative Risk: **673.14**
- **Archetype:** `file_cluster_17` (Distance: 12.942 IQR)
- **Magnitude:** 847.1 | **LOC:** 1293 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9721%), Concurrency (99.911%), Tech Debt (90.3175%)
- **Heaviest Functions:** `GetEmbyRecordingsAsync` (Impact: 39.3), `GetTimers` (Impact: 30.0), `GetTimersInternal` (Impact: 24.2)

### 6. `src/Jellyfin.LiveTv/IO/ExclusiveLiveStream.cs` (CSHARP) -> Cumulative Risk: **663.88**
- **Archetype:** `file_cluster_13` (Distance: 11.19 IQR)
- **Magnitude:** 47.92 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.7966%), Documentation (99.3764%)
- **Heaviest Functions:** `Open` (Impact: 2.4), `Close` (Impact: 2.2), `GetStream` (Impact: 2.2)

### 7. `Jellyfin.Server.Implementations/Activity/ActivityManager.cs` (CSHARP) -> Cumulative Risk: **660.37**
- **Archetype:** `file_cluster_13` (Distance: 13.02 IQR)
- **Magnitude:** 183.42 | **LOC:** 214 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9976%), State Flux (99.9968%), Tech Debt (99.8115%)
- **Heaviest Functions:** `GetPagedResultAsync` (Impact: 48.2), `ApplyOrdering` (Impact: 13.6), `ApplyOrdering` (Impact: 6.0)

### 8. `MediaBrowser.Controller/Entities/TV/Series.cs` (CSHARP) -> Cumulative Risk: **648.58**
- **Archetype:** `file_cluster_13` (Distance: 12.144 IQR)
- **Magnitude:** 307.72 | **LOC:** 529 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.5377%), Tech Debt (91.8511%), Concurrency (90.7395%)
- **Heaviest Functions:** `RefreshAllMetadata` (Impact: 25.2), `GetSeasonEpisodes` (Impact: 22.4), `GetItemsInternal` (Impact: 19.3)

### 9. `Jellyfin.Server.Implementations/Devices/DeviceManager.cs` (CSHARP) -> Cumulative Risk: **647.45**
- **Archetype:** `file_cluster_4` (Distance: 13.022 IQR)
- **Magnitude:** 270.78 | **LOC:** 312 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9969%), Verification (80.0%)
- **Heaviest Functions:** `GetDevicesForUser` (Impact: 8.1), `GetDevices` (Impact: 7.8), `ToDeviceInfo` (Impact: 7.8)

### 10. `Jellyfin.Server.Implementations/Users/DefaultPasswordResetProvider.cs` (CSHARP) -> Cumulative Risk: **642.65**
- **Archetype:** `file_cluster_13` (Distance: 11.659 IQR)
- **Magnitude:** 120.56 | **LOC:** 140 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (98.6166%), Tech Debt (97.7023%)
- **Heaviest Functions:** `RedeemPasswordResetPin` (Impact: 26.6), `Directory.EnumerateFiles` (Impact: 19.4), `StartForgotPasswordProcess` (Impact: 7.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.83 IQR)
- **Top Global Matches:** file_cluster_8: 12.83, file_cluster_13: 13.095, file_cluster_7: 13.146
- **Magnitude:** 2170.6 | **LOC:** 7852 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (23.499%), Tech Debt (30.8219%)
**Top Internal Functions/Classes:**
  * `GetRkmppVidFiltersPrefered` (Impact: 136.0)
  * `GetVideoBitrateParam` (Impact: 108.6)
  * `GetAppleVidFiltersPreferred` (Impact: 61.4)
  * `GetVaapiLimitedVidFiltersPrefered` (Impact: 51.0)
  * `GetInputFormat` (Impact: 48.8)
    * *Intent:* /// <summary> /// Gets the name of the output video codec.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 640`, `structural_boundaries: 801`, `args: 96`, `func_start: 335`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 610`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 27`
* *Architecture:* `io: 7`, `api: 59`, `import: 22`
* *Defense:* `safety: 131`, `doc: 110`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MediaBrowser.Model.Dto, MediaBrowser.Model.MediaInfo, MediaBrowser.Common.Configuration.IConfigurationManager, Jellyfin.Data, System.Globalization, System.Collections.Generic, System.IO, MediaBrowser.Controller.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Controller/Entities/BaseItem.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.059 IQR)
- **Top Global Matches:** file_cluster_0: 13.059, file_cluster_13: 13.151, file_cluster_11: 13.315
- **Magnitude:** 1733.94 | **LOC:** 2689 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (19.0333%), Tech Debt (99.9758%)
**Top Internal Functions/Classes:**
  * `GetVersionInfo` (Impact: 282.1)
  * `GetBlockUnratedValue` (Impact: 281.3)
  * `GetLinkedChild` (Impact: 244.9)
  * `RefreshMetadataForOwnedItem` (Impact: 25.5)
  * `CreateSortName` (Impact: 20.1)
    * *Intent:* /// <summary>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 312`, `args: 136`, `func_start: 165`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 162`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 22`, `orphaned_logic: 41`
* *Architecture:* `io: 9`, `api: 163`, `concurrency: 31`, `import: 34`
* *Defense:* `safety: 67`, `doc: 231`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.472
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MediaBrowser.Controller.Persistence, MediaBrowser.Controller.Chapters, MediaBrowser.Model.Dto, MediaBrowser.Model.MediaInfo, Microsoft.Extensions.Logging, Jellyfin.Data, Jellyfin.Database.Implementations.Entities, MediaBrowser.Controller.Channels...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Emby.Server.Implementations/Session/SessionManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.758 IQR)
- **Top Global Matches:** file_cluster_4: 13.758, file_cluster_13: 13.763, file_cluster_8: 13.801
- **Magnitude:** 1474.4 | **LOC:** 2155 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (34.6243%), Tech Debt (82.5739%)
**Top Internal Functions/Classes:**
  * `GetSessions` (Impact: 75.3)
    * *Intent:* /// <inheritdoc/>
  * `OnPlaybackStopped` (Impact: 49.2)
    * *Intent:* /// <summary> /// Used to report that playback has ended for an item. /// </summary> /// <param name...
  * `SendPlayCommand` (Impact: 42.2)
    * *Intent:* /// <inheritdoc />
  * `UpdateNowPlayingItem` (Impact: 40.0)
    * *Intent:* /// <summary> /// Updates the now playing item id. /// </summary> /// <returns>Task.</returns>
  * `CreateSessionInfo` (Impact: 30.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 301`, `args: 121`, `func_start: 271`, `class_start: 1`
* *Risk/State:* `state_mutation: 369`, `duplicate_logic: 19`, `orphaned_logic: 18`
* *Architecture:* `api: 52`, `concurrency: 184`, `import: 39`
* *Defense:* `safety: 111`, `doc: 165`, `immutability_locks: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Model.SyncPlay, MediaBrowser.Model.Dto, Microsoft.Extensions.Logging, Jellyfin.Data, MediaBrowser.Controller.Events.Session, Microsoft.EntityFrameworkCore, MediaBrowser.Controller.Authentication, MediaBrowser.Model.Querying...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.038 IQR)
- **Top Global Matches:** file_cluster_8: 13.038, file_cluster_13: 13.076, file_cluster_17: 13.282
- **Magnitude:** 1222.44 | **LOC:** 1483 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 54.5%
- **Risk Profile:** Cognitive Load (67.9076%), Tech Debt (99.9208%)
**Top Internal Functions/Classes:**
  * `GetItem` (Impact: 154.0)
  * `Perform` (Impact: 124.8)
    * *Intent:* /// <inheritdoc/>
  * `GetMediaStream` (Impact: 93.3)
    * *Intent:* /// <summary> /// Gets the media stream. /// </summary> /// <param name="reader">The reader.</param>...
  * `TrackedMigrationStep` (Impact: 19.5)
  * `GetUserData` (Impact: 17.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 272`, `args: 38`, `func_start: 114`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 604`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 27`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 11`, `import: 21`
* *Defense:* `safety: 7`, `doc: 26`, `immutability_locks: 15`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Microsoft.Extensions.Logging, Microsoft.EntityFrameworkCore, System.Data, Jellyfin.Database.Implementations.Entities, System.Globalization, Jellyfin.Database.Implementations.Entities.Chapter, System.Collections.Generic, System.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Emby.Server.Implementations/Dto/DtoService.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.683 IQR)
- **Top Global Matches:** file_cluster_17: 12.683, file_cluster_8: 12.749, file_cluster_13: 12.774
- **Magnitude:** 1199.68 | **LOC:** 1512 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (29.9955%), Tech Debt (55.568%)
**Top Internal Functions/Classes:**
  * `GetChildCount` (Impact: 360.9)
  * `AttachBasicFields` (Impact: 254.3)
  * `AddInheritedImages` (Impact: 76.2)
  * `GetBaseItemDtoInternal` (Impact: 51.8)
  * `AttachPeople` (Impact: 45.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 183`, `args: 76`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 107`, `dead_code: 5`, `planned_debt: 3`, `duplicate_logic: 6`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 19`, `import: 25`
* *Defense:* `safety: 128`, `doc: 28`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MediaBrowser.Controller.Chapters, MediaBrowser.Model.Dto, Microsoft.Extensions.Logging, System.Collections.Frozen, MediaBrowser.Controller.Entities.TV.Series, MediaBrowser.Model.Querying, Jellyfin.Database.Implementations.Entities, MediaBrowser.Controller.Channels...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Model/Dlna/StreamBuilder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.616 IQR)
- **Top Global Matches:** file_cluster_8: 12.616, file_cluster_13: 12.806, file_cluster_17: 12.818
- **Magnitude:** 887.82 | **LOC:** 2400 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (26.02%), Tech Debt (33.4299%)
**Top Internal Functions/Classes:**
  * `GetAudioDirectPlayProfile` (Impact: 286.9)
  * `GetTranscodeReasonForFailedCondition` (Impact: 73.0)
  * `GetSubtitleProfile` (Impact: 71.9)
  * `GetOptimalAudioStream` (Impact: 58.7)
  * `GetVideoDirectPlayProfile` (Impact: 57.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 184`, `args: 50`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 103`, `planned_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 11`, `import: 12`
* *Defense:* `safety: 105`, `doc: 76`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Model.Session, System.Collections.Generic, Jellyfin.Extensions, MediaBrowser.Model.Entities, MediaBrowser.Model.Dto, MediaBrowser.Model.MediaInfo, Jellyfin.Data.Enums, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.723 IQR)
- **Top Global Matches:** file_cluster_13: 12.723, file_cluster_8: 12.81, file_cluster_17: 13.027
- **Magnitude:** 849.86 | **LOC:** 1400 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (33.5893%), Tech Debt (98.2674%)
**Top Internal Functions/Classes:**
  * `ExtractImageInternal` (Impact: 94.1)
  * `ExtractVideoImagesOnIntervalAccelerated` (Impact: 83.5)
    * *Intent:* /// <inheritdoc />
  * `SetFFmpegPath` (Impact: 43.3)
    * *Intent:* /// <summary> /// Run at startup to validate ffmpeg. /// Sets global variables FFmpegPath. /// Prece...
  * `GetMediaInfoInternal` (Impact: 40.5)
    * *Intent:* /// <summary> /// Gets the media info internal. /// </summary> /// <returns>Task{MediaInfoResult}.</...
  * `GetExtraArguments` (Impact: 24.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 199`, `args: 92`, `func_start: 140`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 214`, `planned_debt: 2`, `duplicate_logic: 11`, `orphaned_logic: 15`
* *Architecture:* `io: 8`, `api: 55`, `concurrency: 34`, `import: 32`
* *Defense:* `safety: 45`, `doc: 58`, `sync_locks: 4`, `immutability_locks: 16`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Text.Json, MediaBrowser.Model.Dto, MediaBrowser.Model.MediaInfo, MediaBrowser.MediaEncoding.Probing, Microsoft.Extensions.Logging, System.Globalization, AsyncKeyedLock, MediaBrowser.Model.Globalization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.LiveTv/LiveTvManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.942 IQR)
- **Top Global Matches:** file_cluster_17: 12.942, file_cluster_4: 12.957, file_cluster_13: 13.044
- **Magnitude:** 847.1 | **LOC:** 1293 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (64.5917%), Tech Debt (90.3175%)
**Top Internal Functions/Classes:**
  * `GetEmbyRecordingsAsync` (Impact: 39.3)
  * `GetTimers` (Impact: 30.0)
  * `GetTimersInternal` (Impact: 24.2)
  * `AddInfoToRecordingDto` (Impact: 20.8)
  * `AddRecordingInfo` (Impact: 19.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 311`, `args: 110`, `func_start: 108`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 278`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 12`
* *Architecture:* `api: 33`, `concurrency: 119`, `import: 26`
* *Defense:* `safety: 47`, `doc: 14`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MediaBrowser.Model.Dto, Microsoft.Extensions.Logging, Jellyfin.Data, MediaBrowser.Model.Querying, Jellyfin.Database.Implementations.Entities, MediaBrowser.Controller.Channels, System.Globalization, MediaBrowser.Model.Globalization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Probing/ProbeResultNormalizer.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.149 IQR)
- **Top Global Matches:** file_cluster_8: 12.149, file_cluster_13: 12.278, file_cluster_17: 12.395
- **Magnitude:** 728.88 | **LOC:** 1761 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (44.8147%), Tech Debt (98.974%)
**Top Internal Functions/Classes:**
  * `FetchFromItunesInfo` (Impact: 237.1)
  * `SetAudioInfoFromTags` (Impact: 92.0)
  * `GetMediaInfo` (Impact: 84.1)
    * *Intent:* /// <summary> /// Transforms a FFprobe response into its <see cref="MediaInfo"/> equivalent. /// </s...
  * `Split` (Impact: 35.5)
  * `GetEstimatedAudioBitrate` (Impact: 26.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 127`, `args: 28`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `state_mutation: 119`, `planned_debt: 1`, `duplicate_logic: 9`, `orphaned_logic: 9`
* *Architecture:* `api: 3`, `import: 17`
* *Defense:* `safety: 43`, `doc: 17`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` System.Collections.Generic, MediaBrowser.Controller.Library, System.IO, Jellyfin.Extensions, MediaBrowser.Controller.Extensions, MediaBrowser.Model.Entities, System.Text.RegularExpressions, MediaBrowser.Model.Dto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Controllers/ImageController.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.854 IQR)
- **Top Global Matches:** file_cluster_0: 12.854, file_cluster_13: 13.259, file_cluster_4: 13.326
- **Magnitude:** 659.66 | **LOC:** 2070 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.8272%), Tech Debt (30.9554%)
**Top Internal Functions/Classes:**
  * `GetImageInternal` (Impact: 94.4)
    * *Intent:* /// <summary> /// Get user profile image. /// </summary> /// <param name="userId">User id.</param> /...
  * `PostUserImage` (Impact: 31.1)
    * *Intent:* /// <summary> /// Sets the user image. /// </summary> /// <param name="userId">User Id.</param> /// ...
  * `GetImageResult` (Impact: 24.9)
    * *Intent:* /// <summary> /// Generates or gets the splashscreen. /// </summary>
  * `GetImageInfo` (Impact: 20.5)
  * `GetClientSupportedFormats` (Impact: 16.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 171`, `args: 34`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `state_mutation: 182`, `dead_code: 2`, `orphaned_logic: 20`
* *Architecture:* `io: 8`, `api: 27`, `concurrency: 95`, `import: 35`
* *Defense:* `safety: 43`, `doc: 430`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Net.Mime, System.Drawing, MediaBrowser.Model.Dto, Jellyfin.Api.Helpers, Microsoft.Extensions.Logging, Microsoft.AspNetCore.Mvc, System.Globalization, Jellyfin.Api.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.LiveTv/Listings/SchedulesDirect.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.964 IQR)
- **Top Global Matches:** file_cluster_13: 11.964, file_cluster_8: 12.065, file_cluster_4: 12.106
- **Magnitude:** 638.9 | **LOC:** 815 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.7882%), Tech Debt (72.343%)
**Top Internal Functions/Classes:**
  * `GetProgramsAsync` (Impact: 244.8)
  * `dailySchedules.SelectMany` (Impact: 120.6)
  * `GetHeadends` (Impact: 24.5)
  * `GetChannels` (Impact: 14.7)
  * `GetImageForPrograms` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 170`, `args: 35`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 61`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `api: 10`, `concurrency: 48`, `import: 26`
* *Defense:* `safety: 36`, `doc: 7`, `immutability_locks: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Net.Mime, System.Text.Json, MediaBrowser.Model.Dto, System.Net.Http, Microsoft.Extensions.Logging, MediaBrowser.Controller.Authentication, System.Globalization, AsyncKeyedLock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Subtitles/SubtitleEncoder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.852 IQR)
- **Top Global Matches:** file_cluster_13: 12.852, file_cluster_4: 12.864, file_cluster_8: 12.889
- **Magnitude:** 610.6 | **LOC:** 1054 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (30.8809%), Tech Debt (24.4136%)
**Top Internal Functions/Classes:**
  * `ConvertTextSubtitleToSrtInternal` (Impact: 57.2)
  * `ExtractTextSubtitleInternal` (Impact: 57.2)
  * `ExtractSubtitlesForFile` (Impact: 54.7)
  * `ExtractAllExtractableSubtitlesMKS` (Impact: 35.2)
  * `ExtractAllExtractableSubtitlesInternal` (Impact: 26.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 149`, `args: 37`, `func_start: 110`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 127`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 19`, `api: 11`, `concurrency: 85`, `import: 27`
* *Defense:* `safety: 49`, `doc: 41`, `immutability_locks: 14`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MediaBrowser.Model.Dto, MediaBrowser.Model.MediaInfo, System.Net.Http, Microsoft.Extensions.Logging, System.Globalization, AsyncKeyedLock, System.Collections.Generic, MediaBrowser.Controller.Library...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.LiveTv/Channels/ChannelManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.375 IQR)
- **Top Global Matches:** file_cluster_13: 13.375, file_cluster_4: 13.443, file_cluster_17: 13.506
- **Magnitude:** 590.6 | **LOC:** 1216 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.0482%), Tech Debt (98.8931%)
**Top Internal Functions/Classes:**
  * `GetChannelItemEntityAsync` (Impact: 118.6)
  * `GetChannelsInternalAsync` (Impact: 61.7)
    * *Intent:* /// <inheritdoc />
  * `GetChannel` (Impact: 15.7)
  * `RefreshChannels` (Impact: 11.9)
    * *Intent:* /// <summary> /// Refreshes the associated channels. /// </summary> /// <param name="progress">The p...
  * `Dispose` (Impact: 10.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 166`, `args: 62`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `state_mutation: 147`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 9`
* *Architecture:* `io: 6`, `api: 18`, `concurrency: 76`, `import: 29`
* *Defense:* `safety: 59`, `doc: 53`, `immutability_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` System.Text.Json, MediaBrowser.Model.Dto, MediaBrowser.Model.Channels, Microsoft.Extensions.Logging, MediaBrowser.Controller.Entities.TV.Series, MediaBrowser.Model.Querying, Jellyfin.Database.Implementations.Entities, MediaBrowser.Controller.Channels...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Helpers/DynamicHlsHelper.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.126 IQR)
- **Top Global Matches:** file_cluster_13: 12.126, file_cluster_8: 12.179, file_cluster_7: 12.415
- **Magnitude:** 575.72 | **LOC:** 921 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.5704%), Tech Debt (22.234%)
**Top Internal Functions/Classes:**
  * `AppendPlaylistSupplementalCodecsField` (Impact: 148.7)
    * *Intent:* /// <summary> /// Appends a SUPPLEMENTAL-CODECS field containing formatted strings of /// the active...
  * `GetMasterPlaylistInternal` (Impact: 86.6)
  * `GetPlaylistAudioCodecs` (Impact: 34.1)
  * `GetBitrateVariation` (Impact: 33.1)
  * `GetPlaylistVideoCodecs` (Impact: 28.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 131`, `args: 21`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 82`, `fragile_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `concurrency: 7`, `import: 28`
* *Defense:* `safety: 36`, `doc: 81`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Microsoft.Extensions.Logging, Microsoft.AspNetCore.Mvc, MediaBrowser.Controller.Streaming, Jellyfin.Database.Implementations.Entities, System.Globalization, Jellyfin.Api.Extensions, System.Collections.Generic, MediaBrowser.Controller.Library...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.LocalMetadata/Parsers/BaseItemXmlParser.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.928 IQR)
- **Top Global Matches:** file_cluster_8: 10.928, file_cluster_13: 11.204, file_cluster_7: 11.235
- **Magnitude:** 560.18 | **LOC:** 873 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.7633%), Tech Debt (49.1837%)
**Top Internal Functions/Classes:**
  * `FetchDataFromXmlNode` (Impact: 253.2)
    * *Intent:* /// <summary> /// Fetches metadata from one Xml Element. /// </summary> /// <param name="reader">The...
  * `GetLinkedChild` (Impact: 28.8)
    * *Intent:* /// <summary> /// Get linked child. /// </summary> /// <param name="reader">The xml reader.</param> ...
  * `GetShare` (Impact: 28.8)
    * *Intent:* /// <summary> /// Get share. /// </summary> /// <param name="reader">The xml reader.</param> /// <re...
  * `FetchFromSharesNode` (Impact: 25.0)
  * `FetchDataFromPersonsNode` (Impact: 22.4)
    * *Intent:* /// <summary> /// Fetches the data from persons node. /// </summary> /// <param name="reader">The re...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 93`, `args: 16`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 61`, `duplicate_logic: 6`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 3`, `import: 16`
* *Defense:* `safety: 10`, `doc: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Threading, System.Collections.Generic, System.IO, Jellyfin.Extensions, MediaBrowser.Controller.Extensions, MediaBrowser.Model.Entities, System.Text, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Emby.Server.Implementations/Playlists/PlaylistManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.546 IQR)
- **Top Global Matches:** file_cluster_4: 12.546, file_cluster_13: 12.557, file_cluster_17: 12.588
- **Magnitude:** 545.12 | **LOC:** 689 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (58.7299%), Tech Debt (96.2386%)
**Top Internal Functions/Classes:**
  * `SavePlaylistFile` (Impact: 79.5)
    * *Intent:* /// <inheritdoc />
  * `CreatePlaylist` (Impact: 56.0)
  * `AddToPlaylistInternal` (Impact: 28.1)
  * `MoveItemAsync` (Impact: 27.0)
  * `UpdatePlaylist` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 141`, `args: 52`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 117`, `duplicate_logic: 9`, `orphaned_logic: 10`
* *Architecture:* `io: 14`, `api: 16`, `concurrency: 56`, `import: 24`
* *Defense:* `safety: 39`, `doc: 4`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Microsoft.Extensions.Logging, MediaBrowser.Model.Playlists, Jellyfin.Database.Implementations.Entities, System.Globalization, System.Collections.Generic, MediaBrowser.Controller.Library, System.IO, MediaBrowser.Controller.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.Networking/Manager/NetworkManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.402 IQR)
- **Top Global Matches:** file_cluster_13: 13.402, file_cluster_17: 13.493, file_cluster_8: 13.552
- **Magnitude:** 535.28 | **LOC:** 1178 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (26.9328%), Tech Debt (80.4138%)
**Top Internal Functions/Classes:**
  * `InitializeOverrides` (Impact: 43.7)
    * *Intent:* /// <summary> /// Parses the user defined overrides into the dictionary object. /// Overrides are th...
  * `GetInterfacesCore` (Impact: 29.8)
    * *Intent:* /// <summary> /// Generate a list of all the interface ip addresses and submasks where that are in t...
  * `FilterBindSettings` (Impact: 27.5)
    * *Intent:* /// <summary> /// Filters a list of bind addresses and exclusions on available interfaces. /// </sum...
  * `GetBindAddress` (Impact: 27.5)
    * *Intent:* /// <inheritdoc/>
  * `GetAllBindInterfaces` (Impact: 24.0)
    * *Intent:* /// <summary> /// Reads the jellyfin configuration of the configuration manager and produces a list ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 150`, `args: 64`, `func_start: 110`, `class_start: 1`
* *Risk/State:* `state_mutation: 201`, `duplicate_logic: 8`, `orphaned_logic: 5`
* *Architecture:* `api: 22`, `concurrency: 1`, `import: 17`
* *Defense:* `safety: 29`, `doc: 124`, `sync_locks: 8`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` System.Threading, System.Collections.Generic, Microsoft.AspNetCore.Http, System.Net.Sockets, System.Net.NetworkInformation, MediaBrowser.Model.Net, System.Net, MediaBrowser.Common.Configuration.IConfigurationManager...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Controllers/DynamicHlsController.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.491 IQR)
- **Top Global Matches:** file_cluster_0: 13.491, file_cluster_13: 13.518, file_cluster_4: 13.796
- **Magnitude:** 528.66 | **LOC:** 2082 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (31.1408%), Tech Debt (36.3013%)
**Top Internal Functions/Classes:**
  * `GetAudioArguments` (Impact: 63.9)
  * `GetVideoArguments` (Impact: 57.3)
  * `GetSegmentResult` (Impact: 54.6)
    * *Intent:* /// <param name="playSessionId">The play session id.</param> /// <param name="segmentContainer">The ...
  * `GetCommandLineArguments` (Impact: 39.7)
    * *Intent:* /// <param name="enableAutoStreamCopy">Whether or not to allow automatic stream copy if requested va...
  * `_transcodeManager.LockAsync` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 141`, `args: 24`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `state_mutation: 187`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 19`, `api: 4`, `concurrency: 27`, `import: 32`
* *Defense:* `safety: 61`, `doc: 88`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Jellyfin.Api.Helpers, Microsoft.Extensions.Logging, Microsoft.AspNetCore.Mvc, MediaBrowser.Controller.Streaming, System.Globalization, Jellyfin.Api.Extensions, System.Collections.Generic, MediaBrowser.Controller.Library...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Controller/Entities/UserViewBuilder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.904 IQR)
- **Top Global Matches:** file_cluster_8: 10.904, file_cluster_17: 11.071, file_cluster_13: 11.181
- **Magnitude:** 524.1 | **LOC:** 1028 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (20.9622%), Tech Debt (35.4765%)
**Top Internal Functions/Classes:**
  * `Filter` (Impact: 263.2)
  * `GetUserItems` (Impact: 53.2)
  * `SortAndPage` (Impact: 17.1)
  * `GetMediaFolders` (Impact: 11.4)
  * `GetMovieGenres` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 209`, `args: 51`, `func_start: 111`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `dead_code: 3`, `duplicate_logic: 5`, `orphaned_logic: 3`
* *Architecture:* `api: 8`, `import: 14`
* *Defense:* `safety: 37`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Controller.Entities.TV.Episode, System.Collections.Generic, MediaBrowser.Controller.Library, MediaBrowser.Controller.TV, Jellyfin.Extensions, MediaBrowser.Model.Entities, Jellyfin.Database.Implementations.Enums, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.LiveTv/Recordings/RecordingsManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.513 IQR)
- **Top Global Matches:** file_cluster_13: 12.513, file_cluster_4: 12.591, file_cluster_8: 12.639
- **Magnitude:** 523.06 | **LOC:** 839 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.2382%), Tech Debt (17.0631%)
**Top Internal Functions/Classes:**
  * `RecordStream` (Impact: 32.1)
    * *Intent:* /// <inheritdoc />
  * `RemovePathFromLibraryAsync` (Impact: 29.1)
  * `CreateRecordingFolders` (Impact: 25.6)
    * *Intent:* /// <inheritdoc />
  * `GetRecordingPath` (Impact: 24.8)
  * `EnforceKeepUpTo` (Impact: 21.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 146`, `args: 37`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `state_mutation: 146`, `orphaned_logic: 6`
* *Architecture:* `io: 27`, `api: 9`, `concurrency: 66`, `import: 33`
* *Defense:* `safety: 36`, `doc: 24`, `immutability_locks: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.Model.Dto, MediaBrowser.Model.MediaInfo, System.Net.Http, Microsoft.Extensions.Logging, System.Globalization, AsyncKeyedLock, MediaBrowser.Controller.Entities.TV, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Controller/Entities/Folder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.683 IQR)
- **Top Global Matches:** file_cluster_13: 12.683, file_cluster_8: 12.801, file_cluster_0: 12.903
- **Magnitude:** 521.8 | **LOC:** 1882 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 46.7%
- **Risk Profile:** Cognitive Load (17.1756%), Tech Debt (31.472%)
**Top Internal Functions/Classes:**
  * `RequiresPostFiltering` (Impact: 47.6)
  * `IsLibraryFolderAccessible` (Impact: 26.6)
  * `FillUserDataDtoValues` (Impact: 24.1)
  * `QueryWithPostFiltering2` (Impact: 22.4)
  * `QueryRecursive` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 170`, `args: 63`, `func_start: 107`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 105`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `api: 42`, `concurrency: 40`, `import: 28`
* *Defense:* `safety: 34`, `doc: 103`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MediaBrowser.Model.Dto, Microsoft.Extensions.Logging, Jellyfin.Data, MediaBrowser.Controller.Entities.TV.Series, MediaBrowser.Model.Querying, MediaBrowser.Controller.Channels, Jellyfin.Database.Implementations.Entities, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Providers/Plugins/Tmdb/TmdbClientManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.025 IQR)
- **Top Global Matches:** file_cluster_4: 14.025, file_cluster_13: 14.117, file_cluster_16: 14.323
- **Magnitude:** 483.72 | **LOC:** 719 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (48.3569%), Tech Debt (84.7288%)
**Top Internal Functions/Classes:**
  * `GetSeriesGroupAsync` (Impact: 47.2)
    * *Intent:* /// <summary> /// Gets a tv show episode group from the TMDb API based on the show id and the displa...
  * `ValidatePreferences` (Impact: 43.9)
  * `GetEpisodeAsync` (Impact: 35.0)
    * *Intent:* /// <summary> /// Gets a tv season from the TMDb API based on the tv show's TMDb id. /// </summary> ...
  * `SearchCollectionAsync` (Impact: 16.7)
  * `GetMovieAsync` (Impact: 16.2)
    * *Intent:* /// <summary> /// Gets a movie from the TMDb API based on its TMDb id. /// </summary> /// <param nam...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 100`, `args: 36`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `state_mutation: 78`, `duplicate_logic: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 19`, `concurrency: 111`, `import: 17`
* *Defense:* `safety: 37`, `doc: 142`, `immutability_locks: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Threading, TMDbLib.Objects.Movies, System.Collections.Generic, MediaBrowser.Model.Entities, TMDbLib.Objects.General, MediaBrowser.Model.Dto, TMDbLib.Client, TMDbLib.Objects.People...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.XbmcMetadata/Parsers/BaseNfoParser.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.965 IQR)
- **Top Global Matches:** file_cluster_13: 10.965, file_cluster_8: 11.06, file_cluster_7: 11.324
- **Magnitude:** 480.86 | **LOC:** 1020 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (11.1241%), Tech Debt (37.9905%)
**Top Internal Functions/Classes:**
  * `Fetch` (Impact: 245.7)
    * *Intent:* /// <summary> /// Fetches the specified item. /// </summary> /// <param name="item">The <see cref="M...
  * `FetchFromVideoNode` (Impact: 51.7)
  * `FetchFromRatingNode` (Impact: 30.2)
  * `FetchFromRatingsNode` (Impact: 23.1)
  * `FetchFromStreamDetailsNode` (Impact: 22.5)
    * *Intent:* /// <summary>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 77`, `args: 15`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 4`, `import: 22`
* *Defense:* `safety: 7`, `doc: 42`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MediaBrowser.XbmcMetadata.Savers, Microsoft.Extensions.Logging, System.Xml, MediaBrowser.Controller.Entities.TV, System.Globalization, System.Collections.Generic, MediaBrowser.Controller.Library, System.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Emby.Server.Implementations/Localization/LocalizationManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.399 IQR)
- **Top Global Matches:** file_cluster_13: 12.399, file_cluster_8: 12.624, file_cluster_17: 12.658
- **Magnitude:** 471.94 | **LOC:** 563 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (32.7676%), Tech Debt (94.8017%)
**Top Internal Functions/Classes:**
  * `GetLocalizationOptions` (Impact: 147.7)
    * *Intent:* // Handle prefix country code to handle "DE-18"
  * `GetParentalRatings` (Impact: 38.6)
    * *Intent:* /// <inheritdoc />
  * `LoadCultures` (Impact: 36.8)
  * `reader.ReadAllLinesAsync` (Impact: 36.7)
  * `LoadAll` (Impact: 26.3)
    * *Intent:* /// <summary> /// Loads all resources into memory. /// </summary> /// <returns><see cref="Task" />.<...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 218`, `args: 25`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 76`, `planned_debt: 1`, `orphaned_logic: 12`
* *Architecture:* `api: 10`, `concurrency: 8`, `import: 16`
* *Defense:* `safety: 23`, `doc: 27`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Generic, MediaBrowser.Controller.Configuration, System.IO, Jellyfin.Extensions, MediaBrowser.Model.Entities, System.Text.Json, System.Linq, Microsoft.Extensions.Logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Providers/Manager/ItemImageProvider.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.059 IQR)
- **Top Global Matches:** file_cluster_13: 12.059, file_cluster_8: 12.085, file_cluster_4: 12.341
- **Magnitude:** 469.68 | **LOC:** 750 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.9347%), Tech Debt (60.8539%)
**Top Internal Functions/Classes:**
  * `DownloadMultiImages` (Impact: 73.7)
  * `RefreshFromProvider` (Impact: 48.9)
    * *Intent:* /// <summary> /// Refreshes from a dynamic provider. /// </summary>
  * `RefreshFromProvider` (Impact: 42.5)
    * *Intent:* /// <summary> /// Refreshes from a remote provider. /// </summary> /// <param name="item">The item.<...
  * `images.Where` (Impact: 42.1)
  * `DownloadImage` (Impact: 37.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 124`, `args: 28`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`, `duplicate_logic: 4`, `orphaned_logic: 6`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 31`, `import: 23`
* *Defense:* `safety: 36`, `doc: 57`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` System.Net.Mime, MediaBrowser.Model.MediaInfo, System.Net.Http, Microsoft.Extensions.Logging, MediaBrowser.Controller.Entities.TV, System.Collections.Generic, MediaBrowser.Controller.Library, System.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/Jellyfin.Providers.Tests/MediaInfo/EmbeddedImageProviderTests.cs` (CSHARP) | Magnitude: 78.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 56, func_start: 26, generics: 26
- `Jellyfin.Api/Controllers/PluginsController.cs` (CSHARP) | Magnitude: 70.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 136, doc: 70, structural_boundaries: 55, func_start: 31
- `MediaBrowser.Controller/Entities/AudioBook.cs` (CSHARP) | Magnitude: 33.02 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 15, api: 13, args: 9
- `MediaBrowser.Controller/Entities/TV/Episode.cs` (CSHARP) | Magnitude: 217.1 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 266, structural_boundaries: 74, branch: 47, state_mutation: 45
- `tests/Jellyfin.Model.Tests/Extensions/StringHelperTests.cs` (CSHARP) | Magnitude: 8.68 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, decorators: 7, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `MediaBrowser.Model/Tasks/ITaskTrigger.cs` (CSHARP) | Magnitude: 24.56 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 19, indent_spaces: 7, structural_boundaries: 5, args: 2
- `src/Jellyfin.Drawing.Skia/UnplayedCountIndicator.cs` (CSHARP) | Magnitude: 16.68 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, doc: 15, structural_boundaries: 12, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/BaseItemEntity.cs` (CSHARP) | Magnitude: 187.86 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: api: 86, state_mutation: 85, indent_spaces: 85, generics: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `MediaBrowser.Controller/Drawing/IImageEncoder.cs` (CSHARP) | Magnitude: 38.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 62, indent_spaces: 14, args: 6, func_start: 6
- `Jellyfin.Api/Controllers/ScheduledTasksController.cs` (CSHARP) | Magnitude: 40.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 85, doc: 43, structural_boundaries: 32, func_start: 21
- `MediaBrowser.Providers/Lyric/LyricManager.cs` (CSHARP) | Magnitude: 286.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 347, structural_boundaries: 137, func_start: 65, concurrency: 59
- `MediaBrowser.Model/Extensions/LibraryOptionsExtension.cs` (CSHARP) | Magnitude: 17.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 14, doc: 8, state_mutation: 6
- `tests/Jellyfin.XbmcMetadata.Tests/Parsers/MovieNfoParserTests.cs` (CSHARP) | Magnitude: 73.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 215, func_start: 98, test: 85, sec_high_risk_execution: 81

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `MediaBrowser.Model/IO/AsyncFile.cs` (CSHARP) | Magnitude: 18.98 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 20, structural_boundaries: 8, api: 6
- `MediaBrowser.Model/Drawing/ImageFormatExtensions.cs` (CSHARP) | Magnitude: 17.16 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 20, args: 16, closures: 16
- `Jellyfin.Server.Implementations/Item/OrderMapper.cs` (CSHARP) | Magnitude: 29.04 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 99, args: 85, closures: 82, indent_spaces: 58

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/Jellyfin.Providers.Tests/Manager/MetadataServiceTests.cs` (CSHARP) | Magnitude: 181.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 282, state_mutation: 102, func_start: 71, sec_high_risk_execution: 60
- `Jellyfin.Api/BaseJellyfinApiController.cs` (CSHARP) | Magnitude: 6.58 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 15, structural_boundaries: 9, generics: 7, indent_spaces: 7
- `Jellyfin.Data/Events/Users/UserCreatedEventArgs.cs` (CSHARP) | Magnitude: 4.3 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, indent_spaces: 6, structural_boundaries: 3, api: 2
- `Jellyfin.Data/Events/Users/UserDeletedEventArgs.cs` (CSHARP) | Magnitude: 4.3 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, indent_spaces: 6, structural_boundaries: 3, api: 2
- `Jellyfin.Data/Events/Users/UserLockedOutEventArgs.cs` (CSHARP) | Magnitude: 4.3 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, indent_spaces: 6, structural_boundaries: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Jellyfin.LiveTv/LiveTvManager.cs` (CSHARP) | Magnitude: 847.1 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 999, structural_boundaries: 311, state_mutation: 278, branch: 139
- `Emby.Naming/AudioBook/AudioBookListResolver.cs` (CSHARP) | Magnitude: 85.12 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 45, state_mutation: 22, branch: 20
- `MediaBrowser.Providers/Plugins/Tmdb/Configuration/config.html` (HTML) | Magnitude: 57.78 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 42, ui_framework: 42, args: 30
- `Emby.Server.Implementations/Dto/DtoService.cs` (CSHARP) | Magnitude: 1199.68 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1092, branch: 260, structural_boundaries: 183, safety: 128
- `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` (CSHARP) | Magnitude: 391.98 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 485, structural_boundaries: 241, args: 135, state_mutation: 124

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `MediaBrowser.Providers/Plugins/StudioImages/Configuration/config.html` (HTML) | Magnitude: 30.06 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 14, args: 9, concurrency: 8
- `MediaBrowser.Providers/Plugins/MusicBrainz/Configuration/config.html` (HTML) | Magnitude: 33.4 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 18, args: 14, ui_framework: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Emby.Server.Implementations/Session/SessionManager.cs` (CSHARP) | Magnitude: 1474.4 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1571, state_mutation: 369, structural_boundaries: 301, func_start: 271
- `Emby.Server.Implementations/Playlists/PlaylistManager.cs` (CSHARP) | Magnitude: 545.12 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 535, structural_boundaries: 141, state_mutation: 117, branch: 99
- `src/Jellyfin.LiveTv/Listings/SchedulesDirectDtos/MapDto.cs` (CSHARP) | Magnitude: 38.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 27, indent_spaces: 19, api: 9, state_mutation: 8
- `src/Jellyfin.LiveTv/LiveTvMediaSourceProvider.cs` (CSHARP) | Magnitude: 204.02 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 237, structural_boundaries: 59, concurrency: 48, branch: 39
- `tests/Jellyfin.Server.Integration.Tests/Controllers/PluginsControllerTests.cs` (CSHARP) | Magnitude: 37.22 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 18, concurrency: 13, sec_high_risk_execution: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `Emby.Naming/Video/StubTypeRule.cs` (CSHARP) | Magnitude: 10.26 | Delta: **0.146 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 16, indent_spaces: 10, api: 4, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Emby.Naming/Video/Format3DResult.cs` (CSHARP) | Magnitude: 8.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 16, indent_spaces: 10, api: 4, structural_boundaries: 2
- `Jellyfin.Api/Constants/UserRoles.cs` (CSHARP) | Magnitude: 17.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, api: 4, immutability_locks: 3, indent_spaces: 3
- `Jellyfin.Api/Models/SyncPlayDtos/NewGroupRequestDto.cs` (CSHARP) | Magnitude: 7.08 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, indent_spaces: 5, api: 3, structural_boundaries: 2
- `MediaBrowser.Model/Lyrics/RemoteLyricInfoDto.cs` (CSHARP) | Magnitude: 18.64 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 7, api: 4, safety: 3
- `src/Jellyfin.MediaEncoding.Hls/Playlist/CreateMainPlaylistRequest.cs` (CSHARP) | Magnitude: 21.98 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 38, indent_spaces: 19, api: 10, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Emby.Naming/Common/MediaType.cs` (CSHARP) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 12, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2
- `MediaBrowser.Controller/IServerApplicationPaths.cs` (CSHARP) | Magnitude: 16.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 47, indent_spaces: 15, structural_boundaries: 7, import: 5
- `MediaBrowser.Controller/Providers/RefreshPriority.cs` (CSHARP) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 12, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2
- `MediaBrowser.Model/SyncPlay/GroupRepeatMode.cs` (CSHARP) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 12, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2
- `MediaBrowser.Model/Configuration/MetadataOptions.cs` (CSHARP) | Magnitude: 24.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, state_mutation: 13, api: 9, structural_boundaries: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` -> Churn: **100.0%** | Cog Load: 31.1724% | Debt: 99.9839%
- `MediaBrowser.Controller/Entities/BaseItem.cs` -> Churn: **75.17%** | Cog Load: 19.0333% | Debt: 99.9758%
- `MediaBrowser.MediaEncoding/Probing/ProbeResultNormalizer.cs` -> Churn: **74.28%** | Cog Load: 44.8147% | Debt: 98.974%
- `Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs` -> Churn: **74.1%** | Cog Load: 67.9076% | Debt: 99.9208%
- `Jellyfin.Server.Implementations/Item/PeopleRepository.cs` -> Churn: **50.37%** | Cog Load: 26.4431% | Debt: 88.3151%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Jellyfin.LiveTv/LiveTvManager.cs` -> **evan314159** (100.0% isolated ownership) | Magnitude: 847.1
- `src/Jellyfin.LiveTv/Channels/ChannelManager.cs` -> **evan314159** (100.0% isolated ownership) | Magnitude: 590.6
- `Jellyfin.Api/Helpers/DynamicHlsHelper.cs` -> **nyanmisaka** (100.0% isolated ownership) | Magnitude: 575.72
- `MediaBrowser.Providers/Manager/ItemImageProvider.cs` -> **theguymadmax** (100.0% isolated ownership) | Magnitude: 469.68
- `MediaBrowser.Providers/MediaInfo/FFProbeVideoInfo.cs` -> **IceStormNG** (100.0% isolated ownership) | Magnitude: 416.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `MediaBrowser.Controller/Entities/Audio/Audio.cs` -> **Severity: 1804.956** (Blast Radius: 20.944 * Doc Risk: 86.1801%)
- `MediaBrowser.Model/MediaInfo/MediaInfo.cs` -> **Severity: 1342.982** (Blast Radius: 13.569 * Doc Risk: 98.9743%)
- `src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/Libraries/Library.cs` -> **Severity: 704.68** (Blast Radius: 59.116 * Doc Risk: 11.9203%)
- `MediaBrowser.Controller/Entities/Extensions.cs` -> **Severity: 669.468** (Blast Radius: 56.162 * Doc Risk: 11.9203%)
- `src/Jellyfin.LiveTv/TunerHosts/HdHomerun/Channels.cs` -> **Severity: 519.469** (Blast Radius: 5.196 * Doc Risk: 99.9748%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
