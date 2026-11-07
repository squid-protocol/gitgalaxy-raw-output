# ARCHITECTURAL_BRIEF: exiftool
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/exiftool/exiftool` |
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
- **Scope:** 1050 analyzed artifact(s), 521420 LOC.
- **Load-bearing artifact:** `lib/Image/ExifTool/Exif.pm` -- 46 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/Image/ExifTool.pm` -- pulls in 49 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/Image/ExifTool.pod` at magnitude 32502.48 (structural weight, not risk).
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
| Total Artifacts | 1252 |
| Analyzed Artifacts (Scanned) | 1050 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 202 |
| Total LOC | 521420 |
| Volatility Index | 0.015 |
| % Scanned of codebase = | 83.9% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5606 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0892 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2312 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 87 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 481 | 0 | 45.8% |
| PERL | 356 | 347867 | 33.9% |
| HTML | 174 | 173289 | 16.6% |
| XML | 30 | 0 | 2.9% |
| JSON | 2 | 74 | 0.2% |
| MARKDOWN | 2 | 0 | 0.2% |
| CSS | 2 | 59 | 0.2% |
| CSV | 2 | 96 | 0.2% |
| YAML | 1 | 35 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 16 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1032 |
| cp1252 | cp1252-fallback | 9 |
| latin-1 | latin-1-fallback | 7 |
| utf-16-be | bom | 1 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 66%, Declarative / Non-Code 17%, Compute Cores Files 7%, Many-Argument Workhorses Files 5%, Large Core Modules (3) 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 567 | 54.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 483 | 46.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 202*

**Composition by Extension & Reason:**
- `.jpg`: 41x Excluded (Explicitly Denied Extension: '.jpg')
- `.html`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2086 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 15764 LOC), 1x Excluded (Machine-Generated Source Code Signature: 692 LOC)
- `.pdf`: 7x Excluded (Explicitly Denied Extension: '.pdf')
- `.pm`: 1x Excluded (Embedded Hex Payload: 13758 hex tokens in 1736 LOC), 1x Excluded (Embedded Hex Payload: 15064 hex tokens in 2089 LOC), 1x Excluded (Embedded Hex Payload: 27045 hex tokens in 3624 LOC)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.log`: 3x Excluded (Unsupported Extension: '.log')
- `no_extension`: 1x Excluded (Machine-Generated Source Code Signature: 11924 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tif`: 2x Excluded (Unsupported Extension: '.tif')
- `.ogg`: 2x Excluded (Explicitly Denied Extension: '.ogg')
- `.pfm`: 2x Excluded (Unsupported Extension: '.pfm')
- `.jxl`: 2x Excluded (Unsupported Extension: '.jxl')
- `.avi`: 2x Excluded (Explicitly Denied Extension: '.avi')
- `.x3f`: 2x Excluded (Unsupported Extension: '.x3f')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dat`: 1x Excluded (Unsupported Extension: '.dat')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.1 | 23.1 | 8.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 90.4 | 34.9 | 51.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.8 | 4.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 51.2 | 3.4 | 2.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 39.4 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 48.0 | 37.6 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.8 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.3 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 10.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 32.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5037 | 194 | 6 | `lib/Image/ExifTool.pm` |
| cleanup | 1054 | 204 | 1 | `exiftool` |
| guards | 687 | 281 | 1 | `lib/Image/ExifTool.pm` |
| danger | 265 | 50 | 0 | `build_geolocation` |
| concurrency | 123 | 15 | 0 | `lib/Image/ExifTool/CanonCustom.pm` |
| connectivity | 4623 | 305 | 9 | `html/ancient_history.html` |
| io | 20829 | 212 | 11 | `html/makernote_types.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 39 | 12 | 0 | `validate` |
| time | 378 | 48 | 0 | `exiftool` |
| serialization | 0 | 0 | 0 | - |
| regex | 7868 | 194 | 11 | `lib/Image/ExifTool/Sony.pm` |
| events | 1459 | 150 | 2 | `lib/Image/ExifTool/Writer.pl` |
| tests | 6 | 5 | 0 | `lib/Image/ExifTool/TagNames.pod` |
| docs | 386 | 384 | 1 | `html/index.html` |
| debt | 2387 | 228 | 4 | `html/ancient_history.html` |
| mutation | 158585 | 503 | 351 | `html/makernote_types.html` |
| dead_code | 313 | 123 | 1 | `lib/Image/ExifTool.pm` |
| credential | 58 | 13 | 0 | `lib/Image/ExifTool/Sony.pm` |
| threat | 190 | 46 | 0 | `lib/Image/ExifTool.pm` |
| ml_ai | 1538 | 101 | 0 | `lib/Image/ExifTool/Sony.pm` |
| ui | 2800 | 187 | 1 | `html/ancient_history.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `html/makernote_types.html` (Hits: 8241)
- `html/index.html` (Hits: 1926)
- `html/ancient_history.html` (Hits: 1561)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Exif.pm** (`lib/Image/ExifTool/Exif.pm`) — 46 inbound connections
2. **XMP.pm** (`lib/Image/ExifTool/XMP.pm`) — 44 inbound connections
3. **Writer.pl** (`lib/Image/ExifTool/Writer.pl`) — 36 inbound connections
4. **RandomAccess.pm** (`lib/File/RandomAccess.pm`) — 30 inbound connections
5. **GPS.pm** (`lib/Image/ExifTool/GPS.pm`) — 18 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ExifTool.pm** (`lib/Image/ExifTool.pm`) — 49 outbound dependencies
2. **BuildTagLookup.pm** (`lib/Image/ExifTool/BuildTagLookup.pm`) — 27 outbound dependencies
3. **exiftool** (`exiftool`) — 25 outbound dependencies
4. **windows_exiftool** (`windows_exiftool`) — 25 outbound dependencies
5. **Writer.pl** (`lib/Image/ExifTool/Writer.pl`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `WriteQuickTime` **(Many-Argument Workhorses)** (@ `lib/Image/ExifTool/WriteQuickTime.pl`) -> Impact: **1144.8** | LOC: 1296
  * *Intent:* #------------------------------------------------------------------------------ # Write a series of QuickTime atoms from file or in memory # Inputs: 0...
- `WriteExif` **(Many-Argument Workhorses)** (@ `lib/Image/ExifTool/WriteExif.pl`) -> Impact: **1074.2** | LOC: 1685
  * *Intent:* #------------------------------------------------------------------------------ # Write EXIF directory # Inputs: 0) ExifTool object ref, 1) source dir...
- `SetNewValue` **(Many-Argument Workhorses)** (@ `lib/Image/ExifTool/Writer.pl`) -> Impact: **1063.7** | LOC: 926
  * *Intent:* # EditOnly - flag set if tag should never be created (regardless of file type). # If this is set, then IsCreating must be false # CreateOnly - flag se...
- `GetImageInfo` **(Many-Argument Workhorses)** (@ `exiftool`) -> Impact: **892.5** | LOC: 1015
  * *Intent:* #------------------------------------------------------------------------------ # Get image information from EXIF data in file (or write file if writi...
- `GetImageInfo` **(Many-Argument Workhorses)** (@ `windows_exiftool`) -> Impact: **892.5** | LOC: 1015
  * *Intent:* #------------------------------------------------------------------------------ # Get image information from EXIF data in file (or write file if writi...
- `ProcessJPEG` **(Many-Argument Workhorses)** (@ `lib/Image/ExifTool.pm`) -> Impact: **824.8** | LOC: 1216
  * *Intent:* #------------------------------------------------------------------------------ # Extract metadata from a jpg image # Inputs: 0) ExifTool object refer...
- `LoadTrackLog` **(Many-Argument Workhorses)** (@ `lib/Image/ExifTool/Geotag.pm`) -> Impact: **735.3** | LOC: 746
  * *Intent:* # fixtype- type of fix ('none'|'2d'|'3d'|'dgps'|'pps') # pdop - dilution of precision # hdop - horizontal DOP # vdop - vertical DOP # sats - comma-sep...
- `ProcessExif` **(Many-Argument Workhorses)** (@ `lib/Image/ExifTool/Exif.pm`) -> Impact: **727.8** | LOC: 916
  * *Intent:* #------------------------------------------------------------------------------ # Process EXIF directory # Inputs: 0) ExifTool ref, 1) dirInfo ref, 2)...
- `WriteJPEG` **(Many-Argument Workhorses)** (@ `lib/Image/ExifTool/Writer.pl`) -> Impact: **695.5** | LOC: 1127
  * *Intent:* #------------------------------------------------------------------------------ # Inputs: 0) ExifTool object reference, 1) dirInfo reference # Returns...
- `ParseXMPElement` **(Many-Argument Workhorses)** (@ `lib/Image/ExifTool/XMP.pm`) -> Impact: **648.1** | LOC: 461
  * *Intent:* #------------------------------------------------------------------------------ # Recursively parse nested XMP data element # Inputs: 0) ExifTool ref,...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/Image/ExifTool` | 189 | 100650.07 | 40.95% | 8.94% |
| `lib/Image` | 2 | 42883.18 | 62.52% | 12.02% |
| `__monolith__` | 12 | 11961.18 | 39.06% | 1.64% |
| `t` | 561 | 5121.9 | 7.95% | 0.04% |
| `lib/Image/ExifTool/Lang` | 18 | 1523.34 | 4.3% | 3.47% |
| `lib/File` | 2 | 459.5 | 60.49% | 46.72% |
| `lib/Image/ExifTool/Charset` | 26 | 404.42 | 0.0% | 0.0% |
| `config_files` | 20 | 210.4 | 0.0% | 0.0% |
| `t/images` | 23 | 154.6 | 0.0% | 0.0% |
| `html` | 37 | 76.99 | 3.05% | 9.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/Image/ExifTool/Other.pm` -> **98.8393%** Exposure
- `lib/File/RandomAccess.pm` -> **93.4395%** Exposure
- `html/config.html` -> **80.7991%** Exposure
- `html/ancient_history.html` -> **66.479%** Exposure
- `lib/Image/ExifTool/JSON.pm` -> **41.1651%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `build_geolocation` -> **100.0%** Exposure
- `exiftool` -> **100.0%** Exposure
- `lib/File/RandomAccess.pm` -> **100.0%** Exposure
- `lib/Image/ExifTool.pm` -> **100.0%** Exposure
- `lib/Image/ExifTool/7Z.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/Image/ExifTool.pm` -> **32** Orphaned Functions | **0** Duplicates
- `lib/Image/ExifTool/Writer.pl` -> **32** Orphaned Functions | **0** Duplicates
- `lib/Image/ExifTool/QuickTimeStream.pl` -> **15** Orphaned Functions | **0** Duplicates
- `lib/Image/ExifTool/WriteExif.pl` -> **8** Orphaned Functions | **0** Duplicates
- `lib/Image/ExifTool/WriteIPTC.pl` -> **7** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1493` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/Image/ExifTool.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.898)
- **Top Global Matches:** file_cluster_2: 4.898, file_cluster_13: 5.753, file_cluster_17: 6.246
- **Magnitude:** 32502.48 | **LOC:** 3093 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (62.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.1%), Guard Balance (formerly Safety Score) (53.6%), Complexity Load (formerly Cognitive Load) (29.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 49 instances
* *Memory Alloc (weighted view):* 78
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 780`, `structural_boundaries: 174`, `args: 15`, `func_start: 1`
* *Risk/State:* `state_mutation: 57`, `fragile_debt: 2`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 2`, `import: 48`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Image/ExifTool.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.429)
- **Top Global Matches:** file_cluster_6: 7.429, file_cluster_4: 13.109, file_cluster_8: 13.486
- **Magnitude:** 10380.7 | **LOC:** 10226 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **49**; blast radius 0.573; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessJPEG` **(Many-Argument Workhorses)** (Impact: 824.8)
    * *Intent:* #------------------------------------------------------------------------------ # Extract metadata f...
  * `ExtractInfo` **(Compute Cores)** (Impact: 296.6)
    * *Intent:* #------------------------------------------------------------------------------ # Extract meta infor...
  * `DoProcessTIFF` **(Many-Argument Workhorses)** (Impact: 279.0)
    * *Intent:* #------------------------------------------------------------------------------ # Process TIFF data ...
  * `ProcessBinaryData` **(Many-Argument Workhorses)** (Impact: 276.9)
    * *Intent:* #------------------------------------------------------------------------------ # Process binary dat...
  * `Options` **(Many-Argument Workhorses)** (Impact: 271.2)
    * *Intent:* #------------------------------------------------------------------------------ # Get/set ExifTool o...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 77 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1543 instances
* *Concurrency (weighted view):* 10
* *Memory Alloc (weighted view):* 157
* *State Mutation (weighted view):* 4769
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2804`, `structural_boundaries: 1865`, `args: 373`, `func_start: 237`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 1683`, `dead_code: 4`, `fragile_debt: 8`, `unreferenced_by_name: 32`
* *Architecture:* `io: 3`, `api: 240`, `concurrency: 5`, `import: 82`
* *Defense:* `safety: 57`, `cleanup: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` CodedCharacterSet, Compact, Cwd, Digest::MD5, Digest::SHA, Encode, Exporter, File::Basename...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Image/ExifTool/Writer.pl` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.049)
- **Top Global Matches:** file_cluster_8: 7.049, file_cluster_6: 12.891, file_cluster_4: 21.306
- **Magnitude:** 9946.7 | **LOC:** 7415 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); it depends on **24**; blast radius 44.009; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.1%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SetNewValue` **(Many-Argument Workhorses)** (Impact: 1063.7)
    * *Intent:* # EditOnly - flag set if tag should never be created (regardless of file type). # If this is set, th...
  * `WriteJPEG` **(Many-Argument Workhorses)** (Impact: 695.5)
    * *Intent:* #------------------------------------------------------------------------------ # Inputs: 0) ExifToo...
  * `WriteInfo` **(Many-Argument Workhorses)** (Impact: 405.3)
    * *Intent:* #------------------------------------------------------------------------------ # Write information ...
  * `SetNewValuesFromFile` **(Many-Argument Workhorses)** (Impact: 405.1)
    * *Intent:* # set new values from information in specified file # Inputs: 0) ExifTool object reference, 1) sourc...
  * `InsertTagValues` **(Many-Argument Workhorses)** (Impact: 369.3)
    * *Intent:* # 'Warn' - issue minor warning on missing tag (and return undef if warning sent) # 'Silent' - just r...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 78 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1351 instances
* *Concurrency (weighted view):* 24
* *Memory Alloc (weighted view):* 54
* *State Mutation (weighted view):* 4117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2458`, `structural_boundaries: 1452`, `args: 196`, `func_start: 108`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 1415`, `dead_code: 1`, `fragile_debt: 5`, `unreferenced_by_name: 32`
* *Architecture:* `io: 2`, `api: 108`, `concurrency: 4`, `import: 40`
* *Defense:* `safety: 50`, `doc: 1`, `cleanup: 76`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.009
  * `Choke Point (Betweenness):` 0.003096 | `Ripple Effect (Closeness):` 0.083326
  * `Imports (Out-Degree: 14):` Cwd, Encode, Image::ExifTool::Canon, Image::ExifTool::CanonRaw, Image::ExifTool::CanonVRD, Image::ExifTool::Fixup, Image::ExifTool::MacOS, Image::ExifTool::Panasonic...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `exiftool` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.018)
- **Top Global Matches:** file_cluster_6: 10.018, file_cluster_8: 10.192, file_cluster_4: 17.47
- **Magnitude:** 5680.7 | **LOC:** 8139 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.573; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Complexity Load (formerly Cognitive Load) (97.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetImageInfo` **(Many-Argument Workhorses)** (Impact: 892.5)
    * *Intent:* #------------------------------------------------------------------------------ # Get image informat...
  * `SetImageInfo` **(Many-Argument Workhorses)** (Impact: 445.3)
    * *Intent:* #------------------------------------------------------------------------------ # Set information in...
  * `ScanDir` **(Many-Argument Workhorses)** (Impact: 130.4)
    * *Intent:* #------------------------------------------------------------------------------ # Scan directory for...
  * `FilenameSPrintf` **(Compute Cores)** (Impact: 84.8)
    * *Intent:* #------------------------------------------------------------------------------ # A sort of sprintf ...
  * `NextUnusedFilename` **(Compute Cores)** (Impact: 78.8)
    * *Intent:* #------------------------------------------------------------------------------ # Expand '%c' and '%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 184 instances
