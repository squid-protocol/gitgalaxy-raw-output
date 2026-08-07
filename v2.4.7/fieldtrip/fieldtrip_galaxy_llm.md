# ARCHITECTURAL_BRIEF: fieldtrip
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/fieldtrip` |
| **Timestamp** | `2026-08-07T04:35:08.129267+00:00` |
| **Scan Duration** | `8.1s` |
| **Git Branch** | `master` |
| **Git Commit** | `2f3917526e6a01d37fbb224a02618f4fc61d47d9` |
| **Git Remote** | `https://github.com/fieldtrip/fieldtrip` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2222 malicious artifacts.

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
| Total Artifacts | 8018 |
| Analyzed Artifacts (Scanned) | 2351 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5667 |
| Total LOC | 222995 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 29.3% |
| Dominant Lang | MATLAB |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7253 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2835 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7461 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 44 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MATLAB | 1860 | 182003 | 79.1% |
| C | 206 | 21275 | 8.8% |
| CPP | 76 | 9283 | 3.2% |
| PLAINTEXT | 65 | 0 | 2.8% |
| MARKDOWN | 62 | 0 | 2.6% |
| JAVA | 37 | 4769 | 1.6% |
| MAKEFILE | 28 | 2062 | 1.2% |
| SHELL | 6 | 2658 | 0.3% |
| PYTHON | 5 | 596 | 0.2% |
| XML | 2 | 0 | 0.1% |
| OBJECTIVE-C | 2 | 317 | 0.1% |
| BATCH | 2 | 32 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.502`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_17 | 1293 | 55.0% |
| file_cluster_8 | 633 | 26.9% |
| file_cluster_13 | 152 | 6.5% |
| file_cluster_9 | 78 | 3.3% |
| file_cluster_11 | 37 | 1.6% |
| file_cluster_4 | 17 | 0.7% |
| file_cluster_6 | 4 | 0.2% |
| file_cluster_10 | 4 | 0.2% |
| file_cluster_12 | 4 | 0.2% |
| file_cluster_2 | 1 | 0.0% |
| file_cluster_0 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 127 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5667*

**Composition by Extension & Reason:**
- `.m`: 3441x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 81 exceeds 500 chars), 2x Excluded (Machine-Generated Source Code Signature: 36 LOC)
- `no_extension`: 101x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 97x Excluded (Binary Format Detected), 4x Unsupported Format (.undeterminable)
- `.mexa64`: 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 72x Excluded (Unsupported Extension: '.mexa64'), 35x Excluded (Binary Format Detected)
- `.mexmaci64`: 90x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 64x Excluded (Unsupported Extension: '.mexmaci64'), 31x Excluded (Binary Format Detected)
- `.mexw64`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 55x Excluded (Unsupported Extension: '.mexw64'), 30x Excluded (Binary Format Detected)
- `.mexw32`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 59x Excluded (Unsupported Extension: '.mexw32'), 30x Excluded (Binary Format Detected)
- `.mat`: 80x Excluded (Unsupported Extension: '.mat'), 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.mexmaca64`: 75x Excluded (Unsupported Extension: '.mexmaca64'), 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 30x Excluded (Binary Format Detected)
- `.mexglx`: 54x Excluded (Unsupported Extension: '.mexglx'), 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 25x Excluded (Binary Format Detected)
- `.mexmaci`: 55x Excluded (Unsupported Extension: '.mexmaci'), 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 28x Excluded (Binary Format Detected)
- `.txt`: 92x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.p`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.p')
- `.c`: 74x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.exe`: 62x Excluded (Explicitly Denied Extension: '.exe')
- `.mexmac`: 31x Excluded (Unsupported Extension: '.mexmac'), 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Binary Format Detected)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 63.9 | 77.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 91.1 | 97.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.1 | 13.9 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.0 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.9 | 1.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 91.5 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 14.5 | 10.7 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.9 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 25.5 | 17.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `fileio/private/read_besa_besa.m` (Hits: 190)
- `fileio/private/read_4d_hdr.m` (Hits: 161)
- `fileio/private/read_itab_mhd.m` (Hits: 112)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **buffer.h** (`realtime/src/buffer/src/buffer.h`) — 69 inbound connections
2. **stdint.h** (`realtime/src/buffer/src/win32/stdint.h`) — 17 inbound connections
3. **platform_includes.h** (`realtime/src/buffer/src/platform_includes.h`) — 16 inbound connections
4. **socketserver.h** (`realtime/src/buffer/src/socketserver.h`) — 11 inbound connections
5. **FtBuffer.h** (`realtime/src/buffer/cpp/FtBuffer.h`) — 11 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **platform_includes.h** (`realtime/src/buffer/src/platform_includes.h`) — 22 outbound dependencies
2. **rfbevent.c** (`src/rfbevent.c`) — 18 outbound dependencies
3. **opengl_client.cc** (`realtime/src/acquisition/siemens/src/opengl_client.cc`) — 18 outbound dependencies
4. **neuromag2ft.c** (`realtime/src/acquisition/neuromag/neuromag2ft.c`) — 16 outbound dependencies
5. **viewer.cc** (`realtime/src/utilities/viewer/viewer.cc`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `read` (@ `realtime/src/acquisition/openbci/java/src/OpenBCI_ADS1299.java`) -> Impact: **474.3** | LOC: 583
- `main` (@ `realtime/src/acquisition/openbci/openbci2ft.c`) -> Impact: **372.9** | LOC: 738
- `ft_realtime_headlocalizer` (@ `realtime/online_meg/ft_realtime_headlocalizer.m`) -> Impact: **360.0** | LOC: 1068
  * *Intent:* % FT_REALTIME_HEADLOCALIZER is a real-time application for online visualization of % the head position for the CTF275 and the Neuromag/Elekta/Megin sy...
- `iniHandler` (@ `realtime/src/acquisition/openbci/openbci2ft.c`) -> Impact: **311.6** | LOC: 149
- `main` (@ `realtime/src/acquisition/jaga/jaga2ft.c`) -> Impact: **266.5** | LOC: 619
  * *Intent:* /* see http://stackoverflow.com/questions/230062/whats-the-best-way-to-check-if-a-file-exists-in-c-cross-platform */
- `main` (@ `realtime/src/utilities/audio/ft2audio.c`) -> Impact: **248.5** | LOC: 398
- `writeChannelSettings` (@ `realtime/src/acquisition/openbci/java/src/OpenBCI_ADS1299.java`) -> Impact: **246.0** | LOC: 209
- `mexFunction` (@ `src/nanstd.c`) -> Impact: **215.4** | LOC: 327
  * *Intent:* #if defined (COMPILER_MSVC) #include <math.h> #define isnan _isnan #define INFINITY (HUGE_VAL+HUGE_VAL) #define NAN (INFINITY - INFINITY) #elif define...
- `mexFunction` (@ `src/nanvar.c`) -> Impact: **215.4** | LOC: 327
  * *Intent:* #if defined (COMPILER_MSVC) #include <math.h> #define isnan _isnan #define INFINITY (HUGE_VAL+HUGE_VAL) #define NAN (INFINITY - INFINITY) #elif define...
- `iniHandler` (@ `realtime/src/acquisition/jaga/jaga2ft.c`) -> Impact: **178.8** | LOC: 88

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `fileio/private` | 358 | 84354.92 | 71.32% | 39.89% |
| `private` | 317 | 67799.33 | 64.75% | 31.18% |
| `__monolith__` | 159 | 58417.23 | 73.48% | 45.91% |
| `fileio` | 34 | 37541.84 | 67.84% | 25.85% |
| `utilities` | 93 | 18235.38 | 67.73% | 49.28% |
| `forward/private` | 96 | 16356.89 | 65.96% | 27.28% |
| `plotting/private` | 90 | 15061.41 | 69.78% | 33.88% |
| `utilities/private` | 118 | 14491.3 | 67.14% | 32.73% |
| `plotting` | 30 | 11243.46 | 73.53% | 24.29% |
| `preproc` | 25 | 9175.28 | 59.69% | 12.22% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bis2fieldtrip.m` -> **100.0%** Exposure
- `compat/matlablt2019a/writecell.m` -> **100.0%** Exposure
- `compat/matlablt2019a/writematrix.m` -> **100.0%** Exposure
- `compat/matlablt2022a/clim.m` -> **100.0%** Exposure
- `connectivity/private/ft_debug.m` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `besa2fieldtrip.m` -> **100.0%** Exposure
- `bis2fieldtrip.m` -> **100.0%** Exposure
- `compat/matlablt2010b/@uint64/abs.m` -> **100.0%** Exposure
- `compat/matlablt2010b/@uint64/all.m` -> **100.0%** Exposure
- `compat/matlablt2010b/@uint64/any.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `realtime/src/acquisition/openbci/java/src/Serial.java` -> **13** Orphaned Functions | **28** Duplicates
- `realtime/src/acquisition/openbci/java/src/OpenBCI_ADS1299.java` -> **34** Orphaned Functions | **5** Duplicates
- `realtime/src/buffer/java/nl/fcdonders/fieldtrip/BufferClient.java` -> **16** Orphaned Functions | **16** Duplicates
- `realtime/src/buffer/cpp/FtBuffer.h` -> **0** Orphaned Functions | **22** Duplicates
- `realtime/src/acquisition/amp/AmpServerClient.cpp` -> **20** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`realtime/src/acquisition/jaga/jaga2ft.c`** -> AI Confidence: **99.48%**
2. **`realtime/src/acquisition/neuromag/process_tag.c`** -> AI Confidence: **99.48%**
3. **`realtime/src/acquisition/openbci/openbci2ft.c`** -> AI Confidence: **99.48%**
4. **`realtime/src/acquisition/siemens/src/sap2nifti.c`** -> AI Confidence: **99.48%**
5. **`realtime/src/acquisition/unicorn/unicorn2ft.c`** -> AI Confidence: **99.48%**
6. **`realtime/src/buffer/src/tcpserver.c`** -> AI Confidence: **99.48%**
7. **`realtime/src/buffer/src/tcpsocket.c`** -> AI Confidence: **99.48%**
8. **`realtime/src/utilities/audio/ft2audio.c`** -> AI Confidence: **99.48%**
9. **`realtime/src/utilities/playback/recording.c`** -> AI Confidence: **99.48%**
10. **`src/rfbevent.c`** -> AI Confidence: **99.48%**
11. **`realtime/src/acquisition/emotiv/emotiv2ft.cc`** -> AI Confidence: **99.48%**
12. **`realtime/src/acquisition/modeeg/modeeg2ft_2chn.cc`** -> AI Confidence: **99.48%**
13. **`realtime/src/acquisition/neuralynx/nlx2ft.cc`** -> AI Confidence: **99.48%**
14. **`realtime/src/acquisition/tmsi/tmsi2ft.cpp`** -> AI Confidence: **99.48%**
15. **`realtime/src/utilities/sine2ft/sine2ft.cc`** -> AI Confidence: **99.48%**
16. **`realtime/src/acquisition/ctf/ctf2ft_v1.c`** -> AI Confidence: **99.39%**
17. **`realtime/src/acquisition/neuromag/neuromag2ft.c`** -> AI Confidence: **99.39%**
18. **`realtime/src/acquisition/siemens/src/save_as_nifti.c`** -> AI Confidence: **99.39%**
19. **`realtime/src/buffer/src/dmarequest.c`** -> AI Confidence: **99.39%**
20. **`realtime/src/buffer/src/util.c`** -> AI Confidence: **99.39%**
21. **`realtime/src/acquisition/siemens/src/Brain3dWindow.cc`** -> AI Confidence: **99.39%**
22. **`realtime/src/acquisition/siemens/src/nii_to_buffer.cc`** -> AI Confidence: **99.39%**
23. **`realtime/src/acquisition/tmsi/tmsidriver.cpp`** -> AI Confidence: **99.39%**
24. **`realtime/src/buffer/java/bufferserver/network/ConnectionThread.java`** -> AI Confidence: **99.39%**
25. **`realtime/src/buffer/src/timestamp.c`** -> AI Confidence: **99.35%**
26. **`realtime/src/utilities/viewer/viewer.cc`** -> AI Confidence: **99.35%**
27. **`realtime/src/acquisition/brainproducts/rda2ft.c`** -> AI Confidence: **99.34%**
28. **`realtime/src/acquisition/siemens/src/siemensap.c`** -> AI Confidence: **99.34%**
29. **`realtime/src/buffer/src/socketserver.c`** -> AI Confidence: **99.34%**
30. **`realtime/src/buffer/test/interface_write.c`** -> AI Confidence: **99.34%**
31. **`realtime/src/buffer/test/sinewave.c`** -> AI Confidence: **99.34%**
32. **`realtime/src/buffer/test/test_benchmark.c`** -> AI Confidence: **99.34%**
33. **`realtime/src/buffer/test/test_getdat.c`** -> AI Confidence: **99.34%**
34. **`realtime/src/buffer/test/test_gethdr.c`** -> AI Confidence: **99.34%**
35. **`realtime/src/buffer/test/test_waitdat.c`** -> AI Confidence: **99.34%**
36. **`realtime/src/utilities/buffer/buffer_unix.c`** -> AI Confidence: **99.34%**
37. **`realtime/src/utilities/playback/playback.c`** -> AI Confidence: **99.34%**
38. **`src/nanmean.c`** -> AI Confidence: **99.34%**
39. **`src/nanstd.c`** -> AI Confidence: **99.34%**
40. **`src/nansum.c`** -> AI Confidence: **99.34%**
41. **`src/nanvar.c`** -> AI Confidence: **99.34%**
42. **`contrib/spike/private/spike_crossx.c`** -> AI Confidence: **99.32%**
43. **`realtime/online_eeg/private/midiIn.c`** -> AI Confidence: **99.32%**
44. **`realtime/online_mri/ft_omri_smooth_volume.c`** -> AI Confidence: **99.32%**
45. **`realtime/src/acquisition/neuromag/process_data.c`** -> AI Confidence: **99.32%**
46. **`realtime/src/buffer/matlab/buffer_flushdat.c`** -> AI Confidence: **99.32%**
47. **`realtime/src/buffer/matlab/buffer_flushevt.c`** -> AI Confidence: **99.32%**
48. **`realtime/src/buffer/matlab/buffer_flushhdr.c`** -> AI Confidence: **99.32%**
49. **`realtime/src/buffer/matlab/buffer_getdat.c`** -> AI Confidence: **99.32%**
50. **`realtime/src/buffer/matlab/buffer_gethdr.c`** -> AI Confidence: **99.32%**
51. **`realtime/src/buffer/matlab/buffer_putdat.c`** -> AI Confidence: **99.32%**
52. **`realtime/src/buffer/matlab/buffer_puthdr.c`** -> AI Confidence: **99.32%**
53. **`realtime/src/buffer/matlab/buffer_waitdat.c`** -> AI Confidence: **99.32%**
54. **`realtime/src/buffer/src/tcprequest.c`** -> AI Confidence: **99.32%**
55. **`src/inv3x3.c`** -> AI Confidence: **99.32%**
56. **`src/lmoutr.c`** -> AI Confidence: **99.32%**
57. **`src/ltrisect.c`** -> AI Confidence: **99.32%**
58. **`src/meg_leadfield1.c`** -> AI Confidence: **99.32%**
59. **`src/plinproj.c`** -> AI Confidence: **99.32%**
60. **`src/ptriproj.c`** -> AI Confidence: **99.32%**
61. **`src/routlm.c`** -> AI Confidence: **99.32%**
62. **`src/solid_angle.c`** -> AI Confidence: **99.32%**
63. **`realtime/src/acquisition/siemens/src/pixeldata_to_remote_buffer.cc`** -> AI Confidence: **99.32%**
64. **`realtime/src/buffer/cpp/odmTest.cc`** -> AI Confidence: **99.32%**
65. **`src/combineClusters.cpp`** -> AI Confidence: **99.32%**
66. **`realtime/src/acquisition/ctf/ctf2ft_v2.c`** -> AI Confidence: **99.31%**
67. **`realtime/src/acquisition/ctf/ctf_simulate.c`** -> AI Confidence: **99.31%**
68. **`realtime/src/acquisition/modeeg/serial.c`** -> AI Confidence: **99.31%**
69. **`realtime/src/acquisition/neurosky/serial.c`** -> AI Confidence: **99.31%**
70. **`realtime/src/acquisition/openbci/serial.c`** -> AI Confidence: **99.31%**
71. **`realtime/src/acquisition/unicorn/serial.c`** -> AI Confidence: **99.31%**
72. **`realtime/src/buffer/src/compat_clock_gettime.c`** -> AI Confidence: **99.31%**
73. **`realtime/src/buffer/src/compat_fsync.c`** -> AI Confidence: **99.31%**
74. **`realtime/src/buffer/test/test_pthread.c`** -> AI Confidence: **99.31%**
75. **`realtime/src/buffer/test/test_socketclient.c`** -> AI Confidence: **99.31%**
76. **`realtime/src/utilities/serial2event/serial.c`** -> AI Confidence: **99.31%**
77. **`realtime/src/acquisition/amp/AmpServerClient.cpp`** -> AI Confidence: **99.31%**
78. **`realtime/src/acquisition/siemens/src/gui_buffer_client.cc`** -> AI Confidence: **99.31%**
79. **`realtime/src/acquisition/siemens/src/gui_streamer.cc`** -> AI Confidence: **99.31%**
80. **`realtime/src/acquisition/siemens/src/opengl_client.cc`** -> AI Confidence: **99.31%**
81. **`realtime/src/acquisition/tobi/tia2ft.cpp`** -> AI Confidence: **99.31%**
82. **`realtime/src/buffer/cpp/StringServer.cc`** -> AI Confidence: **99.31%**
83. **`realtime/src/buffer/java/bufferserver/BufferServer.java`** -> AI Confidence: **99.31%**
84. **`realtime/src/buffer/java/bufferserver/data/SavingRingDataStore.java`** -> AI Confidence: **99.31%**
85. **`realtime/src/buffer/java/bufferserver/network/NetworkProtocol.java`** -> AI Confidence: **99.31%**
86. **`.github/scripts/suggest_tests.py`** -> AI Confidence: **99.29%**
87. **`connectivity/private/det2x2.m`** -> AI Confidence: **99.29%**
88. **`connectivity/private/inv2x2.m`** -> AI Confidence: **99.29%**
89. **`connectivity/private/istrue.m`** -> AI Confidence: **99.29%**
90. **`connectivity/private/standardise.m`** -> AI Confidence: **99.29%**
91. **`contrib/misc/private/ignorefields.m`** -> AI Confidence: **99.29%**
92. **`contrib/nutmegtrip/private/nmt_ts_intervalpower.m`** -> AI Confidence: **99.29%**
93. **`contrib/spike/ft_spike_plot_isi.m`** -> AI Confidence: **99.29%**
94. **`contrib/spike/private/isrealmat.m`** -> AI Confidence: **99.29%**
95. **`contrib/spike/private/isrealvec.m`** -> AI Confidence: **99.29%**
96. **`contrib/spike/private/smartinput.m`** -> AI Confidence: **99.29%**
97. **`fileio/ft_chanunit.m`** -> AI Confidence: **99.29%**
98. **`fileio/ft_filetype.m`** -> AI Confidence: **99.29%**
99. **`fileio/ft_filter_event.m`** -> AI Confidence: **99.29%**
100. **`fileio/private/fixcoordsys.m`** -> AI Confidence: **99.29%**
101. **`fileio/private/ft_datatype.m`** -> AI Confidence: **99.29%**
102. **`fileio/private/ft_determine_units.m`** -> AI Confidence: **99.29%**
103. **`fileio/private/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
104. **`fileio/private/ft_senstype.m`** -> AI Confidence: **99.29%**
105. **`fileio/private/ft_warp_apply.m`** -> AI Confidence: **99.29%**
106. **`fileio/private/getorthoviewpos.m`** -> AI Confidence: **99.29%**
107. **`fileio/private/ignorefields.m`** -> AI Confidence: **99.29%**
108. **`fileio/private/istrue.m`** -> AI Confidence: **99.29%**
109. **`fileio/private/ndgrid.m`** -> AI Confidence: **99.29%**
110. **`fileio/private/yokogawa2headmodel.m`** -> AI Confidence: **99.29%**
111. **`forward/ft_determine_units.m`** -> AI Confidence: **99.29%**
112. **`forward/ft_headmodel_infinite.m`** -> AI Confidence: **99.29%**
113. **`forward/ft_senstype.m`** -> AI Confidence: **99.29%**
114. **`forward/private/fixcoordsys.m`** -> AI Confidence: **99.29%**
115. **`forward/private/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
116. **`forward/private/ft_warp_apply.m`** -> AI Confidence: **99.29%**
117. **`forward/private/istrue.m`** -> AI Confidence: **99.29%**
118. **`ft_artifact_tms.m`** -> AI Confidence: **99.29%**
119. **`ft_statistics_analytic.m`** -> AI Confidence: **99.29%**
120. **`inverse/private/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
121. **`inverse/private/ft_senstype.m`** -> AI Confidence: **99.29%**
122. **`plotting/private/colorspec2rgb.m`** -> AI Confidence: **99.29%**
123. **`plotting/private/coordsys2label.m`** -> AI Confidence: **99.29%**
124. **`plotting/private/fixcoordsys.m`** -> AI Confidence: **99.29%**
125. **`plotting/private/ft_determine_units.m`** -> AI Confidence: **99.29%**
126. **`plotting/private/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
127. **`plotting/private/ft_senstype.m`** -> AI Confidence: **99.29%**
128. **`plotting/private/ft_warp_apply.m`** -> AI Confidence: **99.29%**
129. **`plotting/private/intersect_plane.m`** -> AI Confidence: **99.29%**
130. **`plotting/private/istrue.m`** -> AI Confidence: **99.29%**
131. **`plotting/private/ndgrid.m`** -> AI Confidence: **99.29%**
132. **`plotting/private/setviewpoint.m`** -> AI Confidence: **99.29%**
133. **`preproc/private/filter_with_correction.m`** -> AI Confidence: **99.29%**
134. **`preproc/private/istrue.m`** -> AI Confidence: **99.29%**
135. **`private/colorspec2rgb.m`** -> AI Confidence: **99.29%**
136. **`private/combine_transform.m`** -> AI Confidence: **99.29%**
137. **`private/coordsys2label.m`** -> AI Confidence: **99.29%**
138. **`private/det2x2.m`** -> AI Confidence: **99.29%**
139. **`private/dimnum.m`** -> AI Confidence: **99.29%**
140. **`private/fixcoordsys.m`** -> AI Confidence: **99.29%**
141. **`private/ft_fetch_sens.m`** -> AI Confidence: **99.29%**
142. **`private/ft_getuserfun.m`** -> AI Confidence: **99.29%**
143. **`private/getorthoviewpos.m`** -> AI Confidence: **99.29%**
144. **`private/grid2transform.m`** -> AI Confidence: **99.29%**
145. **`private/handle_edit_input.m`** -> AI Confidence: **99.29%**
146. **`private/ignorefields.m`** -> AI Confidence: **99.29%**
147. **`private/isrealmat.m`** -> AI Confidence: **99.29%**
148. **`private/isrealvec.m`** -> AI Confidence: **99.29%**
149. **`private/ndgrid.m`** -> AI Confidence: **99.29%**
150. **`private/print_tim.m`** -> AI Confidence: **99.29%**
151. **`private/read_besa_src.m`** -> AI Confidence: **99.29%**
152. **`private/setviewpoint.m`** -> AI Confidence: **99.29%**
153. **`private/smartinput.m`** -> AI Confidence: **99.29%**
154. **`private/standardise.m`** -> AI Confidence: **99.29%**
155. **`private/swapmemfile.m`** -> AI Confidence: **99.29%**
156. **`private/transform2grid.m`** -> AI Confidence: **99.29%**
157. **`qsub/private/istrue.m`** -> AI Confidence: **99.29%**
158. **`qsub/private/print_mem.m`** -> AI Confidence: **99.29%**
159. **`qsub/private/print_tim.m`** -> AI Confidence: **99.29%**
160. **`realtime/example/ft_realtime_ctfproxy.m`** -> AI Confidence: **99.29%**
161. **`realtime/example/ft_realtime_signalproxy.m`** -> AI Confidence: **99.29%**
162. **`realtime/online_eeg/private/compile_midi.m`** -> AI Confidence: **99.29%**
163. **`specest/private/filter_with_correction.m`** -> AI Confidence: **99.29%**
164. **`specest/private/istrue.m`** -> AI Confidence: **99.29%**
165. **`src/det2x2.m`** -> AI Confidence: **99.29%**
166. **`src/inv2x2.m`** -> AI Confidence: **99.29%**
167. **`statfun/private/istrue.m`** -> AI Confidence: **99.29%**
168. **`utilities/ft_datatype.m`** -> AI Confidence: **99.29%**
169. **`utilities/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
170. **`utilities/ft_warp_apply.m`** -> AI Confidence: **99.29%**
171. **`utilities/istrue.m`** -> AI Confidence: **99.29%**
172. **`utilities/private/coordsys2label.m`** -> AI Confidence: **99.29%**
173. **`utilities/private/fixcoordsys.m`** -> AI Confidence: **99.29%**
174. **`utilities/private/ignorefields.m`** -> AI Confidence: **99.29%**
175. **`utilities/private/smartinput.m`** -> AI Confidence: **99.29%**
176. **`realtime/online_mri/monitor_quality`** -> AI Confidence: **99.29%**
177. **`realtime/src/rebuild.sh`** -> AI Confidence: **99.29%**
178. **`compat/matlablt2010b/@uint64/max.c`** -> AI Confidence: **99.29%**
179. **`compat/matlablt2010b/@uint64/min.c`** -> AI Confidence: **99.29%**
180. **`compat/matlablt2010b/@uint64/minus.c`** -> AI Confidence: **99.29%**
181. **`compat/matlablt2010b/@uint64/plus.c`** -> AI Confidence: **99.29%**
182. **`compat/matlablt2010b/@uint64/rdivide.c`** -> AI Confidence: **99.29%**
183. **`compat/matlablt2010b/@uint64/times.c`** -> AI Confidence: **99.29%**
184. **`realtime/src/acquisition/siemens/include/unixtime.h`** -> AI Confidence: **99.29%**
185. **`realtime/src/acquisition/siemens/src/sap2matlab.c`** -> AI Confidence: **99.29%**
186. **`realtime/src/buffer/matlab/buffer_getevt.c`** -> AI Confidence: **99.29%**
187. **`realtime/src/buffer/matlab/buffer_putevt.c`** -> AI Confidence: **99.29%**
188. **`realtime/src/buffer/src/rdaserver.c`** -> AI Confidence: **99.29%**
189. **`realtime/src/buffer/test/demo_sinewave.c`** -> AI Confidence: **99.29%**
190. **`realtime/src/buffer/test/test_flushdat.c`** -> AI Confidence: **99.29%**
191. **`realtime/src/buffer/test/test_flushevt.c`** -> AI Confidence: **99.29%**
192. **`realtime/src/buffer/test/test_flushhdr.c`** -> AI Confidence: **99.29%**
193. **`realtime/src/buffer/test/test_getevt.c`** -> AI Confidence: **99.29%**
194. **`realtime/src/utilities/serial2event/serial2event.c`** -> AI Confidence: **99.29%**
195. **`src/ft_getopt.c`** -> AI Confidence: **99.29%**
196. **`src/ft_spike_sub_crossx.c`** -> AI Confidence: **99.29%**
197. **`src/mtimes3x3.c`** -> AI Confidence: **99.29%**
198. **`src/nanaccum.c`** -> AI Confidence: **99.29%**
199. **`src/sandwich2x2.c`** -> AI Confidence: **99.29%**
200. **`src/sandwich3x3.c`** -> AI Confidence: **99.29%**
201. **`src/splint_gh.c`** -> AI Confidence: **99.29%**
202. **`realtime/src/acquisition/siemens/include/compiler.h`** -> AI Confidence: **99.29%**
203. **`realtime/src/acquisition/siemens/include/platform.h`** -> AI Confidence: **99.29%**
204. **`realtime/src/buffer/src/compiler.h`** -> AI Confidence: **99.29%**
205. **`realtime/src/buffer/src/platform.h`** -> AI Confidence: **99.29%**
206. **`realtime/src/acquisition/gtec/CheckServerReply.cpp`** -> AI Confidence: **99.29%**
207. **`realtime/src/acquisition/gtec/EscapeXML.cpp`** -> AI Confidence: **99.29%**
208. **`realtime/src/acquisition/gtec/ReadMeasurementData.cpp`** -> AI Confidence: **99.29%**
209. **`realtime/src/acquisition/modeeg/modeeg2ft.cc`** -> AI Confidence: **99.29%**
210. **`realtime/src/acquisition/neurosky/thinkgear2ft.cc`** -> AI Confidence: **99.29%**
211. **`realtime/src/acquisition/siemens/src/PixelDataGrabber.cc`** -> AI Confidence: **99.29%**
212. **`realtime/src/acquisition/siemens/src/testFolderWatcher.cc`** -> AI Confidence: **99.29%**
213. **`realtime/src/buffer/cpp/mex/myfilter.cc`** -> AI Confidence: **99.29%**
214. **`realtime/src/acquisition/openbci/java/src/OpenBCI_ADS1299.java`** -> AI Confidence: **99.29%**
215. **`realtime/src/acquisition/openbci/java/src/openBCI2ft.java`** -> AI Confidence: **99.29%**
216. **`realtime/src/buffer/matlab/buffer.m`** -> AI Confidence: **99.29%**
217. **`utilities/printstruct.m`** -> AI Confidence: **99.29%**
218. **`realtime/src/buffer/cpp/ConsoleInput.h`** -> AI Confidence: **99.28%**
219. **`realtime/src/acquisition/neuromag/include/fiff.h`** -> AI Confidence: **99.26%**
220. **`realtime/src/buffer/cpp/OnlineDataManager.h`** -> AI Confidence: **99.25%**
221. **`realtime/src/acquisition/ctf/ctf2ft_v3.c`** -> AI Confidence: **99.24%**
222. **`realtime/src/buffer/test/test_socketserver.c`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `utilities/ft_trackusage.m` -> **99.9999%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `724` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1328` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `realtime/src/buffer/src/util.c` (C) -> Cumulative Risk: **706.28**
- **Archetype:** `file_cluster_13` (Distance: 13.4 IQR)
- **Magnitude:** 249.18 | **LOC:** 204 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9824%), Safety Score (92.9107%)
- **Heaviest Functions:** `append` (Impact: 28.5), `bufwrite` (Impact: 21.3), `bufread` (Impact: 19.1)

