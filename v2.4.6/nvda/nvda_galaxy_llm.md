# ARCHITECTURAL_BRIEF: nvda
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/nvda` |
| **Timestamp** | `2026-08-03T21:15:05.110783+00:00` |
| **Scan Duration** | `5.35s` |
| **Git Branch** | `master` |
| **Git Commit** | `a94c7f85bd2e8e3e290b314244ea921c4cd01b4c` |
| **Git Remote** | `https://github.com/nvaccess/nvda.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 815 malicious artifacts.

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
| Total Artifacts | 1365 |
| Analyzed Artifacts (Scanned) | 850 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 515 |
| Total LOC | 151616 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 62.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4879 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0855 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8173 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 91 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 674 | 139697 | 79.3% |
| CPP | 107 | 10924 | 12.6% |
| MARKDOWN | 22 | 0 | 2.6% |
| POWERSHELL | 14 | 375 | 1.6% |
| PLAINTEXT | 10 | 0 | 1.2% |
| BATCH | 7 | 67 | 0.8% |
| MAKEFILE | 5 | 190 | 0.6% |
| CSHARP | 4 | 168 | 0.5% |
| RUST | 3 | 137 | 0.4% |
| XML | 2 | 0 | 0.2% |
| C | 1 | 40 | 0.1% |
| HTML | 1 | 18 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.359`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 382 | 44.9% |
| file_cluster_13 | 381 | 44.8% |
| file_cluster_16 | 31 | 3.6% |
| file_cluster_0 | 12 | 1.4% |
| file_cluster_4 | 4 | 0.5% |
| file_cluster_11 | 3 | 0.4% |
| file_cluster_7 | 3 | 0.4% |
| file_cluster_15 | 1 | 0.1% |
| file_cluster_9 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 32 | 3.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 515*

**Composition by Extension & Reason:**
- `.dic`: 129x Excluded (Unsupported Extension: '.dic')
- `.md`: 82x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Lexical Monotony: High structural repetition detected in 5023 LOC), 2x Excluded (Lexical Monotony: High structural repetition detected in 5111 LOC)
- `.po`: 64x Excluded (Unsupported Extension: '.po')
- `.xliff`: 59x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 27x Unsupported Format (.undeterminable), 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 24x Excluded (Unsupported Extension: '.ini')
- `.py`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wav`: 16x Excluded (Explicitly Denied Extension: '.wav')
- `.ttf`: 13x Excluded (Explicitly Denied Extension: '.ttf')
- `.yml`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.robot`: 8x Excluded (Unsupported Extension: '.robot')
- `.pot`: 7x Excluded (Unsupported Extension: '.pot')
- `.yaml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.acf`: 5x Excluded (Unsupported Extension: '.acf')
- `.idl`: 5x Excluded (Unsupported Extension: '.idl')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.2 | 19.0 | 9.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 18.1 | 6.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 28.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 27.3 | 2.4 | 80.0 |
| API Exposure | 0.0 | 15.1 | 3.7 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 41.2 | 17.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.2 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.1 | 26.3 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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
5. **NVDAState.py** (`source/NVDAState.py`) — 56 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **core.py** (`source/core.py`) — 74 outbound dependencies
2. **settingsDialogs.py** (`source/gui/settingsDialogs.py`) — 71 outbound dependencies
3. **braille.py** (`source/braille.py`) — 59 outbound dependencies
4. **globalCommands.py** (`source/globalCommands.py`) — 57 outbound dependencies
5. **excel.py** (`source/NVDAObjects/window/excel.py`) — 50 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` (@ `source/NVDAObjects/IAccessible/ia2TextMozilla.py`) -> Impact: **839.2** | LOC: 704
- `iterate` (@ `source/NVDAObjects/window/excel.py`) -> Impact: **698.3** | LOC: 1080
- `checkForUpdate` (@ `source/updateCheck.py`) -> Impact: **677.7** | LOC: 914
- `speakTypedCharacters` (@ `source/speech/speech.py`) -> Impact: **673.4** | LOC: 508
- `event_valueChange` (@ `source/NVDAObjects/behaviors.py`) -> Impact: **619.5** | LOC: 889
- `getCurrentAutoDisplayDescription` (@ `source/gui/settingsDialogs.py`) -> Impact: **559.1** | LOC: 1067
  * *Intent:* # due to some not very well understood mis ordering of event processing, we force NVDA to # process pending events. This fixes an issue where the chec...
- `getAccessibleTextLineBounds` (@ `source/JABHandler.py`) -> Impact: **497.6** | LOC: 530
  * *Intent:* # Fast path: perform the Java Access Bridge call directly return self._javaGetAccessibleTextRange(start, end) text = [] while start <= end: bufferSize...
- `removeOldLibFiles` (@ `source/installer.py`) -> Impact: **488.3** | LOC: 829
- `_synthWarningDialog` (@ `source/gui/settingsDialogs.py`) -> Impact: **475.5** | LOC: 1270
  * *Intent:* # document formatting settings panel. landmarksText = _("Lan&dmarks and regions") self.landmarksCheckBox = elementsGroup.addItem(wx.CheckBox(elementsG...
