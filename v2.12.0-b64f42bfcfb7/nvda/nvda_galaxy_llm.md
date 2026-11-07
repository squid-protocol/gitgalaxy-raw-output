# ARCHITECTURAL_BRIEF: nvda
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nvaccess/nvda.git` |
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
- **Scope:** 914 analyzed artifact(s), 160206 LOC.
- **Load-bearing artifact:** `source/controlTypes/__init__.py` -- 116 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `source/core.py` -- pulls in 74 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `source/speech/speech.py` at magnitude 4849.4 (structural weight, not risk).
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
| Total Artifacts | 1364 |
| Analyzed Artifacts (Scanned) | 914 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 450 |
| Total LOC | 160206 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 67.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5387 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0235 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 31.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3359 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 93 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 691 | 141456 | 75.6% |
| CPP | 107 | 16209 | 11.7% |
| MARKDOWN | 66 | 0 | 7.2% |
| YAML | 15 | 1703 | 1.6% |
| POWERSHELL | 14 | 362 | 1.5% |
| BATCH | 7 | 61 | 0.8% |
| PLAINTEXT | 5 | 0 | 0.5% |
| MAKEFILE | 4 | 117 | 0.4% |
| XML | 2 | 0 | 0.2% |
| CSS | 2 | 208 | 0.2% |
| HTML | 1 | 90 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 913 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 21%, Data / Markup / Trivial 20%, Declarative / Non-Code 12%, Parameter Forwarders Files 11%, Encapsulated Accessors Files 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 843 | 92.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 71 | 7.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 450*

**Composition by Extension & Reason:**
- `.dic`: 129x Excluded (Unsupported Extension: '.dic')
- `.po`: 64x Excluded (Unsupported Extension: '.po')
- `.xliff`: 59x Excluded (Unsupported Extension: '.xliff')
- `no_extension`: 28x Unsupported Format (.undeterminable), 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Lexical Monotony: High structural repetition detected in 5023 LOC), 2x Excluded (Lexical Monotony: High structural repetition detected in 5111 LOC)
- `.ini`: 24x Excluded (Unsupported Extension: '.ini')
- `.wav`: 16x Excluded (Explicitly Denied Extension: '.wav')
- `.ttf`: 13x Excluded (Explicitly Denied Extension: '.ttf')
- `.robot`: 8x Excluded (Unsupported Extension: '.robot')
- `.pot`: 7x Excluded (Unsupported Extension: '.pot')
- `.acf`: 5x Excluded (Unsupported Extension: '.acf')
- `.idl`: 5x Excluded (Unsupported Extension: '.idl')
- `.cs`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.subst`: 3x Excluded (Unsupported Extension: '.subst')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 28.2 | 21.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.4 | 53.3 | 59.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 25.2 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.3 | 11.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 63.6 | 99.6 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.1 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.7 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 58.1 | 72.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1455 | 336 | 5 | `source/gui/settingsDialogs.py` |
| cleanup | 124 | 59 | 0 | `source/_remoteClient/server.py` |
| guards | 10516 | 541 | 32 | `source/NVDAObjects/IAccessible/__init__.py` |
| danger | 3843 | 447 | 12 | `source/NVDAObjects/IAccessible/__init__.py` |
| concurrency | 767 | 164 | 3 | `source/speech/speech.py` |
| connectivity | 9408 | 664 | 27 | `source/globalCommands.py` |
| io | 1086 | 141 | 2 | `source/installer.py` |
| crypto | 12 | 6 | 0 | `source/_remoteClient/server.py` |
| ipc | 106 | 46 | 0 | `source/COMRegistrationFixes/__init__.py` |
| time | 176 | 63 | 0 | `source/gui/settingsDialogs.py` |
| serialization | 4 | 4 | 0 | `ensureuv.ps1` |
| regex | 98 | 51 | 0 | `source/markdownTranslate.py` |
| events | 1121 | 143 | 2 | `tests/unit/test_extensionPoints.py` |
| tests | 1663 | 88 | 0 | `tests/unit/test_config.py` |
| docs | 5179 | 600 | 15 | `source/winBindings/kernel32.py` |
| debt | 527 | 140 | 1 | `tests/unit/test_extensionPoints.py` |
| mutation | 66513 | 739 | 195 | `source/gui/settingsDialogs.py` |
| dead_code | 1944 | 244 | 6 | `tests/unit/test_config.py` |
| credential | 13 | 3 | 0 | `.github/workflows/testAndPublish.yml` |
| threat | 10 | 5 | 0 | `source/brailleDisplayDrivers/ecoBraille.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 32 | 7 | 0 | `tests/system/robot/symbolPronunciationTests.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.75**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `source/installer.py` (Hits: 118)
- `source/addonHandler/__init__.py` (Hits: 63)
- `source/config/__init__.py` (Hits: 45)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`source/controlTypes/__init__.py`) — 116 inbound connections
2. **api.py** (`source/api.py`) — 94 inbound connections
3. **winUser.py** (`source/winUser.py`) — 92 inbound connections
4. **appModuleHandler.py** (`source/appModuleHandler.py`) — 88 inbound connections
5. **braille.py** (`source/braille.py`) — 84 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **core.py** (`source/core.py`) — 74 outbound dependencies
2. **settingsDialogs.py** (`source/gui/settingsDialogs.py`) — 71 outbound dependencies
3. **braille.py** (`source/braille.py`) — 58 outbound dependencies
4. **globalCommands.py** (`source/globalCommands.py`) — 57 outbound dependencies
5. **__init__.py** (`source/NVDAObjects/IAccessible/__init__.py`) — 54 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `MshtmlVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (@ `nvdaHelper/vbufBackends/mshtml/mshtml.cpp`) -> Impact: **946.1** | LOC: 588
- `GeckoVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (@ `nvdaHelper/vbufBackends/gecko_ia2/gecko_ia2.cpp`) -> Impact: **915.6** | LOC: 853
- `getFormatFieldSpeech` **(Many-Argument Workhorses)** (@ `source/speech/speech.py`) -> Impact: **848.0** | LOC: 499
  * *Intent:* # C901 'getFormatFieldSpeech' is too complex # Note: when working on getFormatFieldSpeech, look for opportunities to simplify # and move logic out int...
