# ARCHITECTURAL_BRIEF: nvda
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nvaccess/nvda.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 904 analyzed artifact(s), 158915 LOC.
- **Load-bearing artifact:** `source/winUser.py` -- 92 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 904 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 460 |
| Total LOC | 158915 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 66.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5333 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0674 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.5396 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 103 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 692 | 141491 | 76.5% |
| CPP | 107 | 16209 | 11.8% |
| MARKDOWN | 56 | 0 | 6.2% |
| POWERSHELL | 14 | 362 | 1.5% |
| PLAINTEXT | 10 | 0 | 1.1% |
| BATCH | 7 | 61 | 0.8% |
| CSHARP | 4 | 164 | 0.4% |
| RUST | 4 | 173 | 0.4% |
| MAKEFILE | 4 | 117 | 0.4% |
| XML | 2 | 0 | 0.2% |
| CSS | 2 | 208 | 0.2% |
| C | 1 | 40 | 0.1% |
| HTML | 1 | 90 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `1.978`
> **Composition Archetype:** `Hub-Coupled App` (z +1.98; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 21%, Data / Markup / Trivial 18%, Declarative / Non-Code 12%, Parameter Forwarders Files 11%, Encapsulated Accessors Files 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 838 | 92.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 66 | 7.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 460*

**Composition by Extension & Reason:**
- `.dic`: 129x Excluded (Unsupported Extension: '.dic')
- `.po`: 64x Excluded (Unsupported Extension: '.po')
- `.xliff`: 59x Excluded (Unsupported Extension: '.xliff')
- `.md`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Lexical Monotony: High structural repetition detected in 5023 LOC), 2x Excluded (Lexical Monotony: High structural repetition detected in 5111 LOC)
- `no_extension`: 28x Unsupported Format (.undeterminable), 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 24x Excluded (Unsupported Extension: '.ini')
- `.wav`: 16x Excluded (Explicitly Denied Extension: '.wav')
- `.ttf`: 13x Excluded (Explicitly Denied Extension: '.ttf')
- `.yml`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.robot`: 8x Excluded (Unsupported Extension: '.robot')
- `.pot`: 7x Excluded (Unsupported Extension: '.pot')
- `.yaml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.acf`: 5x Excluded (Unsupported Extension: '.acf')
- `.idl`: 5x Excluded (Unsupported Extension: '.idl')
- `.subst`: 3x Excluded (Unsupported Extension: '.subst')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 28.5 | 21.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 69.1 | 80.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 25.3 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.6 | 10.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 63.7 | 99.6 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.5 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 58.2 | 71.8 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5232 | 407 | 8 | `nvdaHelper/vbufBase/storage.cpp` |
| cleanup | 124 | 59 | 0 | `source/_remoteClient/server.py` |
| guards | 10532 | 544 | 32 | `source/NVDAObjects/IAccessible/__init__.py` |
| danger | 3856 | 448 | 12 | `source/NVDAObjects/IAccessible/__init__.py` |
| concurrency | 772 | 166 | 3 | `source/speech/speech.py` |
| connectivity | 9387 | 665 | 28 | `source/globalCommands.py` |
| io | 1081 | 138 | 2 | `source/installer.py` |
| crypto | 10 | 6 | 0 | `source/_remoteClient/server.py` |
| ipc | 75 | 20 | 0 | `source/COMRegistrationFixes/__init__.py` |
| time | 178 | 65 | 0 | `source/gui/settingsDialogs.py` |
| serialization | 4 | 4 | 0 | `ensureuv.ps1` |
| regex | 98 | 51 | 0 | `source/markdownTranslate.py` |
| events | 1115 | 140 | 2 | `tests/unit/test_extensionPoints.py` |
| tests | 1663 | 88 | 0 | `tests/unit/test_config.py` |
| docs | 5140 | 590 | 15 | `source/winBindings/kernel32.py` |
| debt | 491 | 135 | 1 | `tests/unit/test_extensionPoints.py` |
| mutation | 66564 | 741 | 195 | `source/gui/settingsDialogs.py` |
| dead_code | 2141 | 314 | 7 | `tests/unit/test_config.py` |
| credential | 3 | 2 | 0 | `tests/unit/test_config.py` |
| threat | 1151 | 322 | 3 | `source/NVDAState.py` |
| ml_ai | 1 | 1 | 0 | `extras/controllerClient/examples/example_rust/examples/example_rust.rs` |
| ui | 35 | 9 | 0 | `tests/system/robot/symbolPronunciationTests.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.7889**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `source/installer.py` (Hits: 118)
- `source/addonHandler/__init__.py` (Hits: 63)
- `source/config/__init__.py` (Hits: 45)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **winUser.py** (`source/winUser.py`) — 92 inbound connections
2. **appModuleHandler.py** (`source/appModuleHandler.py`) — 88 inbound connections
3. **ui.py** (`source/ui.py`) — 72 inbound connections
4. **wx.py** (`source/NVDAObjects/IAccessible/wx.py`) — 69 inbound connections
5. **NVDAState.py** (`source/NVDAState.py`) — 57 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **core.py** (`source/core.py`) — 74 outbound dependencies
2. **settingsDialogs.py** (`source/gui/settingsDialogs.py`) — 71 outbound dependencies
3. **braille.py** (`source/braille.py`) — 59 outbound dependencies
4. **globalCommands.py** (`source/globalCommands.py`) — 57 outbound dependencies
5. **excel.py** (`source/NVDAObjects/window/excel.py`) — 50 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `MshtmlVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (@ `nvdaHelper/vbufBackends/mshtml/mshtml.cpp`) -> Impact: **946.1** | LOC: 588
- `GeckoVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (@ `nvdaHelper/vbufBackends/gecko_ia2/gecko_ia2.cpp`) -> Impact: **915.6** | LOC: 853
- `getFormatFieldSpeech` **(Many-Argument Workhorses)** (@ `source/speech/speech.py`) -> Impact: **848.0** | LOC: 499
  * *Intent:* # C901 'getFormatFieldSpeech' is too complex # Note: when working on getFormatFieldSpeech, look for opportunities to simplify # and move logic out int...
