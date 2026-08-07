# ARCHITECTURAL_BRIEF: reactos
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/OS/reactos` |
| **Timestamp** | `2026-08-07T03:45:05.953199+00:00` |
| **Scan Duration** | `85.48s` |
| **Git Branch** | `master` |
| **Git Commit** | `1ae75e00ae1e785aa8b89ef56afab36b3ad9d27c` |
| **Git Remote** | `https://github.com/reactos/reactos.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 13026 malicious artifacts.

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
| Total Artifacts | 28403 |
| Analyzed Artifacts (Scanned) | 14767 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 13636 |
| Total LOC | 4031907 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 52.0% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.079 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 948 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 11258 | 3625591 | 76.2% |
| CPP | 1630 | 364945 | 11.0% |
| PLAINTEXT | 1513 | 0 | 10.2% |
| ASSEMBLY | 120 | 18526 | 0.8% |
| XML | 59 | 0 | 0.4% |
| MAKEFILE | 43 | 3730 | 0.3% |
| MARKDOWN | 32 | 0 | 0.2% |
| BATCH | 19 | 2665 | 0.1% |
| BINARY_THREAT | 18 | 18 | 0.1% |
| SHELL | 14 | 1695 | 0.1% |
| M4 | 12 | 2599 | 0.1% |
| PYTHON | 10 | 2192 | 0.1% |
| HTML | 10 | 1346 | 0.1% |
| JAVASCRIPT | 10 | 4680 | 0.1% |
| YACC | 7 | 2696 | 0.0% |
| YAML | 4 | 35 | 0.0% |
| PERL | 2 | 1074 | 0.0% |
| OBJECTIVE-C | 2 | 14 | 0.0% |
| CSHARP | 2 | 36 | 0.0% |
| RUST | 1 | 18 | 0.0% |
| CSS | 1 | 47 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.625`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 11289 | 76.4% |
| file_cluster_13 | 1715 | 11.6% |
| file_cluster_9 | 91 | 0.6% |
| file_cluster_12 | 42 | 0.3% |
| file_cluster_11 | 21 | 0.1% |
| file_cluster_7 | 20 | 0.1% |
| Unknown | 18 | 0.1% |
| file_cluster_0 | 14 | 0.1% |
| file_cluster_2 | 4 | 0.0% |
| file_cluster_17 | 3 | 0.0% |
| file_cluster_4 | 3 | 0.0% |
| file_cluster_6 | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1545 | 10.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 13636*

**Composition by Extension & Reason:**
- `.rc`: 5076x Excluded (Unsupported Extension: '.rc'), 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.rc)
- `.c`: 1094x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 59x Excluded (Machine-Generated Source Code Signature: 13 LOC), 19x Excluded (Machine-Generated Source Code Signature: 15 LOC)
- `.bmp`: 1298x Excluded (Explicitly Denied Extension: '.bmp'), 1x Excluded (Explicitly Denied Extension: '.BMP')
- `.h`: 839x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (Machine-Generated Source Code Signature: 177 LOC)
- `.cpp`: 920x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 891 LOC), 1x Excluded (Embedded Array/Matrix Payload: 3483 commas in 933 LOC)
- `.ico`: 833x Excluded (Explicitly Denied Extension: '.ico')
- `.spec`: 571x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.idl`: 326x Excluded (Unsupported Extension: '.idl'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 157x Unsupported Format (.undeterminable), 103x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 25x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.rgs`: 176x Excluded (Unsupported Extension: '.rgs'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mak`: 171x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hpp`: 163x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nls`: 162x Excluded (Unsupported Extension: '.nls')
- `.s`: 159x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 22x Excluded (Embedded Hex Payload: 1218 hex tokens in 621 LOC), 13x Excluded (Embedded Hex Payload: 1026 hex tokens in 525 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 39.1 | 37.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 56.0 | 73.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 31.1 | 10.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 25.0 | 2.4 | 80.0 |
| API Exposure | 0.0 | 19.9 | 9.2 | 10.7 | 0.0 |
| Concurrency Exposure | 0.0 | 95.2 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 60.3 | 99.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 44.3 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 67.3 | 93.8 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.9 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `modules/rosapps/applications/net/dhcpd/configure` (Hits: 895)
- `modules/rostests/winetests/gdiplus/metafile.c` (Hits: 883)
- `dll/win32/winhttp/request.c` (Hits: 433)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **windef.h** (`sdk/include/psdk/windef.h`) — 1590 inbound connections
2. **stdlib.h** (`sdk/tools/mkisofs/schilytools/include/schily/stdlib.h`) — 653 inbound connections
3. **winreg.h** (`sdk/include/psdk/winreg.h`) — 442 inbound connections
4. **winnls.h** (`sdk/include/psdk/winnls.h`) — 429 inbound connections
5. **initguid.h** (`sdk/include/psdk/initguid.h`) — 292 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **precomp.h** (`dll/win32/shell32/precomp.h`) — 87 outbound dependencies
2. **win32kp.h** (`win32ss/win32kp.h`) — 76 outbound dependencies
3. **all.h** (`dll/opengl/mesa/all.h`) — 67 outbound dependencies
4. **freeldr.h** (`boot/freeldr/freeldr/include/freeldr.h`) — 64 outbound dependencies
5. **precomp.h** (`dll/win32/browseui/precomp.h`) — 54 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `PathAllocCanonicalize` (@ `dll/win32/kernelbase/wine/path.c`) -> Impact: **1467.8** | LOC: 2077
- `PathCchSkipRoot` (@ `dll/win32/kernelbase/wine/path.c`) -> Impact: **1354.7** | LOC: 2133
- `get_struct_fc` (@ `sdk/tools/widl/typegen.c`) -> Impact: **1232.5** | LOC: 1529
- `shader_generate_glsl_declarations` (@ `dll/directx/wine/wined3d/glsl_shader.c`) -> Impact: **1140.7** | LOC: 1357
- `PathCanonicalizeW` (@ `dll/win32/kernelbase/wine/path.c`) -> Impact: **1116.3** | LOC: 2061
- `TreeListProc` (@ `base/setup/reactos/treelist.c`) -> Impact: **1083.2** | LOC: 2266
- `UrlCombineW` (@ `dll/win32/shlwapi/url.c`) -> Impact: **1082.9** | LOC: 1488
- `msvcrt_create_io_inherit_block` (@ `dll/win32/msvcrt/file.c`) -> Impact: **1075.5** | LOC: 2249
- `_eof` (@ `dll/win32/msvcrt/file.c`) -> Impact: **1075.4** | LOC: 2247
- `shader_glsl_get_register_name` (@ `dll/directx/wine/wined3d/glsl_shader.c`) -> Impact: **1033.8** | LOC: 1325

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `sdk/include/psdk` | 486 | 82931.26 | 10.29% | 5.32% |
| `dll/directx/wine/wined3d` | 32 | 56427.68 | 66.54% | 56.25% |
| `drivers/filesystems/btrfs` | 44 | 53641.08 | 61.53% | 28.01% |
| `dll/win32/msi` | 45 | 49069.76 | 66.14% | 39.01% |
| `dll/win32/mshtml` | 83 | 48581.32 | 60.57% | 76.79% |
| `dll/win32/comctl32` | 43 | 45609.44 | 63.45% | 42.09% |
| `dll/win32/kernelbase/wine` | 19 | 41287.0 | 50.18% | 68.7% |
| `dll/opengl/mesa` | 115 | 39570.1 | 39.86% | 23.88% |
| `win32ss/user/ntuser` | 94 | 38938.8 | 44.78% | 34.29% |
| `dll/win32/msvcrt` | 50 | 36092.62 | 39.44% | 61.59% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `base/applications/mspaint/miniature.cpp` -> **100.0%** Exposure
- `base/applications/mspaint/mouse.cpp` -> **100.0%** Exposure
- `base/applications/network/telnet/src/stl_bids.h` -> **100.0%** Exposure
- `base/applications/network/telnet/src/tcharmap.h` -> **100.0%** Exposure
- `base/applications/network/telnet/src/tkeydef.cpp` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `base/applications/atactl/atactl.cpp` -> **100.0%** Exposure
- `base/applications/charmap_new/Cell.cpp` -> **100.0%** Exposure
- `base/applications/charmap_new/GridView.cpp` -> **100.0%** Exposure
- `base/applications/cleanmgr/cleanmgr/CCleanupHandler.cpp` -> **100.0%** Exposure
- `base/applications/cleanmgr/cleanmgr/CCleanupHandlerList.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `dll/opengl/mesa/api.c` -> **339** Orphaned Functions | **0** Duplicates
- `base/ctf/cicero/cicuif.cpp` -> **237** Orphaned Functions | **2** Duplicates
- `modules/rosapps/applications/net/tsclient/porting-tools/mstscax/mstscax.cpp` -> **121** Orphaned Functions | **113** Duplicates
- `base/ctf/msutb/msutb.cpp` -> **220** Orphaned Functions | **10** Duplicates
- `modules/rostests/winetests/jscript/lang.js` -> **4** Orphaned Functions | **151** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`base/applications/atactl/atactl.cpp`** -> AI Confidence: **99.48%**
2. **`base/applications/charmap_new/precomp.h`** -> AI Confidence: **99.48%**
3. **`base/applications/fltmc/fltmc.cpp`** -> AI Confidence: **99.48%**
4. **`base/applications/network/ftp/precomp.h`** -> AI Confidence: **99.48%**
5. **`base/applications/network/telnet/precomp.h`** -> AI Confidence: **99.48%**
6. **`base/applications/rapps/gui.cpp`** -> AI Confidence: **99.48%**
7. **`base/services/tftpd/tftpd.cpp`** -> AI Confidence: **99.48%**
8. **`dll/3rdparty/libxslt/precomp.h`** -> AI Confidence: **99.48%**
9. **`dll/opengl/glu32/src/libnurbs/internals/slicer.cc`** -> AI Confidence: **99.48%**
10. **`dll/opengl/glu32/src/libnurbs/internals/subdivider.cc`** -> AI Confidence: **99.48%**
11. **`dll/opengl/glu32/src/libnurbs/nurbtess/sampleMonoPoly.cc`** -> AI Confidence: **99.48%**
12. **`dll/shellext/shellbtrfs/balance.cpp`** -> AI Confidence: **99.48%**
13. **`dll/shellext/shellbtrfs/contextmenu.cpp`** -> AI Confidence: **99.48%**
14. **`dll/shellext/shellbtrfs/devices.cpp`** -> AI Confidence: **99.48%**
15. **`dll/shellext/shellbtrfs/propsheet.cpp`** -> AI Confidence: **99.48%**
16. **`dll/shellext/shellbtrfs/scrub.cpp`** -> AI Confidence: **99.48%**
17. **`dll/win32/devmgr/precomp.h`** -> AI Confidence: **99.48%**
18. **`dll/win32/ws2help/precomp.h`** -> AI Confidence: **99.48%**
19. **`modules/rosapps/applications/devutils/lnktool/lnktool.cpp`** -> AI Confidence: **99.48%**
20. **`modules/rosapps/applications/explorer-old/taskbar/desktopbar.cpp`** -> AI Confidence: **99.48%**
21. **`modules/rosapps/applications/net/tsclient/rdesktop/uiports/qtewin.cpp`** -> AI Confidence: **99.48%**
22. **`modules/rosapps/applications/sysutils/regexpl/RegistryExplorer.cpp`** -> AI Confidence: **99.48%**
23. **`modules/rosapps/applications/sysutils/utils/sdkparse/sdkparse.cpp`** -> AI Confidence: **99.48%**
24. **`modules/rostests/apitests/afd/precomp.h`** -> AI Confidence: **99.48%**
25. **`modules/rostests/apitests/sdk/delayimp.cpp`** -> AI Confidence: **99.48%**
26. **`modules/rostests/apitests/shell32/ShellExecCmdLine.cpp`** -> AI Confidence: **99.48%**
27. **`sdk/lib/drivers/wdf/kmdf/src/core/fxbugcheckcallback.cpp`** -> AI Confidence: **99.48%**
28. **`sdk/tools/txt2nls/main.cpp`** -> AI Confidence: **99.48%**
29. **`win32ss/user/imm32/precomp.h`** -> AI Confidence: **99.48%**
30. **`base/applications/cmdutils/at/at.c`** -> AI Confidence: **99.48%**
31. **`base/applications/cmdutils/attrib/attrib.c`** -> AI Confidence: **99.48%**
32. **`base/applications/cmdutils/comp/comp.c`** -> AI Confidence: **99.48%**
33. **`base/applications/cmdutils/eventcreate/eventcreate.c`** -> AI Confidence: **99.48%**
34. **`base/applications/cmdutils/mode/mode.c`** -> AI Confidence: **99.48%**
35. **`base/applications/cmdutils/more/more.c`** -> AI Confidence: **99.48%**
36. **`base/applications/extrac32/extrac32.c`** -> AI Confidence: **99.48%**
37. **`base/applications/findstr/findstr.c`** -> AI Confidence: **99.48%**
38. **`base/applications/games/winmine/main.c`** -> AI Confidence: **99.48%**
39. **`base/applications/magnify/magnifier.c`** -> AI Confidence: **99.48%**
40. **`base/applications/msconfig_new/fileextractdialog.c`** -> AI Confidence: **99.48%**
41. **`base/applications/mstsc/rdesktop.h`** -> AI Confidence: **99.48%**
42. **`base/applications/network/arp/arp.c`** -> AI Confidence: **99.48%**
43. **`base/applications/network/ipconfig/ipconfig.c`** -> AI Confidence: **99.48%**
44. **`base/applications/network/netstat/netstat.c`** -> AI Confidence: **99.48%**
45. **`base/applications/network/route/route.c`** -> AI Confidence: **99.48%**
46. **`base/applications/regedit/regedit.c`** -> AI Confidence: **99.48%**
47. **`base/applications/runas/runas.c`** -> AI Confidence: **99.48%**
48. **`base/applications/sdbinst/sdbinst.c`** -> AI Confidence: **99.48%**
49. **`base/services/dcomlaunch/network.c`** -> AI Confidence: **99.48%**
50. **`base/services/nfsd/acl.c`** -> AI Confidence: **99.48%**
51. **`base/services/nfsd/ea.c`** -> AI Confidence: **99.48%**
52. **`base/services/nfsd/getattr.c`** -> AI Confidence: **99.48%**
53. **`base/services/nfsd/mount.c`** -> AI Confidence: **99.48%**
54. **`base/services/nfsd/nfs41_compound.c`** -> AI Confidence: **99.48%**
55. **`base/services/nfsd/nfs41_daemon.c`** -> AI Confidence: **99.48%**
56. **`base/services/nfsd/nfs41_rpc.c`** -> AI Confidence: **99.48%**
57. **`base/services/nfsd/open.c`** -> AI Confidence: **99.48%**
58. **`base/services/nfsd/readdir.c`** -> AI Confidence: **99.48%**
59. **`base/services/nfsd/readwrite.c`** -> AI Confidence: **99.48%**
60. **`base/services/nfsd/recovery.c`** -> AI Confidence: **99.48%**
61. **`base/services/nfsd/setattr.c`** -> AI Confidence: **99.48%**
62. **`base/services/nfsd/volume.c`** -> AI Confidence: **99.48%**
63. **`base/setup/reactos/drivepage.c`** -> AI Confidence: **99.48%**
64. **`base/setup/reactos/reactos.c`** -> AI Confidence: **99.48%**
65. **`base/setup/reactos/treelist.c`** -> AI Confidence: **99.48%**
66. **`base/setup/usetup/usetup.c`** -> AI Confidence: **99.48%**
67. **`base/setup/welcome/welcome.c`** -> AI Confidence: **99.48%**
68. **`base/system/autochk/autochk.c`** -> AI Confidence: **99.48%**
69. **`base/system/msiexec/msiexec.c`** -> AI Confidence: **99.48%**
70. **`base/system/regsvr32/regsvr32.c`** -> AI Confidence: **99.48%**
71. **`base/system/rundll32/rundll32.c`** -> AI Confidence: **99.48%**
72. **`boot/freeldr/fdebug/fdebug.c`** -> AI Confidence: **99.48%**
73. **`boot/freeldr/freeldr/ntldr/headless.c`** -> AI Confidence: **99.48%**
74. **`boot/freeldr/freeldr/ntldr/setupldr.c`** -> AI Confidence: **99.48%**
75. **`boot/freeldr/freeldr/ntldr/winldr.c`** -> AI Confidence: **99.48%**
76. **`dll/3rdparty/libjpeg/ckconfig.c`** -> AI Confidence: **99.48%**
77. **`dll/3rdparty/libjpeg/rdjpgcom.c`** -> AI Confidence: **99.48%**
78. **`dll/3rdparty/libtiff/tif_luv.c`** -> AI Confidence: **99.48%**
79. **`dll/3rdparty/libtirpc/src/asprintf.c`** -> AI Confidence: **99.48%**
80. **`dll/3rdparty/libxslt/extra.c`** -> AI Confidence: **99.48%**
81. **`dll/3rdparty/libxslt/functions.c`** -> AI Confidence: **99.48%**
82. **`dll/3rdparty/libxslt/namespaces.c`** -> AI Confidence: **99.48%**
83. **`dll/3rdparty/libxslt/numbers.c`** -> AI Confidence: **99.48%**
84. **`dll/3rdparty/libxslt/preproc.c`** -> AI Confidence: **99.48%**
85. **`dll/3rdparty/libxslt/transform.c`** -> AI Confidence: **99.48%**
86. **`dll/3rdparty/libxslt/xslt.c`** -> AI Confidence: **99.48%**
87. **`dll/3rdparty/libxslt/xsltlocale.c`** -> AI Confidence: **99.48%**
88. **`dll/3rdparty/mbedtls/aes.c`** -> AI Confidence: **99.48%**
89. **`dll/3rdparty/mbedtls/cmac.c`** -> AI Confidence: **99.48%**
90. **`dll/3rdparty/mbedtls/debug.c`** -> AI Confidence: **99.48%**
91. **`dll/3rdparty/mbedtls/entropy.c`** -> AI Confidence: **99.48%**
92. **`dll/3rdparty/mbedtls/error.c`** -> AI Confidence: **99.48%**
93. **`dll/3rdparty/mbedtls/nist_kw.c`** -> AI Confidence: **99.48%**
94. **`dll/3rdparty/mbedtls/pem.c`** -> AI Confidence: **99.48%**
95. **`dll/directx/ddraw/Vtable/DirectD3D2_Vtable.c`** -> AI Confidence: **99.48%**
96. **`dll/directx/ddraw/Vtable/DirectD3D3_Vtable.c`** -> AI Confidence: **99.48%**
97. **`dll/directx/ddraw/Vtable/DirectD3D7_Vtable.c`** -> AI Confidence: **99.48%**
98. **`dll/directx/ddraw/Vtable/DirectD3D_Vtable.c`** -> AI Confidence: **99.48%**
99. **`dll/directx/ddraw/Vtable/DirectDraw2_Vtable.c`** -> AI Confidence: **99.48%**
100. **`dll/directx/ddraw/Vtable/DirectDraw4_Vtable.c`** -> AI Confidence: **99.48%**
101. **`dll/directx/ddraw/Vtable/DirectDraw7_Vtable.c`** -> AI Confidence: **99.48%**
102. **`dll/directx/ddraw/Vtable/DirectDrawSurface2_Vtable.c`** -> AI Confidence: **99.48%**
103. **`dll/directx/ddraw/Vtable/DirectDrawSurface3_Vtable.c`** -> AI Confidence: **99.48%**
104. **`dll/directx/ddraw/Vtable/DirectDrawSurface4_Vtable.c`** -> AI Confidence: **99.48%**
105. **`dll/directx/ddraw/Vtable/DirectDrawSurface7_Vtable.c`** -> AI Confidence: **99.48%**
106. **`dll/directx/ddraw/Vtable/DirectDrawSurface_Vtable.c`** -> AI Confidence: **99.48%**
107. **`dll/directx/ddraw/Vtable/DirectDraw_Vtable.c`** -> AI Confidence: **99.48%**
108. **`dll/directx/wine/dinput/effect_linuxinput.c`** -> AI Confidence: **99.48%**
109. **`dll/np/nfs/nfs41_np.c`** -> AI Confidence: **99.48%**
110. **`dll/opengl/mesa/accum.c`** -> AI Confidence: **99.48%**
111. **`dll/opengl/mesa/alphabuf.c`** -> AI Confidence: **99.48%**
112. **`dll/opengl/mesa/blend.c`** -> AI Confidence: **99.48%**
113. **`dll/opengl/mesa/clip.c`** -> AI Confidence: **99.48%**
114. **`dll/opengl/mesa/context.c`** -> AI Confidence: **99.48%**
115. **`dll/opengl/mesa/copypix.c`** -> AI Confidence: **99.48%**
116. **`dll/opengl/mesa/depth.c`** -> AI Confidence: **99.48%**
117. **`dll/opengl/mesa/dlist.c`** -> AI Confidence: **99.48%**
118. **`dll/opengl/mesa/drawpix.c`** -> AI Confidence: **99.48%**
119. **`dll/opengl/mesa/enable.c`** -> AI Confidence: **99.48%**
120. **`dll/opengl/mesa/eval.c`** -> AI Confidence: **99.48%**
121. **`dll/opengl/mesa/feedback.c`** -> AI Confidence: **99.48%**
122. **`dll/opengl/mesa/fog.c`** -> AI Confidence: **99.48%**
123. **`dll/opengl/mesa/get.c`** -> AI Confidence: **99.48%**
124. **`dll/opengl/mesa/image.c`** -> AI Confidence: **99.48%**
125. **`dll/opengl/mesa/light.c`** -> AI Confidence: **99.48%**
126. **`dll/opengl/mesa/logic.c`** -> AI Confidence: **99.48%**
127. **`dll/opengl/mesa/pb.c`** -> AI Confidence: **99.48%**
128. **`dll/opengl/mesa/pixel.c`** -> AI Confidence: **99.48%**
129. **`dll/opengl/mesa/rastpos.c`** -> AI Confidence: **99.48%**
130. **`dll/opengl/mesa/readpix.c`** -> AI Confidence: **99.48%**
131. **`dll/opengl/mesa/span.c`** -> AI Confidence: **99.48%**
132. **`dll/opengl/mesa/stencil.c`** -> AI Confidence: **99.48%**
133. **`dll/opengl/mesa/texstate.c`** -> AI Confidence: **99.48%**
134. **`dll/opengl/mesa/triangle.c`** -> AI Confidence: **99.48%**
135. **`dll/opengl/mesa/varray.c`** -> AI Confidence: **99.48%**
136. **`dll/opengl/mesa/vbrender.c`** -> AI Confidence: **99.48%**
137. **`dll/opengl/mesa/vbxform.c`** -> AI Confidence: **99.48%**
138. **`dll/win32/batt/batt.c`** -> AI Confidence: **99.48%**
139. **`dll/win32/cabinet/fdi.c`** -> AI Confidence: **99.48%**
140. **`dll/win32/comctl32/button.c`** -> AI Confidence: **99.48%**
141. **`dll/win32/comctl32/datetime.c`** -> AI Confidence: **99.48%**
142. **`dll/win32/comctl32/edit.c`** -> AI Confidence: **99.48%**
143. **`dll/win32/comctl32/tab.c`** -> AI Confidence: **99.48%**
144. **`dll/win32/comctl32/theme_scrollbar.c`** -> AI Confidence: **99.48%**
145. **`dll/win32/comdlg32/finddlg.c`** -> AI Confidence: **99.48%**
146. **`dll/win32/coml2/stg_prop.c`** -> AI Confidence: **99.48%**
147. **`dll/win32/crypt32/base64.c`** -> AI Confidence: **99.48%**
148. **`dll/win32/crypt32/cert.c`** -> AI Confidence: **99.48%**
149. **`dll/win32/crypt32/chain.c`** -> AI Confidence: **99.48%**
150. **`dll/win32/crypt32/msg.c`** -> AI Confidence: **99.48%**
151. **`dll/win32/crypt32/object.c`** -> AI Confidence: **99.48%**
152. **`dll/win32/crypt32/serialize.c`** -> AI Confidence: **99.48%**
153. **`dll/win32/crypt32/str.c`** -> AI Confidence: **99.48%**
154. **`dll/win32/dbghelp/coff.c`** -> AI Confidence: **99.48%**
155. **`dll/win32/dbghelp/inflate.c`** -> AI Confidence: **99.48%**
156. **`dll/win32/gdiplus/image.c`** -> AI Confidence: **99.48%**
157. **`dll/win32/itss/lzx.c`** -> AI Confidence: **99.48%**
158. **`dll/win32/kernel32/winnls/string/format_msg.c`** -> AI Confidence: **99.48%**
159. **`dll/win32/kernel32/winnls/string/lcformat.c`** -> AI Confidence: **99.48%**
160. **`dll/win32/mapi32/sendmail.c`** -> AI Confidence: **99.48%**
161. **`dll/win32/mpr/wnet.c`** -> AI Confidence: **99.48%**
162. **`dll/win32/msacm32/msacm32_main.c`** -> AI Confidence: **99.48%**
163. **`dll/win32/mscms/mscms_main.c`** -> AI Confidence: **99.48%**
164. **`dll/win32/mscms/transform.c`** -> AI Confidence: **99.48%**
165. **`dll/win32/msisip/main.c`** -> AI Confidence: **99.48%**
166. **`dll/win32/mspatcha/lzx.c`** -> AI Confidence: **99.48%**
167. **`dll/win32/msvcrt/locale.c`** -> AI Confidence: **99.48%**
168. **`dll/win32/msvcrt/undname.c`** -> AI Confidence: **99.48%**
169. **`dll/win32/msvidc32/msvideo1.c`** -> AI Confidence: **99.48%**
170. **`dll/win32/netid/netid.c`** -> AI Confidence: **99.48%**
171. **`dll/win32/oleaut32/varformat.c`** -> AI Confidence: **99.48%**
172. **`dll/win32/oleaut32/variant.c`** -> AI Confidence: **99.48%**
173. **`dll/win32/psapi/main.c`** -> AI Confidence: **99.48%**
174. **`dll/win32/riched20/editor.c`** -> AI Confidence: **99.48%**
175. **`dll/win32/rpcrt4/ndr_marshall.c`** -> AI Confidence: **99.48%**
176. **`dll/win32/rpcrt4/ndr_stubless.c`** -> AI Confidence: **99.48%**
177. **`dll/win32/rpcrt4/thunks.c`** -> AI Confidence: **99.48%**
178. **`dll/win32/secur32/wine/ntlm.c`** -> AI Confidence: **99.48%**
179. **`dll/win32/shell32/vista.c`** -> AI Confidence: **99.48%**
180. **`dll/win32/shell32/wine/classes.c`** -> AI Confidence: **99.48%**
181. **`dll/win32/shell32/wine/shell32_main.c`** -> AI Confidence: **99.48%**
182. **`dll/win32/shlwapi/clist.c`** -> AI Confidence: **99.48%**
183. **`dll/win32/shlwapi/url.c`** -> AI Confidence: **99.48%**
184. **`dll/win32/shlwapi/wsprintf.c`** -> AI Confidence: **99.48%**
185. **`dll/win32/syssetup/wizard.c`** -> AI Confidence: **99.48%**
186. **`dll/win32/usp10/bidi.c`** -> AI Confidence: **99.48%**
187. **`dll/win32/usp10/breaking.c`** -> AI Confidence: **99.48%**
188. **`dll/win32/usp10/indic.c`** -> AI Confidence: **99.48%**
189. **`dll/win32/version/version.c`** -> AI Confidence: **99.48%**
190. **`dll/win32/winhttp/url.c`** -> AI Confidence: **99.48%**
191. **`dll/win32/winmm/mci.c`** -> AI Confidence: **99.48%**
192. **`dll/win32/wintrust/softpub.c`** -> AI Confidence: **99.48%**
193. **`dll/win32/wldap32/add.c`** -> AI Confidence: **99.48%**
194. **`dll/win32/wldap32/bind.c`** -> AI Confidence: **99.48%**
195. **`dll/win32/wldap32/compare.c`** -> AI Confidence: **99.48%**
196. **`dll/win32/wldap32/modify.c`** -> AI Confidence: **99.48%**
197. **`dll/win32/wldap32/modrdn.c`** -> AI Confidence: **99.48%**
198. **`dll/win32/wldap32/option.c`** -> AI Confidence: **99.48%**
199. **`dll/win32/wldap32/rename.c`** -> AI Confidence: **99.48%**
200. **`dll/win32/wldap32/search.c`** -> AI Confidence: **99.48%**
201. **`drivers/bluetooth/fbtusb/fbtrwr.c`** -> AI Confidence: **99.48%**
202. **`drivers/bus/acpi/acpica/dispatcher/dsfield.c`** -> AI Confidence: **99.48%**
203. **`drivers/bus/acpi/acpica/dispatcher/dsmethod.c`** -> AI Confidence: **99.48%**
204. **`drivers/bus/acpi/acpica/dispatcher/dsobject.c`** -> AI Confidence: **99.48%**
205. **`drivers/bus/acpi/acpica/dispatcher/dsopcode.c`** -> AI Confidence: **99.48%**
206. **`drivers/bus/acpi/acpica/dispatcher/dspkginit.c`** -> AI Confidence: **99.48%**
207. **`drivers/bus/acpi/acpica/dispatcher/dsutils.c`** -> AI Confidence: **99.48%**
208. **`drivers/bus/acpi/acpica/dispatcher/dswexec.c`** -> AI Confidence: **99.48%**
209. **`drivers/bus/acpi/acpica/dispatcher/dswload.c`** -> AI Confidence: **99.48%**
210. **`drivers/bus/acpi/acpica/dispatcher/dswload2.c`** -> AI Confidence: **99.48%**
211. **`drivers/bus/acpi/acpica/executer/exconfig.c`** -> AI Confidence: **99.48%**
212. **`drivers/bus/acpi/acpica/executer/exoparg1.c`** -> AI Confidence: **99.48%**
213. **`drivers/bus/acpi/acpica/include/acpi.h`** -> AI Confidence: **99.48%**
214. **`drivers/bus/acpi/acpica/include/platform/acenv.h`** -> AI Confidence: **99.48%**
215. **`drivers/bus/acpi/acpica/include/platform/acfreebsd.h`** -> AI Confidence: **99.48%**
216. **`drivers/bus/acpi/acpica/include/platform/acnetbsd.h`** -> AI Confidence: **99.48%**
217. **`drivers/bus/acpi/acpica/namespace/nsparse.c`** -> AI Confidence: **99.48%**
218. **`drivers/bus/acpi/acpica/parser/psargs.c`** -> AI Confidence: **99.48%**
219. **`drivers/bus/acpi/acpica/parser/psloop.c`** -> AI Confidence: **99.48%**
220. **`drivers/bus/acpi/acpica/parser/psparse.c`** -> AI Confidence: **99.48%**
221. **`drivers/bus/acpi/acpica/parser/psxface.c`** -> AI Confidence: **99.48%**
222. **`drivers/filesystems/nfs/nfs41_driver.c`** -> AI Confidence: **99.48%**
223. **`drivers/filesystems/udfs/Include/CrossNt/CrossNt.h`** -> AI Confidence: **99.48%**
224. **`drivers/network/tcpip/ip/transport/tcp/event.c`** -> AI Confidence: **99.48%**
225. **`drivers/network/tcpip/lwip/src/apps/http/makefsdata/makefsdata.c`** -> AI Confidence: **99.48%**
226. **`drivers/network/tcpip/lwip/src/apps/snmp/snmp_msg.c`** -> AI Confidence: **99.48%**
227. **`drivers/network/tcpip/lwip/src/core/init.c`** -> AI Confidence: **99.48%**
228. **`drivers/network/tcpip/lwip/src/core/ipv4/icmp.c`** -> AI Confidence: **99.48%**
229. **`drivers/network/tcpip/lwip/src/core/ipv6/dhcp6.c`** -> AI Confidence: **99.48%**
230. **`drivers/network/tcpip/lwip/src/core/memp.c`** -> AI Confidence: **99.48%**
231. **`drivers/network/tcpip/lwip/src/core/tcp_in.c`** -> AI Confidence: **99.48%**
232. **`drivers/network/tcpip/lwip/src/netif/lowpan6_common.c`** -> AI Confidence: **99.48%**
233. **`drivers/network/tcpip/lwip/src/netif/ppp/lcp.c`** -> AI Confidence: **99.48%**
234. **`drivers/network/tcpip/lwip/src/netif/ppp/multilink.c`** -> AI Confidence: **99.48%**
235. **`drivers/network/tcpip/lwip/src/netif/ppp/utils.c`** -> AI Confidence: **99.48%**
236. **`drivers/storage/class/cdrom/aacs.c`** -> AI Confidence: **99.48%**
237. **`drivers/storage/class/cdrom/cdrom.c`** -> AI Confidence: **99.48%**
238. **`drivers/storage/class/cdrom/init.c`** -> AI Confidence: **99.48%**
239. **`drivers/storage/class/cdrom/ioctl.c`** -> AI Confidence: **99.48%**
240. **`drivers/storage/class/cdrom/scratch.c`** -> AI Confidence: **99.48%**
241. **`drivers/storage/class/cdrom/sense.c`** -> AI Confidence: **99.48%**
242. **`drivers/storage/class/cdrom/zpodd.c`** -> AI Confidence: **99.48%**
243. **`drivers/storage/class/classpnp/classwmi.c`** -> AI Confidence: **99.48%**
244. **`drivers/storage/class/disk/disk.h`** -> AI Confidence: **99.48%**
245. **`drivers/storage/class/ramdisk/ramdisk.c`** -> AI Confidence: **99.48%**
246. **`drivers/storage/ide/uniata/inc/CrossNt.h`** -> AI Confidence: **99.48%**
247. **`hal/halx86/include/hal.h`** -> AI Confidence: **99.48%**
248. **`modules/rosapps/applications/cmdutils/touch/touch.c`** -> AI Confidence: **99.48%**
249. **`modules/rosapps/applications/net/ncftp/libncftp/syshdrs.h`** -> AI Confidence: **99.48%**
250. **`modules/rosapps/applications/net/ncftp/ncftp/getline.c`** -> AI Confidence: **99.48%**
251. **`modules/rosapps/applications/net/ncftp/ncftp/syshdrs.h`** -> AI Confidence: **99.48%**
252. **`modules/rosapps/applications/net/tsclient/rdesktop/serial.c`** -> AI Confidence: **99.48%**
253. **`modules/rosapps/applications/net/tsclient/rdesktop/xwin.c`** -> AI Confidence: **99.48%**
254. **`modules/rosapps/applications/screensavers/matrix/screensave.c`** -> AI Confidence: **99.48%**
255. **`modules/rosapps/applications/sysutils/logevent/logevent.c`** -> AI Confidence: **99.48%**
256. **`modules/rosapps/drivers/vfd/vfddbg.c`** -> AI Confidence: **99.48%**
257. **`modules/rosapps/templates/mdi/childwnd.c`** -> AI Confidence: **99.48%**
258. **`modules/rostests/apitests/appshim/versionlie.c`** -> AI Confidence: **99.48%**
259. **`modules/rostests/apitests/gdi32/StretchBlt.c`** -> AI Confidence: **99.48%**
260. **`modules/rostests/apitests/iphlpapi/SendARP.c`** -> AI Confidence: **99.48%**
261. **`modules/rostests/apitests/localspl/dll/fpEnumPrinters.c`** -> AI Confidence: **99.48%**
262. **`modules/rostests/apitests/localspl/dll/fpSetJob.c`** -> AI Confidence: **99.48%**
263. **`modules/rostests/apitests/localspl/tests.c`** -> AI Confidence: **99.48%**
264. **`modules/rostests/kmtests/kmtest_drv/kmtest_drv.c`** -> AI Confidence: **99.48%**
265. **`modules/rostests/tests/regdump/regproc.c`** -> AI Confidence: **99.48%**
266. **`modules/rostests/win32/winlogon/wlntfytests/wlntfytests.c`** -> AI Confidence: **99.48%**
267. **`modules/rostests/winetests/advapi32/service.c`** -> AI Confidence: **99.48%**
268. **`modules/rostests/winetests/crypt32/protectdata.c`** -> AI Confidence: **99.48%**
269. **`modules/rostests/winetests/gdi32/bitmap.c`** -> AI Confidence: **99.48%**
270. **`modules/rostests/winetests/gdi32/palette.c`** -> AI Confidence: **99.48%**
271. **`modules/rostests/winetests/hid/device.c`** -> AI Confidence: **99.48%**
272. **`modules/rostests/winetests/kernel32/atom.c`** -> AI Confidence: **99.48%**
273. **`modules/rostests/winetests/kernel32/codepage.c`** -> AI Confidence: **99.48%**
274. **`modules/rostests/winetests/kernel32/heap.c`** -> AI Confidence: **99.48%**
275. **`modules/rostests/winetests/kernel32/locale.c`** -> AI Confidence: **99.48%**
276. **`modules/rostests/winetests/kernel32/mailslot.c`** -> AI Confidence: **99.48%**
277. **`modules/rostests/winetests/kernel32/toolhelp.c`** -> AI Confidence: **99.48%**
278. **`modules/rostests/winetests/localui/localui.c`** -> AI Confidence: **99.48%**
279. **`modules/rostests/winetests/mmdevapi/dependency.c`** -> AI Confidence: **99.48%**
280. **`modules/rostests/winetests/riched20/txtsrv.c`** -> AI Confidence: **99.48%**
281. **`modules/rostests/winetests/rpcrt4/rpc.c`** -> AI Confidence: **99.48%**
282. **`modules/rostests/winetests/shdocvw/shortcut.c`** -> AI Confidence: **99.48%**
283. **`modules/rostests/winetests/shlwapi/istream.c`** -> AI Confidence: **99.48%**
284. **`modules/rostests/winetests/shlwapi/url.c`** -> AI Confidence: **99.48%**
285. **`modules/rostests/winetests/twain_32/dsm.c`** -> AI Confidence: **99.48%**
286. **`modules/rostests/winetests/user32/dce.c`** -> AI Confidence: **99.48%**
287. **`modules/rostests/winetests/user32/dde.c`** -> AI Confidence: **99.48%**
288. **`modules/rostests/winetests/wininet/http.c`** -> AI Confidence: **99.48%**
289. **`modules/rostests/winetests/winmm/capture.c`** -> AI Confidence: **99.48%**
290. **`modules/rostests/winetests/winmm/midi.c`** -> AI Confidence: **99.48%**
291. **`modules/rostests/winetests/winmm/mixer.c`** -> AI Confidence: **99.48%**
292. **`modules/rostests/winetests/winmm/wave.c`** -> AI Confidence: **99.48%**
293. **`ntoskrnl/include/internal/ntoskrnl.h`** -> AI Confidence: **99.48%**
294. **`sdk/include/c++/stlport/stl/_range_errors.c`** -> AI Confidence: **99.48%**
295. **`sdk/include/c++/stlport/stl/config/_system.h`** -> AI Confidence: **99.48%**
296. **`sdk/include/c++/stlport/stl/config/features.h`** -> AI Confidence: **99.48%**
297. **`sdk/include/psdk/windows.h`** -> AI Confidence: **99.48%**
298. **`sdk/include/reactos/libs/mbedtls/oid.h`** -> AI Confidence: **99.48%**
299. **`sdk/include/reactos/libs/mbedtls/platform.h`** -> AI Confidence: **99.48%**
300. **`sdk/lib/3rdparty/freetype/src/autofit/afcjk.c`** -> AI Confidence: **99.48%**
301. **`sdk/lib/3rdparty/freetype/src/autofit/afglobal.c`** -> AI Confidence: **99.48%**
302. **`sdk/lib/3rdparty/freetype/src/base/ftobjs.c`** -> AI Confidence: **99.48%**
303. **`sdk/lib/3rdparty/freetype/src/bdf/bdfdrivr.c`** -> AI Confidence: **99.48%**
304. **`sdk/lib/3rdparty/freetype/src/bzip2/ftbzip2.c`** -> AI Confidence: **99.48%**
305. **`sdk/lib/3rdparty/freetype/src/cff/cffgload.c`** -> AI Confidence: **99.48%**
306. **`sdk/lib/3rdparty/freetype/src/cff/cffload.c`** -> AI Confidence: **99.48%**
307. **`sdk/lib/3rdparty/freetype/src/cff/cffobjs.c`** -> AI Confidence: **99.48%**
308. **`sdk/lib/3rdparty/freetype/src/cff/cffparse.c`** -> AI Confidence: **99.48%**
309. **`sdk/lib/3rdparty/freetype/src/cid/cidgload.c`** -> AI Confidence: **99.48%**
310. **`sdk/lib/3rdparty/freetype/src/cid/cidload.c`** -> AI Confidence: **99.48%**
311. **`sdk/lib/3rdparty/freetype/src/pcf/pcfdrivr.c`** -> AI Confidence: **99.48%**
312. **`sdk/lib/3rdparty/freetype/src/pfr/pfrobjs.c`** -> AI Confidence: **99.48%**
313. **`sdk/lib/3rdparty/freetype/src/psaux/cffdecode.c`** -> AI Confidence: **99.48%**
314. **`sdk/lib/3rdparty/freetype/src/psaux/psauxmod.c`** -> AI Confidence: **99.48%**
315. **`sdk/lib/3rdparty/freetype/src/psaux/psobjs.c`** -> AI Confidence: **99.48%**
316. **`sdk/lib/3rdparty/freetype/src/psaux/t1decode.c`** -> AI Confidence: **99.48%**
317. **`sdk/lib/3rdparty/freetype/src/sfnt/sfdriver.c`** -> AI Confidence: **99.48%**
318. **`sdk/lib/3rdparty/freetype/src/sfnt/sfobjs.c`** -> AI Confidence: **99.48%**
319. **`sdk/lib/3rdparty/freetype/src/sfnt/ttcmap.c`** -> AI Confidence: **99.48%**
320. **`sdk/lib/3rdparty/freetype/src/sfnt/ttsbit.c`** -> AI Confidence: **99.48%**
321. **`sdk/lib/3rdparty/freetype/src/truetype/ttgload.c`** -> AI Confidence: **99.48%**
322. **`sdk/lib/3rdparty/freetype/src/truetype/ttgxvar.c`** -> AI Confidence: **99.48%**
323. **`sdk/lib/3rdparty/freetype/src/truetype/ttinterp.c`** -> AI Confidence: **99.48%**
324. **`sdk/lib/3rdparty/freetype/src/truetype/ttpload.c`** -> AI Confidence: **99.48%**
325. **`sdk/lib/3rdparty/freetype/src/type1/t1driver.c`** -> AI Confidence: **99.48%**
326. **`sdk/lib/3rdparty/freetype/src/type1/t1gload.c`** -> AI Confidence: **99.48%**
327. **`sdk/lib/3rdparty/freetype/src/type1/t1load.c`** -> AI Confidence: **99.48%**
328. **`sdk/lib/3rdparty/freetype/src/winfonts/winfnt.c`** -> AI Confidence: **99.48%**
329. **`sdk/tools/log2lines/cache.c`** -> AI Confidence: **99.48%**
330. **`sdk/tools/log2lines/cmd.c`** -> AI Confidence: **99.48%**
331. **`sdk/tools/log2lines/help.c`** -> AI Confidence: **99.48%**
332. **`sdk/tools/log2lines/log2lines.c`** -> AI Confidence: **99.48%**
333. **`sdk/tools/mkisofs/schilytools/include/schily/align.h`** -> AI Confidence: **99.48%**
334. **`sdk/tools/mkisofs/schilytools/include/schily/avoffset.h`** -> AI Confidence: **99.48%**
335. **`sdk/tools/mkisofs/schilytools/include/schily/xconfig.h`** -> AI Confidence: **99.48%**
336. **`sdk/tools/mkisofs/schilytools/libschily/fnmatch.c`** -> AI Confidence: **99.48%**
337. **`sdk/tools/mkisofs/schilytools/libschily/format.c`** -> AI Confidence: **99.48%**
338. **`sdk/tools/mkisofs/schilytools/libschily/searchinpath.c`** -> AI Confidence: **99.48%**
339. **`sdk/tools/port/getopt.c`** -> AI Confidence: **99.48%**
340. **`sdk/tools/widl/expr.c`** -> AI Confidence: **99.48%**
341. **`sdk/tools/widl/typegen.c`** -> AI Confidence: **99.48%**
342. **`sdk/tools/widl/write_msft.c`** -> AI Confidence: **99.48%**
343. **`subsystems/mvdm/ntvdm/bios/bios.c`** -> AI Confidence: **99.48%**
344. **`subsystems/mvdm/ntvdm/bios/bios32/bios32.c`** -> AI Confidence: **99.48%**
345. **`subsystems/mvdm/ntvdm/bios/bios32/dskbios32.c`** -> AI Confidence: **99.48%**
346. **`subsystems/mvdm/ntvdm/bios/bios32/kbdbios32.c`** -> AI Confidence: **99.48%**
347. **`subsystems/mvdm/ntvdm/bios/bios32/moubios32.c`** -> AI Confidence: **99.48%**
348. **`subsystems/mvdm/ntvdm/bios/bios32/vbe.c`** -> AI Confidence: **99.48%**
349. **`subsystems/mvdm/ntvdm/clock.c`** -> AI Confidence: **99.48%**
350. **`subsystems/mvdm/ntvdm/cpu/callback.c`** -> AI Confidence: **99.48%**
351. **`subsystems/mvdm/ntvdm/dos/dos32krnl/dos.c`** -> AI Confidence: **99.48%**
352. **`subsystems/mvdm/ntvdm/dos/dos32krnl/emsdrv.c`** -> AI Confidence: **99.48%**
353. **`subsystems/mvdm/ntvdm/dos/dos32krnl/himem.c`** -> AI Confidence: **99.48%**
354. **`subsystems/mvdm/ntvdm/dos/dos32krnl/process.c`** -> AI Confidence: **99.48%**
355. **`subsystems/mvdm/ntvdm/dos/mouse32.c`** -> AI Confidence: **99.48%**
356. **`subsystems/mvdm/ntvdm/emulator.c`** -> AI Confidence: **99.48%**
357. **`subsystems/mvdm/ntvdm/hardware/cmos.c`** -> AI Confidence: **99.48%**
358. **`subsystems/mvdm/ntvdm/hardware/mouse.c`** -> AI Confidence: **99.48%**
359. **`subsystems/mvdm/ntvdm/hardware/pit.c`** -> AI Confidence: **99.48%**
360. **`subsystems/mvdm/ntvdm/hardware/ps2.c`** -> AI Confidence: **99.48%**
361. **`subsystems/mvdm/ntvdm/hardware/sound/speaker.c`** -> AI Confidence: **99.48%**
362. **`subsystems/mvdm/ntvdm/ntvdm.c`** -> AI Confidence: **99.48%**
363. **`win32ss/gdi/gdi32/wine/enhmetafile.c`** -> AI Confidence: **99.48%**
364. **`win32ss/gdi/gdi32/wine/metafile.c`** -> AI Confidence: **99.48%**
365. **`win32ss/gdi/gdi32/wine/mfdrv/text.c`** -> AI Confidence: **99.48%**
366. **`win32ss/user/winsrv/consrv/frontends/gui/conwnd.c`** -> AI Confidence: **99.48%**
367. **`dll/win32/browseui/shellbars/shellbars.h`** -> AI Confidence: **99.44%**
368. **`dll/win32/shell32/shellmenu/shellmenu.h`** -> AI Confidence: **99.44%**
369. **`modules/rosapps/applications/sysutils/regexpl/ph.h`** -> AI Confidence: **99.44%**
370. **`modules/rosapps/applications/net/dhcpd/src/include/headers.h`** -> AI Confidence: **99.44%**
371. **`subsystems/csr/csrsrv/srv.h`** -> AI Confidence: **99.44%**
372. **`sdk/tools/mkisofs/schilytools/libschily/stdio/schilyio.h`** -> AI Confidence: **99.43%**
373. **`drivers/filesystems/udfs/udffs.h`** -> AI Confidence: **99.42%**
374. **`sdk/lib/3rdparty/stlport/src/iostream.cpp`** -> AI Confidence: **99.42%**
375. **`boot/freeldr/freeldr/include/freeldr.h`** -> AI Confidence: **99.42%**
376. **`dll/opengl/mesa/all.h`** -> AI Confidence: **99.42%**
377. **`drivers/filesystems/fastfat/fatprocs.h`** -> AI Confidence: **99.42%**
378. **`modules/rosapps/applications/net/ncftp/sio/syshdrs.h`** -> AI Confidence: **99.42%**
379. **`sdk/include/dxsdk/dshow.h`** -> AI Confidence: **99.42%**
380. **`sdk/include/ndk/ntndk.h`** -> AI Confidence: **99.42%**
381. **`sdk/include/psdk/gdiplus.h`** -> AI Confidence: **99.42%**
382. **`sdk/include/psdk/rpc.h`** -> AI Confidence: **99.42%**
383. **`sdk/tools/mkisofs/schilytools/include/schily/unistd.h`** -> AI Confidence: **99.42%**
384. **`sdk/tools/mkisofs/schilytools/include/schily/wchar.h`** -> AI Confidence: **99.42%**
385. **`base/applications/drwtsn32/main.cpp`** -> AI Confidence: **99.39%**
386. **`base/applications/msconfig_new/srvpage.cpp`** -> AI Confidence: **99.39%**
387. **`base/applications/network/tracert/tracert.cpp`** -> AI Confidence: **99.39%**
388. **`base/applications/rapps/loaddlg.cpp`** -> AI Confidence: **99.39%**
389. **`dll/opengl/glu32/src/libnurbs/nurbtess/partitionY.cc`** -> AI Confidence: **99.39%**
390. **`dll/shellext/shellbtrfs/recv.cpp`** -> AI Confidence: **99.39%**
391. **`dll/shellext/shellbtrfs/volpropsheet.cpp`** -> AI Confidence: **99.39%**
392. **`dll/win32/shell32/shellmenu/CMenuFocusManager.cpp`** -> AI Confidence: **99.39%**
393. **`dll/win32/shlwapi/autocomp.cpp`** -> AI Confidence: **99.39%**
394. **`modules/rosapps/applications/devutils/shlextdbg/shlextdbg.cpp`** -> AI Confidence: **99.39%**
395. **`modules/rosapps/applications/net/roshttpd/httpd.cpp`** -> AI Confidence: **99.39%**
396. **`modules/rosapps/applications/net/roshttpd/roshttpd.cpp`** -> AI Confidence: **99.39%**
397. **`modules/rosapps/applications/net/tsclient/rdesktop/uiports/qtwin.cpp`** -> AI Confidence: **99.39%**
398. **`modules/rosapps/applications/sysutils/fontsub/fontsub.cpp`** -> AI Confidence: **99.39%**
399. **`modules/rostests/apitests/apphelp/db.cpp`** -> AI Confidence: **99.39%**
400. **`modules/rostests/apitests/shell32/ShellState.cpp`** -> AI Confidence: **99.39%**
401. **`sdk/lib/drivers/wdf/kmdf/src/librarycommon/fxlibrarycommon.cpp`** -> AI Confidence: **99.39%**
402. **`sdk/tools/ms2ps/ms2ps.cpp`** -> AI Confidence: **99.39%**
403. **`base/applications/cmdutils/doskey/doskey.c`** -> AI Confidence: **99.39%**
404. **`base/applications/cmdutils/find/find.c`** -> AI Confidence: **99.39%**
405. **`base/applications/cmdutils/label/label.c`** -> AI Confidence: **99.39%**
406. **`base/applications/cmdutils/wmic/main.c`** -> AI Confidence: **99.39%**
407. **`base/applications/fontview/fontview.c`** -> AI Confidence: **99.39%**
408. **`base/applications/msconfig_new/msconfig.c`** -> AI Confidence: **99.39%**
409. **`base/applications/network/ping/ping.c`** -> AI Confidence: **99.39%**
410. **`base/applications/screensavers/3dtext/3dtext.c`** -> AI Confidence: **99.39%**
411. **`base/applications/screensavers/logon/logon.c`** -> AI Confidence: **99.39%**
412. **`base/applications/winhlp32/hlpfile.c`** -> AI Confidence: **99.39%**
413. **`base/applications/winhlp32/winhelp.c`** -> AI Confidence: **99.39%**
414. **`base/applications/wordpad/print.c`** -> AI Confidence: **99.39%**
415. **`base/applications/wordpad/wordpad.c`** -> AI Confidence: **99.39%**
416. **`base/services/audiosrv/pnp.c`** -> AI Confidence: **99.39%**
417. **`base/services/nfsd/lookup.c`** -> AI Confidence: **99.39%**
418. **`base/services/nfsd/nfs41_client.c`** -> AI Confidence: **99.39%**
419. **`base/services/nfsd/nfs41_ops.c`** -> AI Confidence: **99.39%**
420. **`base/services/nfsd/nfs41_session.c`** -> AI Confidence: **99.39%**
421. **`base/services/rpcss/setup.c`** -> AI Confidence: **99.39%**
422. **`base/setup/lib/utils/osdetect.c`** -> AI Confidence: **99.39%**
423. **`base/setup/lib/utils/partlist.c`** -> AI Confidence: **99.39%**
424. **`base/system/chkdsk/chkdsk.c`** -> AI Confidence: **99.39%**
425. **`base/system/conime/conime.c`** -> AI Confidence: **99.39%**
426. **`base/system/format/format.c`** -> AI Confidence: **99.39%**
427. **`boot/freeldr/tools/rrmdir.c`** -> AI Confidence: **99.39%**
428. **`dll/3rdparty/libtirpc/src/authsspi_prot.c`** -> AI Confidence: **99.39%**
429. **`dll/3rdparty/libtirpc/src/clnt_perror.c`** -> AI Confidence: **99.39%**
430. **`dll/3rdparty/libxslt/attrvt.c`** -> AI Confidence: **99.39%**
431. **`dll/3rdparty/libxslt/imports.c`** -> AI Confidence: **99.39%**
432. **`dll/3rdparty/libxslt/keys.c`** -> AI Confidence: **99.39%**
433. **`dll/3rdparty/libxslt/variables.c`** -> AI Confidence: **99.39%**
434. **`dll/3rdparty/libxslt/xsltutils.c`** -> AI Confidence: **99.39%**
435. **`dll/3rdparty/mbedtls/bignum.c`** -> AI Confidence: **99.39%**
436. **`dll/3rdparty/mbedtls/ecp.c`** -> AI Confidence: **99.39%**
437. **`dll/3rdparty/mbedtls/pkcs5.c`** -> AI Confidence: **99.39%**
438. **`dll/3rdparty/mbedtls/pkwrite.c`** -> AI Confidence: **99.39%**
439. **`dll/3rdparty/mbedtls/rsa.c`** -> AI Confidence: **99.39%**
440. **`dll/3rdparty/mbedtls/sha256.c`** -> AI Confidence: **99.39%**
441. **`dll/3rdparty/mbedtls/ssl_cli.c`** -> AI Confidence: **99.39%**
442. **`dll/3rdparty/mbedtls/ssl_srv.c`** -> AI Confidence: **99.39%**
443. **`dll/3rdparty/mbedtls/ssl_tls.c`** -> AI Confidence: **99.39%**
444. **`dll/3rdparty/mbedtls/x509_crl.c`** -> AI Confidence: **99.39%**
445. **`dll/appcompat/apphelp/apphelp.c`** -> AI Confidence: **99.39%**
446. **`dll/appcompat/shims/layer/dispmode.c`** -> AI Confidence: **99.39%**
447. **`dll/cpl/inetcpl/connections.c`** -> AI Confidence: **99.39%**
448. **`dll/cpl/inetcpl/content.c`** -> AI Confidence: **99.39%**
449. **`dll/cpl/inetcpl/general.c`** -> AI Confidence: **99.39%**
450. **`dll/cpl/inetcpl/security.c`** -> AI Confidence: **99.39%**
451. **`dll/directx/d3d9/d3d9_caps.c`** -> AI Confidence: **99.39%**
452. **`dll/directx/wine/devenum/createdevenum.c`** -> AI Confidence: **99.39%**
453. **`dll/directx/wine/dinput/dinput_main.c`** -> AI Confidence: **99.39%**
454. **`dll/directx/wine/dinput/joystick_linux.c`** -> AI Confidence: **99.39%**
455. **`dll/directx/wine/dinput/joystick_linuxinput.c`** -> AI Confidence: **99.39%**
456. **`dll/directx/wine/msdmo/dmoreg.c`** -> AI Confidence: **99.39%**
457. **`dll/directx/wine/quartz/acmwrapper.c`** -> AI Confidence: **99.39%**
458. **`dll/directx/wine/quartz/avidec.c`** -> AI Confidence: **99.39%**
459. **`dll/directx/wine/quartz/filesource.c`** -> AI Confidence: **99.39%**
460. **`dll/directx/wine/quartz/mpegsplit.c`** -> AI Confidence: **99.39%**
461. **`dll/directx/wine/quartz/pin.c`** -> AI Confidence: **99.39%**
462. **`dll/directx/wine/quartz/regsvr.c`** -> AI Confidence: **99.39%**
463. **`dll/opengl/mesa/lines.c`** -> AI Confidence: **99.39%**
464. **`dll/opengl/mesa/misc.c`** -> AI Confidence: **99.39%**
465. **`dll/opengl/mesa/teximage.c`** -> AI Confidence: **99.39%**
466. **`dll/opengl/mesa/texture.c`** -> AI Confidence: **99.39%**
467. **`dll/win32/advapi32/wine/cred.c`** -> AI Confidence: **99.39%**
468. **`dll/win32/avicap32/avicap32.c`** -> AI Confidence: **99.39%**
469. **`dll/win32/avifil32/extrachunk.c`** -> AI Confidence: **99.39%**
470. **`dll/win32/avifil32/getframe.c`** -> AI Confidence: **99.39%**
471. **`dll/win32/bthci/bthci.c`** -> AI Confidence: **99.39%**
472. **`dll/win32/comctl32/combo.c`** -> AI Confidence: **99.39%**
473. **`dll/win32/comctl32/commctrl.c`** -> AI Confidence: **99.39%**
474. **`dll/win32/comctl32/ipaddress.c`** -> AI Confidence: **99.39%**
475. **`dll/win32/comctl32/listbox.c`** -> AI Confidence: **99.39%**
476. **`dll/win32/comctl32/listview.c`** -> AI Confidence: **99.39%**
477. **`dll/win32/comctl32/propsheet.c`** -> AI Confidence: **99.39%**
478. **`dll/win32/comctl32/static.c`** -> AI Confidence: **99.39%**
479. **`dll/win32/comctl32/syslink.c`** -> AI Confidence: **99.39%**
480. **`dll/win32/comctl32/tooltips.c`** -> AI Confidence: **99.39%**
481. **`dll/win32/comctl32/treeview.c`** -> AI Confidence: **99.39%**
482. **`dll/win32/comdlg32/colordlg.c`** -> AI Confidence: **99.39%**
483. **`dll/win32/comdlg32/filedlg.c`** -> AI Confidence: **99.39%**
484. **`dll/win32/comdlg32/fontdlg.c`** -> AI Confidence: **99.39%**
485. **`dll/win32/comdlg32/printdlg.c`** -> AI Confidence: **99.39%**
486. **`dll/win32/crypt32/crl.c`** -> AI Confidence: **99.39%**
487. **`dll/win32/crypt32/ctl.c`** -> AI Confidence: **99.39%**
488. **`dll/win32/crypt32/decode.c`** -> AI Confidence: **99.39%**
489. **`dll/win32/crypt32/encode.c`** -> AI Confidence: **99.39%**
490. **`dll/win32/crypt32/protectdata.c`** -> AI Confidence: **99.39%**
491. **`dll/win32/crypt32/store.c`** -> AI Confidence: **99.39%**
492. **`dll/win32/cryptdlg/main.c`** -> AI Confidence: **99.39%**
493. **`dll/win32/cryptnet/cryptnet_main.c`** -> AI Confidence: **99.39%**
494. **`dll/win32/cryptui/main.c`** -> AI Confidence: **99.39%**
495. **`dll/win32/dbghelp/stabs.c`** -> AI Confidence: **99.39%**
496. **`dll/win32/fusion/asmname.c`** -> AI Confidence: **99.39%**
497. **`dll/win32/fusion/assembly.c`** -> AI Confidence: **99.39%**
498. **`dll/win32/gdiplus/graphics.c`** -> AI Confidence: **99.39%**
499. **`dll/win32/hhctrl.ocx/hhctrl.c`** -> AI Confidence: **99.39%**
500. **`dll/win32/iccvid/iccvid.c`** -> AI Confidence: **99.39%**
501. **`dll/win32/imaadp32.acm/imaadp32.c`** -> AI Confidence: **99.39%**
502. **`dll/win32/jscript/global.c`** -> AI Confidence: **99.39%**
503. **`dll/win32/kernel32/wine/profile.c`** -> AI Confidence: **99.39%**
504. **`dll/win32/kernelbase/wine/loader.c`** -> AI Confidence: **99.39%**
505. **`dll/win32/kernelbase/wine/locale.c`** -> AI Confidence: **99.39%**
506. **`dll/win32/kernelbase/wine/path.c`** -> AI Confidence: **99.39%**
507. **`dll/win32/kernelbase/wine/registry.c`** -> AI Confidence: **99.39%**
508. **`dll/win32/kernelbase/wine/volume.c`** -> AI Confidence: **99.39%**
509. **`dll/win32/mcicda/mcicda.c`** -> AI Confidence: **99.39%**
510. **`dll/win32/mciqtz32/mciqtz.c`** -> AI Confidence: **99.39%**
511. **`dll/win32/mciwave/mciwave.c`** -> AI Confidence: **99.39%**
512. **`dll/win32/mpr/pwcache.c`** -> AI Confidence: **99.39%**
513. **`dll/win32/msacm32/driver.c`** -> AI Confidence: **99.39%**
514. **`dll/win32/msacm32/filter.c`** -> AI Confidence: **99.39%**
515. **`dll/win32/msacm32/format.c`** -> AI Confidence: **99.39%**
516. **`dll/win32/msacm32/internal.c`** -> AI Confidence: **99.39%**
517. **`dll/win32/msacm32/stream.c`** -> AI Confidence: **99.39%**
518. **`dll/win32/msg711.acm/msg711.c`** -> AI Confidence: **99.39%**
519. **`dll/win32/msi/action.c`** -> AI Confidence: **99.39%**
520. **`dll/win32/msi/appsearch.c`** -> AI Confidence: **99.39%**
521. **`dll/win32/msi/classes.c`** -> AI Confidence: **99.39%**
522. **`dll/win32/msi/custom.c`** -> AI Confidence: **99.39%**
523. **`dll/win32/msi/msi.c`** -> AI Confidence: **99.39%**
524. **`dll/win32/msi/source.c`** -> AI Confidence: **99.39%**
525. **`dll/win32/msi/upgrade.c`** -> AI Confidence: **99.39%**
526. **`dll/win32/msvfw32/mciwnd.c`** -> AI Confidence: **99.39%**
527. **`dll/win32/msvfw32/msvideo_main.c`** -> AI Confidence: **99.39%**
528. **`dll/win32/mswsock/nsplookup.c`** -> AI Confidence: **99.39%**
529. **`dll/win32/msxml3/schema.c`** -> AI Confidence: **99.39%**
530. **`dll/win32/oleaut32/recinfo.c`** -> AI Confidence: **99.39%**
531. **`dll/win32/oleaut32/usrmarshal.c`** -> AI Confidence: **99.39%**
532. **`dll/win32/oledlg/insobjdlg.c`** -> AI Confidence: **99.39%**
533. **`dll/win32/oledlg/pastespl.c`** -> AI Confidence: **99.39%**
534. **`dll/win32/propsys/propvar.c`** -> AI Confidence: **99.39%**
535. **`dll/win32/riched20/reader.c`** -> AI Confidence: **99.39%**
536. **`dll/win32/riched20/txthost.c`** -> AI Confidence: **99.39%**
537. **`dll/win32/rpcrt4/ndr_clientserver.c`** -> AI Confidence: **99.39%**
538. **`dll/win32/rpcrt4/ndr_es.c`** -> AI Confidence: **99.39%**
539. **`dll/win32/rpcrt4/rpc_binding.c`** -> AI Confidence: **99.39%**
540. **`dll/win32/rsaenh/rsaenh.c`** -> AI Confidence: **99.39%**
541. **`dll/win32/shell32/wine/control.c`** -> AI Confidence: **99.39%**
542. **`dll/win32/shell32/wine/shellord.c`** -> AI Confidence: **99.39%**
543. **`dll/win32/shell32/wine/shellpath.c`** -> AI Confidence: **99.39%**
544. **`dll/win32/shlwapi/path.c`** -> AI Confidence: **99.39%**
545. **`dll/win32/shlwapi/reg.c`** -> AI Confidence: **99.39%**
546. **`dll/win32/shlwapi/string.c`** -> AI Confidence: **99.39%**
547. **`dll/win32/sndblst/sndblst.c`** -> AI Confidence: **99.39%**
548. **`dll/win32/syssetup/install.c`** -> AI Confidence: **99.39%**
549. **`dll/win32/tapi32/assisted.c`** -> AI Confidence: **99.39%**
550. **`dll/win32/usp10/shape.c`** -> AI Confidence: **99.39%**
551. **`dll/win32/wbemprox/reg.c`** -> AI Confidence: **99.39%**
552. **`dll/win32/windowscodecs/icoformat.c`** -> AI Confidence: **99.39%**
553. **`dll/win32/windowscodecs/regsvr.c`** -> AI Confidence: **99.39%**
554. **`dll/win32/windowscodecs/tgaformat.c`** -> AI Confidence: **99.39%**
555. **`dll/win32/wininet/dialogs.c`** -> AI Confidence: **99.39%**
556. **`dll/win32/wininet/ftp.c`** -> AI Confidence: **99.39%**
557. **`dll/win32/wininet/http.c`** -> AI Confidence: **99.39%**
558. **`dll/win32/wininet/utility.c`** -> AI Confidence: **99.39%**
559. **`dll/win32/wintrust/asn.c`** -> AI Confidence: **99.39%**
560. **`dll/win32/wintrust/wintrust_main.c`** -> AI Confidence: **99.39%**
561. **`dll/win32/wldap32/delete.c`** -> AI Confidence: **99.39%**
562. **`dll/win32/wldap32/extended.c`** -> AI Confidence: **99.39%**
563. **`dll/win32/wldap32/init.c`** -> AI Confidence: **99.39%**
564. **`drivers/bluetooth/fbtusb/fbtdev.c`** -> AI Confidence: **99.39%**
565. **`drivers/bluetooth/fbtusb/fbtpnp.c`** -> AI Confidence: **99.39%**
566. **`drivers/bluetooth/fbtusb/fbtpwr.c`** -> AI Confidence: **99.39%**
567. **`drivers/bluetooth/fbtusb/fbtusb.c`** -> AI Confidence: **99.39%**
568. **`drivers/bluetooth/fbtusb/fbtwmi.c`** -> AI Confidence: **99.39%**
569. **`drivers/filesystems/nfs/nfs41_debug.c`** -> AI Confidence: **99.39%**
570. **`drivers/network/netio/netio.c`** -> AI Confidence: **99.39%**
571. **`drivers/network/tcpip/lwip/src/api/api_msg.c`** -> AI Confidence: **99.39%**
572. **`drivers/network/tcpip/lwip/src/api/sockets.c`** -> AI Confidence: **99.39%**
573. **`drivers/network/tcpip/lwip/src/apps/http/httpd.c`** -> AI Confidence: **99.39%**
574. **`drivers/network/tcpip/lwip/src/apps/http/makefsdata/tinydir.h`** -> AI Confidence: **99.39%**
575. **`drivers/network/tcpip/lwip/src/apps/snmp/snmpv3_mbedtls.c`** -> AI Confidence: **99.39%**
576. **`drivers/network/tcpip/lwip/src/apps/sntp/sntp.c`** -> AI Confidence: **99.39%**
577. **`drivers/network/tcpip/lwip/src/core/dns.c`** -> AI Confidence: **99.39%**
578. **`drivers/network/tcpip/lwip/src/core/ipv4/ip4.c`** -> AI Confidence: **99.39%**
579. **`drivers/network/tcpip/lwip/src/core/ipv6/ip6.c`** -> AI Confidence: **99.39%**
580. **`drivers/network/tcpip/lwip/src/include/netif/ppp/pppcrypt.h`** -> AI Confidence: **99.39%**
581. **`drivers/network/tcpip/lwip/src/netif/ppp/auth.c`** -> AI Confidence: **99.39%**
582. **`drivers/network/tcpip/lwip/src/netif/ppp/ccp.c`** -> AI Confidence: **99.39%**
583. **`drivers/network/tcpip/lwip/src/netif/ppp/chap-new.c`** -> AI Confidence: **99.39%**
584. **`drivers/network/tcpip/lwip/src/netif/ppp/ipcp.c`** -> AI Confidence: **99.39%**
585. **`drivers/network/tcpip/lwip/src/netif/ppp/pppoe.c`** -> AI Confidence: **99.39%**
586. **`drivers/network/tcpip/lwip/src/netif/ppp/pppol2tp.c`** -> AI Confidence: **99.39%**
587. **`drivers/network/tcpip/lwip/src/netif/ppp/vj.c`** -> AI Confidence: **99.39%**
588. **`drivers/storage/class/cdrom/autorun.c`** -> AI Confidence: **99.39%**
589. **`drivers/storage/class/cdrom/mmc.c`** -> AI Confidence: **99.39%**
590. **`drivers/storage/class/cdrom/pnppower.c`** -> AI Confidence: **99.39%**
591. **`drivers/wdm/audio/hdaudbus/driver.h`** -> AI Confidence: **99.39%**
592. **`modules/rosapps/applications/cmdutils/vcdcli/vcdcli.c`** -> AI Confidence: **99.39%**
593. **`modules/rosapps/applications/cmdutils/vfdcmd/vfdcmd.c`** -> AI Confidence: **99.39%**
594. **`modules/rosapps/applications/net/ncftp/ncftp/cmds.c`** -> AI Confidence: **99.39%**
595. **`modules/rosapps/applications/net/ncftp/ncftp/progress.c`** -> AI Confidence: **99.39%**
596. **`modules/rosapps/applications/net/tsclient/rdesktop/rdesktop.c`** -> AI Confidence: **99.39%**
597. **`modules/rosapps/applications/net/tsclient/rdesktop/rdpdr.c`** -> AI Confidence: **99.39%**
598. **`modules/rosapps/applications/net/tsclient/rdesktop/uiports/svgawin.c`** -> AI Confidence: **99.39%**
599. **`modules/rosapps/applications/net/tsclient/rdesktop/vnc/vnc.c`** -> AI Confidence: **99.39%**
600. **`modules/rosapps/applications/net/tsclient/rdesktop/xkeymap.c`** -> AI Confidence: **99.39%**
601. **`modules/rosapps/applications/screensavers/matrix/config.c`** -> AI Confidence: **99.39%**
602. **`modules/rosapps/applications/screensavers/mazescr/maze.c`** -> AI Confidence: **99.39%**
603. **`modules/rosapps/applications/sysutils/ctm/ctm.c`** -> AI Confidence: **99.39%**
604. **`modules/rosapps/applications/sysutils/lsdd/lsdd.c`** -> AI Confidence: **99.39%**
605. **`modules/rosapps/applications/sysutils/mkdosfs/mkdosfs.c`** -> AI Confidence: **99.39%**
606. **`modules/rosapps/applications/sysutils/systeminfo/systeminfo.c`** -> AI Confidence: **99.39%**
607. **`modules/rosapps/applications/sysutils/utils/pnpdump/pnpdump.c`** -> AI Confidence: **99.39%**
608. **`modules/rosapps/drivers/vcdrom/vcdrom.c`** -> AI Confidence: **99.39%**
609. **`modules/rosapps/templates/mdi/framewnd.c`** -> AI Confidence: **99.39%**
610. **`modules/rosapps/templates/mdi/panelwnd.c`** -> AI Confidence: **99.39%**
611. **`modules/rostests/apitests/apphelp/apphelp.c`** -> AI Confidence: **99.39%**
612. **`modules/rostests/apitests/apphelp/env.c`** -> AI Confidence: **99.39%**
613. **`modules/rostests/apitests/comctl32/button.c`** -> AI Confidence: **99.39%**
614. **`modules/rostests/apitests/setupapi/SetupDiInstallClassExA.c`** -> AI Confidence: **99.39%**
615. **`modules/rostests/winetests/advapi32/crypt.c`** -> AI Confidence: **99.39%**
616. **`modules/rostests/winetests/comdlg32/filedlg.c`** -> AI Confidence: **99.39%**
617. **`modules/rostests/winetests/crypt32/ctl.c`** -> AI Confidence: **99.39%**
618. **`modules/rostests/winetests/crypt32/object.c`** -> AI Confidence: **99.39%**
619. **`modules/rostests/winetests/dinput/joystick.c`** -> AI Confidence: **99.39%**
620. **`modules/rostests/winetests/fusion/asmname.c`** -> AI Confidence: **99.39%**
621. **`modules/rostests/winetests/gdi32/dc.c`** -> AI Confidence: **99.39%**
622. **`modules/rostests/winetests/gdi32/path.c`** -> AI Confidence: **99.39%**
623. **`modules/rostests/winetests/kernel32/file.c`** -> AI Confidence: **99.39%**
624. **`modules/rostests/winetests/kernel32/loader.c`** -> AI Confidence: **99.39%**
625. **`modules/rostests/winetests/kernel32/path.c`** -> AI Confidence: **99.39%**
626. **`modules/rostests/winetests/kernel32/pipe.c`** -> AI Confidence: **99.39%**
627. **`modules/rostests/winetests/kernel32/profile.c`** -> AI Confidence: **99.39%**
628. **`modules/rostests/winetests/mmdevapi/render.c`** -> AI Confidence: **99.39%**
629. **`modules/rostests/winetests/mscms/profile.c`** -> AI Confidence: **99.39%**
630. **`modules/rostests/winetests/msvcrt/dir.c`** -> AI Confidence: **99.39%**
631. **`modules/rostests/winetests/secur32/ntlm.c`** -> AI Confidence: **99.39%**
632. **`modules/rostests/winetests/shell32/shlexec.c`** -> AI Confidence: **99.39%**
633. **`modules/rostests/winetests/urlmon/protocol.c`** -> AI Confidence: **99.39%**
634. **`modules/rostests/winetests/urlmon/url.c`** -> AI Confidence: **99.39%**
635. **`modules/rostests/winetests/user32/class.c`** -> AI Confidence: **99.39%**
636. **`modules/rostests/winetests/user32/clipboard.c`** -> AI Confidence: **99.39%**
637. **`modules/rostests/winetests/user32/monitor.c`** -> AI Confidence: **99.39%**
638. **`modules/rostests/winetests/user32/static.c`** -> AI Confidence: **99.39%**
639. **`modules/rostests/winetests/user32/text.c`** -> AI Confidence: **99.39%**
640. **`modules/rostests/winetests/winhttp/winhttp.c`** -> AI Confidence: **99.39%**
641. **`modules/rostests/winetests/winspool/info.c`** -> AI Confidence: **99.39%**
642. **`modules/rostests/winetests/wintrust/asn.c`** -> AI Confidence: **99.39%**
643. **`ntoskrnl/kd/kdio.c`** -> AI Confidence: **99.39%**
644. **`sdk/include/c++/stlport/stl/_bitset.h`** -> AI Confidence: **99.39%**
645. **`sdk/include/reactos/libs/libmpg123/mpg123lib_intern.h`** -> AI Confidence: **99.39%**
646. **`sdk/include/reactos/libs/mbedtls/ssl_internal.h`** -> AI Confidence: **99.39%**
647. **`sdk/lib/3rdparty/freetype/src/cff/cffdrivr.c`** -> AI Confidence: **99.39%**
648. **`sdk/lib/3rdparty/freetype/src/cid/cidobjs.c`** -> AI Confidence: **99.39%**
649. **`sdk/lib/3rdparty/freetype/src/gzip/ftgzip.c`** -> AI Confidence: **99.39%**
650. **`sdk/lib/3rdparty/freetype/src/pfr/pfrdrivr.c`** -> AI Confidence: **99.39%**
651. **`sdk/lib/3rdparty/freetype/src/psaux/psintrp.c`** -> AI Confidence: **99.39%**
652. **`sdk/lib/3rdparty/freetype/src/pshinter/pshrec.c`** -> AI Confidence: **99.39%**
653. **`sdk/lib/3rdparty/freetype/src/raster/ftraster.c`** -> AI Confidence: **99.39%**
654. **`sdk/lib/3rdparty/freetype/src/smooth/ftgrays.c`** -> AI Confidence: **99.39%**
655. **`sdk/lib/3rdparty/freetype/src/truetype/ttsubpix.c`** -> AI Confidence: **99.39%**
656. **`sdk/tools/hhpcomp/lzx_compress/lzx_layer.c`** -> AI Confidence: **99.39%**
657. **`sdk/tools/isohybrid/isohybrid.c`** -> AI Confidence: **99.39%**
658. **`sdk/tools/log2lines/options.c`** -> AI Confidence: **99.39%**
659. **`sdk/tools/mkisofs/schilytools/libschily/fconv.c`** -> AI Confidence: **99.39%**
660. **`sdk/tools/mkisofs/schilytools/libschily/getargs.c`** -> AI Confidence: **99.39%**
661. **`sdk/tools/mkisofs/schilytools/libschily/getexecpath.c`** -> AI Confidence: **99.39%**
662. **`sdk/tools/mkisofs/schilytools/mkisofs/boot.c`** -> AI Confidence: **99.39%**
663. **`sdk/tools/mkisofs/schilytools/mkisofs/mkisofs.c`** -> AI Confidence: **99.39%**
664. **`sdk/tools/widl/client.c`** -> AI Confidence: **99.39%**
665. **`sdk/tools/widl/header.c`** -> AI Confidence: **99.39%**
666. **`subsystems/mvdm/ntvdm/cpu/cpu.c`** -> AI Confidence: **99.39%**
667. **`subsystems/mvdm/ntvdm/dos/dem.c`** -> AI Confidence: **99.39%**
668. **`subsystems/mvdm/ntvdm/dos/dos32krnl/bios.c`** -> AI Confidence: **99.39%**
669. **`subsystems/mvdm/ntvdm/dos/dos32krnl/device.c`** -> AI Confidence: **99.39%**
670. **`subsystems/mvdm/ntvdm/dos/dos32krnl/dosfiles.c`** -> AI Confidence: **99.39%**
671. **`subsystems/mvdm/ntvdm/dos/dos32krnl/memory.c`** -> AI Confidence: **99.39%**
672. **`subsystems/mvdm/ntvdm/hardware/video/svga.c`** -> AI Confidence: **99.39%**
673. **`win32ss/gdi/gdi32/wine/enhmfdrv/graphics.c`** -> AI Confidence: **99.39%**
674. **`win32ss/printing/base/printui/printui.c`** -> AI Confidence: **99.39%**
675. **`dll/opengl/mesa/points.c`** -> AI Confidence: **99.35%**
676. **`dll/win32/avifil32/api.c`** -> AI Confidence: **99.35%**
677. **`dll/win32/avifil32/avifile.c`** -> AI Confidence: **99.35%**
678. **`dll/win32/comctl32/header.c`** -> AI Confidence: **99.35%**
679. **`dll/win32/comctl32/rebar.c`** -> AI Confidence: **99.35%**
680. **`dll/win32/crypt32/sip.c`** -> AI Confidence: **99.35%**
681. **`dll/win32/dbghelp/msc.c`** -> AI Confidence: **99.35%**
682. **`dll/win32/fusion/asmcache.c`** -> AI Confidence: **99.35%**
683. **`dll/win32/msftedit/msftedit_main.c`** -> AI Confidence: **99.35%**
684. **`dll/win32/ole32/ole2.c`** -> AI Confidence: **99.35%**
685. **`dll/win32/ole32/storage32.c`** -> AI Confidence: **99.35%**
686. **`modules/rosapps/applications/net/tsclient/rdesktop/disk.c`** -> AI Confidence: **99.35%**
687. **`modules/rostests/winetests/kernel32/volume.c`** -> AI Confidence: **99.35%**
688. **`sdk/lib/3rdparty/freetype/src/type1/t1objs.c`** -> AI Confidence: **99.35%**
689. **`base/applications/drwtsn32/sysinfo.cpp`** -> AI Confidence: **99.34%**
690. **`base/applications/sndrec32/sndrec32.cpp`** -> AI Confidence: **99.34%**
691. **`base/applications/sndrec32/stdafx.h`** -> AI Confidence: **99.34%**
692. **`dll/opengl/glu32/src/libnurbs/internals/patch.cc`** -> AI Confidence: **99.34%**
693. **`dll/shellext/acppage/CLayerUIPropPage.cpp`** -> AI Confidence: **99.34%**
694. **`dll/win32/shell32/dialogs/drvdefext.cpp`** -> AI Confidence: **99.34%**
695. **`modules/rosapps/applications/explorer-old/taskbar/startmenu.cpp`** -> AI Confidence: **99.34%**
696. **`modules/rosapps/applications/sysutils/regexpl/ShellCommandDir.cpp`** -> AI Confidence: **99.34%**
697. **`modules/rosapps/applications/sysutils/regexpl/ShellCommandSetValue.cpp`** -> AI Confidence: **99.34%**
698. **`modules/rosapps/applications/sysutils/regexpl/ShellCommandValue.cpp`** -> AI Confidence: **99.34%**
699. **`modules/rosapps/applications/sysutils/utils/sdkparse/tokenize.cpp`** -> AI Confidence: **99.34%**
700. **`modules/rosapps/templates/mdi/StdAfx.h`** -> AI Confidence: **99.34%**
701. **`modules/rostests/apitests/atl/CString.cpp`** -> AI Confidence: **99.34%**
702. **`modules/rostests/apitests/shell32/CFSFolder.cpp`** -> AI Confidence: **99.34%**
703. **`modules/rostests/winetests/msvcrt/precomp.h`** -> AI Confidence: **99.34%**
704. **`sdk/lib/3rdparty/stlport/src/details/fstream_unistd.cpp`** -> AI Confidence: **99.34%**
705. **`sdk/lib/3rdparty/stlport/src/time_facets.cpp`** -> AI Confidence: **99.34%**
706. **`sdk/tools/cabman/cabman.cxx`** -> AI Confidence: **99.34%**
707. **`base/applications/cmdutils/dbgprint/dbgprint.c`** -> AI Confidence: **99.34%**
708. **`base/applications/cmdutils/fc/fc.c`** -> AI Confidence: **99.34%**
709. **`base/applications/cmdutils/hostname/hostname.c`** -> AI Confidence: **99.34%**
710. **`base/applications/cmdutils/tree/tree.c`** -> AI Confidence: **99.34%**
711. **`base/applications/cmdutils/xcopy/xcopy.c`** -> AI Confidence: **99.34%**
712. **`base/applications/msconfig/msconfig.c`** -> AI Confidence: **99.34%**
713. **`base/applications/mscutils/eventvwr/eventvwr.c`** -> AI Confidence: **99.34%**
714. **`base/services/nfsd/service.c`** -> AI Confidence: **99.34%**
715. **`base/services/nfsd/symlink.c`** -> AI Confidence: **99.34%**
716. **`base/services/nfsd/upcall.c`** -> AI Confidence: **99.34%**
717. **`base/services/telnetd/syslog.c`** -> AI Confidence: **99.34%**
718. **`base/setup/lib/utils/volutil.c`** -> AI Confidence: **99.34%**
719. **`base/system/lsass/lsass.c`** -> AI Confidence: **99.34%**
720. **`base/system/services/database.c`** -> AI Confidence: **99.34%**
721. **`base/system/winlogon/sas.c`** -> AI Confidence: **99.34%**
722. **`boot/freeldr/freeldr/arch/i386/pc/machpc.c`** -> AI Confidence: **99.34%**
723. **`boot/freeldr/freeldr/ntldr/wlregistry.c`** -> AI Confidence: **99.34%**
724. **`dll/3rdparty/libjpeg/djpeg.c`** -> AI Confidence: **99.34%**
725. **`dll/3rdparty/libpng/pngpriv.h`** -> AI Confidence: **99.34%**
726. **`dll/3rdparty/libtiff/tif_pixarlog.c`** -> AI Confidence: **99.34%**
727. **`dll/3rdparty/libtirpc/src/xdr_array.c`** -> AI Confidence: **99.34%**
728. **`dll/3rdparty/mbedtls/camellia.c`** -> AI Confidence: **99.34%**
729. **`dll/3rdparty/mbedtls/ssl_cache.c`** -> AI Confidence: **99.34%**
730. **`dll/3rdparty/mbedtls/ssl_ciphersuites.c`** -> AI Confidence: **99.34%**
731. **`dll/3rdparty/mbedtls/xtea.c`** -> AI Confidence: **99.34%**
732. **`dll/appcompat/apphelp/shimeng.c`** -> AI Confidence: **99.34%**
733. **`dll/appcompat/shims/layer/vmhorizon.c`** -> AI Confidence: **99.34%**
734. **`dll/cpl/intl/languages.c`** -> AI Confidence: **99.34%**
735. **`dll/directx/d3d9/d3d9_callbacks.c`** -> AI Confidence: **99.34%**
736. **`dll/directx/wine/d3dxof/parsing.c`** -> AI Confidence: **99.34%**
737. **`dll/opengl/mesa/shade.c`** -> AI Confidence: **99.34%**
738. **`dll/opengl/mesa/xform.c`** -> AI Confidence: **99.34%**
739. **`dll/shellext/deskmon/deskmon.c`** -> AI Confidence: **99.34%**
740. **`dll/win32/cards/cards.c`** -> AI Confidence: **99.34%**
741. **`dll/win32/comctl32/draglist.c`** -> AI Confidence: **99.34%**
742. **`dll/win32/crypt32/message.c`** -> AI Confidence: **99.34%**
743. **`dll/win32/crypt32/regstore.c`** -> AI Confidence: **99.34%**
744. **`dll/win32/gdiplus/graphicspath.c`** -> AI Confidence: **99.34%**
745. **`dll/win32/ifmon/ip.c`** -> AI Confidence: **99.34%**
746. **`dll/win32/kernel32/winnls/string/locale.c`** -> AI Confidence: **99.34%**
747. **`dll/win32/msgina/shutdown.c`** -> AI Confidence: **99.34%**
748. **`dll/win32/msi/font.c`** -> AI Confidence: **99.34%**
749. **`dll/win32/msvcrt/mbcs.c`** -> AI Confidence: **99.34%**
750. **`dll/win32/netapi32/netlogon.c`** -> AI Confidence: **99.34%**
751. **`dll/win32/netcfgx/tcpipconf_notify.c`** -> AI Confidence: **99.34%**
752. **`dll/win32/newdev/wizard.c`** -> AI Confidence: **99.34%**
753. **`dll/win32/oleaut32/safearray.c`** -> AI Confidence: **99.34%**
754. **`dll/win32/qmgr/file.c`** -> AI Confidence: **99.34%**
755. **`dll/win32/shimgvw/shimgvw.c`** -> AI Confidence: **99.34%**
756. **`dll/win32/syssetup/security.c`** -> AI Confidence: **99.34%**
757. **`dll/win32/twain_32/twain32_main.c`** -> AI Confidence: **99.34%**
758. **`dll/win32/vbscript/lex.c`** -> AI Confidence: **99.34%**
759. **`dll/win32/wbemprox/process.c`** -> AI Confidence: **99.34%**
760. **`dll/win32/wbemprox/service.c`** -> AI Confidence: **99.34%**
761. **`dll/win32/windowscodecs/uuid.c`** -> AI Confidence: **99.34%**
762. **`dll/win32/wininet/inflate.c`** -> AI Confidence: **99.34%**
763. **`drivers/bus/acpi/acpica/dispatcher/dsargs.c`** -> AI Confidence: **99.34%**
764. **`drivers/bus/acpi/acpica/dispatcher/dscontrol.c`** -> AI Confidence: **99.34%**
765. **`drivers/bus/acpi/acpica/dispatcher/dsinit.c`** -> AI Confidence: **99.34%**
766. **`drivers/bus/acpi/acpica/dispatcher/dsmthdat.c`** -> AI Confidence: **99.34%**
767. **`drivers/bus/acpi/acpica/events/evregion.c`** -> AI Confidence: **99.34%**
768. **`drivers/bus/acpi/acpica/events/evxface.c`** -> AI Confidence: **99.34%**
769. **`drivers/bus/acpi/acpica/executer/excreate.c`** -> AI Confidence: **99.34%**
770. **`drivers/bus/acpi/acpica/executer/exdump.c`** -> AI Confidence: **99.34%**
771. **`drivers/bus/acpi/acpica/executer/exfield.c`** -> AI Confidence: **99.34%**
772. **`drivers/bus/acpi/acpica/executer/exfldio.c`** -> AI Confidence: **99.34%**
773. **`drivers/bus/acpi/acpica/executer/exoparg2.c`** -> AI Confidence: **99.34%**
774. **`drivers/bus/acpi/acpica/executer/exoparg3.c`** -> AI Confidence: **99.34%**
775. **`drivers/bus/acpi/acpica/executer/exoparg6.c`** -> AI Confidence: **99.34%**
776. **`drivers/bus/acpi/acpica/executer/exprep.c`** -> AI Confidence: **99.34%**
777. **`drivers/bus/acpi/acpica/executer/exresnte.c`** -> AI Confidence: **99.34%**
778. **`drivers/bus/acpi/acpica/executer/exresolv.c`** -> AI Confidence: **99.34%**
779. **`drivers/bus/acpi/acpica/executer/exresop.c`** -> AI Confidence: **99.34%**
780. **`drivers/bus/acpi/acpica/executer/exserial.c`** -> AI Confidence: **99.34%**
781. **`drivers/bus/acpi/acpica/executer/exstore.c`** -> AI Confidence: **99.34%**
782. **`drivers/bus/acpi/acpica/include/platform/acenvex.h`** -> AI Confidence: **99.34%**
783. **`drivers/bus/acpi/acpica/namespace/nsaccess.c`** -> AI Confidence: **99.34%**
784. **`drivers/bus/acpi/acpica/namespace/nseval.c`** -> AI Confidence: **99.34%**
785. **`drivers/bus/acpi/acpica/namespace/nsload.c`** -> AI Confidence: **99.34%**
786. **`drivers/bus/acpi/acpica/parser/psobject.c`** -> AI Confidence: **99.34%**
787. **`drivers/bus/acpi/acpica/parser/psopinfo.c`** -> AI Confidence: **99.34%**
788. **`drivers/bus/acpi/acpica/parser/pstree.c`** -> AI Confidence: **99.34%**
789. **`drivers/bus/acpi/acpica/utilities/utdelete.c`** -> AI Confidence: **99.34%**
790. **`drivers/bus/acpi/acpica/utilities/utxfinit.c`** -> AI Confidence: **99.34%**
791. **`drivers/bus/acpi_new/uacpi/source/sleep.c`** -> AI Confidence: **99.34%**
792. **`drivers/filesystems/ext2/src/fileinfo.c`** -> AI Confidence: **99.34%**
793. **`drivers/input/kbdclass/kbdclass.c`** -> AI Confidence: **99.34%**
794. **`drivers/network/tcpip/lwip/src/apps/snmp/snmp_mib2_snmp.c`** -> AI Confidence: **99.34%**
795. **`drivers/network/tcpip/lwip/src/core/ipv6/ip6_addr.c`** -> AI Confidence: **99.34%**
796. **`drivers/network/tcpip/lwip/src/netif/ppp/fsm.c`** -> AI Confidence: **99.34%**
797. **`drivers/network/tcpip/lwip/src/netif/ppp/upap.c`** -> AI Confidence: **99.34%**
798. **`drivers/storage/class/cdrom/common.c`** -> AI Confidence: **99.34%**
799. **`drivers/storage/class/classpnp/class.c`** -> AI Confidence: **99.34%**
800. **`drivers/storage/class/classpnp/power.c`** -> AI Confidence: **99.34%**
801. **`drivers/storage/class/disk/disk.c`** -> AI Confidence: **99.34%**
802. **`drivers/storage/ide/atapi/atapi.c`** -> AI Confidence: **99.34%**
803. **`hal/halx86/mp/apic.c`** -> AI Confidence: **99.34%**
804. **`modules/rosapps/applications/devutils/syscalldump/syscalldump.c`** -> AI Confidence: **99.34%**
805. **`modules/rosapps/applications/net/dhcpd/src/parsing/parser.c`** -> AI Confidence: **99.34%**
806. **`modules/rosapps/applications/net/ncftp/ncftp/shell.c`** -> AI Confidence: **99.34%**
807. **`modules/rosapps/applications/screensavers/matrix/matrix.c`** -> AI Confidence: **99.34%**
808. **`modules/rosapps/applications/screensavers/matrix/settings.c`** -> AI Confidence: **99.34%**
809. **`modules/rosapps/applications/sysutils/gettype/gettype.c`** -> AI Confidence: **99.34%**
810. **`modules/rosapps/applications/sysutils/utils/sdkparse/EnumFilesImpl.h`** -> AI Confidence: **99.34%**
811. **`modules/rosapps/templates/dialog/dialog.c`** -> AI Confidence: **99.34%**
812. **`modules/rosapps/templates/dialog/page2.c`** -> AI Confidence: **99.34%**
813. **`modules/rosapps/templates/dialog/page3.c`** -> AI Confidence: **99.34%**
814. **`modules/rosapps/templates/mdi/ros2win.c`** -> AI Confidence: **99.34%**
815. **`modules/rostests/apitests/compiler/ms/seh/xcpt4u.c`** -> AI Confidence: **99.34%**
816. **`modules/rostests/apitests/crt/_vsnprintf.c`** -> AI Confidence: **99.34%**
817. **`modules/rostests/apitests/crt/_vsnwprintf.c`** -> AI Confidence: **99.34%**
818. **`modules/rostests/apitests/crt/fpcontrol.c`** -> AI Confidence: **99.34%**
819. **`modules/rostests/apitests/dnsapi/DnsQuery.c`** -> AI Confidence: **99.34%**
820. **`modules/rostests/apitests/msvcrt/splitpath.c`** -> AI Confidence: **99.34%**
821. **`modules/rostests/apitests/winspool/EnumPrinters.c`** -> AI Confidence: **99.34%**
822. **`modules/rostests/apitests/winspool/GetPrinter.c`** -> AI Confidence: **99.34%**
823. **`modules/rostests/apitests/winspool/GetPrinterData.c`** -> AI Confidence: **99.34%**
824. **`modules/rostests/apitests/winspool/IsValidDevmode.c`** -> AI Confidence: **99.34%**
825. **`modules/rostests/drivers/tcpip/InterfaceInfo.c`** -> AI Confidence: **99.34%**
826. **`modules/rostests/kmtests/kmtest_drv/kmtest_standalone.c`** -> AI Confidence: **99.34%**
827. **`modules/rostests/tests/copymove/copymove.c`** -> AI Confidence: **99.34%**
828. **`modules/rostests/tests/create-links/create-links.c`** -> AI Confidence: **99.34%**
829. **`modules/rostests/tests/dirdlg/dirdlg.c`** -> AI Confidence: **99.34%**
830. **`modules/rostests/tests/diskspeed/diskspeed.c`** -> AI Confidence: **99.34%**
831. **`modules/rostests/tests/dnsapi/dnsapi.c`** -> AI Confidence: **99.34%**
832. **`modules/rostests/tests/regdump/regcmds.c`** -> AI Confidence: **99.34%**
833. **`modules/rostests/tests/wcstombs-tests/wcstombs-tests.c`** -> AI Confidence: **99.34%**
834. **`modules/rostests/win32/msvcrt/fileio/main.c`** -> AI Confidence: **99.34%**
835. **`modules/rostests/winetests/crypt32/base64.c`** -> AI Confidence: **99.34%**
836. **`modules/rostests/winetests/gdi32/pen.c`** -> AI Confidence: **99.34%**
837. **`modules/rostests/winetests/kernel32/drive.c`** -> AI Confidence: **99.34%**
838. **`modules/rostests/winetests/localspl/localmon.c`** -> AI Confidence: **99.34%**
839. **`modules/rostests/winetests/secur32/negotiate.c`** -> AI Confidence: **99.34%**
840. **`modules/rostests/winetests/serialui/confdlg.c`** -> AI Confidence: **99.34%**
841. **`modules/rostests/winetests/shell32/shlfileop.c`** -> AI Confidence: **99.34%**
842. **`modules/rostests/winetests/ucrtbase/scanf.c`** -> AI Confidence: **99.34%**
843. **`modules/rostests/winetests/user32/menu.c`** -> AI Confidence: **99.34%**
844. **`modules/rostests/winetests/winhttp/url.c`** -> AI Confidence: **99.34%**
845. **`modules/rostests/winetests/winmm/joystick.c`** -> AI Confidence: **99.34%**
846. **`modules/rostests/winetests/winmm/mmio.c`** -> AI Confidence: **99.34%**
847. **`modules/rostests/winetests/ws2_32/protocol.c`** -> AI Confidence: **99.34%**
848. **`ntoskrnl/fstub/disksup.c`** -> AI Confidence: **99.34%**
849. **`ntoskrnl/include/internal/arch/intrin_i.h`** -> AI Confidence: **99.34%**
850. **`ntoskrnl/include/internal/arch/ke.h`** -> AI Confidence: **99.34%**
851. **`ntoskrnl/include/internal/arch/mm.h`** -> AI Confidence: **99.34%**
852. **`ntoskrnl/kd/kdmain.c`** -> AI Confidence: **99.34%**
853. **`ntoskrnl/mm/section.c`** -> AI Confidence: **99.34%**
854. **`ntoskrnl/tests/fsrtl.c`** -> AI Confidence: **99.34%**
855. **`sdk/include/c++/stlport/iomanip.h`** -> AI Confidence: **99.34%**
856. **`sdk/include/c++/stlport/stl/config/_apple.h`** -> AI Confidence: **99.34%**
857. **`sdk/include/c++/stlport/stl/config/_windows.h`** -> AI Confidence: **99.34%**
858. **`sdk/include/c++/stlport/streambuf.h`** -> AI Confidence: **99.34%**
859. **`sdk/include/ndk/arch/ketypes.h`** -> AI Confidence: **99.34%**
860. **`sdk/include/ndk/arch/mmtypes.h`** -> AI Confidence: **99.34%**
861. **`sdk/include/reactos/libs/mbedtls/pkcs12.h`** -> AI Confidence: **99.34%**
862. **`sdk/include/reactos/libs/mbedtls/pkcs5.h`** -> AI Confidence: **99.34%**
863. **`sdk/lib/3rdparty/freetype/src/autofit/aflatin.c`** -> AI Confidence: **99.34%**
864. **`sdk/lib/3rdparty/freetype/src/autofit/aflatin2.c`** -> AI Confidence: **99.34%**
865. **`sdk/lib/3rdparty/freetype/src/autofit/afloader.c`** -> AI Confidence: **99.34%**
866. **`sdk/lib/3rdparty/freetype/src/base/ftstroke.c`** -> AI Confidence: **99.34%**
867. **`sdk/lib/3rdparty/freetype/src/bdf/bdflib.c`** -> AI Confidence: **99.34%**
868. **`sdk/lib/3rdparty/freetype/src/cid/cidparse.c`** -> AI Confidence: **99.34%**
869. **`sdk/lib/3rdparty/freetype/src/gzip/infblock.c`** -> AI Confidence: **99.34%**
870. **`sdk/lib/3rdparty/freetype/src/gzip/infcodes.c`** -> AI Confidence: **99.34%**
871. **`sdk/lib/3rdparty/freetype/src/gzip/infutil.c`** -> AI Confidence: **99.34%**
872. **`sdk/lib/3rdparty/freetype/src/pcf/pcfread.c`** -> AI Confidence: **99.34%**
873. **`sdk/lib/3rdparty/freetype/src/pfr/pfrgload.c`** -> AI Confidence: **99.34%**
874. **`sdk/lib/3rdparty/freetype/src/pfr/pfrsbit.c`** -> AI Confidence: **99.34%**
875. **`sdk/lib/3rdparty/freetype/src/psaux/afmparse.c`** -> AI Confidence: **99.34%**
876. **`sdk/lib/3rdparty/freetype/src/psaux/psblues.c`** -> AI Confidence: **99.34%**
877. **`sdk/lib/3rdparty/freetype/src/psaux/psfont.c`** -> AI Confidence: **99.34%**
878. **`sdk/lib/3rdparty/freetype/src/pshinter/pshalgo.c`** -> AI Confidence: **99.34%**
879. **`sdk/lib/3rdparty/freetype/src/raster/ftrend1.c`** -> AI Confidence: **99.34%**
880. **`sdk/lib/3rdparty/freetype/src/sfnt/pngshim.c`** -> AI Confidence: **99.34%**
881. **`sdk/lib/3rdparty/freetype/src/sfnt/sfwoff.c`** -> AI Confidence: **99.34%**
882. **`sdk/lib/3rdparty/freetype/src/sfnt/sfwoff2.c`** -> AI Confidence: **99.34%**
883. **`sdk/lib/3rdparty/freetype/src/sfnt/ttbdf.c`** -> AI Confidence: **99.34%**
884. **`sdk/lib/3rdparty/freetype/src/sfnt/ttkern.c`** -> AI Confidence: **99.34%**
885. **`sdk/lib/3rdparty/freetype/src/sfnt/ttload.c`** -> AI Confidence: **99.34%**
886. **`sdk/lib/3rdparty/freetype/src/sfnt/ttmtx.c`** -> AI Confidence: **99.34%**
887. **`sdk/lib/3rdparty/freetype/src/sfnt/ttpost.c`** -> AI Confidence: **99.34%**
888. **`sdk/lib/3rdparty/freetype/src/smooth/ftsmooth.c`** -> AI Confidence: **99.34%**
889. **`sdk/lib/3rdparty/freetype/src/type1/t1afm.c`** -> AI Confidence: **99.34%**
890. **`sdk/lib/3rdparty/freetype/src/type1/t1parse.c`** -> AI Confidence: **99.34%**
891. **`sdk/lib/3rdparty/freetype/src/type42/t42objs.c`** -> AI Confidence: **99.34%**
892. **`sdk/lib/3rdparty/freetype/src/type42/t42parse.c`** -> AI Confidence: **99.34%**
893. **`sdk/lib/3rdparty/stlport/src/c_locale.c`** -> AI Confidence: **99.34%**
894. **`sdk/tools/create_nls/create_nls.c`** -> AI Confidence: **99.34%**
895. **`sdk/tools/fatten/fatten.c`** -> AI Confidence: **99.34%**
896. **`sdk/tools/geninc/geninc.c`** -> AI Confidence: **99.34%**
897. **`sdk/tools/hhpcomp/lzx_compress/lz_nonslide.c`** -> AI Confidence: **99.34%**
898. **`sdk/tools/mkhive/mkhive.c`** -> AI Confidence: **99.34%**
899. **`sdk/tools/mkisofs/schilytools/include/schily/device.h`** -> AI Confidence: **99.34%**
900. **`sdk/tools/mkisofs/schilytools/include/schily/param.h`** -> AI Confidence: **99.34%**
901. **`sdk/tools/mkisofs/schilytools/libmdigest/byte_order.h`** -> AI Confidence: **99.34%**
902. **`sdk/tools/mkisofs/schilytools/libschily/astoll.c`** -> AI Confidence: **99.34%**
903. **`sdk/tools/mkisofs/schilytools/mkisofs/name.c`** -> AI Confidence: **99.34%**
904. **`sdk/tools/mkisofs/schilytools/mkisofs/rock.c`** -> AI Confidence: **99.34%**
905. **`sdk/tools/pefixup.c`** -> AI Confidence: **99.34%**
906. **`sdk/tools/spec2def/spec2def.c`** -> AI Confidence: **99.34%**
907. **`sdk/tools/unicode/string.c`** -> AI Confidence: **99.34%**
908. **`subsystems/csr/csrss/csrss.c`** -> AI Confidence: **99.34%**
909. **`subsystems/mvdm/ntvdm/bios/umamgr.c`** -> AI Confidence: **99.34%**
910. **`subsystems/mvdm/ntvdm/hardware/dma.c`** -> AI Confidence: **99.34%**
911. **`subsystems/mvdm/ntvdm/hardware/ppi.c`** -> AI Confidence: **99.34%**
912. **`subsystems/mvdm/ntvdm/int32.c`** -> AI Confidence: **99.34%**
913. **`win32ss/drivers/videoprt/dispatch.c`** -> AI Confidence: **99.34%**
914. **`win32ss/gdi/ntgdi/freetype.c`** -> AI Confidence: **99.34%**
915. **`win32ss/user/ntuser/main.c`** -> AI Confidence: **99.34%**
916. **`win32ss/user/winsrv/concfg/concfg.h`** -> AI Confidence: **99.34%**
917. **`win32ss/user/winsrv/consrv/console.c`** -> AI Confidence: **99.34%**
918. **`win32ss/user/winsrv/consrv/frontends/gui/guisettings.c`** -> AI Confidence: **99.34%**
919. **`win32ss/user/winsrv/usersrv/harderror.c`** -> AI Confidence: **99.34%**
920. **`sdk/lib/3rdparty/freetype/src/gzip/zutil.h`** -> AI Confidence: **99.33%**
921. **`base/applications/cmdutils/certutil/hashfile.cpp`** -> AI Confidence: **99.32%**
922. **`base/ctf/ctfmon/CRegWatcher.cpp`** -> AI Confidence: **99.32%**
923. **`dll/opengl/glu32/src/libnurbs/internals/monoTriangulationBackend.cc`** -> AI Confidence: **99.32%**
924. **`dll/opengl/glu32/src/libnurbs/nurbtess/sampleCompTop.cc`** -> AI Confidence: **99.32%**
925. **`dll/win32/devmgr/properties/devprblm.cpp`** -> AI Confidence: **99.32%**
926. **`dll/win32/shell32/dialogs/drive.cpp`** -> AI Confidence: **99.32%**
927. **`dll/win32/shell32/shlexec.cpp`** -> AI Confidence: **99.32%**
928. **`drivers/wdm/audio/drivers/CMIDriver/adapter.hpp`** -> AI Confidence: **99.32%**
929. **`drivers/wdm/audio/drivers/CMIDriver/minwave.cpp`** -> AI Confidence: **99.32%**
930. **`drivers/wdm/audio/hdaudbus/fdo.cpp`** -> AI Confidence: **99.32%**
931. **`drivers/wdm/audio/hdaudbus/sof-tplg.cpp`** -> AI Confidence: **99.32%**
932. **`modules/rosapps/applications/explorer-old/taskbar/taskbar.cpp`** -> AI Confidence: **99.32%**
933. **`modules/rosapps/applications/explorer-old/taskbar/traynotify.cpp`** -> AI Confidence: **99.32%**
934. **`modules/rosapps/applications/sysutils/regexpl/Completion.cpp`** -> AI Confidence: **99.32%**
935. **`modules/rosapps/applications/sysutils/regexpl/ShellCommandDeleteKey.cpp`** -> AI Confidence: **99.32%**
936. **`modules/rosapps/applications/sysutils/regexpl/ShellCommandNewKey.cpp`** -> AI Confidence: **99.32%**
937. **`modules/rostests/apitests/atl/CRegKey.cpp`** -> AI Confidence: **99.32%**
938. **`modules/rostests/apitests/shell32/GetDisplayNameOf.cpp`** -> AI Confidence: **99.32%**
939. **`modules/rostests/apitests/shell32/ShellExec_RunDLL.cpp`** -> AI Confidence: **99.32%**
940. **`modules/rostests/tests/primitives/primitives.cpp`** -> AI Confidence: **99.32%**
941. **`ntoskrnl/mm/ARM3/wslist.cpp`** -> AI Confidence: **99.32%**
942. **`sdk/tools/pipetools/piperead.cpp`** -> AI Confidence: **99.32%**
943. **`base/applications/cmdutils/sort/sort.c`** -> AI Confidence: **99.32%**
944. **`base/applications/msconfig_new/regutils.c`** -> AI Confidence: **99.32%**
945. **`base/applications/mscutils/eventvwr/evtdetctl.c`** -> AI Confidence: **99.32%**
946. **`base/applications/mscutils/servman/mainwnd.c`** -> AI Confidence: **99.32%**
947. **`base/applications/mstsc/connectdialog.c`** -> AI Confidence: **99.32%**
948. **`base/applications/mstsc/mppc.c`** -> AI Confidence: **99.32%**
949. **`base/applications/network/net/cmdStatistics.c`** -> AI Confidence: **99.32%**
950. **`base/applications/network/nslookup/nslookup.c`** -> AI Confidence: **99.32%**
951. **`base/applications/notepad/main.c`** -> AI Confidence: **99.32%**
952. **`base/applications/notepad/printing.c`** -> AI Confidence: **99.32%**
953. **`base/applications/regedit/childwnd.c`** -> AI Confidence: **99.32%**
954. **`base/setup/usetup/keytrans.c`** -> AI Confidence: **99.32%**
955. **`base/shell/cmd/cmd.c`** -> AI Confidence: **99.32%**
956. **`base/shell/cmd/ver.c`** -> AI Confidence: **99.32%**
957. **`base/system/diskpart/format.c`** -> AI Confidence: **99.32%**
958. **`base/system/services/services.c`** -> AI Confidence: **99.32%**
959. **`base/system/smss/smss.c`** -> AI Confidence: **99.32%**
960. **`boot/freeldr/freeldr/ntldr/wlmemory.c`** -> AI Confidence: **99.32%**
961. **`boot/freeldr/tools/rcopy.c`** -> AI Confidence: **99.32%**
962. **`dll/3rdparty/dxtn/txc_compress_dxtn.c`** -> AI Confidence: **99.32%**
963. **`dll/3rdparty/libjpeg/jcdctmgr.c`** -> AI Confidence: **99.32%**
964. **`dll/3rdparty/libjpeg/jddctmgr.c`** -> AI Confidence: **99.32%**
965. **`dll/3rdparty/libjpeg/jfdctfst.c`** -> AI Confidence: **99.32%**
966. **`dll/3rdparty/libjpeg/jfdctint.c`** -> AI Confidence: **99.32%**
967. **`dll/3rdparty/libjpeg/jidctflt.c`** -> AI Confidence: **99.32%**
968. **`dll/3rdparty/libjpeg/jidctfst.c`** -> AI Confidence: **99.32%**
969. **`dll/3rdparty/libjpeg/jidctint.c`** -> AI Confidence: **99.32%**
970. **`dll/3rdparty/libjpeg/jmemmgr.c`** -> AI Confidence: **99.32%**
971. **`dll/3rdparty/libpng/pngrtran.c`** -> AI Confidence: **99.32%**
972. **`dll/3rdparty/libtiff/tif_getimage.c`** -> AI Confidence: **99.32%**
973. **`dll/3rdparty/libtiff/tif_print.c`** -> AI Confidence: **99.32%**
974. **`dll/3rdparty/mbedtls/version_features.c`** -> AI Confidence: **99.32%**
975. **`dll/cpl/desk/desktop.c`** -> AI Confidence: **99.32%**
976. **`dll/cpl/hotplug/enum.c`** -> AI Confidence: **99.32%**
977. **`dll/cpl/input/edit_dialog.c`** -> AI Confidence: **99.32%**
978. **`dll/cpl/openglcfg/general.c`** -> AI Confidence: **99.32%**
979. **`dll/cpl/sysdm/virtmem.c`** -> AI Confidence: **99.32%**
980. **`dll/directx/ddraw/cleanup.c`** -> AI Confidence: **99.32%**
981. **`dll/directx/wine/d3dx9_36/txc_fetch_dxtn.c`** -> AI Confidence: **99.32%**
982. **`dll/ntdll/ldr/verifier.c`** -> AI Confidence: **99.32%**
983. **`dll/opengl/glu32/src/libtess/normal.c`** -> AI Confidence: **99.32%**
984. **`dll/win32/advapi32/wine/crypt_des.c`** -> AI Confidence: **99.32%**
985. **`dll/win32/fmifs/chkdsk.c`** -> AI Confidence: **99.32%**
986. **`dll/win32/fmifs/format.c`** -> AI Confidence: **99.32%**
987. **`dll/win32/framedyn/main.c`** -> AI Confidence: **99.32%**
988. **`dll/win32/hhctrl.ocx/index.c`** -> AI Confidence: **99.32%**
989. **`dll/win32/kernel32/client/dosdev.c`** -> AI Confidence: **99.32%**
990. **`dll/win32/kernel32/client/file/move.c`** -> AI Confidence: **99.32%**
991. **`dll/win32/mciavi32/info.c`** -> AI Confidence: **99.32%**
992. **`dll/win32/msports/classinst.c`** -> AI Confidence: **99.32%**
993. **`dll/win32/msxml3/xdr.c`** -> AI Confidence: **99.32%**
994. **`dll/win32/netapi32/user.c`** -> AI Confidence: **99.32%**
995. **`dll/win32/newdev/newdev.c`** -> AI Confidence: **99.32%**
996. **`dll/win32/samsrv/setup.c`** -> AI Confidence: **99.32%**
997. **`dll/win32/syssetup/netinstall.c`** -> AI Confidence: **99.32%**
998. **`dll/win32/userenv/profile.c`** -> AI Confidence: **99.32%**
999. **`drivers/base/bootvid/framebuf/bootvid.c`** -> AI Confidence: **99.32%**
1000. **`drivers/base/bootvid/i386/xbox/bootvid.c`** -> AI Confidence: **99.32%**
1001. **`drivers/bus/acpi/acpica/dispatcher/dswscope.c`** -> AI Confidence: **99.32%**
1002. **`drivers/bus/acpi/acpica/events/evgpeutil.c`** -> AI Confidence: **99.32%**
1003. **`drivers/bus/acpi/acpica/events/evxfevnt.c`** -> AI Confidence: **99.32%**
1004. **`drivers/bus/acpi/acpica/executer/exdebug.c`** -> AI Confidence: **99.32%**
1005. **`drivers/bus/acpi/acpica/executer/exstorob.c`** -> AI Confidence: **99.32%**
1006. **`drivers/bus/acpi/acpica/hardware/hwregs.c`** -> AI Confidence: **99.32%**
1007. **`drivers/bus/acpi/acpica/hardware/hwxface.c`** -> AI Confidence: **99.32%**
1008. **`drivers/bus/acpi/acpica/namespace/nsobject.c`** -> AI Confidence: **99.32%**
1009. **`drivers/bus/acpi/acpica/namespace/nswalk.c`** -> AI Confidence: **99.32%**
1010. **`drivers/bus/acpi/acpica/resources/rsinfo.c`** -> AI Confidence: **99.32%**
1011. **`drivers/bus/acpi/acpica/resources/rslist.c`** -> AI Confidence: **99.32%**
1012. **`drivers/bus/acpi/acpica/resources/rsmisc.c`** -> AI Confidence: **99.32%**
1013. **`drivers/bus/acpi/acpica/tables/tbfind.c`** -> AI Confidence: **99.32%**
1014. **`drivers/bus/acpi/acpica/utilities/utaddress.c`** -> AI Confidence: **99.32%**
1015. **`drivers/bus/acpi/acpica/utilities/utcopy.c`** -> AI Confidence: **99.32%**
1016. **`drivers/bus/acpi/acpica/utilities/uteval.c`** -> AI Confidence: **99.32%**
1017. **`drivers/bus/acpi/acpica/utilities/utids.c`** -> AI Confidence: **99.32%**
1018. **`drivers/bus/acpi/acpica/utilities/utobject.c`** -> AI Confidence: **99.32%**
1019. **`drivers/bus/acpi/acpica/utilities/utownerid.c`** -> AI Confidence: **99.32%**
1020. **`drivers/bus/acpi/acpica/utilities/utresdecode.c`** -> AI Confidence: **99.32%**
1021. **`drivers/bus/acpi/acpica/utilities/utstring.c`** -> AI Confidence: **99.32%**
1022. **`drivers/bus/acpi/busmgr/utils.c`** -> AI Confidence: **99.32%**
1023. **`drivers/bus/acpi/main.c`** -> AI Confidence: **99.32%**
1024. **`drivers/bus/acpi_new/uacpi/include/uacpi/platform/atomic.h`** -> AI Confidence: **99.32%**
1025. **`drivers/bus/acpi_new/uacpi/include/uacpi/platform/config.h`** -> AI Confidence: **99.32%**
1026. **`drivers/bus/pci/pci.c`** -> AI Confidence: **99.32%**
1027. **`drivers/crypto/ksecdd/dispatch.c`** -> AI Confidence: **99.32%**
1028. **`drivers/filesystems/fs_rec/btrfs.c`** -> AI Confidence: **99.32%**
1029. **`drivers/filesystems/fs_rec/cdfs.c`** -> AI Confidence: **99.32%**
1030. **`drivers/filesystems/fs_rec/ext.c`** -> AI Confidence: **99.32%**
1031. **`drivers/filesystems/fs_rec/ffs.c`** -> AI Confidence: **99.32%**
1032. **`drivers/filesystems/fs_rec/reiserfs.c`** -> AI Confidence: **99.32%**
1033. **`drivers/filesystems/fs_rec/udfs.c`** -> AI Confidence: **99.32%**
1034. **`drivers/filesystems/vfatfs/fcb.c`** -> AI Confidence: **99.32%**
1035. **`drivers/filesystems/vfatfs/kdbg.c`** -> AI Confidence: **99.32%**
1036. **`drivers/filters/fltmgr/Context.c`** -> AI Confidence: **99.32%**
1037. **`drivers/filters/fltmgr/Registry.c`** -> AI Confidence: **99.32%**
1038. **`drivers/input/sermouse/detect.c`** -> AI Confidence: **99.32%**
1039. **`drivers/ksfilter/ks/irp.c`** -> AI Confidence: **99.32%**
1040. **`drivers/network/dd/netkvm/Common/ParaNdis-Oid.c`** -> AI Confidence: **99.32%**
1041. **`drivers/network/dd/netkvm/wxp/ParaNdis5-Oid.c`** -> AI Confidence: **99.32%**
1042. **`drivers/network/tcpip/lwip/src/include/lwip/ip6_addr.h`** -> AI Confidence: **99.32%**
1043. **`drivers/network/tcpip/tcpip/dispatch.c`** -> AI Confidence: **99.32%**
1044. **`drivers/storage/class/classpnp/autorun.c`** -> AI Confidence: **99.32%**
1045. **`drivers/storage/class/classpnp/create.c`** -> AI Confidence: **99.32%**
1046. **`drivers/storage/class/classpnp/debug.c`** -> AI Confidence: **99.32%**
1047. **`drivers/storage/class/classpnp/lock.c`** -> AI Confidence: **99.32%**
1048. **`drivers/storage/class/classpnp/retry.c`** -> AI Confidence: **99.32%**
1049. **`drivers/storage/class/classpnp/xferpkt.c`** -> AI Confidence: **99.32%**
1050. **`drivers/storage/floppy/fdc/fdo.c`** -> AI Confidence: **99.32%**
1051. **`drivers/storage/port/scsiport/ioctl.c`** -> AI Confidence: **99.32%**
1052. **`drivers/storage/port/scsiport/registry.c`** -> AI Confidence: **99.32%**
1053. **`drivers/usb/usbehci/usbehci.c`** -> AI Confidence: **99.32%**
1054. **`drivers/usb/usbhub/ioctl.c`** -> AI Confidence: **99.32%**
1055. **`drivers/usb/usbhub/pnp.c`** -> AI Confidence: **99.32%**
1056. **`drivers/usb/usbhub/power.c`** -> AI Confidence: **99.32%**
1057. **`drivers/usb/usbohci/usbohci.c`** -> AI Confidence: **99.32%**
1058. **`drivers/usb/usbport/endpoint.c`** -> AI Confidence: **99.32%**
1059. **`drivers/usb/usbport/pnp.c`** -> AI Confidence: **99.32%**
1060. **`drivers/usb/usbport/queue.c`** -> AI Confidence: **99.32%**
1061. **`drivers/usb/usbport/roothub.c`** -> AI Confidence: **99.32%**
1062. **`drivers/usb/usbport/urb.c`** -> AI Confidence: **99.32%**
1063. **`drivers/usb/usbport/usbport.c`** -> AI Confidence: **99.32%**
1064. **`drivers/usb/usbuhci/usbuhci.c`** -> AI Confidence: **99.32%**
1065. **`hal/halarm/generic/halinit.c`** -> AI Confidence: **99.32%**
1066. **`hal/halx86/apic/apictimer.c`** -> AI Confidence: **99.32%**
1067. **`hal/halx86/generic/dma.c`** -> AI Confidence: **99.32%**
1068. **`hal/halx86/generic/nmi.c`** -> AI Confidence: **99.32%**
1069. **`hal/halx86/smp/mps/mps.c`** -> AI Confidence: **99.32%**
1070. **`modules/rosapps/applications/cmdutils/y/y.c`** -> AI Confidence: **99.32%**
1071. **`modules/rosapps/applications/devutils/bootvid_font_generator/bootvid_font_generator.c`** -> AI Confidence: **99.32%**
1072. **`modules/rosapps/applications/net/ncftp/Strn/Strntok.c`** -> AI Confidence: **99.32%**
1073. **`modules/rosapps/applications/net/ncftp/Strn/strtokc.c`** -> AI Confidence: **99.32%**
1074. **`modules/rosapps/applications/net/tsclient/rdesktop/mppc.c`** -> AI Confidence: **99.32%**
1075. **`modules/rosapps/applications/notevil/notevil.c`** -> AI Confidence: **99.32%**
1076. **`modules/rosapps/applications/sysutils/utils/sdkparse/assert.h`** -> AI Confidence: **99.32%**
1077. **`modules/rosapps/drivers/vfd/vfddev.c`** -> AI Confidence: **99.32%**
1078. **`modules/rosapps/drivers/vfd/vfddrv.c`** -> AI Confidence: **99.32%**
1079. **`modules/rosapps/drivers/vfd/vfdlink.c`** -> AI Confidence: **99.32%**
1080. **`modules/rosapps/drivers/vfd/vfdpnp.c`** -> AI Confidence: **99.32%**
1081. **`modules/rosapps/drivers/vfd/vfdrdwr.c`** -> AI Confidence: **99.32%**
1082. **`modules/rostests/apitests/compiler/ms_seh.c`** -> AI Confidence: **99.32%**
1083. **`modules/rostests/apitests/iphlpapi/GetExtendedTcpTable.c`** -> AI Confidence: **99.32%**
1084. **`modules/rostests/apitests/iphlpapi/GetExtendedUdpTable.c`** -> AI Confidence: **99.32%**
1085. **`modules/rostests/apitests/iphlpapi/GetNetworkParams.c`** -> AI Confidence: **99.32%**
1086. **`modules/rostests/apitests/iphlpapi/GetOwnerModuleFromTcpEntry.c`** -> AI Confidence: **99.32%**
1087. **`modules/rostests/apitests/iphlpapi/GetOwnerModuleFromUdpEntry.c`** -> AI Confidence: **99.32%**
1088. **`modules/rostests/apitests/kernel32/DeviceIoControl.c`** -> AI Confidence: **99.32%**
1089. **`modules/rostests/apitests/shlwapi/PathUnExpandEnvStrings.c`** -> AI Confidence: **99.32%**
1090. **`modules/rostests/kmtests/example/Example_drv.c`** -> AI Confidence: **99.32%**
1091. **`modules/rostests/kmtests/ntos_io/IoCreateFile_drv.c`** -> AI Confidence: **99.32%**
1092. **`modules/rostests/kmtests/ntos_io/IoDeviceInterface.c`** -> AI Confidence: **99.32%**
1093. **`modules/rostests/kmtests/ntos_ke/KeSpinLock.c`** -> AI Confidence: **99.32%**
1094. **`modules/rostests/kmtests/ntos_mm/MmMapLockedPagesSpecifyCache_drv.c`** -> AI Confidence: **99.32%**
1095. **`modules/rostests/kmtests/ntos_mm/MmMapLockedPagesSpecifyCache_user.c`** -> AI Confidence: **99.32%**
1096. **`modules/rostests/kmtests/ntos_se/SeQueryInfoToken.c`** -> AI Confidence: **99.32%**
1097. **`modules/rostests/tests/accelerator/accelerator.c`** -> AI Confidence: **99.32%**
1098. **`modules/rostests/tests/carets/carets.c`** -> AI Confidence: **99.32%**
1099. **`modules/rostests/tests/global_mem/global_mem.c`** -> AI Confidence: **99.32%**
1100. **`modules/rostests/tests/guithreadinfo/guithreadinfo.c`** -> AI Confidence: **99.32%**
1101. **`modules/rostests/tests/winhello/winhello.c`** -> AI Confidence: **99.32%**
1102. **`modules/rostests/unittests/isapnp/tests.c`** -> AI Confidence: **99.32%**
1103. **`modules/rostests/win32/cmd/batch.c`** -> AI Confidence: **99.32%**
1104. **`modules/rostests/winetests/cmd/batch.c`** -> AI Confidence: **99.32%**
1105. **`modules/rostests/winetests/d3dx9_36/texture.c`** -> AI Confidence: **99.32%**
1106. **`modules/rostests/winetests/dsound/dsound8.c`** -> AI Confidence: **99.32%**
1107. **`ntoskrnl/cc/view.c`** -> AI Confidence: **99.32%**
1108. **`ntoskrnl/ex/handle.c`** -> AI Confidence: **99.32%**
1109. **`ntoskrnl/fsrtl/pnp.c`** -> AI Confidence: **99.32%**
1110. **`ntoskrnl/kd/kdprompt.c`** -> AI Confidence: **99.32%**
1111. **`ntoskrnl/kd/kdterminal.c`** -> AI Confidence: **99.32%**
1112. **`ntoskrnl/kd64/kdapi.c`** -> AI Confidence: **99.32%**
1113. **`ntoskrnl/kd64/kddata.c`** -> AI Confidence: **99.32%**
1114. **`ntoskrnl/ke/bug.c`** -> AI Confidence: **99.32%**
1115. **`ntoskrnl/ke/i386/kiinit.c`** -> AI Confidence: **99.32%**
1116. **`ntoskrnl/ke/krnlinit.c`** -> AI Confidence: **99.32%**
1117. **`ntoskrnl/mm/ARM3/i386/init.c`** -> AI Confidence: **99.32%**
1118. **`ntoskrnl/mm/ARM3/iosup.c`** -> AI Confidence: **99.32%**
1119. **`ntoskrnl/mm/ARM3/largepag.c`** -> AI Confidence: **99.32%**
1120. **`ntoskrnl/mm/ARM3/mdlsup.c`** -> AI Confidence: **99.32%**
1121. **`ntoskrnl/mm/ARM3/mmdbg.c`** -> AI Confidence: **99.32%**
1122. **`ntoskrnl/mm/ARM3/mminit.c`** -> AI Confidence: **99.32%**
1123. **`ntoskrnl/mm/ARM3/pfnlist.c`** -> AI Confidence: **99.32%**
1124. **`ntoskrnl/mm/ARM3/sysldr.c`** -> AI Confidence: **99.32%**
1125. **`ntoskrnl/mm/ARM3/syspte.c`** -> AI Confidence: **99.32%**
1126. **`ntoskrnl/mm/ARM3/virtual.c`** -> AI Confidence: **99.32%**
1127. **`ntoskrnl/mm/ARM3/zeropage.c`** -> AI Confidence: **99.32%**
1128. **`ntoskrnl/mm/balance.c`** -> AI Confidence: **99.32%**
1129. **`ntoskrnl/mm/freelist.c`** -> AI Confidence: **99.32%**
1130. **`ntoskrnl/mm/rmap.c`** -> AI Confidence: **99.32%**
1131. **`ntoskrnl/mm/shutdown.c`** -> AI Confidence: **99.32%**
1132. **`ntoskrnl/se/tokencls.c`** -> AI Confidence: **99.32%**
1133. **`ntoskrnl/tests/TestDebug.c`** -> AI Confidence: **99.32%**
1134. **`sdk/include/c++/stlport/exception.h`** -> AI Confidence: **99.32%**
1135. **`sdk/include/c++/stlport/new.h`** -> AI Confidence: **99.32%**
1136. **`sdk/include/c++/stlport/stddef.h`** -> AI Confidence: **99.32%**
1137. **`sdk/include/c++/stlport/stl/_slist.c`** -> AI Confidence: **99.32%**
1138. **`sdk/include/c++/stlport/stl/config/_dm.h`** -> AI Confidence: **99.32%**
1139. **`sdk/include/c++/stlport/stl/config/_msvc.h`** -> AI Confidence: **99.32%**
1140. **`sdk/include/c++/stlport/stl/config/_mwerks.h`** -> AI Confidence: **99.32%**
1141. **`sdk/include/c++/stlport/wchar.h`** -> AI Confidence: **99.32%**
1142. **`sdk/include/reactos/libs/mbedtls/cmac.h`** -> AI Confidence: **99.32%**
1143. **`sdk/include/reactos/libs/mbedtls/padlock.h`** -> AI Confidence: **99.32%**
1144. **`sdk/lib/3rdparty/adns/src/config.h`** -> AI Confidence: **99.32%**
1145. **`sdk/lib/3rdparty/adns/src/config.h.in`** -> AI Confidence: **99.32%**
1146. **`sdk/lib/3rdparty/adns/src/reply.c`** -> AI Confidence: **99.32%**
1147. **`sdk/lib/3rdparty/freetype/src/base/ftcid.c`** -> AI Confidence: **99.32%**
1148. **`sdk/lib/3rdparty/freetype/src/gzip/inftrees.c`** -> AI Confidence: **99.32%**
1149. **`sdk/tools/fatten/fatfs/ff.c`** -> AI Confidence: **99.32%**
1150. **`sdk/tools/mkisofs/schilytools/include/schily/btorder.h`** -> AI Confidence: **99.32%**
1151. **`sdk/tools/mkisofs/schilytools/include/schily/dirent.h`** -> AI Confidence: **99.32%**
1152. **`sdk/tools/mkisofs/schilytools/include/schily/io.h`** -> AI Confidence: **99.32%**
1153. **`sdk/tools/mkisofs/schilytools/include/schily/maxpath.h`** -> AI Confidence: **99.32%**
1154. **`subsystems/csr/csrsrv/api.c`** -> AI Confidence: **99.32%**
1155. **`subsystems/win/basesrv/vdm.c`** -> AI Confidence: **99.32%**
1156. **`win32ss/drivers/videoprt/child.c`** -> AI Confidence: **99.32%**
1157. **`win32ss/user/ntuser/ime.c`** -> AI Confidence: **99.32%**
1158. **`win32ss/user/ntuser/window.c`** -> AI Confidence: **99.32%**
1159. **`win32ss/user/rtl/image.c`** -> AI Confidence: **99.32%**
1160. **`win32ss/user/user32/controls/edit.c`** -> AI Confidence: **99.32%**
1161. **`win32ss/user/user32/misc/exticon.c`** -> AI Confidence: **99.32%**
1162. **`win32ss/user/user32/windows/messagebox.c`** -> AI Confidence: **99.32%**
1163. **`win32ss/user/winsrv/concfg/settings.c`** -> AI Confidence: **99.32%**
1164. **`win32ss/user/winsrv/consrv/frontends/gui/fullscreen.c`** -> AI Confidence: **99.32%**
1165. **`win32ss/user/winsrv/consrv/frontends/gui/text.c`** -> AI Confidence: **99.32%**
1166. **`win32ss/user/winsrv/consrv/handle.c`** -> AI Confidence: **99.32%**
1167. **`base/ctf/cicero/cicbase.cpp`** -> AI Confidence: **99.31%**
1168. **`base/ctf/msctf/mlng.cpp`** -> AI Confidence: **99.31%**
1169. **`base/ctf/msctf/utils.cpp`** -> AI Confidence: **99.31%**
1170. **`base/shell/cmd/precomp.h`** -> AI Confidence: **99.31%**
1171. **`dll/opengl/glu32/src/libnurbs/internals/curvesub.cc`** -> AI Confidence: **99.31%**
1172. **`dll/shellext/shellbtrfs/factory.cpp`** -> AI Confidence: **99.31%**
1173. **`dll/shellext/shellbtrfs/iconoverlay.cpp`** -> AI Confidence: **99.31%**
1174. **`dll/shellext/shellbtrfs/main.cpp`** -> AI Confidence: **99.31%**
1175. **`dll/win32/shell32/shellmenu/CMenuBand.cpp`** -> AI Confidence: **99.31%**
1176. **`dll/win32/shell32/shellmenu/CMenuToolbars.cpp`** -> AI Confidence: **99.31%**
1177. **`dll/win32/shlwapi/propbag.cpp`** -> AI Confidence: **99.31%**
1178. **`dll/win32/shlwapi/utils.cpp`** -> AI Confidence: **99.31%**
1179. **`dll/win32/uxtheme/pngsup.cpp`** -> AI Confidence: **99.31%**
1180. **`modules/rosapps/applications/fraginator/Fraginator.cpp`** -> AI Confidence: **99.31%**
1181. **`modules/rosapps/applications/net/netreg/netreg.cpp`** -> AI Confidence: **99.31%**
1182. **`modules/rostests/apitests/browseui/IACLCustomMRU.cpp`** -> AI Confidence: **99.31%**
1183. **`modules/rostests/apitests/browseui/IAutoComplete.cpp`** -> AI Confidence: **99.31%**
1184. **`modules/rostests/apitests/fontext/GetDisplayNameOf.cpp`** -> AI Confidence: **99.31%**
1185. **`modules/rostests/apitests/fontext/shellext.cpp`** -> AI Confidence: **99.31%**
1186. **`modules/rostests/apitests/shell32/ShellExecuteEx.cpp`** -> AI Confidence: **99.31%**
1187. **`modules/rostests/apitests/shlwapi/IsQSForward.cpp`** -> AI Confidence: **99.31%**
1188. **`sdk/lib/3rdparty/stlport/src/allocators.cpp`** -> AI Confidence: **99.31%**
1189. **`sdk/lib/3rdparty/stlport/src/details/fstream_stdio.cpp`** -> AI Confidence: **99.31%**
1190. **`sdk/lib/3rdparty/stlport/src/facets_byname.cpp`** -> AI Confidence: **99.31%**
1191. **`sdk/lib/3rdparty/stlport/src/locale_impl.cpp`** -> AI Confidence: **99.31%**
1192. **`sdk/lib/3rdparty/stlport/src/num_put_float.cpp`** -> AI Confidence: **99.31%**
1193. **`sdk/lib/drivers/wdf/kmdf/src/dynamic/version/version.cpp`** -> AI Confidence: **99.31%**
1194. **`sdk/tools/cabman/CCFDATAStorage.cxx`** -> AI Confidence: **99.31%**
1195. **`sdk/tools/cabman/cabinet.cxx`** -> AI Confidence: **99.31%**
1196. **`sdk/tools/gcc_plugin_seh/main.cpp`** -> AI Confidence: **99.31%**
1197. **`sdk/tools/hhpcomp/hhpcomp.cpp`** -> AI Confidence: **99.31%**
1198. **`sdk/tools/hhpcomp/utils.cpp`** -> AI Confidence: **99.31%**
1199. **`base/applications/cmdutils/chcp/chcp.c`** -> AI Confidence: **99.31%**
1200. **`base/applications/cmdutils/help/help.c`** -> AI Confidence: **99.31%**
1201. **`base/applications/cmdutils/where/where.c`** -> AI Confidence: **99.31%**
1202. **`base/applications/cmdutils/wscript/main.c`** -> AI Confidence: **99.31%**
1203. **`base/applications/kbswitch/kbswitch.c`** -> AI Confidence: **99.31%**
1204. **`base/applications/network/wlanconf/wlanconf.c`** -> AI Confidence: **99.31%**
1205. **`base/applications/regedit/regproc.c`** -> AI Confidence: **99.31%**
1206. **`base/services/nfsd/daemon_debug.c`** -> AI Confidence: **99.31%**
1207. **`base/services/nfsd/delegation.c`** -> AI Confidence: **99.31%**
1208. **`base/services/nfsd/idmap.c`** -> AI Confidence: **99.31%**
1209. **`base/services/nfsd/lock.c`** -> AI Confidence: **99.31%**
1210. **`base/services/nfsd/name_cache.c`** -> AI Confidence: **99.31%**
1211. **`base/services/nfsd/nfs41_server.c`** -> AI Confidence: **99.31%**
1212. **`base/services/nfsd/nfs41_superblock.c`** -> AI Confidence: **99.31%**
1213. **`base/services/nfsd/nfs41_xdr.c`** -> AI Confidence: **99.31%**
1214. **`base/services/nfsd/util.c`** -> AI Confidence: **99.31%**
1215. **`base/services/rpcss/rpcss_main.c`** -> AI Confidence: **99.31%**
1216. **`base/setup/reactos/spapisup/fileqsup.c`** -> AI Confidence: **99.31%**
1217. **`base/shell/filebrowser/filebrowser.c`** -> AI Confidence: **99.31%**
1218. **`boot/freeldr/freeldr/disk/scsiport.c`** -> AI Confidence: **99.31%**
1219. **`boot/freeldr/install/install.c`** -> AI Confidence: **99.31%**
1220. **`boot/freeldr/install/linux/finstext2.c`** -> AI Confidence: **99.31%**
1221. **`dll/3rdparty/libjpeg/jmemmac.c`** -> AI Confidence: **99.31%**
1222. **`dll/3rdparty/libtiff/mkg3states.c`** -> AI Confidence: **99.31%**
1223. **`dll/3rdparty/libtirpc/src/auth_des.c`** -> AI Confidence: **99.31%**
1224. **`dll/3rdparty/libtirpc/src/auth_gss.c`** -> AI Confidence: **99.31%**
1225. **`dll/3rdparty/libtirpc/src/auth_sspi.c`** -> AI Confidence: **99.31%**
1226. **`dll/3rdparty/libtirpc/src/auth_time.c`** -> AI Confidence: **99.31%**
1227. **`dll/3rdparty/libtirpc/src/authgss_prot.c`** -> AI Confidence: **99.31%**
1228. **`dll/3rdparty/libtirpc/src/clnt_bcast.c`** -> AI Confidence: **99.31%**
1229. **`dll/3rdparty/libtirpc/src/clnt_dg.c`** -> AI Confidence: **99.31%**
1230. **`dll/3rdparty/libtirpc/src/clnt_generic.c`** -> AI Confidence: **99.31%**
1231. **`dll/3rdparty/libtirpc/src/clnt_simple.c`** -> AI Confidence: **99.31%**
1232. **`dll/3rdparty/libtirpc/src/clnt_vc.c`** -> AI Confidence: **99.31%**
1233. **`dll/3rdparty/libtirpc/src/crypt_client.c`** -> AI Confidence: **99.31%**
1234. **`dll/3rdparty/libtirpc/src/getnetconfig.c`** -> AI Confidence: **99.31%**
1235. **`dll/3rdparty/libtirpc/src/getrpcent.c`** -> AI Confidence: **99.31%**
1236. **`dll/3rdparty/libtirpc/src/key_call.c`** -> AI Confidence: **99.31%**
1237. **`dll/3rdparty/libtirpc/src/netnamer.c`** -> AI Confidence: **99.31%**
1238. **`dll/3rdparty/libtirpc/src/pmap_clnt.c`** -> AI Confidence: **99.31%**
1239. **`dll/3rdparty/libtirpc/src/rpcb_clnt.c`** -> AI Confidence: **99.31%**
1240. **`dll/3rdparty/libtirpc/src/svc.c`** -> AI Confidence: **99.31%**
1241. **`dll/3rdparty/libtirpc/src/svc_auth_des.c`** -> AI Confidence: **99.31%**
1242. **`dll/3rdparty/libtirpc/src/svc_generic.c`** -> AI Confidence: **99.31%**
1243. **`dll/3rdparty/libtirpc/src/svc_run.c`** -> AI Confidence: **99.31%**
1244. **`dll/3rdparty/libtirpc/src/svc_simple.c`** -> AI Confidence: **99.31%**
1245. **`dll/3rdparty/libtirpc/src/xdr.c`** -> AI Confidence: **99.31%**
1246. **`dll/3rdparty/libtirpc/src/xdr_float.c`** -> AI Confidence: **99.31%**
1247. **`dll/3rdparty/libtirpc/src/xdr_rec.c`** -> AI Confidence: **99.31%**
1248. **`dll/3rdparty/libtirpc/src/xdr_reference.c`** -> AI Confidence: **99.31%**
1249. **`dll/3rdparty/libxslt/attributes.c`** -> AI Confidence: **99.31%**
1250. **`dll/3rdparty/libxslt/documents.c`** -> AI Confidence: **99.31%**
1251. **`dll/3rdparty/libxslt/pattern.c`** -> AI Confidence: **99.31%**
1252. **`dll/3rdparty/libxslt/security.c`** -> AI Confidence: **99.31%**
1253. **`dll/3rdparty/libxslt/templates.c`** -> AI Confidence: **99.31%**
1254. **`dll/3rdparty/mbedtls/asn1parse.c`** -> AI Confidence: **99.31%**
1255. **`dll/3rdparty/mbedtls/cipher.c`** -> AI Confidence: **99.31%**
1256. **`dll/3rdparty/mbedtls/cipher_wrap.c`** -> AI Confidence: **99.31%**
1257. **`dll/3rdparty/mbedtls/dhm.c`** -> AI Confidence: **99.31%**
1258. **`dll/3rdparty/mbedtls/ecdsa.c`** -> AI Confidence: **99.31%**
1259. **`dll/3rdparty/mbedtls/entropy_poll.c`** -> AI Confidence: **99.31%**
1260. **`dll/3rdparty/mbedtls/md.c`** -> AI Confidence: **99.31%**
1261. **`dll/3rdparty/mbedtls/memory_buffer_alloc.c`** -> AI Confidence: **99.31%**
1262. **`dll/3rdparty/mbedtls/net_sockets.c`** -> AI Confidence: **99.31%**
1263. **`dll/3rdparty/mbedtls/oid.c`** -> AI Confidence: **99.31%**
1264. **`dll/3rdparty/mbedtls/pk.c`** -> AI Confidence: **99.31%**
1265. **`dll/3rdparty/mbedtls/pkcs11.c`** -> AI Confidence: **99.31%**
1266. **`dll/3rdparty/mbedtls/pkcs12.c`** -> AI Confidence: **99.31%**
1267. **`dll/3rdparty/mbedtls/pkparse.c`** -> AI Confidence: **99.31%**
1268. **`dll/3rdparty/mbedtls/platform_util.c`** -> AI Confidence: **99.31%**
1269. **`dll/3rdparty/mbedtls/sha512.c`** -> AI Confidence: **99.31%**
1270. **`dll/3rdparty/mbedtls/ssl_ticket.c`** -> AI Confidence: **99.31%**
1271. **`dll/3rdparty/mbedtls/timing.c`** -> AI Confidence: **99.31%**
1272. **`dll/3rdparty/mbedtls/x509.c`** -> AI Confidence: **99.31%**
1273. **`dll/3rdparty/mbedtls/x509_crt.c`** -> AI Confidence: **99.31%**
1274. **`dll/3rdparty/mbedtls/x509_csr.c`** -> AI Confidence: **99.31%**
1275. **`dll/3rdparty/mbedtls/x509write_crt.c`** -> AI Confidence: **99.31%**
1276. **`dll/3rdparty/mbedtls/x509write_csr.c`** -> AI Confidence: **99.31%**
1277. **`dll/appcompat/shims/genral/msys2.c`** -> AI Confidence: **99.31%**
1278. **`dll/appcompat/shims/genral/themes.c`** -> AI Confidence: **99.31%**
1279. **`dll/appcompat/shims/layer/versionlie.c`** -> AI Confidence: **99.31%**
1280. **`dll/cpl/inetcpl/inetcpl.c`** -> AI Confidence: **99.31%**
1281. **`dll/cpl/mmsys/mmsys.c`** -> AI Confidence: **99.31%**
1282. **`dll/directx/d3d9/adapter.c`** -> AI Confidence: **99.31%**
1283. **`dll/directx/d3d9/d3d9_create.c`** -> AI Confidence: **99.31%**
1284. **`dll/directx/d3d9/d3d9_impl.c`** -> AI Confidence: **99.31%**
1285. **`dll/directx/wine/d3dcompiler_43/preproc.c`** -> AI Confidence: **99.31%**
1286. **`dll/directx/wine/d3dx9_36/effect.c`** -> AI Confidence: **99.31%**
1287. **`dll/directx/wine/d3dx9_36/mesh.c`** -> AI Confidence: **99.31%**
1288. **`dll/directx/wine/dinput/device.c`** -> AI Confidence: **99.31%**
1289. **`dll/directx/wine/dinput/joystick_osx.c`** -> AI Confidence: **99.31%**
1290. **`dll/directx/wine/dinput/keyboard.c`** -> AI Confidence: **99.31%**
1291. **`dll/directx/wine/dinput/mouse.c`** -> AI Confidence: **99.31%**
1292. **`dll/directx/wine/dmusic/dmusic_main.c`** -> AI Confidence: **99.31%**
1293. **`dll/directx/wine/dplayx/dplaysp.c`** -> AI Confidence: **99.31%**
1294. **`dll/directx/wine/dplayx/dplayx_global.c`** -> AI Confidence: **99.31%**
1295. **`dll/directx/wine/dplayx/dplayx_messages.c`** -> AI Confidence: **99.31%**
1296. **`dll/directx/wine/dxdiagn/provider.c`** -> AI Confidence: **99.31%**
1297. **`dll/directx/wine/msdmo/dmort.c`** -> AI Confidence: **99.31%**
1298. **`dll/directx/wine/qcap/avimux.c`** -> AI Confidence: **99.31%**
1299. **`dll/directx/wine/qcap/capturegraph.c`** -> AI Confidence: **99.31%**
1300. **`dll/directx/wine/qcap/smartteefilter.c`** -> AI Confidence: **99.31%**
1301. **`dll/directx/wine/qcap/v4l.c`** -> AI Confidence: **99.31%**
1302. **`dll/directx/wine/qcap/yuv.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `dll/3rdparty/mbedtls/pkwrite.c` -> **99.9134%** Exposure
- `dll/3rdparty/mbedtls/pkparse.c` -> **98.9612%** Exposure
- `dll/3rdparty/mbedtls/x509write_crt.c` -> **92.2689%** Exposure
- `modules/rostests/winetests/crypt32/base64.c` -> **88.4707%** Exposure
- `dll/3rdparty/mbedtls/x509_crt.c` -> **46.7919%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `556` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `45532` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `boot/freeldr/freeldr/arch/uefi/uefihw.c` (C) -> Cumulative Risk: **712.76**
- **Archetype:** `file_cluster_8` (Distance: 12.435 IQR)
- **Magnitude:** 222.62 | **LOC:** 353 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.6859%)
- **Heaviest Functions:** `UefiFindAcpiTable` (Impact: 17.4), `DetectDisplayController` (Impact: 13.9), `DetectAcpiBios` (Impact: 8.0)

### 2. `base/applications/network/netsh/netsh.c` (C) -> Cumulative Risk: **711.62**
- **Archetype:** `file_cluster_8` (Distance: 11.908 IQR)
- **Magnitude:** 387.82 | **LOC:** 510 | **CtrlFlow:** 79.0% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), State Flux (99.9995%)
- **Heaviest Functions:** `wmain` (Impact: 64.8), `MergeStrings` (Impact: 9.6), `PrintError` (Impact: 7.8)