- `AdobeAcrobatVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (@ `nvdaHelper/vbufBackends/adobeAcrobat/adobeAcrobat.cpp`) -> Impact: **419.9** | LOC: 418
- `getTextInfoSpeech` **(Many-Argument Workhorses)** (@ `source/speech/speech.py`) -> Impact: **397.3** | LOC: 386
  * *Intent:* # C901 'getTextInfoSpeech' is too complex # Note: when working on getTextInfoSpeech, look for opportunities to simplify # and move logic out into smal...
- `_getTextWithFieldsForUIARange` **(Many-Argument Workhorses)** (@ `source/NVDAObjects/UIA/__init__.py`) -> Impact: **282.5** | LOC: 310
  * *Intent:* # C901 '_getTextWithFieldsForUIARange' is too complex # Note: when working on getPropertiesBraille, look for opportunities to simplify # and move logi...
- `getControlFieldSpeech` **(Many-Argument Workhorses)** (@ `source/speech/speech.py`) -> Impact: **262.4** | LOC: 327
  * *Intent:* # C901 'getControlFieldSpeech' is too complex # Note: when working on getControlFieldSpeech, look for opportunities to simplify # and move logic out i...
- `generateXMLAttribsForFormatting` **(Many-Argument Workhorses)** (@ `nvdaHelper/remote/winword.cpp`) -> Impact: **244.0** | LOC: 176
- `winEventProcHook` **(Many-Argument Workhorses)** (@ `nvdaHelper/remote/ia2LiveRegions.cpp`) -> Impact: **185.8** | LOC: 152
- `getPresentationCategory` **(Many-Argument Workhorses)** (@ `source/textInfos/__init__.py`) -> Impact: **185.0** | LOC: 172

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `source` | 101 | 34433.66 | 42.73% | 5.66% |
| `source/gui` | 19 | 9137.14 | 43.54% | 5.92% |
| `source/NVDAObjects/IAccessible` | 21 | 8533.96 | 45.08% | 26.56% |
| `source/appModules` | 79 | 8273.4 | 33.28% | 57.86% |
| `source/NVDAObjects/window` | 10 | 7347.44 | 61.14% | 3.61% |
| `source/speech` | 11 | 6509.5 | 32.15% | 1.22% |
| `nvdaHelper/remote` | 37 | 6240.92 | 31.07% | 26.72% |
| `source/brailleDisplayDrivers` | 22 | 6027.08 | 54.15% | 32.76% |
| `source/NVDAObjects/UIA` | 10 | 5863.84 | 55.08% | 7.18% |
| `tests/unit` | 41 | 5194.14 | 8.73% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `nvdaHelper/local/nvdaControllerInternal.cpp` -> **100.0%** Exposure
- `source/brailleDisplayDrivers/brltty.py` -> **99.9994%** Exposure
- `source/_bridge/components/services/nvwave.py` -> **99.9991%** Exposure
- `source/appModules/mmc.py` -> **99.999%** Exposure
- `source/appModules/shellexperiencehost.py` -> **99.9925%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ci/scripts/setBuildVersionVars.ps1` -> **100.0%** Exposure
- `ci/scripts/setSconsArgs.ps1` -> **100.0%** Exposure
- `ci/scripts/mozillaSyms.py` -> **100.0%** Exposure
- `site_scons/site_tools/doxygen.py` -> **100.0%** Exposure
- `site_scons/site_tools/msrpc.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/unit/test_extensionPoints.py` -> **40** Orphaned Functions | **58** Duplicates
- `tests/unit/test_config.py` -> **77** Orphaned Functions | **0** Duplicates
- `source/appModules/powerpnt.py` -> **57** Orphaned Functions | **2** Duplicates
- `nvdaHelper/vbufBase/storage.cpp` -> **54** Orphaned Functions | **0** Duplicates
- `tests/unit/test_messageDialog.py` -> **53** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5932` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `source/speech/speech.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.558)
- **Top Global Matches:** file_cluster_6: 6.558, file_cluster_4: 11.863, file_cluster_8: 14.297
- **Magnitude:** 4849.4 | **LOC:** 3171 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **43**; blast radius 1.924; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.3%), Complexity Load (formerly Cognitive Load) (84.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 83.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFormatFieldSpeech` **(Many-Argument Workhorses)** (Impact: 848.0)
    * *Intent:* # C901 'getFormatFieldSpeech' is too complex # Note: when working on getFormatFieldSpeech, look for ...
  * `getTextInfoSpeech` **(Many-Argument Workhorses)** (Impact: 397.3)
    * *Intent:* # C901 'getTextInfoSpeech' is too complex # Note: when working on getTextInfoSpeech, look for opport...
  * `getControlFieldSpeech` **(Many-Argument Workhorses)** (Impact: 262.4)
    * *Intent:* # C901 'getControlFieldSpeech' is too complex # Note: when working on getControlFieldSpeech, look fo...
  * `_getSpellingSpeechWithoutCharMode` **(Many-Argument Workhorses)** (Impact: 148.1)
  * `getPropertiesSpeech` **(Many-Argument Workhorses)** (Impact: 143.4)
    * *Intent:* # C901 'getPropertiesSpeech' is too complex # Note: when working on getPropertiesSpeech, look for op...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 699 instances
* *State Mutation (weighted view):* 2150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 939`, `structural_boundaries: 266`, `args: 61`, `func_start: 61`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 752`
* *Architecture:* `api: 48`, `import: 50`
* *Defense:* `safety: 49`, `doc: 32`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.924
  * `Choke Point (Betweenness):` 0.008334 | `Ripple Effect (Closeness):` 0.158721
  * `Imports (Out-Degree: 35):` .commands, .extensions, .languageHandling, .manager, .priorities, .sayAll, .shortcutKeys, .types...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `source/gui/settingsDialogs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.906)