- `AdobeAcrobatVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (@ `nvdaHelper/vbufBackends/adobeAcrobat/adobeAcrobat.cpp`) -> Impact: **425.9** | LOC: 418
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
| `source` | 101 | 34433.66 | 42.73% | 6.35% |
| `source/gui` | 19 | 9134.84 | 43.54% | 9.11% |
| `source/NVDAObjects/IAccessible` | 21 | 8531.96 | 45.08% | 31.81% |
| `source/appModules` | 79 | 8269.4 | 33.28% | 67.54% |
| `source/NVDAObjects/window` | 10 | 7343.44 | 61.14% | 13.72% |
| `source/speech` | 11 | 6509.5 | 32.15% | 1.59% |
| `nvdaHelper/remote` | 37 | 6234.12 | 31.56% | 28.23% |
| `source/brailleDisplayDrivers` | 22 | 6027.08 | 54.15% | 36.87% |
| `source/NVDAObjects/UIA` | 10 | 5835.84 | 55.08% | 41.59% |
| `tests/unit` | 41 | 5194.14 | 8.73% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `source/NVDAObjects/IAccessible/webKit.py` -> **100.0%** Exposure
- `nvdaHelper/local/nvdaControllerInternal.cpp` -> **100.0%** Exposure
- `source/NVDAObjects/window/winConsole.py` -> **99.9999%** Exposure
- `source/brailleDisplayDrivers/brltty.py` -> **99.9997%** Exposure
- `source/appModules/mmc.py` -> **99.9996%** Exposure
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
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5982` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `source/speech/speech.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4849.4 | **LOC:** 3171 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **42**; blast radius 0.58; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (84.2%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 752`, `dead_code: 4`
* *Architecture:* `api: 48`, `import: 50`
* *Defense:* `safety: 49`, `doc: 32`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.58
  * `Choke Point (Betweenness):` 0.000184 | `Ripple Effect (Closeness):` 0.003951
  * `Imports (Out-Degree: 23):` , .commands, .extensions, .priorities, .sayAll, .shortcutKeys, .types, NVDAObjects...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `source/gui/settingsDialogs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4257.86 | **LOC:** 6712 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 26.7%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **71**; blast radius 0.952; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 1306`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 7`, `api: 206`, `concurrency: 1`, `import: 82`
* *Defense:* `safety: 76`, `doc: 68`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.952
  * `Choke Point (Betweenness):` 0.002228 | `Ripple Effect (Closeness):` 0.008729
  * `Imports (Out-Degree: 37):` , .addonStoreGui.controls.messageDialogs, .dpiScalingHelper, _magnifier.config, _magnifier.utils.types, _remoteClient, abc, addonStore.models.channel...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `source/globalCommands.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3747.78 | **LOC:** 5468 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **57**; blast radius 3.992; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (97.0%), Guard Balance (formerly Safety Score) (91.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.7%)
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
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 656`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 263`, `import: 64`
* *Defense:* `safety: 84`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.992
  * `Choke Point (Betweenness):` 0.027145 | `Ripple Effect (Closeness):` 0.122907
  * `Imports (Out-Degree: 33):` NVDAObjects, NVDAObjects.UIA, _magnifier, _magnifier.commands, _remoteClient, annotation, api, appModuleHandler...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `source/braille.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3685.34 | **LOC:** 4054 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **59**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (49.6%)
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
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 677`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 124`, `concurrency: 3`, `import: 76`
* *Defense:* `safety: 80`, `doc: 98`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` NVDAObjects, annotation, api, autoSettingsUtils.driverSetting, baseObject, bdDetect, brailleDisplayDrivers, brailleInput...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/UIA/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2998.32 | **LOC:** 2794 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%)
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
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 524`, `dead_code: 1`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 126`, `import: 50`
* *Defense:* `safety: 167`, `doc: 33`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` , .excel, .wordDocument, NVDAObjects, NVDAObjects.behaviors, NVDAObjects.window, NVDAObjects.window.edit, NVDAState...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/IAccessible/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2779.28 | **LOC:** 2697 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.2%), Complexity Load (formerly Cognitive Load) (67.0%), Connectivity (formerly Api Exposure) (54.0%)
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
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 492`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `io: 2`, `api: 128`, `import: 67`
* *Defense:* `safety: 257`, `doc: 24`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` , .mozilla, .msOffice, .winword, IAccessibleHandler, JABHandler, NVDAHelper, NVDAObjects...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/window/excel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2325.76 | **LOC:** 2645 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **50**; blast radius 0.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Complexity Load (formerly Cognitive Load) (83.8%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 519`, `dead_code: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 165`, `import: 54`
* *Defense:* `safety: 77`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.816
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.001106
  * `Imports (Out-Degree: 22):` , .., ._msOffice, ._msOfficeChart, .excelCellBorder, NVDAHelper, NVDAHelper.localLib, NVDAState...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `nvdaHelper/vbufBackends/mshtml/mshtml.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2164.34 | **LOC:** 1425 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MshtmlVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (Impact: 946.1)
  * `fillVBuf_helper_collectAndUpdateTableInfo` **(Many-Argument Workhorses)** (Impact: 108.9)
  * `LocateHTMLElementInDocument` **(Compute Cores)** (Impact: 56.9)
  * `getIAccessibleInfo` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `getAttributesFromHTMLDOMNode` **(Many-Argument Workhorses)** (Impact: 38.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 727
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 441`, `structural_boundaries: 106`, `args: 290`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 245`, `dead_code: 4`, `unreferenced_by_name: 8`
* *Architecture:* `import: 16`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` algorithm, atlcomcli.h, log.h, map, mshtml.h, node.h, oleacc.h, oleidl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/window/winword.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2145.78 | **LOC:** 2230 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **38**; blast radius 0.823; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Complexity Load (formerly Cognitive Load) (85.5%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.823
  * `Choke Point (Betweenness):` 0.003175 | `Ripple Effect (Closeness):` 0.082163
  * `Imports (Out-Degree: 18):` , ..behaviors, ._msOffice, NVDAHelper, XMLFormatting, braille, browseMode, colors...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `source/browseMode.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2011.62 | **LOC:** 2729 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.5%)
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
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 347`, `dead_code: 4`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 79`, `import: 50`
* *Defense:* `safety: 57`, `doc: 38`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` NVDAObjects, NVDAObjects.UIA.wordDocument, NVDAObjects.window.winword, abc, api, appModules.kindle, aria, braille...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/appModules/powerpnt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1663.32 | **LOC:** 1744 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Debt Markers (formerly Tech Debt) (89.0%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` NVDAObjects, NVDAObjects.IAccessible, NVDAObjects.behaviors, NVDAObjects.window, NVDAObjects.window._msOfficeChart, api, appModuleHandler, braille...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nvdaHelper/vbufBackends/gecko_ia2/gecko_ia2.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1640.04 | **LOC:** 1550 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.4%), Guard Balance (formerly Safety Score) (85.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GeckoVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (Impact: 915.6)
  * `GeckoVBufBackend_t::renderThread_winEventProcHook` **(Many-Argument Workhorses)** (Impact: 128.8)
  * `fillTableHeaders` **(Many-Argument Workhorses)** (Impact: 26.2)
  * `GeckoVBufBackend_t::fillVBufAriaDetails` **(Many-Argument Workhorses)** (Impact: 22.0)
  * `GeckoVBufBackend_t::getRelationElementsOfType` **(Many-Argument Workhorses)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 123`, `args: 154`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 115`, `fragile_debt: 2`, `unreferenced_by_name: 17`
* *Architecture:* `api: 1`, `import: 20`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` atlcomcli.h, ia2utils.h, log.h, functional, gecko_ia2.h, ia2.h, map, memory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nvdaHelper/vbufBase/storage.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1463.7 | **LOC:** 1247 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Debt Markers (formerly Tech Debt) (91.6%), Complexity Load (formerly Cognitive Load) (90.3%)
- **Documentation Coverage:** 98.3871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VBufStorage_buffer_t::getLineOffsets` **(Many-Argument Workhorses)** (Impact: 136.9)
  * `VBufStorage_buffer_t::findNodeByAttributes` **(Many-Argument Workhorses)** (Impact: 102.5)
  * `VBufStorage_fieldNode_t::nextNodeInTree` **(Many-Argument Workhorses)** (Impact: 59.4)
    * *Intent:* //field node implementation
  * `VBufStorage_buffer_t::insertNode` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `VBufStorage_buffer_t::unlinkFieldNode` **(Compute Cores)** (Impact: 48.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 204 instances
* *State Mutation (weighted view):* 639
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 127`, `args: 215`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 231`, `unreferenced_by_name: 54`
* *Architecture:* `import: 16`
* *Defense:* `safety: 5`, `doc: 4`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` algorithm, log.h, xml.h, fstream, iostream, iterator, list, map...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/IAccessible/MSHTML.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1365.88 | **LOC:** 1273 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **27**; blast radius 0.644; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.644
  * `Choke Point (Betweenness):` 0.00016 | `Ripple Effect (Closeness):` 0.003319
  * `Imports (Out-Degree: 7):` , .., ..behaviors, ..window, IAccessibleHandler, NVDAObjects.UIA, UIAHandler, api...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `nvdaHelper/remote/winword.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1313.26 | **LOC:** 1463 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.5%), Complexity Load (formerly Cognitive Load) (53.6%)
- **Documentation Coverage:** 96.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateXMLAttribsForFormatting` **(Many-Argument Workhorses)** (Impact: 244.0)
  * `winword_getTextInRange_helper` **(Many-Argument Workhorses)** (Impact: 170.1)
  * `generateTableXML` **(Many-Argument Workhorses)** (Impact: 95.2)
  * `generateFormFieldXML` **(Many-Argument Workhorses)** (Impact: 79.0)
  * `detectAndGenerateColumnFormatXML` **(Many-Argument Workhorses)** (Impact: 49.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 449`, `structural_boundaries: 127`, `args: 80`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 98`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` comdef.h, log.h, xml.h, nvdaHelperRemote.h, oleacc.h, optional, Constants.h, Fields.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/_synthDrivers32/sapi4.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1230.88 | **LOC:** 1268 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.7%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (77.8%)
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
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 268`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 17`
* *Architecture:* `api: 56`, `concurrency: 8`, `import: 26`
* *Defense:* `safety: 46`, `doc: 31`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ._sapi4, collections, comtypes, config, ctypes, ctypes.wintypes, datetime, enum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/UIAHandler/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1187.84 | **LOC:** 1536 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.2%)
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
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 164`, `dead_code: 2`
* *Architecture:* `api: 28`, `concurrency: 3`, `import: 40`
* *Defense:* `safety: 55`, `doc: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` , IAccessibleHandler.internalWinEventHandler, NVDAHelper, NVDAObjects.UIA, NVDAObjects.window, api, appModuleHandler, aria...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/window/edit.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1169.04 | **LOC:** 1118 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **24**; blast radius 0.967; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.967
  * `Choke Point (Betweenness):` 0.000226 | `Ripple Effect (Closeness):` 0.007743
  * `Imports (Out-Degree: 13):` , ..behaviors, NVDAHelper.localLib, api, colors, comInterfaces.tom, comtypes, config...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1137.94 | **LOC:** 1658 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` .lockscreen, NVDAObjects.window, annotation, api, appModuleHandler, aria, baseObject, braille...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/IAccessible/ia2TextMozilla.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1084.42 | **LOC:** 852 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 0.584; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%)
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
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 190`, `dead_code: 2`
* *Architecture:* `api: 10`, `import: 17`
* *Defense:* `safety: 42`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.584
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.00295
  * `Imports (Out-Degree: 3):` , NVDAHelper, NVDAObjects, NVDAObjects.IAccessible, api, comInterfaces, compoundDocuments, comtypes...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `source/config/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1054.84 | **LOC:** 1434 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Debt Markers (formerly Tech Debt) (86.6%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 211`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `io: 45`, `api: 48`, `import: 42`
* *Defense:* `safety: 67`, `doc: 43`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` , .configSpec, .featureFlag, .registry, NVDAState, addonHandler, addonHandler.packaging, addonStore.models.status...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/displayModel.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1052.92 | **LOC:** 791 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` NVDAHelper, NVDAObjects.window, XMLFormatting, api, colors, ctypes, locationHelper, logHandler...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/textInfos/offsets.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1040.18 | **LOC:** 796 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **15**; blast radius 1.524; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.524
  * `Choke Point (Betweenness):` 0.00019 | `Ripple Effect (Closeness):` 0.072068
  * `Imports (Out-Degree: 4):` NVDAHelper, NVDAObjects, NVDAState, abc, config, ctypes, dataclasses, locationHelper...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `source/IAccessibleHandler/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1035.86 | **LOC:** 1306 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.8%)
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
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 160`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 34`, `import: 37`
* *Defense:* `safety: 73`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` , .orderedWinEventLimiter, .types, .utils, JABHandler, NVDAObjects.IAccessible, NVDAObjects.IAccessible.mscandui, NVDAObjects.UIA.wordDocument...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nvdaHelper/vbufBackends/adobeAcrobat/adobeAcrobat.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1005.96 | **LOC:** 870 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.441; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AdobeAcrobatVBufBackend_t::fillVBuf` **(Many-Argument Workhorses)** (Impact: 425.9)
  * `renderText` **(Many-Argument Workhorses)** (Impact: 116.7)
  * `AdobeAcrobatVBufBackend_t::renderThread_winEventProcHook` **(Many-Argument Workhorses)** (Impact: 41.4)
  * `fillExplicitTableHeadersForCell` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* /* * Adds table header info for a single cell which explicitly defines headers * using the Headers a...
  * `processText` **(Compute Cores)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 51`, `args: 134`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 103`, `fragile_debt: 3`, `unreferenced_by_name: 9`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` adobeAcrobat.h, ia2utils.h, log.h, iomanip, oleacc.h, nvdaHelperRemote.h, set, sstream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `source/gui/settingsDialogs.py` -> Churn: **100.0%** | Cog Load: 75.0298% | Debt: 11.1879%
- `source/globalCommands.py` -> Churn: **85.74%** | Cog Load: 66.1461% | Debt: 7.7551%
- `source/mathPres/MathCAT/preferences.py` -> Churn: **69.83%** | Cog Load: 60.76% | Debt: 0.0%
- `source/gui/installerGui.py` -> Churn: **52.18%** | Cog Load: 63.8788% | Debt: 18.7231%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `source/NVDAObjects/window/excel.py` -> **Cyrille Bougot** (100.0% isolated ownership) | Magnitude: 2325.76
- `source/NVDAObjects/window/winword.py` -> **Leonard de Ruijter** (100.0% isolated ownership) | Magnitude: 2145.78
- `source/_synthDrivers32/sapi4.py` -> **Michael Curran** (100.0% isolated ownership) | Magnitude: 1230.88
- `source/NVDAObjects/window/edit.py` -> **Sean Budd** (100.0% isolated ownership) | Magnitude: 1169.04
- `source/NVDAObjects/__init__.py` -> **Leonard de Ruijter** (100.0% isolated ownership) | Magnitude: 1137.94

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `source/globalCommands.py` -> **Severity: 2.714** (Bridge: 0.0271 * Flux: 99.9999%)
- `source/inputCore.py` -> **Severity: 1.51** (Bridge: 0.0151 * Flux: 100.0%)
- `source/utils/security.py` -> **Severity: 1.43** (Bridge: 0.0143 * Flux: 100.0%)
- `source/ui.py` -> **Severity: 1.117** (Bridge: 0.0112 * Flux: 99.4266%)
- `source/eventHandler.py` -> **Severity: 0.848** (Bridge: 0.0085 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `source/winUser.py` -> **Severity: 16.517** (Embedded: 0.1699 * Error Risk: 97.2048%)
- `source/winKernel.py` -> **Severity: 16.161** (Embedded: 0.1703 * Error Risk: 94.9154%)
- `source/winBindings/kernel32.py` -> **Severity: 15.38** (Embedded: 0.1739 * Error Risk: 88.4245%)
- `source/winVersion.py` -> **Severity: 14.661** (Embedded: 0.1616 * Error Risk: 90.7154%)
- `source/baseObject.py` -> **Severity: 14.569** (Embedded: 0.1519 * Error Risk: 95.9103%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `source/winBindings/advapi32.py` -> **Severity: 2550.8** (Blast Radius: 25.508 * Doc Risk: 100.0%)
- `source/UIAHandler/_remoteOps/instructions/_base.py` -> **Severity: 2002.4** (Blast Radius: 20.024 * Doc Risk: 100.0%)
- `source/NVDAState.py` -> **Severity: 1846.462** (Blast Radius: 21.612 * Doc Risk: 85.4369%)
- `source/winUser.py` -> **Severity: 1798.188** (Blast Radius: 19.852 * Doc Risk: 90.5797%)
- `source/UIAHandler/_remoteOps/instructions/string.py` -> **Severity: 1641.0** (Blast Radius: 16.41 * Doc Risk: 100.0%)

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