* *Amplified Cascading Flux:* 1001 instances
* *High Risk Execution (weighted view):* 6
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 3055
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3051`, `structural_boundaries: 1103`, `args: 195`, `func_start: 100`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 7`, `state_mutation: 1053`, `dead_code: 3`, `fragile_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `io: 308`, `api: 100`, `concurrency: 2`, `import: 110`
* *Defense:* `safety: 26`, `doc: 1`, `cleanup: 202`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Cwd, Encode, File::Glob, FileHandle, IO::Handle, Image::ExifTool, Image::ExifTool::Geolocation, Image::ExifTool::HTML...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `windows_exiftool` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.576)
- **Top Global Matches:** file_cluster_6: 9.576, file_cluster_8: 10.339, file_cluster_4: 16.985
- **Magnitude:** 5574.52 | **LOC:** 5069 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.573; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Complexity Load (formerly Cognitive Load) (98.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetImageInfo` **(Many-Argument Workhorses)** (Impact: 892.5)
    * *Intent:* #------------------------------------------------------------------------------ # Get image informat...
  * `SetImageInfo` **(Many-Argument Workhorses)** (Impact: 445.3)
    * *Intent:* #------------------------------------------------------------------------------ # Set information in...
  * `ScanDir` **(Many-Argument Workhorses)** (Impact: 130.4)
    * *Intent:* #------------------------------------------------------------------------------ # Scan directory for...
  * `FilenameSPrintf` **(Compute Cores)** (Impact: 84.8)
    * *Intent:* #------------------------------------------------------------------------------ # A sort of sprintf ...
  * `NextUnusedFilename` **(Compute Cores)** (Impact: 78.8)
    * *Intent:* #------------------------------------------------------------------------------ # Expand '%c' and '%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 185 instances
