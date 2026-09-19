# ARCHITECTURAL_BRIEF: jellyfin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jellyfin/jellyfin.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 2015 analyzed artifact(s), 167366 LOC.
- **Load-bearing artifact:** `src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/Libraries/Library.cs` -- 252 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Emby.Server.Implementations/ApplicationHost.cs` -- pulls in 102 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` at magnitude 5151.72 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 2015 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 319 |
| Total LOC | 167366 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.3% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4567 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1517 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0642 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 1839 | 151790 | 91.3% |
| JSON | 153 | 14969 | 7.6% |
| HTML | 7 | 591 | 0.3% |
| PLAINTEXT | 6 | 0 | 0.3% |
| MARKDOWN | 6 | 0 | 0.3% |
| XML | 2 | 0 | 0.1% |
| SHELL | 2 | 16 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.393`
> **Composition Archetype:** `Mid Flat Project` (z +2.39; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 28%, State Mutators Files 20%, Data / Markup / Trivial 13%, Large Core Modules (2) 8%, Generic / Templated Code Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2003 | 99.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 0.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 319*

**Composition by Extension & Reason:**
- `.cs`: 97x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 1596 LOC), 2x Excluded (Machine-Generated Source Code Signature: 1611 LOC)
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.5 | 6.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.6 | 34.3 | 45.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.9 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 17.0 | 5.5 | 5.6 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 76.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 20.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 315 | 145 | 0 | `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` |
| cleanup | 184 | 74 | 0 | `Emby.Server.Implementations/ScheduledTasks/ScheduledTaskWorker.cs` |
| guards | 12731 | 989 | 15 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| danger | 1378 | 672 | 1 | `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` |
| concurrency | 4778 | 430 | 6 | `Emby.Server.Implementations/Session/SessionManager.cs` |
| connectivity | 11650 | 1814 | 12 | `MediaBrowser.Controller/Entities/BaseItem.cs` |
| io | 1039 | 219 | 1 | `Emby.Server.Implementations/IO/ManagedFileSystem.cs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` |
| time | 420 | 151 | 0 | `src/Jellyfin.Database/Jellyfin.Database.Implementations/Locking/OptimisticLockBehavior.cs` |
| serialization | 110 | 39 | 0 | `tests/Jellyfin.Extensions.Tests/Json/Converters/JsonCommaDelimitedCollectionTests.cs` |
| regex | 13 | 9 | 0 | `Emby.Naming/Book/BookFileNameParser.cs` |
| events | 1727 | 238 | 1 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| tests | 2433 | 150 | 0 | `tests/Jellyfin.MediaEncoding.Tests/Probing/ProbeResultNormalizerTests.cs` |
| docs | 36568 | 1484 | 43 | `Jellyfin.Api/Controllers/ImageController.cs` |
| debt | 213 | 116 | 0 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| mutation | 35328 | 1284 | 40 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| dead_code | 2908 | 967 | 4 | `MediaBrowser.Controller/Entities/BaseItem.cs` |
| credential | 35 | 11 | 0 | `Emby.Naming/Common/NamingOptions.cs` |
| threat | 69 | 52 | 0 | `MediaBrowser.MediaEncoding/Encoder/ApplePlatformHelper.cs` |
| ml_ai | 193 | 62 | 0 | `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` |
| ui | 86 | 9 | 0 | `MediaBrowser.Providers/Plugins/Tmdb/Configuration/config.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Emby.Server.Implementations/IO/ManagedFileSystem.cs` (Hits: 32)
- `src/Jellyfin.LiveTv/Recordings/RecordingsManager.cs` (Hits: 32)
- `MediaBrowser.Providers/Manager/ImageSaver.cs` (Hits: 31)

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

- `ApplyTranscodingConditions` **(Many-Argument Workhorses)** (@ `MediaBrowser.Model/Dlna/StreamBuilder.cs`) -> Impact: **532.2** | LOC: 503
- `TranslateQuery` **(Many-Argument Workhorses)** (@ `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs`) -> Impact: **425.3** | LOC: 946
- `GetItems` **(Many-Argument Workhorses)** (@ `Jellyfin.Api/Controllers/ItemsController.cs`) -> Impact: **408.9** | LOC: 343
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
- `BuildStreamVideoItem` **(Many-Argument Workhorses)** (@ `MediaBrowser.Model/Dlna/StreamBuilder.cs`) -> Impact: **244.6** | LOC: 211
- `GetMediaStream` **(Many-Argument Workhorses)** (@ `MediaBrowser.MediaEncoding/Probing/ProbeResultNormalizer.cs`) -> Impact: **200.7** | LOC: 347
  * *Intent:* /// <summary> /// Converts ffprobe stream info to our MediaStream class. /// </summary> /// <param name="isAudio">if set to <c>true</c> [is info].</pa...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Jellyfin.Api/Controllers` | 59 | 9878.54 | 16.95% | 55.55% |
