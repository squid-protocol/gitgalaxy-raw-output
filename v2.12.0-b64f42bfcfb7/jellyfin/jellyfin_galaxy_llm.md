# ARCHITECTURAL_BRIEF: jellyfin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jellyfin/jellyfin.git` |
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
- **Scope:** 2223 analyzed artifact(s), 188639 LOC.
- **Load-bearing artifact:** `src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/Libraries/Library.cs` -- 299 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Emby.Server.Implementations/ApplicationHost.cs` -- pulls in 102 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` at magnitude 5150.32 (structural weight, not risk).
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
| Total Artifacts | 2334 |
| Analyzed Artifacts (Scanned) | 2223 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 111 |
| Total LOC | 188639 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 95.2% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5412 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2247 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3059 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 103 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 1934 | 161633 | 87.0% |
| JSON | 235 | 25687 | 10.6% |
| PLAINTEXT | 19 | 0 | 0.9% |
| YAML | 11 | 698 | 0.5% |
| MARKDOWN | 8 | 0 | 0.4% |
| HTML | 7 | 591 | 0.3% |
| XML | 5 | 0 | 0.2% |
| CSS | 2 | 14 | 0.1% |
| SHELL | 2 | 16 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2185 |
| utf-8 | bom | 38 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 27%, State Mutators Files 19%, Data / Markup / Trivial 17%, Large Core Modules (2) 7%, Generic / Templated Code Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2193 | 98.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 27 | 1.2% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 111*

**Composition by Extension & Reason:**
- `.csproj`: 32x Excluded (Unsupported Extension: '.csproj'), 10x Unsupported Format (.csproj)
- `.cs`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 1596 LOC), 2x Excluded (Machine-Generated Source Code Signature: 1611 LOC)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace'), 1x Unsupported Format (.undeterminable)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.props`: 3x Excluded (Unsupported Extension: '.props'), 1x Unsupported Format (.props)
- `.nfo`: 1x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (Saturation: Line 35 exceeds 500 chars), 1x Excluded (Saturation: Line 12 exceeds 500 chars)
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 16938 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2399 LOC)
- `.srt`: 2x Excluded (Unsupported Extension: '.srt')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (Saturation: Line 48 exceeds 500 chars)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.sln`: 1x Excluded (Unsupported Extension: '.sln')
- `.dotsettings`: 1x Excluded (Unsupported Extension: '.DotSettings')
- `.ass`: 1x Excluded (Unsupported Extension: '.ass')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.5 | 6.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.4 | 30.9 | 47.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 17.0 | 5.2 | 5.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 94.1 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.2 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 20.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 306 | 143 | 0 | `Emby.Server.Implementations/Library/LibraryManager.cs` |
| cleanup | 197 | 79 | 0 | `Emby.Server.Implementations/ScheduledTasks/ScheduledTaskWorker.cs` |
| guards | 13855 | 1064 | 14 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| danger | 1482 | 718 | 1 | `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` |
| concurrency | 5005 | 461 | 5 | `Emby.Server.Implementations/Session/SessionManager.cs` |
| connectivity | 12113 | 1916 | 11 | `MediaBrowser.Controller/Entities/BaseItem.cs` |
| io | 1188 | 248 | 1 | `Emby.Server.Implementations/Library/LibraryManager.cs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` |
| time | 439 | 157 | 0 | `src/Jellyfin.Database/Jellyfin.Database.Implementations/Locking/OptimisticLockBehavior.cs` |
| serialization | 118 | 41 | 0 | `tests/Jellyfin.Extensions.Tests/Json/Converters/JsonCommaDelimitedCollectionTests.cs` |
| regex | 13 | 9 | 0 | `Emby.Naming/Book/BookFileNameParser.cs` |
| events | 1849 | 262 | 1 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| tests | 2592 | 163 | 0 | `tests/Jellyfin.MediaEncoding.Tests/Probing/ProbeResultNormalizerTests.cs` |
| docs | 38540 | 1568 | 40 | `Jellyfin.Api/Controllers/ImageController.cs` |
| debt | 242 | 127 | 0 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| mutation | 37574 | 1360 | 38 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| dead_code | 3096 | 1033 | 4 | `MediaBrowser.Controller/Entities/BaseItem.cs` |
| credential | 39 | 14 | 0 | `Emby.Naming/Common/NamingOptions.cs` |
| threat | 89 | 8 | 0 | `Emby.Server.Implementations/Localization/Core/fa.json` |
| ml_ai | 202 | 69 | 0 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| ui | 86 | 9 | 0 | `MediaBrowser.Providers/Plugins/Tmdb/Configuration/config.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Emby.Server.Implementations/Library/LibraryManager.cs` (Hits: 49)
- `Emby.Server.Implementations/IO/ManagedFileSystem.cs` (Hits: 32)
- `src/Jellyfin.LiveTv/Recordings/RecordingsManager.cs` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Library.cs** (`src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/Libraries/Library.cs`) — 299 inbound connections
2. **Extensions.cs** (`MediaBrowser.Controller/Entities/Extensions.cs`) — 232 inbound connections
3. **Audio.cs** (`MediaBrowser.Controller/Entities/Audio/Audio.cs`) — 102 inbound connections
4. **MediaInfo.cs** (`MediaBrowser.Model/MediaInfo/MediaInfo.cs`) — 64 inbound connections
5. **LibraryManager.cs** (`Emby.Server.Implementations/Library/LibraryManager.cs`) — 35 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ApplicationHost.cs** (`Emby.Server.Implementations/ApplicationHost.cs`) — 102 outbound dependencies
2. **LibraryManager.cs** (`Emby.Server.Implementations/Library/LibraryManager.cs`) — 54 outbound dependencies
3. **ProviderManager.cs** (`MediaBrowser.Providers/Manager/ProviderManager.cs`) — 41 outbound dependencies
4. **SessionManager.cs** (`Emby.Server.Implementations/Session/SessionManager.cs`) — 40 outbound dependencies
5. **LibraryController.cs** (`Jellyfin.Api/Controllers/LibraryController.cs`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ApplyTranscodingConditions` **(Many-Argument Workhorses)** (@ `MediaBrowser.Model/Dlna/StreamBuilder.cs`) -> Impact: **532.2** | LOC: 503
- `TranslateQuery` **(Many-Argument Workhorses)** (@ `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs`) -> Impact: **425.3** | LOC: 946
- `GetItems` **(Many-Argument Workhorses)** (@ `Jellyfin.Api/Controllers/ItemsController.cs`) -> Impact: **390.2** | LOC: 343
  * *Intent:* /// <param name="minWidth">Optional. Filter by the minimum width of the item.</param> /// <param name="minHeight">Optional. Filter by the minimum heig...
- `FetchDataFromXmlNode` **(Many-Argument Workhorses)** (@ `MediaBrowser.XbmcMetadata/Parsers/BaseNfoParser.cs`) -> Impact: **272.5** | LOC: 393
  * *Intent:* /// <summary> /// Fetches metadata from an XML node. /// </summary> /// <param name="reader">The <see cref="XmlReader"/>.</param> /// <param name="ite...
- `Filter` **(Many-Argument Workhorses)** (@ `MediaBrowser.Controller/Entities/UserViewBuilder.cs`) -> Impact: **263.7** | LOC: 473
- `AttachBasicFields` **(Many-Argument Workhorses)** (@ `Emby.Server.Implementations/Dto/DtoService.cs`) -> Impact: **254.3** | LOC: 524
  * *Intent:* /// <summary> /// Sets simple property values on a DTOBaseItem. /// </summary> /// <param name="dto">The dto.</param> /// <param name="item">The item....
- `GetPostedPlaybackInfo` **(Many-Argument Workhorses)** (@ `Jellyfin.Api/Controllers/MediaInfoController.cs`) -> Impact: **254.1** | LOC: 134
  * *Intent:* /// <param name="subtitleStreamIndex">The subtitle stream index.</param> /// <param name="maxAudioChannels">The maximum number of audio channels.</par...