* *Amplified Cascading Flux:* 981 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 2993
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2154`, `structural_boundaries: 1043`, `args: 184`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 1031`, `dead_code: 3`, `fragile_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 7`, `api: 101`, `import: 40`
* *Defense:* `safety: 26`, `cleanup: 201`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Cwd, Encode, File::Glob, FileHandle, IO::Handle, Image::ExifTool, Image::ExifTool::Geolocation, Image::ExifTool::HTML...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Image/ExifTool/QuickTimeStream.pl` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.26)
- **Top Global Matches:** file_cluster_3: 10.26, file_cluster_8: 14.571, file_cluster_6: 27.266
- **Magnitude:** 3826.18 | **LOC:** 3806 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.573; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Process_text` **(Many-Argument Workhorses)** (Impact: 454.9)
    * *Intent:* #------------------------------------------------------------------------------ # Process subtitle '...
  * `ProcessFreeGPS` **(Many-Argument Workhorses)** (Impact: 426.4)
    * *Intent:* #------------------------------------------------------------------------------ # Process "freeGPS "...
  * `ProcessSamples` **(Compute Cores)** (Impact: 172.8)
    * *Intent:* #------------------------------------------------------------------------------ # Extract embedded m...
  * `ProcessInsta360` **(Many-Argument Workhorses)** (Impact: 147.9)
    * *Intent:* #------------------------------------------------------------------------------ # Extract informatio...
  * `ProcessNMEA` **(Compute Cores)** (Impact: 114.8)
    * *Intent:* #------------------------------------------------------------------------------ # Process 'gps ' ato...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 538 instances
