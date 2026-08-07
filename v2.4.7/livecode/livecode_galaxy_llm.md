# ARCHITECTURAL_BRIEF: livecode
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/livecode` |
| **Timestamp** | `2026-08-07T05:08:25.219206+00:00` |
| **Scan Duration** | `12.98s` |
| **Git Branch** | `develop` |
| **Git Commit** | `4606a10ea10b16d5071d0f9f263ccdd7ede8b31d` |
| **Git Remote** | `https://github.com/livecode/livecode.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1744 malicious artifacts.

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
| Total Artifacts | 7645 |
| Analyzed Artifacts (Scanned) | 1996 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5649 |
| Total LOC | 441788 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 26.1% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3296 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.064 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6035 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 73 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 1023 | 317078 | 51.3% |
| LIVECODE | 366 | 40476 | 18.3% |
| MARKDOWN | 163 | 0 | 8.2% |
| OBJECTIVE-C | 103 | 39244 | 5.2% |
| PYTHON | 96 | 14288 | 4.8% |
| JAVA | 79 | 15071 | 4.0% |
| XML | 36 | 0 | 1.8% |
| C | 35 | 10069 | 1.8% |
| PERL | 28 | 1071 | 1.4% |
| SHELL | 21 | 641 | 1.1% |
| PLAINTEXT | 20 | 0 | 1.0% |
| JAVASCRIPT | 11 | 1385 | 0.6% |
| MAKEFILE | 5 | 849 | 0.3% |
| BATCH | 5 | 147 | 0.3% |
| HTML | 3 | 1452 | 0.2% |
| JSON | 2 | 17 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.731`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1046 | 52.4% |
| file_cluster_13 | 514 | 25.8% |
| file_cluster_2 | 88 | 4.4% |
| file_cluster_17 | 56 | 2.8% |
| file_cluster_7 | 43 | 2.2% |
| file_cluster_12 | 24 | 1.2% |
| file_cluster_4 | 16 | 0.8% |
| file_cluster_9 | 13 | 0.7% |
| file_cluster_0 | 6 | 0.3% |
| file_cluster_16 | 4 | 0.2% |
| file_cluster_11 | 2 | 0.1% |
| file_cluster_6 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 183 | 9.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5649*

**Composition by Extension & Reason:**
- `.lcdoc`: 2630x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1707x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 67 LOC)
- `.json`: 335x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.test`: 322x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 127x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 88x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Unsupported Format (.undeterminable), 2x Excluded (Binary Format Detected)
- `.lcb`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 47 exceeds 500 chars), 2x Excluded (Saturation: Line 49 exceeds 500 chars)
- `.py`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.diff`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 1583 hex tokens in 907 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1456 LOC)
- `.txt`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 13053 LOC), 1x Excluded (Monolithic Amalgamation: 161855 LOC exceeds safe regex boundaries)
- `.strings`: 18x Excluded (Unsupported Extension: '.strings')
- `.b`: 18x Unsupported Format (.b)
- `.sh`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.livecode`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Binary Format Detected), 1x Excluded (Saturation: Line 6 exceeds 500 chars)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 32.3 | 32.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 67.6 | 82.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 45.8 | 27.2 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 27.8 | 2.4 | 80.0 |
| API Exposure | 0.0 | 16.0 | 2.3 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 62.8 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 99.5 | 2.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 18.6 | 11.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `extensions/libraries/timezone/tz/Makefile` (Hits: 70)
- `tests/lcs/core/network/network.livecodescript` (Hits: 54)
- `config.py` (Hits: 45)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **prefix.h** (`engine/src/prefix.h`) — 435 inbound connections
2. **parsedef.h** (`engine/src/parsedef.h`) — 422 inbound connections
3. **globdefs.h** (`engine/src/globdefs.h`) — 416 inbound connections
4. **filedefs.h** (`engine/src/filedefs.h`) — 410 inbound connections
5. **objdefs.h** (`engine/src/objdefs.h`) — 402 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **globals.cpp** (`engine/src/globals.cpp`) — 58 outbound dependencies
2. **opensslsocket.cpp** (`engine/src/opensslsocket.cpp`) — 54 outbound dependencies
3. **object.cpp** (`engine/src/object.cpp`) — 52 outbound dependencies
4. **mode_development.cpp** (`engine/src/mode_development.cpp`) — 49 outbound dependencies
5. **Engine.java** (`engine/src/java/com/runrev/android/Engine.java`) — 49 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `MCFilesExecPerformReadFixedFor` (@ `engine/src/exec-files.cpp`) -> Impact: **1305.3** | LOC: 1363
  * *Intent:* ////////////////////////////////////////////////////////////////////////////////
- `MCObject::handleself` (@ `engine/src/object.cpp`) -> Impact: **1155.3** | LOC: 2106
- `MCDeployToMacOSXMainBody` (@ `engine/src/deploy_macosx.cpp`) -> Impact: **1107.0** | LOC: 1178
  * *Intent:* * local symbols (further grouped by the module they are from) * defined external symbols (further grouped by the module they are from) * undefined sym...
- `MCFilesExecPerformReadCodeUnit` (@ `engine/src/exec-files.cpp`) -> Impact: **1046.3** | LOC: 1247
- `MCObject::exechandler` (@ `engine/src/object.cpp`) -> Impact: **1017.5** | LOC: 2128
  * *Intent:* // MM-2012-09-05: [[ Property Listener ]]
- `MCObject::drawborder` (@ `engine/src/object.cpp`) -> Impact: **928.0** | LOC: 2200
  * *Intent:* // MW-2009-01-29: [[ Bug ]] Cards and stack parentScripts don't work. // This method first looks for a handler for the given message in its own script...