- `FetchDataFromXmlNode` **(Many-Argument Workhorses)** (@ `MediaBrowser.LocalMetadata/Parsers/BaseItemXmlParser.cs`) -> Impact: **253.2** | LOC: 387
  * *Intent:* /// <summary> /// Fetches metadata from one Xml Element. /// </summary> /// <param name="reader">The reader.</param> /// <param name="itemResult">The ...
- `BuildStreamVideoItem` **(Many-Argument Workhorses)** (@ `MediaBrowser.Model/Dlna/StreamBuilder.cs`) -> Impact: **241.4** | LOC: 211
- `AddCommonNodes` **(Many-Argument Workhorses)** (@ `MediaBrowser.XbmcMetadata/Savers/BaseNfoSaver.cs`) -> Impact: **200.0** | LOC: 349
  * *Intent:* /// <summary> /// Adds the common nodes. /// </summary>

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Jellyfin.Api/Controllers` | 59 | 9665.74 | 16.95% | 52.63% |
| `MediaBrowser.Controller/MediaEncoding` | 16 | 6057.17 | 10.83% | 18.51% |
| `MediaBrowser.Controller/Entities` | 46 | 4791.8 | 10.76% | 41.99% |
| `Emby.Server.Implementations/Library` | 17 | 3918.6 | 27.26% | 34.01% |
| `MediaBrowser.Model/Dlna` | 24 | 3070.64 | 4.45% | 11.57% |
| `Jellyfin.Server.Implementations/Item` | 7 | 2585.78 | 25.38% | 59.39% |
| `MediaBrowser.Providers/Manager` | 5 | 2486.9 | 27.15% | 17.55% |
| `Jellyfin.Server/Migrations/Routines` | 29 | 2341.42 | 16.8% | 28.48% |
| `src/Jellyfin.LiveTv` | 4 | 2269.94 | 77.92% | 34.42% |
| `Jellyfin.Api/Helpers` | 8 | 1887.72 | 27.78% | 48.14% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `MediaBrowser.Controller/BaseItemManager/BaseItemManager.cs` -> **100.0%** Exposure
- `MediaBrowser.Controller/Extensions/ConfigurationExtensions.cs` -> **100.0%** Exposure
- `MediaBrowser.Controller/IO/IPathManager.cs` -> **99.9999%** Exposure
- `Jellyfin.Api/Extensions/ClaimsPrincipalExtensions.cs` -> **99.999%** Exposure
- `.github/workflows/release-bump-version.yaml` -> **99.9989%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Emby.Naming/Common/EpisodeExpression.cs` -> **100.0%** Exposure
- `Emby.Naming/Video/CleanStringParser.cs` -> **100.0%** Exposure
- `Emby.Photos/PhotoProvider.cs` -> **100.0%** Exposure
- `Emby.Server.Implementations/Dto/DtoService.cs` -> **100.0%** Exposure
- `Jellyfin.Api/Controllers/DisplayPreferencesController.cs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `MediaBrowser.Controller/Entities/BaseItem.cs` -> **44** Orphaned Functions | **0** Duplicates
- `Emby.Server.Implementations/Library/LibraryManager.cs` -> **41** Orphaned Functions | **0** Duplicates
- `Jellyfin.Api/Controllers/LiveTvController.cs` -> **39** Orphaned Functions | **0** Duplicates
- `Jellyfin.Api/Controllers/ImageController.cs` -> **27** Orphaned Functions | **0** Duplicates
- `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` -> **25** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/Jellyfin.LiveTv.Tests/Test Data/SchedulesDirect/token_live_response.json` -> **100.0%** Exposure
- `MediaBrowser.Providers/Plugins/Tmdb/TmdbUtils.cs` -> **99.9833%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11214` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.977)
- **Top Global Matches:** file_cluster_6: 5.977, file_cluster_8: 11.809, file_cluster_4: 13.054
- **Magnitude:** 5150.32 | **LOC:** 7852 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **23**; blast radius 1.411; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.0%), Guard Balance (formerly Safety Score) (58.0%)
- **Documentation Coverage:** 74.7899% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetVideoQualityParam` **(Many-Argument Workhorses)** (Impact: 154.2)
    * *Intent:* /// <summary> /// Gets the video bitrate to specify on the command line. /// </summary> /// <param n...
  * `GetIntelQsvDx11VidFiltersPrefered` **(Many-Argument Workhorses)** (Impact: 151.1)
  * `GetIntelQsvVaapiVidFiltersPrefered` **(Many-Argument Workhorses)** (Impact: 142.9)
  * `GetRkmppVidFiltersPrefered` **(Many-Argument Workhorses)** (Impact: 124.2)
  * `GetIntelVaapiFullVidFiltersPrefered` **(Many-Argument Workhorses)** (Impact: 123.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 472 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1522
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1341`, `structural_boundaries: 1494`, `args: 229`, `func_start: 140`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 578`, `dead_code: 2`, `planned_debt: 7`, `fragile_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `io: 8`, `api: 102`, `concurrency: 1`, `import: 23`
* *Defense:* `safety: 256`, `doc: 209`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.411
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.004643
  * `Imports (Out-Degree: 5):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Common.Configuration, MediaBrowser.Common.Configuration.IConfigurationManager, MediaBrowser.Controller.Extensions, MediaBrowser.Controller.IO...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.159)
- **Top Global Matches:** file_cluster_4: 11.159, file_cluster_6: 12.351, file_cluster_12: 14.566
- **Magnitude:** 2161.2 | **LOC:** 2737 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 47.6%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **35**; blast radius 0.913; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.5%), Guard Balance (formerly Safety Score) (72.0%), Complexity Load (formerly Cognitive Load) (60.6%)
- **Documentation Coverage:** 23.2558% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TranslateQuery` **(Many-Argument Workhorses)** (Impact: 425.3)
  * `Map` **(Many-Argument Workhorses)** (Impact: 112.5)
    * *Intent:* /// <summary> /// Maps a Entity to the DTO. /// </summary> /// <param name="entity">The entity.</par...
  * `Map` **(Defensive Guards)** (Impact: 63.6)
    * *Intent:* /// <summary> /// Maps a Entity to the DTO. /// </summary> /// <param name="dto">The entity.</param>...
  * `ApplyOrder` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `UpdateOrInsertItems` **(Callbacks & Closures)** (Impact: 38.8)
    * *Intent:* /// <inheritdoc cref="IItemRepository"/>
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 317 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 1061
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 743`, `args: 488`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 427`, `dead_code: 13`, `planned_debt: 3`, `fragile_debt: 2`, `unreferenced_by_name: 25`
* *Architecture:* `api: 34`, `concurrency: 23`, `import: 35`
* *Defense:* `safety: 147`, `doc: 77`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.00144
  * `Imports (Out-Degree: 7):` Jellyfin.Data.Enums, Jellyfin.Database.Implementations, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Entities.BaseItemEntity, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, Jellyfin.Extensions.Json, Jellyfin.Server.Implementations.Extensions...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `MediaBrowser.Model/Dlna/StreamBuilder.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.579)
