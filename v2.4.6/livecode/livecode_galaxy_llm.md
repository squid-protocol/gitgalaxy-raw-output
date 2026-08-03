# ARCHITECTURAL_BRIEF: livecode
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/livecode` |
| **Timestamp** | `2026-08-03T21:05:07.031369+00:00` |
| **Scan Duration** | `13.39s` |
| **Git Branch** | `develop` |
| **Git Commit** | `4606a10ea10b16d5071d0f9f263ccdd7ede8b31d` |
| **Git Remote** | `https://github.com/livecode/livecode.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1744 malicious artifacts.

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
| Total Artifacts | 7645 |
| Analyzed Artifacts (Scanned) | 1996 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5649 |
| Total LOC | 441788 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 26.1% |
| Dominant Lang | LIVECODE |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3283 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `4.733`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1047 | 52.5% |
| file_cluster_13 | 513 | 25.7% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 32.7 | 33.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 42.1 | 38.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 44.1 | 23.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 30.1 | 2.4 | 80.0 |
| API Exposure | 0.0 | 16.0 | 2.3 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 62.8 | 99.9 | 100.0 |
| Commented Logic Exposure | 0.0 | 99.5 | 2.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 25.0 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 30.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.4 | 0.0 | 0.0 |
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

- `MCFilesExecPerformReadFixedFor` (@ `engine/src/exec-files.cpp`) -> Impact: **8727.9** | LOC: 1363
  * *Intent:* ////////////////////////////////////////////////////////////////////////////////
- `__MCStringCantBeEqualToNative` (@ `libfoundation/src/foundation-string.cpp`) -> Impact: **4626.5** | LOC: 2083
- `MCDeployToMacOSXMainBody` (@ `engine/src/deploy_macosx.cpp`) -> Impact: **3727.1** | LOC: 1178
  * *Intent:* * local symbols (further grouped by the module they are from) * defined external symbols (further grouped by the module they are from) * undefined sym...
- `MCObject::exechandler` (@ `engine/src/object.cpp`) -> Impact: **3295.1** | LOC: 2128
  * *Intent:* // MM-2012-09-05: [[ Property Listener ]]
- `ProcessItem` (@ `engine/src/button.cpp`) -> Impact: **3289.0** | LOC: 1036
- `compute_paragraph_number` (@ `engine/src/fieldh.cpp`) -> Impact: **2861.0** | LOC: 679
  * *Intent:* #include "mcerror.h" #include "util.h" #include "MCBlock.h" #include "line.h" #include "globals.h" #include "text.h" #include "osspec.h" //#include "t...