- `MCStringsEvalMatchText` (@ `engine/src/exec-strings.cpp`) -> Impact: **867.2** | LOC: 1417
- `GetResource` (@ `engine/src/dskmac.cpp`) -> Impact: **845.0** | LOC: 1615
- `MCProperty::parse` (@ `engine/src/property.cpp`) -> Impact: **759.0** | LOC: 665
- `__MCStringCantBeEqualToNative` (@ `libfoundation/src/foundation-string.cpp`) -> Impact: **750.2** | LOC: 2083

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `engine/src` | 816 | 351312.44 | 35.42% | 65.02% |
| `ide-support` | 9 | 35503.08 | 86.0% | 27.33% |
| `libfoundation/src` | 59 | 26340.14 | 45.95% | 73.49% |
| `builder` | 16 | 23364.0 | 60.58% | 13.53% |
| `libgraphics/src` | 21 | 10390.32 | 38.07% | 72.02% |
| `libscript/src` | 72 | 10117.0 | 20.94% | 51.56% |
| `libbrowser/src` | 27 | 8301.45 | 29.44% | 45.86% |
| `builder/installer` | 19 | 8282.64 | 87.9% | 6.42% |
| `lcidlc/src` | 24 | 7513.88 | 22.07% | 41.19% |
| `revbrowser/src` | 18 | 6137.82 | 26.35% | 51.47% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `engine/src/mac-menu.mm` -> **100.0%** Exposure
- `engine/src/mac-window.mm` -> **100.0%** Exposure
- `engine/src/mbliphone.mm` -> **100.0%** Exposure
- `engine/src/mbliphoneapp.mm` -> **100.0%** Exposure
- `engine/src/mbliphonedc.mm` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `gyp/gyp_main.py` -> **100.0%** Exposure
- `util/emscripten-genwhitelist.py` -> **100.0%** Exposure
- `util/emscripten-javascriptify.py` -> **100.0%** Exposure
- `engine/src/coretextfonts.mm` -> **100.0%** Exposure
- `engine/src/coretextlayout.mm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `engine/src/exec-interface2.cpp` -> **183** Orphaned Functions | **9** Duplicates
- `engine/src/funcs.h` -> **0** Orphaned Functions | **169** Duplicates
- `engine/src/uidc.cpp` -> **164** Orphaned Functions | **2** Duplicates
- `engine/src/exec-interface-field-chunk.cpp` -> **95** Orphaned Functions | **67** Duplicates
- `engine/src/module-canvas.cpp` -> **143** Orphaned Functions | **17** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`engine/src/coretextfonts.mm`** -> AI Confidence: **99.48%**
2. **`engine/src/externalv1.mm`** -> AI Confidence: **99.48%**
3. **`engine/src/mac-av-player.mm`** -> AI Confidence: **99.48%**
4. **`engine/src/mac-core.mm`** -> AI Confidence: **99.48%**
5. **`engine/src/mac-cursor.mm`** -> AI Confidence: **99.48%**
6. **`engine/src/mac-dialog.mm`** -> AI Confidence: **99.48%**
7. **`engine/src/mac-menu.mm`** -> AI Confidence: **99.48%**
8. **`engine/src/mac-qt-player.mm`** -> AI Confidence: **99.48%**
9. **`engine/src/mac-qt-recorder.mm`** -> AI Confidence: **99.48%**
10. **`engine/src/mac-snapshot.mm`** -> AI Confidence: **99.48%**
11. **`engine/src/mac-surface.mm`** -> AI Confidence: **99.48%**
12. **`engine/src/mac-theme.mm`** -> AI Confidence: **99.48%**
13. **`engine/src/mac-window.mm`** -> AI Confidence: **99.48%**
14. **`engine/src/mbliphone-theme.mm`** -> AI Confidence: **99.48%**
15. **`engine/src/mbliphone.mm`** -> AI Confidence: **99.48%**
16. **`engine/src/mbliphoneactivityindicator.mm`** -> AI Confidence: **99.48%**
17. **`engine/src/mbliphonead.mm`** -> AI Confidence: **99.48%**
18. **`engine/src/mbliphoneapp.mm`** -> AI Confidence: **99.48%**
19. **`engine/src/mbliphonebrowser.mm`** -> AI Confidence: **99.48%**
20. **`engine/src/mbliphonebusyindicator.mm`** -> AI Confidence: **99.48%**
21. **`engine/src/mbliphonecalendar.mm`** -> AI Confidence: **99.48%**
22. **`engine/src/mbliphonecamera.mm`** -> AI Confidence: **99.48%**
23. **`engine/src/mbliphonecontact.mm`** -> AI Confidence: **99.48%**
24. **`engine/src/mbliphonecontrol.mm`** -> AI Confidence: **99.48%**
25. **`engine/src/mbliphonedc.mm`** -> AI Confidence: **99.48%**
26. **`engine/src/mbliphonedialog.mm`** -> AI Confidence: **99.48%**
27. **`engine/src/mbliphoneembedded.mm`** -> AI Confidence: **99.48%**
28. **`engine/src/mbliphoneextra.mm`** -> AI Confidence: **99.48%**
29. **`engine/src/mbliphonefs.mm`** -> AI Confidence: **99.48%**
30. **`engine/src/mbliphonegfx.mm`** -> AI Confidence: **99.48%**
31. **`engine/src/mbliphoneidletimer.mm`** -> AI Confidence: **99.48%**
32. **`engine/src/mbliphoneinput.mm`** -> AI Confidence: **99.48%**
33. **`engine/src/mbliphonemail.mm`** -> AI Confidence: **99.48%**
34. **`engine/src/mbliphonemediapick.mm`** -> AI Confidence: **99.48%**
35. **`engine/src/mbliphonenotification.mm`** -> AI Confidence: **99.48%**
36. **`engine/src/mbliphoneorientation.mm`** -> AI Confidence: **99.48%**
37. **`engine/src/mbliphonepick.mm`** -> AI Confidence: **99.48%**
38. **`engine/src/mbliphonepickdate.mm`** -> AI Confidence: **99.48%**
39. **`engine/src/mbliphoneplayer.mm`** -> AI Confidence: **99.48%**
40. **`engine/src/mbliphonereachability.mm`** -> AI Confidence: **99.48%**
41. **`engine/src/mbliphonescroller.mm`** -> AI Confidence: **99.48%**
42. **`engine/src/mbliphonesensor.mm`** -> AI Confidence: **99.48%**
43. **`engine/src/mbliphonesound.mm`** -> AI Confidence: **99.48%**
44. **`engine/src/mbliphonestack.mm`** -> AI Confidence: **99.48%**
45. **`engine/src/mbliphonestore.mm`** -> AI Confidence: **99.48%**
46. **`engine/src/mbliphonevideo.mm`** -> AI Confidence: **99.48%**
47. **`engine/src/mode_installer_osx.mm`** -> AI Confidence: **99.48%**
48. **`engine/src/native-layer-ios.mm`** -> AI Confidence: **99.48%**
49. **`engine/src/native-layer-mac.mm`** -> AI Confidence: **99.48%**
50. **`engine/src/osxcisupport.mm`** -> AI Confidence: **99.48%**
51. **`engine/src/osxmisc.mm`** -> AI Confidence: **99.48%**
52. **`engine/src/osxtheme.mm`** -> AI Confidence: **99.48%**
53. **`lcidlc/src/Support.mm`** -> AI Confidence: **99.48%**
54. **`libbrowser/src/libbrowser_osx_webview.mm`** -> AI Confidence: **99.48%**
55. **`libbrowser/src/libbrowser_uiwebview.mm`** -> AI Confidence: **99.48%**
56. **`libfoundation/src/foundation-objc.mm`** -> AI Confidence: **99.48%**
57. **`revvideograbber/src/revcapture.mm`** -> AI Confidence: **99.48%**
58. **`engine/src/answer.cpp`** -> AI Confidence: **99.48%**
59. **`engine/src/ask.cpp`** -> AI Confidence: **99.48%**
60. **`engine/src/button.cpp`** -> AI Confidence: **99.48%**
61. **`engine/src/buttondraw.cpp`** -> AI Confidence: **99.48%**
62. **`engine/src/card.cpp`** -> AI Confidence: **99.48%**
63. **`engine/src/cardlst.cpp`** -> AI Confidence: **99.48%**
64. **`engine/src/chunk.cpp`** -> AI Confidence: **99.48%**
65. **`engine/src/cmdss.cpp`** -> AI Confidence: **99.48%**
66. **`engine/src/control.cpp`** -> AI Confidence: **99.48%**
67. **`engine/src/date.cpp`** -> AI Confidence: **99.48%**
68. **`engine/src/debug.cpp`** -> AI Confidence: **99.48%**
69. **`engine/src/deploy_emscripten.cpp`** -> AI Confidence: **99.48%**
70. **`engine/src/deploy_sign.cpp`** -> AI Confidence: **99.48%**
71. **`engine/src/desktop-ans.cpp`** -> AI Confidence: **99.48%**
72. **`engine/src/desktop.cpp`** -> AI Confidence: **99.48%**
73. **`engine/src/em-main.cpp`** -> AI Confidence: **99.48%**
74. **`engine/src/em-osspec-misc.cpp`** -> AI Confidence: **99.48%**
75. **`engine/src/exec-dialog.cpp`** -> AI Confidence: **99.48%**
76. **`engine/src/exec-filters.cpp`** -> AI Confidence: **99.48%**
77. **`engine/src/exec-keywords.cpp`** -> AI Confidence: **99.48%**
78. **`engine/src/exec-mail.cpp`** -> AI Confidence: **99.48%**
79. **`engine/src/field.cpp`** -> AI Confidence: **99.48%**
80. **`engine/src/fieldf.cpp`** -> AI Confidence: **99.48%**
81. **`engine/src/fieldh.cpp`** -> AI Confidence: **99.48%**
82. **`engine/src/fieldhtml.cpp`** -> AI Confidence: **99.48%**
83. **`engine/src/fields.cpp`** -> AI Confidence: **99.48%**
84. **`engine/src/fieldstyledtext.cpp`** -> AI Confidence: **99.48%**
85. **`engine/src/freetype-font.cpp`** -> AI Confidence: **99.48%**
86. **`engine/src/handler.cpp`** -> AI Confidence: **99.48%**
87. **`engine/src/hc.cpp`** -> AI Confidence: **99.48%**
88. **`engine/src/ibmp.cpp`** -> AI Confidence: **99.48%**
89. **`engine/src/ide.cpp`** -> AI Confidence: **99.48%**
90. **`engine/src/ifile.cpp`** -> AI Confidence: **99.48%**
91. **`engine/src/iimport.cpp`** -> AI Confidence: **99.48%**
92. **`engine/src/image.cpp`** -> AI Confidence: **99.48%**
93. **`engine/src/ipng.cpp`** -> AI Confidence: **99.48%**
94. **`engine/src/irle.cpp`** -> AI Confidence: **99.48%**
95. **`engine/src/iutil.cpp`** -> AI Confidence: **99.48%**
96. **`engine/src/keywords.cpp`** -> AI Confidence: **99.48%**
97. **`engine/src/license.cpp`** -> AI Confidence: **99.48%**
98. **`engine/src/linux-theme.cpp`** -> AI Confidence: **99.48%**
99. **`engine/src/lnxcolor.cpp`** -> AI Confidence: **99.48%**
100. **`engine/src/lnxdnd.cpp`** -> AI Confidence: **99.48%**
101. **`engine/src/lnxgtktheme.cpp`** -> AI Confidence: **99.48%**
102. **`engine/src/mblcalendar.cpp`** -> AI Confidence: **99.48%**
103. **`engine/src/mblcontact.cpp`** -> AI Confidence: **99.48%**
104. **`engine/src/operator.cpp`** -> AI Confidence: **99.48%**
105. **`engine/src/osxfield.cpp`** -> AI Confidence: **99.48%**
106. **`engine/src/paragraf.cpp`** -> AI Confidence: **99.48%**
107. **`engine/src/pickle.cpp`** -> AI Confidence: **99.48%**
108. **`engine/src/property.cpp`** -> AI Confidence: **99.48%**
109. **`engine/src/rtf.cpp`** -> AI Confidence: **99.48%**
110. **`engine/src/scrolbar.cpp`** -> AI Confidence: **99.48%**
111. **`engine/src/scrollbardraw.cpp`** -> AI Confidence: **99.48%**
112. **`engine/src/segment.cpp`** -> AI Confidence: **99.48%**
113. **`engine/src/srvoutput.cpp`** -> AI Confidence: **99.48%**
114. **`engine/src/srvscript.cpp`** -> AI Confidence: **99.48%**
115. **`engine/src/stacke.cpp`** -> AI Confidence: **99.48%**
116. **`engine/src/sysw32network.cpp`** -> AI Confidence: **99.48%**
117. **`engine/src/text-simplebreakingengine.cpp`** -> AI Confidence: **99.48%**
118. **`engine/src/util.cpp`** -> AI Confidence: **99.48%**
119. **`engine/src/w32dcw32.cpp`** -> AI Confidence: **99.48%**
120. **`engine/src/w32icon.cpp`** -> AI Confidence: **99.48%**
121. **`engine/src/w32theme.cpp`** -> AI Confidence: **99.48%**
122. **`engine/src/widget.cpp`** -> AI Confidence: **99.48%**
123. **`engine/src/windows-theme.cpp`** -> AI Confidence: **99.48%**
124. **`libfoundation/src/foundation-locale.cpp`** -> AI Confidence: **99.48%**
125. **`revmobile/src/revmobile.cpp`** -> AI Confidence: **99.48%**
126. **`revxml/src/revxml.cpp`** -> AI Confidence: **99.48%**
127. **`revzip/src/revzip.cpp`** -> AI Confidence: **99.48%**
128. **`engine/src/bitmapeffect.cpp`** -> AI Confidence: **99.39%**
129. **`engine/src/block.cpp`** -> AI Confidence: **99.39%**
130. **`engine/src/cmdsf.cpp`** -> AI Confidence: **99.39%**
131. **`engine/src/cmdsm.cpp`** -> AI Confidence: **99.39%**
132. **`engine/src/cmdsp.cpp`** -> AI Confidence: **99.39%**
133. **`engine/src/deploy.cpp`** -> AI Confidence: **99.39%**
134. **`engine/src/deploy_macosx.cpp`** -> AI Confidence: **99.39%**
135. **`engine/src/desktop-menu.cpp`** -> AI Confidence: **99.39%**
136. **`engine/src/dsklnxmain.cpp`** -> AI Confidence: **99.39%**
137. **`engine/src/dskmain.cpp`** -> AI Confidence: **99.39%**
138. **`engine/src/exec-files.cpp`** -> AI Confidence: **99.39%**
139. **`engine/src/exec-pick.cpp`** -> AI Confidence: **99.39%**
140. **`engine/src/exec-sensor.cpp`** -> AI Confidence: **99.39%**
141. **`engine/src/exec.cpp`** -> AI Confidence: **99.39%**
142. **`engine/src/fieldrtf.cpp`** -> AI Confidence: **99.39%**
143. **`engine/src/font.cpp`** -> AI Confidence: **99.39%**
144. **`engine/src/gradient.cpp`** -> AI Confidence: **99.39%**
145. **`engine/src/graphic.cpp`** -> AI Confidence: **99.39%**
146. **`engine/src/group.cpp`** -> AI Confidence: **99.39%**
147. **`engine/src/idraw.cpp`** -> AI Confidence: **99.39%**
148. **`engine/src/igif.cpp`** -> AI Confidence: **99.39%**
149. **`engine/src/image_rep_mutable.cpp`** -> AI Confidence: **99.39%**
150. **`engine/src/image_rep_resampled.cpp`** -> AI Confidence: **99.39%**
151. **`engine/src/iquantization.cpp`** -> AI Confidence: **99.39%**
152. **`engine/src/lnxans.cpp`** -> AI Confidence: **99.39%**
153. **`engine/src/lnxdce.cpp`** -> AI Confidence: **99.39%**
154. **`engine/src/lnxdclnx.cpp`** -> AI Confidence: **99.39%**
155. **`engine/src/lnxgtkthemedrawing.cpp`** -> AI Confidence: **99.39%**
156. **`engine/src/mcio.cpp`** -> AI Confidence: **99.39%**
157. **`engine/src/mcssl.cpp`** -> AI Confidence: **99.39%**
158. **`engine/src/metacontext.cpp`** -> AI Confidence: **99.39%**
159. **`engine/src/mode_test.cpp`** -> AI Confidence: **99.39%**
160. **`engine/src/objectprops.cpp`** -> AI Confidence: **99.39%**
161. **`engine/src/osxcoreimage.cpp`** -> AI Confidence: **99.39%**
162. **`engine/src/osximage.cpp`** -> AI Confidence: **99.39%**
163. **`engine/src/osxprinter.cpp`** -> AI Confidence: **99.39%**
164. **`engine/src/scriptpt.cpp`** -> AI Confidence: **99.39%**
165. **`engine/src/srvmain.cpp`** -> AI Confidence: **99.39%**
166. **`engine/src/srvmultipart.cpp`** -> AI Confidence: **99.39%**
167. **`engine/src/stack.cpp`** -> AI Confidence: **99.39%**
168. **`engine/src/stack3.cpp`** -> AI Confidence: **99.39%**
169. **`engine/src/stacklst.cpp`** -> AI Confidence: **99.39%**
170. **`engine/src/sysspec-url.cpp`** -> AI Confidence: **99.39%**
171. **`engine/src/text-paragraph.cpp`** -> AI Confidence: **99.39%**
172. **`engine/src/text-segment.cpp`** -> AI Confidence: **99.39%**
173. **`engine/src/visual.cpp`** -> AI Confidence: **99.39%**
174. **`engine/src/w32color.cpp`** -> AI Confidence: **99.39%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `39` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10712` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `engine/src/java/com/runrev/android/NetworkModule.java` (JAVA) -> Cumulative Risk: **733.65**
- **Archetype:** `file_cluster_4` (Distance: 11.569 IQR)
- **Magnitude:** 186.92 | **LOC:** 247 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9979%), Concurrency (99.8756%), State Flux (99.0442%)
- **Heaviest Functions:** `getNetworkInterfaces` (Impact: 15.5), `postURL` (Impact: 14.9), `putURL` (Impact: 12.6)