* *Memory Alloc (weighted view):* 24
* *State Mutation (weighted view):* 1678
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 989`, `structural_boundaries: 491`, `args: 71`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 602`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 41`, `import: 9`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Image::ExifTool, Image::ExifTool::GoPro, Image::ExifTool::H264, Image::ExifTool::Import, Image::ExifTool::QuickTime, Image::ExifTool::XMP, Time::Local, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Image/ExifTool/BuildTagLookup.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.942)
- **Top Global Matches:** file_cluster_3: 8.942, file_cluster_8: 28.861, file_cluster_6: 41.889
- **Magnitude:** 3184.32 | **LOC:** 2873 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **27**; blast radius 1.061; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Compute Cores)** (Impact: 556.9)
    * *Intent:* #------------------------------------------------------------------------------ # New - create new B...
  * `WriteTagNames` **(Many-Argument Workhorses)** (Impact: 535.6)
    * *Intent:* #------------------------------------------------------------------------------ # Write the TagName ...
  * `WriteTagLookup` **(Many-Argument Workhorses)** (Impact: 84.0)
    * *Intent:* #------------------------------------------------------------------------------ # Rewrite this file ...
  * `CloseHtmlFiles` **(Compute Cores)** (Impact: 37.5)
    * *Intent:* #------------------------------------------------------------------------------ # Close all html fil...
  * `NumbersFirst` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* #------------------------------------------------------------------------------ # Sort numbers first...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 566 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 1738
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 975`, `structural_boundaries: 426`, `args: 25`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 606`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 18`, `api: 16`, `import: 30`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.061
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.000953
  * `Imports (Out-Degree: 11):` C, Exporter, Image::ExifTool, Image::ExifTool::Canon, Image::ExifTool::Exif, Image::ExifTool::HTML, Image::ExifTool::IPTC, Image::ExifTool::MacOS...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/WriteQuickTime.pl` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 12.104)
- **Top Global Matches:** file_cluster_3: 12.104, file_cluster_8: 12.797, file_cluster_6: 25.324
- **Magnitude:** 3174.94 | **LOC:** 2280 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.573; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.8%), Guard Balance (formerly Safety Score) (81.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WriteQuickTime` **(Many-Argument Workhorses)** (Impact: 1144.8)
    * *Intent:* #------------------------------------------------------------------------------ # Write a series of ...
  * `WriteItemInfo` **(Many-Argument Workhorses)** (Impact: 287.4)
    * *Intent:* #------------------------------------------------------------------------------ # Write ItemInformat...
  * `Handle_iloc` **(Many-Argument Workhorses)** (Impact: 85.0)
    * *Intent:* #------------------------------------------------------------------------------ # Handle offsets in ...
  * `WriteKeys` **(Many-Argument Workhorses)** (Impact: 77.2)
    * *Intent:* #------------------------------------------------------------------------------ # Write Meta Keys to...
  * `FormatQTValue` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* #------------------------------------------------------------------------------ # Format QuickTime v...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 465 instances
* *Memory Alloc (weighted view):* 14
* *State Mutation (weighted view):* 1405
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 819`, `structural_boundaries: 418`, `args: 24`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 475`, `planned_debt: 8`, `fragile_debt: 4`, `unreferenced_by_name: 6`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Compress::Zlib, Image::ExifTool::MIE, country, language, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Image/ExifTool/Exif.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.752)
- **Top Global Matches:** file_cluster_8: 8.752, file_cluster_6: 9.388, file_cluster_4: 17.437
- **Magnitude:** 3145.82 | **LOC:** 7230 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **14**; blast radius 73.235; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.9%), Complexity Load (formerly Cognitive Load) (61.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessExif` **(Many-Argument Workhorses)** (Impact: 727.8)
    * *Intent:* #------------------------------------------------------------------------------ # Process EXIF direc...
  * `PrintLensID` **(Many-Argument Workhorses)** (Impact: 315.8)
  * `CalcScaleFactor35efl` **(Many-Argument Workhorses)** (Impact: 89.6)
    * *Intent:* #------------------------------------------------------------------------------ # Calculate scale fa...
  * `ConvertExifText` **(Many-Argument Workhorses)** (Impact: 62.8)
    * *Intent:* #------------------------------------------------------------------------------ # Convert EXIF text ...
  * `GetLensInfo` **(Compute Cores)** (Impact: 35.5)
    * *Intent:* #------------------------------------------------------------------------------ # Get lens info from...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 472 instances
* *Memory Alloc (weighted view):* 137
* *State Mutation (weighted view):* 1454
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1159`, `structural_boundaries: 690`, `args: 85`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 510`, `fragile_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 44`, `import: 19`
* *Defense:* `safety: 21`, `doc: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 73.235
  * `Choke Point (Betweenness):` 0.002585 | `Ripple Effect (Closeness):` 0.082725
  * `Imports (Out-Degree: 12):` Image::ExifTool, Image::ExifTool::ASF, Image::ExifTool::Canon, Image::ExifTool::Fixup, Image::ExifTool::GPS, Image::ExifTool::ICC_Profile, Image::ExifTool::MakerNotes, Image::ExifTool::Minolta...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/QuickTime.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.961)
- **Top Global Matches:** file_cluster_6: 7.961, file_cluster_8: 10.307, file_cluster_4: 15.467
- **Magnitude:** 3077.24 | **LOC:** 10736 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 2.236; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.3%), Guard Balance (formerly Safety Score) (57.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessMOV` **(Many-Argument Workhorses)** (Impact: 593.7)
    * *Intent:* #------------------------------------------------------------------------------ # Process a QuickTim...
  * `HandleItemInfo` **(Compute Cores)** (Impact: 128.7)
    * *Intent:* #------------------------------------------------------------------------------ # Process item infor...
  * `ProcessKeys` **(Many-Argument Workhorses)** (Impact: 72.9)
    * *Intent:* #------------------------------------------------------------------------------ # Read Meta Keys and...
  * `ConvertISO6709` **(Compute Cores)** (Impact: 59.3)
    * *Intent:* #------------------------------------------------------------------------------ # Convert ISO 6709 s...
  * `ParseItemLocation` **(Compute Cores)** (Impact: 44.8)
    * *Intent:* # infe - raw data for 'infe' box (when writing only) [retracted] # ipma: # Association - list of ass...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Cascading Flux:* 484 instances
* *Memory Alloc (weighted view):* 117
* *State Mutation (weighted view):* 1512
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1018`, `structural_boundaries: 801`, `args: 112`, `func_start: 80`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 544`, `fragile_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 80`, `import: 17`
* *Defense:* `safety: 10`, `doc: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.236
  * `Choke Point (Betweenness):` 0.00013 | `Ripple Effect (Closeness):` 0.003972
  * `Imports (Out-Degree: 9):` Compress::Zlib, Image::ExifTool, Image::ExifTool::Exif, Image::ExifTool::Font, Image::ExifTool::GPS, Image::ExifTool::ID3, Image::ExifTool::LigoGPS, Image::ExifTool::MIE...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/XMP.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.826)