- `MCStringsEvalMatchText` (@ `engine/src/exec-strings.cpp`) -> Impact: **2858.1** | LOC: 1417
- `GetResource` (@ `engine/src/dskmac.cpp`) -> Impact: **2755.6** | LOC: 1615
- `__MCScriptResolveForeignFunctionBindingF` (@ `libscript/src/script-instance.cpp`) -> Impact: **2649.6** | LOC: 1025
- `MCProperty::parse` (@ `engine/src/property.cpp`) -> Impact: **2573.3** | LOC: 665

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `validate_platform` (@ `config.py`) -> **O(2^N) [Recursive]**
- `ParseTarget` (@ `gyp/tools/graphviz.py`) -> **O(2^N) [Recursive]**
- `PrintDependencies` (@ `gyp/tools/pretty_sln.py`) -> **O(2^N) [Recursive]**
- `MergeAttributes` (@ `gyp/tools/pretty_vcproj.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # No attributes to merge? if not node2.attributes: return for (name, value2) in node2.attributes.items(): # Don't merge the 'Name' attribute. if name ...
- `quitMenuItemSelected` (@ `engine/src/mac-menu.mm`) -> **O(2^N) [Recursive]**
- `QTSetComponentProperty` (@ `engine/src/mac-qt-recorder.mm`) -> **O(2^N) [Recursive]**
- `viewDidLoad` (@ `engine/src/mbliphoneapp.mm`) -> **O(2^N) [Recursive]**
- `MCBitmapEffectDefault` (@ `engine/src/bitmapeffect.cpp`) -> **O(2^N) [Recursive]**
- `ProcessItem` (@ `engine/src/button.cpp`) -> **O(2^N) [Recursive]**
- `MCCdata` (@ `engine/src/cdata.cpp`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `MCObject::exechandler` (@ `engine/src/object.cpp`) -> DB Complexity: **650**
  * *Intent:* // MM-2012-09-05: [[ Property Listener ]]
- `augment` (@ `util/perfect/perfect.c`) -> DB Complexity: **577**
  * *Intent:* /* to be called from the macro renew only */
- `MCStringsEvalMatchText` (@ `engine/src/exec-strings.cpp`) -> DB Complexity: **526**
- `GetResource` (@ `engine/src/dskmac.cpp`) -> DB Complexity: **473**
- `MCDeployToMacOSXMainBody` (@ `engine/src/deploy_macosx.cpp`) -> DB Complexity: **455**
  * *Intent:* * local symbols (further grouped by the module they are from) * defined external symbols (further grouped by the module they are from) * undefined sym...
- `MCExecContext::ConvertToLegacyRectangle` (@ `engine/src/exec.cpp`) -> DB Complexity: **443**
- `MCParagraph::loadattrs` (@ `engine/src/paragrafattr.cpp`) -> DB Complexity: **409**
- `MCProperListGetNumberAtIndex` (@ `engine/src/module-canvas.cpp`) -> DB Complexity: **407**
- `__MCStringCantBeEqualToNative` (@ `libfoundation/src/foundation-string.cpp`) -> DB Complexity: **386**
- `MCFilesExecPerformReadFixedFor` (@ `engine/src/exec-files.cpp`) -> DB Complexity: **334**
  * *Intent:* ////////////////////////////////////////////////////////////////////////////////

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `engine/src` | 816 | 448715.55 | 35.44% | 63.31% |
| `ide-support` | 9 | 218763.35 | 86.6% | 27.33% |
| `builder` | 16 | 133028.88 | 60.91% | 13.53% |
| `libfoundation/src` | 59 | 39237.95 | 48.84% | 70.67% |
| `builder/installer` | 19 | 28021.24 | 89.83% | 6.42% |
| `extensions/widgets/androidfield` | 1 | 19603.15 | 47.19% | 0.0% |
| `tests/lcs/core/math` | 6 | 18484.1 | 28.34% | 0.0% |
| `tests` | 10 | 18479.62 | 41.03% | 0.0% |
| `tests/lcs/core/engine` | 32 | 17403.06 | 19.3% | 0.0% |
| `libscript/src` | 72 | 15046.6 | 21.29% | 51.26% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `engine/src/mac-window.mm` -> **100.0%** Exposure
- `engine/src/mbliphone.mm` -> **100.0%** Exposure
- `engine/src/mbliphoneapp.mm` -> **100.0%** Exposure
- `engine/src/mbliphonemisc.mm` -> **100.0%** Exposure
- `engine/src/mbliphonenfc.mm` -> **100.0%** Exposure
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
- `engine/src/exec-interface-field-chunk.cpp` -> **95** Orphaned Functions | **64** Duplicates
- `libfoundation/include/foundation-auto.h` -> **0** Orphaned Functions | **143** Duplicates

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

### Obfuscation & Evasion Surface
- `engine/src/mac-menu.mm` -> **100.0%** Exposure
- `ide-support/revliburl.livecodescript` -> **0.0017%** Exposure
### Exploit Generation Surface
- `buildbot.py` -> **100.0%** Exposure
- `config.py` -> **100.0%** Exposure
- `fetch.py` -> **100.0%** Exposure
- `gyp/tools/graphviz.py` -> **100.0%** Exposure
- `gyp/tools/pretty_sln.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `buildbot.py` -> **100.0%** Exposure
- `fetch.py` -> **100.0%** Exposure
- `prebuilt/archive.py` -> **100.0%** Exposure
- `prebuilt/extract.py` -> **100.0%** Exposure
- `prebuilt/package.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `engine/src/mac-internal.h` -> **10.0%** Exposure
- `engine/src/imagebitmap.cpp` -> **10.0%** Exposure
- `engine/src/mcstring.cpp` -> **10.0%** Exposure
- `engine/src/metacontext.cpp` -> **10.0%** Exposure
- `engine/src/newobj.cpp` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `buildbot.py` -> **100.0%** Exposure
- `config.py` -> **100.0%** Exposure
- `gyp/PRESUBMIT.py` -> **100.0%** Exposure
- `gyp/tools/graphviz.py` -> **100.0%** Exposure
- `gyp/tools/pretty_sln.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `39` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10712` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `engine/src/java/com/runrev/android/billing/samsung/SamsungBillingProvider.java` (JAVA) -> Cumulative Risk: **873.54**
- **Archetype:** `file_cluster_8` (Distance: 11.35 IQR)
- **Magnitude:** 802.98 | **LOC:** 609 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9983%)
- **Heaviest Functions:** `mapResponseCode` (Impact: 86.3), `OnSucceedGetInboxList` (Impact: 55.8), `handleRequestPayment` (Impact: 52.6)

### 2. `engine/src/java/com/runrev/android/NetworkModule.java` (JAVA) -> Cumulative Risk: **867.32**
- **Archetype:** `file_cluster_4` (Distance: 11.553 IQR)
- **Magnitude:** 269.62 | **LOC:** 247 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getNetworkInterfaces` (Impact: 99.5), `postURL` (Impact: 28.3), `putURL` (Impact: 23.8)

### 3. `engine/src/java/com/runrev/android/nativecontrol/InputControl.java` (JAVA) -> Cumulative Risk: **860.95**
- **Archetype:** `file_cluster_8` (Distance: 11.446 IQR)
- **Magnitude:** 340.7 | **LOC:** 333 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `createView` (Impact: 22.6), `setIsPassword` (Impact: 18.6), `setScrollingEnabled` (Impact: 18.5)

### 4. `engine/src/java/com/runrev/android/AdModule.java` (JAVA) -> Cumulative Risk: **850.84**
- **Archetype:** `file_cluster_8` (Distance: 10.454 IQR)
- **Magnitude:** 297.72 | **LOC:** 297 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9772%)
- **Heaviest Functions:** `InneractiveAdWrapper` (Impact: 109.4), `initContainer` (Impact: 14.6), `setVisible` (Impact: 13.9)