- **Top Global Matches:** file_cluster_12: 7.906, file_cluster_16: 8.767, file_cluster_4: 8.892
- **Magnitude:** 4257.86 | **LOC:** 6712 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **71**; blast radius 2.06; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.0%)
- **Documentation Coverage:** 83.908% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeSettings` **(Many-Argument Workhorses)** (Impact: 94.4)
  * `makeSettings` **(Many-Argument Workhorses)** (Impact: 49.7)
  * `makeSettings` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 38.7)
  * `haveConfigDefaultsBeenRestored` **(Compute Cores)** (Impact: 37.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 529 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 2364
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 560`, `structural_boundaries: 552`, `args: 257`, `func_start: 246`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 1306`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 7`, `api: 206`, `concurrency: 1`, `import: 82`
* *Defense:* `safety: 76`, `doc: 68`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.06
  * `Choke Point (Betweenness):` 0.017507 | `Ripple Effect (Closeness):` 0.156042
  * `Imports (Out-Degree: 51):` .addonStoreGui.controls.messageDialogs, .dpiScalingHelper, .guiHelper, .nvdaControls, _magnifier.config, _magnifier.utils.types, _remoteClient, abc...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `source/globalCommands.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.395)
- **Top Global Matches:** file_cluster_15: 7.395, file_cluster_12: 7.637, file_cluster_16: 8.677
- **Magnitude:** 3747.78 | **LOC:** 5468 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **57**; blast radius 2.48; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (97.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.475% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `script_navigatorObject_current` **(Defensive Guards)** (Impact: 42.3)
  * `script_toggleScreenCurtain` **(Stateful Encapsulated Methods)** (Impact: 35.5)
  * `_reportFormattingHelper` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* # Report all formatting-related changes regardless of user settings # when explicitly requested. if ...
  * `script_reportLinkDestination` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `script_reportDetailsSummary` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* """Report the annotation details summary for the single character under the caret or the object with...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 541 instances
* *State Mutation (weighted view):* 1738
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 741`, `structural_boundaries: 544`, `args: 275`, `func_start: 272`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 656`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 263`, `import: 64`
* *Defense:* `safety: 84`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.48
  * `Choke Point (Betweenness):` 0.022251 | `Ripple Effect (Closeness):` 0.157694
  * `Imports (Out-Degree: 54):` NVDAObjects, NVDAObjects.UIA, _magnifier, _magnifier.commands, _remoteClient, annotation, api, appModuleHandler...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `source/braille.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.928)
- **Top Global Matches:** file_cluster_4: 7.928, file_cluster_12: 9.566, file_cluster_5: 10.167
- **Magnitude:** 3685.34 | **LOC:** 4054 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **84** in-repo importer(s); it depends on **58**; blast radius 8.68; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.8%), Connectivity (formerly Api Exposure) (49.6%)
- **Documentation Coverage:** 62.8472% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_addTextWithFields` **(Stateful Encapsulated Methods)** (Impact: 88.5)
  * `getPropertiesBraille` **(Compute Cores)** (Impact: 87.8)
    * *Intent:* # C901 'getPropertiesBraille' is too complex # Note: when working on getPropertiesBraille, look for ...
  * `getFormatFieldBraille` **(Many-Argument Workhorses)** (Impact: 77.4)
    * *Intent:* """Generates the braille text for the given format field. @param field: The format field to examine....
  * `getControlFieldBraille` **(Many-Argument Workhorses)** (Impact: 64.3)
  * `_getControlFieldForReportStart` **(Many-Argument Workhorses)** (Impact: 59.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 562 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 1801
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 715`, `structural_boundaries: 499`, `args: 172`, `func_start: 171`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 677`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 124`, `concurrency: 3`, `import: 76`
* *Defense:* `safety: 80`, `doc: 98`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.68
  * `Choke Point (Betweenness):` 0.03691 | `Ripple Effect (Closeness):` 0.188523
  * `Imports (Out-Degree: 48):` NVDAObjects, annotation, api, autoSettingsUtils.driverSetting, baseObject, bdDetect, brailleDisplayDrivers, brailleInput...
  * `Imported By (In-Degree: 84):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/UIA/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.451)
- **Top Global Matches:** file_cluster_4: 7.451, file_cluster_12: 9.148, file_cluster_16: 9.915
- **Magnitude:** 2998.32 | **LOC:** 2794 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **39**; blast radius 2.665; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%), Guard Balance (formerly Safety Score) (74.0%)
- **Documentation Coverage:** 90.8% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getTextWithFieldsForUIARange` **(Many-Argument Workhorses)** (Impact: 282.5)
    * *Intent:* # C901 '_getTextWithFieldsForUIARange' is too complex # Note: when working on getPropertiesBraille, ...
  * `findOverlayClasses` **(Many-Argument Workhorses)** (Impact: 166.1)
    * *Intent:* # C901 'findOverlayClasses' is too complex # Note: when working on findOverlayClasses, look for oppo...
  * `_getFormatFieldAtRange` **(Many-Argument Workhorses)** (Impact: 71.8)
  * `_getTextWithFields_text` **(Many-Argument Workhorses)** (Impact: 50.1)
  * `_get_states` **(Defensive Guards)** (Impact: 48.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 442 instances
* *State Mutation (weighted view):* 1408
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 542`, `structural_boundaries: 478`, `args: 147`, `func_start: 147`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 524`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 126`, `import: 50`
* *Defense:* `safety: 167`, `doc: 33`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.665
  * `Choke Point (Betweenness):` 0.011295 | `Ripple Effect (Closeness):` 0.154069
  * `Imports (Out-Degree: 31):` .VisualStudio, .chromium, .excel, .spartanEdge, .sysListView32, .web, .winConsoleUIA, .wordDocument...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/IAccessible/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.638)
- **Top Global Matches:** file_cluster_12: 8.638, file_cluster_4: 8.921, file_cluster_16: 10.102
- **Magnitude:** 2779.28 | **LOC:** 2697 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **59** in-repo importer(s); it depends on **54**; blast radius 4.435; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.6%), Complexity Load (formerly Cognitive Load) (67.0%), Connectivity (formerly Api Exposure) (56.3%)
- **Documentation Coverage:** 94.9807% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findOverlayClasses` **(Many-Argument Workhorses)** (Impact: 141.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 74.8)
    * *Intent:* # C901: 'IAccessible.__init__' is too complex
  * `normalizeIA2TextFormatField` **(Defensive Guards)** (Impact: 45.6)
  * `_isEqual` **(Compute Cores)** (Impact: 42.5)
  * `kwargsFromSuper` **(Many-Argument Workhorses)** (Impact: 32.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 444 instances
* *State Mutation (weighted view):* 1380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 547`, `structural_boundaries: 623`, `args: 151`, `func_start: 151`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 492`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `io: 2`, `api: 128`, `import: 67`
* *Defense:* `safety: 257`, `doc: 24`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.435
  * `Choke Point (Betweenness):` 0.016653 | `Ripple Effect (Closeness):` 0.15487
  * `Imports (Out-Degree: 39):` .MSHTML, .adobeAcrobat, .chromium, .mozilla, .msOffice, .mscandui, .webKit, .winConsole...
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/window/excel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.554)
- **Top Global Matches:** file_cluster_12: 6.554, file_cluster_16: 8.629, file_cluster_15: 9.056
- **Magnitude:** 2325.76 | **LOC:** 2645 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **50**; blast radius 0.871; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%)
- **Documentation Coverage:** 94.1896% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getFormatFieldAndOffsets` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `setAsHeaderCell` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `populateHeaderCellTrackerFromNames` **(Defensive Guards)** (Impact: 36.0)
  * `iterate` **(Compute Cores)** (Impact: 34.2)
    * *Intent:* """ returns a generator that emits L{QuickNavItem} objects for this collection. @param position: an ...
  * `forgetHeaderCell` **(Compute Cores)** (Impact: 25.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 299 instances
* *State Mutation (weighted view):* 1117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 552`, `args: 206`, `func_start: 200`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 519`, `duplicate_logic: 8`
* *Architecture:* `api: 165`, `import: 54`
* *Defense:* `safety: 77`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.871
  * `Choke Point (Betweenness):` 0.002799 | `Ripple Effect (Closeness):` 0.130262
  * `Imports (Out-Degree: 36):` ..NVDAObjectTextInfo, .Window, ._msOffice, ._msOfficeChart, .excelCellBorder, NVDAHelper, NVDAHelper.localLib, NVDAState...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `nvdaHelper/vbufBackends/mshtml/mshtml.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.66)
- **Top Global Matches:** file_cluster_8: 7.66, file_cluster_6: 10.736, file_cluster_4: 19.085
- **Magnitude:** 2155.14 | **LOC:** 1425 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.436; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MshtmlVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (Impact: 946.1)
  * `fillVBuf_helper_collectAndUpdateTableInfo` **(Many-Argument Workhorses)** (Impact: 108.9)
  * `getIAccessibleInfo` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `LocateHTMLElementInDocument` **(Compute Cores)** (Impact: 55.1)
  * `getAttributesFromHTMLDOMNode` **(Many-Argument Workhorses)** (Impact: 38.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 238 instances
* *State Mutation (weighted view):* 721
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 106`, `args: 290`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 245`, `unreferenced_by_name: 8`
* *Architecture:* `import: 16`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.436
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.001094
  * `Imports (Out-Degree: 9):` algorithm, atlcomcli.h, log.h, map, mshtml.h, node.h, oleacc.h, oleidl.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/window/winword.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.186)
- **Top Global Matches:** file_cluster_4: 6.186, file_cluster_16: 8.2, file_cluster_15: 8.47
- **Magnitude:** 2145.78 | **LOC:** 2230 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **39**; blast radius 0.66; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%)
- **Documentation Coverage:** 94.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_normalizeControlField` **(Many-Argument Workhorses)** (Impact: 55.4)
  * `_normalizeFormatField` **(Many-Argument Workhorses)** (Impact: 54.7)
  * `move` **(Many-Argument Workhorses)** (Impact: 53.6)
  * `getTextWithFields` **(Defensive Guards)** (Impact: 42.8)
    * *Intent:* # C901 'getTextWithFields' is too complex # Note: when working on getTextWithFields, look for opport...
  * `_iterHeadings` **(Stateful Encapsulated Methods)** (Impact: 40.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 302 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 1160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 354`, `args: 133`, `func_start: 108`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 556`, `duplicate_logic: 2`
* *Architecture:* `api: 120`, `import: 41`
* *Defense:* `safety: 36`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.66
  * `Choke Point (Betweenness):` 0.001571 | `Ripple Effect (Closeness):` 0.128885
  * `Imports (Out-Degree: 32):` ..behaviors, .Window, ._msOffice, ._msOfficeChart, NVDAHelper, XMLFormatting, braille, browseMode...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `source/browseMode.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.293)
- **Top Global Matches:** file_cluster_4: 6.293, file_cluster_12: 8.44, file_cluster_16: 9.417
- **Magnitude:** 2011.62 | **LOC:** 2729 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **45**; blast radius 1.375; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.5%), Guard Balance (formerly Safety Score) (71.5%)
- **Documentation Coverage:** 76.5957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_iterTextStyle` **(Many-Argument Workhorses)** (Impact: 71.9)
  * `event_gainFocus` **(Many-Argument Workhorses)** (Impact: 70.8)
  * `shouldPassThrough` **(Many-Argument Workhorses)** (Impact: 55.5)
    * *Intent:* """Determine whether pass through mode should be enabled (focus mode) or disabled (browse mode) for ...
  * `_expandStyle` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `_set_selection` **(Stateful Encapsulated Methods)** (Impact: 34.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 282 instances
* *State Mutation (weighted view):* 911
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 317`, `args: 117`, `func_start: 110`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 347`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 79`, `import: 50`
* *Defense:* `safety: 57`, `doc: 38`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.007087 | `Ripple Effect (Closeness):` 0.149849
  * `Imports (Out-Degree: 34):` NVDAObjects, NVDAObjects.UIA.wordDocument, NVDAObjects.window.winword, abc, api, appModules.kindle, aria, braille...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `source/appModules/powerpnt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.629)
- **Top Global Matches:** file_cluster_4: 7.629, file_cluster_12: 7.763, file_cluster_16: 9.112
- **Magnitude:** 1663.32 | **LOC:** 1744 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 0.384; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (88.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.1%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getShapeText` **(Many-Argument Workhorses)** (Impact: 46.4)
  * `_getFormatFieldAndOffsets` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `_get_selection` **(Defensive Guards)** (Impact: 40.1)
    * *Intent:* """Fetches an NVDAObject representing the current presentation's selected slide, shape or text frame...
  * `_getShapeLocationText` **(Many-Argument Workhorses)** (Impact: 36.3)
  * `_get__overlapInfo` **(Stateful Encapsulated Methods)** (Impact: 30.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 272 instances
* *State Mutation (weighted view):* 960
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 345`, `args: 105`, `func_start: 105`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 416`, `duplicate_logic: 2`, `unreferenced_by_name: 57`
* *Architecture:* `api: 47`, `import: 39`
* *Defense:* `safety: 60`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.384
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` NVDAObjects, NVDAObjects.IAccessible, NVDAObjects.behaviors, NVDAObjects.window, NVDAObjects.window._msOfficeChart, api, appModuleHandler, braille...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nvdaHelper/vbufBackends/gecko_ia2/gecko_ia2.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.188)
- **Top Global Matches:** file_cluster_4: 5.188, file_cluster_15: 10.176, file_cluster_12: 10.462
- **Magnitude:** 1632.34 | **LOC:** 1550 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.384; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GeckoVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (Impact: 915.6)
  * `GeckoVBufBackend_t::renderThread_winEventProcHook` **(Many-Argument Workhorses)** (Impact: 123.1)
  * `fillTableHeaders` **(Many-Argument Workhorses)** (Impact: 26.2)
  * `GeckoVBufBackend_t::fillVBufAriaDetails` **(Many-Argument Workhorses)** (Impact: 22.0)
  * `GeckoVBufBackend_t::getSelectedItem` **(Type Conversions)** (Impact: 15.9)
    * *Intent:* /** * Get the selected item or the first item if no item is selected. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 420`, `structural_boundaries: 123`, `args: 154`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 115`, `fragile_debt: 2`, `unreferenced_by_name: 17`
* *Architecture:* `api: 1`, `import: 20`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.384
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` atlcomcli.h, ia2utils.h, log.h, functional, gecko_ia2.h, ia2.h, map, memory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nvdaHelper/vbufBase/storage.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.255)
- **Top Global Matches:** file_cluster_4: 5.255, file_cluster_6: 9.503, file_cluster_15: 11.269
- **Magnitude:** 1441.3 | **LOC:** 1247 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 4.134; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (91.2%), Complexity Load (formerly Cognitive Load) (90.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.3871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VBufStorage_buffer_t::getLineOffsets` **(Many-Argument Workhorses)** (Impact: 129.6)
  * `VBufStorage_buffer_t::findNodeByAttributes` **(Many-Argument Workhorses)** (Impact: 102.5)
  * `VBufStorage_fieldNode_t::nextNodeInTree` **(Many-Argument Workhorses)** (Impact: 59.4)
    * *Intent:* //field node implementation
  * `VBufStorage_buffer_t::insertNode` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `VBufStorage_buffer_t::unlinkFieldNode` **(Compute Cores)** (Impact: 48.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 198 instances
* *State Mutation (weighted view):* 627
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 127`, `args: 215`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 231`, `unreferenced_by_name: 54`
* *Architecture:* `import: 16`
* *Defense:* `safety: 5`, `doc: 4`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.134
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.009089
  * `Imports (Out-Degree: 4):` algorithm, log.h, xml.h, fstream, iostream, iterator, list, map...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/IAccessible/MSHTML.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.289)
- **Top Global Matches:** file_cluster_12: 7.289, file_cluster_7: 9.008, file_cluster_5: 9.08
- **Magnitude:** 1365.88 | **LOC:** 1273 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **27**; blast radius 0.557; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 97.2414% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 44.7)
  * `_get_states` **(Compute Cores)** (Impact: 32.4)
  * `findOverlayClasses` **(Defensive Guards)** (Impact: 27.6)
  * `kwargsFromSuper` **(Defensive Guards)** (Impact: 24.4)
  * `locateHTMLElementByID` **(Defensive Guards)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 210 instances
* *State Mutation (weighted view):* 666
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 328`, `args: 79`, `func_start: 79`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 246`
* *Architecture:* `api: 78`, `import: 28`
* *Defense:* `safety: 100`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.557
  * `Choke Point (Betweenness):` 0.001001 | `Ripple Effect (Closeness):` 0.120757
  * `Imports (Out-Degree: 23):` ..InvalidNVDAObject, ..behaviors, ..window, .IAccessible, IAccessibleHandler, NVDAObjects.UIA, UIAHandler, api...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `nvdaHelper/remote/winword.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.261)
- **Top Global Matches:** file_cluster_8: 10.261, file_cluster_3: 14.004, file_cluster_6: 22.718
- **Magnitude:** 1304.86 | **LOC:** 1463 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.437; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.5%), Complexity Load (formerly Cognitive Load) (53.2%)
- **Documentation Coverage:** 96.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateXMLAttribsForFormatting` **(Many-Argument Workhorses)** (Impact: 244.0)
  * `winword_getTextInRange_helper` **(Many-Argument Workhorses)** (Impact: 166.6)
  * `generateTableXML` **(Many-Argument Workhorses)** (Impact: 95.2)
  * `generateFormFieldXML` **(Many-Argument Workhorses)** (Impact: 79.0)
  * `generateInlineShapeXML` **(Many-Argument Workhorses)** (Impact: 49.0)
    * *Intent:* /** * Generates an opening tag for the first inline shape in this range if one exists. * If the func...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 444`, `structural_boundaries: 127`, `args: 80`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 98`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.437
  * `Choke Point (Betweenness):` 8e-05 | `Ripple Effect (Closeness):` 0.009089
  * `Imports (Out-Degree: 8):` comdef.h, log.h, xml.h, nvdaHelperRemote.h, oleacc.h, optional, Constants.h, Fields.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `source/_synthDrivers32/sapi4.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.41)