| `MediaBrowser.Controller/MediaEncoding` | 16 | 6062.37 | 10.88% | 20.18% |
| `MediaBrowser.Controller/Entities` | 46 | 4808.6 | 10.84% | 44.31% |
| `MediaBrowser.Model/Dlna` | 24 | 3077.64 | 4.46% | 13.51% |
| `Jellyfin.Server.Implementations/Item` | 6 | 2567.04 | 29.01% | 56.8% |
| `MediaBrowser.Providers/Manager` | 5 | 2525.8 | 27.35% | 17.87% |
| `Jellyfin.Server/Migrations/Routines` | 28 | 2438.5 | 19.17% | 35.1% |
| `src/Jellyfin.LiveTv` | 4 | 2286.84 | 78.1% | 35.86% |
| `Jellyfin.Api/Helpers` | 8 | 1907.52 | 28.04% | 51.34% |
| `MediaBrowser.Providers/MediaInfo` | 12 | 1832.9 | 28.48% | 17.46% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `MediaBrowser.Controller/BaseItemManager/BaseItemManager.cs` -> **100.0%** Exposure
- `MediaBrowser.Controller/Extensions/ConfigurationExtensions.cs` -> **100.0%** Exposure
- `MediaBrowser.Controller/IO/IPathManager.cs` -> **99.9999%** Exposure
- `Jellyfin.Api/Extensions/ClaimsPrincipalExtensions.cs` -> **99.9994%** Exposure
- `MediaBrowser.Controller/Entities/AudioBook.cs` -> **99.9992%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Emby.Naming/Common/EpisodeExpression.cs` -> **100.0%** Exposure
- `Emby.Naming/Video/CleanStringParser.cs` -> **100.0%** Exposure
- `Emby.Photos/PhotoProvider.cs` -> **100.0%** Exposure
- `Emby.Server.Implementations/Dto/DtoService.cs` -> **100.0%** Exposure
- `Jellyfin.Api/Controllers/DisplayPreferencesController.cs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `MediaBrowser.Controller/Entities/BaseItem.cs` -> **44** Orphaned Functions | **0** Duplicates
- `Jellyfin.Api/Controllers/LiveTvController.cs` -> **39** Orphaned Functions | **0** Duplicates
- `Jellyfin.Api/Controllers/ImageController.cs` -> **27** Orphaned Functions | **0** Duplicates
- `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` -> **25** Orphaned Functions | **0** Duplicates
- `Emby.Server.Implementations/SyncPlay/Group.cs` -> **24** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `MediaBrowser.Providers/Plugins/Tmdb/TmdbUtils.cs` -> **99.9833%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10413` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `MediaBrowser.Controller/MediaEncoding/EncodingHelper.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5151.72 | **LOC:** 7852 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.3%), Guard Balance (formerly Safety Score) (72.5%)
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
* *Structure:* `branch: 1342`, `structural_boundaries: 1494`, `args: 229`, `func_start: 140`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 578`, `dead_code: 3`, `planned_debt: 7`, `fragile_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `io: 8`, `api: 102`, `concurrency: 1`, `import: 23`
* *Defense:* `safety: 256`, `doc: 209`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Common.Configuration, MediaBrowser.Common.Configuration.IConfigurationManager, MediaBrowser.Controller.Extensions, MediaBrowser.Controller.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2168.5 | **LOC:** 2737 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 42.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (94.5%), Complexity Load (formerly Cognitive Load) (60.6%)
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
* *Structure:* `branch: 423`, `structural_boundaries: 743`, `args: 488`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 427`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`, `unreferenced_by_name: 25`
* *Architecture:* `api: 34`, `concurrency: 23`, `import: 35`
* *Defense:* `safety: 147`, `doc: 77`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Jellyfin.Data.Enums, Jellyfin.Database.Implementations, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Entities.BaseItemEntity, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, Jellyfin.Extensions.Json, Jellyfin.Server.Implementations.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Model/Dlna/StreamBuilder.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1989.08 | **LOC:** 2400 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (52.4%), Complexity Load (formerly Cognitive Load) (45.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.1%)
- **Documentation Coverage:** 64.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ApplyTranscodingConditions` **(Many-Argument Workhorses)** (Impact: 532.2)
  * `BuildStreamVideoItem` **(Many-Argument Workhorses)** (Impact: 244.6)
  * `BuildVideoItem` **(Defensive Guards)** (Impact: 110.0)
  * `GetSubtitleProfile` **(Many-Argument Workhorses)** (Impact: 71.8)
    * *Intent:* /// <summary> /// Normalizes input container. /// </summary> /// <param name="mediaSource">The <see ...
  * `GetOptimalAudioStream` **(Many-Argument Workhorses)** (Impact: 69.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 138 instances
* *State Mutation (weighted view):* 438
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 629`, `structural_boundaries: 320`, `args: 96`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 162`, `planned_debt: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 12`, `import: 12`
* *Defense:* `safety: 203`, `doc: 81`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Model.Dto, MediaBrowser.Model.Entities, MediaBrowser.Model.Extensions, MediaBrowser.Model.MediaInfo, MediaBrowser.Model.Session, Microsoft.Extensions.Logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Emby.Server.Implementations/Session/SessionManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1415.94 | **LOC:** 2155 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.8%), Guard Balance (formerly Safety Score) (69.4%), Complexity Load (formerly Cognitive Load) (38.5%)
- **Documentation Coverage:** 26.2712% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetSessions` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* /// <inheritdoc/>
  * `SendPlayCommand` **(Many-Argument Workhorses)** (Impact: 42.2)
    * *Intent:* /// <inheritdoc />
  * `UpdateNowPlayingItem` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* /// <summary> /// Updates the now playing item id. /// </summary> /// <returns>Task.</returns>
  * `CreateSessionInfo` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `OnPlaybackStopped` **(Defensive Guards)** (Impact: 30.6)
    * *Intent:* /// <summary> /// Used to report that playback has ended for an item. /// </summary> /// <param name...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 132 instances