- **Top Global Matches:** file_cluster_8: 6.826, file_cluster_6: 17.324, file_cluster_3: 19.985
- **Magnitude:** 2959.22 | **LOC:** 4685 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **44** in-repo importer(s); it depends on **10**; blast radius 32.862; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseXMPElement` **(Many-Argument Workhorses)** (Impact: 648.1)
    * *Intent:* #------------------------------------------------------------------------------ # Recursively parse ...
  * `ProcessXMP` **(Many-Argument Workhorses)** (Impact: 355.8)
    * *Intent:* #------------------------------------------------------------------------------ # Process XMP data #...
  * `FoundXMP` **(Many-Argument Workhorses)** (Impact: 255.3)
    * *Intent:* #------------------------------------------------------------------------------ # We found an XMP pr...
  * `AddFlattenedTags` **(Many-Argument Workhorses)** (Impact: 115.1)
    * *Intent:* #------------------------------------------------------------------------------ # Generate flattened...
  * `PrintLensID` **(Many-Argument Workhorses)** (Impact: 63.1)
    * *Intent:* #------------------------------------------------------------------------------ # Inputs: 0) ExifToo...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 17 instances
* *Amplified Cascading Flux:* 389 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 1191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1054`, `structural_boundaries: 407`, `args: 61`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 413`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 8`, `unreferenced_by_name: 5`
* *Architecture:* `api: 41`, `import: 13`
* *Defense:* `safety: 10`, `doc: 1`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.862
  * `Choke Point (Betweenness):` 0.00166 | `Ripple Effect (Closeness):` 0.085394
  * `Imports (Out-Degree: 5):` Exporter, Image::ExifTool, Image::ExifTool::Charset, Image::ExifTool::Exif, Image::ExifTool::GPS, Image::ExifTool::PDF, closing, in...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/WriteExif.pl` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_6: 6.526, file_cluster_8: 11.783, file_cluster_4: 13.642
- **Magnitude:** 2898.2 | **LOC:** 2748 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.573; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.6%), Guard Balance (formerly Safety Score) (80.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WriteExif` **(Many-Argument Workhorses)** (Impact: 1074.2)
    * *Intent:* #------------------------------------------------------------------------------ # Write EXIF directo...
  * `ValidateImageData` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* #------------------------------------------------------------------------------ # Validate image dat...
  * `AddImageDataHash` **(Compute Cores)** (Impact: 43.9)
    * *Intent:* #------------------------------------------------------------------------------ # Add specified imag...
  * `RebuildMakerNotes` **(Many-Argument Workhorses)** (Impact: 33.0)
    * *Intent:* #------------------------------------------------------------------------------ # rebuild maker note...
  * `ProcessTiffIFD` **(Compute Cores)** (Impact: 30.6)
    * *Intent:* #------------------------------------------------------------------------------ # Read/Write IFD wit...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 21 instances
* *Amplified Cascading Flux:* 480 instances
* *Memory Alloc (weighted view):* 30
* *State Mutation (weighted view):* 1500
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 727`, `structural_boundaries: 515`, `args: 30`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 540`, `fragile_debt: 5`, `unreferenced_by_name: 8`
* *Architecture:* `api: 15`, `import: 7`
* *Defense:* `safety: 5`, `doc: 1`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Image::ExifTool::Canon, Image::ExifTool::Fixup, Image::ExifTool::PanasonicRaw, Image::ExifTool::Sony, offset, strict, vars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Image/ExifTool/Geotag.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.736)
- **Top Global Matches:** file_cluster_8: 8.736, file_cluster_6: 10.829, file_cluster_4: 18.877
- **Magnitude:** 2555.42 | **LOC:** 1693 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 1.085; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.3%), Guard Balance (formerly Safety Score) (86.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LoadTrackLog` **(Many-Argument Workhorses)** (Impact: 735.3)
    * *Intent:* # fixtype- type of fix ('none'|'2d'|'3d'|'dgps'|'pps') # pdop - dilution of precision # hdop - horiz...
  * `SetGeoValues` **(Many-Argument Workhorses)** (Impact: 385.9)
    * *Intent:* #------------------------------------------------------------------------------ # Set new geotagging...
  * `ConvertGeosync` **(Compute Cores)** (Impact: 97.4)
    * *Intent:* #------------------------------------------------------------------------------ # Convert Geotagging...
  * `FindFix` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* #------------------------------------------------------------------------------ # Find nearest fix c...
  * `ScanOutwards` **(Many-Argument Workhorses)** (Impact: 19.3)
    * *Intent:* #------------------------------------------------------------------------------ # Scan outwards for ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 388 instances
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 1171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 699`, `structural_boundaries: 257`, `args: 29`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 395`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 17`, `import: 9`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.085
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.001907
  * `Imports (Out-Degree: 2):` Image::ExifTool, Image::ExifTool::GPS, Time::Local, YYYY, strict, time, vars
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/PDF.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.416)
- **Top Global Matches:** file_cluster_8: 11.416, file_cluster_3: 13.817, file_cluster_6: 23.661
- **Magnitude:** 2434.58 | **LOC:** 2539 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 6.402; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.8%), Guard Balance (formerly Safety Score) (73.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessDict` **(Many-Argument Workhorses)** (Impact: 445.1)
    * *Intent:* #------------------------------------------------------------------------------ # Process PDF dictio...
  * `DecryptInit` **(Many-Argument Workhorses)** (Impact: 155.8)
    * *Intent:* #------------------------------------------------------------------------------ # Initialize decrypt...
  * `ReadPDF` **(Many-Argument Workhorses)** (Impact: 134.6)
    * *Intent:* #------------------------------------------------------------------------------ # Extract informatio...
  * `DecodeStream` **(Many-Argument Workhorses)** (Impact: 117.6)
    * *Intent:* #------------------------------------------------------------------------------ # Decode filtered st...
  * `ExtractObject` **(Many-Argument Workhorses)** (Impact: 108.2)
    * *Intent:* #------------------------------------------------------------------------------ # Extract PDF object...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 20 instances
* *Amplified Cascading Flux:* 341 instances
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 1044
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 613`, `structural_boundaries: 498`, `args: 56`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 362`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `io: 4`, `api: 33`, `import: 14`
* *Defense:* `safety: 10`, `doc: 1`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.402
  * `Choke Point (Betweenness):` 0.000174 | `Ripple Effect (Closeness):` 0.059062
  * `Imports (Out-Degree: 1):` Compress::Zlib, Digest::MD5, Digest::SHA, Encode, Exporter, Filter, Image::ExifTool, Image::ExifTool::AES...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/WriteXMP.pl` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.692)
- **Top Global Matches:** file_cluster_3: 7.692, file_cluster_8: 21.126, file_cluster_6: 33.868
- **Magnitude:** 2273.32 | **LOC:** 1665 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.573; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.4%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WriteXMP` **(Many-Argument Workhorses)** (Impact: 587.4)
    * *Intent:* #------------------------------------------------------------------------------ # Write XMP informat...
  * `SetPropertyPath` **(Many-Argument Workhorses)** (Impact: 110.1)
    * *Intent:* #------------------------------------------------------------------------------ # Set PropertyPath f...
  * `CheckXMP` **(Many-Argument Workhorses)** (Impact: 96.6)
    * *Intent:* #------------------------------------------------------------------------------ # Check XMP values f...
  * `WriteGSpherical` **(Compute Cores)** (Impact: 69.2)
    * *Intent:* #------------------------------------------------------------------------------ # Hack to use XMP wr...
  * `ValidateProperty` **(Compute Cores)** (Impact: 54.1)
    * *Intent:* #------------------------------------------------------------------------------ # Validate XMP prope...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 315 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 948
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 721`, `structural_boundaries: 313`, `args: 38`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 318`, `fragile_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 23`, `import: 7`
* *Defense:* `safety: 5`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.573
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Digest::MD5, Image::ExifTool, YYYY, list, strict, vars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Image/ExifTool/Nikon.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.952)
- **Top Global Matches:** file_cluster_8: 8.952, file_cluster_6: 9.464, file_cluster_4: 17.428
- **Magnitude:** 1803.36 | **LOC:** 14280 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 1.143; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (63.3%), Guard Balance (formerly Safety Score) (53.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessNikonEncrypted` **(Many-Argument Workhorses)** (Impact: 90.0)
    * *Intent:* #------------------------------------------------------------------------------ # Read/Write Nikon E...
  * `PrepareNikonOffsets` **(Many-Argument Workhorses)** (Impact: 55.4)
    * *Intent:* #------------------------------------------------------------------------------ # Prepare to process...
  * `InitEncryptedSubdir` **(Compute Cores)** (Impact: 42.5)
    * *Intent:* #------------------------------------------------------------------------------ # Initialize SubDire...
  * `PrescanExif` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* #------------------------------------------------------------------------------ # Pre-scan EXIF dire...
  * `ProcessNikonApp` **(Compute Cores)** (Impact: 39.4)
    * *Intent:* #------------------------------------------------------------------------------ # Extract informatio...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 269 instances