### 2. `engine/src/em-liburl.js` (JAVASCRIPT) -> Cumulative Risk: **713.62**
- **Archetype:** `file_cluster_4` (Distance: 15.151 IQR)
- **Magnitude:** 287.34 | **LOC:** 277 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9655%), Tech Debt (99.6948%)
- **Heaviest Functions:** `mergeInto` (Impact: 70.9), `requestSend` (Impact: 16.6), `requestCreate` (Impact: 11.9)

### 3. `engine/src/java/com/runrev/android/nativecontrol/InputControl.java` (JAVA) -> Cumulative Risk: **657.18**
- **Archetype:** `file_cluster_8` (Distance: 11.412 IQR)
- **Magnitude:** 253.2 | **LOC:** 333 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9788%), Documentation (98.7781%)
- **Heaviest Functions:** `setIsPassword` (Impact: 9.7), `setScrollingEnabled` (Impact: 9.5), `createView` (Impact: 9.2)

### 4. `engine/src/java/com/runrev/android/DialogModule.java` (JAVA) -> Cumulative Risk: **636.87**
- **Archetype:** `file_cluster_8` (Distance: 11.019 IQR)
- **Magnitude:** 244.98 | **LOC:** 297 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9657%), Safety Score (89.3906%)
- **Heaviest Functions:** `showListPicker` (Impact: 45.6), `showAnswerDialog` (Impact: 18.9), `showDatePicker` (Impact: 18.2)