### 2. `realtime/src/buffer/src/tcpsocket.c` (C) -> Cumulative Risk: **701.59**
- **Archetype:** `file_cluster_4` (Distance: 13.108 IQR)
- **Magnitude:** 245.12 | **LOC:** 238 | **CtrlFlow:** 83.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9912%), Documentation (99.7887%)
- **Heaviest Functions:** `tcpsocket` (Impact: 81.8), `cleanup_tcpsocket` (Impact: 9.6)

### 3. `realtime/src/buffer/src/interface.c` (C) -> Cumulative Risk: **696.18**
- **Archetype:** `file_cluster_4` (Distance: 13.977 IQR)
- **Magnitude:** 474.94 | **LOC:** 476 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.6196%), Documentation (95.9801%)
- **Heaviest Functions:** `open_connection` (Impact: 32.0), `wait_data` (Impact: 22.9), `read_header` (Impact: 21.3)

### 4. `realtime/src/buffer/src/tcpserver.c` (C) -> Cumulative Risk: **688.63**
- **Archetype:** `file_cluster_4` (Distance: 13.16 IQR)
- **Magnitude:** 288.74 | **LOC:** 271 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9741%), Documentation (99.4039%)
- **Heaviest Functions:** `tcpserver` (Impact: 114.4), `cleanup_tcpserver` (Impact: 5.8)