* *Memory Alloc (weighted view):* 206
* *State Mutation (weighted view):* 949
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1096`, `structural_boundaries: 794`, `args: 115`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 411`, `unreferenced_by_name: 2`
* *Architecture:* `api: 36`, `import: 16`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.002145
  * `Imports (Out-Degree: 6):` Image::ExifTool, Image::ExifTool::Exif, Image::ExifTool::GPS, Image::ExifTool::ICC_Profile, Image::ExifTool::NikonCapture, Image::ExifTool::NikonCustom, Image::ExifTool::XMP, SerialNumber...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/XMPStruct.pl` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 13.432)
- **Top Global Matches:** file_cluster_3: 13.432, file_cluster_8: 34.239, file_cluster_1: 36.623
- **Magnitude:** 1561.56 | **LOC:** 958 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 3.641; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.9%), Guard Balance (formerly Safety Score) (85.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CheckStruct` **(Many-Argument Workhorses)** (Impact: 167.8)
    * *Intent:* #------------------------------------------------------------------------------ # Recursively valida...
  * `InflateStruct` **(Compute Cores)** (Impact: 154.1)
    * *Intent:* #------------------------------------------------------------------------------ # Inflate structure ...
  * `RestoreStruct` **(Many-Argument Workhorses)** (Impact: 151.2)
    * *Intent:* #------------------------------------------------------------------------------ # Restore XMP struct...
  * `AddNewStruct` **(Many-Argument Workhorses)** (Impact: 105.0)
    * *Intent:* #------------------------------------------------------------------------------ # Add new structure ...
  * `DeleteStruct` **(Many-Argument Workhorses)** (Impact: 103.0)
    * *Intent:* #------------------------------------------------------------------------------ # Delete matching st...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 227 instances
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 683
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 380`, `structural_boundaries: 185`, `args: 29`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 229`, `unreferenced_by_name: 2`
* *Architecture:* `api: 18`, `import: 5`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.641
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.057838
  * `Imports (Out-Degree: 2):` Image::ExifTool, Image::ExifTool::TagLookup, Image::ExifTool::XMP, strict, vars
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/MIE.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.164)
- **Top Global Matches:** file_cluster_3: 6.164, file_cluster_8: 25.765, file_cluster_6: 38.84
- **Magnitude:** 1505.16 | **LOC:** 2584 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 1.394; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.3%), Guard Balance (formerly Safety Score) (64.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WriteMIEGroup` **(Many-Argument Workhorses)** (Impact: 426.1)
    * *Intent:* #------------------------------------------------------------------------------ # Rewrite a MIE dire...
  * `ProcessMIEGroup` **(Many-Argument Workhorses)** (Impact: 171.9)
    * *Intent:* #------------------------------------------------------------------------------ # Process MIE direct...
  * `ProcessMIE` **(Many-Argument Workhorses)** (Impact: 120.1)
    * *Intent:* #------------------------------------------------------------------------------ # Read/write a MIE f...
  * `ReadMIEValue` **(Many-Argument Workhorses)** (Impact: 44.0)
    * *Intent:* #------------------------------------------------------------------------------ # ReadValue() with a...
  * `UpdateMieMap` **(Compute Cores)** (Impact: 23.1)
    * *Intent:* #------------------------------------------------------------------------------ # Add user-defined M...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 203 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 625
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 644`, `structural_boundaries: 224`, `args: 21`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 219`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 14`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.394
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.003893
  * `Imports (Out-Degree: 4):` Compress::Zlib, Image::ExifTool, Image::ExifTool::Exif, Image::ExifTool::GPS, strict, units, vars
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/FlashPix.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.627)
- **Top Global Matches:** file_cluster_8: 8.627, file_cluster_6: 8.935, file_cluster_4: 16.99
- **Magnitude:** 1490.74 | **LOC:** 2432 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 1.797; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessFPX` **(Many-Argument Workhorses)** (Impact: 212.8)
    * *Intent:* #------------------------------------------------------------------------------ # Extract informatio...
  * `ReadFPXValue` **(Many-Argument Workhorses)** (Impact: 160.0)
    * *Intent:* #------------------------------------------------------------------------------ # Read FlashPix valu...
  * `ProcessProperties` **(Many-Argument Workhorses)** (Impact: 104.2)
    * *Intent:* #------------------------------------------------------------------------------ # Process FlashPix p...
  * `ProcessFPXR` **(Many-Argument Workhorses)** (Impact: 84.2)
    * *Intent:* #------------------------------------------------------------------------------ # Extract informatio...
  * `ProcessDocumentTable` **(Compute Cores)** (Impact: 59.8)
    * *Intent:* #------------------------------------------------------------------------------ # Process Microsoft ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 203 instances
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 617
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 336`, `args: 51`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 211`, `dead_code: 2`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 37`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.797
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.00286
  * `Imports (Out-Degree: 6):` Image::ExifTool, Image::ExifTool::ASF, Image::ExifTool::Exif, Image::ExifTool::Microsoft, strict, vars
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/HtmlDump.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.205)
- **Top Global Matches:** file_cluster_3: 6.205, file_cluster_8: 24.916, file_cluster_6: 37.922
- **Magnitude:** 1412.46 | **LOC:** 934 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.598; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Print` **(Many-Argument Workhorses)** (Impact: 219.5)
    * *Intent:* #------------------------------------------------------------------------------ # Print dump informa...
  * `DumpTable` **(Many-Argument Workhorses)** (Impact: 216.6)
    * *Intent:* #------------------------------------------------------------------------------ # Dump a block of da...
  * `FinishTiffDump` **(Many-Argument Workhorses)** (Impact: 95.7)
    * *Intent:* #------------------------------------------------------------------------------ # Finish dumping of ...
  * `Open` **(Many-Argument Workhorses)** (Impact: 50.5)
    * *Intent:* #------------------------------------------------------------------------------ # Open or close a sp...
  * `high` **(Compute Cores)** (Impact: 46.3)
    * *Intent:* // highlight/unhighlight text
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 222 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 681
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 186`, `args: 20`, `func_start: 14`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 237`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 7`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.598
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000953
  * `Imports (Out-Degree: 1):` Image::ExifTool, Image::ExifTool::HTML, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/Sony.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.026)