- **Top Global Matches:** file_cluster_8: 8.579, file_cluster_6: 9.234, file_cluster_4: 17.364
- **Magnitude:** 1982.08 | **LOC:** 2400 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 0.545; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (50.7%), Complexity Load (formerly Cognitive Load) (45.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.7%)
- **Documentation Coverage:** 64.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ApplyTranscodingConditions` **(Many-Argument Workhorses)** (Impact: 532.2)
  * `BuildStreamVideoItem` **(Many-Argument Workhorses)** (Impact: 241.4)
  * `BuildVideoItem` **(Defensive Guards)** (Impact: 108.2)
  * `GetSubtitleProfile` **(Many-Argument Workhorses)** (Impact: 71.8)
    * *Intent:* /// <summary> /// Normalizes input container. /// </summary> /// <param name="mediaSource">The <see ...
  * `GetOptimalAudioStream` **(Many-Argument Workhorses)** (Impact: 69.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 137 instances
* *State Mutation (weighted view):* 436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 625`, `structural_boundaries: 320`, `args: 96`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 162`, `planned_debt: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 12`, `import: 12`
* *Defense:* `safety: 203`, `doc: 81`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.545
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.002057
  * `Imports (Out-Degree: 11):` Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Model.Dto, MediaBrowser.Model.Entities, MediaBrowser.Model.Extensions, MediaBrowser.Model.MediaInfo, MediaBrowser.Model.Session, Microsoft.Extensions.Logging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Emby.Server.Implementations/Library/LibraryManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.707)
- **Top Global Matches:** file_cluster_0: 8.707, file_cluster_16: 8.8, file_cluster_4: 9.068
- **Magnitude:** 1905.1 | **LOC:** 3390 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **54**; blast radius 5.895; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Concurrency Surface (formerly Concurrency) (87.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.0%), Guard Balance (formerly Safety Score) (48.4%)
- **Documentation Coverage:** 68.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FillMissingEpisodeNumbersFromPath` **(Many-Argument Workhorses)** (Impact: 54.7)
    * *Intent:* /// <inheritdoc />
  * `FindExtras` **(Stateful Encapsulated Methods)** (Impact: 49.6)
  * `DeleteItem` **(Many-Argument Workhorses)** (Impact: 45.2)
  * `ResolvePath` **(Many-Argument Workhorses)** (Impact: 35.7)
  * `AddVirtualFolder` **(Many-Argument Workhorses)** (Impact: 34.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 122 instances
* *Concurrency (weighted view):* 136
* *State Mutation (weighted view):* 452
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 540`, `args: 218`, `func_start: 136`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 208`, `unreferenced_by_name: 41`
* *Architecture:* `io: 49`, `api: 104`, `concurrency: 66`, `import: 54`
* *Defense:* `safety: 263`, `doc: 190`, `sync_locks: 4`, `immutability_locks: 22`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.895
  * `Choke Point (Betweenness):` 0.001086 | `Ripple Effect (Closeness):` 0.02062
  * `Imports (Out-Degree: 21):` BitFaster.Caching.Lru, Emby.Naming.Common, Emby.Naming.TV, Emby.Naming.TV.EpisodeInfo, Emby.Naming.Video.VideoResolver, Emby.Server.Implementations.Library.Resolvers, Emby.Server.Implementations.Library.Validators, Emby.Server.Implementations.Playlists...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `Emby.Server.Implementations/Session/SessionManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.853)
- **Top Global Matches:** file_cluster_4: 6.853, file_cluster_16: 8.982, file_cluster_15: 9.355
- **Magnitude:** 1393.44 | **LOC:** 2155 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **40**; blast radius 0.842; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.8%), Guard Balance (formerly Safety Score) (56.7%), Complexity Load (formerly Cognitive Load) (38.3%)
- **Documentation Coverage:** 26.2712% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetSessions` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* /// <inheritdoc/>
  * `UpdateNowPlayingItem` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* /// <summary> /// Updates the now playing item id. /// </summary> /// <returns>Task.</returns>
  * `SendPlayCommand` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* /// <inheritdoc />
  * `CreateSessionInfo` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `OnPlaybackStopped` **(Defensive Guards)** (Impact: 30.6)
    * *Intent:* /// <summary> /// Used to report that playback has ended for an item. /// </summary> /// <param name...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 132 instances
* *Concurrency (weighted view):* 174
* *State Mutation (weighted view):* 480
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 306`, `args: 130`, `func_start: 76`, `class_start: 1`
* *Risk/State:* `state_mutation: 216`, `unreferenced_by_name: 18`
* *Architecture:* `api: 52`, `concurrency: 99`, `import: 40`
* *Defense:* `safety: 112`, `doc: 165`, `immutability_locks: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.842
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0009
  * `Imports (Out-Degree: 4):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Data.Queries, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Entities.Security, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `MediaBrowser.Controller/Entities/BaseItem.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.269)
- **Top Global Matches:** file_cluster_0: 8.269, file_cluster_16: 8.369, file_cluster_15: 8.388
- **Magnitude:** 1341.4 | **LOC:** 2689 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **34**; blast radius 0.952; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (81.9%), Debt Markers (formerly Tech Debt) (75.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.8%)
- **Documentation Coverage:** 68.5567% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetVersionInfo` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `GetMediaSourceName` **(Compute Cores)** (Impact: 30.3)
  * `RefreshMetadataForOwnedItem` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `AddImages` **(Defensive Guards)** (Impact: 18.2)
    * *Intent:* /// <summary> /// Adds the images, updating metadata if they already are part of this item. /// </su...
  * `IsParentalAllowed` **(Defensive Guards)** (Impact: 18.1)
    * *Intent:* /// <summary> /// Determines if a given user has access to this item. /// </summary> /// <param name...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 128 instances
* *Concurrency (weighted view):* 82
* *State Mutation (weighted view):* 432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 403`, `args: 178`, `func_start: 109`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 176`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 44`
* *Architecture:* `io: 13`, `api: 198`, `concurrency: 47`, `import: 34`
* *Defense:* `safety: 91`, `doc: 335`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.952
  * `Choke Point (Betweenness):` 0.000268 | `Ripple Effect (Closeness):` 0.008845
  * `Imports (Out-Degree: 18):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Channels, MediaBrowser.Controller.Chapters...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `Jellyfin.Api/Controllers/DynamicHlsController.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.556)
- **Top Global Matches:** file_cluster_6: 9.556, file_cluster_8: 10.812, file_cluster_4: 16.774
- **Magnitude:** 1328.24 | **LOC:** 2082 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **32**; blast radius 0.633; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.5%), Mutation Surface (formerly State Flux) (88.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.8%), Guard Balance (formerly Safety Score) (43.2%)
- **Documentation Coverage:** 54.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetLiveHlsStream` **(Many-Argument Workhorses)** (Impact: 148.7)
    * *Intent:* /// <param name="videoCodec">Optional. Specify a video codec to encode to, e.g. h264.</param> /// <p...
  * `GetHlsAudioSegment` **(Many-Argument Workhorses)** (Impact: 102.3)
    * *Intent:* /// <param name="transcodingMaxAudioChannels">Optional. The maximum number of audio channels to tran...
  * `GetMasterHlsAudioPlaylist` **(Many-Argument Workhorses)** (Impact: 98.4)
    * *Intent:* /// <param name="cpuCoreLimit">Optional. The limit of how many cpu cores to use.</param> /// <param ...
  * `GetVariantHlsAudioPlaylist` **(Many-Argument Workhorses)** (Impact: 97.4)
    * *Intent:* /// <param name="transcodingMaxAudioChannels">Optional. The maximum number of audio channels to tran...
  * `GetHlsVideoSegment` **(Many-Argument Workhorses)** (Impact: 96.7)
    * *Intent:* /// <param name="cpuCoreLimit">Optional. The limit of how many cpu cores to use.</param> /// <param ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 50 instances
* *Concurrency (weighted view):* 106
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 191`, `args: 33`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 73`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 22`, `api: 10`, `concurrency: 51`, `import: 32`
* *Defense:* `safety: 146`, `doc: 431`, `immutability_locks: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.00045
  * `Imports (Out-Degree: 11):` Jellyfin.Api.Attributes, Jellyfin.Api.Extensions, Jellyfin.Api.Helpers, Jellyfin.Api.Models.StreamingDtos, Jellyfin.Data.Enums, Jellyfin.Extensions, Jellyfin.MediaEncoding.Hls.Playlist, MediaBrowser.Common.Configuration...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Emby.Server.Implementations/Dto/DtoService.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.285)
- **Top Global Matches:** file_cluster_6: 7.285, file_cluster_4: 8.414, file_cluster_16: 15.423
- **Magnitude:** 1300.32 | **LOC:** 1512 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.342; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.7%), Guard Balance (formerly Safety Score) (62.7%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AttachBasicFields` **(Many-Argument Workhorses)** (Impact: 254.3)
    * *Intent:* /// <summary> /// Sets simple property values on a DTOBaseItem. /// </summary> /// <param name="dto"...
  * `AddInheritedImages` **(Many-Argument Workhorses)** (Impact: 76.2)
  * `GetBaseItemDtoInternal` **(Many-Argument Workhorses)** (Impact: 45.1)
  * `AttachPeople` **(Many-Argument Workhorses)** (Impact: 41.1)
    * *Intent:* /// <summary> /// Attaches People DTO's to a DTOBaseItem. /// </summary> /// <param name="dto">The d...
  * `AttachUserSpecificInfo` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* /// <summary> /// Attaches the user specific info. /// </summary>
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 173 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 579
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 192`, `args: 83`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 233`, `dead_code: 6`, `planned_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 4`, `import: 33`
* *Defense:* `safety: 134`, `doc: 30`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Extensions, MediaBrowser.Common, MediaBrowser.Controller.Channels, MediaBrowser.Controller.Chapters, MediaBrowser.Controller.Drawing, MediaBrowser.Controller.Dto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Probing/ProbeResultNormalizer.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.387)
- **Top Global Matches:** file_cluster_6: 6.387, file_cluster_4: 7.961, file_cluster_16: 15.132
- **Magnitude:** 1293.22 | **LOC:** 1761 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.488; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.4%), Complexity Load (formerly Cognitive Load) (35.2%)
- **Documentation Coverage:** 62.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetMediaStream` **(Many-Argument Workhorses)** (Impact: 198.5)
    * *Intent:* /// <summary> /// Converts ffprobe stream info to our MediaStream class. /// </summary> /// <param n...
  * `GetMediaInfo` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* /// <summary> /// Transforms a FFprobe response into its <see cref="MediaInfo"/> equivalent. /// </s...
  * `SetAudioInfoFromTags` **(Many-Argument Workhorses)** (Impact: 55.2)
  * `FetchWtvInfo` **(Many-Argument Workhorses)** (Impact: 36.6)
  * `ReadFromDictNode` **(Many-Argument Workhorses)** (Impact: 34.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 231`, `args: 62`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 192`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 17`