### 5. `realtime/src/buffer/src/socketserver.c` (C) -> Cumulative Risk: **687.22**
- **Archetype:** `file_cluster_4` (Distance: 13.479 IQR)
- **Magnitude:** 631.8 | **LOC:** 475 | **CtrlFlow:** 82.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (98.8107%), Safety Score (96.4172%)
- **Heaviest Functions:** `_buffer_socket_func` (Impact: 112.2), `ft_start_buffer_server` (Impact: 80.0), `_buffer_server_func` (Impact: 45.9)

### 6. `realtime/src/buffer/matlab/buffer_mxutils.c` (C) -> Cumulative Risk: **670.98**
- **Archetype:** `file_cluster_13` (Distance: 12.084 IQR)
- **Magnitude:** 227.22 | **LOC:** 169 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.3978%)
- **Heaviest Functions:** `matrix_from_ft_type_data` (Impact: 29.6), `ft_mx_append` (Impact: 23.3), `class_id_from_ft_type` (Impact: 14.3)

### 7. `realtime/src/utilities/serial2event/serial2event.c` (C) -> Cumulative Risk: **668.84**
- **Archetype:** `file_cluster_4` (Distance: 14.099 IQR)
- **Magnitude:** 748.04 | **LOC:** 604 | **CtrlFlow:** 88.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8239%), Documentation (95.2408%)
- **Heaviest Functions:** `parseConfig` (Impact: 123.5), `main` (Impact: 57.3), `_udp_thread` (Impact: 13.7)