### 5. `engine/src/java/com/runrev/android/URLLoader.java` (JAVA) -> Cumulative Risk: **823.32**
- **Archetype:** `file_cluster_8` (Distance: 11.498 IQR)
- **Magnitude:** 341.98 | **LOC:** 337 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.6722%)
- **Heaviest Functions:** `run` (Impact: 153.2), `setMethod` (Impact: 32.5), `setSSLVerification` (Impact: 22.1)

### 6. `engine/src/java/com/runrev/android/SoundModule.java` (JAVA) -> Cumulative Risk: **818.42**
- **Archetype:** `file_cluster_8` (Distance: 10.61 IQR)
- **Magnitude:** 1084.4 | **LOC:** 729 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `playSound` (Impact: 183.3), `setSound` (Impact: 47.8), `playerComplete` (Impact: 41.3)

### 7. `engine/src/java/com/runrev/android/billing/google/GoogleBillingProvider.java` (JAVA) -> Cumulative Risk: **815.02**
- **Archetype:** `file_cluster_8` (Distance: 10.711 IQR)
- **Magnitude:** 733.76 | **LOC:** 599 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9826%)
- **Heaviest Functions:** `mapResponseCode` (Impact: 86.3), `requestProductDetails` (Impact: 62.0), `consumePurchase` (Impact: 44.2)

### 8. `engine/src/java/com/runrev/android/billing/amazon/AmazonBillingProvider.java` (JAVA) -> Cumulative Risk: **805.85**
- **Archetype:** `file_cluster_8` (Distance: 10.616 IQR)
- **Magnitude:** 1299.58 | **LOC:** 535 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9997%)
- **Heaviest Functions:** `onPurchaseResponse` (Impact: 405.3), `onPurchaseUpdatesResponse` (Impact: 244.3), `onItemDataResponse` (Impact: 162.5)

### 9. `engine/src/java/com/runrev/android/DialogModule.java` (JAVA) -> Cumulative Risk: **804.07**
- **Archetype:** `file_cluster_8` (Distance: 11.037 IQR)
- **Magnitude:** 447.88 | **LOC:** 297 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9657%)
- **Heaviest Functions:** `showListPicker` (Impact: 257.8), `showDatePicker` (Impact: 54.9), `showAnswerDialog` (Impact: 18.9)