* *Defense:* `safety: 67`, `doc: 74`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.488
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00045
  * `Imports (Out-Degree: 4):` Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Controller.Extensions, MediaBrowser.Controller.Library, MediaBrowser.Model.Dto, MediaBrowser.Model.Entities, MediaBrowser.Model.Globalization, MediaBrowser.Model.MediaInfo...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.73)
- **Top Global Matches:** file_cluster_6: 6.73, file_cluster_4: 10.009, file_cluster_8: 16.359
- **Magnitude:** 1220.26 | **LOC:** 1483 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.633; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.6%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetItem` **(Compute Cores)** (Impact: 129.5)
  * `Perform` **(I/O & Config Routines)** (Impact: 62.9)
    * *Intent:* /// <inheritdoc/>
  * `GetMediaStream` **(Compute Cores)** (Impact: 62.9)
    * *Intent:* /// <summary> /// Gets the media stream. /// </summary> /// <param name="reader">The reader.</param>...
  * `ItemImageInfoFromValueString` **(Compute Cores)** (Impact: 26.4)
  * `GetUserData` **(Stateful Encapsulated Methods)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 261 instances
* *State Mutation (weighted view):* 821
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 295`, `args: 39`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 299`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 12`, `import: 23`
* *Defense:* `safety: 8`, `doc: 26`, `immutability_locks: 16`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.00045
  * `Imports (Out-Degree: 4):` Emby.Server.Implementations.Data, Jellyfin.Database.Implementations, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Entities.BaseItemEntity, Jellyfin.Database.Implementations.Entities.Chapter, Jellyfin.Extensions, Jellyfin.Server.Implementations.Item, Jellyfin.Server.ServerSetupApp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `MediaBrowser.Providers/Manager/MetadataService.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.702)
- **Top Global Matches:** file_cluster_4: 6.702, file_cluster_6: 10.735, file_cluster_16: 11.54
- **Magnitude:** 1016.76 | **LOC:** 1316 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.452; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (97.5%), Guard Balance (formerly Safety Score) (59.0%), Complexity Load (formerly Cognitive Load) (57.8%)
- **Documentation Coverage:** 92.1053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MergeBaseItemData` **(Many-Argument Workhorses)** (Impact: 143.9)
  * `RefreshWithProviders` **(Many-Argument Workhorses)** (Impact: 75.5)
  * `RefreshMetadata` **(Stateful Encapsulated Methods)** (Impact: 66.3)
  * `GetProviders` **(Many-Argument Workhorses)** (Impact: 23.0)
    * *Intent:* /// <summary> /// Gets the providers. /// </summary> /// <param name="item">A media item.</param> //...
  * `UpdatePremiereDate` **(Defensive Guards)** (Impact: 22.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 98 instances
* *Concurrency (weighted view):* 79
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 190`, `args: 60`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 129`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 6`, `concurrency: 34`, `import: 19`
* *Defense:* `safety: 64`, `doc: 25`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.452
  * `Choke Point (Betweenness):` 0.000147 | `Ripple Effect (Closeness):` 0.010912
  * `Imports (Out-Degree: 8):` Jellyfin.Extensions, MediaBrowser.Controller.Configuration, MediaBrowser.Controller.Entities, MediaBrowser.Controller.Entities.Audio, MediaBrowser.Controller.IO, MediaBrowser.Controller.Library, MediaBrowser.Controller.Persistence, MediaBrowser.Controller.Providers...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `MediaBrowser.Controller/Entities/Folder.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.235)
- **Top Global Matches:** file_cluster_4: 7.235, file_cluster_0: 9.631, file_cluster_16: 9.697
- **Magnitude:** 979.9 | **LOC:** 1882 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **32**; blast radius 0.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Concurrency Surface (formerly Concurrency) (85.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.5%)
- **Documentation Coverage:** 68.9655% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ValidateChildrenInternal2` **(Many-Argument Workhorses)** (Impact: 100.5)
  * `AllowBoxSetCollapsing` **(Compute Cores)** (Impact: 58.3)
  * `RequiresPostFiltering` **(Compute Cores)** (Impact: 32.0)
  * `AddChildrenFromCollection` **(Many-Argument Workhorses)** (Impact: 24.5)
  * `GetLinkedChildren` **(Defensive Guards)** (Impact: 24.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 67 instances
* *Concurrency (weighted view):* 67
* *State Mutation (weighted view):* 229
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 325`, `args: 104`, `func_start: 57`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 95`, `dead_code: 1`, `unreferenced_by_name: 11`
* *Architecture:* `io: 1`, `api: 54`, `concurrency: 37`, `import: 32`
* *Defense:* `safety: 79`, `doc: 132`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.464
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.008163
  * `Imports (Out-Degree: 14):` J2N.Collections.Generic.Extensions, Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Controller.Channels, MediaBrowser.Controller.Collections...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Jellyfin.LiveTv/LiveTvManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.605)
- **Top Global Matches:** file_cluster_0: 8.605, file_cluster_16: 9.347, file_cluster_10: 9.783
- **Magnitude:** 924.5 | **LOC:** 1293 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **26**; blast radius 0.539; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.6%)
- **Documentation Coverage:** 91.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetEmbyRecordingsAsync` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `GetTimers` **(Callbacks & Closures)** (Impact: 26.6)
  * `AddRecordingInfo` **(Stateful Encapsulated Methods)** (Impact: 23.3)
  * `AddChannelInfo` **(Many-Argument Workhorses)** (Impact: 20.9)
  * `AddInfoToRecordingDto` **(Many-Argument Workhorses)** (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 99 instances
* *Concurrency (weighted view):* 144
* *State Mutation (weighted view):* 357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 311`, `args: 110`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 159`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 33`, `concurrency: 94`, `import: 26`
* *Defense:* `safety: 47`, `doc: 14`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.539
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001013
  * `Imports (Out-Degree: 5):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.LiveTv.Configuration, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Channels...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Jellyfin.LiveTv/Channels/ChannelManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.756)