- `script_review_currentCharacter` (@ `source/globalCommands.py`) -> Impact: **466.2** | LOC: 1530

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `connectBluetooth` (@ `source/brailleDisplayDrivers/papenmeier.py`) -> **O(2^N) [Recursive]**
- `_normalizeControlField` (@ `source/virtualBuffers/MSHTML.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # C901 'MSHTMLTextInfo._normalizeControlField' is too complex (42) # Look for opportunities to simplify this function.
- `getTextFromIAccessible` (@ `nvdaHelper/remote/textFromIAccessible.cpp`) -> **O(2^N) [Recursive]**
- `generate` (@ `ci/scripts/mozillaSyms.py`) -> **O(2^N) [Recursive]**
- `getRecursiveDataFiles` (@ `runtime-builders/synthDriverHost32/setup-runtime.py`) -> **O(2^N) [Recursive]**
- `MSRPCStubs_buildEmitter` (@ `site_scons/site_tools/msrpc.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # This build emitter tells the builder that a header file, a client stub c file, and a server stub c file will be generated
- `recursive_install` (@ `site_scons/site_tools/recursiveInstall.py`) -> **O(2^N) [Recursive]**
- `initialize` (@ `source/IAccessibleHandler/__init__.py`) -> **O(2^N) [Recursive]**
- `nvdaControllerInternal_reportLiveRegion` (@ `source/NVDAHelper/__init__.py`) -> **O(2^N) [Recursive]**
- `terminate` (@ `source/NVDAHelper/__init__.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `removeOldLibFiles` (@ `source/installer.py`) -> DB Complexity: **259**
- `queueTextChangeNotify` (@ `nvdaHelper/remote/gdiHooks.cpp`) -> DB Complexity: **179**
- `__init__` (@ `source/addonHandler/__init__.py`) -> DB Complexity: **138**
- `checkForUpdate` (@ `source/updateCheck.py`) -> DB Complexity: **116**
- `getCellStates` (@ `nvdaHelper/remote/excel.cpp`) -> DB Complexity: **81**
  * *Intent:* // have GDI calculate the size of the text in pixels, using the loaded font.
- `_logTrace` (@ `source/_synthDrivers32/sapi4.py`) -> DB Complexity: **72**
  * *Intent:* """ Decorator that wraps the COM methods, logs the calls, and converts COMError exceptions to silent ReturnHRESULTs. :param logAll: If true, logs ever...
- `__init__` (@ `source/brailleDisplayDrivers/papenmeier.py`) -> DB Complexity: **67**
- `push` (@ `source/pythonConsole.py`) -> DB Complexity: **67**
- `_convertProsody` (@ `source/synthDrivers/oneCore.py`) -> DB Complexity: **66**
- `displayModel_t::renderText` (@ `nvdaHelper/remote/displayModel.cpp`) -> DB Complexity: **64**
  * *Intent:* // If a focus rectangle was also contained in the source area, copy the focus rectangle as well

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `source` | 101 | 24660.84 | 19.58% | 16.02% |
| `source/UIAHandler` | 8 | 21893.35 | 9.91% | 27.79% |
| `nvdaHelper/remote` | 37 | 7430.54 | 45.76% | 32.91% |
| `source/NVDAObjects/IAccessible` | 21 | 7374.02 | 22.47% | 58.26% |
| `source/appModules` | 79 | 6996.13 | 17.66% | 74.43% |
| `source/gui` | 19 | 6311.06 | 18.03% | 52.66% |
| `source/brailleDisplayDrivers` | 22 | 5175.76 | 28.55% | 52.03% |
| `source/NVDAObjects/window` | 10 | 4144.84 | 17.42% | 33.58% |
| `tests/unit` | 41 | 3831.64 | 3.64% | 0.0% |
| `source/speech` | 11 | 3031.7 | 27.15% | 22.39% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `site_scons/site_tools/gettextTool.py` -> **100.0%** Exposure
- `source/NVDAObjects/IAccessible/SysMonthCal32.py` -> **100.0%** Exposure
- `source/NVDAObjects/IAccessible/delphi.py` -> **100.0%** Exposure
- `source/NVDAObjects/IAccessible/msOffice.py` -> **100.0%** Exposure
- `source/NVDAObjects/IAccessible/qt.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ci/scripts/installNVDA.ps1` -> **100.0%** Exposure
- `ci/scripts/setBuildVersionVars.ps1` -> **100.0%** Exposure
- `ci/scripts/setSconsArgs.ps1` -> **100.0%** Exposure
- `source/NVDAObjects/IAccessible/winConsole.py` -> **100.0%** Exposure
- `source/_bridge/components/proxies/synthDriver.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/unit/test_extensionPoints.py` -> **33** Orphaned Functions | **65** Duplicates
- `tests/unit/test_config.py` -> **68** Orphaned Functions | **22** Duplicates
- `tests/unit/test_messageDialog.py` -> **49** Orphaned Functions | **5** Duplicates
- `tests/unit/test_remote/test_transport.py` -> **29** Orphaned Functions | **21** Duplicates
- `source/gui/settingsDialogs.py` -> **0** Orphaned Functions | **46** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`nvdaHelper/remote/displayModel.cpp`** -> AI Confidence: **99.48%**
2. **`nvdaHelper/remote/excel.cpp`** -> AI Confidence: **99.48%**
3. **`nvdaHelper/vbufBackends/gecko_ia2/gecko_ia2.cpp`** -> AI Confidence: **99.48%**
4. **`nvdaHelper/vbufBackends/webKit/webKit.cpp`** -> AI Confidence: **99.48%**
5. **`source/speech/speech.py`** -> AI Confidence: **99.42%**
6. **`nvdaHelper/remote/WinWord/Fields.cpp`** -> AI Confidence: **99.39%**
7. **`nvdaHelper/remote/ia2LiveRegions.cpp`** -> AI Confidence: **99.39%**
8. **`nvdaHelper/remote/ime.cpp`** -> AI Confidence: **99.39%**
9. **`nvdaHelper/remote/textFromIAccessible.cpp`** -> AI Confidence: **99.39%**
10. **`nvdaHelper/remote/winword.cpp`** -> AI Confidence: **99.39%**
11. **`nvdaHelper/vbufBackends/mshtml/mshtml.cpp`** -> AI Confidence: **99.39%**
12. **`nvdaHelper/vbufBackends/mshtml/node.cpp`** -> AI Confidence: **99.39%**
13. **`nvdaHelper/vbufBase/storage.cpp`** -> AI Confidence: **99.39%**
14. **`nvdaHelper/vbufBackends/lotusNotesRichText/lotusNotesRichText.cpp`** -> AI Confidence: **99.34%**
15. **`nvdaHelper/common/log.h`** -> AI Confidence: **99.32%**
16. **`nvdaHelper/common/xml.h`** -> AI Confidence: **99.32%**
17. **`source/IAccessibleHandler/__init__.py`** -> AI Confidence: **99.31%**
18. **`source/IAccessibleHandler/internalWinEventHandler.py`** -> AI Confidence: **99.31%**
19. **`source/IAccessibleHandler/orderedWinEventLimiter.py`** -> AI Confidence: **99.31%**
20. **`source/NVDAObjects/IAccessible/MSHTML.py`** -> AI Confidence: **99.31%**
21. **`source/NVDAObjects/IAccessible/__init__.py`** -> AI Confidence: **99.31%**
22. **`source/NVDAObjects/IAccessible/adobeAcrobat.py`** -> AI Confidence: **99.31%**
23. **`source/NVDAObjects/IAccessible/ia2TextMozilla.py`** -> AI Confidence: **99.31%**
24. **`source/NVDAObjects/IAccessible/winword.py`** -> AI Confidence: **99.31%**
25. **`source/NVDAObjects/JAB/__init__.py`** -> AI Confidence: **99.31%**
26. **`source/NVDAObjects/UIA/__init__.py`** -> AI Confidence: **99.31%**
27. **`source/NVDAObjects/UIA/spartanEdge.py`** -> AI Confidence: **99.31%**
28. **`source/NVDAObjects/UIA/web.py`** -> AI Confidence: **99.31%**
29. **`source/NVDAObjects/UIA/wordDocument.py`** -> AI Confidence: **99.31%**
30. **`source/NVDAObjects/behaviors.py`** -> AI Confidence: **99.31%**
31. **`source/NVDAObjects/window/edit.py`** -> AI Confidence: **99.31%**
32. **`source/NVDAObjects/window/winword.py`** -> AI Confidence: **99.31%**
33. **`source/UIAHandler/__init__.py`** -> AI Confidence: **99.31%**
34. **`source/UIAHandler/_remoteOps/remoteAPI.py`** -> AI Confidence: **99.31%**
35. **`source/UIAHandler/browseMode.py`** -> AI Confidence: **99.31%**
36. **`source/UIAHandler/utils.py`** -> AI Confidence: **99.31%**
37. **`source/_magnifier/commands.py`** -> AI Confidence: **99.31%**
38. **`source/_remoteClient/client.py`** -> AI Confidence: **99.31%**
39. **`source/_remoteClient/input.py`** -> AI Confidence: **99.31%**
40. **`source/_synthDrivers32/sapi4.py`** -> AI Confidence: **99.31%**
41. **`source/appModules/calculator.py`** -> AI Confidence: **99.31%**
42. **`source/appModules/eclipse.py`** -> AI Confidence: **99.31%**
43. **`source/appModules/explorer.py`** -> AI Confidence: **99.31%**
44. **`source/appModules/logonui.py`** -> AI Confidence: **99.31%**
45. **`source/appModules/outlook.py`** -> AI Confidence: **99.31%**
46. **`source/appModules/windowsinternal_composableshell_experiences_textinput_inputapp.py`** -> AI Confidence: **99.31%**
47. **`source/appModules/wlmail.py`** -> AI Confidence: **99.31%**
48. **`source/audioDucking.py`** -> AI Confidence: **99.31%**
49. **`source/braille.py`** -> AI Confidence: **99.31%**
50. **`source/brailleDisplayDrivers/albatross/driver.py`** -> AI Confidence: **99.31%**
51. **`source/brailleDisplayDrivers/alva.py`** -> AI Confidence: **99.31%**
52. **`source/brailleDisplayDrivers/baum.py`** -> AI Confidence: **99.31%**
53. **`source/brailleDisplayDrivers/brailleNote.py`** -> AI Confidence: **99.31%**
54. **`source/brailleDisplayDrivers/brailliantB.py`** -> AI Confidence: **99.31%**
55. **`source/brailleDisplayDrivers/dotPad/driver.py`** -> AI Confidence: **99.31%**
56. **`source/brailleDisplayDrivers/eurobraille/driver.py`** -> AI Confidence: **99.31%**
57. **`source/brailleDisplayDrivers/freedomScientific.py`** -> AI Confidence: **99.31%**
58. **`source/brailleDisplayDrivers/hedoMobilLine.py`** -> AI Confidence: **99.31%**
59. **`source/brailleDisplayDrivers/hidBrailleStandard.py`** -> AI Confidence: **99.31%**
60. **`source/brailleDisplayDrivers/hims.py`** -> AI Confidence: **99.31%**
61. **`source/brailleDisplayDrivers/lilli.py`** -> AI Confidence: **99.31%**
62. **`source/brailleDisplayDrivers/nlseReaderZoomax.py`** -> AI Confidence: **99.31%**
63. **`source/brailleDisplayDrivers/papenmeier.py`** -> AI Confidence: **99.31%**
64. **`source/brailleDisplayDrivers/papenmeier_serial.py`** -> AI Confidence: **99.31%**
65. **`source/brailleDisplayDrivers/seika.py`** -> AI Confidence: **99.31%**
66. **`source/brailleDisplayDrivers/seikantk.py`** -> AI Confidence: **99.31%**
67. **`source/config/profileUpgradeSteps.py`** -> AI Confidence: **99.31%**
68. **`source/documentNavigation/paragraphHelper.py`** -> AI Confidence: **99.31%**
69. **`source/gui/addonStoreGui/viewModels/store.py`** -> AI Confidence: **99.31%**
70. **`source/gui/configProfiles.py`** -> AI Confidence: **99.31%**
71. **`source/gui/exit.py`** -> AI Confidence: **99.31%**
72. **`source/gui/installerGui.py`** -> AI Confidence: **99.31%**
73. **`source/gui/settingsDialogs.py`** -> AI Confidence: **99.31%**
74. **`source/l10nUtil.py`** -> AI Confidence: **99.31%**
75. **`source/mathPres/MathCAT/speech.py`** -> AI Confidence: **99.31%**
76. **`source/nvda.pyw`** -> AI Confidence: **99.31%**
77. **`source/nvda_slave.pyw`** -> AI Confidence: **99.31%**
78. **`source/speech/manager.py`** -> AI Confidence: **99.31%**
79. **`source/synthDrivers/sapi5.py`** -> AI Confidence: **99.31%**
80. **`source/textInfos/__init__.py`** -> AI Confidence: **99.31%**
81. **`source/textInfos/offsets.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `source/IAccessibleHandler/__init__.py` -> **100.0%** Exposure
- `source/NVDAHelper/__init__.py` -> **100.0%** Exposure
- `source/NVDAObjects/IAccessible/__init__.py` -> **100.0%** Exposure
- `source/NVDAObjects/IAccessible/ia2TextMozilla.py` -> **100.0%** Exposure
- `source/NVDAObjects/window/winword.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `ci/scripts/tests/licenseCheck.ps1` -> **100.0%** Exposure
- `ci/scripts/tests/systemTests.ps1` -> **100.0%** Exposure
- `ci/scripts/tests/translationCheck.ps1` -> **100.0%** Exposure
- `ci/scripts/tests/unitTests.ps1` -> **100.0%** Exposure
- `ensureuv.ps1` -> **100.0%** Exposure
### Raw Memory Manipulation
- `nvdaHelper/vbufBackends/mshtml/mshtml.cpp` -> **9.9646%** Exposure
- `nvdaHelper/vbufBackends/gecko_ia2/gecko_ia2.cpp` -> **4.6426%** Exposure
- `nvdaHelper/remote/winword.cpp` -> **1.1681%** Exposure
- `nvdaHelper/remote/ime.cpp` -> **0.0061%** Exposure
- `nvdaHelper/remote/excel.cpp` -> **0.0053%** Exposure
### Algorithmic DoS Exposure
- `source/speechDictHandler/types.py` -> **100.0%** Exposure
- `nvdaHelper/remote/WinWord/Fields.cpp` -> **100.0%** Exposure
- `nvdaHelper/remote/gdiHooks.cpp` -> **100.0%** Exposure
- `nvdaHelper/remote/textFromIAccessible.cpp` -> **100.0%** Exposure
- `extras/controllerClient/examples/example_csharp/NVDA.cs` -> **99.9999%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5843` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `source/_bridge/runtimes/synthDriverHost/core.py` (PYTHON) -> Cumulative Risk: **730.51**
- **Archetype:** `file_cluster_4` (Distance: 10.816 IQR)
- **Magnitude:** 122.74 | **LOC:** 129 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (99.2401%)
- **Heaviest Functions:** `run` (Impact: 52.0), `schedule` (Impact: 5.3), `__lt__` (Impact: 3.7)

### 2. `source/remotePythonConsole.py` (PYTHON) -> Cumulative Risk: **682.59**
- **Archetype:** `file_cluster_4` (Distance: 11.849 IQR)
- **Magnitude:** 62.2 | **LOC:** 96 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), State Flux (99.9969%), Concurrency (99.9875%)
- **Heaviest Functions:** `handle` (Impact: 10.5), `setPrompt` (Impact: 3.7), `initialize` (Impact: 2.2)

### 3. `source/UIAHandler/_remoteOps/operation.py` (PYTHON) -> Cumulative Risk: **672.91**
- **Archetype:** `file_cluster_13` (Distance: 11.254 IQR)
- **Magnitude:** 262.06 | **LOC:** 353 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Injection Surface (100.0%), State Flux (99.8205%)
- **Heaviest Functions:** `_refreshStaticInstructions` (Impact: 18.4), `_executeUntilSuccess` (Impact: 16.9), `__init__` (Impact: 16.6)

### 4. `nvdaHelper/remote/WinWord/Fields.cpp` (CPP) -> Cumulative Risk: **671.89**
- **Archetype:** `file_cluster_13` (Distance: 13.408 IQR)
- **Magnitude:** 200.58 | **LOC:** 135 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.7341%)
- **Heaviest Functions:** `Fields::Fields` (Impact: 70.4), `Fields::hasLinks` (Impact: 12.7), `Fields::getEndOfPageNumberFieldAtIndex` (Impact: 8.4)