### 10. `engine/src/java/com/runrev/android/NotificationModule.java` (JAVA) -> Cumulative Risk: **794.37**
- **Archetype:** `file_cluster_8` (Distance: 11.275 IQR)
- **Magnitude:** 562.66 | **LOC:** 646 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9986%)
- **Heaviest Functions:** `onReceive` (Impact: 50.3), `dispatchNotifications` (Impact: 44.2), `setupStatusBarNotification` (Impact: 33.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ide-support/revsaveasandroidstandalone.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.367 IQR)
- **Top Global Matches:** file_cluster_17: 14.367, file_cluster_4: 14.789, file_cluster_11: 14.888
- **Magnitude:** 103457.71 | **LOC:** 2184 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.6934%), Tech Debt (19.3591%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1059`, `structural_boundaries: 556`, `args: 91`, `func_start: 54`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 885`, `dead_code: 29`, `fragile_debt: 11`
* *Architecture:* `io: 17`, `api: 10`, `concurrency: 31`, `import: 2`
* *Defense:* `safety: 102`, `doc: 2`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/installer_utilities.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.274 IQR)
- **Top Global Matches:** file_cluster_17: 12.274, file_cluster_8: 12.408, file_cluster_4: 12.573
- **Magnitude:** 43423.51 | **LOC:** 1626 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (91.9666%), Tech Debt (10.359%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 537`, `structural_boundaries: 202`, `args: 62`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 9`, `state_mutation: 287`, `dead_code: 6`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 7`, `concurrency: 9`
* *Defense:* `safety: 16`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revsaveasstandalone.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.641 IQR)
- **Top Global Matches:** file_cluster_17: 13.641, file_cluster_0: 14.357, file_cluster_11: 14.357
- **Magnitude:** 32211.72 | **LOC:** 2675 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (91.121%), Tech Debt (63.4024%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 560`, `structural_boundaries: 256`, `args: 30`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 8`, `state_mutation: 531`, `dead_code: 14`, `fragile_debt: 16`
* *Architecture:* `io: 4`, `api: 9`, `concurrency: 6`
* *Defense:* `safety: 26`, `sync_locks: 6`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pStack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/builder_utilities.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.778 IQR)
- **Top Global Matches:** file_cluster_8: 11.778, file_cluster_17: 11.843, file_cluster_4: 11.931
- **Magnitude:** 26701.32 | **LOC:** 894 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (77.615%), Tech Debt (9.7353%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 199`, `args: 99`, `func_start: 81`
* *Risk/State:* `state_mutation: 167`, `planned_debt: 1`
* *Architecture:* `io: 8`, `api: 74`, `concurrency: 27`, `import: 1`
* *Defense:* `safety: 12`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` (builderSystemFolder()
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revdocsparser.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.002 IQR)
- **Top Global Matches:** file_cluster_17: 14.002, file_cluster_8: 14.344, file_cluster_11: 14.395
- **Magnitude:** 24959.36 | **LOC:** 2938 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (82.2225%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 310`, `args: 33`, `func_start: 26`
* *Risk/State:* `state_mutation: 739`, `dead_code: 11`
* *Architecture:* `api: 25`
* *Defense:* `safety: 2`, `doc: 9`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revdeploylibraryandroid.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.409 IQR)
- **Top Global Matches:** file_cluster_8: 12.409, file_cluster_17: 12.531, file_cluster_4: 12.747
- **Magnitude:** 21091.56 | **LOC:** 626 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (91.6827%), Tech Debt (21.3815%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 179`, `args: 60`, `func_start: 40`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 264`, `fragile_debt: 3`
* *Architecture:* `api: 31`, `concurrency: 6`
* *Defense:* `safety: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/widgets/androidfield/androidfield.lcb` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.59 IQR)
- **Top Global Matches:** file_cluster_2: 11.59, file_cluster_8: 11.711, file_cluster_17: 11.72
- **Magnitude:** 19603.15 | **LOC:** 1809 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (47.1942%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 365`, `args: 22`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 374`, `dead_code: 9`
* *Architecture:* `api: 6`
* *Defense:* `safety: 10`, `doc: 44`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/tools_builder.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.951 IQR)
- **Top Global Matches:** file_cluster_17: 12.951, file_cluster_8: 13.482, file_cluster_0: 13.503
- **Magnitude:** 15629.84 | **LOC:** 978 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (87.5467%), Tech Debt (10.238%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 154`, `args: 32`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 240`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 5`, `import: 1`
* *Defense:* `safety: 29`, `doc: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` (builderRepoFolder()
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revsaveasiosstandalone.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.421 IQR)
- **Top Global Matches:** file_cluster_17: 13.421, file_cluster_4: 13.731, file_cluster_0: 13.916
- **Magnitude:** 14057.29 | **LOC:** 2136 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (92.5265%), Tech Debt (19.694%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 148`, `args: 32`, `func_start: 12`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 203`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 9`, `api: 2`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 32`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revdeploylibraryios.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.121 IQR)
- **Top Global Matches:** file_cluster_17: 13.121, file_cluster_4: 13.244, file_cluster_0: 13.564
- **Magnitude:** 13368.24 | **LOC:** 724 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (94.3606%), Tech Debt (90.2152%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 118`, `args: 36`, `func_start: 19`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 216`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 9`
* *Architecture:* `api: 16`, `concurrency: 12`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/package_compiler.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.463 IQR)
- **Top Global Matches:** file_cluster_17: 14.463, file_cluster_4: 14.61, file_cluster_11: 14.722
- **Magnitude:** 11898.76 | **LOC:** 1836 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (94.6524%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 140`, `args: 25`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 284`, `dead_code: 8`
* *Architecture:* `io: 3`, `api: 5`, `concurrency: 7`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/lcs/core/math/math.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.806 IQR)
- **Top Global Matches:** file_cluster_8: 13.806, file_cluster_0: 13.89, file_cluster_11: 13.901
- **Magnitude:** 11563.95 | **LOC:** 940 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (36.0765%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 91`, `args: 60`, `func_start: 60`
* *Risk/State:* `state_mutation: 255`, `dead_code: 10`
* *Architecture:* `api: 60`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/widgets/switchbutton/switchbutton.lcb` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.464 IQR)
- **Top Global Matches:** file_cluster_2: 11.464, file_cluster_8: 11.527, file_cluster_17: 11.774
- **Magnitude:** 11535.94 | **LOC:** 582 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (66.9524%), Tech Debt (18.1039%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 105`, `args: 43`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 168`, `fragile_debt: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 3`, `doc: 14`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/release_notes_builder.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.751 IQR)
- **Top Global Matches:** file_cluster_17: 12.751, file_cluster_8: 12.924, file_cluster_13: 13.094
- **Magnitude:** 11006.45 | **LOC:** 1453 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (79.089%), Tech Debt (13.3128%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 148`, `args: 58`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 253`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 10`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` (builderSystemFolder(), it
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec-files.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.165 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 3.866 IQR)
- **Top Global Matches:** file_cluster_8: 15.165, file_cluster_7: 15.192, file_cluster_13: 15.323
- **Magnitude:** 10628.74 | **LOC:** 2769 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 334
- **Risk Profile:** Cognitive Load (47.4999%), Tech Debt (89.6897%)
**Top Internal Functions/Classes:**
  * `MCFilesExecPerformReadFixedFor` (Impact: 8727.9 | O(2^N) | DB: 334)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCFilesExecLaunchUrl` (Impact: 86.0 | O(N^3) | DB: 25)
  * `MCFilesEvalFileItemsOfDirectory` (Impact: 38.2 | O(N^6) | DB: 4)
  * `MCFilesEvalSetRegistryWithType` (Impact: 31.5 | O(N^1) | DB: 10)
  * `MCFilesExecPerformOpenProcess` (Impact: 30.4 | O(N^3) | DB: 3)
    * *Intent:* // MW-2008-08-14: [[ Bug 6898 ]] Interpreting this as a signed char causes sprintf
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 492`, `structural_boundaries: 202`, `args: 234`, `func_start: 110`
* *Risk/State:* `state_mutation: 1389`, `fragile_debt: 13`, `orphaned_logic: 34`
* *Architecture:* `import: 14`
* *Defense:* `doc: 630`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` exec.h, osspec.h, globals.h, securemode.h, uidc.h, filedefs.h, mcerror.h, util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/environment/stackbehavior.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.718 IQR)
- **Top Global Matches:** file_cluster_17: 12.718, file_cluster_4: 12.988, file_cluster_8: 13.07
- **Magnitude:** 9608.93 | **LOC:** 1038 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (63.4185%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 120`, `args: 41`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 206`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 17`, `concurrency: 7`
* *Defense:* `safety: 13`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benchmarks/lcs/strings/native.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.936 IQR)
- **Top Global Matches:** file_cluster_8: 11.936, file_cluster_17: 12.363, file_cluster_7: 12.545
- **Magnitude:** 9487.67 | **LOC:** 710 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (82.3465%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 320`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 371`
* *Architecture:* `api: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/installer/installeruiupdatecheckcardbehavior.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.082 IQR)
- **Top Global Matches:** file_cluster_17: 16.082, file_cluster_4: 16.125, file_cluster_0: 16.401
- **Magnitude:** 9392.92 | **LOC:** 802 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (93.7186%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 85`, `args: 35`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 84`, `dead_code: 16`
* *Architecture:* `io: 3`, `api: 13`, `concurrency: 22`, `import: 1`
* *Defense:* `safety: 9`, `sync_locks: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tPrefStack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/lcs/core/engine/engine.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.651 IQR)
- **Top Global Matches:** file_cluster_2: 11.651, file_cluster_17: 11.67, file_cluster_4: 11.918
- **Magnitude:** 7554.99 | **LOC:** 545 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.3469%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 92`, `args: 83`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 8`, `state_mutation: 83`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 39`, `concurrency: 10`, `import: 2`
* *Defense:* `safety: 6`, `sync_locks: 1`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/lcs/core/files/files.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.618 IQR)
- **Top Global Matches:** file_cluster_8: 12.618, file_cluster_17: 12.625, file_cluster_0: 12.679
- **Magnitude:** 7259.04 | **LOC:** 434 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.5157%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 59`, `args: 29`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 132`, `dead_code: 1`
* *Architecture:* `io: 22`, `api: 16`
* *Defense:* `safety: 13`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/dskmac.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.098 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.008 IQR)
- **Top Global Matches:** file_cluster_13: 15.098, file_cluster_8: 15.101, file_cluster_7: 15.198
- **Magnitude:** 6864.34 | **LOC:** 6008 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 473
- **Risk Profile:** Cognitive Load (46.5836%), Tech Debt (90.3975%)
**Top Internal Functions/Classes:**
  * `GetResource` (Impact: 2755.6 | O(N^6) | DB: 473)
  * `SetResource` (Impact: 412.4 | O(N^6) | DB: 25)
  * `MCS_startprocess_unix` (Impact: 340.6 | O(N^6) | DB: 56)
  * `MCAppleEventHandlerDoSpecial` (Impact: 152.4 | O(N^6) | DB: 41)
  * `MCS_startprocess_launch` (Impact: 145.7 | O(N^5) | DB: 80)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 291`, `args: 182`, `func_start: 87`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 4`, `state_mutation: 2452`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 31`, `duplicate_logic: 4`, `orphaned_logic: 26`