### 3. `boot/freeldr/freeldr/arch/i386/pc/pcvideo.c` (C) -> Cumulative Risk: **705.27**
- **Archetype:** `file_cluster_8` (Distance: 12.19 IQR)
- **Magnitude:** 415.3 | **LOC:** 1316 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (92.7865%)
- **Heaviest Functions:** `PcVideoSetMode` (Impact: 21.9), `PcVideoSetMode80x50_80x43` (Impact: 6.5), `PcVideoDetectVideoCard` (Impact: 5.2)

### 4. `drivers/base/kdgdb/kdcom.c` (C) -> Cumulative Risk: **701.96**
- **Archetype:** `file_cluster_13` (Distance: 12.662 IQR)
- **Magnitude:** 222.72 | **LOC:** 312 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (90.149%)
- **Heaviest Functions:** `KdDebuggerInitialize0` (Impact: 27.3), `KdpDbgPrint` (Impact: 8.5), `KdpPollBreakIn` (Impact: 6.2)

### 5. `drivers/base/kdcom/kdcom.c` (C) -> Cumulative Risk: **701.95**
- **Archetype:** `file_cluster_13` (Distance: 12.734 IQR)
- **Magnitude:** 235.24 | **LOC:** 310 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (93.691%)
- **Heaviest Functions:** `KdDebuggerInitialize0` (Impact: 26.1), `KdpDbgPrint` (Impact: 8.5), `KdpPollByte` (Impact: 7.0)