- **Top Global Matches:** file_cluster_0: 8.756, file_cluster_16: 8.906, file_cluster_4: 9.763
- **Magnitude:** 825.06 | **LOC:** 1216 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **34**; blast radius 1.492; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (55.9%), Complexity Load (formerly Cognitive Load) (48.3%)
- **Documentation Coverage:** 30.5085% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetChannelItemEntityAsync` **(Many-Argument Workhorses)** (Impact: 118.6)
  * `GetChannelItems` **(Many-Argument Workhorses)** (Impact: 33.4)
  * `GetChannelsInternalAsync` **(Defensive Guards)** (Impact: 26.6)
    * *Intent:* /// <inheritdoc />
  * `GetChannelItemsInternal` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* /// <inheritdoc />
  * `GetChannelDataCachePath` **(Many-Argument Workhorses)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 85 instances
* *Concurrency (weighted view):* 132
* *State Mutation (weighted view):* 292
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 242`, `args: 83`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 122`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 9`, `api: 23`, `concurrency: 82`, `import: 34`
* *Defense:* `safety: 82`, `doc: 62`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.492
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.008266
  * `Imports (Out-Degree: 6):` AsyncKeyedLock, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, Jellyfin.Extensions.Json, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Channels...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.926)
- **Top Global Matches:** file_cluster_4: 6.926, file_cluster_16: 8.977, file_cluster_15: 9.307
- **Magnitude:** 757.44 | **LOC:** 1400 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **32**; blast radius 0.439; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.5%), Concurrency Surface (formerly Concurrency) (54.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ExtractImageInternal` **(Many-Argument Workhorses)** (Impact: 80.9)
  * `ExtractVideoImagesOnIntervalAccelerated` **(Many-Argument Workhorses)** (Impact: 71.8)
    * *Intent:* /// <inheritdoc />
  * `ExtractVideoImagesOnIntervalInternal` **(Many-Argument Workhorses)** (Impact: 47.5)
  * `GetMediaInfoInternal` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /// <summary> /// Gets the media info internal. /// </summary> /// <returns>Task{MediaInfoResult}.</...
  * `SetFFmpegPath` **(I/O & Config Routines)** (Impact: 23.3)
    * *Intent:* /// <summary> /// Run at startup to validate ffmpeg. /// Sets global variables FFmpegPath. /// Prece...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 59 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 210`, `args: 92`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 108`, `planned_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `io: 11`, `api: 55`, `concurrency: 26`, `import: 32`
* *Defense:* `safety: 49`, `doc: 58`, `sync_locks: 4`, `immutability_locks: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.439
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.00045
  * `Imports (Out-Degree: 5):` AsyncKeyedLock, Jellyfin.Data.Enums, Jellyfin.Extensions, Jellyfin.Extensions.Json, Jellyfin.Extensions.Json.Converters, MediaBrowser.Common, MediaBrowser.Common.Configuration, MediaBrowser.Common.Extensions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Jellyfin.Api/Controllers/ImageController.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 8.766)
- **Top Global Matches:** file_cluster_13: 8.766, file_cluster_0: 8.81, file_cluster_16: 9.319
- **Magnitude:** 718.64 | **LOC:** 2070 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **35**; blast radius 0.633; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.1%), Mutation Surface (formerly State Flux) (71.7%), Guard Balance (formerly Safety Score) (46.4%), Debt Markers (formerly Tech Debt) (35.7%)
- **Documentation Coverage:** 24.3902% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetImageInternal` **(Many-Argument Workhorses)** (Impact: 89.9)
  * `GetImageResult` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `GetItemImageInfos` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* /// <summary> /// Get item image infos. /// </summary> /// <param name="itemId">Item id.</param> ///...
  * `GetSplashscreen` **(Many-Argument Workhorses)** (Impact: 13.5)
    * *Intent:* /// <summary> /// Generates or gets the splashscreen. /// </summary> /// <param name="tag">Supply th...
  * `GetUserImage` **(Defensive Guards)** (Impact: 12.6)
    * *Intent:* /// <summary> /// Get user profile image. /// </summary> /// <param name="userId">User id.</param> /...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 121
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 227`, `args: 46`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `state_mutation: 52`, `dead_code: 1`, `unreferenced_by_name: 27`
* *Architecture:* `io: 9`, `api: 32`, `concurrency: 91`, `import: 35`
* *Defense:* `safety: 61`, `doc: 515`, `immutability_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.00045
  * `Imports (Out-Degree: 10):` Jellyfin.Api.Attributes, Jellyfin.Api.Extensions, Jellyfin.Api.Helpers, Jellyfin.Extensions, MediaBrowser.Common.Api, MediaBrowser.Common.Configuration, MediaBrowser.Controller.Configuration, MediaBrowser.Controller.Drawing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Jellyfin.LiveTv/DefaultLiveTvService.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.061)
- **Top Global Matches:** file_cluster_16: 8.061, file_cluster_0: 8.306, file_cluster_15: 8.607
- **Magnitude:** 708.98 | **LOC:** 1000 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **22**; blast radius 0.506; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.6102% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UpdateTimersForSeriesTimer` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `CopyProgramInfoToTimerInfo` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `CreateTimer` **(Defensive Guards)** (Impact: 19.7)
  * `CreateTimer` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `CancelTimerInternal` **(Stateful Encapsulated Methods)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 96
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 149`, `args: 55`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 152`, `unreferenced_by_name: 15`
* *Architecture:* `api: 27`, `concurrency: 51`, `import: 22`
* *Defense:* `safety: 45`, `doc: 2`, `immutability_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.506
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001013
  * `Imports (Out-Degree: 4):` Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, Jellyfin.LiveTv.Configuration, Jellyfin.LiveTv.Timers, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Configuration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `MediaBrowser.XbmcMetadata/Parsers/BaseNfoParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.337)
- **Top Global Matches:** file_cluster_6: 7.337, file_cluster_4: 9.765, file_cluster_9: 15.782
- **Magnitude:** 708.26 | **LOC:** 1020 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.342; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.4%), Complexity Load (formerly Cognitive Load) (23.2%)
- **Documentation Coverage:** 52.9412% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FetchDataFromXmlNode` **(Many-Argument Workhorses)** (Impact: 272.5)
    * *Intent:* /// <summary> /// Fetches metadata from an XML node. /// </summary> /// <param name="reader">The <se...
  * `FetchFromVideoNode` **(Many-Argument Workhorses)** (Impact: 51.7)
  * `Fetch` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* /// <summary> /// Fetches the specified item. /// </summary> /// <param name="item">The <see cref="M...
  * `FetchFromRatingNode` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `FetchThumbNode` **(Stateful Encapsulated Methods)** (Impact: 25.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 144`, `args: 26`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 64`
* *Architecture:* `io: 2`, `api: 4`, `import: 22`
* *Defense:* `safety: 22`, `doc: 52`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Common.Configuration, MediaBrowser.Common.Providers, MediaBrowser.Controller.Entities, MediaBrowser.Controller.Entities.Movies, MediaBrowser.Controller.Entities.TV, MediaBrowser.Controller.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Emby.Server.Implementations/Library/MediaSourceManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.357)
- **Top Global Matches:** file_cluster_16: 8.357, file_cluster_0: 8.384, file_cluster_4: 8.619
- **Magnitude:** 637.56 | **LOC:** 925 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **33**; blast radius 0.716; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (64.1%), Guard Balance (formerly Safety Score) (56.7%)
- **Documentation Coverage:** 81.0345% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AddMediaInfoWithProbe` **(Many-Argument Workhorses)** (Impact: 81.6)
  * `GetPlaybackMediaSources` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `AddMediaInfo` **(Stateful Encapsulated Methods)** (Impact: 23.7)
  * `SetDefaultAudioAndSubtitleStreamIndices` **(Defensive Guards)** (Impact: 19.2)
  * `GetStaticMediaSources` **(Defensive Guards)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 88
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 191`, `args: 59`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 88`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 4`, `api: 24`, `concurrency: 48`, `import: 33`
* *Defense:* `safety: 39`, `doc: 9`, `immutability_locks: 17`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.716
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.008945
  * `Imports (Out-Degree: 8):` AsyncKeyedLock, Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, Jellyfin.Extensions.Json, MediaBrowser.Common.Configuration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Jellyfin.Server.Implementations/Users/UserManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 9.104)