### 8. `realtime/src/utilities/playback/ft_storage.c` (C) -> Cumulative Risk: **658.15**
- **Archetype:** `file_cluster_13` (Distance: 13.512 IQR)
- **Magnitude:** 240.06 | **LOC:** 213 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.7804%), Documentation (96.8595%)
- **Heaviest Functions:** `ft_storage_create` (Impact: 77.4), `ft_storage_add_timing` (Impact: 5.5), `ft_storage_add_samples` (Impact: 5.2)

### 9. `src/ft_getopt.c` (C) -> Cumulative Risk: **657.82**
- **Archetype:** `file_cluster_13` (Distance: 14.655 IQR)
- **Magnitude:** 148.44 | **LOC:** 127 | **CtrlFlow:** 94.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.5913%), Safety Score (95.7232%)
- **Heaviest Functions:** `mexFunction` (Impact: 75.9)

### 10. `bin/ft_postfreesurferscript.sh` (SHELL) -> Cumulative Risk: **649.43**
- **Archetype:** `file_cluster_11` (Distance: 16.484 IQR)
- **Magnitude:** 151.28 | **LOC:** 296 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.8235%), Safety Score (98.1892%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 65.3), `__global_context__` (Impact: 7.5), `Anonymous_Block` (Impact: 5.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `fileio/ft_read_event.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.867 IQR)
- **Top Global Matches:** file_cluster_17: 15.867, file_cluster_11: 15.941, file_cluster_0: 16.002
- **Magnitude:** 14255.23 | **LOC:** 2690 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.4849%), Tech Debt (18.1963%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 614`, `structural_boundaries: 591`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2599`, `dead_code: 29`, `fragile_debt: 12`
* *Architecture:* `io: 6`
* *Defense:* `safety: 223`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_sourcemovie.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.795 IQR)
- **Top Global Matches:** file_cluster_17: 13.795, file_cluster_8: 13.86, file_cluster_2: 14.0
- **Magnitude:** 4854.76 | **LOC:** 742 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.9069%), Tech Debt (12.0991%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 64`, `args: 10`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 565`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* `safety: 30`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_read_mri.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.671 IQR)
- **Top Global Matches:** file_cluster_17: 14.671, file_cluster_8: 14.679, file_cluster_11: 14.722
- **Magnitude:** 4426.72 | **LOC:** 920 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.6332%), Tech Debt (17.9643%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 83`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 822`, `dead_code: 6`, `fragile_debt: 3`
* *Architecture:* `io: 3`
* *Defense:* `safety: 26`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/private/avw_img_write.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.576 IQR)
- **Top Global Matches:** file_cluster_8: 13.576, file_cluster_17: 13.759, file_cluster_0: 13.842
- **Magnitude:** 3691.51 | **LOC:** 839 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2888%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 73`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 387`, `dead_code: 2`
* *Architecture:* `io: 54`
* *Defense:* `safety: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_statistics_mvpa.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.399 IQR)
- **Top Global Matches:** file_cluster_17: 15.399, file_cluster_11: 15.498, file_cluster_0: 15.523
- **Magnitude:** 3264.64 | **LOC:** 635 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (84.2948%), Tech Debt (14.8742%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 75`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 408`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* `safety: 75`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_read_header.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.514 IQR)
- **Top Global Matches:** file_cluster_17: 15.514, file_cluster_11: 15.632, file_cluster_0: 15.757
- **Magnitude:** 3221.5 | **LOC:** 3097 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (77.1549%), Tech Debt (24.3271%)
**Top Internal Functions/Classes:**
  * `fixchantype` (Impact: 4.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to fill...
  * `fixchanunit` (Impact: 4.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to fill...
  * `recursive_read_header` (Impact: 2.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to dete...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 602`, `structural_boundaries: 334`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3165`, `dead_code: 23`, `planned_debt: 6`, `fragile_debt: 10`, `orphaned_logic: 1`
* *Architecture:* `io: 9`
* *Defense:* `safety: 188`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_filetype.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.918 IQR)
- **Top Global Matches:** file_cluster_8: 14.918, file_cluster_11: 15.143, file_cluster_17: 15.232
- **Magnitude:** 3148.36 | **LOC:** 1873 | **CtrlFlow:** 92.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (89.6715%), Tech Debt (19.5984%)
**Top Internal Functions/Classes:**
  * `ft_filetype` (Impact: 7.5)
    * *Intent:* % FT_FILETYPE determines the filetype of many EEG/MEG/MRI data files by % looking at the name, exten...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 776`, `structural_boundaries: 65`, `args: 13`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 3111`, `dead_code: 4`, `fragile_debt: 10`
* *Architecture:* `io: 8`
* *Defense:* `safety: 17`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `connectivity/ft_connectivity_mutualinformation.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.976 IQR)
- **Top Global Matches:** file_cluster_11: 14.976, file_cluster_17: 15.028, file_cluster_8: 15.065
- **Magnitude:** 3096.43 | **LOC:** 747 | **CtrlFlow:** 63.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.0426%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 57`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 630`, `dead_code: 7`
* *Architecture:* None
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `private/clusterstat.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.586 IQR)
- **Top Global Matches:** file_cluster_11: 14.586, file_cluster_17: 14.625, file_cluster_8: 14.647
- **Magnitude:** 3022.06 | **LOC:** 563 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (87.6699%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 67`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 543`, `dead_code: 6`
* *Architecture:* None
* *Defense:* `safety: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `private/volumeedit.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.598 IQR)
- **Top Global Matches:** file_cluster_8: 13.598, file_cluster_17: 13.874, file_cluster_13: 14.0
- **Magnitude:** 2875.07 | **LOC:** 482 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.7275%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 21`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 398`, `dead_code: 1`
* *Architecture:* None
* *Defense:* `safety: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/private/ctf2grad.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.64 IQR)
- **Top Global Matches:** file_cluster_17: 15.64, file_cluster_11: 15.681, file_cluster_0: 15.795
- **Magnitude:** 2577.97 | **LOC:** 554 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.5952%), Tech Debt (14.822%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 56`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 569`, `dead_code: 7`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* `safety: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `private/ctf2grad.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.64 IQR)
- **Top Global Matches:** file_cluster_17: 15.64, file_cluster_11: 15.681, file_cluster_0: 15.795
- **Magnitude:** 2577.97 | **LOC:** 554 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.5952%), Tech Debt (14.822%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 56`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 569`, `dead_code: 7`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* `safety: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `private/ft_singletrialanalysis_aseo.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.356 IQR)
- **Top Global Matches:** file_cluster_8: 14.356, file_cluster_17: 14.414, file_cluster_11: 14.463
- **Magnitude:** 2253.04 | **LOC:** 575 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.0286%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 54`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 463`, `dead_code: 3`
* *Architecture:* None
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `private/prepare_mesh_cortexhull.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 17.379 IQR)
- **Top Global Matches:** file_cluster_17: 17.379, file_cluster_11: 17.47, file_cluster_9: 17.476
- **Magnitude:** 2116.02 | **LOC:** 587 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.3732%), Tech Debt (31.9038%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 39`, `args: 5`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 250`, `dead_code: 14`, `fragile_debt: 2`
* *Architecture:* `io: 7`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/private/ft_checkdata.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.414 IQR)
- **Top Global Matches:** file_cluster_17: 16.414, file_cluster_11: 16.548, file_cluster_0: 16.628
- **Magnitude:** 2064.36 | **LOC:** 1911 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.8619%), Tech Debt (19.1054%)
**Top Internal Functions/Classes:**
  * `chan2source` (Impact: 17.1)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `print_segmentationinfo` (Impact: 12.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%%%...
  * `ft_checkdata` (Impact: 6.0)
    * *Intent:* % FT_CHECKDATA checks the input data of the main FieldTrip functions, e.g. whether the % type of dat...
  * `source2raw` (Impact: 2.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 492`, `structural_boundaries: 230`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1998`, `dead_code: 34`, `planned_debt: 1`, `fragile_debt: 9`
* *Architecture:* None
* *Defense:* `safety: 122`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utilities/ft_checkdata.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.414 IQR)
- **Top Global Matches:** file_cluster_17: 16.414, file_cluster_11: 16.548, file_cluster_0: 16.628
- **Magnitude:** 2064.36 | **LOC:** 1911 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.8619%), Tech Debt (19.1054%)
**Top Internal Functions/Classes:**
  * `chan2source` (Impact: 17.1)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `print_segmentationinfo` (Impact: 12.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%%%...
  * `ft_checkdata` (Impact: 6.0)
    * *Intent:* % FT_CHECKDATA checks the input data of the main FieldTrip functions, e.g. whether the % type of dat...
  * `source2raw` (Impact: 2.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 492`, `structural_boundaries: 230`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1998`, `dead_code: 34`, `planned_debt: 1`, `fragile_debt: 9`
* *Architecture:* None
* *Defense:* `safety: 122`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/private/read_edf.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.084 IQR)
- **Top Global Matches:** file_cluster_17: 14.084, file_cluster_8: 14.122, file_cluster_11: 14.218
- **Magnitude:** 2058.08 | **LOC:** 468 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.8954%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 36`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 393`, `dead_code: 2`
* *Architecture:* `io: 14`
* *Defense:* `safety: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/synchronize-private.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.375 IQR)
- **Top Global Matches:** file_cluster_8: 13.375, file_cluster_7: 13.865, file_cluster_1: 14.079
- **Magnitude:** 1996.38 | **LOC:** 4226 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (50.8371%), Tech Debt (8.273%)
**Top Internal Functions/Classes:**
  * `sync` (Impact: 16.1)
    * *Intent:* #!/usr/bin/env bash ################################################################################...
  * `__global_context__` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 3`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1931`, `orphaned_logic: 1`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_databrowser.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.784 IQR)
- **Top Global Matches:** file_cluster_17: 15.784, file_cluster_11: 15.938, file_cluster_0: 15.986
- **Magnitude:** 1905.54 | **LOC:** 2391 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (72.5133%), Tech Debt (64.3949%)
**Top Internal Functions/Classes:**
  * `ft_databrowser` (Impact: 8.7)
    * *Intent:* % FT_DATABROWSER can be used for visual inspection of data. Artifacts that were % detected by artifa...
  * `cb_datacursortext` (Impact: 8.1)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 234`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 1856`, `dead_code: 36`, `fragile_debt: 21`, `orphaned_logic: 1`
* *Architecture:* `io: 1`
* *Defense:* `safety: 88`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_defaults.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.901 IQR)
- **Top Global Matches:** file_cluster_17: 13.901, file_cluster_0: 13.995, file_cluster_8: 13.996
- **Magnitude:** 1871.09 | **LOC:** 452 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.8204%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 52`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 85`, `dead_code: 5`
* *Architecture:* `io: 1`
* *Defense:* `safety: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `connectivity/ft_connectivity_granger.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.067 IQR)
- **Top Global Matches:** file_cluster_8: 14.067, file_cluster_17: 14.242, file_cluster_11: 14.253
- **Magnitude:** 1755.73 | **LOC:** 484 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1391%), Tech Debt (27.3547%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 65`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 352`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* None
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_sourceplot.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.757 IQR)
- **Top Global Matches:** file_cluster_17: 14.757, file_cluster_11: 14.953, file_cluster_8: 14.958
- **Magnitude:** 1743.18 | **LOC:** 2164 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.6113%), Tech Debt (10.7512%)
**Top Internal Functions/Classes:**
  * `cb_keyboard` (Impact: 13.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `ft_sourceplot` (Impact: 10.5)
    * *Intent:* % FT_SOURCEPLOT plots functional source reconstruction data on slices or on a surface, % optionally ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 529`, `structural_boundaries: 213`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 1689`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* None
* *Defense:* `safety: 102`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/private/read_4d_hdr.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.604 IQR)
- **Top Global Matches:** file_cluster_17: 14.604, file_cluster_0: 14.671, file_cluster_11: 14.686
- **Magnitude:** 1725.59 | **LOC:** 534 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.7326%), Tech Debt (34.1815%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 34`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 482`, `dead_code: 7`, `fragile_debt: 4`
* *Architecture:* `io: 161`
* *Defense:* `safety: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `realtime/src/acquisition/openbci/openbci2ft.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.568 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.035 IQR)
- **Top Global Matches:** file_cluster_13: 14.568, file_cluster_8: 14.65, file_cluster_11: 14.675
- **Magnitude:** 1704.94 | **LOC:** 1097 | **CtrlFlow:** 94.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.2273%), Tech Debt (11.7682%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 372.9)
  * `iniHandler` (Impact: 311.6)
  * `interpret24bitAsInt32` (Impact: 5.8)
  * `interpret16bitAsInt32` (Impact: 5.8)
  * `serialWriteSlow` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 343`, `structural_boundaries: 20`, `args: 5`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 844`, `dead_code: 7`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 142`, `import: 12`
* *Defense:* `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` math.h, socketserver.h, stdlib.h, stdio.h, types.h, signal.h, ini.h, platform.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_read_data.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.455 IQR)
- **Top Global Matches:** file_cluster_8: 14.455, file_cluster_11: 14.489, file_cluster_17: 14.558
- **Magnitude:** 1636.38 | **LOC:** 1775 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.4632%), Tech Debt (14.877%)
**Top Internal Functions/Classes:**
  * `ft_read_data` (Impact: 16.9)
    * *Intent:* % FT_READ_DATA reads data from a variety of EEG, MEG and other time series data files % and represen...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 189`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1595`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 4`
* *Architecture:* `io: 16`
* *Defense:* `safety: 56`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `realtime/src/acquisition/openbci/java/src/OpenBCI_ADS1299.java` (JAVA) | Magnitude: 1284.62 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 621, branch: 337, sec_high_risk_execution: 136, args: 60

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `fileio/private/ft_warp_apply.m` (MATLAB) | Magnitude: 843.84 | Delta: **0.288 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: scientific: 775, state_mutation: 102, indent_spaces: 72, branch: 48
- `forward/private/ft_warp_apply.m` (MATLAB) | Magnitude: 843.84 | Delta: **0.288 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: scientific: 775, state_mutation: 102, indent_spaces: 72, branch: 48
- `plotting/private/ft_warp_apply.m` (MATLAB) | Magnitude: 843.84 | Delta: **0.288 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: scientific: 775, state_mutation: 102, indent_spaces: 72, branch: 48
- `utilities/ft_warp_apply.m` (MATLAB) | Magnitude: 843.84 | Delta: **0.288 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: scientific: 775, state_mutation: 102, indent_spaces: 72, branch: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `fileio/private/read_shm_event.m` (MATLAB) | Magnitude: 119.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 97, indent_spaces: 46, structural_boundaries: 25, branch: 15
- `realtime/src/buffer/cpp/TemplateVectorMath.h` (C) | Magnitude: 135.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 108, indent_spaces: 44, branch: 18, api: 4
- `fileio/private/surface_normals.m` (MATLAB) | Magnitude: 241.33 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 52, scientific: 12, indent_spaces: 12, branch: 9
- `forward/private/surface_normals.m` (MATLAB) | Magnitude: 241.33 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 52, scientific: 12, indent_spaces: 12, branch: 9
- `plotting/private/surface_normals.m` (MATLAB) | Magnitude: 241.33 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 52, scientific: 12, indent_spaces: 12, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `realtime/src/acquisition/gtec/SetupgNautilusXMLConfig.hpp` (CPP) | Magnitude: 49.4 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 53, reflection_metaprogramming: 52, state_mutation: 33, indent_tabs: 12
- `realtime/src/acquisition/gtec/SetupgHIampXMLConfig.hpp` (CPP) | Magnitude: 52.24 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 45, reflection_metaprogramming: 44, state_mutation: 36, indent_tabs: 12
- `realtime/src/acquisition/gtec/SetupgUSBampXMLConfig.hpp` (CPP) | Magnitude: 53.18 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 44, reflection_metaprogramming: 43, state_mutation: 37, indent_tabs: 10
- `realtime/src/acquisition/gtec/XMLDefinitions.hpp` (CPP) | Magnitude: 37.8 | Delta: **0.248 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 39, reflection_metaprogramming: 38, state_mutation: 22, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/mxDeserialize_cpp.cpp` (CPP) | Magnitude: 28.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, macros: 10, structural_boundaries: 8, branch: 7
- `src/mxSerialize_cpp.cpp` (CPP) | Magnitude: 28.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, macros: 9, structural_boundaries: 8, branch: 7
- `realtime/src/buffer/cpp/GDF_BackgroundWriter.h` (C) | Magnitude: 209.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 166, state_mutation: 90, api: 54, structural_boundaries: 36
- `realtime/src/buffer/matlab/buffer_mxutils.h` (C) | Magnitude: 19.28 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 5, api: 4, structural_boundaries: 3, import: 3
- `realtime/src/acquisition/siemens/python/fakeScanner.py` (PYTHON) | Magnitude: 12.24 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 18, branch: 9, structural_boundaries: 8, indent_spaces: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `connectivity/ft_connectivity_pdc.m` (MATLAB) | Magnitude: 93.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 85, indent_spaces: 31, branch: 17, structural_boundaries: 14
- `fileio/private/xsens_mvnx.m` (MATLAB) | Magnitude: 387.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 352, indent_spaces: 219, structural_boundaries: 125, branch: 56
- `private/openedf.m` (MATLAB) | Magnitude: 665.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 177, indent_spaces: 44, branch: 29, structural_boundaries: 17
- `utilities/ft_trackusage.m` (MATLAB) | Magnitude: 101.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 65, indent_spaces: 65, structural_boundaries: 30, branch: 18
- `fileio/private/read_eeglabheader.m` (MATLAB) | Magnitude: 76.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 66, indent_spaces: 32, branch: 21, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `compat/matlablt2019b/colororder.m` (MATLAB) | Magnitude: 12.56 | Delta: **0.251 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: func_start: 1, state_mutation: 1, ui_framework: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `realtime/src/buffer/src/interface.c` (C) | Magnitude: 474.94 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 269, state_mutation: 263, pointers: 199, branch: 57
- `realtime/src/buffer/java/bufferserver/data/SimpleDataStore.java` (JAVA) | Magnitude: 276.44 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 230, structural_boundaries: 74, branch: 52, doc: 45
- `realtime/src/buffer/src/rdaserver.c` (C) | Magnitude: 569.12 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 339, indent_tabs: 312, pointers: 182, branch: 99
- `qsub/qsubcellfun.m` (MATLAB) | Magnitude: 335.44 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 289, indent_spaces: 171, branch: 82, structural_boundaries: 68
- `realtime/src/acquisition/openbci/java/src/Serial.java` (JAVA) | Magnitude: 416.1 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 294, branch: 92, structural_boundaries: 66, func_start: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `fileio/private/decode_res4.m` (MATLAB) | Magnitude: 81.47 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 25, indent_spaces: 22, io: 6, cleanup: 6
- `compat/obsolete/ft_prepare_singleshell.m` (MATLAB) | Magnitude: 34.68 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 28, branch: 5, structural_boundaries: 3, indent_spaces: 3
- `fileio/ft_flush_event.m` (MATLAB) | Magnitude: 148.76 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 9, branch: 8, structural_boundaries: 3
- `fileio/private/read_neuromag_eve.m` (MATLAB) | Magnitude: 27.86 | Delta: **0.323 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 8, io: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `realtime/src/acquisition/siemens/include/siemensap.h` (C) | Magnitude: 45.92 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 59, api: 29, pointers: 20, indent_tabs: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `ft_freqdescriptives.m` (MATLAB) | Magnitude: 170.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 162, indent_spaces: 42, branch: 31, structural_boundaries: 15
- `src/splint_gh.c` (C) | Magnitude: 232.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 153, indent_spaces: 90, api: 25, branch: 20
- `forward/private/magnetic_dipole.m` (MATLAB) | Magnitude: 47.62 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 23, scientific: 13, memory_alloc: 3, args: 1
- `nutmeg2fieldtrip.m` (MATLAB) | Magnitude: 254.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 212, indent_spaces: 144, branch: 62, structural_boundaries: 36
- `ft_conjunctionanalysis.m` (MATLAB) | Magnitude: 118.18 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 105, indent_spaces: 100, branch: 42, safety: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `connectivity/private/mtimes3x3.m` (MATLAB) | Magnitude: 29.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: scientific: 27, state_mutation: 10, args: 1, func_start: 1
- `private/mtimes3x3.m` (MATLAB) | Magnitude: 29.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: scientific: 27, state_mutation: 10, args: 1, func_start: 1
- `src/mtimes3x3.m` (MATLAB) | Magnitude: 29.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: scientific: 27, state_mutation: 10, args: 1, func_start: 1
- `bis2fieldtrip.m` (MATLAB) | Magnitude: 13.42 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 10, args: 1, func_start: 1, dead_code: 1
- `src/nanstd.m` (MATLAB) | Magnitude: 3.46 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, state_mutation: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `qsub/qsubget.m` -> Churn: **100.0%** | Cog Load: 81.3204% | Debt: 0.0%
- `ft_statistics_mvpa.m` -> Churn: **81.91%** | Cog Load: 84.2948% | Debt: 14.8742%
- `bin/synchronize-private.sh` -> Churn: **81.9%** | Cog Load: 50.8371% | Debt: 8.273%
- `ft_electrodeplacement.m` -> Churn: **77.46%** | Cog Load: 69.1024% | Debt: 10.8343%
- `ft_statistics_montecarlo.m` -> Churn: **66.67%** | Cog Load: 83.1331% | Debt: 26.8038%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `fileio/ft_read_event.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 14255.23
- `ft_statistics_mvpa.m` -> **Jan Mathijs Schoffelen** (85.7% isolated ownership) | Magnitude: 3264.64
- `private/clusterstat.m` -> **Jan-Mathijs Schoffelen** (100.0% isolated ownership) | Magnitude: 3022.06
- `fileio/private/ctf2grad.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 2577.97
- `private/ctf2grad.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 2577.97

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `realtime/src/buffer/src/buffer.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 23.3422%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `realtime/src/buffer/src/buffer.h` -> **Severity: 1932.067** (Blast Radius: 20.342 * Doc Risk: 94.9792%)
- `realtime/src/buffer/src/win32/stdint.h` -> **Severity: 1868.618** (Blast Radius: 19.101 * Doc Risk: 97.8283%)
- `realtime/src/buffer/src/message.h` -> **Severity: 636.788** (Blast Radius: 6.368 * Doc Risk: 99.9981%)
- `realtime/src/buffer/src/platform_includes.h` -> **Severity: 615.857** (Blast Radius: 11.835 * Doc Risk: 52.0369%)
- `realtime/src/buffer/src/swapbytes.h` -> **Severity: 317.624** (Blast Radius: 3.177 * Doc Risk: 99.976%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