### 5. `ensureuv.ps1` (POWERSHELL) -> Cumulative Risk: **669.48**
- **Archetype:** `file_cluster_0` (Distance: 12.338 IQR)
- **Magnitude:** 98.8 | **LOC:** 119 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Injection Surface (100.0%), State Flux (99.9939%)
- **Heaviest Functions:** `Install-Uv` (Impact: 51.5), `Invoke-Uv` (Impact: 1.2)

### 6. `source/UIAHandler/_remoteOps/localExecute.py` (PYTHON) -> Cumulative Risk: **666.75**
- **Archetype:** `file_cluster_13` (Distance: 11.348 IQR)
- **Magnitude:** 123.02 | **LOC:** 229 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Tech Debt (99.708%), State Flux (96.4818%)
- **Heaviest Functions:** `execute` (Impact: 7.8), `_operationStatusFromException` (Impact: 7.3), `_execute_ForkIfFalse` (Impact: 7.3)

### 7. `nvdaHelper/remote/gdiHooks.cpp` (CPP) -> Cumulative Risk: **644.39**
- **Archetype:** `file_cluster_13` (Distance: 13.552 IQR)
- **Magnitude:** 935.6 | **LOC:** 1275 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (92.4142%)
- **Heaviest Functions:** `queueTextChangeNotify` (Impact: 340.7), `LeaveCriticalSection` (Impact: 11.2), `textChangeNotifyTimerProc` (Impact: 4.8)