- **Top Global Matches:** file_cluster_16: 9.104, file_cluster_0: 9.252, file_cluster_4: 9.255
- **Magnitude:** 606.18 | **LOC:** 895 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 0.706; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (56.4%), Guard Balance (formerly Safety Score) (55.1%)
- **Documentation Coverage:** 25.4902% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AuthenticateUser` **(Many-Argument Workhorses)** (Impact: 52.6)
    * *Intent:* /// <inheritdoc/>
  * `GetUserDto` **(Defensive Guards)** (Impact: 23.2)
    * *Intent:* /// <inheritdoc/>
  * `UpdatePolicyAsync` **(Callbacks & Closures)** (Impact: 12.5)
    * *Intent:* /// <inheritdoc/>
  * `GetAuthenticationProviders` **(Stateful Encapsulated Methods)** (Impact: 9.8)
  * `AuthenticateLocalUser` **(Stateful Encapsulated Methods)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 179
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 192`, `args: 87`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 113`, `planned_debt: 3`, `unreferenced_by_name: 12`
* *Architecture:* `api: 25`, `concurrency: 84`, `import: 29`
* *Defense:* `safety: 49`, `doc: 36`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.706
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0009
  * `Imports (Out-Degree: 2):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Data.Events.Users, Jellyfin.Database.Implementations, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `MediaBrowser.LocalMetadata/Parsers/BaseItemXmlParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.941)
- **Top Global Matches:** file_cluster_4: 7.941, file_cluster_9: 9.869, file_cluster_6: 11.733
- **Magnitude:** 587.38 | **LOC:** 873 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.342; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.5%), Complexity Load (formerly Cognitive Load) (21.3%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FetchDataFromXmlNode` **(Many-Argument Workhorses)** (Impact: 253.2)
    * *Intent:* /// <summary> /// Fetches metadata from one Xml Element. /// </summary> /// <param name="reader">The...
  * `FetchFromSharesNode` **(Stateful Encapsulated Methods)** (Impact: 25.0)
  * `FetchDataFromPersonsNode` **(Stateful Encapsulated Methods)** (Impact: 22.4)
    * *Intent:* /// <summary> /// Fetches the data from persons node. /// </summary> /// <param name="reader">The re...
  * `FetchFromTagsNode` **(Stateful Encapsulated Methods)** (Impact: 19.1)
  * `FetchFromTaglinesNode` **(Stateful Encapsulated Methods)** (Impact: 18.9)
    * *Intent:* /// <summary> /// Fetches from taglines node. /// </summary> /// <param name="reader">The reader.</p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 93`, `args: 16`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 43`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 3`, `import: 16`
* *Defense:* `safety: 10`, `doc: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Controller.Entities, MediaBrowser.Controller.Extensions, MediaBrowser.Controller.Playlists, MediaBrowser.Controller.Providers, MediaBrowser.Model.Entities, Microsoft.Extensions.Logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Helpers/StreamingHelpers.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 5.892)
- **Top Global Matches:** file_cluster_3: 5.892, file_cluster_8: 20.209, file_cluster_6: 33.168
- **Magnitude:** 585.18 | **LOC:** 608 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **23**; blast radius 0.504; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.6%), Complexity Load (formerly Cognitive Load) (44.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetStreamingState` **(Many-Argument Workhorses)** (Impact: 166.5)
    * *Intent:* /// Gets the current streaming state. /// </summary> /// <param name="streamingRequest">The <see cre...
  * `ParseParams` **(Compute Cores)** (Impact: 164.0)
    * *Intent:* /// <summary> /// Parses the parameters. /// </summary> /// <param name="request">The request.</para...
  * `GetOutputFileExtension` **(Stateful Encapsulated Methods)** (Impact: 31.5)
    * *Intent:* /// <summary> /// Gets the output file extension. /// </summary> /// <param name="state">The state.<...
  * `ParseStreamOptions` **(Stateful Encapsulated Methods)** (Impact: 5.0)
    * *Intent:* /// <summary> /// Parses query parameters as StreamOptions. /// </summary> /// <param name="queryStr...
  * `GetContainerFileExtension` **(Stateful Encapsulated Methods)** (Impact: 4.9)
    * *Intent:* /// <summary> /// Parses the container into its file extension. /// </summary> /// <param name="cont...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 62 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 74`, `args: 9`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 2`, `concurrency: 4`, `import: 23`
* *Defense:* `safety: 38`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.001875
  * `Imports (Out-Degree: 6):` Jellyfin.Api.Extensions, Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Common.Configuration, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Configuration, MediaBrowser.Controller.Entities, MediaBrowser.Controller.Library...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Jellyfin.Api/Controllers/ItemsController.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.555)
- **Top Global Matches:** file_cluster_4: 9.555, file_cluster_6: 9.778, file_cluster_13: 15.175
- **Magnitude:** 582.26 | **LOC:** 1041 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.633; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.1%), Guard Balance (formerly Safety Score) (49.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.7%), Complexity Load (formerly Cognitive Load) (14.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetItems` **(Many-Argument Workhorses)** (Impact: 390.2)
    * *Intent:* /// <param name="minWidth">Optional. Filter by the minimum width of the item.</param> /// <param nam...
  * `GetResumeItems` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* /// <param name="searchTerm">The search term.</param> /// <param name="parentId">Specify this to loc...
  * `UpdateItemUserData` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* /// <summary> /// Update Item User Data. /// </summary> /// <param name="userId">The user id.</param...
  * `GetItemUserData` **(Defensive Guards)** (Impact: 8.3)
    * *Intent:* /// <summary> /// Get Item User Data. /// </summary> /// <param name="userId">The user id.</param> /...
  * `GetResumeItemsLegacy` **(Many-Argument Workhorses)** (Impact: 5.8)
    * *Intent:* /// <param name="searchTerm">The search term.</param> /// <param name="parentId">Specify this to loc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 83`, `args: 22`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 42`, `unreferenced_by_name: 3`
* *Architecture:* `api: 10`, `import: 23`
* *Defense:* `safety: 36`, `doc: 266`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00045
  * `Imports (Out-Degree: 5):` Jellyfin.Api.Extensions, Jellyfin.Api.Helpers, Jellyfin.Api.ModelBinders, Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Common.Extensions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `MediaBrowser.Controller/Entities/UserViewBuilder.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.24)
- **Top Global Matches:** file_cluster_4: 7.24, file_cluster_16: 9.351, file_cluster_0: 9.93
- **Magnitude:** 577.5 | **LOC:** 1028 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **17**; blast radius 0.681; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.7%), Complexity Load (formerly Cognitive Load) (41.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Filter` **(Many-Argument Workhorses)** (Impact: 263.7)
  * `GetUserItems` **(Many-Argument Workhorses)** (Impact: 53.2)
  * `SortAndPage` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `GetMediaFolders` **(Stateful Encapsulated Methods)** (Impact: 11.4)
  * `GetTvView` **(Stateful Encapsulated Methods)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 209`, `args: 54`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 79`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 8`, `import: 17`
* *Defense:* `safety: 37`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.681
  * `Choke Point (Betweenness):` 0.00027 | `Ripple Effect (Closeness):` 0.010344
  * `Imports (Out-Degree: 9):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Controller.Entities.TV.Episode, MediaBrowser.Controller.Entities.TV.Series, MediaBrowser.Controller.Library...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `MediaBrowser.Providers/Manager/ProviderManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.808)