* *Architecture:* `io: 12`, `api: 2`, `import: 37`
* *Defense:* `safety: 1`, `doc: 240`, `sync_locks: 24`, `immutability_locks: 16`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` osspec.h, osxprefix.h, stat.h, mcio.h, parsedef.h, sysctl.h, exec.h, dispatch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/docs_builder.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.049 IQR)
- **Top Global Matches:** file_cluster_17: 12.049, file_cluster_8: 12.25, file_cluster_13: 12.576
- **Magnitude:** 6469.66 | **LOC:** 398 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (80.0106%), Tech Debt (19.1869%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 84`, `args: 30`, `func_start: 18`
* *Risk/State:* `state_mutation: 177`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 9`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` (builderRepoFolder()
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libfoundation/src/foundation-string.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.719 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.639 IQR)
- **Top Global Matches:** file_cluster_8: 14.719, file_cluster_7: 14.767, file_cluster_13: 14.857
- **Magnitude:** 6403.52 | **LOC:** 7360 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 386
- **Risk Profile:** Cognitive Load (47.0082%), Tech Debt (35.9641%)
**Top Internal Functions/Classes:**
  * `__MCStringCantBeEqualToNative` (Impact: 4626.5 | O(2^N) | DB: 386)
  * `__MCStringExpandAt` (Impact: 317.5 | O(N^6) | DB: 75)
  * `MCStringWildcardMatch` (Impact: 10.9 | O(N^2) | DB: 3)
  * `__MCStringDestroy` (Impact: 10.7 | O(N^3))
  * `__MCStringIsTrivial` (Impact: 3.9 | O(N^1) | DB: 2)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// // AL-2015-02-06: [...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 435`, `structural_boundaries: 222`, `args: 107`, `func_start: 84`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 1374`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 11`, `orphaned_logic: 7`