### 8. `source/_bridge/components/services/synthDriver.py` (PYTHON) -> Cumulative Risk: **637.28**
- **Archetype:** `file_cluster_13` (Distance: 11.243 IQR)
- **Magnitude:** 239.34 | **LOC:** 232 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `speak` (Impact: 43.9), `__init__` (Impact: 21.6), `terminate` (Impact: 18.2)

### 9. `source/NVDAObjects/behaviors.py` (PYTHON) -> Cumulative Risk: **629.09**
- **Archetype:** `file_cluster_13` (Distance: 12.239 IQR)
- **Magnitude:** 817.52 | **LOC:** 1027 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9983%), Concurrency (99.1974%), State Flux (98.6164%)
- **Heaviest Functions:** `event_valueChange` (Impact: 619.5), `_get_shouldCreateTreeInterceptor` (Impact: 3.7)

### 10. `source/brailleDisplayDrivers/eurobraille/driver.py` (PYTHON) -> Cumulative Risk: **617.2**
- **Archetype:** `file_cluster_13` (Distance: 11.54 IQR)
- **Magnitude:** 196.34 | **LOC:** 406 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.986%), Concurrency (98.576%)
- **Heaviest Functions:** `__init__` (Impact: 55.6), `terminate` (Impact: 14.5), `registerAutomaticDetection` (Impact: 3.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `source/UIAHandler/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.891 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.177 IQR)
- **Top Global Matches:** file_cluster_8: 10.891, file_cluster_13: 11.138, file_cluster_17: 11.335
- **Magnitude:** 21174.17 | **LOC:** 1536 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.3513%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 349`, `structural_boundaries: 206`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 80`, `dead_code: 2`
* *Architecture:* `api: 27`, `concurrency: 13`, `import: 40`
* *Defense:* `safety: 65`, `doc: 18`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` time, appModuleHandler, config, logHandler, comtypes.client, aria, winBindings, winBindings.uiAutomationCore...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/gui/settingsDialogs.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.991 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.752 IQR)
- **Top Global Matches:** file_cluster_8: 12.991, file_cluster_13: 13.155, file_cluster_7: 13.275
- **Magnitude:** 3111.48 | **LOC:** 6712 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 25.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (25.8162%), Tech Debt (75.834%)
**Top Internal Functions/Classes:**
  * `getCurrentAutoDisplayDescription` (Impact: 559.1 | O(2^N) | DB: 57)
    * *Intent:* # due to some not very well understood mis ordering of event processing, we force NVDA to # process ...
  * `_synthWarningDialog` (Impact: 475.5 | O(2^N) | DB: 63)
    * *Intent:* # document formatting settings panel. landmarksText = _("Lan&dmarks and regions") self.landmarksChec...
  * `_validateAllPanels` (Impact: 343.3 | O(2^N) | DB: 32)
  * `__init__` (Impact: 85.0 | O(2^N) | DB: 14)
  * `makeSettings` (Impact: 44.2 | O(N^1) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 607`, `structural_boundaries: 542`, `args: 257`, `func_start: 246`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 638`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 46`
* *Architecture:* `io: 7`, `api: 205`, `concurrency: 1`, `import: 82`
* *Defense:* `safety: 113`, `doc: 149`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.058
  * `Choke Point (Betweenness):` 0.001153 | `Ripple Effect (Closeness):` 0.009295
  * `Imports (Out-Degree: 37):` copy, characterProcessing, math, languageHandler, wx.lib, utils, config, time...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/IAccessible/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.238 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.017 IQR)
- **Top Global Matches:** file_cluster_13: 13.238, file_cluster_8: 13.394, file_cluster_0: 13.524
- **Magnitude:** 2478.56 | **LOC:** 2697 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (31.1898%), Tech Debt (16.2855%)
**Top Internal Functions/Classes:**
  * `getSelectedItemsCount` (Impact: 464.6 | O(2^N) | DB: 20)
    * *Intent:* # accSelection can return IDispatch for a single selected child object
  * `findOverlayClasses` (Impact: 388.1 | O(2^N) | DB: 56)
  * `_get_value` (Impact: 188.9 | O(2^N) | DB: 4)
  * `_isEqual` (Impact: 82.4 | O(2^N) | DB: 1)
    * *Intent:* # Cache the parent.
  * `normalizeIA2TextFormatField` (Impact: 70.4 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 655`, `structural_boundaries: 623`, `args: 151`, `func_start: 151`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 328`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 104`, `import: 67`
* *Defense:* `safety: 283`, `doc: 48`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` comtypes.hresult, displayModel, compoundDocuments, languageHandler, time, config, JABHandler, locationHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/braille.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.322 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.618 IQR)
- **Top Global Matches:** file_cluster_13: 13.322, file_cluster_8: 13.519, file_cluster_16: 13.568
- **Magnitude:** 2347.94 | **LOC:** 4054 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (41.8731%), Tech Debt (54.1223%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 447.7 | O(2^N) | DB: 32)
  * `rindex` (Impact: 357.7 | O(2^N) | DB: 34)
    * *Intent:* # no page turn support
  * `_addTextWithFields` (Impact: 129.9 | O(N^2) | DB: 19)
  * `getFormatFieldBraille` (Impact: 76.9 | O(N^1) | DB: 12)
  * `update` (Impact: 61.0 | O(2^N) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 755`, `structural_boundaries: 495`, `args: 172`, `func_start: 171`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 639`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `api: 104`, `concurrency: 8`, `import: 76`
* *Defense:* `safety: 108`, `doc: 229`, `test: 1`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` globalCommands, displayModel, time, hwIo, config, winAPI.secureDesktop, logHandler, scriptHandler...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/globalCommands.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.686 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.843 IQR)
- **Top Global Matches:** file_cluster_0: 11.686, file_cluster_8: 11.703, file_cluster_13: 11.986
- **Magnitude:** 2104.12 | **LOC:** 5468 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 23.8%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (14.6952%), Tech Debt (7.7552%)
**Top Internal Functions/Classes:**
  * `script_review_currentCharacter` (Impact: 466.2 | O(N^1) | DB: 5)
  * `script_previousSynthSetting` (Impact: 270.5 | O(N^1))
  * `script_touch_changeMode` (Impact: 190.7 | O(N^1) | DB: 7)
  * `script_braille_cycleShowMessages` (Impact: 70.6 | O(N^1))
  * `script_navigatorObject_current` (Impact: 44.0 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 799`, `structural_boundaries: 522`, `args: 275`, `func_start: 272`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 55`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 340`, `import: 64`
* *Defense:* `safety: 109`, `doc: 44`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.401
  * `Choke Point (Betweenness):` 0.026718 | `Ripple Effect (Closeness):` 0.126648
  * `Imports (Out-Degree: 33):` characterProcessing, appModuleHandler, languageHandler, config, logHandler, scriptHandler, base64, brailleInput...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `nvdaHelper/vbufBackends/mshtml/mshtml.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.673 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.735 IQR)