* *Concurrency (weighted view):* 174
* *State Mutation (weighted view):* 480
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 306`, `args: 130`, `func_start: 76`, `class_start: 1`
* *Risk/State:* `state_mutation: 216`, `unreferenced_by_name: 18`
* *Architecture:* `api: 52`, `concurrency: 99`, `import: 40`
* *Defense:* `safety: 112`, `doc: 165`, `immutability_locks: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Data.Queries, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Entities.Security, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Controllers/DynamicHlsController.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1351.64 | **LOC:** 2082 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.5%), Mutation Surface (formerly State Flux) (88.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.6%), Guard Balance (formerly Safety Score) (30.7%)
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
* *Structure:* `branch: 207`, `structural_boundaries: 191`, `args: 33`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 73`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 22`, `api: 10`, `concurrency: 51`, `import: 32`
* *Defense:* `safety: 146`, `doc: 431`, `immutability_locks: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Jellyfin.Api.Attributes, Jellyfin.Api.Extensions, Jellyfin.Api.Helpers, Jellyfin.Api.Models.StreamingDtos, Jellyfin.Data.Enums, Jellyfin.Extensions, Jellyfin.MediaEncoding.Hls.Playlist, MediaBrowser.Common.Configuration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Controller/Entities/BaseItem.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1349.4 | **LOC:** 2689 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.471; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (81.9%), Debt Markers (formerly Tech Debt) (75.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.9%)
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
* *Structure:* `branch: 259`, `structural_boundaries: 403`, `args: 178`, `func_start: 111`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 176`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 44`
* *Architecture:* `io: 13`, `api: 198`, `concurrency: 47`, `import: 34`
* *Defense:* `safety: 91`, `doc: 335`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000496
  * `Imports (Out-Degree: 4):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Channels, MediaBrowser.Controller.Chapters...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Emby.Server.Implementations/Dto/DtoService.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1305.72 | **LOC:** 1512 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.7%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AttachBasicFields` **(Many-Argument Workhorses)** (Impact: 254.3)
    * *Intent:* /// <summary> /// Sets simple property values on a DTOBaseItem. /// </summary> /// <param name="dto"...
  * `AddInheritedImages` **(Many-Argument Workhorses)** (Impact: 76.2)
  * `GetBaseItemDtoInternal` **(Many-Argument Workhorses)** (Impact: 47.3)
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
* *Structure:* `branch: 261`, `structural_boundaries: 192`, `args: 83`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 233`, `dead_code: 5`, `planned_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 4`, `import: 33`
* *Defense:* `safety: 134`, `doc: 30`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Extensions, MediaBrowser.Common, MediaBrowser.Controller.Channels, MediaBrowser.Controller.Chapters, MediaBrowser.Controller.Drawing, MediaBrowser.Controller.Dto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Probing/ProbeResultNormalizer.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1297.22 | **LOC:** 1761 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.0%), Complexity Load (formerly Cognitive Load) (35.3%)
- **Documentation Coverage:** 62.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetMediaStream` **(Many-Argument Workhorses)** (Impact: 200.7)
    * *Intent:* /// <summary> /// Converts ffprobe stream info to our MediaStream class. /// </summary> /// <param n...
  * `GetMediaInfo` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* /// <summary> /// Transforms a FFprobe response into its <see cref="MediaInfo"/> equivalent. /// </s...
  * `SetAudioInfoFromTags` **(Many-Argument Workhorses)** (Impact: 55.2)
  * `FetchWtvInfo` **(Many-Argument Workhorses)** (Impact: 38.4)
  * `ReadFromDictNode` **(Many-Argument Workhorses)** (Impact: 34.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 231`, `args: 62`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 192`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 17`