* *Architecture:* `import: 11`
* *Defense:* `doc: 416`, `immutability_locks: 45`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` foundation-chunk.h, langinfo.h, Windows.h, foundation-unicode.h, errno.h, foundation-string-native.cpp.h, foundation-auto.h, locale.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/object.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.511 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.792 IQR)
- **Top Global Matches:** file_cluster_13: 15.511, file_cluster_8: 15.536, file_cluster_7: 15.641
- **Magnitude:** 6308.72 | **LOC:** 5885 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 650
- **Risk Profile:** Cognitive Load (47.5601%), Tech Debt (64.2052%)
**Top Internal Functions/Classes:**
  * `MCObject::exechandler` (Impact: 3295.1 | O(N^6) | DB: 650)
    * *Intent:* // MM-2012-09-05: [[ Property Listener ]]
  * `MCObject::savefontattrs` (Impact: 378.0 | O(N^4) | DB: 155)
  * `MCObject::close` (Impact: 16.9 | O(N^2) | DB: 6)
  * `MCObject::copyfontattrs` (Impact: 15.8 | O(N^2) | DB: 8)
  * `MCObject::isdeletable` (Impact: 13.5 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 680`, `structural_boundaries: 304`, `args: 218`, `func_start: 143`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2509`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 23`, `orphaned_logic: 15`