- **Top Global Matches:** file_cluster_12: 8.41, file_cluster_16: 8.48, file_cluster_0: 8.799
- **Magnitude:** 1230.88 | **LOC:** 1268 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.384; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.4%), Concurrency Surface (formerly Concurrency) (75.6%)
- **Documentation Coverage:** 68.3453% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_set_voice` **(Stateful Encapsulated Methods)** (Impact: 54.5)
  * `speak` **(Defensive Guards)** (Impact: 39.9)
  * `IAudio_UnClaim` **(Stateful Encapsulated Methods)** (Impact: 15.4)
    * *Intent:* """Releases the multimedia device asynchronously. Called after the engine completes writing all audi...
  * `_logTrace` **(Stateful Encapsulated Methods)** (Impact: 14.3)
    * *Intent:* """ Decorator that wraps the COM methods, logs the calls, and converts COMError exceptions to silent...
  * `ITTSBufNotifySink_BookMark` **(Compute Cores)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 173 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 216`, `args: 86`, `func_start: 85`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 268`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 17`
* *Architecture:* `api: 56`, `concurrency: 8`, `import: 26`
* *Defense:* `safety: 46`, `doc: 31`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.384
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` ._sapi4, collections, comtypes, config, ctypes, ctypes.wintypes, datetime, enum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/UIAHandler/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.514)
- **Top Global Matches:** file_cluster_8: 6.514, file_cluster_6: 11.368, file_cluster_4: 19.98
- **Magnitude:** 1187.84 | **LOC:** 1536 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **33**; blast radius 7.02; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.2%), Guard Balance (formerly Safety Score) (62.8%)
- **Documentation Coverage:** 70.9677% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_isUIAWindowHelper` **(Many-Argument Workhorses)** (Impact: 105.5)
    * *Intent:* # C901: '_isUIAWindowHelper' is too complex # Note: when working on _isUIAWindowHelper, look for opp...
  * `IUIAutomationEventHandler_HandleAutomationEvent` **(Many-Argument Workhorses)** (Impact: 101.2)
  * `IUIAutomationPropertyChangedEventHandler_HandlePropertyChangedEvent` **(Many-Argument Workhorses)** (Impact: 83.0)
  * `IUIAutomationFocusChangedEventHandler_HandleFocusChangedEvent` **(Many-Argument Workhorses)** (Impact: 54.3)
  * `IUIAutomationNotificationEventHandler_HandleNotificationEvent` **(Many-Argument Workhorses)** (Impact: 49.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 119 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 216`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 164`
* *Architecture:* `api: 28`, `concurrency: 3`, `import: 40`
* *Defense:* `safety: 55`, `doc: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.02
  * `Choke Point (Betweenness):` 0.035789 | `Ripple Effect (Closeness):` 0.153804
  * `Imports (Out-Degree: 21):` .remote, .utils, IAccessibleHandler.internalWinEventHandler, NVDAHelper, NVDAObjects.UIA, NVDAObjects.window, api, appModuleHandler...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/window/edit.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.952)
- **Top Global Matches:** file_cluster_4: 5.952, file_cluster_16: 7.633, file_cluster_12: 8.21
- **Magnitude:** 1169.04 | **LOC:** 1118 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **24**; blast radius 1.071; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (65.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getFormatFieldAtRange` **(Many-Argument Workhorses)** (Impact: 53.2)
    * *Intent:* # C901 '_getFormatFieldAtRange' is too complex # Note: when working on _getFormatFieldAtRange look f...
  * `_getFormatFieldAndOffsets` **(Many-Argument Workhorses)** (Impact: 47.4)
    * *Intent:* # C901 '_getFormatFieldAndOffsets' is too complex # Note: when working on _getFormatFieldAndOffsets ...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 23.9)
  * `_getEmbeddedObjectLabel` **(Defensive Guards)** (Impact: 20.0)
  * `_getTextRange` **(Many-Argument Workhorses)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 197 instances
* *State Mutation (weighted view):* 663
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 155`, `args: 45`, `func_start: 45`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 269`, `fragile_debt: 1`
* *Architecture:* `api: 46`, `import: 25`
* *Defense:* `safety: 35`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.071
  * `Choke Point (Betweenness):` 0.000531 | `Ripple Effect (Closeness):` 0.135394
  * `Imports (Out-Degree: 19):` ..behaviors, .Window, NVDAHelper.localLib, api, colors, comInterfaces.tom, comtypes, config...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.229)