* *Defense:* `safety: 67`, `doc: 74`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Controller.Extensions, MediaBrowser.Controller.Library, MediaBrowser.Model.Dto, MediaBrowser.Model.Entities, MediaBrowser.Model.Globalization, MediaBrowser.Model.MediaInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1234.16 | **LOC:** 1483 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 55.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.9%), Complexity Load (formerly Cognitive Load) (69.7%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetItem` **(Compute Cores)** (Impact: 129.5)
  * `Perform` **(I/O & Config Routines)** (Impact: 72.8)
    * *Intent:* /// <inheritdoc/>
  * `GetMediaStream` **(Compute Cores)** (Impact: 62.9)
    * *Intent:* /// <summary> /// Gets the media stream. /// </summary> /// <param name="reader">The reader.</param>...
  * `ItemImageInfoFromValueString` **(Compute Cores)** (Impact: 26.4)
  * `GetUserData` **(Stateful Encapsulated Methods)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 263 instances
* *State Mutation (weighted view):* 825
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 295`, `args: 39`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 299`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 12`, `import: 23`
* *Defense:* `safety: 8`, `doc: 26`, `immutability_locks: 16`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Emby.Server.Implementations.Data, Jellyfin.Database.Implementations, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Entities.BaseItemEntity, Jellyfin.Database.Implementations.Entities.Chapter, Jellyfin.Extensions, Jellyfin.Server.Implementations.Item, Jellyfin.Server.ServerSetupApp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Providers/Manager/MetadataService.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1037.26 | **LOC:** 1316 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (97.5%), Guard Balance (formerly Safety Score) (75.4%), Complexity Load (formerly Cognitive Load) (58.4%)
- **Documentation Coverage:** 92.1053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MergeBaseItemData` **(Many-Argument Workhorses)** (Impact: 143.9)
  * `RefreshWithProviders` **(Many-Argument Workhorses)** (Impact: 84.0)
  * `RefreshMetadata` **(Stateful Encapsulated Methods)** (Impact: 68.3)
  * `ExecuteRemoteProviders` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `GetProviders` **(Many-Argument Workhorses)** (Impact: 23.0)
    * *Intent:* /// <summary> /// Gets the providers. /// </summary> /// <param name="item">A media item.</param> //...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 99 instances
* *Concurrency (weighted view):* 79
* *State Mutation (weighted view):* 327
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 190`, `args: 60`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 129`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 6`, `concurrency: 34`, `import: 19`
* *Defense:* `safety: 64`, `doc: 25`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Jellyfin.Extensions, MediaBrowser.Controller.Configuration, MediaBrowser.Controller.Entities, MediaBrowser.Controller.Entities.Audio, MediaBrowser.Controller.IO, MediaBrowser.Controller.Library, MediaBrowser.Controller.Persistence, MediaBrowser.Controller.Providers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Controller/Entities/Folder.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 985.3 | **LOC:** 1882 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 58.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Concurrency Surface (formerly Concurrency) (85.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.7%)
- **Documentation Coverage:** 68.9655% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ValidateChildrenInternal2` **(Many-Argument Workhorses)** (Impact: 100.5)
  * `AllowBoxSetCollapsing` **(Compute Cores)** (Impact: 58.3)
  * `RequiresPostFiltering` **(Compute Cores)** (Impact: 32.0)
  * `AddChildrenFromCollection` **(Many-Argument Workhorses)** (Impact: 24.5)
  * `GetLinkedChildren` **(Defensive Guards)** (Impact: 24.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 67
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 325`, `args: 104`, `func_start: 57`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 95`, `unreferenced_by_name: 11`
* *Architecture:* `io: 1`, `api: 54`, `concurrency: 37`, `import: 32`
* *Defense:* `safety: 79`, `doc: 132`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` J2N.Collections.Generic.Extensions, Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Controller.Channels, MediaBrowser.Controller.Collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.LiveTv/LiveTvManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 929.0 | **LOC:** 1293 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (82.0%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 131`, `structural_boundaries: 311`, `args: 110`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 159`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 33`, `concurrency: 94`, `import: 26`
* *Defense:* `safety: 47`, `doc: 14`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.LiveTv.Configuration, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Channels...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.LiveTv/Channels/ChannelManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 830.16 | **LOC:** 1216 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (67.6%), Complexity Load (formerly Cognitive Load) (48.3%)
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
* *Amplified Cascading Flux:* 86 instances
* *Concurrency (weighted view):* 132
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 242`, `args: 83`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 122`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 9`, `api: 23`, `concurrency: 82`, `import: 34`
* *Defense:* `safety: 82`, `doc: 62`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` AsyncKeyedLock, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, Jellyfin.Extensions.Json, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Channels...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 785.24 | **LOC:** 1400 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.2%), Concurrency Surface (formerly Concurrency) (54.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ExtractImageInternal` **(Many-Argument Workhorses)** (Impact: 87.5)
  * `ExtractVideoImagesOnIntervalAccelerated` **(Many-Argument Workhorses)** (Impact: 75.7)
    * *Intent:* /// <inheritdoc />
  * `ExtractVideoImagesOnIntervalInternal` **(Many-Argument Workhorses)** (Impact: 56.0)
  * `GetMediaInfoInternal` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* /// <summary> /// Gets the media info internal. /// </summary> /// <returns>Task{MediaInfoResult}.</...
  * `SetFFmpegPath` **(I/O & Config Routines)** (Impact: 24.3)
    * *Intent:* /// <summary> /// Run at startup to validate ffmpeg. /// Sets global variables FFmpegPath. /// Prece...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 59 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 210`, `args: 92`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 108`, `planned_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `io: 11`, `api: 55`, `concurrency: 26`, `import: 32`
* *Defense:* `safety: 49`, `doc: 58`, `sync_locks: 4`, `immutability_locks: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AsyncKeyedLock, Jellyfin.Data.Enums, Jellyfin.Extensions, Jellyfin.Extensions.Json, Jellyfin.Extensions.Json.Converters, MediaBrowser.Common, MediaBrowser.Common.Configuration, MediaBrowser.Common.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Controllers/ImageController.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 740.34 | **LOC:** 2070 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.1%), Mutation Surface (formerly State Flux) (71.7%), Guard Balance (formerly Safety Score) (39.6%), Debt Markers (formerly Tech Debt) (36.1%)
- **Documentation Coverage:** 24.3902% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetImageInternal` **(Many-Argument Workhorses)** (Impact: 94.4)
  * `GetImageResult` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `GetItemImageInfos` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* /// <summary> /// Get item image infos. /// </summary> /// <param name="itemId">Item id.</param> ///...
  * `GetUserImage` **(Many-Argument Workhorses)** (Impact: 14.6)
    * *Intent:* /// <summary> /// Get user profile image. /// </summary> /// <param name="userId">User id.</param> /...
  * `PostUserImage` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* /// <summary> /// Sets the user image. /// </summary> /// <param name="userId">User Id.</param> /// ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 121
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 227`, `args: 46`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `state_mutation: 52`, `dead_code: 2`, `unreferenced_by_name: 27`
* *Architecture:* `io: 9`, `api: 32`, `concurrency: 91`, `import: 35`
* *Defense:* `safety: 61`, `doc: 515`, `immutability_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Api.Attributes, Jellyfin.Api.Extensions, Jellyfin.Api.Helpers, Jellyfin.Extensions, MediaBrowser.Common.Api, MediaBrowser.Common.Configuration, MediaBrowser.Controller.Configuration, MediaBrowser.Controller.Drawing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.XbmcMetadata/Parsers/BaseNfoParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 720.26 | **LOC:** 1020 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (23.7%)
- **Documentation Coverage:** 52.9412% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FetchDataFromXmlNode` **(Many-Argument Workhorses)** (Impact: 272.5)
    * *Intent:* /// <summary> /// Fetches metadata from an XML node. /// </summary> /// <param name="reader">The <se...
  * `FetchFromVideoNode` **(Many-Argument Workhorses)** (Impact: 51.7)
  * `FetchThumbNode` **(Stateful Encapsulated Methods)** (Impact: 35.3)
  * `Fetch` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* /// <summary> /// Fetches the specified item. /// </summary> /// <param name="item">The <see cref="M...
  * `FetchFromRatingNode` **(Many-Argument Workhorses)** (Impact: 30.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 144`, `args: 26`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 64`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 22`
* *Defense:* `safety: 22`, `doc: 52`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Common.Configuration, MediaBrowser.Common.Providers, MediaBrowser.Controller.Entities, MediaBrowser.Controller.Entities.Movies, MediaBrowser.Controller.Entities.TV, MediaBrowser.Controller.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.LiveTv/DefaultLiveTvService.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 719.98 | **LOC:** 1000 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Complexity Load (formerly Cognitive Load) (81.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.6102% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UpdateTimersForSeriesTimer` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `CopyProgramInfoToTimerInfo` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `CreateTimer` **(Defensive Guards)** (Impact: 21.4)
  * `OnTimerManagerTimerFired` **(Defensive Guards)** (Impact: 20.2)
  * `CreateTimer` **(Many-Argument Workhorses)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 96
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 149`, `args: 55`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 152`, `unreferenced_by_name: 15`
* *Architecture:* `api: 27`, `concurrency: 51`, `import: 22`
* *Defense:* `safety: 45`, `doc: 2`, `immutability_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, Jellyfin.LiveTv.Configuration, Jellyfin.LiveTv.Timers, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Configuration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Server.Implementations/Users/UserManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 635.68 | **LOC:** 895 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (65.4%), Debt Markers (formerly Tech Debt) (57.7%)
- **Documentation Coverage:** 25.4902% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AuthenticateUser` **(Many-Argument Workhorses)** (Impact: 77.2)
    * *Intent:* /// <inheritdoc/>
  * `GetUserDto` **(Defensive Guards)** (Impact: 23.2)
    * *Intent:* /// <inheritdoc/>
  * `UpdatePolicyAsync` **(Callbacks & Closures)** (Impact: 12.5)
    * *Intent:* /// <inheritdoc/>
  * `RenameUser` **(Defensive Guards)** (Impact: 10.6)
    * *Intent:* /// <inheritdoc/>
  * `GetAuthenticationProviders` **(Stateful Encapsulated Methods)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 179
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 192`, `args: 87`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 113`, `planned_debt: 3`, `unreferenced_by_name: 12`
* *Architecture:* `api: 25`, `concurrency: 84`, `import: 29`
* *Defense:* `safety: 49`, `doc: 36`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Data.Events.Users, Jellyfin.Database.Implementations, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Controllers/ItemsController.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 612.36 | **LOC:** 1041 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.1%), Guard Balance (formerly Safety Score) (48.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.1%), Debt Markers (formerly Tech Debt) (11.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetItems` **(Many-Argument Workhorses)** (Impact: 408.9)
    * *Intent:* /// <param name="minWidth">Optional. Filter by the minimum width of the item.</param> /// <param nam...
  * `GetResumeItems` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* /// <param name="searchTerm">The search term.</param> /// <param name="parentId">Specify this to loc...
  * `UpdateItemUserData` **(Defensive Guards)** (Impact: 11.5)
    * *Intent:* /// <summary> /// Update Item User Data. /// </summary> /// <param name="userId">The user id.</param...
  * `GetItemUserData` **(Defensive Guards)** (Impact: 10.0)
    * *Intent:* /// <summary> /// Get Item User Data. /// </summary> /// <param name="userId">The user id.</param> /...
  * `GetResumeItemsLegacy` **(Many-Argument Workhorses)** (Impact: 9.8)
    * *Intent:* /// <param name="searchTerm">The search term.</param> /// <param name="parentId">Specify this to loc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 83`, `args: 22`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 42`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 10`, `import: 23`
* *Defense:* `safety: 36`, `doc: 266`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Api.Extensions, Jellyfin.Api.Helpers, Jellyfin.Api.ModelBinders, Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Common.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.LocalMetadata/Parsers/BaseItemXmlParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 587.38 | **LOC:** 873 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.9%), Complexity Load (formerly Cognitive Load) (21.3%)
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
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 43`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 3`, `import: 16`
* *Defense:* `safety: 10`, `doc: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Controller.Entities, MediaBrowser.Controller.Extensions, MediaBrowser.Controller.Playlists, MediaBrowser.Controller.Providers, MediaBrowser.Model.Entities, Microsoft.Extensions.Logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Jellyfin.Api/Helpers/StreamingHelpers.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 585.18 | **LOC:** 608 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (44.3%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Api.Extensions, Jellyfin.Data.Enums, Jellyfin.Extensions, MediaBrowser.Common.Configuration, MediaBrowser.Common.Extensions, MediaBrowser.Controller.Configuration, MediaBrowser.Controller.Entities, MediaBrowser.Controller.Library...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Providers/Manager/ProviderManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 584.16 | **LOC:** 1173 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.9%), Mutation Surface (formerly State Flux) (93.2%), Debt Markers (formerly Tech Debt) (67.8%), Guard Balance (formerly Safety Score) (44.6%)
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
* *Structure:* `branch: 93`, `structural_boundaries: 243`, `args: 105`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 75`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `io: 4`, `api: 31`, `concurrency: 52`, `import: 41`
* *Defense:* `safety: 74`, `doc: 70`, `sync_locks: 4`, `immutability_locks: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` AsyncKeyedLock, Jellyfin.Data.Enums, Jellyfin.Data.Events, Jellyfin.Extensions, MediaBrowser.Common.Net, MediaBrowser.Controller, MediaBrowser.Controller.BaseItemManager, MediaBrowser.Controller.Configuration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.Controller/Entities/UserViewBuilder.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 577.5 | **LOC:** 1028 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.5%), Complexity Load (formerly Cognitive Load) (41.2%)
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
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 79`, `dead_code: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 8`, `import: 17`
* *Defense:* `safety: 37`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Jellyfin.Data, Jellyfin.Data.Enums, Jellyfin.Database.Implementations.Entities, Jellyfin.Database.Implementations.Enums, Jellyfin.Extensions, MediaBrowser.Controller.Entities.TV.Episode, MediaBrowser.Controller.Entities.TV.Series, MediaBrowser.Controller.Library...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Jellyfin.Networking/Manager/NetworkManager.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 572.28 | **LOC:** 1178 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.8%), Complexity Load (formerly Cognitive Load) (22.0%)
- **Documentation Coverage:** 4.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetBindAddress` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* /// <inheritdoc/>
  * `InitializeOverrides` **(Compute Cores)** (Impact: 29.7)
    * *Intent:* /// <summary> /// Parses the user defined overrides into the dictionary object. /// Overrides are th...
  * `FilterBindSettings` **(Many-Argument Workhorses)** (Impact: 27.5)
    * *Intent:* /// <summary> /// Filters a list of bind addresses and exclusions on available interfaces. /// </sum...
  * `MatchesPublishedServerUrl` **(Many-Argument Workhorses)** (Impact: 25.1)
    * *Intent:* /// <summary> /// Attempts to match the source against the published server URL overrides. /// </sum...
  * `GetAllBindInterfaces` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* /// <summary> /// Reads the jellyfin configuration of the configuration manager and produces a list ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 209`, `args: 95`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 96`, `unreferenced_by_name: 3`
* *Architecture:* `api: 25`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 41`, `doc: 157`, `sync_locks: 8`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` J2N.Collections.Generic.Extensions, MediaBrowser.Common.Configuration, MediaBrowser.Common.Configuration.IConfigurationManager, MediaBrowser.Common.Net, MediaBrowser.Controller.Extensions.ConfigurationExtensions, MediaBrowser.Model.Net, Microsoft.AspNetCore.Http, Microsoft.Extensions.Configuration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MediaBrowser.MediaEncoding/Subtitles/SubtitleEncoder.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 571.0 | **LOC:** 1054 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 62.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.413; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (96.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.3%), Guard Balance (formerly Safety Score) (53.1%)
- **Documentation Coverage:** 68.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConvertTextSubtitleToSrtInternal` **(Many-Argument Workhorses)** (Impact: 37.1)
    * *Intent:* /// <summary> /// Converts the text subtitle to SRT internal. /// </summary> /// <param name="subtit...
  * `ExtractAllExtractableSubtitlesMKS` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `ExtractTextSubtitleInternal` **(Many-Argument Workhorses)** (Impact: 32.7)
  * `ExtractSubtitlesForFile` **(Many-Argument Workhorses)** (Impact: 32.3)
  * `ExtractAllExtractableSubtitlesInternal` **(Stateful Encapsulated Methods)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 103
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 192`, `args: 47`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 64`, `unreferenced_by_name: 2`
* *Architecture:* `io: 21`, `api: 12`, `concurrency: 68`, `import: 27`
* *Defense:* `safety: 55`, `doc: 41`, `immutability_locks: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AsyncKeyedLock, MediaBrowser.Common, MediaBrowser.Common.Configuration, MediaBrowser.Common.Extensions, MediaBrowser.Common.Net, MediaBrowser.Controller.Configuration, MediaBrowser.Controller.Entities, MediaBrowser.Controller.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Jellyfin.Server.Implementations/Item/BaseItemRepository.cs` -> Churn: **100.0%** | Cog Load: 60.5564% | Debt: 38.0995%
- `Jellyfin.Server/Migrations/Routines/MigrateLibraryDb.cs` -> Churn: **70.93%** | Cog Load: 69.6751% | Debt: 10.9772%
- `MediaBrowser.Controller/Entities/BaseItem.cs` -> Churn: **63.85%** | Cog Load: 24.6003% | Debt: 75.7351%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Jellyfin.LiveTv/LiveTvManager.cs` -> **evan314159** (100.0% isolated ownership) | Magnitude: 929.0
- `src/Jellyfin.LiveTv/Channels/ChannelManager.cs` -> **evan314159** (100.0% isolated ownership) | Magnitude: 830.16
- `MediaBrowser.MediaEncoding/Encoder/MediaEncoder.cs` -> **gnattu** (100.0% isolated ownership) | Magnitude: 785.24
- `MediaBrowser.Providers/Manager/ProviderManager.cs` -> **theguymadmax** (100.0% isolated ownership) | Magnitude: 584.16
- `MediaBrowser.Providers/MediaInfo/FFProbeVideoInfo.cs` -> **IceStormNG** (100.0% isolated ownership) | Magnitude: 551.8

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `MediaBrowser.Controller/Entities/Video.cs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.6653%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `MediaBrowser.Controller/Entities/Extensions.cs` -> **Severity: 6.802** (Embedded: 0.1096 * Error Risk: 62.0779%)
- `src/Jellyfin.Database/Jellyfin.Database.Implementations/Entities/Libraries/Library.cs` -> **Severity: 5.908** (Embedded: 0.1254 * Error Risk: 47.1104%)
- `MediaBrowser.Controller/Entities/Audio/Audio.cs` -> **Severity: 2.927** (Embedded: 0.0438 * Error Risk: 66.8914%)
- `MediaBrowser.Model/MediaInfo/MediaInfo.cs` -> **Severity: 1.949** (Embedded: 0.0308 * Error Risk: 63.3804%)
- `MediaBrowser.Controller/Entities/Video.cs` -> **Severity: 0.388** (Embedded: 0.006 * Error Risk: 65.1159%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `MediaBrowser.Controller/Entities/Audio/Audio.cs` -> **Severity: 1641.592** (Blast Radius: 20.893 * Doc Risk: 78.5714%)
- `MediaBrowser.Model/MediaInfo/MediaInfo.cs` -> **Severity: 1353.5** (Blast Radius: 13.535 * Doc Risk: 100.0%)
- `MediaBrowser.Controller/Entities/Video.cs` -> **Severity: 378.791** (Blast Radius: 4.441 * Doc Risk: 85.2941%)
- `MediaBrowser.Controller/Entities/AudioBook.cs` -> **Severity: 181.4** (Blast Radius: 1.814 * Doc Risk: 100.0%)
- `MediaBrowser.Controller/Playlists/Playlist.cs` -> **Severity: 124.5** (Blast Radius: 1.245 * Doc Risk: 100.0%)

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