### 5. `toolchain/lc-compile/src/operator.c` (C) -> Cumulative Risk: **632.88**
- **Archetype:** `file_cluster_13` (Distance: 13.598 IQR)
- **Magnitude:** 335.48 | **LOC:** 504 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.4452%), Safety Score (90.9345%)
- **Heaviest Functions:** `CompareNodePrecedence` (Impact: 24.1), `ReorderOperatorExpression` (Impact: 20.4), `DivideNodeListAt` (Impact: 5.2)

### 6. `engine/src/java/com/runrev/android/nativecontrol/VideoControl.java` (JAVA) -> Cumulative Risk: **629.73**
- **Archetype:** `file_cluster_8` (Distance: 10.586 IQR)
- **Magnitude:** 224.56 | **LOC:** 296 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9933%), Documentation (99.8897%), State Flux (99.5899%)
- **Heaviest Functions:** `setFile` (Impact: 10.2), `createView` (Impact: 8.4), `setShowController` (Impact: 7.2)

### 7. `toolchain/libcompile/src/position.c` (C) -> Cumulative Risk: **622.36**
- **Archetype:** `file_cluster_13` (Distance: 13.992 IQR)
- **Magnitude:** 399.86 | **LOC:** 404 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (98.2828%), Safety Score (93.6456%)
- **Heaviest Functions:** `__InitializeFileLines` (Impact: 22.6), `AddFile` (Impact: 19.9), `__FindNextSeparator` (Impact: 14.3)

### 8. `engine/src/java/com/runrev/android/AdModule.java` (JAVA) -> Cumulative Risk: **620.98**
- **Archetype:** `file_cluster_8` (Distance: 10.476 IQR)
- **Magnitude:** 210.82 | **LOC:** 297 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.9284%), State Flux (95.7241%), Safety Score (86.431%)
- **Heaviest Functions:** `InneractiveAdWrapper` (Impact: 45.7), `getIAdType` (Impact: 24.7), `setVisible` (Impact: 7.2)

### 9. `libfoundation/include/foundation-span.h` (CPP) -> Cumulative Risk: **620.6**
- **Archetype:** `file_cluster_8` (Distance: 12.781 IQR)
- **Magnitude:** 370.46 | **LOC:** 473 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (95.8061%)
- **Heaviest Functions:** `MCSpanIterator` (Impact: 7.5), `subspan` (Impact: 6.5), `operator==` (Impact: 3.7)