* *Architecture:* `io: 2`, `import: 51`
* *Defense:* `safety: 1`, `doc: 260`, `immutability_locks: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 51):` osspec.h, hndlrlst.h, mcio.h, graphicscontext.h, aclip.h, parsedef.h, graphic.h, undolst.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/lcs/core/control/try.livecodescript` (LIVECODE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.205 IQR)
- **Top Global Matches:** file_cluster_8: 13.205, file_cluster_17: 13.461, file_cluster_0: 13.544
- **Magnitude:** 6130.23 | **LOC:** 253 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.9316%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 22`, `args: 22`, `func_start: 21`
* *Risk/State:* `state_mutation: 12`, `fragile_debt: 9`
* *Architecture:* `api: 21`
* *Defense:* `safety: 119`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/lcs/core/engine/message-box.livecodescript` (LIVECODE) | Magnitude: 58.12 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 28, structural_boundaries: 21, state_mutation: 12, args: 4
- `util/weak_stub_maker.pl` (PERL) | Magnitude: 287.14 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 260, state_mutation: 197, branch: 82, structural_boundaries: 81
- `revmobile/src/CoreSimulator.h` (OBJECTIVE-C) | Magnitude: 102.3 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: explicit_casts: 443, safety_bypasses: 241, pointers: 241, args: 224
- `engine/rsrc/emscripten-html-template.html` (HTML) | Magnitude: 137.5 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 182, state_mutation: 31, structural_boundaries: 25, branch: 22
- `revmobile/src/DVTiPhoneSimulatorRemoteClient.h` (OBJECTIVE-C) | Magnitude: 83.78 | Delta: **0.234 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: explicit_casts: 246, pointers: 137, safety_bypasses: 135, func_start: 120

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `engine/src/bsdiff_build.cpp` (CPP) | Magnitude: 1016.14 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 690, indent_tabs: 250, branch: 108, doc: 52
- `libfoundation/src/foundation-hash.h` (CPP) | Magnitude: 124.24 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 61, indent_spaces: 56, structural_boundaries: 44, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `engine/src/test.h` (CPP) | Magnitude: 33.68 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 18, pointers: 15, args: 13, macros: 13
- `engine/src/deploy_windows.cpp` (CPP) | Magnitude: 2351.1 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 692, indent_tabs: 419, indent_spaces: 228, branch: 133
- `engine/src/deploy_macosx.cpp` (CPP) | Magnitude: 5506.84 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 1512, indent_tabs: 807, branch: 386, pointers: 234
- `engine/src/deploysecurity.h` (CPP) | Magnitude: 13.08 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 52, macros: 2, pointers: 2, structural_boundaries: 1
- `tools/extract-debug-symbols.sh` (SHELL) | Magnitude: 0.07 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 42, state_mutation: 29, branch: 24, reflection_metaprogramming: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `engine/src/mac-sound.mm` (OBJECTIVE-C) | Magnitude: 293.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 133, state_mutation: 108, doc: 104, branch: 43
- `engine/src/securemode.cpp` (CPP) | Magnitude: 73.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 44, state_mutation: 29, structural_boundaries: 28, args: 14
- `engine/src/dskmac.cpp` (CPP) | Magnitude: 6864.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 2452, indent_spaces: 1459, indent_tabs: 945, branch: 549
- `libfoundation/include/system-stream.h` (CPP) | Magnitude: 19.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 6, state_mutation: 4, macros: 4, structural_boundaries: 3
- `engine/src/exec-interface-field.cpp` (CPP) | Magnitude: 1199.36 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 600, indent_spaces: 290, indent_tabs: 170, doc: 122

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `engine/src/java/com/runrev/android/Contact.java` (JAVA) | Magnitude: 815.98 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 467, branch: 111, structural_boundaries: 106, indent_spaces: 87
- `engine/src/java/com/runrev/android/billing/google/Inventory.java` (JAVA) | Magnitude: 69.74 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 22, args: 13, func_start: 12
- `engine/src/rawarray.h` (CPP) | Magnitude: 28.36 | Delta: **0.149 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 52, structural_boundaries: 47, indent_tabs: 36, args: 19
- `libcore/include/thunk.h` (CPP) | Magnitude: 26.9 | Delta: **0.324 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 69, doc: 61, args: 17, state_mutation: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/lcs/core/graphics/graphics.livecodescript` (LIVECODE) | Magnitude: 2636.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 93, branch: 55, structural_boundaries: 26, explicit_casts: 26
- `tests/_compilertestrunnerbehavior.livecodescript` (LIVECODE) | Magnitude: 5793.09 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 196, state_mutation: 145, branch: 114, structural_boundaries: 85
- `builder/installer/uninstalleruistackbehavior.livecodescript` (LIVECODE) | Magnitude: 1360.4 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 62, branch: 36, structural_boundaries: 28, state_mutation: 25
- `tests/lcs/core/engine/extension.livecodescript` (LIVECODE) | Magnitude: 918.54 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, branch: 22, args: 13, state_mutation: 12
- `extensions/widgets/paletteactions/tests/basic.livecodescript` (LIVECODE) | Magnitude: 105.0 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 15, state_mutation: 6, ui_framework: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/lcs/core/field/lineIndent.livecodescript` (LIVECODE) | Magnitude: 54.19 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: ui_framework: 8, structural_boundaries: 4, state_mutation: 4, indent_spaces: 4
- `tests/lcs/core/engine/engine.livecodescript` (LIVECODE) | Magnitude: 7554.99 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 92, args: 83, state_mutation: 83, ui_framework: 82
- `tests/lcs/core/field/listStyle.livecodescript` (LIVECODE) | Magnitude: 62.79 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: ui_framework: 12, state_mutation: 10, structural_boundaries: 9, indent_spaces: 4
- `tests/lcs/core/field/textAlign.livecodescript` (LIVECODE) | Magnitude: 61.27 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: ui_framework: 12, state_mutation: 9, structural_boundaries: 8, indent_spaces: 4
- `extensions/widgets/segmented/tests/properties.livecodescript` (LIVECODE) | Magnitude: 27.12 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 4, ui_framework: 4, globals: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `engine/src/java/com/runrev/android/NetworkModule.java` (JAVA) | Magnitude: 269.62 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 126, indent_spaces: 63, structural_boundaries: 46, state_mutation: 40
- `builder/installer/installeruiconfirmcardbehavior.livecodescript` (LIVECODE) | Magnitude: 647.52 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 46, state_mutation: 35, structural_boundaries: 33, branch: 28
- `tests/lcs/core/chunks/widget.livecodescript` (LIVECODE) | Magnitude: 32.68 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: concurrency: 6, indent_tabs: 6, structural_boundaries: 4, ui_framework: 4
- `builder/installer/installeruiwaitcardbehavior.livecodescript` (LIVECODE) | Magnitude: 1389.36 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 77, branch: 38, structural_boundaries: 36, state_mutation: 24
- `tests/_testrunnerbehavior.livecodescript` (LIVECODE) | Magnitude: 5533.51 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 204, state_mutation: 117, branch: 111, structural_boundaries: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `engine/src/mixin-refcounted.h` (CPP) | Magnitude: 61.82 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 20, state_mutation: 16, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `engine/src/capsule.h` (CPP) | Magnitude: 18.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 70, indent_tabs: 11, args: 8, structural_boundaries: 7
- `libgraphics/include/graphics.h` (CPP) | Magnitude: 832.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 526, doc: 500, indent_tabs: 311, structural_boundaries: 306
- `libfoundation/src/foundation-chunk.cpp` (CPP) | Magnitude: 1102.34 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 448, state_mutation: 423, doc: 286, branch: 161
- `engine/src/minizip.h` (CPP) | Magnitude: 19.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 78, indent_tabs: 17, structural_boundaries: 15, pointers: 10
- `libgraphics/src/w32text.cpp` (CPP) | Magnitude: 331.8 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 176, doc: 156, indent_spaces: 77, indent_tabs: 74

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `libfoundation/include/foundation-objc.h` (OBJECTIVE-C) | Magnitude: 29.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 7, args: 3, func_start: 3, import: 3
- `engine/src/objectpropsets.cpp` (CPP) | Magnitude: 631.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 351, indent_tabs: 267, doc: 113, branch: 91
- `engine/src/lnxdclnx.cpp` (CPP) | Magnitude: 1151.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 428, indent_spaces: 365, branch: 155, pointers: 146
- `revvideograbber/src/dsvideograbber.h` (CPP) | Magnitude: 85.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 153, structural_boundaries: 75, args: 51, state_mutation: 39
- `engine/src/cardlst.cpp` (CPP) | Magnitude: 475.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 206, indent_tabs: 165, pointers: 83, branch: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `revmobile/src/reviphoneproxy.mm` (OBJECTIVE-C) | Magnitude: 358.64 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 142, indent_tabs: 97, doc: 78, indent_spaces: 69
- `libfoundation/include/system-error.h` (CPP) | Magnitude: 14.12 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 6, structural_boundaries: 3, args: 2, macros: 2
- `engine/src/raw-clipboard.h` (CPP) | Magnitude: 36.22 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 24, state_mutation: 19, immutability_locks: 15
- `extensions/libraries/timezone/tz/Makefile` (MAKEFILE) | Magnitude: 971.92 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 190, structural_boundaries: 145, io: 70, branch: 69
- `engine/src/mcsemaphore.h` (CPP) | Magnitude: 72.82 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_0`
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

- `libfoundation/include/foundation-span.h` -> **Severity: 2370.177** (Blast Radius: 23.703 * Doc Risk: 99.9948%)
- `engine/src/dllst.h` -> **Severity: 729.953** (Blast Radius: 9.214 * Doc Risk: 79.2222%)
- `libfoundation/include/foundation-auto.h` -> **Severity: 324.804** (Blast Radius: 27.248 * Doc Risk: 11.9203%)
- `engine/src/object.h` -> **Severity: 231.981** (Blast Radius: 19.461 * Doc Risk: 11.9203%)
- `toolchain/libcompile/include/report.h` -> **Severity: 211.6** (Blast Radius: 2.116 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