- **Top Global Matches:** file_cluster_8: 14.673, file_cluster_13: 14.799, file_cluster_11: 14.987
- **Magnitude:** 1531.18 | **LOC:** 1425 | **CtrlFlow:** 75.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (77.5223%), Tech Debt (19.1039%)
**Top Internal Functions/Classes:**
  * `LocateHTMLElementInDocument` (Impact: 108.8 | O(2^N) | DB: 48)
  * `getIAccessibleInfo` (Impact: 56.4 | O(N^1) | DB: 35)
  * `getAttributesFromHTMLDOMNode` (Impact: 42.1 | O(N^1) | DB: 15)
  * `getCurrentStyleInfoFromHTMLDOMNode` (Impact: 36.6 | O(N^1) | DB: 20)
  * `fillTextFormatting_helper` (Impact: 34.2 | O(N^1) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 90`, `args: 225`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 1121`, `dead_code: 1`, `orphaned_logic: 9`
* *Architecture:* `import: 16`
* *Defense:* `doc: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` map, windows.h, oleidl.h, backend.h, oleacc.h, string, mshtml.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/speech/speech.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.766 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.108 IQR)
- **Top Global Matches:** file_cluster_13: 12.766, file_cluster_8: 12.815, file_cluster_16: 12.967
- **Magnitude:** 1461.0 | **LOC:** 3171 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (56.4484%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `speakTypedCharacters` (Impact: 673.4 | O(2^N) | DB: 33)
  * `getIndentationSpeech` (Impact: 32.8 | O(N^1) | DB: 7)
  * `_rowAndColumnCountText` (Impact: 20.0 | O(N^1))
    * *Intent:* # Translators: Speaks current row number (example output: row 3).
  * `getCurrentLanguage` (Impact: 12.8 | O(N^1))
  * `getCharDescListFromText` (Impact: 11.4 | O(N^1) | DB: 1)
    * *Intent:* # The pitch change may be useful, # as a pitch change may be harder to notice, # and continuing the ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 952`, `structural_boundaries: 258`, `args: 61`, `func_start: 61`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 523`, `dead_code: 4`
* *Architecture:* `api: 56`, `import: 50`
* *Defense:* `safety: 63`, `doc: 101`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.644
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004207
  * `Imports (Out-Degree: 23):` copy, characterProcessing, textUtils.uniscribe, time, languageHandler, config, logHandler, scriptHandler...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `source/browseMode.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.876 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.986 IQR)
- **Top Global Matches:** file_cluster_13: 11.876, file_cluster_8: 11.954, file_cluster_7: 12.152
- **Magnitude:** 1420.02 | **LOC:** 2729 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (24.324%), Tech Debt (61.264%)
**Top Internal Functions/Classes:**
  * `_replayFocusEnteredEvents` (Impact: 449.7 | O(2^N) | DB: 16)
    * *Intent:* # When a control (such as a combo box) is expanded, we expect that its descendants will be classed a...
  * `_getLabelForProperties` (Impact: 142.7 | O(N^1) | DB: 5)
  * `_set_selection` (Impact: 66.4 | O(2^N) | DB: 6)
    * *Intent:* # This treeInterceptor is gaining focus for the first time.
  * `reportPassThrough` (Impact: 32.0 | O(2^N) | DB: 3)
    * *Intent:* """Reports the pass through mode if it has changed. @param treeInterceptor: The current Browse Mode ...
  * `filter` (Impact: 28.4 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 316`, `args: 116`, `func_start: 110`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 194`, `dead_code: 4`, `planned_debt: 3`, `duplicate_logic: 14`
* *Architecture:* `io: 1`, `api: 80`, `import: 50`
* *Defense:* `safety: 70`, `doc: 79`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` time, utils, config, abc, logHandler, scriptHandler, aria, weakref...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/appModules/foobar2000.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.943 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.095 IQR)
- **Top Global Matches:** file_cluster_13: 9.943, file_cluster_8: 10.261, file_cluster_0: 10.285
- **Magnitude:** 1387.13 | **LOC:** 212 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.8383%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 47`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`, `dead_code: 2`
* *Architecture:* `api: 7`, `import: 12`
* *Defense:* `safety: 4`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.906
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001178
  * `Imports (Out-Degree: 5):` ui, NVDAObjects, utils.localisation, appModuleHandler, datetime, re, logHandler, scriptHandler...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/UIA/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.693 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.427 IQR)
- **Top Global Matches:** file_cluster_8: 12.693, file_cluster_13: 12.699, file_cluster_7: 12.943
- **Magnitude:** 1249.2 | **LOC:** 2794 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (23.0199%), Tech Debt (61.1357%)
**Top Internal Functions/Classes:**
  * `_getFormatFieldFontSize` (Impact: 396.7 | O(2^N) | DB: 1)
  * `event_stateChange` (Impact: 25.2 | O(2^N))
  * `_get_positionInfo` (Impact: 16.7 | O(N^1))
    * *Intent:* # r is a tuple of floats representing left, top, width and height. return locationHelper.RectLTWH.fr...
  * `_get_positionInfo` (Impact: 15.1 | O(N^1))
  * `event_UIA_dropTargetEffect` (Impact: 15.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 618`, `structural_boundaries: 475`, `args: 147`, `func_start: 147`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 313`, `dead_code: 1`, `fragile_debt: 4`, `duplicate_logic: 15`
* *Architecture:* `api: 99`, `import: 50`
* *Defense:* `safety: 177`, `doc: 74`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` displayModel, time, languageHandler, config, locationHelper, logHandler, .excel, NVDAObjects.behaviors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/window/winword.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.102 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.074 IQR)
- **Top Global Matches:** file_cluster_8: 11.102, file_cluster_13: 11.223, file_cluster_0: 11.426
- **Magnitude:** 1166.32 | **LOC:** 2230 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (24.8269%), Tech Debt (89.4457%)
**Top Internal Functions/Classes:**
  * `_move` (Impact: 357.4 | O(2^N))
  * `activate` (Impact: 69.9 | O(N^1) | DB: 9)
    * *Intent:* # Translators: a distance from the left edge of the page in Microsoft Word
  * `get` (Impact: 32.9 | O(2^N))
  * `iterate` (Impact: 29.7 | O(N^1) | DB: 5)
  * `compareEndPoints` (Impact: 27.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 346`, `args: 108`, `func_start: 108`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 119`, `duplicate_logic: 32`
* *Architecture:* `api: 130`, `import: 41`
* *Defense:* `safety: 45`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.914
  * `Choke Point (Betweenness):` 0.003118 | `Ripple Effect (Closeness):` 0.084717
  * `Imports (Out-Degree: 18):` time, languageHandler, utils.urlUtils, config, locationHelper, logHandler, scriptHandler, comtypes.client...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/IAccessible/MSHTML.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.509 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.957 IQR)
- **Top Global Matches:** file_cluster_8: 12.509, file_cluster_13: 12.542, file_cluster_0: 12.83
- **Magnitude:** 1153.66 | **LOC:** 1273 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (49.6749%), Tech Debt (35.8812%)
**Top Internal Functions/Classes:**
  * `_get_location` (Impact: 296.7 | O(N^1) | DB: 17)
  * `__init__` (Impact: 96.1 | O(2^N) | DB: 3)
  * `expand` (Impact: 95.4 | O(2^N) | DB: 2)
  * `locateHTMLElementByID` (Impact: 75.1 | O(2^N))
  * `findOverlayClasses` (Impact: 60.5 | O(2^N) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 319`, `args: 79`, `func_start: 79`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 138`, `duplicate_logic: 8`
* *Architecture:* `api: 56`, `import: 28`
* *Defense:* `safety: 133`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.715
  * `Choke Point (Betweenness):` 0.001309 | `Ripple Effect (Closeness):` 0.003534
  * `Imports (Out-Degree: 7):` locationHelper, logHandler, comtypes.client, aria, winBindings, IAccessibleHandler, api, ctypes...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/window/excel.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.986 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.759 IQR)
- **Top Global Matches:** file_cluster_13: 11.986, file_cluster_8: 12.019, file_cluster_0: 12.032
- **Magnitude:** 1097.26 | **LOC:** 2645 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (29.0952%), Tech Debt (9.6295%)
**Top Internal Functions/Classes:**
  * `iterate` (Impact: 698.3 | O(2^N) | DB: 50)
  * `__getattr__` (Impact: 11.9 | O(N^1))
    * *Intent:* """Module level `__getattr__` used to preserve backward compatibility."""
  * `__init__` (Impact: 7.7 | O(N^1) | DB: 5)
  * `QuickNavItemClass` (Impact: 1.9 | O(N^1))
  * `collectionFromWorksheet` (Impact: 1.9 | O(N^1))
    * *Intent:* """The particular L{ExcelCellInfoQuicknavItem} subclass for objects that should be emitted from the ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 552`, `args: 204`, `func_start: 200`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 190`, `dead_code: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 138`, `import: 54`
* *Defense:* `safety: 98`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.906
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001178
  * `Imports (Out-Degree: 21):` displayModel, time, winAPI.winUser.functions, utils.urlUtils, config, NVDAHelper.localLib, abc, logHandler...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `source/NVDAObjects/IAccessible/ia2TextMozilla.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.162 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.899 IQR)