### 6. `drivers/base/bootvid/i386/xbox/bootvid.c` (C) -> Cumulative Risk: **701.35**
- **Archetype:** `file_cluster_8` (Distance: 13.374 IQR)
- **Magnitude:** 479.02 | **LOC:** 431 | **CtrlFlow:** 91.8% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.003%)
- **Heaviest Functions:** `VidInitialize` (Impact: 23.0), `ApplyPalette` (Impact: 11.7), `PreserveRow` (Impact: 8.2)

### 7. `dll/win32/uiautomationcore/uia_provider.c` (C) -> Cumulative Risk: **692.5**
- **Archetype:** `file_cluster_8` (Distance: 12.834 IQR)
- **Magnitude:** 964.48 | **LOC:** 2320 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (94.7595%)
- **Heaviest Functions:** `msaa_acc_get_child_pos` (Impact: 170.9), `base_hwnd_provider_GetPropertyValue` (Impact: 31.6), `msaa_acc_compare` (Impact: 29.1)

### 8. `boot/freeldr/freeldr/arch/uefi/uefivid.c` (C) -> Cumulative Risk: **690.75**
- **Archetype:** `file_cluster_8` (Distance: 11.913 IQR)
- **Magnitude:** 365.82 | **LOC:** 710 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 77.8%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.995%), Churn (81.0%)
- **Heaviest Functions:** `UefiInitializeBgrtLogo` (Impact: 41.3), `UefiGetLogoSourceCoordinates` (Impact: 12.7), `UefiDrawBgrtLogo` (Impact: 11.4)