### 10. `engine/src/java/com/runrev/android/URLLoader.java` (JAVA) -> Cumulative Risk: **619.47**
- **Archetype:** `file_cluster_8` (Distance: 11.478 IQR)
- **Magnitude:** 246.58 | **LOC:** 337 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6722%), Tech Debt (99.3513%), Safety Score (86.1776%)
- **Heaviest Functions:** `run` (Impact: 48.1), `setMethod` (Impact: 16.9), `setHeaders` (Impact: 16.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ide-support/revsaveasandroidstandalone.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.245 IQR)
- **Top Global Matches:** file_cluster_17: 14.245, file_cluster_4: 14.67, file_cluster_11: 14.77
- **Magnitude:** 12386.08 | **LOC:** 2184 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.2074%), Tech Debt (19.3591%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1059`, `structural_boundaries: 556`, `func_start: 54`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 885`, `dead_code: 29`, `fragile_debt: 11`
* *Architecture:* `io: 17`, `api: 10`, `concurrency: 31`, `import: 2`
* *Defense:* `safety: 102`, `doc: 2`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/object.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.556 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_13: 15.556, file_cluster_8: 15.583, file_cluster_7: 15.688
- **Magnitude:** 7681.12 | **LOC:** 5885 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.6703%), Tech Debt (99.9676%)
**Top Internal Functions/Classes:**
  * `MCObject::handleself` (Impact: 1155.3)
  * `MCObject::exechandler` (Impact: 1017.5)
    * *Intent:* // MM-2012-09-05: [[ Property Listener ]]
  * `MCObject::drawborder` (Impact: 928.0)
    * *Intent:* // MW-2009-01-29: [[ Bug ]] Cards and stack parentScripts don't work. // This method first looks for...
  * `MCObject::resolveparentscript` (Impact: 316.7)
  * `MCObject::setforeground` (Impact: 253.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 680`, `structural_boundaries: 304`, `args: 179`, `func_start: 143`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2479`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 23`, `duplicate_logic: 6`, `orphaned_logic: 122`
* *Architecture:* `io: 2`, `import: 51`
* *Defense:* `safety: 1`, `doc: 260`, `immutability_locks: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 51):` license.h, resolution.h, parentscript.h, osspec.h, globdefs.h, widget.h, eps.h, graphic.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revsaveasstandalone.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.555 IQR)
- **Top Global Matches:** file_cluster_17: 13.555, file_cluster_0: 14.275, file_cluster_11: 14.275
- **Magnitude:** 6586.56 | **LOC:** 2675 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.4284%), Tech Debt (63.4024%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 560`, `structural_boundaries: 256`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 8`, `state_mutation: 531`, `dead_code: 14`, `fragile_debt: 16`
* *Architecture:* `io: 4`, `api: 9`, `concurrency: 6`
* *Defense:* `safety: 26`, `sync_locks: 6`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pStack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/installer_utilities.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.082 IQR)
- **Top Global Matches:** file_cluster_17: 12.082, file_cluster_8: 12.217, file_cluster_4: 12.385
- **Magnitude:** 6101.08 | **LOC:** 1626 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.1494%), Tech Debt (10.359%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 537`, `structural_boundaries: 202`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 9`, `state_mutation: 287`, `dead_code: 6`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 7`, `concurrency: 9`
* *Defense:* `safety: 16`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/dskmac.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.106 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.01 IQR)
- **Top Global Matches:** file_cluster_13: 15.106, file_cluster_8: 15.11, file_cluster_7: 15.207
- **Magnitude:** 5963.74 | **LOC:** 6008 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.3566%), Tech Debt (98.3781%)
**Top Internal Functions/Classes:**
  * `GetResource` (Impact: 845.0)
  * `RequestAE` (Impact: 690.1)
  * `TextConvertToUnicode` (Impact: 656.8)
  * `SetResource` (Impact: 122.5)
  * `MCS_startprocess_unix` (Impact: 105.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 291`, `args: 155`, `func_start: 87`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 4`, `state_mutation: 2450`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 31`, `duplicate_logic: 4`, `orphaned_logic: 59`
* *Architecture:* `io: 12`, `api: 2`, `import: 37`
* *Defense:* `safety: 1`, `doc: 240`, `sync_locks: 24`, `immutability_locks: 16`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` AuthorizationTags.h, pwd.h, securemode.h, osspec.h, globdefs.h, ioctl.h, CoreFoundation.h, dispatch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revdocsparser.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.903 IQR)
- **Top Global Matches:** file_cluster_17: 13.903, file_cluster_8: 14.248, file_cluster_11: 14.299
- **Magnitude:** 5249.08 | **LOC:** 2938 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.2225%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 310`, `func_start: 26`
* *Risk/State:* `state_mutation: 739`, `dead_code: 11`
* *Architecture:* `api: 25`
* *Defense:* `safety: 2`, `doc: 9`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec-files.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.127 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 3.822 IQR)
- **Top Global Matches:** file_cluster_8: 15.127, file_cluster_7: 15.153, file_cluster_13: 15.284
- **Magnitude:** 5171.14 | **LOC:** 2769 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.5289%), Tech Debt (99.9457%)
**Top Internal Functions/Classes:**
  * `MCFilesExecPerformReadFixedFor` (Impact: 1305.3)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCFilesExecPerformReadCodeUnit` (Impact: 1046.3)
  * `MCFilesExecWriteToStream` (Impact: 165.1)
  * `MCFilesExecPerformReadTextUntil` (Impact: 143.2)
  * `MCFilesExecPerformReadChunk` (Impact: 109.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 492`, `structural_boundaries: 202`, `args: 169`, `func_start: 110`
* *Risk/State:* `state_mutation: 1339`, `fragile_debt: 13`, `duplicate_logic: 8`, `orphaned_logic: 76`
* *Architecture:* `import: 14`
* *Defense:* `doc: 630`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` objdefs.h, mcerror.h, parsedef.h, prefix.h, mcio.h, util.h, securemode.h, uidc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/widgets/androidfield/androidfield.lcb` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.554 IQR)
- **Top Global Matches:** file_cluster_2: 11.554, file_cluster_8: 11.675, file_cluster_17: 11.684
- **Magnitude:** 4989.2 | **LOC:** 1809 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.8173%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 365`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 374`, `dead_code: 9`
* *Architecture:* `api: 6`
* *Defense:* `safety: 10`, `doc: 44`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/mblhandlers.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.759 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.211 IQR)
- **Top Global Matches:** file_cluster_8: 14.759, file_cluster_7: 14.918, file_cluster_13: 15.002
- **Magnitude:** 4809.24 | **LOC:** 4981 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.0804%), Tech Debt (41.0665%)
**Top Internal Functions/Classes:**
  * `MCHandlePick` (Impact: 61.1)
  * `MCHandlePickDate` (Impact: 56.5)
  * `MCHandleSensorReading` (Impact: 54.7)
  * `MCHandleSetFullScreenRectForOrientations` (Impact: 49.2)
  * `MCMediaTypeFromString` (Impact: 46.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 785`, `structural_boundaries: 605`, `args: 207`, `func_start: 192`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 192`, `state_mutation: 2828`, `dead_code: 3`, `fragile_debt: 26`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `import: 18`
* *Defense:* `doc: 428`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` objdefs.h, prefix.h, parsedef.h, param.h, mcio.h, mblsyntax.h, util.h, foundation-chunk.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.715 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.235 IQR)
- **Top Global Matches:** file_cluster_8: 14.715, file_cluster_13: 14.854, file_cluster_7: 14.914
- **Magnitude:** 4694.12 | **LOC:** 3772 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.5183%), Tech Debt (94.4163%)
**Top Internal Functions/Classes:**
  * `MCExecContext::ConvertToLegacyRectangle` (Impact: 715.0)
  * `MCExecFetchProperty` (Impact: 569.4)
  * `MCExecStoreProperty` (Impact: 447.5)
  * `MCExecTypeConvertToValueRefAndReleaseAlw` (Impact: 94.9)
  * `MCExecTypeConvertNumbers` (Impact: 93.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 773`, `structural_boundaries: 288`, `args: 79`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 99`, `state_mutation: 2056`, `planned_debt: 1`, `fragile_debt: 22`, `duplicate_logic: 4`, `orphaned_logic: 34`
* *Architecture:* `import: 25`
* *Defense:* `doc: 104`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` license.h, securemode.h, osspec.h, globdefs.h, scriptpt.h, variable.h, parsedef.h, param.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec-interface.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_7` (Drift: 15.828 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.658 IQR)
- **Top Global Matches:** file_cluster_7: 15.828, file_cluster_8: 15.838, file_cluster_13: 15.861
- **Magnitude:** 4238.64 | **LOC:** 4643 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.8622%), Tech Debt (99.9948%)
**Top Internal Functions/Classes:**
  * `MCInterfaceExecDrawerOrSheetStack` (Impact: 599.7)
  * `MCInterfaceExecExportImageToFile` (Impact: 171.1)
  * `MCInterfaceProcessToContainer` (Impact: 112.5)
  * `MCInterfaceExecClone` (Impact: 66.6)
    * *Intent:* // MW-2011-11-15: [[ Bug 9846 ]] Lock the screen to prevent the snapshot
  * `MCInterfaceExecResetTemplate` (Impact: 51.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 557`, `structural_boundaries: 332`, `args: 337`, `func_start: 180`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 5`, `state_mutation: 1888`, `planned_debt: 1`, `fragile_debt: 31`, `duplicate_logic: 4`, `orphaned_logic: 153`
* *Architecture:* `import: 43`
* *Defense:* `doc: 1245`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` eps.h, globdefs.h, graphic.h, widget.h, osspec.h, dispatch.h, scriptpt.h, variable.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libfoundation/src/foundation-string.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.778 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.624 IQR)
- **Top Global Matches:** file_cluster_8: 14.778, file_cluster_7: 14.826, file_cluster_13: 14.913
- **Magnitude:** 4203.82 | **LOC:** 7360 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.5355%), Tech Debt (91.7269%)
**Top Internal Functions/Classes:**
  * `__MCStringCantBeEqualToNative` (Impact: 750.2)
  * `MCStringFormatV` (Impact: 716.2)
  * `MCStringMapCodepointIndices` (Impact: 340.4)
  * `__MCStringExpandAt` (Impact: 102.5)
  * `MCStringCreateWithBytes` (Impact: 96.8)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// #include "foundatio...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 435`, `structural_boundaries: 222`, `args: 107`, `func_start: 84`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 1368`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 11`, `orphaned_logic: 45`
* *Architecture:* `import: 11`
* *Defense:* `doc: 416`, `immutability_locks: 45`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` locale.h, iconv.h, langinfo.h, foundation-bidi.h, foundation-string-native.cpp.h, Windows.h, foundation-chunk.h, foundation-unicode.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec-strings.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.373 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.354 IQR)
- **Top Global Matches:** file_cluster_8: 15.373, file_cluster_13: 15.378, file_cluster_7: 15.39
- **Magnitude:** 4076.88 | **LOC:** 2638 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.1882%), Tech Debt (99.3642%)
**Top Internal Functions/Classes:**
  * `MCStringsEvalMatchText` (Impact: 867.2)
  * `MCStringsEvalFormat` (Impact: 749.2)
  * `MCStringsExecSort` (Impact: 209.7)
    * *Intent:* // We have just skipped a delimiter (the 'after' one) so increment
  * `MCStringsDoSort` (Impact: 107.6)
  * `MCStringsExecFilterDelimited` (Impact: 37.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 375`, `structural_boundaries: 162`, `args: 106`, `func_start: 82`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 1628`, `dead_code: 3`, `fragile_debt: 18`, `duplicate_logic: 2`, `orphaned_logic: 48`
* *Architecture:* `import: 20`
* *Defense:* `doc: 419`, `sync_locks: 2`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` osspec.h, globdefs.h, scriptpt.h, exec-strings.h, variable.h, parsedef.h, util.h, filedefs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/module-canvas.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.385 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.644 IQR)
- **Top Global Matches:** file_cluster_8: 14.385, file_cluster_7: 14.527, file_cluster_13: 14.691
- **Magnitude:** 3958.04 | **LOC:** 7185 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.5101%), Tech Debt (99.9077%)
**Top Internal Functions/Classes:**
  * `MCProperListGetNumberAtIndex` (Impact: 517.2)
  * `MCSVGParseParams` (Impact: 89.7)
  * `MCCanvasEffectMakeWithPropertyArray` (Impact: 82.7)
  * `MCSVGParse` (Impact: 72.3)
  * `MCGPathToSVGDataCallback` (Impact: 47.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 447`, `structural_boundaries: 439`, `args: 332`, `func_start: 255`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 1888`, `dead_code: 3`, `planned_debt: 18`, `fragile_debt: 1`, `duplicate_logic: 17`, `orphaned_logic: 143`
* *Architecture:* `import: 7`
* *Defense:* `doc: 374`, `sync_locks: 1`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` prefix.h, module-canvas.h, image.h, widget.h, module-engine.h, module-canvas-internal.h, stack.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/paragraf.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.761 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.698 IQR)
- **Top Global Matches:** file_cluster_8: 14.761, file_cluster_13: 14.924, file_cluster_11: 14.996
- **Magnitude:** 3636.08 | **LOC:** 4022 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.278%), Tech Debt (99.9752%)
**Top Internal Functions/Classes:**
  * `MCParagraph::fillselect` (Impact: 469.3)
  * `MCParagraph::setfocus` (Impact: 176.2)
  * `MCParagraph::draw` (Impact: 138.4)
  * `MCParagraph::fmovefocus` (Impact: 128.6)
  * `MCParagraph::load` (Impact: 73.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 566`, `structural_boundaries: 103`, `args: 73`, `func_start: 43`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2116`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 57`, `duplicate_logic: 2`, `orphaned_logic: 40`
* *Architecture:* `import: 20`
* *Defense:* `safety: 2`, `immutability_locks: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` globdefs.h, context.h, exec-interface.h, parsedef.h, util.h, filedefs.h, line.h, stackfileformat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/dskw32.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.191 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.445 IQR)
- **Top Global Matches:** file_cluster_13: 15.191, file_cluster_8: 15.261, file_cluster_7: 15.303
- **Magnitude:** 3592.92 | **LOC:** 3889 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.6163%), Tech Debt (98.4578%)
**Top Internal Functions/Classes:**
  * `GetEnv` (Impact: 349.7)
  * `StartElevatedProcess` (Impact: 108.4)
    * *Intent:* // SN-2015-04-13: [[ Bug 14696 ]] We don't want to leave a
  * `MCS_windows_elevation_bootstrap_main` (Impact: 86.6)
    * *Intent:* // Check that the path was successfully copied
  * `QueryRegistry` (Impact: 85.2)
  * `GetStandardFolder` (Impact: 82.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 481`, `structural_boundaries: 321`, `args: 218`, `func_start: 92`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 7`, `state_mutation: 1969`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 16`, `duplicate_logic: 6`, `orphaned_logic: 61`
* *Architecture:* `io: 1`, `api: 1`, `import: 44`
* *Defense:* `doc: 453`, `sync_locks: 29`, `immutability_locks: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` sys\Timeb.h, signal.h, time.h, io.h, securemode.h, osspec.h, globdefs.h, dispatch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/hc.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.06 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.036 IQR)
- **Top Global Matches:** file_cluster_8: 15.06, file_cluster_13: 15.305, file_cluster_7: 15.422
- **Magnitude:** 3580.12 | **LOC:** 2515 | **CtrlFlow:** 86.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.4618%), Tech Debt (54.7644%)
**Top Internal Functions/Classes:**
  * `MCHcstak::read` (Impact: 198.3)
  * `convert_hcbitmap_data` (Impact: 102.9)
    * *Intent:* // Turn the current MChcstat stringref into a mutable stringref
  * `MCHccard::parse` (Impact: 40.4)
  * `MCHcbkgd::parse` (Impact: 40.2)
  * `MCHctext::parse` (Impact: 16.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 83`, `args: 44`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 3012`, `fragile_debt: 13`, `orphaned_logic: 22`
* *Architecture:* `import: 23`
* *Defense:* `sync_locks: 1`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` objptr.h, hc.h, globdefs.h, font.h, exec-interface.h, card.h, parsedef.h, util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/ibmp.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.726 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.74 IQR)
- **Top Global Matches:** file_cluster_8: 15.726, file_cluster_7: 15.836, file_cluster_13: 15.873
- **Magnitude:** 3532.46 | **LOC:** 2975 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.4437%), Tech Debt (89.2982%)
**Top Internal Functions/Classes:**
  * `bmp_read_dib_header` (Impact: 87.6)
  * `bmp_read_rle4_image` (Impact: 84.4)
    * *Intent:* *t_dst_ptr++ = MCGPixelPackNative(t_color[2], t_color[1], t_color[0], 255);
  * `MCBitmapConvertRow` (Impact: 77.3)
  * `bmp_read_rle8_image` (Impact: 75.7)
  * `MCXWDImageLoader::LoadFrames` (Impact: 66.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 375`, `structural_boundaries: 94`, `args: 69`, `func_start: 50`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2486`, `planned_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 20`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `doc: 234`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` objdefs.h, parsedef.h, prefix.h, mcio.h, imageloader.h, util.h, image.h, filedefs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/deploy_macosx.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_12` (Drift: 15.43 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.669 IQR)
- **Top Global Matches:** file_cluster_12: 15.43, file_cluster_13: 15.479, file_cluster_8: 15.487
- **Magnitude:** 3306.94 | **LOC:** 2903 | **CtrlFlow:** 77.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.7497%), Tech Debt (43.0688%)
**Top Internal Functions/Classes:**
  * `MCDeployToMacOSXMainBody` (Impact: 1107.0)
    * *Intent:* * local symbols (further grouped by the module they are from) * defined external symbols (further gr...
  * `MCDeployForEachMacOSXArchitecture` (Impact: 232.9)
  * `MCDeployToMacOSX` (Impact: 79.8)
  * `swap_load_command` (Impact: 54.3)
    * *Intent:* /* * The 64-bit segment load command indicates that a part of this file is to be * mapped into a 64-...
  * `MCDeployExtractArchCallbackBody` (Impact: 41.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 386`, `structural_boundaries: 111`, `args: 38`, `func_start: 35`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1512`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 8`, `orphaned_logic: 5`
* *Architecture:* `import: 12`
* *Defense:* `doc: 208`, `sync_locks: 5`, `immutability_locks: 21`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` objdefs.h, parsedef.h, prefix.h, handler.h, deploy.h, statemnt.h, filedefs.h, uuid.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec-interface-object.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.456 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.5 IQR)
- **Top Global Matches:** file_cluster_8: 14.456, file_cluster_7: 14.597, file_cluster_13: 14.609
- **Magnitude:** 3255.02 | **LOC:** 4865 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.6627%), Tech Debt (99.3494%)
**Top Internal Functions/Classes:**
  * `MCObject::GetColor` (Impact: 461.4)
  * `MCObject::SetTextFont` (Impact: 161.2)
  * `MCObject::SetProperties` (Impact: 160.2)
  * `MCObjectListAppendObjectAndBehaviors` (Impact: 104.3)
  * `MCObject::DoGetProperties` (Impact: 94.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 188`, `args: 167`, `func_start: 108`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1540`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 15`, `orphaned_logic: 95`
* *Architecture:* `import: 34`
* *Defense:* `doc: 264`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` license.h, objptr.h, parentscript.h, globdefs.h, dispatch.h, object.h, scriptpt.h, font.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/builder_utilities.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.441 IQR)
- **Top Global Matches:** file_cluster_8: 11.441, file_cluster_17: 11.507, file_cluster_4: 11.598
- **Magnitude:** 3211.32 | **LOC:** 894 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.615%), Tech Debt (9.7353%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 199`, `func_start: 81`
* *Risk/State:* `state_mutation: 167`, `planned_debt: 1`
* *Architecture:* `io: 8`, `api: 74`, `concurrency: 27`, `import: 1`
* *Defense:* `safety: 12`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` (builderSystemFolder()
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/ide.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.354 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.538 IQR)
- **Top Global Matches:** file_cluster_13: 15.354, file_cluster_8: 15.385, file_cluster_7: 15.47
- **Magnitude:** 3208.44 | **LOC:** 2631 | **CtrlFlow:** 79.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.4009%), Tech Debt (79.7255%)
**Top Internal Functions/Classes:**
  * `tokenize_stringref` (Impact: 246.0)
  * `tokenize` (Impact: 243.3)
  * `OnObject` (Impact: 92.1)
  * `match_comment` (Impact: 80.9)
  * `match_comment_stringref` (Impact: 76.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 494`, `structural_boundaries: 125`, `args: 125`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 4`, `state_mutation: 1886`, `dead_code: 3`, `fragile_debt: 3`, `duplicate_logic: 2`, `orphaned_logic: 33`
* *Architecture:* `api: 1`, `import: 33`
* *Defense:* `doc: 261`, `sync_locks: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` parentscript.h, graphic.h, globdefs.h, osspec.h, dispatch.h, scriptpt.h, object.h, variable.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revdeploylibraryandroid.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.133 IQR)
- **Top Global Matches:** file_cluster_8: 12.133, file_cluster_17: 12.258, file_cluster_4: 12.479
- **Magnitude:** 3180.6 | **LOC:** 626 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.3594%), Tech Debt (21.3815%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 179`, `func_start: 40`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 264`, `fragile_debt: 3`
* *Architecture:* `api: 31`, `concurrency: 6`
* *Defense:* `safety: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/tools_builder.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.804 IQR)
- **Top Global Matches:** file_cluster_17: 12.804, file_cluster_8: 13.34, file_cluster_0: 13.362
- **Magnitude:** 3151.64 | **LOC:** 978 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.5467%), Tech Debt (10.238%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 154`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 240`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 5`, `import: 1`
* *Defense:* `safety: 29`, `doc: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` (builderRepoFolder()
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/w32theme.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.101 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.747 IQR)
- **Top Global Matches:** file_cluster_8: 15.101, file_cluster_13: 15.187, file_cluster_7: 15.245
- **Magnitude:** 3046.26 | **LOC:** 1990 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.7641%), Tech Debt (78.8243%)
**Top Internal Functions/Classes:**
  * `MCNativeTheme::GetThemePartAndState` (Impact: 433.6)
  * `MCNativeTheme::GetTheme` (Impact: 127.6)
  * `MCNativeTheme::getwidgetrect` (Impact: 95.0)
  * `MCNativeTheme::getscrollbarrects` (Impact: 72.5)
  * `MCNativeTheme::drawscrollcontrols` (Impact: 69.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 530`, `structural_boundaries: 119`, `args: 88`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 3`, `state_mutation: 1875`, `dead_code: 2`, `fragile_debt: 7`, `orphaned_logic: 29`
* *Architecture:* `import: 17`
* *Defense:* `doc: 130`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` objdefs.h, w32theme.h, uxtheme.h, mctheme.h, parsedef.h, prefix.h, w32dc.h, util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/lcs/core/engine/message-box.livecodescript` (LIVECODE) | Magnitude: 31.76 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 28, structural_boundaries: 21, state_mutation: 12, func_start: 4
- `util/weak_stub_maker.pl` (PERL) | Magnitude: 271.64 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 260, state_mutation: 195, structural_boundaries: 98, branch: 78
- `revmobile/src/CoreSimulator.h` (OBJECTIVE-C) | Magnitude: 102.3 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: explicit_casts: 443, safety_bypasses: 241, pointers: 241, args: 224
- `engine/rsrc/emscripten-html-template.html` (HTML) | Magnitude: 84.5 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 182, state_mutation: 31, structural_boundaries: 25, branch: 22
- `revmobile/src/DVTiPhoneSimulatorRemoteClient.h` (OBJECTIVE-C) | Magnitude: 83.78 | Delta: **0.234 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: explicit_casts: 246, pointers: 137, safety_bypasses: 135, func_start: 120

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `engine/src/bsdiff_build.cpp` (CPP) | Magnitude: 955.54 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 690, indent_tabs: 250, branch: 108, doc: 52
- `libfoundation/src/foundation-hash.h` (CPP) | Magnitude: 97.94 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 61, indent_spaces: 56, structural_boundaries: 44, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `engine/src/test.h` (CPP) | Magnitude: 33.68 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 18, pointers: 15, args: 13, macros: 13
- `engine/src/deploy_windows.cpp` (CPP) | Magnitude: 1269.7 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 692, indent_tabs: 419, indent_spaces: 228, branch: 133
- `engine/src/deploy_macosx.cpp` (CPP) | Magnitude: 3306.94 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 1512, indent_tabs: 807, branch: 386, pointers: 234
- `engine/src/deploysecurity.h` (CPP) | Magnitude: 13.08 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 52, macros: 2, pointers: 2, structural_boundaries: 1
- `engine/src/shacommon.h` (CPP) | Magnitude: 56.1 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 42, structural_boundaries: 19, macros: 17, reflection_metaprogramming: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `engine/src/mac-sound.mm` (OBJECTIVE-C) | Magnitude: 236.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 133, state_mutation: 108, doc: 104, branch: 43
- `engine/src/securemode.cpp` (CPP) | Magnitude: 73.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 44, state_mutation: 29, structural_boundaries: 28, args: 14
- `libfoundation/src/foundation-unicode.cpp` (CPP) | Magnitude: 1060.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 566, state_mutation: 393, branch: 169, doc: 156
- `libfoundation/include/system-stream.h` (CPP) | Magnitude: 19.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 6, state_mutation: 4, macros: 4, structural_boundaries: 3
- `engine/src/dskmac.cpp` (CPP) | Magnitude: 5963.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 2450, indent_spaces: 1459, indent_tabs: 945, branch: 549

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `engine/src/java/com/runrev/android/Contact.java` (JAVA) | Magnitude: 437.98 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 467, branch: 111, structural_boundaries: 106, indent_spaces: 87
- `engine/src/java/com/runrev/android/billing/google/Inventory.java` (JAVA) | Magnitude: 50.34 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 22, args: 12, func_start: 12
- `engine/src/rawarray.h` (CPP) | Magnitude: 28.36 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 52, structural_boundaries: 47, indent_tabs: 36, args: 27
- `libcore/include/thunk.h` (CPP) | Magnitude: 26.9 | Delta: **0.324 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 69, doc: 61, args: 16, state_mutation: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/lcs/core/graphics/graphics.livecodescript` (LIVECODE) | Magnitude: 691.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 93, branch: 55, structural_boundaries: 26, explicit_casts: 26
- `tests/_compilertestrunnerbehavior.livecodescript` (LIVECODE) | Magnitude: 1427.88 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 196, state_mutation: 145, branch: 114, structural_boundaries: 85
- `builder/installer/uninstalleruistackbehavior.livecodescript` (LIVECODE) | Magnitude: 448.68 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 62, branch: 36, structural_boundaries: 28, state_mutation: 25
- `tests/lcs/core/engine/extension.livecodescript` (LIVECODE) | Magnitude: 287.96 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, branch: 22, state_mutation: 12, structural_boundaries: 9
- `extensions/widgets/paletteactions/tests/basic.livecodescript` (LIVECODE) | Magnitude: 68.4 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 15, state_mutation: 6, ui_framework: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/lcs/core/field/lineIndent.livecodescript` (LIVECODE) | Magnitude: 41.76 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: ui_framework: 8, structural_boundaries: 4, state_mutation: 4, indent_spaces: 4
- `tests/lcs/core/engine/engine.livecodescript` (LIVECODE) | Magnitude: 1104.52 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 92, state_mutation: 83, ui_framework: 82, branch: 78
- `tests/lcs/core/field/listStyle.livecodescript` (LIVECODE) | Magnitude: 50.36 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: ui_framework: 12, state_mutation: 10, structural_boundaries: 9, indent_spaces: 4
- `tests/lcs/core/field/textAlign.livecodescript` (LIVECODE) | Magnitude: 48.84 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: ui_framework: 12, state_mutation: 9, structural_boundaries: 8, indent_spaces: 4
- `extensions/widgets/segmented/tests/properties.livecodescript` (LIVECODE) | Magnitude: 17.3 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 4, ui_framework: 4, globals: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `builder/installer/installeruiconfirmcardbehavior.livecodescript` (LIVECODE) | Magnitude: 357.52 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 46, state_mutation: 35, structural_boundaries: 33, branch: 28
- `engine/src/java/com/runrev/android/NetworkModule.java` (JAVA) | Magnitude: 186.92 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 126, indent_spaces: 63, structural_boundaries: 46, state_mutation: 40
- `tests/lcs/core/chunks/widget.livecodescript` (LIVECODE) | Magnitude: 22.68 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: concurrency: 6, indent_tabs: 6, structural_boundaries: 4, ui_framework: 4
- `builder/installer/installeruiwaitcardbehavior.livecodescript` (LIVECODE) | Magnitude: 485.88 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 77, branch: 38, structural_boundaries: 36, state_mutation: 24
- `tests/_testrunnerbehavior.livecodescript` (LIVECODE) | Magnitude: 1400.24 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 204, state_mutation: 117, branch: 111, structural_boundaries: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `engine/src/mixin-refcounted.h` (CPP) | Magnitude: 45.12 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 20, state_mutation: 16, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `engine/src/capsule.h` (CPP) | Magnitude: 18.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 70, indent_tabs: 11, args: 8, structural_boundaries: 7
- `libgraphics/include/graphics.h` (CPP) | Magnitude: 817.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 526, doc: 500, indent_tabs: 311, structural_boundaries: 306
- `libfoundation/src/foundation-chunk.cpp` (CPP) | Magnitude: 772.64 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 448, state_mutation: 423, doc: 286, branch: 161
- `engine/src/minizip.h` (CPP) | Magnitude: 19.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 78, indent_tabs: 17, structural_boundaries: 15, pointers: 10
- `lcidlc/src/Value.h` (CPP) | Magnitude: 19.84 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 130, args: 25, pointers: 12, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `libfoundation/include/foundation-objc.h` (OBJECTIVE-C) | Magnitude: 29.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 7, args: 3, func_start: 3, import: 3
- `engine/src/lnxdclnx.cpp` (CPP) | Magnitude: 742.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 428, indent_spaces: 365, branch: 155, pointers: 146
- `engine/src/objectpropsets.cpp` (CPP) | Magnitude: 601.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 351, indent_tabs: 267, doc: 113, branch: 91
- `revvideograbber/src/dsvideograbber.h` (CPP) | Magnitude: 85.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 153, structural_boundaries: 75, args: 51, state_mutation: 39
- `engine/src/cmds.cpp` (CPP) | Magnitude: 548.8 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 385, state_mutation: 227, branch: 120, pointers: 104

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `revmobile/src/reviphoneproxy.mm` (OBJECTIVE-C) | Magnitude: 252.44 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 142, indent_tabs: 97, doc: 78, indent_spaces: 69
- `libfoundation/include/system-error.h` (CPP) | Magnitude: 14.12 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 6, structural_boundaries: 3, args: 3, macros: 2
- `engine/src/raw-clipboard.h` (CPP) | Magnitude: 36.22 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 24, state_mutation: 19, immutability_locks: 15
- `extensions/libraries/timezone/tz/Makefile` (MAKEFILE) | Magnitude: 941.92 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 190, structural_boundaries: 145, io: 70, branch: 66
- `engine/src/mcsemaphore.h` (CPP) | Magnitude: 64.42 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 61, state_mutation: 33, macros: 12, structural_boundaries: 11

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `engine/src/globals.h` -> **Severity: 0.107** (Bridge: 0.0025 * Flux: 43.7406%)
- `engine/src/object.h` -> **Severity: 0.059** (Bridge: 0.0006 * Flux: 99.9474%)
- `libfoundation/include/foundation-auto.h` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 99.9981%)
- `engine/src/sysdefs.h` -> **Severity: 0.028** (Bridge: 0.002 * Flux: 14.2514%)
- `engine/src/image.h` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libfoundation/include/foundation-span.h` -> **Severity: 1419.321** (Blast Radius: 23.703 * Doc Risk: 59.8794%)
- `libfoundation/include/foundation-auto.h` -> **Severity: 324.804** (Blast Radius: 27.248 * Doc Risk: 11.9203%)
- `engine/src/object.h` -> **Severity: 231.981** (Blast Radius: 19.461 * Doc Risk: 11.9203%)
- `toolchain/libcompile/include/report.h` -> **Severity: 211.6** (Blast Radius: 2.116 * Doc Risk: 100.0%)
- `engine/src/globdefs.h` -> **Severity: 205.446** (Blast Radius: 17.235 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