- **Top Global Matches:** file_cluster_5: 7.229, file_cluster_12: 8.616, file_cluster_7: 10.754
- **Magnitude:** 1137.94 | **LOC:** 1658 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **59** in-repo importer(s); it depends on **33**; blast radius 6.646; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Connectivity (formerly Api Exposure) (65.4%)
- **Documentation Coverage:** 29.3233% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Many-Argument Workhorses)** (Impact: 59.0)
  * `_findSimpleNext` **(Stateful Encapsulated Methods)** (Impact: 53.0)
  * `_get_presentationType` **(Compute Cores)** (Impact: 36.1)
  * `event_mouseMove` **(Stateful Encapsulated Methods)** (Impact: 34.2)
  * `findBestAPIClass` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* """ Finds out the highest-level APIClass this object can get to given these kwargs, and updates the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 124 instances
* *State Mutation (weighted view):* 421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 337`, `args: 130`, `func_start: 130`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 173`, `planned_debt: 3`
* *Architecture:* `api: 127`, `import: 36`
* *Defense:* `safety: 37`, `doc: 107`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.646
  * `Choke Point (Betweenness):` 0.013791 | `Ripple Effect (Closeness):` 0.177654
  * `Imports (Out-Degree: 29):` .lockscreen, NVDAObjects.window, annotation, api, appModuleHandler, aria, baseObject, braille...
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/IAccessible/ia2TextMozilla.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.146)
- **Top Global Matches:** file_cluster_6: 8.146, file_cluster_8: 11.241, file_cluster_4: 15.392
- **Magnitude:** 1084.42 | **LOC:** 852 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.44; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%)
- **Documentation Coverage:** 96.9697% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_findUnitEndpoints` **(Many-Argument Workhorses)** (Impact: 118.5)
  * `move` **(Stateful Encapsulated Methods)** (Impact: 67.6)
  * `_getText` **(Many-Argument Workhorses)** (Impact: 56.5)
  * `_iterRecursiveText` **(Many-Argument Workhorses)** (Impact: 45.1)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 44.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 178 instances
* *State Mutation (weighted view):* 546
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 124`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 190`
* *Architecture:* `api: 10`, `import: 17`
* *Defense:* `safety: 42`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.44
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.097982
  * `Imports (Out-Degree: 10):` .IA2TextTextInfo, .IAccessible, NVDAHelper, NVDAObjects, NVDAObjects.IAccessible, api, comInterfaces, compoundDocuments...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `source/config/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.765)
- **Top Global Matches:** file_cluster_12: 6.765, file_cluster_5: 6.877, file_cluster_7: 9.224
- **Magnitude:** 1054.84 | **LOC:** 1434 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **35**; blast radius 0.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.4%)
- **Documentation Coverage:** 41.0256% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__setitem__` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `__getitem__` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `_setSystemConfig` **(Stateful Encapsulated Methods)** (Impact: 25.9)
  * `deleteProfile` **(Defensive Guards)** (Impact: 25.2)
    * *Intent:* """Delete a profile. @param name: The name of the profile to delete. @type name: str @raise LookupEr...
  * `renameProfile` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* """Rename a profile. @param oldName: The current name of the profile. @type oldName: str @param newN...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 513
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 268`, `args: 74`, `func_start: 74`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 211`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `io: 45`, `api: 48`, `import: 42`
* *Defense:* `safety: 67`, `doc: 43`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.879
  * `Choke Point (Betweenness):` 0.006815 | `Ripple Effect (Closeness):` 0.122355
  * `Imports (Out-Degree: 19):` .aggregatedSection, .configSpec, .featureFlag, .profileUpgrader, .registry, NVDAState, addonHandler, addonHandler.packaging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `source/displayModel.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.803)
- **Top Global Matches:** file_cluster_12: 6.803, file_cluster_16: 7.976, file_cluster_4: 8.311
- **Magnitude:** 1052.92 | **LOC:** 791 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **20**; blast radius 1.658; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 97.2973% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processFieldsAndRectsRangeReadingdirection` **(Many-Argument Workhorses)** (Impact: 119.1)
  * `_findCaretOffsetFromLocation` **(Stateful Encapsulated Methods)** (Impact: 32.9)
  * `_getFieldsInRange` **(Stateful Encapsulated Methods)** (Impact: 29.6)
  * `processWindowChunksInLine` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `_getSelectionOffsets` **(Stateful Encapsulated Methods)** (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 175 instances
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 140`, `args: 43`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 201`
* *Architecture:* `api: 33`, `import: 21`
* *Defense:* `safety: 35`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.658
  * `Choke Point (Betweenness):` 0.002472 | `Ripple Effect (Closeness):` 0.159003
  * `Imports (Out-Degree: 15):` NVDAHelper, NVDAObjects.window, XMLFormatting, api, colors, ctypes, locationHelper, logHandler...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `nvdaHelper/remote/gdiHooks.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.547)
- **Top Global Matches:** file_cluster_4: 5.547, file_cluster_15: 8.881, file_cluster_16: 10.059
- **Magnitude:** 1051.96 | **LOC:** 1275 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.437; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.5%), Complexity Load (formerly Cognitive Load) (55.5%)
- **Documentation Coverage:** 92.1569% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ExtTextOutHelper` **(Many-Argument Workhorses)** (Impact: 174.3)
    * *Intent:* */
  * `StretchBlt_helper` **(Many-Argument Workhorses)** (Impact: 95.9)
  * `fake_ScriptStringOut` **(Many-Argument Workhorses)** (Impact: 35.0)
  * `charSetToCodePage` **(Compute Cores)** (Impact: 27.4)
    * *Intent:* //Converts a GDI font charset identifier to a Windows codePage identifier
  * `fake_ScriptStringAnalyse` **(Many-Argument Workhorses)** (Impact: 27.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 178`, `args: 104`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 105`, `unreferenced_by_name: 7`
* *Architecture:* `api: 6`, `import: 16`
* *Defense:* `safety: 1`, `doc: 4`, `sync_locks: 1`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.437
  * `Choke Point (Betweenness):` 8.5e-05 | `Ripple Effect (Closeness):` 0.009633
  * `Imports (Out-Degree: 9):` algorithm, apiHook.h, lock.h, log.h, displayModel.h, dllmain.h, gdiHooks.h, list...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `source/textInfos/offsets.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.776)
- **Top Global Matches:** file_cluster_4: 7.776, file_cluster_12: 8.287, file_cluster_16: 8.763
- **Magnitude:** 1040.18 | **LOC:** 796 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **15**; blast radius 1.603; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 77.6471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `move` **(Stateful Encapsulated Methods)** (Impact: 101.7)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 29.9)
    * *Intent:* """Constructor. Subclasses may extend this to perform implementation specific initialisation, callin...
  * `_get_boundingRects` **(Defensive Guards)** (Impact: 28.9)
    * *Intent:* # C901 '_get_boundingRects' is too complex # Note: when working on _get_boundingRects, look for oppo...
  * `_getUnitOffsets` **(Stateful Encapsulated Methods)** (Impact: 23.5)
    * *Intent:* """Gets the start and end offsets of the unit containing the given offset. :param unit: Any of UNIT_...
  * `_calculateUniscribeOffsets` **(Many-Argument Workhorses)** (Impact: 20.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 149`, `args: 54`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 174`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 15`
* *Defense:* `safety: 16`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.603
  * `Choke Point (Betweenness):` 0.001182 | `Ripple Effect (Closeness):` 0.141542
  * `Imports (Out-Degree: 9):` NVDAHelper, NVDAObjects, NVDAState, abc, config, ctypes, dataclasses, locationHelper...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `source/IAccessibleHandler/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.966)
- **Top Global Matches:** file_cluster_6: 7.966, file_cluster_4: 11.551, file_cluster_8: 16.436
- **Magnitude:** 1035.86 | **LOC:** 1306 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **34**; blast radius 1.37; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.8%), Guard Balance (formerly Safety Score) (68.4%)
- **Documentation Coverage:** 72.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `winEventToNVDAEvent` **(Many-Argument Workhorses)** (Impact: 67.8)
    * *Intent:* # C901 'winEventToNVDAEvent' is too complex # Note: when working on winEventToNVDAEvent, look for op...
  * `processFocusWinEvent` **(Many-Argument Workhorses)** (Impact: 50.4)
    * *Intent:* """checks to see if the focus win event is not the same as the existing focus, then converts the win...
  * `processGenericWinEvent` **(Many-Argument Workhorses)** (Impact: 43.8)
    * *Intent:* """Converts the win event to an NVDA event, Checks to see if this NVDAObject equals the current focu...
  * `processForegroundWinEvent` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* """checks to see if the foreground win event is not the same as the existing focus or any of its par...
  * `pumpAll` **(I/O & Config Routines)** (Impact: 32.2)
    * *Intent:* # C901 'pumpAll' is too complex
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 140 instances
* *State Mutation (weighted view):* 440
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 195`, `args: 37`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 160`, `fragile_debt: 1`
* *Architecture:* `api: 34`, `import: 37`
* *Defense:* `safety: 73`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.37
  * `Choke Point (Betweenness):` 0.00441 | `Ripple Effect (Closeness):` 0.149515
  * `Imports (Out-Degree: 24):` .internalWinEventHandler, .orderedWinEventLimiter, .types, .utils, JABHandler, NVDAObjects.IAccessible, NVDAObjects.IAccessible.mscandui, NVDAObjects.UIA.wordDocument...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/system/libraries/_chromeArgs.py` (PYTHON) | Magnitude: 4.86 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 16, branch: 2, structural_boundaries: 2, doc: 2
- `tests/system/libraries/SystemTestSpy/speechSpyGlobalPlugin.py` (PYTHON) | Magnitude: 393.12 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 385, structural_boundaries: 147, core_var_decl: 72, args: 61
- `tests/unit/__init__.py` (PYTHON) | Magnitude: 21.44 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 24, import: 19, state_mutation: 16, io: 6
- `source/controlTypes/deprecatedAliases.py` (PYTHON) | Magnitude: 217.28 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 199, core_var_decl: 199, design_upper_case: 193, indent_tabs: 19
- `source/brailleViewer/__init__.py` (PYTHON) | Magnitude: 37.7 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 35, structural_boundaries: 23, core_var_decl: 10, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `ci/scripts/setSconsArgs.ps1` (POWERSHELL) | Magnitude: 41.48 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: globals: 15, state_mutation: 10, branch: 4, io: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `nvdaHelper/remote/typedCharacter.cpp` (CPP) | Magnitude: 28.16 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 13, pointers: 7, branch: 6, core_var_decl: 6
- `source/garbageHandler.py` (PYTHON) | Magnitude: 73.88 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 27, structural_boundaries: 15, branch: 10, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `source/_remoteClient/menu.py` (PYTHON) | Magnitude: 64.84 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 130, structural_boundaries: 26, args: 11, func_start: 11
- `source/NVDAObjects/IAccessible/ia2Web.py` (PYTHON) | Magnitude: 411.96 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 298, structural_boundaries: 124, branch: 73, state_mutation: 67
- `source/hwIo/base.py` (PYTHON) | Magnitude: 289.62 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 256, structural_boundaries: 71, branch: 55, state_mutation: 36
- `source/_synthDrivers32/sapi4.py` (PYTHON) | Magnitude: 1230.88 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 914, state_mutation: 268, structural_boundaries: 216, branch: 174
- `source/md2html.py` (PYTHON) | Magnitude: 157.06 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 129, core_var_decl: 50, structural_boundaries: 43, branch: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `source/winBindings/advapi32.py` (PYTHON) | Magnitude: 44.54 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 94, state_mutation: 32, doc: 19, core_var_decl: 18
- `tests/unit/test_l10nUtil.py` (PYTHON) | Magnitude: 66.04 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 98, core_var_decl: 30, design_snake_case: 30, explicit_casts: 24
- `source/_bridge/clients/synthDriverHost32/synthDriver.py` (PYTHON) | Magnitude: 6.34 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 9, structural_boundaries: 8, api: 3, args: 2
- `source/treeInterceptorHandler.py` (PYTHON) | Magnitude: 221.42 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 171, structural_boundaries: 104, api: 42, args: 41
- `tests/unit/test_remote/test_remoteClient.py` (PYTHON) | Magnitude: 173.3 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 210, structural_boundaries: 74, state_mutation: 57, args: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `source/appModules/notepadPlusPlus.py` (PYTHON) | Magnitude: 26.92 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 13, api: 6, branch: 5
- `source/brailleDisplayDrivers/brailliantB.py` (PYTHON) | Magnitude: 265.76 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 303, state_mutation: 64, core_var_decl: 59, branch: 49
- `source/gui/nvdaControls.py` (PYTHON) | Magnitude: 327.52 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 356, structural_boundaries: 98, core_var_decl: 97, design_snake_case: 63
- `tests/unit/test_braille/test_brailleDisplayDrivers.py` (PYTHON) | Magnitude: 114.0 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 132, state_mutation: 36, structural_boundaries: 32, core_var_decl: 28
- `source/jobObject.py` (PYTHON) | Magnitude: 49.44 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 52, structural_boundaries: 17, api: 7, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `nvdaHelper/remote/gdiHooks.h` (CPP) | Magnitude: 3.36 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 38, structural_boundaries: 13, macros: 6, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `source/winBindings/hid.py` (PYTHON) | Magnitude: 64.16 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 87, state_mutation: 57, core_var_decl: 23, doc: 19
- `source/keyLabels.py` (PYTHON) | Magnitude: 9.96 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 80, structural_boundaries: 4, state_mutation: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `source/appModules/powerpnt.py` (PYTHON) | Magnitude: 1663.32 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 1227, state_mutation: 416, core_var_decl: 383, structural_boundaries: 345
- `source/diffHandler.py` (PYTHON) | Magnitude: 140.44 | Delta: **0.168** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 67, structural_boundaries: 38, branch: 28, state_mutation: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `source/gui/inputGestures.py` (PYTHON) | Magnitude: 693.26 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 621, structural_boundaries: 157, state_mutation: 155, core_var_decl: 134
- `nvdaHelper/common/COMUtils.h` (CPP) | Magnitude: 21.32 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 40, structural_boundaries: 14, branch: 6, args: 6
- `source/characterProcessing.py` (PYTHON) | Magnitude: 791.7 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 601, state_mutation: 169, core_var_decl: 157, branch: 139
- `source/winAPI/sessionTracking.py` (PYTHON) | Magnitude: 79.64 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 112, structural_boundaries: 54, state_mutation: 32, core_var_decl: 31
- `source/appModules/shellexperiencehost.py` (PYTHON) | Magnitude: 63.8 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 39, structural_boundaries: 27, branch: 12, api: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `source/appModules/windowsinternal_composableshell_experiences_textinput_inputapp.py` (PYTHON) | Magnitude: 333.9 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 268, branch: 79, structural_boundaries: 61, state_mutation: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `source/globalPluginHandler.py` (PYTHON) | Magnitude: 46.82 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 34, structural_boundaries: 27, import: 9, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `source/utils/urlUtils.py` (PYTHON) | Magnitude: 37.14 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 33, structural_boundaries: 20, branch: 10, core_var_decl: 9
- `source/appModules/loudtalks.py` (PYTHON) | Magnitude: 32.26 | Delta: **0.166** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 17, branch: 6, state_mutation: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `source/gui/settingsDialogs.py` -> Churn: **100.0%** | Cog Load: 75.0298% | Debt: 11.0368%
- `source/globalCommands.py` -> Churn: **80.42%** | Cog Load: 66.1461% | Debt: 7.67%
- `source/mathPres/MathCAT/preferences.py` -> Churn: **71.21%** | Cog Load: 60.76% | Debt: 0.0%
- `source/gui/installerGui.py` -> Churn: **53.21%** | Cog Load: 63.8788% | Debt: 17.3372%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `source/braille.py` -> **Noelia Ruiz Martínez** (100.0% isolated ownership) | Magnitude: 3685.34
- `source/NVDAObjects/window/winword.py` -> **Leonard de Ruijter** (100.0% isolated ownership) | Magnitude: 2145.78
- `nvdaHelper/vbufBackends/gecko_ia2/gecko_ia2.cpp` -> **Bram Duvigneau** (100.0% isolated ownership) | Magnitude: 1632.34
- `source/_synthDrivers32/sapi4.py` -> **Michael Curran** (100.0% isolated ownership) | Magnitude: 1230.88
- `source/NVDAObjects/window/edit.py` -> **Sean Budd** (100.0% isolated ownership) | Magnitude: 1169.04

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `source/braille.py` -> **Severity: 3.691** (Bridge: 0.0369 * Flux: 100.0%)
- `source/UIAHandler/__init__.py` -> **Severity: 3.579** (Bridge: 0.0358 * Flux: 99.9974%)
- `source/gui/__init__.py` -> **Severity: 3.097** (Bridge: 0.031 * Flux: 99.9625%)
- `source/appModuleHandler.py` -> **Severity: 2.429** (Bridge: 0.0243 * Flux: 100.0%)
- `source/inputCore.py` -> **Severity: 2.268** (Bridge: 0.0227 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `source/languageHandler.py` -> **Severity: 15.556** (Embedded: 0.1967 * Error Risk: 79.0918%)
- `source/winKernel.py` -> **Severity: 15.372** (Embedded: 0.2128 * Error Risk: 72.2482%)
- `source/braille.py` -> **Severity: 15.049** (Embedded: 0.1885 * Error Risk: 79.8243%)
- `source/winBindings/kernel32.py` -> **Severity: 15.026** (Embedded: 0.2273 * Error Risk: 66.1141%)
- `source/extensionPoints/__init__.py` -> **Severity: 14.909** (Embedded: 0.2162 * Error Risk: 68.961%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `source/NVDAState.py` -> **Severity: 2460.241** (Blast Radius: 28.796 * Doc Risk: 85.4369%)
- `source/winBindings/advapi32.py` -> **Severity: 1943.0** (Blast Radius: 19.43 * Doc Risk: 100.0%)
- `source/winUser.py` -> **Severity: 994.837** (Blast Radius: 10.983 * Doc Risk: 90.5797%)
- `source/objidl.py` -> **Severity: 866.6** (Blast Radius: 8.666 * Doc Risk: 100.0%)
- `source/winBindings/jobapi2.py` -> **Severity: 695.0** (Blast Radius: 6.95 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 63 literal sites + 44 sites through wrappers = 107
- **`panics_and_aborts`:** 1326 literal sites + 2 sites through wrappers = 1328

- `macro_addHTMLAttributeToMap` (macro, memory_alloc, primitive): 41 call sites in 1 files -- `nvdaHelper/vbufBackends/mshtml/mshtml.cpp`
- `getCompositionString` (function, memory_alloc, primitive): 3 call sites in 1 files -- `nvdaHelper/remote/ime.cpp`
- `IAccessibleFromHTMLNode` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `source/NVDAObjects/IAccessible/MSHTML.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 34525 call pairs -- scoped 35.0%, unique 0.4%, ambiguous 13.5%, external 51.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 31410 | 36.9% | 0.0% | 13.9% | 49.2% |
| cpp | 3094 | 15.4% | 4.2% | 10.2% | 70.1% |
| html | 15 | 13.3% | 0.0% | 0.0% | 86.7% |
| powershell | 6 | 0.0% | 0.0% | 0.0% | 100.0% |

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