### 9. `base/services/nfsd/util.c` (C) -> Cumulative Risk: **690.4**
- **Archetype:** `file_cluster_13` (Distance: 12.91 IQR)
- **Magnitude:** 490.6 | **LOC:** 449 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.6102%)
- **Heaviest Functions:** `nfs_to_windows_error` (Impact: 77.3), `create_silly_rename` (Impact: 15.4), `map_symlink_errors` (Impact: 14.4)

### 10. `dll/3rdparty/libtiff/tif_open.c` (C) -> Cumulative Risk: **690.18**
- **Archetype:** `file_cluster_8` (Distance: 13.123 IQR)
- **Magnitude:** 905.96 | **LOC:** 946 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.4539%)
- **Heaviest Functions:** `TIFFClientOpenExt` (Impact: 421.6), `_TIFFcallocExt` (Impact: 13.6), `_TIFFreallocExt` (Impact: 12.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `base/setup/reactos/treelist.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.497 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.442 IQR)
- **Top Global Matches:** file_cluster_8: 15.497, file_cluster_7: 15.704, file_cluster_13: 15.766
- **Magnitude:** 16600.48 | **LOC:** 13734 | **CtrlFlow:** 85.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.6474%), Tech Debt (7.892%)
**Top Internal Functions/Classes:**
  * `TreeListProc` (Impact: 1083.2)
  * `TreeListDraw` (Impact: 308.6)
  * `TreeListInsertItem` (Impact: 288.6)
  * `TreeListMouseClick` (Impact: 241.6)
  * `TreeListKeyDown` (Impact: 197.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3246`, `structural_boundaries: 570`, `args: 8`, `func_start: 66`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 10609`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1320`, `import: 7`
* *Defense:* `safety: 1`, `doc: 150`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` malloc.h, treelist.h, tchar.h, string.h, reactos.h, stdio.h, windows.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/directx/wine/wined3d/glsl_shader.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.368 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.073 IQR)
- **Top Global Matches:** file_cluster_8: 14.368, file_cluster_7: 14.638, file_cluster_13: 14.68
- **Magnitude:** 11314.22 | **LOC:** 11981 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.3631%), Tech Debt (78.3766%)
**Top Internal Functions/Classes:**
  * `shader_generate_glsl_declarations` (Impact: 1140.7)
  * `shader_glsl_get_register_name` (Impact: 1033.8)
  * `print_glsl_info_log` (Impact: 602.8)
  * `shader_glsl_generate_ffp_fragment_shader` (Impact: 351.9)
  * `set_glsl_shader_program` (Impact: 260.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1634`, `structural_boundaries: 1016`, `args: 161`, `func_start: 160`, `class_start: 293`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 3236`, `planned_debt: 1`, `fragile_debt: 52`, `orphaned_logic: 69`
* *Architecture:* `api: 1246`, `import: 6`
* *Defense:* `doc: 14`, `immutability_locks: 420`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` float.h, wined3d_private.h, limits.h, stdio.h, config.h, port.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/kernelbase/wine/locale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.645 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.687 IQR)
- **Top Global Matches:** file_cluster_8: 14.645, file_cluster_7: 14.811, file_cluster_13: 14.829
- **Magnitude:** 10153.0 | **LOC:** 8377 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.0413%), Tech Debt (12.3438%)
**Top Internal Functions/Classes:**
  * `get_locale_info` (Impact: 284.1)
  * `append_weights` (Impact: 138.2)
  * `find_substring` (Impact: 128.8)
  * `lcmap_string` (Impact: 115.5)
    * *Intent:* 0x01, 0x00, 0x01, 0x00, /* U+30a8- */ 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, /* U+30b0- */
  * `get_calendar_info` (Impact: 112.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2373`, `structural_boundaries: 937`, `args: 36`, `func_start: 235`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 4`, `state_mutation: 4671`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 23`
* *Architecture:* `api: 1876`, `import: 11`
* *Defense:* `doc: 129`, `immutability_locks: 402`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdlib.h, debug.h, winternl.h, stdarg.h, winbase.h, winuser.h, winreg.h, winnls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/kernelbase/wine/path.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.555 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.381 IQR)
- **Top Global Matches:** file_cluster_8: 14.555, file_cluster_13: 14.702, file_cluster_11: 14.766
- **Magnitude:** 9706.86 | **LOC:** 5310 | **CtrlFlow:** 75.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.085%), Tech Debt (69.7913%)
**Top Internal Functions/Classes:**
  * `PathAllocCanonicalize` (Impact: 1467.8)
  * `PathCchSkipRoot` (Impact: 1354.7)
  * `PathCanonicalizeW` (Impact: 1116.3)
  * `rewrite_url` (Impact: 382.6)
  * `UrlCombineW` (Impact: 212.3)
    * *Intent:* *out_len = lstrlenW(out);
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1438`, `structural_boundaries: 475`, `args: 58`, `func_start: 142`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 2839`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 10`, `orphaned_logic: 66`
* *Architecture:* `api: 763`, `import: 20`
* *Defense:* `safety: 17`, `doc: 4`, `immutability_locks: 179`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` debug.h, winternl.h, pathcch.h, exception.h, stdarg.h, string.h, winbase.h, stdbool.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sdk/include/vcruntime/emmintrin.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.7%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.059 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.44 IQR)
- **Top Global Matches:** file_cluster_8: 10.059, file_cluster_7: 10.735, file_cluster_1: 11.019
- **Magnitude:** 8393.13 | **LOC:** 1967 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5417%), Tech Debt (9.999%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 344`, `args: 81`, `func_start: 233`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 70`, `fragile_debt: 3`
* *Architecture:* `api: 623`, `import: 2`
* *Defense:* `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` xmmintrin.h, vcruntime.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `modules/rostests/winetests/d3dx9_36/mesh.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.821 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.424 IQR)
- **Top Global Matches:** file_cluster_8: 13.821, file_cluster_7: 14.156, file_cluster_13: 14.236
- **Magnitude:** 8338.92 | **LOC:** 11637 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.5915%), Tech Debt (8.2985%)
**Top Internal Functions/Classes:**
  * `check_vertex_components` (Impact: 191.4)
  * `compare_text_outline_mesh` (Impact: 145.5)
  * `create_outline` (Impact: 102.9)
  * `test_convert_point_reps_to_adjacency` (Impact: 73.7)
    * *Intent:* /* mesh2 (left) * * 3 0--1 * /| | / * / | |/ * 5--4 2
  * `test_convert_adjacency_to_point_reps` (Impact: 69.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 718`, `structural_boundaries: 558`, `args: 66`, `func_start: 97`, `class_start: 117`
* *Risk/State:* `safety_bypasses: 194`, `state_mutation: 4542`, `dead_code: 4`, `fragile_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 1784`, `import: 8`
* *Defense:* `safety: 6`, `immutability_locks: 941`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` d3dx9.h, test.h, limits.h, initguid.h, rmxfguid.h, rmxftmpl.h, float.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/winhttp/request.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.866 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.982 IQR)
- **Top Global Matches:** file_cluster_8: 14.866, file_cluster_11: 14.998, file_cluster_0: 15.012
- **Magnitude:** 8262.76 | **LOC:** 6172 | **CtrlFlow:** 61.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (78.027%), Tech Debt (29.9744%)
**Top Internal Functions/Classes:**
  * `query_headers` (Impact: 178.6)
  * `send_request` (Impact: 135.9)
  * `receive_response` (Impact: 133.1)
  * `do_authorization` (Impact: 123.4)
  * `open_connection` (Impact: 101.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1387`, `structural_boundaries: 864`, `args: 124`, `func_start: 193`, `class_start: 123`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 3962`, `dead_code: 1`, `fragile_debt: 31`, `orphaned_logic: 11`
* *Architecture:* `io: 433`, `api: 1010`, `import: 17`
* *Defense:* `safety: 21`, `doc: 9`, `test: 14`, `immutability_locks: 52`, `cleanup: 102`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` schannel.h, ws2tcpip.h, ntsecapi.h, debug.h, assert.h, winhttp.h, winternl.h, ole2.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dll/opengl/glu32/src/libutil/mipmap.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.123 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.948 IQR)
- **Top Global Matches:** file_cluster_8: 15.123, file_cluster_0: 15.164, file_cluster_11: 15.167
- **Magnitude:** 7885.64 | **LOC:** 8943 | **CtrlFlow:** 74.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (8.4718%)
**Top Internal Functions/Classes:**
  * `scale_internal_float` (Impact: 954.6)
  * `closestFit` (Impact: 952.3)
  * `gluBuild3DMipmapLevelsCore` (Impact: 168.0)
  * `empty_image` (Impact: 132.7)
  * `scale_internal_ushort` (Impact: 82.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 962`, `structural_boundaries: 323`, `args: 39`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 144`, `state_mutation: 4338`, `dead_code: 12`, `orphaned_logic: 4`
* *Architecture:* `api: 638`, `import: 4`
* *Defense:* `safety: 100`, `doc: 1`, `test: 98`, `immutability_locks: 336`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.h, types.h, assert.h, gluos.h, glu.h, dlfcn.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/cryptui/main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.091 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.507 IQR)
- **Top Global Matches:** file_cluster_8: 14.091, file_cluster_13: 14.347, file_cluster_7: 14.371
- **Magnitude:** 7792.44 | **LOC:** 7608 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.6799%), Tech Debt (29.2359%)
**Top Internal Functions/Classes:**
  * `add_properties` (Impact: 686.9)
  * `add_v1_fields` (Impact: 683.0)
  * `add_cert_string_to_control` (Impact: 649.1)
  * `cert_mgr_dlg_proc` (Impact: 591.4)
  * `create_advanced_filter` (Impact: 452.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 808`, `structural_boundaries: 270`, `args: 7`, `func_start: 110`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 2446`, `planned_debt: 2`, `fragile_debt: 12`, `orphaned_logic: 22`
* *Architecture:* `io: 3`, `api: 761`, `import: 19`
* *Defense:* `doc: 3`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` softpub.h, winbase.h, hlink.h, winuser.h, cryptuires.h, richole.h, debug.h, richedit.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/msvcrt/file.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.925 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.403 IQR)
- **Top Global Matches:** file_cluster_8: 14.925, file_cluster_13: 14.966, file_cluster_7: 15.028
- **Magnitude:** 7505.44 | **LOC:** 5897 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (55.9193%), Tech Debt (90.1064%)
**Top Internal Functions/Classes:**
  * `msvcrt_create_io_inherit_block` (Impact: 1075.5)
  * `_eof` (Impact: 1075.4)
  * `_fread_nolock` (Impact: 567.9)
  * `_write` (Impact: 110.7)
  * `read_utf8` (Impact: 84.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 877`, `structural_boundaries: 473`, `args: 98`, `func_start: 194`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 2475`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 12`, `orphaned_logic: 90`
* *Architecture:* `io: 20`, `api: 815`, `import: 19`
* *Defense:* `safety: 45`, `doc: 167`, `immutability_locks: 111`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` io.h, wincon.h, msvcrt.h, winbase.h, limits.h, asm.h, time.h, debug.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/msi/action.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.462 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.891 IQR)
- **Top Global Matches:** file_cluster_8: 14.462, file_cluster_13: 14.705, file_cluster_11: 14.734
- **Magnitude:** 7486.56 | **LOC:** 7854 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.2992%), Tech Debt (22.3467%)
**Top Internal Functions/Classes:**
  * `MSI_SetFeatureStates` (Impact: 88.5)
  * `ITERATE_WriteEnvironmentString` (Impact: 71.5)
  * `parse_prop` (Impact: 59.6)
  * `ITERATE_RemoveEnvironmentString` (Impact: 49.8)
  * `ACTION_ProcessComponents` (Impact: 37.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1358`, `structural_boundaries: 535`, `args: 4`, `func_start: 208`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 4100`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 32`, `orphaned_logic: 3`
* *Architecture:* `io: 27`, `api: 1321`, `import: 18`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 87`, `cleanup: 169`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` debug.h, msipriv.h, objbase.h, resource.h, stdarg.h, winbase.h, winuser.h, winreg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/filesystems/btrfs/flushthread.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.857 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.319 IQR)
- **Top Global Matches:** file_cluster_8: 14.857, file_cluster_11: 15.053, file_cluster_13: 15.097
- **Magnitude:** 7450.76 | **LOC:** 7947 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.6068%), Tech Debt (16.4478%)
**Top Internal Functions/Classes:**
  * `try_tree_amalgamate` (Impact: 457.8)
  * `flush_fcb` (Impact: 211.1)
  * `update_tree_extents` (Impact: 108.7)
  * `drop_chunk` (Impact: 101.0)
  * `rationalize_extents` (Impact: 99.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1460`, `structural_boundaries: 605`, `args: 1`, `func_start: 55`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 4235`, `dead_code: 4`, `fragile_debt: 13`, `orphaned_logic: 9`
* *Architecture:* `io: 22`, `api: 936`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ntddstor.h, xxhash.h, ata.h, ntddscsi.h, crc32c.h, btrfs_drv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/samsrv/samrpc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.826 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.966 IQR)
- **Top Global Matches:** file_cluster_8: 13.826, file_cluster_12: 14.144, file_cluster_7: 14.175
- **Magnitude:** 7388.66 | **LOC:** 9825 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.1186%), Tech Debt (14.5045%)
**Top Internal Functions/Classes:**
  * `SampQueryUserAll` (Impact: 124.0)
  * `SamrCreateUser2InDomain` (Impact: 90.6)
  * `SamrCreateUserInDomain` (Impact: 85.0)
  * `SamrSetInformationUser2` (Impact: 83.1)
  * `SamrQueryInformationUser2` (Impact: 82.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1571`, `structural_boundaries: 196`, `args: 1`, `func_start: 129`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3603`, `dead_code: 1`, `fragile_debt: 16`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 1459`, `import: 1`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` samsrv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/rostests/winetests/mshtml/activex.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.586 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.988 IQR)
- **Top Global Matches:** file_cluster_8: 11.586, file_cluster_7: 12.126, file_cluster_13: 12.311
- **Magnitude:** 7276.13 | **LOC:** 2813 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.3142%), Tech Debt (9.0855%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 296`, `args: 18`, `func_start: 193`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 590`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 331`, `import: 2`
* *Defense:* `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test_tlb.h, precomp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/urlmon/uri.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.632 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.282 IQR)
- **Top Global Matches:** file_cluster_8: 14.632, file_cluster_7: 14.876, file_cluster_13: 14.877
- **Magnitude:** 7240.02 | **LOC:** 7329 | **CtrlFlow:** 77.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.1856%), Tech Debt (68.8018%)
**Top Internal Functions/Classes:**
  * `canonicalize_ipv4address` (Impact: 570.4)
  * `canonicalize_implicit_ipv4address` (Impact: 566.1)
  * `canonicalize_path_hierarchical` (Impact: 532.6)
    * *Intent:* /* Parses the userinfo part of the URI (if it exists). The userinfo field of * a URI can consist of ...
  * `canonicalize_hierpart` (Impact: 493.6)
    * *Intent:* /* For res URIs, everything before the first '/' is
  * `canonicalize_scheme` (Impact: 462.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1046`, `structural_boundaries: 296`, `func_start: 121`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 2618`, `planned_debt: 1`, `fragile_debt: 16`, `orphaned_logic: 37`
* *Architecture:* `api: 571`, `import: 6`
* *Defense:* `doc: 9`, `immutability_locks: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` debug.h, limits.h, urlmon_main.h, strsafe.h, shlwapi.h, wchar.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/storage/ide/uniata/id_ata.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.687 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.441 IQR)
- **Top Global Matches:** file_cluster_8: 14.687, file_cluster_11: 14.983, file_cluster_13: 15.043
- **Magnitude:** 7229.18 | **LOC:** 11726 | **CtrlFlow:** 88.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (94.57%), Tech Debt (21.6877%)
**Top Internal Functions/Classes:**
  * `IdeSendCommand` (Impact: 792.1)
  * `AtapiStartIo__` (Impact: 621.0)
  * `AtapiHwInitialize__` (Impact: 597.8)
  * `AtapiCallBack__` (Impact: 323.7)
  * `DriverEntry` (Impact: 170.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1271`, `structural_boundaries: 161`, `args: 316`, `func_start: 51`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 3595`, `dead_code: 24`, `planned_debt: 6`, `fragile_debt: 11`, `orphaned_logic: 17`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `safety: 4`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdafx.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/comctl32/listview.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.887 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.424 IQR)
- **Top Global Matches:** file_cluster_8: 14.887, file_cluster_11: 14.944, file_cluster_0: 14.984
- **Magnitude:** 6963.52 | **LOC:** 12174 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.8037%), Tech Debt (24.5566%)
**Top Internal Functions/Classes:**
  * `LISTVIEW_MouseMove` (Impact: 589.5)
  * `notify_dispinfoT` (Impact: 510.5)
  * `LISTVIEW_LButtonUp` (Impact: 351.7)
    * *Intent:* /**
  * `LISTVIEW_StyleChanged` (Impact: 306.8)
    * *Intent:* /*** * DESCRIPTION:
  * `LISTVIEW_DrawItemPart` (Impact: 284.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1097`, `structural_boundaries: 395`, `args: 4`, `func_start: 94`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 2720`, `dead_code: 12`, `planned_debt: 2`, `fragile_debt: 10`, `orphaned_logic: 14`
* *Architecture:* `api: 806`
* *Defense:* `safety: 29`, `doc: 69`, `test: 11`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` stdlib.h, comctl32.h, debug.h, assert.h, wingdi.h, stdarg.h, string.h, winbase.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/directx/wine/wined3d/arb_program_shader.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.975 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.046 IQR)
- **Top Global Matches:** file_cluster_8: 13.975, file_cluster_7: 14.27, file_cluster_13: 14.304
- **Magnitude:** 6720.1 | **LOC:** 7944 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.425%), Tech Debt (26.3837%)
**Top Internal Functions/Classes:**
  * `shader_hw_scalar_op` (Impact: 831.9)
  * `shader_hw_sgn` (Impact: 331.6)
  * `shader_arb_get_register_name` (Impact: 280.3)
    * *Intent:* /* If further constants are dirty, reload them without clamping. * * The alternative is not to touch...
  * `shader_arb_select` (Impact: 232.0)
  * `gen_arbfp_ffp_shader` (Impact: 224.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1002`, `structural_boundaries: 600`, `args: 97`, `func_start: 98`, `class_start: 138`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 2181`, `planned_debt: 8`, `fragile_debt: 18`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `api: 675`, `import: 4`
* *Defense:* `doc: 5`, `immutability_locks: 253`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` wined3d_private.h, stdio.h, config.h, port.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/opengl/mesa/get.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.129 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.871 IQR)
- **Top Global Matches:** file_cluster_8: 15.129, file_cluster_13: 15.416, file_cluster_11: 15.427
- **Magnitude:** 6511.88 | **LOC:** 3199 | **CtrlFlow:** 99.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.576%), Tech Debt (12.5775%)
**Top Internal Functions/Classes:**
  * `gl_GetBooleanv` (Impact: 519.0)
    * *Intent:* /* * $Log: get.c,v $ * Revision 1.19 1998/02/04 05:00:28 brianp * more casts for Amiga StormC * * Re...
  * `gl_GetFloatv` (Impact: 519.0)
    * *Intent:* *params = (GLdouble) ctx->Pixel.ZoomX;
  * `gl_GetDoublev` (Impact: 517.0)
  * `gl_GetIntegerv` (Impact: 517.0)
    * *Intent:* *params = (GLfloat) ctx->Pixel.ZoomY;
  * `gl_GetPointerv` (Impact: 18.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1937`, `structural_boundaries: 10`, `func_start: 5`
* *Risk/State:* `state_mutation: 3394`, `planned_debt: 12`, `orphaned_logic: 5`
* *Architecture:* `api: 966`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` dlist.h, all.h, context.h, string.h, get.h, types.h, macros.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/filesystems/nfs/nfs41_driver.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.491 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.664 IQR)
- **Top Global Matches:** file_cluster_8: 14.491, file_cluster_11: 14.729, file_cluster_12: 14.758
- **Magnitude:** 6485.06 | **LOC:** 7245 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.5637%), Tech Debt (11.4039%)
**Top Internal Functions/Classes:**
  * `nfs41_UpcallWaitForReply` (Impact: 686.4)
  * `nfs41_DevFcbXXXControlFile` (Impact: 424.3)
    * *Intent:* /* validate buffer length */
  * `nfs41_CreateVNetRoot` (Impact: 81.0)
  * `nfs41_downcall` (Impact: 59.8)
    * *Intent:* #endif #if 1 /* 08/27/2010: it looks like we really don't need to call * MmUnmapLockedPages() eventh...
  * `handle_upcall` (Impact: 46.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 990`, `structural_boundaries: 249`, `args: 1`, `func_start: 115`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2769`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 10`
* *Architecture:* `io: 34`, `api: 1307`, `import: 8`
* *Defense:* `safety: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` nfs41_np.h, nfs41_driver.h, nfs41_debug.h, winerror.h, pseh2.h, windef.h, rx.h, ntstrsafe.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/rpcrt4/ndr_marshall.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.478 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.742 IQR)
- **Top Global Matches:** file_cluster_8: 14.478, file_cluster_13: 14.622, file_cluster_7: 14.633
- **Magnitude:** 6374.22 | **LOC:** 7307 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (77.3891%), Tech Debt (68.5703%)
**Top Internal Functions/Classes:**
  * `NdrPointerBufferSize` (Impact: 323.0)
  * `array_read_variance_and_unmarshall` (Impact: 126.6)
  * `ComplexUnmarshall` (Impact: 76.0)
  * `ComputeConformanceOrVariance` (Impact: 67.9)
  * `ComplexBufferSize` (Impact: 67.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1188`, `structural_boundaries: 286`, `args: 19`, `func_start: 115`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 3204`, `dead_code: 13`, `planned_debt: 17`, `fragile_debt: 57`, `orphaned_logic: 13`
* *Architecture:* `api: 1241`, `import: 16`
* *Defense:* `safety: 2`, `doc: 97`, `test: 1`, `immutability_locks: 212`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` rpcndr.h, debug.h, assert.h, poppack.h, stdarg.h, limits.h, string.h, winbase.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/ctf/cicero/cicuif.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.194 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.693 IQR)
- **Top Global Matches:** file_cluster_8: 15.194, file_cluster_7: 15.333, file_cluster_1: 15.549
- **Magnitude:** 6301.34 | **LOC:** 5474 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.5877%), Tech Debt (99.6627%)
**Top Internal Functions/Classes:**
  * `CUIFWindow::WindowProc` (Impact: 176.4)
  * `CUIFMenu::InitShow` (Impact: 97.0)
  * `CUIFButton2::OnPaintNoTheme` (Impact: 67.6)
  * `CUIFMenu::OnKeyDown` (Impact: 54.0)
  * `CUIFWindow::HandleMouseMsg` (Impact: 44.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 929`, `structural_boundaries: 459`, `args: 590`, `func_start: 267`
* *Risk/State:* `state_mutation: 3913`, `fragile_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 237`
* *Architecture:* `import: 2`
* *Defense:* `doc: 709`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cicuif.h, precomp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/bus/acpi_new/uacpi/source/interpreter.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.538 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.898 IQR)
- **Top Global Matches:** file_cluster_8: 14.538, file_cluster_13: 14.74, file_cluster_7: 14.833
- **Magnitude:** 6260.64 | **LOC:** 6052 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (46.5114%)
**Top Internal Functions/Classes:**
  * `resolve_name_string` (Impact: 863.1)
    * *Intent:* // Only used if the method is serialized
  * `handle_create_op_region` (Impact: 853.0)
  * `handle_create_buffer_field` (Impact: 467.4)
  * `handle_create_field` (Impact: 129.1)
  * `handle_concatenate` (Impact: 57.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 845`, `structural_boundaries: 380`, `args: 52`, `func_start: 78`, `class_start: 97`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2160`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 44`
* *Architecture:* `io: 2`, `api: 767`, `import: 19`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types.h, notify.h, dynamic_array.h, shareable.h, kernel_api.h, utilities.h, helpers.h, context.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/rostests/winetests/ntdll/string.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_11` (Drift: 18.57 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.972 IQR)
- **Top Global Matches:** file_cluster_11: 18.57, file_cluster_0: 18.59, file_cluster_17: 18.634
- **Magnitude:** 6193.42 | **LOC:** 1341 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.3226%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `one_i64tow_test` (Impact: 16.3)
  * `test_ulongtow` (Impact: 13.4)
  * `test_ulonglongtow` (Impact: 13.0)
  * `one_i64toa_test` (Impact: 10.0)
  * `test_wtoi64` (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 103`, `args: 30`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 5893`, `dead_code: 37`
* *Architecture:* `api: 102`, `import: 2`
* *Defense:* `safety: 5`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, ntdll_test.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/gdiplus/graphics.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.577 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.121 IQR)
- **Top Global Matches:** file_cluster_8: 14.577, file_cluster_13: 14.732, file_cluster_11: 14.77
- **Magnitude:** 5919.2 | **LOC:** 7523 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.8161%), Tech Debt (95.3841%)
**Top Internal Functions/Classes:**
  * `GdipDrawImagePointsRect` (Impact: 460.1)
  * `brush_can_fill_path` (Impact: 381.7)
  * `gdip_format_string` (Impact: 76.8)
  * `apply_image_attributes` (Impact: 59.9)
  * `draw_poly` (Impact: 53.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 991`, `structural_boundaries: 415`, `args: 2`, `func_start: 139`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 2790`, `planned_debt: 3`, `fragile_debt: 37`, `orphaned_logic: 82`
* *Architecture:* `io: 218`, `api: 1044`, `import: 18`
* *Defense:* `doc: 8`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` olectl.h, math.h, debug.h, wingdi.h, objbase.h, ole2.h, stdarg.h, limits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `drivers/ksfilter/ks/misc.c` (C) | Magnitude: 87.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, api: 43, pointers: 26, state_mutation: 22
- `dll/opengl/mesa/clip.c` (C) | Magnitude: 396.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 306, pointers: 160, indent_spaces: 105, branch: 43
- `dll/directx/ddraw/Ddraw/ddraw_setcooperativelevel.c` (C) | Magnitude: 91.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 93, state_mutation: 55, pointers: 30, branch: 20
- `drivers/multimedia/audio/sndblst.old/dma.c` (C) | Magnitude: 54.26 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, pointers: 42, api: 20, state_mutation: 20
- `modules/rosapps/applications/sysutils/pedump/pedump.c` (C) | Magnitude: 1193.82 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 624, indent_spaces: 465, api: 294, pointers: 159

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `dll/opengl/glu32/src/libnurbs/internals/arctess.cc` (CPP) | Magnitude: 755.98 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 570, indent_spaces: 184, pointers: 109, indent_tabs: 79
- `drivers/bus/acpi/busmgr/bus.c` (C) | Magnitude: 1022.56 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 437, state_mutation: 333, pointers: 180, branch: 172
- `dll/win32/riched20/paint.c` (C) | Magnitude: 140.44 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 105, indent_spaces: 104, pointers: 65, branch: 29
- `dll/opengl/glu32/src/libnurbs/nurbtess/monoChain.cc` (CPP) | Magnitude: 1033.26 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 742, indent_spaces: 280, pointers: 221, branch: 133
- `modules/rostests/winetests/ntdll/string.c` (C) | Magnitude: 6193.42 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 5893, indent_spaces: 906, pointers: 188, structural_boundaries: 103

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `dll/win32/rsaenh/rsa.c` (C) | Magnitude: 283.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: pointers: 98, state_mutation: 68, indent_spaces: 67, branch: 36
- `sdk/include/psdk/d3d.h` (C) | Magnitude: 60.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 993, macros: 810, reflection_metaprogramming: 614, indent_spaces: 307
- `sdk/include/psdk/specstrings.h` (C) | Magnitude: 24.18 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 143, reflection_metaprogramming: 92, branch: 19, indent_spaces: 11
- `sdk/include/psdk/mapival.h` (C) | Magnitude: 27.84 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 102, macros: 74, reflection_metaprogramming: 70, api: 11
- `boot/freeldr/freeldr/include/bytesex.h` (C) | Magnitude: 19.2 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 9, reflection_metaprogramming: 6, bitwise_ops: 6, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `base/applications/network/telnet/src/tncon.cpp` (CPP) | Magnitude: 289.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 142, indent_tabs: 138, doc: 103, branch: 58
- `drivers/filesystems/btrfs/zstd/zstd_compress_sequences.h` (C) | Magnitude: 44.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 27, immutability_locks: 24, indent_spaces: 23, safety: 12
- `modules/rostests/tests/event/event.c` (C) | Magnitude: 31.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 21, state_mutation: 11, branch: 6, debug_prints: 6
- `drivers/network/tcpip/lwip/src/include/lwip/tcpbase.h` (C) | Magnitude: 41.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, macros: 15, indent_spaces: 11, api: 5
- `dll/directx/wine/d3dxof/mszip.c` (C) | Magnitude: 967.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 596, indent_spaces: 390, branch: 95, api: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `dll/opengl/glu32/src/libnurbs/nurbtess/polyDBG.cc` (CPP) | Magnitude: 675.14 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 448, indent_spaces: 281, pointers: 214, branch: 127
- `dll/opengl/glu32/src/libnurbs/nurbtess/searchTree.cc` (CPP) | Magnitude: 235.04 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 158, indent_spaces: 122, pointers: 97, branch: 51
- `boot/freeldr/bootsect/fat.S` (ASSEMBLY) | Magnitude: 200.08 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 237, args: 203, structural_boundaries: 111, branch: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `base/applications/mspaint/help/usage.html` (HTML) | Magnitude: 16.72 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 12, structural_boundaries: 10, ui_framework: 8, args: 5
- `modules/rosapps/nukecamp/NSView.m` (OBJECTIVE-C) | Magnitude: 5.34 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: explicit_casts: 4, structural_boundaries: 2, args: 2, func_start: 2
- `modules/rostests/tests/button2/buttontst2.c` (C) | Magnitude: 107.22 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 51, ui_framework: 28, api: 23
- `base/applications/mspaint/help/tools.html` (HTML) | Magnitude: 17.46 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 36, ui_framework: 22, args: 17, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `boot/remaster.sh` (SHELL) | Magnitude: 187.08 | Delta: **0.139 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 72, branch: 66, indent_spaces: 46, debug_prints: 41
- `sdk/lib/3rdparty/stlport/src/cxa.c` (C) | Magnitude: 151.28 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 76, indent_spaces: 69, pointers: 54, structural_boundaries: 40
- `sdk/tools/rgenstat/web/index.html` (HTML) | Magnitude: 0.03 | Delta: **0.708 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 12, indent_tabs: 7, structural_boundaries: 4, io: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `dll/directx/wine/dmusic/clock.c` (C) | Magnitude: 79.7 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 42, indent_spaces: 42, state_mutation: 37, api: 23
- `ntoskrnl/KrnlFun.c` (C) | Magnitude: 10.52 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 52, planned_debt: 2, fragile_debt: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `sdk/include/reactos/libs/mbedtls/x509_crt.h` (C) | Magnitude: 140.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 210, api: 122, indent_spaces: 91, pointers: 86
- `modules/rosapps/applications/net/ncftp/ncftp/version.c` (C) | Magnitude: 36.24 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 15, api: 6, globals: 5, doc: 4
- `drivers/filesystems/udfs/namesup.h` (C) | Magnitude: 32.4 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 44, api: 17, indent_spaces: 11, macros: 2
- `base/applications/network/telnet/src/tmapldr.h` (CPP) | Magnitude: 12.26 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 44, indent_tabs: 10, state_mutation: 8, args: 5
- `sdk/include/reactos/x86x64/Amd/Cpuid.h` (C) | Magnitude: 143.5 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 407, indent_spaces: 139, api: 125, structural_boundaries: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `dll/opengl/glu32/src/libnurbs/internals/varray.cc` (CPP) | Magnitude: 181.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 113, pointers: 38, indent_spaces: 38, branch: 24
- `dll/win32/imaadp32.acm/imaadp32.c` (C) | Magnitude: 923.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 469, indent_spaces: 418, pointers: 387, branch: 217
- `dll/win32/msrle32/msrle32.c` (C) | Magnitude: 1952.7 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1208, indent_spaces: 729, pointers: 490, branch: 365
- `dll/win32/qmgr/qmgr.h` (C) | Magnitude: 88.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 66, indent_spaces: 60, pointers: 22, structural_boundaries: 21
- `base/services/rpcss/setup.c` (C) | Magnitude: 93.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 37, api: 22, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `drivers/filesystems/btrfs/zstd/zstd_compress_literals.h` (C) | Magnitude: 24.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 10, pointers: 10, api: 9, structural_boundaries: 7
- `drivers/network/tcpip/lwip/src/netif/ppp/upap.c` (C) | Magnitude: 11.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ownership: 3, branch: 2, macros: 2, import: 1
- `dll/win32/jscript/regexp.h` (C) | Magnitude: 39.4 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 26, indent_spaces: 22, pointers: 14, structural_boundaries: 13
- `sdk/lib/3rdparty/freetype/src/pcf/pcfutil.h` (C) | Magnitude: 19.34 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, args: 6, api: 4, structural_boundaries: 3
- `win32ss/user/user32/include/dde_private.h` (C) | Magnitude: 69.92 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 64, structural_boundaries: 17, indent_spaces: 17, macros: 10

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `base/applications/network/netsh/netsh.c` -> Churn: **100.0%** | Cog Load: 94.7923% | Debt: 38.5094%
- `base/applications/network/netsh/context.c` -> Churn: **89.33%** | Cog Load: 62.6844% | Debt: 14.013%
- `base/applications/network/route/route.c` -> Churn: **82.19%** | Cog Load: 75.4229% | Debt: 9.1302%
- `boot/freeldr/freeldr/arch/uefi/uefivid.c` -> Churn: **81.0%** | Cog Load: 80.8498% | Debt: 56.0016%
- `dll/win32/netcfgx/tcpipconf_notify.c` -> Churn: **81.0%** | Cog Load: 70.0672% | Debt: 11.8484%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `dll/win32/winhttp/request.c` -> **winesync** (100.0% isolated ownership) | Magnitude: 8262.76
- `dll/win32/msvcrt/file.c` -> **Timo Kreuzer** (100.0% isolated ownership) | Magnitude: 7505.44
- `drivers/storage/ide/uniata/id_ata.cpp` -> **Serge Gautherie** (100.0% isolated ownership) | Magnitude: 7229.18
- `dll/win32/comctl32/listview.c` -> **Emanuele Luca Cerea** (100.0% isolated ownership) | Magnitude: 6963.52
- `modules/rostests/winetests/msxml3/domdoc.c` -> **Timo Kreuzer** (100.0% isolated ownership) | Magnitude: 5435.18

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `sdk/include/psdk/specstrings.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 14.4692%)
- `sdk/include/psdk/strsafe.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `sdk/include/psdk/windef.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 18.5427%)
- `sdk/include/psdk/winsafer.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 90.9715%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `sdk/include/psdk/windef.h` -> **Severity: 2972.4** (Blast Radius: 29.724 * Doc Risk: 100.0%)
- `sdk/include/psdk/minwindef.h` -> **Severity: 2537.9** (Blast Radius: 25.379 * Doc Risk: 100.0%)
- `sdk/include/psdk/winnls.h` -> **Severity: 1273.0** (Blast Radius: 12.73 * Doc Risk: 100.0%)
- `sdk/include/wine/winnt.h` -> **Severity: 1158.3** (Blast Radius: 11.583 * Doc Risk: 100.0%)
- `sdk/include/psdk/stringapiset.h` -> **Severity: 1093.405** (Blast Radius: 10.937 * Doc Risk: 99.973%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