- **Top Global Matches:** file_cluster_13: 12.162, file_cluster_8: 12.262, file_cluster_11: 12.513
- **Magnitude:** 1096.62 | **LOC:** 852 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (82.4203%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 839.2 | O(2^N) | DB: 53)
  * `_getControlFieldForObject` (Impact: 29.1 | O(2^N))
  * `_get_boundingRects` (Impact: 13.3 | O(N^1) | DB: 1)
  * `_isCaretAtEndOfLine` (Impact: 11.8 | O(N^1))
  * `_getEmbedded` (Impact: 7.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 124`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 163`, `dead_code: 2`
* *Architecture:* `api: 8`, `import: 17`
* *Defense:* `safety: 44`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.648
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003141
  * `Imports (Out-Degree: 3):` NVDAObjects, ctypes, compoundDocuments, textInfos, controlTypes, winUser, comtypes, locationHelper...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `source/_synthDrivers32/sapi4.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.453 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.144 IQR)
- **Top Global Matches:** file_cluster_13: 13.453, file_cluster_0: 13.503, file_cluster_16: 13.657
- **Magnitude:** 1080.88 | **LOC:** 1268 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (47.8075%), Tech Debt (73.4834%)
**Top Internal Functions/Classes:**
  * `_logTrace` (Impact: 387.6 | O(2^N) | DB: 72)
    * *Intent:* """ Decorator that wraps the COM methods, logs the calls, and converts COMError exceptions to silent...
  * `speak` (Impact: 124.2 | O(N^1) | DB: 43)
  * `ITTSBufNotifySink_BookMark` (Impact: 27.6 | O(2^N))
  * `_getAvailableVoices` (Impact: 20.1 | O(N^1) | DB: 3)
  * `IUnknown_Release` (Impact: 13.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 207`, `args: 86`, `func_start: 85`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 346`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 7`, `orphaned_logic: 3`
* *Architecture:* `api: 56`, `concurrency: 38`, `import: 26`
* *Defense:* `safety: 50`, `doc: 73`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` time, config, winreg, logHandler, speech.commands, weakref, winBindings, ctypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/ui.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.587 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.786 IQR)
- **Top Global Matches:** file_cluster_13: 9.587, file_cluster_8: 9.598, file_cluster_16: 9.983
- **Magnitude:** 975.41 | **LOC:** 317 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.6024%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 52`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 4`, `api: 5`, `import: 24`
* *Defense:* `safety: 8`, `doc: 29`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.226
  * `Choke Point (Betweenness):` 0.012614 | `Ripple Effect (Closeness):` 0.168908
  * `Imports (Out-Degree: 6):` html, logHandler, comtypes.client, config.configFlags, nh3, ctypes, to, gui...
  * `Imported By (In-Degree: 72):` (Excluded from Brief to save tokens)

### `nvdaHelper/remote/gdiHooks.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.552 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.022 IQR)
- **Top Global Matches:** file_cluster_13: 13.552, file_cluster_8: 13.564, file_cluster_7: 13.848
- **Magnitude:** 935.6 | **LOC:** 1275 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 179
- **Risk Profile:** Cognitive Load (71.9951%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `queueTextChangeNotify` (Impact: 340.7 | O(N^2) | DB: 179)
  * `LeaveCriticalSection` (Impact: 11.2 | O(2^N))
    * *Intent:* //Call the real function
  * `textChangeNotifyTimerProc` (Impact: 4.8 | O(N^1) | DB: 2)
  * `LeaveCriticalSection` (Impact: 4.5 | O(2^N))
  * `apiHook_hookFunction_safe` (Impact: 4.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 114`, `args: 47`, `func_start: 87`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 524`, `duplicate_logic: 13`, `orphaned_logic: 2`
* *Architecture:* `api: 4`, `import: 16`
* *Defense:* `doc: 19`, `sync_locks: 1`, `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` map, windows.h, gdiHooks.h, optional, usp10.h, list, displayModel.h, vector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.837 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.279 IQR)
- **Top Global Matches:** file_cluster_13: 12.837, file_cluster_16: 12.907, file_cluster_8: 13.143
- **Magnitude:** 923.24 | **LOC:** 1658 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (29.1333%), Tech Debt (9.2939%)
**Top Internal Functions/Classes:**
  * `_get_placeholder` (Impact: 116.7 | O(N^1) | DB: 5)
  * `_findSimpleNext` (Impact: 104.4 | O(2^N))
  * `__call__` (Impact: 85.7 | O(N^1) | DB: 4)
  * `_get_presentationType` (Impact: 43.4 | O(N^1))
  * `_get_devInfo` (Impact: 25.7 | O(N^1) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 334`, `args: 130`, `func_start: 130`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 97`, `planned_debt: 3`
* *Architecture:* `api: 131`, `import: 36`
* *Defense:* `safety: 60`, `doc: 221`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` displayModel, time, appModuleHandler, utils.urlUtils, config, locationHelper, logHandler, aria...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nvdaHelper/vbufBackends/mshtml/node.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.016 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.249 IQR)
- **Top Global Matches:** file_cluster_8: 14.016, file_cluster_13: 14.119, file_cluster_7: 14.438
- **Magnitude:** 861.6 | **LOC:** 514 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (94.5209%), Tech Debt (99.7733%)
**Top Internal Functions/Classes:**
  * `MshtmlVBufStorage_controlFieldNode_t::po` (Impact: 72.5 | O(N^1) | DB: 33)
  * `IHTMLChangeSink::Notify` (Impact: 71.9 | O(N^1) | DB: 31)
  * `MshtmlVBufStorage_controlFieldNode_t::pr` (Impact: 52.0 | O(N^1) | DB: 29)
  * `MshtmlVBufStorage_controlFieldNode_t` (Impact: 51.6 | O(2^N) | DB: 2)
  * `MshtmlVBufStorage_controlFieldNode_t::Ms` (Impact: 45.5 | O(N^1) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 51`, `args: 47`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 452`, `duplicate_logic: 12`, `orphaned_logic: 9`
* *Architecture:* `api: 2`, `import: 11`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` windows.h, oleidl.h, list, mshtml.h, node.h, objbase.h, mshtmdid.h, xml.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/brailleDisplayDrivers/papenmeier.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.615 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.884 IQR)
- **Top Global Matches:** file_cluster_13: 13.615, file_cluster_11: 13.822, file_cluster_0: 13.875
- **Magnitude:** 856.58 | **LOC:** 693 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (36.1728%), Tech Debt (20.3009%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 135.0 | O(2^N) | DB: 67)
  * `__init__` (Impact: 110.6 | O(2^N) | DB: 16)
  * `connectBluetooth` (Impact: 42.8 | O(2^N) | DB: 2)
  * `brl_decode_keys_A` (Impact: 25.6 | O(N^1) | DB: 8)
  * `_swapDotBits` (Impact: 19.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 68`, `args: 22`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 345`, `dead_code: 4`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 19`, `import: 13`
* *Defense:* `safety: 28`, `doc: 42`, `test: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` keyboardHandler, time, baseObject, braille, logHandler, typing, inputCore, brailleInput...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/updateCheck.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.994 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_13: 11.994, file_cluster_8: 12.283, file_cluster_11: 12.446
- **Magnitude:** 848.72 | **LOC:** 1126 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 71.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 116
- **Risk Profile:** Cognitive Load (14.8391%), Tech Debt (8.5087%)
**Top Internal Functions/Classes:**
  * `checkForUpdate` (Impact: 677.7 | O(2^N) | DB: 116)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 173`, `args: 59`, `func_start: 52`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 121`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 23`, `api: 31`, `concurrency: 3`, `import: 45`
* *Defense:* `safety: 30`, `doc: 57`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.612
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.008439
  * `Imports (Out-Degree: 13):` time, languageHandler, addonHandler, config, utils, logHandler, garbageHandler, at...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `nvdaHelper/remote/displayModel.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.59 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.608 IQR)
- **Top Global Matches:** file_cluster_13: 14.59, file_cluster_8: 14.702, file_cluster_11: 14.848
- **Magnitude:** 820.52 | **LOC:** 430 | **CtrlFlow:** 85.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (80.8528%), Tech Debt (29.6693%)
**Top Internal Functions/Classes:**
  * `displayModel_t::renderText` (Impact: 84.9 | O(N^1) | DB: 64)
    * *Intent:* // If a focus rectangle was also contained in the source area, copy the focus rectangle as well
  * `displayModel_t::copyRectangle` (Impact: 77.3 | O(N^1) | DB: 37)
  * `displayModel_t::clearRectangle` (Impact: 39.1 | O(N^1) | DB: 24)
  * `displayModelChunk_t::truncate` (Impact: 25.3 | O(N^1) | DB: 19)
  * `displayModel_t::insertChunk` (Impact: 21.0 | O(N^1) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 18`, `args: 31`, `func_start: 15`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 504`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 12`, `import: 10`
* *Defense:* `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` list, string, displayModel.h, xml.h, algorithm, log.h, deque, set...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/NVDAObjects/behaviors.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.239 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.477 IQR)
- **Top Global Matches:** file_cluster_13: 12.239, file_cluster_8: 12.427, file_cluster_0: 12.531
- **Magnitude:** 817.52 | **LOC:** 1027 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (19.8567%), Tech Debt (10.6726%)
**Top Internal Functions/Classes:**
  * `event_valueChange` (Impact: 619.5 | O(2^N) | DB: 48)
  * `_get_shouldCreateTreeInterceptor` (Impact: 3.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 191`, `args: 75`, `func_start: 75`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 109`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 59`, `concurrency: 13`, `import: 24`
* *Defense:* `safety: 28`, `doc: 70`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.637
  * `Choke Point (Betweenness):` 0.003637 | `Ripple Effect (Closeness):` 0.09588
  * `Imports (Out-Degree: 9):` characterProcessing, time, config, logHandler, scriptHandler, queueHandler, editableText, config.configFlags...
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `nvdaHelper/remote/ime.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.905 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.17 IQR)
- **Top Global Matches:** file_cluster_8: 13.905, file_cluster_13: 14.076, file_cluster_11: 14.183
- **Magnitude:** 807.84 | **LOC:** 573 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (91.8547%), Tech Debt (27.3764%)
**Top Internal Functions/Classes:**
  * `handleIMEWindowMessage` (Impact: 88.2 | O(N^1) | DB: 5)
  * `handleReadingStringUpdate` (Impact: 72.6 | O(N^1) | DB: 49)
    * *Intent:* //Only reported for japanese
  * `handleCandidates` (Impact: 31.3 | O(N^1) | DB: 31)
  * `getIMEVersion` (Impact: 24.6 | O(N^1) | DB: 12)
  * `getTIPFilename` (Impact: 15.4 | O(N^1) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 56`, `args: 71`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 479`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ime.h, windows.h, wchar.h, typedCharacter.h, nvdaHelperRemote.h, log.h, tsf.h, nvdaControllerInternal.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nvdaHelper/remote/tsf.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.898 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.61 IQR)
- **Top Global Matches:** file_cluster_8: 13.898, file_cluster_13: 14.034, file_cluster_7: 14.348
- **Magnitude:** 799.66 | **LOC:** 644 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (68.9001%), Tech Debt (89.4745%)
**Top Internal Functions/Classes:**
  * `TsfSink::Initialize` (Impact: 32.2 | O(N^1) | DB: 29)
  * `TSF_winEventHook` (Impact: 26.7 | O(N^1) | DB: 2)
  * `TsfSink::OnActivated` (Impact: 21.8 | O(N^1) | DB: 12)
  * `TsfSink::QueryInterface` (Impact: 20.0 | O(N^1) | DB: 5)
  * `TsfSink::OnEndEdit` (Impact: 20.0 | O(N^1) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 76`, `args: 75`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 524`, `orphaned_logic: 24`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` map, ime.h, windows.h, wchar.h, inputLangChange.h, msctf.h, typedCharacter.h, algorithm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `source/UIAHandler/_remoteOps/instructions/array.py` (PYTHON) | Magnitude: 30.92 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 41, structural_boundaries: 27, api: 14, safety_bypasses: 10
- `source/globalCommands.py` (PYTHON) | Magnitude: 2104.12 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 4101, branch: 799, structural_boundaries: 522, api: 340
- `ensureuv.ps1` (POWERSHELL) | Magnitude: 98.8 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 89, branch: 31, state_mutation: 31, closures: 21
- `source/UIAHandler/_remoteOps/instructions/textRange.py` (PYTHON) | Magnitude: 57.82 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 118, structural_boundaries: 40, safety_bypasses: 34, explicit_casts: 33
- `source/gui/guiHelper.py` (PYTHON) | Magnitude: 225.42 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 264, encapsulation: 80, structural_boundaries: 76, branch: 60

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `nvdaHelper/local/silenceDetect.h` (CPP) | Magnitude: 191.6 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 125, state_mutation: 94, branch: 46, structural_boundaries: 45
- `ci/scripts/installNVDA.ps1` (POWERSHELL) | Magnitude: 31.38 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 15, indent_tabs: 6, structural_boundaries: 5, branch: 3
- `tests/manual/nvdaUI/createUpdatableAddons.ps1` (POWERSHELL) | Magnitude: 18.44 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 17, state_mutation: 8, io: 6, closures: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `source/appModules/doctts.py` (PYTHON) | Magnitude: 12.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, class_start: 1, api: 1, import: 1
- `source/appModules/dosvox.py` (PYTHON) | Magnitude: 12.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, class_start: 1, api: 1, import: 1
- `source/appModules/skype.py` (PYTHON) | Magnitude: 12.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, class_start: 1, api: 1, import: 1
- `source/textInfos/__init__.py` (PYTHON) | Magnitude: 240.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 519, structural_boundaries: 155, branch: 143, doc: 97
- `source/_bridge/components/services/synthDriver.py` (PYTHON) | Magnitude: 239.34 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 184, encapsulation: 53, structural_boundaries: 51, state_mutation: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `ci/scripts/setBuildVersionVars.ps1` (POWERSHELL) | Magnitude: 61.74 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 39, indent_tabs: 26, globals: 23, branch: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `site_scons/site_tools/listModules.py` (PYTHON) | Magnitude: 8.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 21, structural_boundaries: 9, doc: 8, branch: 6
- `source/gui/message.py` (PYTHON) | Magnitude: 510.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 626, doc: 259, encapsulation: 185, structural_boundaries: 177
- `source/addonStore/models/status.py` (PYTHON) | Magnitude: 156.34 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 308, structural_boundaries: 122, encapsulation: 66, branch: 45
- `source/documentNavigation/sentenceHelper.py` (PYTHON) | Magnitude: 6.96 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 6, branch: 2, doc: 2
- `source/utils/caseInsensitiveCollections.py` (PYTHON) | Magnitude: 33.5 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 22, encapsulation: 21, structural_boundaries: 13, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `nvdaHelper/local/UIAEventLimiter/rateLimitedEventHandler.h` (CPP) | Magnitude: 51.94 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 37, doc: 29, concurrency: 18, state_mutation: 17
- `source/remotePythonConsole.py` (PYTHON) | Magnitude: 62.2 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 50, state_mutation: 19, structural_boundaries: 17, concurrency: 13
- `nvdaHelper/localWin10/uwpOcr.cpp` (CPP) | Magnitude: 96.06 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 49, state_mutation: 43, structural_boundaries: 32, args: 13
- `source/_bridge/runtimes/synthDriverHost/core.py` (PYTHON) | Magnitude: 122.74 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 82, encapsulation: 42, concurrency: 31, structural_boundaries: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `extras/controllerClient/examples/example_csharp/SpeechPriority.cs` (CSHARP) | Magnitude: 19.2 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 16, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2
- `tests/unit/extensionPointTestHelpers.py` (PYTHON) | Magnitude: 32.98 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 113, doc: 39, structural_boundaries: 25, encapsulation: 15
- `source/exceptions.py` (PYTHON) | Magnitude: 11.52 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 1, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `source/addonHandler/addonVersionCheck.py` (PYTHON) | Magnitude: 7.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 11, doc: 6, api: 4
- `source/mathPres/MathCAT/localization.py` (PYTHON) | Magnitude: 118.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 263, structural_boundaries: 39, state_mutation: 33, branch: 26
- `nvdaHelper/remote/IA2Support.cpp` (CPP) | Magnitude: 624.8 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 323, indent_tabs: 293, branch: 84, structural_boundaries: 63
- `source/NVDAObjects/UIA/__init__.py` (PYTHON) | Magnitude: 1249.2 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 2170, branch: 618, structural_boundaries: 475, encapsulation: 325
- `tests/unit/test_UIARemoteOps/test_highLevel/test_instructionLimit.py` (PYTHON) | Magnitude: 15.64 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 11, api: 5, test: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `source/localesData.py` (PYTHON) | Magnitude: 13.64 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 5, doc: 2, dead_code: 1, generics: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `source/gui/settingsDialogs.py` -> Churn: **100.0%** | Cog Load: 25.8162% | Debt: 75.834%
- `source/mathPres/MathCAT/preferences.py` -> Churn: **66.91%** | Cog Load: 15.975% | Debt: 99.7794%
- `source/speech/speech.py` -> Churn: **58.03%** | Cog Load: 56.4484% | Debt: 0.0%
- `source/config/__init__.py` -> Churn: **51.64%** | Cog Load: 9.5472% | Debt: 99.9853%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `source/NVDAObjects/IAccessible/MSHTML.py` -> **Sascha Cowley** (100.0% isolated ownership) | Magnitude: 1153.66
- `source/_synthDrivers32/sapi4.py` -> **Michael Curran** (100.0% isolated ownership) | Magnitude: 1080.88
- `source/ui.py` -> **Michael Curran** (100.0% isolated ownership) | Magnitude: 975.41
- `source/NVDAObjects/__init__.py` -> **Leonard de Ruijter** (100.0% isolated ownership) | Magnitude: 923.24
- `source/brailleDisplayDrivers/papenmeier.py` -> **Sascha Cowley** (100.0% isolated ownership) | Magnitude: 856.58

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `source/inputCore.py` -> **Severity: 1.188** (Bridge: 0.0121 * Flux: 98.017%)
- `source/eventHandler.py` -> **Severity: 0.874** (Bridge: 0.0125 * Flux: 70.0843%)
- `source/appModuleHandler.py` -> **Severity: 0.785** (Bridge: 0.0079 * Flux: 99.7006%)
- `source/utils/security.py` -> **Severity: 0.704** (Bridge: 0.0185 * Flux: 38.1316%)
- `source/baseObject.py` -> **Severity: 0.703** (Bridge: 0.0081 * Flux: 86.8375%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `source/utils/displayString.py` -> **Severity: 10.748** (Embedded: 0.1343 * Error Risk: 80.0%)
- `source/buildVersion.py` -> **Severity: 10.669** (Embedded: 0.1334 * Error Risk: 80.0%)
- `source/baseObject.py` -> **Severity: 10.497** (Embedded: 0.1579 * Error Risk: 66.4583%)
- `nvdaHelper/local/textUtils.cpp` -> **Severity: 9.819** (Embedded: 0.1363 * Error Risk: 72.0561%)
- `source/queueHandler.py` -> **Severity: 8.752** (Embedded: 0.1417 * Error Risk: 61.746%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `source/winUser.py` -> **Severity: 2197.7** (Blast Radius: 21.977 * Doc Risk: 100.0%)
- `source/NVDAState.py` -> **Severity: 2151.2** (Blast Radius: 21.512 * Doc Risk: 100.0%)
- `source/winKernel.py` -> **Severity: 1530.1** (Blast Radius: 15.301 * Doc Risk: 100.0%)
- `source/UIAHandler/_remoteOps/builder.py` -> **Severity: 1480.477** (Blast Radius: 16.061 * Doc Risk: 92.1784%)
- `source/UIAHandler/_remoteOps/instructions/string.py` -> **Severity: 1352.395** (Blast Radius: 13.557 * Doc Risk: 99.7562%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