- **Top Global Matches:** file_cluster_6: 9.026, file_cluster_8: 9.084, file_cluster_4: 16.898
- **Magnitude:** 1412.12 | **LOC:** 11929 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **9**; blast radius 9.114; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (61.3%), Guard Balance (formerly Safety Score) (53.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessSR2` **(Many-Argument Workhorses)** (Impact: 107.1)
    * *Intent:* #------------------------------------------------------------------------------ # Read/Write SR2 IFD...
  * `ProcessMoreInfo` **(Many-Argument Workhorses)** (Impact: 61.7)
    * *Intent:* #------------------------------------------------------------------------------ # Read/Write MoreInf...
  * `ProcessSRF` **(Many-Argument Workhorses)** (Impact: 45.2)
    * *Intent:* #------------------------------------------------------------------------------ # Process SRF maker ...
  * `FinishARW` **(Many-Argument Workhorses)** (Impact: 39.0)
    * *Intent:* #------------------------------------------------------------------------------ # Finish writing ARW...
  * `ProcessSonyPIC` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* #------------------------------------------------------------------------------ # Process "SONY PIC\...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 233 instances
* *Memory Alloc (weighted view):* 127
* *State Mutation (weighted view):* 729
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1082`, `structural_boundaries: 571`, `args: 82`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 263`, `fragile_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 34`, `import: 16`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.114
  * `Choke Point (Betweenness):` 0.000262 | `Ripple Effect (Closeness):` 0.065054
  * `Imports (Out-Degree: 5):` Image::ExifTool, Image::ExifTool::Exif, Image::ExifTool::GPS, Image::ExifTool::Minolta, Image::ExifTool::MinoltaRaw, flash, strict, the...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/TagInfoXML.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.673)
- **Top Global Matches:** file_cluster_3: 15.673, file_cluster_1: 33.683, file_cluster_8: 36.895
- **Magnitude:** 1382.76 | **LOC:** 853 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.671; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BuildLangModules` **(Many-Argument Workhorses)** (Impact: 603.3)
    * *Intent:* #------------------------------------------------------------------------------ # Generate Lang modu...
  * `Write` **(Many-Argument Workhorses)** (Impact: 235.6)
    * *Intent:* #------------------------------------------------------------------------------ # Utility to print t...
  * `WriteLangModule` **(Many-Argument Workhorses)** (Impact: 62.5)
    * *Intent:* #------------------------------------------------------------------------------ # Write Lang module ...
  * `NumbersFirst` **(Compute Cores)** (Impact: 20.7)
    * *Intent:* #------------------------------------------------------------------------------ # sort numbers first...
  * `LoadLangModules` **(Defensive Guards)** (Impact: 16.3)
    * *Intent:* #------------------------------------------------------------------------------ # load all lang modu...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Cascading Flux:* 138 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 418
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 146`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 142`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 11`, `import: 13`
* *Defense:* `safety: 4`, `doc: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001907
  * `Imports (Out-Degree: 2):` Exporter, Image::ExifTool, Image::ExifTool::Lang, Image::ExifTool::XMP, strict, vars
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/Canon.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.457)
- **Top Global Matches:** file_cluster_6: 6.457, file_cluster_4: 11.033, file_cluster_8: 15.039
- **Magnitude:** 1331.5 | **LOC:** 10924 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **7**; blast radius 15.488; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (53.7%), Guard Balance (formerly Safety Score) (53.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PrintLensID` **(Many-Argument Workhorses)** (Impact: 211.9)
    * *Intent:* #------------------------------------------------------------------------------ # Attempt to identif...
  * `ProcessSerialData` **(Many-Argument Workhorses)** (Impact: 56.1)
    * *Intent:* #------------------------------------------------------------------------------ # Process a serial s...
  * `ReadODD` **(Compute Cores)** (Impact: 35.9)
    * *Intent:* #------------------------------------------------------------------------------ # Read original deci...
  * `ProcessFilters` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* #------------------------------------------------------------------------------ # Process a creative...
  * `ValidateAFInfo` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* #------------------------------------------------------------------------------ # Validate CanonAFIn...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 188 instances
* *Memory Alloc (weighted view):* 182
* *State Mutation (weighted view):* 627
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 826`, `structural_boundaries: 483`, `args: 54`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 251`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 24`, `import: 8`
* *Defense:* `safety: 4`, `doc: 1`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.488
  * `Choke Point (Betweenness):` 0.000199 | `Ripple Effect (Closeness):` 0.066693
  * `Imports (Out-Degree: 2):` CameraISO, Image::ExifTool, Image::ExifTool::Exif, a, sharpening, strict, vars
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/Plot.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.957)
- **Top Global Matches:** file_cluster_3: 7.957, file_cluster_8: 21.27, file_cluster_6: 33.987
- **Magnitude:** 1235.9 | **LOC:** 734 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.671; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.8%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Draw` **(Many-Argument Workhorses)** (Impact: 343.4)
    * *Intent:* #------------------------------------------------------------------------------ # Draw SVG plot # In...
  * `AddPoints` **(Many-Argument Workhorses)** (Impact: 148.4)
    * *Intent:* #------------------------------------------------------------------------------ # Add points to SVG ...
  * `Settings` **(Compute Cores)** (Impact: 43.7)
    * *Intent:* #------------------------------------------------------------------------------ # Set plot settings ...
  * `GetGridSpacing` **(Compute Cores)** (Impact: 26.8)
    * *Intent:* #------------------------------------------------------------------------------ # Calculate a nice r...
  * `new` **(Type Conversions)** (Impact: 9.1)
    * *Intent:* #------------------------------------------------------------------------------ # Create new plot ob...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 212 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 643
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 108`, `args: 11`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 219`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001907
  * `Imports (Out-Degree: 0):` strict, vars
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Image/ExifTool/PNG.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 12.094)
- **Top Global Matches:** file_cluster_3: 12.094, file_cluster_8: 12.588, file_cluster_6: 25.141
- **Magnitude:** 1156.8 | **LOC:** 1734 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.061; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.6%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FoundPNG` **(Many-Argument Workhorses)** (Impact: 237.1)
    * *Intent:* #------------------------------------------------------------------------------ # Found a PNG tag --...
  * `ProcessPNG` **(Many-Argument Workhorses)** (Impact: 207.8)
    * *Intent:* #------------------------------------------------------------------------------ # Extract meta infor...
  * `ProcessProfile` **(Many-Argument Workhorses)** (Impact: 72.3)
    * *Intent:* #------------------------------------------------------------------------------ # Process encoded PN...
  * `InversePNGDate` **(Compute Cores)** (Impact: 41.0)
    * *Intent:* #------------------------------------------------------------------------------ # Convert EXIF date/...
  * `ConvertPNGDate` **(Compute Cores)** (Impact: 39.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 145 instances
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 217`, `args: 35`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 154`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 25`, `import: 11`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.061
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.000953
  * `Imports (Out-Degree: 3):` Compress::Zlib, Image::ExifTool, Image::ExifTool::Samsung, Image::ExifTool::XMP, YYYY, restriction, strict, vars
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `html/TagNames/PICT.html` (HTML) | Magnitude: 0.03 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 371, design_snake_case: 371, decorators: 223, structural_boundaries: 7
- `html/geolocation.html` (HTML) | Magnitude: 0.42 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 168, io: 126, core_var_decl: 125, design_snake_case: 125
- `html/TagNames/PhotoCD.html` (HTML) | Magnitude: 0.02 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 247, core_var_decl: 81, design_snake_case: 81, decorators: 80
- `t/PLUS.t` (PERL) | Magnitude: 24.68 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 12, branch: 7, debug_prints: 5
- `html/filename.html` (HTML) | Magnitude: 0.31 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 124, core_var_decl: 50, design_snake_case: 50, io: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `lib/Image/ExifTool/JPEG.pm` (PERL) | Magnitude: 56.66 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 701, core_var_decl: 420, design_pascal_case: 350, regex_execution: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/APE.t` (PERL) | Magnitude: 24.52 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, debug_prints: 5, branch: 3
- `t/FLAC.t` (PERL) | Magnitude: 24.52 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, debug_prints: 5, branch: 3
- `t/Flash.t` (PERL) | Magnitude: 24.52 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, debug_prints: 5, branch: 3
- `t/JVC.t` (PERL) | Magnitude: 22.52 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, debug_prints: 5, branch: 3
- `t/Unknown.t` (PERL) | Magnitude: 24.5 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, debug_prints: 5, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `html/mistakes.html` (HTML) | Magnitude: 0.14 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 40, structural_boundaries: 32, core_var_decl: 24, design_snake_case: 23
- `html/commentary.html` (HTML) | Magnitude: 0.28 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 109, structural_boundaries: 73, io: 61, core_var_decl: 49
- `t/LNK.t` (PERL) | Magnitude: 24.52 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, debug_prints: 5, branch: 4
- `t/PhaseOne.t` (PERL) | Magnitude: 24.54 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, debug_prints: 5, branch: 3
- `t/FotoStation.t` (PERL) | Magnitude: 24.56 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, debug_prints: 5, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `lib/Image/ExifTool/Sony.pm` (PERL) | Magnitude: 1412.12 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9852, core_var_decl: 3889, design_pascal_case: 3446, branch: 1082
- `exiftool` (PERL) | Magnitude: 5680.7 | Delta: **0.174** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3998, branch: 3051, structural_boundaries: 1103, state_mutation: 1053

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `exiftool` -> Churn: **100.0%** | Cog Load: 97.5536% | Debt: 9.8274%
- `lib/Image/ExifTool.pm` -> Churn: **100.0%** | Cog Load: 95.8544% | Debt: 15.4024%
- `windows_exiftool` -> Churn: **100.0%** | Cog Load: 98.1448% | Debt: 9.7996%
- `lib/Image/ExifTool/BuildTagLookup.pm` -> Churn: **75.87%** | Cog Load: 95.7157% | Debt: 8.4782%
- `lib/Image/ExifTool/QuickTimeStream.pl` -> Churn: **75.87%** | Cog Load: 81.1531% | Debt: 16.9657%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/Image/ExifTool.pod` -> **exiftool** (100.0% isolated ownership) | Magnitude: 32502.48
- `lib/Image/ExifTool.pm` -> **exiftool** (100.0% isolated ownership) | Magnitude: 10380.7
- `lib/Image/ExifTool/Writer.pl` -> **exiftool** (100.0% isolated ownership) | Magnitude: 9946.7
- `exiftool` -> **exiftool** (100.0% isolated ownership) | Magnitude: 5680.7
- `windows_exiftool` -> **exiftool** (100.0% isolated ownership) | Magnitude: 5574.52

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/Image/ExifTool/Writer.pl` -> **Severity: 0.31** (Bridge: 0.0031 * Flux: 100.0%)
- `lib/Image/ExifTool/Exif.pm` -> **Severity: 0.258** (Bridge: 0.0026 * Flux: 99.8681%)
- `lib/Image/ExifTool/XMP.pm` -> **Severity: 0.166** (Bridge: 0.0017 * Flux: 99.9934%)
- `lib/Image/ExifTool/MacOS.pm` -> **Severity: 0.051** (Bridge: 0.0005 * Flux: 100.0%)
- `lib/Image/ExifTool/ID3.pm` -> **Severity: 0.047** (Bridge: 0.0005 * Flux: 99.9985%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/Image/ExifTool/Writer.pl` -> **Severity: 6.666** (Embedded: 0.0833 * Error Risk: 80.0034%)
- `lib/File/RandomAccess.pm` -> **Severity: 5.683** (Embedded: 0.0732 * Error Risk: 77.679%)
- `lib/Image/ExifTool/XMP.pm` -> **Severity: 5.493** (Embedded: 0.0854 * Error Risk: 64.3297%)
- `lib/Image/ExifTool/Exif.pm` -> **Severity: 5.041** (Embedded: 0.0827 * Error Risk: 60.9319%)
- `lib/Image/ExifTool/XMPStruct.pl` -> **Severity: 4.952** (Embedded: 0.0578 * Error Risk: 85.6256%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/Image/ExifTool/Exif.pm` -> **Severity: 7323.5** (Blast Radius: 73.235 * Doc Risk: 100.0%)
- `lib/Image/ExifTool/Writer.pl` -> **Severity: 4400.9** (Blast Radius: 44.009 * Doc Risk: 100.0%)
- `lib/Image/ExifTool/XMP.pm` -> **Severity: 3286.2** (Blast Radius: 32.862 * Doc Risk: 100.0%)
- `lib/File/RandomAccess.pm` -> **Severity: 1918.4** (Blast Radius: 19.184 * Doc Risk: 100.0%)
- `lib/Image/ExifTool/GPS.pm` -> **Severity: 1844.3** (Blast Radius: 18.443 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1924 literal sites + 1 sites through wrappers = 1925
- **`panics_and_aborts`:** 65 literal sites + 4 sites through wrappers = 69

- `SigInt` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `exiftool`
- `SigInt` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `windows_exiftool`
- `notOK` (function, debug_prints, primitive): 1 call sites in 1 files -- `t/TestLib.pm`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 10521 call pairs -- scoped 10.6%, unique 0.0%, ambiguous 14.7%, external 74.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 10507 | 10.6% | 0.0% | 14.7% | 74.8% |
| html | 14 | 21.4% | 0.0% | 0.0% | 78.6% |

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