- **Top Global Matches:** file_cluster_0: 7.808, file_cluster_10: 9.335, file_cluster_16: 9.617
- **Magnitude:** 571.56 | **LOC:** 1173 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **41**; blast radius 1.159; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.9%), Mutation Surface (formerly State Flux) (93.2%), Debt Markers (formerly Tech Debt) (66.9%), Guard Balance (formerly Safety Score) (48.1%)
- **Documentation Coverage:** 21.6216% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IsSaverEnabledForItem` **(Many-Argument Workhorses)** (Impact: 32.2)
    * *Intent:* /// <summary> /// Determines whether [is saver enabled for item] [the specified saver]. /// </summar...
  * `GetRemoteSearchResults` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `SaveImage` **(Many-Argument Workhorses)** (Impact: 23.0)
    * *Intent:* /// <inheritdoc/>
  * `CanRefreshMetadata` **(Stateful Encapsulated Methods)** (Impact: 21.1)
  * `SaveMetadataAsync` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* /// <summary> /// Saves the metadata. /// </summary> /// <param name="item">The item.</param> /// <p...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 82
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 243`, `args: 105`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 75`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `io: 4`, `api: 31`, `concurrency: 52`, `import: 41`
* *Defense:* `safety: 74`, `doc: 70`, `sync_locks: 4`, `immutability_locks: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.159
  * `Choke Point (Betweenness):` 0.000211 | `Ripple Effect (Closeness):` 0.015267
  * `Imports (Out-Degree: 8):` AsyncKeyedLock, Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Extensions, MediaBrowser.Common.Net, MediaBrowser.Controller, MediaBrowser.Controller.BaseItemManager, MediaBrowser.Controller.Configuration...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Jellyfin.Database/Jellyfin.Database.Providers.Sqlite/Migrations/20240729140605_AddMediaSegments.cs` (CSHARP) | Magnitude: 11.64 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 26, core_var_decl: 9, structural_boundaries: 7, state_mutation: 6
- `tests/Jellyfin.Server.Implementations.Tests/QuickConnect/QuickConnectManagerTests.cs` (CSHARP) | Magnitude: 82.52 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 31, test: 22, args: 21
- `Emby.Server.Implementations/SyncPlay/Group.cs` (CSHARP) | Magnitude: 272.12 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 387, doc: 151, structural_boundaries: 100, core_var_decl: 55
- `MediaBrowser.Controller/Entities/Audio/Audio.cs` (CSHARP) | Magnitude: 61.44 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 31, doc: 19, api: 18
- `Emby.Server.Implementations/Library/ExternalDataManager.cs` (CSHARP) | Magnitude: 25.98 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 20, doc: 13, import: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `MediaBrowser.Controller/Entities/Audio/MusicAlbum.cs` (CSHARP) | Magnitude: 117.86 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 61, core_var_decl: 31, args: 25
- `src/Jellyfin.Database/Jellyfin.Database.Implementations/ModelConfiguration/DisplayPreferencesConfiguration.cs` (CSHARP) | Magnitude: 4.38 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, doc: 4, args: 3
- `MediaBrowser.Model/Dlna/CodecProfile.cs` (CSHARP) | Magnitude: 25.56 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 45, indent_spaces: 29, structural_boundaries: 13, api: 11
- `src/Jellyfin.Database/Jellyfin.Database.Providers.Sqlite/Migrations/20200613202153_AddUsers.Designer.cs` (CSHARP) | Magnitude: 12.02 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 219, structural_boundaries: 18, args: 11, closures: 10
- `tests/Jellyfin.Server.Integration.Tests/Controllers/EncoderController.cs` (CSHARP) | Magnitude: 21.52 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, doc: 15, structural_boundaries: 10, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `MediaBrowser.MediaEncoding/BdInfo/BdInfoFileInfo.cs` (CSHARP) | Magnitude: 14.76 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: doc: 30, indent_spaces: 22, structural_boundaries: 11, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `Emby.Server.Implementations/Images/FolderImageProvider.cs` (CSHARP) | Magnitude: 10.1 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, import: 7, safety: 3
- `MediaBrowser.Providers/MediaInfo/AudioImageProvider.cs` (CSHARP) | Magnitude: 79.34 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 39, core_var_decl: 21, import: 17
- `MediaBrowser.Controller/MediaEncoding/BaseEncodingJobOptions.cs` (CSHARP) | Magnitude: 69.36 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 80, indent_spaces: 75, api: 51, structural_boundaries: 10
- `MediaBrowser.Model/LiveTv/TunerHostInfo.cs` (CSHARP) | Magnitude: 26.06 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, api: 18, state_mutation: 6, core_var_decl: 6
- `MediaBrowser.Model/LiveTv/RecordingQuery.cs` (CSHARP) | Magnitude: 23.88 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 39, indent_spaces: 26, api: 21, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `MediaBrowser.Model/Users/UserPolicy.cs` (CSHARP) | Magnitude: 83.54 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 90, api: 46, doc: 35, core_var_decl: 35
- `tests/Jellyfin.Server.Implementations.Tests/Data/SearchPunctuationTests.cs` (CSHARP) | Magnitude: 32.94 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 30, core_var_decl: 20, args: 12
- `Jellyfin.Api/Controllers/ImageController.cs` (CSHARP) | Magnitude: 718.64 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1372, doc: 515, decorators: 440, structural_boundaries: 227
- `MediaBrowser.Model/SyncPlay/SyncPlayGroupDoesNotExistUpdate.cs` (CSHARP) | Magnitude: 5.12 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 5, indent_spaces: 5, api: 3
- `MediaBrowser.Model/SyncPlay/SyncPlayGroupLeftUpdate.cs` (CSHARP) | Magnitude: 5.12 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 5, indent_spaces: 5, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `MediaBrowser.Model/Net/IPData.cs` (CSHARP) | Magnitude: 26.94 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 32, indent_spaces: 31, api: 9, structural_boundaries: 6
- `src/Jellyfin.Extensions/DictionaryExtensions.cs` (CSHARP) | Magnitude: 24.94 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, doc: 13, structural_boundaries: 9, branch: 4
- `Jellyfin.Api/Helpers/HlsCodecStringHelpers.cs` (CSHARP) | Magnitude: 125.76 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 191, doc: 93, structural_boundaries: 48, branch: 31
- `Jellyfin.Server/Migrations/Routines/DisableLegacyAuthorization.cs` (CSHARP) | Magnitude: 15.78 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, doc: 8, structural_boundaries: 6, api: 3
- `Emby.Server.Implementations/Sorting/CriticRatingComparer.cs` (CSHARP) | Magnitude: 9.68 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 13, indent_spaces: 12, structural_boundaries: 9, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Jellyfin.Api/Models/SystemInfoDtos/SystemStorageDto.cs` (CSHARP) | Magnitude: 20.7 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 27, indent_spaces: 22, structural_boundaries: 15, api: 10
- `Emby.Server.Implementations/Library/MediaSourceManager.cs` (CSHARP) | Magnitude: 637.56 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 705, structural_boundaries: 191, branch: 117, core_var_decl: 106
- `Jellyfin.Api/Auth/DefaultAuthorizationPolicy/DefaultAuthorizationHandler.cs` (CSHARP) | Magnitude: 34.2 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 23, import: 11, doc: 10
- `Jellyfin.Api/Controllers/HlsSegmentController.cs` (CSHARP) | Magnitude: 65.66 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 42, doc: 40, core_var_decl: 28
- `src/Jellyfin.LiveTv/TunerHosts/HdHomerun/HdHomerunUdpStream.cs` (CSHARP) | Magnitude: 91.04 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 52, core_var_decl: 27, import: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `MediaBrowser.Common/Net/NetworkConfigurationStore.cs` (CSHARP) | Magnitude: 6.42 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 9, indent_spaces: 6, structural_boundaries: 3, api: 3
- `MediaBrowser.Model/Dto/TrickplayInfoDto.cs` (CSHARP) | Magnitude: 18.48 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 28, indent_spaces: 18, structural_boundaries: 11, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `Jellyfin.Server.Implementations/DbConfiguration/DatabaseConfigurationStore.cs` (CSHARP) | Magnitude: 6.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 6, indent_spaces: 6, import: 4
- `src/Jellyfin.Drawing.Skia/PercentPlayedDrawer.cs` (CSHARP) | Magnitude: 8.2 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, doc: 9, core_var_decl: 5
- `src/Jellyfin.Database/Jellyfin.Database.Providers.Sqlite/Migrations/20241112152323_FixAncestorIdConfig.cs` (CSHARP) | Magnitude: 6.28 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 4, doc: 3, args: 2
- `.github/workflows/pull-request-conflict.yml` (YAML) | Magnitude: 16.42 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 17, branch: 4, args: 3, structural_boundaries: 2
- `src/Jellyfin.Database/Jellyfin.Database.Providers.Sqlite/Migrations/20250913211637_AddProperParentChildRelationBaseItemWithCascade.cs` (CSHARP) | Magnitude: 6.02 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 36, args: 6, func_start: 6, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/Jellyfin.Server.Integration.Tests/TestPlugin.cs` (CSHARP) | Magnitude: 20.4 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 15, core_var_decl: 8, design_pascal_case: 8
- `MediaBrowser.Controller/Channels/Channel.cs` (CSHARP) | Magnitude: 31.04 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 25, import: 10, args: 8
- `MediaBrowser.Controller/Providers/IHasLookupInfo.cs` (CSHARP) | Magnitude: 19.82 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 2, args: 1, func_start: 1
- `MediaBrowser.Controller/Providers/ILocalImageProvider.cs` (CSHARP) | Magnitude: 20.34 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, doc: 3, import: 2
- `tests/Jellyfin.Server.Implementations.Tests/TypedBaseItem/BaseItemKindTests.cs` (CSHARP) | Magnitude: 20.32 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 20, core_var_decl: 7, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `MediaBrowser.Controller/Session/ISessionController.cs` (CSHARP) | Magnitude: 23.42 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: doc: 17, structural_boundaries: 6, indent_spaces: 6, import: 4
- `MediaBrowser.Controller/Drawing/IImageProcessor.cs` (CSHARP) | Magnitude: 55.02 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 71, indent_spaces: 18, args: 13, func_start: 13
- `Emby.Server.Implementations/Sorting/IsFolderComparer.cs` (CSHARP) | Magnitude: 11.2 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 15, indent_spaces: 12, structural_boundaries: 9, import: 4
- `MediaBrowser.Model/Globalization/CultureDto.cs` (CSHARP) | Magnitude: 14.22 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 26, doc: 19, api: 7, structural_boundaries: 6
- `src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/People.cs` (CSHARP) | Magnitude: 20.22 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: doc: 15, structural_boundaries: 6, api: 5, indent_spaces: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `MediaBrowser.Model/Dlna/ResolutionNormalizer.cs` (CSHARP) | Magnitude: 47.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 14, core_var_decl: 14, branch: 8
- `Jellyfin.Server/Migrations/Routines/MigrateLibraryUserData.cs` (CSHARP) | Magnitude: 62.38 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 46, core_var_decl: 21, import: 15
- `Jellyfin.Api/Auth/UserPermissionPolicy/UserPermissionHandler.cs` (CSHARP) | Magnitude: 19.14 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 12, doc: 8, import: 7
- `Jellyfin.Server/Migrations/PreStartupRoutines/MigrateEncodingOptions.cs` (CSHARP) | Magnitude: 90.18 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 158, core_var_decl: 67, api: 48, design_pascal_case: 44
- `Jellyfin.Api/Auth/FirstTimeSetupPolicy/FirstTimeSetupHandler.cs` (CSHARP) | Magnitude: 22.62 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 8, doc: 8, branch: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/ci-compat.yml` -> Churn: **88.09%** | Cog Load: 3.9185% | Debt: 76.4313%
- `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` -> Churn: **75.47%** | Cog Load: 60.5586% | Debt: 37.701%
- `MediaBrowser.Controller/Entities/BaseItem.cs` -> Churn: **59.81%** | Cog Load: 24.4649% | Debt: 75.3596%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Emby.Server.Implementations/Dto/DtoService.cs` -> **theguymadmax** (100.0% isolated ownership) | Magnitude: 1300.32
- `src/Jellyfin.LiveTv/LiveTvManager.cs` -> **evan314159** (100.0% isolated ownership) | Magnitude: 924.5
- `src/Jellyfin.LiveTv/Channels/ChannelManager.cs` -> **evan314159** (100.0% isolated ownership) | Magnitude: 825.06
- `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` -> **gnattu** (100.0% isolated ownership) | Magnitude: 757.44
- `Emby.Server.Implementations/Library/MediaSourceManager.cs` -> **theguymadmax** (100.0% isolated ownership) | Magnitude: 637.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Emby.Server.Implementations/Library/LibraryManager.cs` -> **Severity: 0.107** (Bridge: 0.0011 * Flux: 98.7366%)
- `MediaBrowser.Controller/Entities/Video.cs` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 99.6653%)
- `MediaBrowser.Controller/Entities/BaseItem.cs` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 99.9005%)
- `MediaBrowser.Controller/Entities/UserViewBuilder.cs` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 95.777%)
- `MediaBrowser.Controller/Entities/UserView.cs` -> **Severity: 0.024** (Bridge: 0.0003 * Flux: 87.1753%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/Libraries/Library.cs` -> **Severity: 6.475** (Embedded: 0.1354 * Error Risk: 47.8228%)
- `MediaBrowser.Controller/Entities/Extensions.cs` -> **Severity: 6.078** (Embedded: 0.1149 * Error Risk: 52.8896%)
- `MediaBrowser.Controller/Entities/Audio/Audio.cs` -> **Severity: 2.872** (Embedded: 0.0521 * Error Risk: 55.1457%)
- `MediaBrowser.Model/MediaInfo/MediaInfo.cs` -> **Severity: 1.664** (Embedded: 0.0313 * Error Risk: 53.1387%)
- `Emby.Server.Implementations/Library/LibraryManager.cs` -> **Severity: 0.998** (Embedded: 0.0206 * Error Risk: 48.3846%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `MediaBrowser.Controller/Entities/Audio/Audio.cs` -> **Severity: 1490.892** (Blast Radius: 18.975 * Doc Risk: 78.5714%)
- `MediaBrowser.Model/MediaInfo/MediaInfo.cs` -> **Severity: 1075.1** (Blast Radius: 10.751 * Doc Risk: 100.0%)
- `tests/Jellyfin.Server.Integration.Tests/AuthHelper.cs` -> **Severity: 470.7** (Blast Radius: 4.707 * Doc Risk: 100.0%)
- `Emby.Server.Implementations/Library/LibraryManager.cs` -> **Severity: 401.47** (Blast Radius: 5.895 * Doc Risk: 68.1034%)
- `MediaBrowser.Model/Net/MimeTypes.cs` -> **Severity: 217.35** (Blast Radius: 2.898 * Doc Risk: 75.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 444 literal sites + 11 sites through wrappers = 455

- `ThrowConflictingFilters` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `MediaBrowser.Controller/Entities/InternalItemsQuery.cs`
- `ThrowAuthenticationException` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `Jellyfin.Server.Implementations/Users/DefaultAuthenticationProvider.cs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 27160 call pairs -- scoped 17.1%, unique 0.6%, ambiguous 30.7%, external 51.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| csharp | 27146 | 17.2% | 0.6% | 30.7% | 51.5% |
| shell | 10 | 0.0% | 0.0% | 0.0% | 100.0% |
| html | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
