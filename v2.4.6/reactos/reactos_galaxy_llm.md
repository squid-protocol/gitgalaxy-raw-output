# ARCHITECTURAL_BRIEF: reactos
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/OS/reactos` |
| **Timestamp** | `2026-08-03T19:22:24.369429+00:00` |
| **Scan Duration** | `89.4s` |
| **Git Branch** | `master` |
| **Git Commit** | `1ae75e00ae1e785aa8b89ef56afab36b3ad9d27c` |
| **Git Remote** | `https://github.com/reactos/reactos.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 13026 malicious artifacts.

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
| file_cluster_8 | 11290 | 76.5% |
| file_cluster_13 | 1714 | 11.6% |
| file_cluster_9 | 92 | 0.6% |
| file_cluster_12 | 41 | 0.3% |
| file_cluster_11 | 21 | 0.1% |
| file_cluster_7 | 19 | 0.1% |
| Unknown | 18 | 0.1% |
| file_cluster_0 | 14 | 0.1% |
| file_cluster_17 | 4 | 0.0% |
| file_cluster_2 | 4 | 0.0% |
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
| Error & Exception Exposure | 0.0 | 100.0 | 27.1 | 16.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.3 | 9.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 32.0 | 2.4 | 80.0 |
| API Exposure | 0.0 | 19.9 | 9.2 | 10.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 60.3 | 99.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 44.3 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 74.1 | 99.5 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 49.5 | 22.9 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 99.7 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
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

- `PathAllocCanonicalize` (@ `dll/win32/kernelbase/wine/path.c`) -> Impact: **9651.9** | LOC: 2077
- `get_struct_fc` (@ `sdk/tools/widl/typegen.c`) -> Impact: **8168.8** | LOC: 1529
- `canonicalize_implicit_ipv4address` (@ `dll/win32/urlmon/uri.c`) -> Impact: **5972.6** | LOC: 1603
- `FDI_read_entries` (@ `dll/win32/cabinet/fdi.c`) -> Impact: **5702.2** | LOC: 1346
- `AtapiDmaInit` (@ `drivers/storage/ide/uniata/id_dma.cpp`) -> Impact: **5671.8** | LOC: 1203
- `registry_callback` (@ `dll/win32/setupapi/install.c`) -> Impact: **5595.4** | LOC: 1401
- `adler32` (@ `dll/win32/dbghelp/inflate.c`) -> Impact: **5227.5** | LOC: 1251
  * *Intent:* #define DEF_WBITS MAX_WBITS #define zmemcpy memcpy #define zmemzero(dest, len) memset(dest, 0, len) #define Assert(cond,msg) #define Trace(x) #define ...
- `adler32` (@ `dll/win32/wininet/inflate.c`) -> Impact: **5227.5** | LOC: 1251
  * *Intent:* #define DEF_WBITS MAX_WBITS #define zmemcpy memcpy #define zmemzero(dest, len) memset(dest, 0, len) #define Assert(cond,msg) #define Trace(x) #define ...
- `fb_copy_to_texture_hwstretch` (@ `dll/directx/wine/wined3d/surface.c`) -> Impact: **5037.1** | LOC: 1292
  * *Intent:* /* * Some games (e.g. warhammer 40k) don't work properly with the odd pitches, preventing * the surface pitch from being used to box non-power2 textur...
- `ChangingWinPos` (@ `base/shell/explorer/traywnd.cpp`) -> Impact: **4489.9** | LOC: 1518
  * *Intent:* coordinates are somewhere within the exclusion rectangle */

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `HideEssentialServiceWarning` (@ `base/applications/msconfig_new/srvpage.cpp`) -> **O(2^N) [Recursive]**
- `Create` (@ `base/applications/rapps/loaddlg.cpp`) -> **O(2^N) [Recursive]**
- `DoMainLoop` (@ `base/ctf/ctfmon/ctfmon.cpp`) -> **O(2^N) [Recursive]**
- `DwInitializeSdFromThreadToken` (@ `base/services/svchost/security.cxx`) -> **O(2^N) [Recursive]**
- `QueryBand` (@ `base/shell/explorer/tbsite.cpp`) -> **O(2^N) [Recursive]**
- `OnLoad` (@ `base/shell/explorer/tbsite.cpp`) -> **O(2^N) [Recursive]**
- `ChangingWinPos` (@ `base/shell/explorer/traywnd.cpp`) -> **O(2^N) [Recursive]**
  * *Intent:* coordinates are somewhere within the exclusion rectangle */
- `ExecContextMenuCmd` (@ `base/shell/explorer/traywnd.cpp`) -> **O(2^N) [Recursive]**
- `CBDAPinControl_fnConstructor` (@ `dll/directx/bdaplgin/pincontrol.cpp`) -> **O(2^N) [Recursive]**
  * *Intent:* /* not supported */
- `CKsDataTypeHandler::KsIsMediaTypeInRange` (@ `dll/directx/ksproxy/datatype.cpp`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `modules/rosapps/applications/net/dhcpd/configure`) -> DB Complexity: **3022**
- `test_filbuf` (@ `modules/rostests/winetests/msvcrt/file.c`) -> DB Complexity: **1291**
- `test_SendInput_keyboard_messages` (@ `modules/rostests/winetests/user32/input.c`) -> DB Complexity: **629**
  * *Intent:* * Lesser General Public License for more details. * * You should have received a copy of the GNU Lesser General Public * License along with this libra...
- `processRequest` (@ `base/services/tftpd/tftpd.cpp`) -> DB Complexity: **602**
- `brush_can_fill_path` (@ `dll/win32/gdiplus/graphics.c`) -> DB Complexity: **601**
- `test_body_style` (@ `modules/rostests/winetests/mshtml/style.c`) -> DB Complexity: **601**
- `msvcrt_create_io_inherit_block` (@ `dll/win32/msvcrt/file.c`) -> DB Complexity: **575**
- `D3DXMatrixDecompose` (@ `dll/directx/wine/d3dx9_36/math.c`) -> DB Complexity: **572**
- `D3DXQuaternionTest` (@ `modules/rostests/winetests/d3dx9_36/math.c`) -> DB Complexity: **565**
- `test_Viewport` (@ `modules/rostests/winetests/d3drm/d3drm.c`) -> DB Complexity: **552**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `dll/directx/wine/wined3d` | 32 | 93225.78 | 66.58% | 54.43% |
| `sdk/include/psdk` | 486 | 84044.76 | 10.29% | 5.32% |
| `drivers/filesystems/btrfs` | 44 | 77461.98 | 61.59% | 26.99% |
| `dll/win32/msi` | 45 | 70074.76 | 66.15% | 38.62% |
| `dll/win32/kernelbase/wine` | 19 | 64713.4 | 50.53% | 59.32% |
| `dll/win32/comctl32` | 43 | 64495.34 | 63.59% | 39.67% |
| `dll/opengl/mesa` | 115 | 57866.7 | 39.71% | 23.49% |
| `win32ss/user/ntuser` | 94 | 57288.3 | 44.8% | 32.7% |
| `dll/win32/mshtml` | 83 | 56162.92 | 60.56% | 76.65% |
| `dll/3rdparty/mbedtls` | 75 | 55516.52 | 67.57% | 35.56% |

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
- `dll/opengl/mesa/api.c` -> **250** Orphaned Functions | **0** Duplicates
- `base/ctf/cicero/cicuif.cpp` -> **227** Orphaned Functions | **2** Duplicates
- `base/ctf/msutb/msutb.cpp` -> **192** Orphaned Functions | **10** Duplicates
- `modules/rosapps/applications/net/tsclient/porting-tools/mstscax/mstscax.cpp` -> **96** Orphaned Functions | **102** Duplicates
- `dll/win32/browseui/commonbrowser.cpp` -> **124** Orphaned Functions | **0** Duplicates

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

### Obfuscation & Evasion Surface
- `ntoskrnl/mm/ARM3/miarm.h` -> **99.7416%** Exposure
- `ntoskrnl/mm/ARM3/mminit.c` -> **90.5296%** Exposure
- `sdk/tools/hhpcomp/chmc/chmc.h` -> **54.5265%** Exposure
- `modules/rosapps/applications/sysutils/mkdosfs/mkdosfs.c` -> **0.6997%** Exposure
- `dll/3rdparty/libtiff/tif_dirread.c` -> **0.6916%** Exposure
### Exploit Generation Surface
- `modules/rostests/winetests/jscript/activex.c` -> **100.0%** Exposure
- `modules/rostests/winetests/jscript/caller.c` -> **100.0%** Exposure
- `modules/rostests/winetests/jscript/jscript.c` -> **100.0%** Exposure
- `modules/rostests/winetests/jscript/run.c` -> **100.0%** Exposure
- `modules/rosapps/applications/devutils/btrfstools/btrfs_structures.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `modules/rosapps/applications/sysutils/regexpl/ShellCommand.h` -> **100.0%** Exposure
- `modules/rosapps/applications/sysutils/regexpl/ShellCommandChangeKey.h` -> **100.0%** Exposure
- `modules/rosapps/applications/sysutils/regexpl/ShellCommandConnect.h` -> **100.0%** Exposure
- `modules/rosapps/applications/sysutils/regexpl/ShellCommandDACL.h` -> **100.0%** Exposure
- `modules/rosapps/applications/sysutils/regexpl/ShellCommandDOKA.h` -> **100.0%** Exposure
### Raw Memory Manipulation
- `modules/rostests/winetests/jscript/run.c` -> **100.0%** Exposure
- `dll/directx/ksproxy/interface.cpp` -> **10.0%** Exposure
- `dll/opengl/glu32/src/libnurbs/interface/bezierPatch.cc` -> **10.0%** Exposure
- `dll/opengl/glu32/src/libnurbs/interface/bezierPatchMesh.cc` -> **10.0%** Exposure
- `dll/opengl/glu32/src/libnurbs/internals/arc.cc` -> **10.0%** Exposure
### Hardcoded Payload Artifacts
- `dll/3rdparty/mbedtls/pkwrite.c` -> **99.9134%** Exposure
- `dll/3rdparty/mbedtls/pkparse.c` -> **98.9612%** Exposure
- `dll/3rdparty/mbedtls/x509write_crt.c` -> **92.2689%** Exposure
- `modules/rostests/winetests/crypt32/base64.c` -> **88.4707%** Exposure
- `dll/3rdparty/mbedtls/x509_crt.c` -> **46.7919%** Exposure
### Algorithmic DoS Exposure
- `base/applications/atactl/atactl.cpp` -> **100.0%** Exposure
- `base/applications/charmap_new/Cell.cpp` -> **100.0%** Exposure
- `base/applications/charmap_new/GridView.cpp` -> **100.0%** Exposure
- `base/applications/charmap_new/MainWindow.cpp` -> **100.0%** Exposure
- `base/applications/cleanmgr/cleanmgr/CCleanupHandler.cpp` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `556` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `45532` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `subsystems/mvdm/ntvdm/dos/dos32krnl/bios.c` (C) -> Cumulative Risk: **854.34**
- **Archetype:** `file_cluster_13` (Distance: 12.35 IQR)
- **Magnitude:** 223.36 | **LOC:** 299 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9524%)
- **Heaviest Functions:** `DosReadCharacter` (Impact: 31.7), `DosEchoCharacter` (Impact: 26.6), `DosBuildSysEnvBlock` (Impact: 16.1)

### 2. `dll/win32/jsproxy/pac.js` (JAVASCRIPT) -> Cumulative Risk: **840.56**
- **Archetype:** `file_cluster_8` (Distance: 12.099 IQR)
- **Magnitude:** 472.5 | **LOC:** 245 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `timeRange` (Impact: 149.8), `dateRange` (Impact: 90.2), `weekdayRange` (Impact: 55.7)

### 3. `dll/win32/msi/msiquery.c` (C) -> Cumulative Risk: **838.29**
- **Archetype:** `file_cluster_8` (Distance: 13.533 IQR)
- **Magnitude:** 1537.04 | **LOC:** 1274 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `msi_view_refresh_row` (Impact: 55.8), `MSI_IterateRecords` (Impact: 43.8), `set_record_type_string` (Impact: 29.7)

### 4. `dll/win32/mshtml/olecmd.c` (C) -> Cumulative Risk: **836.94**
- **Archetype:** `file_cluster_8` (Distance: 12.097 IQR)
- **Magnitude:** 963.32 | **LOC:** 961 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9999%), State Flux (99.9998%)
- **Heaviest Functions:** `exec_print` (Impact: 85.5), `OleCommandTarget_QueryStatus` (Impact: 80.3), `set_print_template` (Impact: 69.2)

### 5. `dll/win32/dbghelp/pe_module.c` (C) -> Cumulative Risk: **832.29**
- **Archetype:** `file_cluster_13` (Distance: 13.222 IQR)
- **Magnitude:** 780.16 | **LOC:** 976 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `pe_locate_with_coff_symbol_table` (Impact: 135.8), `pe_load_coff_symbol_table` (Impact: 108.1), `pe_find_section` (Impact: 43.5)

### 6. `drivers/base/bootvid/i386/xbox/bootvid.c` (C) -> Cumulative Risk: **818.16**
- **Archetype:** `file_cluster_8` (Distance: 13.374 IQR)
- **Magnitude:** 514.32 | **LOC:** 431 | **CtrlFlow:** 91.8% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `VidInitialize` (Impact: 32.0), `DisplayCharacter` (Impact: 16.6), `ApplyPalette` (Impact: 16.1)

### 7. `drivers/filesystems/btrfs/zstd/fse_compress.c` (C) -> Cumulative Risk: **814.25**
- **Archetype:** `file_cluster_13` (Distance: 15.222 IQR)
- **Magnitude:** 1704.86 | **LOC:** 702 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `FSE_writeNCount_generic` (Impact: 236.2), `FSE_normalizeCount` (Impact: 174.5), `FSE_normalizeM2` (Impact: 173.2)

### 8. `base/applications/network/ftp/ftp.c` (C) -> Cumulative Risk: **812.43**
- **Archetype:** `file_cluster_8` (Distance: 13.987 IQR)
- **Magnitude:** 2762.36 | **LOC:** 1798 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `recvrequest` (Impact: 1284.0), `sendrequest` (Impact: 209.7), `getreply` (Impact: 60.0)

### 9. `boot/freeldr/freeldr/arch/uefi/uefihw.c` (C) -> Cumulative Risk: **811.77**
- **Archetype:** `file_cluster_8` (Distance: 12.435 IQR)
- **Magnitude:** 310.72 | **LOC:** 353 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `UefiFindAcpiTable` (Impact: 47.5), `DetectDisplayController` (Impact: 39.0), `DetectAcpiBios` (Impact: 20.5)

### 10. `dll/shellext/fontext/CFontExt.cpp` (CPP) -> Cumulative Risk: **807.11**
- **Archetype:** `file_cluster_8` (Distance: 13.191 IQR)
- **Magnitude:** 1496.74 | **LOC:** 725 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `CFontExt::MenuCallback` (Impact: 198.1), `CFontExt::ParseDisplayName` (Impact: 178.4), `CFontExt::GetUIObjectOf` (Impact: 169.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `base/setup/reactos/treelist.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.497 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.442 IQR)
- **Top Global Matches:** file_cluster_8: 15.497, file_cluster_7: 15.704, file_cluster_13: 15.767
- **Magnitude:** 20225.48 | **LOC:** 13734 | **CtrlFlow:** 85.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 506
- **Risk Profile:** Cognitive Load (48.6474%), Tech Debt (7.892%)
**Top Internal Functions/Classes:**
  * `TreeListProc` (Impact: 3023.1 | O(2^N) | DB: 506)
  * `TreeListDraw` (Impact: 948.6 | O(N^6) | DB: 355)
  * `TreeListMouseClick` (Impact: 669.5 | O(N^5) | DB: 140)
  * `TreeListInsertItem` (Impact: 288.6 | O(N^1) | DB: 229)
  * `TreeListKeyDown` (Impact: 285.0 | O(N^2) | DB: 121)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3246`, `structural_boundaries: 570`, `args: 12`, `func_start: 66`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 10609`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1320`, `import: 7`
* *Defense:* `safety: 1`, `doc: 150`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` string.h, windows.h, stdio.h, malloc.h, reactos.h, tchar.h, treelist.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/kernelbase/wine/locale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.645 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.687 IQR)
- **Top Global Matches:** file_cluster_8: 14.645, file_cluster_7: 14.811, file_cluster_13: 14.829
- **Magnitude:** 17313.6 | **LOC:** 8377 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (69.1847%), Tech Debt (12.3438%)
**Top Internal Functions/Classes:**
  * `get_locale_info` (Impact: 1838.1 | O(2^N) | DB: 76)
  * `append_weights` (Impact: 469.8 | O(N^6) | DB: 17)
  * `find_substring` (Impact: 439.9 | O(N^6) | DB: 39)
  * `lcmap_string` (Impact: 393.3 | O(N^6) | DB: 18)
    * *Intent:* 0x01, 0x00, 0x01, 0x00, /* U+30a8- */ 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, /* U+30b0- */
  * `get_calendar_info` (Impact: 375.4 | O(N^6) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2373`, `structural_boundaries: 937`, `args: 36`, `func_start: 235`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 4`, `state_mutation: 4671`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 23`
* *Architecture:* `api: 1876`, `import: 11`
* *Defense:* `doc: 129`, `immutability_locks: 402`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` winternl.h, stdlib.h, ntstatus.h, winreg.h, winbase.h, winuser.h, stdarg.h, kernelbase.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/directx/wine/wined3d/glsl_shader.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.356 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.073 IQR)
- **Top Global Matches:** file_cluster_8: 14.356, file_cluster_7: 14.625, file_cluster_13: 14.668
- **Magnitude:** 16761.12 | **LOC:** 11981 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 241
- **Risk Profile:** Cognitive Load (92.3811%), Tech Debt (66.2291%)
**Top Internal Functions/Classes:**
  * `shader_generate_glsl_declarations` (Impact: 3822.9 | O(N^6) | DB: 241)
  * `print_glsl_info_log` (Impact: 1937.8 | O(N^6) | DB: 238)
  * `shader_glsl_generate_ffp_fragment_shader` (Impact: 1176.8 | O(N^6) | DB: 101)
  * `set_glsl_shader_program` (Impact: 738.9 | O(N^5) | DB: 111)
  * `shader_glsl_generate_pshader` (Impact: 556.6 | O(N^6) | DB: 34)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1634`, `structural_boundaries: 1016`, `args: 161`, `func_start: 160`, `class_start: 293`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 3236`, `planned_debt: 1`, `fragile_debt: 52`, `orphaned_logic: 45`
* *Architecture:* `api: 1246`, `import: 6`
* *Defense:* `doc: 14`, `immutability_locks: 420`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` limits.h, port.h, wined3d_private.h, float.h, stdio.h, config.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/kernelbase/wine/path.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.534 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.378 IQR)
- **Top Global Matches:** file_cluster_8: 14.534, file_cluster_13: 14.683, file_cluster_11: 14.747
- **Magnitude:** 16697.16 | **LOC:** 5310 | **CtrlFlow:** 75.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 425
- **Risk Profile:** Cognitive Load (96.001%), Tech Debt (28.0384%)
**Top Internal Functions/Classes:**
  * `PathAllocCanonicalize` (Impact: 9651.9 | O(2^N) | DB: 425)
  * `rewrite_url` (Impact: 1287.5 | O(N^6) | DB: 114)
  * `UrlCombineW` (Impact: 605.8 | O(N^5) | DB: 83)
    * *Intent:* *out_len = lstrlenW(out);
  * `UrlEscapeW` (Impact: 254.4 | O(N^6) | DB: 67)
  * `UrlUnescapeW` (Impact: 138.2 | O(N^6) | DB: 35)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1438`, `structural_boundaries: 475`, `args: 58`, `func_start: 142`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 2841`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 10`, `orphaned_logic: 22`
* *Architecture:* `api: 763`, `import: 20`
* *Defense:* `safety: 17`, `doc: 4`, `immutability_locks: 179`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` strsafe.h, pathcch.h, winternl.h, string.h, winbase.h, heap.h, wchar.h, shlwapi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/samsrv/samrpc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.826 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.966 IQR)
- **Top Global Matches:** file_cluster_8: 13.826, file_cluster_12: 14.144, file_cluster_7: 14.175
- **Magnitude:** 14886.26 | **LOC:** 9825 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (85.1186%), Tech Debt (14.5045%)
**Top Internal Functions/Classes:**
  * `SamrSetInformationUser2` (Impact: 521.1 | O(2^N) | DB: 28)
  * `SamrQueryInformationUser2` (Impact: 520.5 | O(2^N) | DB: 28)
  * `SamrCreateUserInDomain` (Impact: 475.1 | O(2^N) | DB: 55)
  * `SamrLookupIdsInDomain` (Impact: 385.1 | O(2^N) | DB: 58)
  * `SampQueryUserAll` (Impact: 374.1 | O(N^6) | DB: 70)
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

### `dll/win32/winhttp/request.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.867 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.983 IQR)
- **Top Global Matches:** file_cluster_8: 14.867, file_cluster_11: 14.999, file_cluster_0: 15.013
- **Magnitude:** 12733.26 | **LOC:** 6172 | **CtrlFlow:** 61.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 152
- **Risk Profile:** Cognitive Load (78.027%), Tech Debt (29.9744%)
**Top Internal Functions/Classes:**
  * `receive_response` (Impact: 642.6 | O(2^N) | DB: 21)
  * `query_headers` (Impact: 601.9 | O(N^6) | DB: 63)
  * `send_request` (Impact: 458.4 | O(N^6) | DB: 34)
  * `do_authorization` (Impact: 403.4 | O(N^6) | DB: 79)
  * `open_connection` (Impact: 334.4 | O(N^6) | DB: 40)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1387`, `structural_boundaries: 864`, `args: 126`, `func_start: 193`, `class_start: 123`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 3962`, `dead_code: 1`, `fragile_debt: 31`, `orphaned_logic: 11`
* *Architecture:* `io: 433`, `api: 1010`, `import: 17`
* *Defense:* `safety: 21`, `doc: 9`, `test: 14`, `immutability_locks: 52`, `cleanup: 102`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` inet_ntop.c, initguid.h, winternl.h, ntsecapi.h, winbase.h, httprequest.h, schannel.h, httprequestid.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/storage/ide/uniata/id_init.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.831 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.801 IQR)
- **Top Global Matches:** file_cluster_8: 14.831, file_cluster_11: 15.149, file_cluster_13: 15.161
- **Magnitude:** 12182.26 | **LOC:** 2990 | **CtrlFlow:** 93.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 306
- **Risk Profile:** Cognitive Load (77.3048%), Tech Debt (8.7774%)
**Top Internal Functions/Classes:**
  * `UniataChipDetect` (Impact: 4114.4 | O(2^N) | DB: 306)
  * `AtapiChipInit` (Impact: 3898.7 | O(2^N) | DB: 305)
  * `UniataChipDetectChannels` (Impact: 1328.1 | O(2^N) | DB: 66)
  * `AtapiReadChipConfig` (Impact: 204.8 | O(2^N) | DB: 33)
  * `AtapiViaSouthBridgeFixup` (Impact: 89.1 | O(N^6) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 658`, `structural_boundaries: 49`, `args: 194`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 2254`, `dead_code: 12`, `fragile_debt: 2`
* *Architecture:* `import: 1`
* *Defense:* `safety: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdafx.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/storage/ide/uniata/id_ata.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.726 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.454 IQR)
- **Top Global Matches:** file_cluster_8: 14.726, file_cluster_11: 15.023, file_cluster_13: 15.084
- **Magnitude:** 11970.58 | **LOC:** 11726 | **CtrlFlow:** 88.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 368
- **Risk Profile:** Cognitive Load (94.5115%), Tech Debt (19.538%)
**Top Internal Functions/Classes:**
  * `AtapiStartIo__` (Impact: 2041.0 | O(N^6) | DB: 286)
  * `AtapiHwInitialize__` (Impact: 1905.5 | O(N^6) | DB: 368)
  * `DriverEntry` (Impact: 1064.1 | O(2^N) | DB: 146)
  * `AtaCommand48` (Impact: 996.8 | O(2^N) | DB: 38)
  * `UniataInitAtaCommands` (Impact: 424.2 | O(2^N) | DB: 28)
    * *Intent:* // Do nothing here
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1271`, `structural_boundaries: 161`, `args: 450`, `func_start: 51`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 3595`, `dead_code: 24`, `planned_debt: 6`, `fragile_debt: 11`, `orphaned_logic: 13`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `safety: 4`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdafx.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/rostests/winetests/d3dx9_36/mesh.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.824 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.423 IQR)
- **Top Global Matches:** file_cluster_8: 13.824, file_cluster_7: 14.159, file_cluster_13: 14.239
- **Magnitude:** 11195.52 | **LOC:** 11637 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 434
- **Risk Profile:** Cognitive Load (60.5915%), Tech Debt (8.2985%)
**Top Internal Functions/Classes:**
  * `check_vertex_components` (Impact: 647.7 | O(N^6) | DB: 56)
  * `compare_text_outline_mesh` (Impact: 410.1 | O(N^5) | DB: 84)
  * `create_outline` (Impact: 341.7 | O(N^6) | DB: 51)
  * `ID3DXAllocateHierarchyImpl_CreateMeshCon` (Impact: 250.2 | O(2^N) | DB: 33)
  * `check_vertex_buffer_` (Impact: 210.7 | O(N^6) | DB: 36)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 718`, `structural_boundaries: 558`, `args: 78`, `func_start: 97`, `class_start: 118`
* *Risk/State:* `safety_bypasses: 194`, `state_mutation: 4542`, `dead_code: 4`, `fragile_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 1784`, `import: 8`
* *Defense:* `safety: 6`, `immutability_locks: 941`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` initguid.h, limits.h, float.h, rmxftmpl.h, rmxfguid.h, stdio.h, d3dx9.h, test.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/filesystems/nfs/nfs41_driver.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.484 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.664 IQR)
- **Top Global Matches:** file_cluster_8: 14.484, file_cluster_11: 14.724, file_cluster_12: 14.753
- **Magnitude:** 10850.76 | **LOC:** 7245 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 369
- **Risk Profile:** Cognitive Load (83.9637%), Tech Debt (11.0833%)
**Top Internal Functions/Classes:**
  * `nfs41_UpcallWaitForReply` (Impact: 4346.4 | O(2^N) | DB: 369)
  * `nfs41_FinalizeNetRoot` (Impact: 236.2 | O(2^N) | DB: 16)
    * *Intent:* #else
  * `nfs41_QueryDirectory` (Impact: 101.2 | O(2^N) | DB: 31)
  * `marshal_nfs41_open` (Impact: 94.0 | O(2^N) | DB: 31)
  * `nfs41_SetEaInformation` (Impact: 89.5 | O(2^N) | DB: 26)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 990`, `structural_boundaries: 249`, `args: 1`, `func_start: 115`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2775`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 9`
* *Architecture:* `io: 34`, `api: 1307`, `import: 8`
* *Defense:* `safety: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` rx.h, nfs41_debug.h, ntstrsafe.h, nfs41_np.h, pseh2.h, winerror.h, nfs41_driver.h, windef.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/urlmon/uri.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.621 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.28 IQR)
- **Top Global Matches:** file_cluster_8: 14.621, file_cluster_7: 14.865, file_cluster_13: 14.865
- **Magnitude:** 10822.62 | **LOC:** 7329 | **CtrlFlow:** 77.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 415
- **Risk Profile:** Cognitive Load (93.3473%), Tech Debt (49.8673%)
**Top Internal Functions/Classes:**
  * `canonicalize_implicit_ipv4address` (Impact: 5972.6 | O(2^N) | DB: 415)
  * `combine_uri` (Impact: 216.9 | O(N^6) | DB: 77)
  * `parse_ipv6address` (Impact: 132.3 | O(N^6) | DB: 28)
  * `CoInternetParseIUri` (Impact: 130.1 | O(N^6) | DB: 19)
  * `parse_canonicalize` (Impact: 97.5 | O(N^6) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1046`, `structural_boundaries: 296`, `args: 2`, `func_start: 121`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 2618`, `planned_debt: 1`, `fragile_debt: 16`, `orphaned_logic: 22`
* *Architecture:* `api: 571`, `import: 6`
* *Defense:* `doc: 9`, `immutability_locks: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` strsafe.h, limits.h, wchar.h, shlwapi.h, urlmon_main.h, debug.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/filesystems/btrfs/flushthread.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.857 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.319 IQR)
- **Top Global Matches:** file_cluster_8: 14.857, file_cluster_11: 15.053, file_cluster_13: 15.097
- **Magnitude:** 10287.56 | **LOC:** 7947 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 352
- **Risk Profile:** Cognitive Load (82.6068%), Tech Debt (16.4478%)
**Top Internal Functions/Classes:**
  * `try_tree_amalgamate` (Impact: 1427.8 | O(N^6) | DB: 352)
  * `update_tree_extents` (Impact: 336.2 | O(N^6) | DB: 85)
  * `flush_fileref` (Impact: 225.8 | O(N^6) | DB: 87)
  * `write_trees` (Impact: 213.7 | O(N^6) | DB: 106)
  * `clean_space_cache_chunk` (Impact: 212.0 | O(N^6) | DB: 36)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1460`, `structural_boundaries: 605`, `args: 1`, `func_start: 55`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 4235`, `dead_code: 4`, `fragile_debt: 13`, `orphaned_logic: 9`
* *Architecture:* `io: 22`, `api: 936`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` crc32c.h, xxhash.h, ntddscsi.h, btrfs_drv.h, ntddstor.h, ata.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/storage/ide/uniata/id_dma.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.321 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.755 IQR)
- **Top Global Matches:** file_cluster_8: 15.321, file_cluster_11: 15.441, file_cluster_13: 15.49
- **Magnitude:** 10145.78 | **LOC:** 2735 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 422
- **Risk Profile:** Cognitive Load (71.8158%), Tech Debt (8.4376%)
**Top Internal Functions/Classes:**
  * `AtapiDmaInit` (Impact: 5671.8 | O(2^N) | DB: 422)
  * `AtapiDmaSetup` (Impact: 772.7 | O(2^N) | DB: 117)
  * `hpt_timing` (Impact: 707.0 | O(N^3) | DB: 86)
  * `promise_timing` (Impact: 295.1 | O(N^3) | DB: 56)
  * `AtapiDmaAlloc` (Impact: 245.4 | O(2^N) | DB: 36)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 687`, `structural_boundaries: 95`, `args: 111`, `func_start: 9`
* *Risk/State:* `state_mutation: 2237`, `dead_code: 15`, `fragile_debt: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 2`, `doc: 28`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdafx.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/msvcrt/file.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.889 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.455 IQR)
- **Top Global Matches:** file_cluster_8: 14.889, file_cluster_13: 14.93, file_cluster_7: 14.993
- **Magnitude:** 10089.04 | **LOC:** 5897 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 575
- **Risk Profile:** Cognitive Load (56.009%), Tech Debt (27.1326%)
**Top Internal Functions/Classes:**
  * `_fread_nolock` (Impact: 3586.6 | O(2^N) | DB: 239)
  * `msvcrt_create_io_inherit_block` (Impact: 2864.5 | O(N^6) | DB: 575)
  * `alloc_pioinfo_block` (Impact: 40.9 | O(N^4) | DB: 8)
  * `get_ioinfo_alloc` (Impact: 27.6 | O(N^4) | DB: 7)
  * `msvcrt_free_fd` (Impact: 27.4 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 877`, `structural_boundaries: 473`, `args: 104`, `func_start: 194`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 2493`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 12`, `duplicate_logic: 4`, `orphaned_logic: 6`
* *Architecture:* `io: 20`, `api: 815`, `import: 19`
* *Defense:* `safety: 45`, `doc: 167`, `immutability_locks: 111`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` winternl.h, mtdll.h, asm.h, types.h, windef.h, direct.h, msvcrt.h, utime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/msi/action.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.462 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.891 IQR)
- **Top Global Matches:** file_cluster_8: 14.462, file_cluster_13: 14.705, file_cluster_11: 14.734
- **Magnitude:** 9795.26 | **LOC:** 7854 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 62
- **Risk Profile:** Cognitive Load (75.2992%), Tech Debt (22.3467%)
**Top Internal Functions/Classes:**
  * `MSI_SetFeatureStates` (Impact: 283.6 | O(N^6) | DB: 47)
  * `ITERATE_WriteEnvironmentString` (Impact: 164.6 | O(N^4) | DB: 62)
  * `parse_prop` (Impact: 142.1 | O(N^4) | DB: 39)
  * `ACTION_ProcessComponents` (Impact: 114.9 | O(N^6) | DB: 25)
  * `ITERATE_InstallService` (Impact: 114.8 | O(N^6) | DB: 35)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1358`, `structural_boundaries: 535`, `args: 4`, `func_start: 208`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 4100`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 32`, `orphaned_logic: 3`
* *Architecture:* `io: 27`, `api: 1321`, `import: 18`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 87`, `cleanup: 169`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` winreg.h, odbcinst.h, shlobj.h, winbase.h, winsvc.h, winuser.h, winerror.h, objbase.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/directx/wine/wined3d/arb_program_shader.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.97 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.047 IQR)
- **Top Global Matches:** file_cluster_8: 13.97, file_cluster_7: 14.265, file_cluster_13: 14.3
- **Magnitude:** 9573.3 | **LOC:** 7944 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 311
- **Risk Profile:** Cognitive Load (92.9853%), Tech Debt (25.6654%)
**Top Internal Functions/Classes:**
  * `shader_hw_scalar_op` (Impact: 2738.1 | O(N^6) | DB: 311)
  * `shader_arb_get_register_name` (Impact: 934.3 | O(N^6) | DB: 45)
    * *Intent:* /* If further constants are dirty, reload them without clamping. * * The alternative is not to touch...
  * `gen_arbfp_ffp_shader` (Impact: 748.5 | O(N^6) | DB: 57)
  * `gen_ffp_instr` (Impact: 366.9 | O(N^3) | DB: 20)
  * `get_argreg` (Impact: 350.0 | O(N^4) | DB: 29)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1002`, `structural_boundaries: 600`, `args: 97`, `func_start: 98`, `class_start: 138`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 2181`, `planned_debt: 8`, `fragile_debt: 18`, `orphaned_logic: 7`
* *Architecture:* `io: 1`, `api: 675`, `import: 4`
* *Defense:* `doc: 5`, `immutability_locks: 253`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` wined3d_private.h, stdio.h, config.h, port.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/3rdparty/mbedtls/ssl_tls.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.94 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.37 IQR)
- **Top Global Matches:** file_cluster_8: 13.94, file_cluster_13: 14.285, file_cluster_7: 14.301
- **Magnitude:** 9299.18 | **LOC:** 9921 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 166
- **Risk Profile:** Cognitive Load (94.5597%), Tech Debt (29.6391%)
**Top Internal Functions/Classes:**
  * `mbedtls_ssl_read` (Impact: 2988.6 | O(N^6) | DB: 166)
    * *Intent:* /* * Handle possible client reconnect with the same UDP quadruplet
  * `mbedtls_ssl_flight_transmit` (Impact: 2051.9 | O(2^N) | DB: 90)
  * `mbedtls_ssl_handle_message_type` (Impact: 379.9 | O(N^6) | DB: 56)
  * `ssl_load_buffered_message` (Impact: 133.2 | O(N^6) | DB: 39)
  * `ssl_get_next_record` (Impact: 119.2 | O(N^6) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1103`, `structural_boundaries: 425`, `args: 9`, `func_start: 135`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1790`, `planned_debt: 1`, `orphaned_logic: 45`
* *Architecture:* `io: 20`, `api: 436`, `import: 9`
* *Defense:* `safety: 60`, `immutability_locks: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` config.h, stdlib.h, oid.h, string.h, debug.h, ssl_internal.h, platform.h, ssl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/system/services/rpcserver.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.482 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.776 IQR)
- **Top Global Matches:** file_cluster_8: 13.482, file_cluster_7: 13.811, file_cluster_13: 13.869
- **Magnitude:** 9273.86 | **LOC:** 6908 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 208
- **Risk Profile:** Cognitive Load (94.4154%), Tech Debt (26.7081%)
**Top Internal Functions/Classes:**
  * `Int_EnumDependentServicesW` (Impact: 2483.8 | O(2^N) | DB: 208)
  * `REnumServicesStatusExW` (Impact: 511.6 | O(2^N) | DB: 52)
  * `REnumServiceGroupW` (Impact: 447.1 | O(2^N) | DB: 48)
  * `RQueryServiceConfig2W` (Impact: 332.9 | O(2^N) | DB: 44)
  * `RQueryServiceConfigA` (Impact: 298.9 | O(2^N) | DB: 45)
    * *Intent:* /* Function 22 */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 900`, `structural_boundaries: 269`, `args: 1`, `func_start: 67`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1981`, `dead_code: 2`, `fragile_debt: 15`, `orphaned_logic: 21`
* *Architecture:* `io: 1`, `api: 1019`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` strsafe.h, services.h, pseh2.h, debug.h, winnls.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/directx/wine/wined3d/shader.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.444 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.135 IQR)
- **Top Global Matches:** file_cluster_8: 13.444, file_cluster_7: 13.764, file_cluster_13: 13.799
- **Magnitude:** 9196.1 | **LOC:** 4254 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 93
- **Risk Profile:** Cognitive Load (96.4412%), Tech Debt (81.926%)
**Top Internal Functions/Classes:**
  * `shader_get_registers_used` (Impact: 1996.8 | O(N^6) | DB: 93)
    * *Intent:* *current_phase = phase;
  * `shader_dump_register` (Impact: 987.6 | O(N^6) | DB: 4)
  * `shader_trace_init` (Impact: 970.3 | O(N^6) | DB: 23)
  * `find_ps_compile_args` (Impact: 826.1 | O(N^6) | DB: 66)
  * `pixel_shader_init` (Impact: 365.1 | O(2^N) | DB: 29)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1104`, `structural_boundaries: 437`, `args: 75`, `func_start: 76`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 4`, `state_mutation: 1274`, `fragile_debt: 32`, `orphaned_logic: 34`
* *Architecture:* `api: 645`, `import: 5`
* *Defense:* `safety: 3`, `immutability_locks: 134`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, port.h, wined3d_private.h, stdio.h, config.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/setupapi/cfgmgr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.87 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.706 IQR)
- **Top Global Matches:** file_cluster_8: 12.87, file_cluster_7: 13.105, file_cluster_13: 13.311
- **Magnitude:** 9080.1 | **LOC:** 8877 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (33.2779%), Tech Debt (30.5859%)
**Top Internal Functions/Classes:**
  * `CM_Open_DevNode_Key_Ex` (Impact: 203.2 | O(2^N) | DB: 21)
  * `CM_Delete_DevNode_Key_Ex` (Impact: 180.7 | O(2^N) | DB: 16)
  * `CM_Query_Resource_Conflict_List` (Impact: 159.7 | O(2^N) | DB: 18)
  * `CM_Get_Next_Res_Des_Ex` (Impact: 138.7 | O(2^N) | DB: 27)
    * *Intent:* /*********************************************************************** * CM_Get_Hardware_Profile_I...
  * `GetDeviceInstanceKeyPath` (Impact: 134.2 | O(2^N) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 922`, `structural_boundaries: 705`, `func_start: 153`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1821`, `fragile_debt: 48`, `orphaned_logic: 2`
* *Architecture:* `api: 2154`, `import: 7`
* *Defense:* `doc: 208`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` dbt.h, winsvc.h, rpc_private.h, winsvc_undoc.h, pseh2.h, pnp_c.h, setupapi_private.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/storage/ide/uniata/id_probe.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.519 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.532 IQR)
- **Top Global Matches:** file_cluster_8: 14.519, file_cluster_11: 14.844, file_cluster_13: 14.858
- **Magnitude:** 8960.4 | **LOC:** 3393 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 447
- **Risk Profile:** Cognitive Load (91.7608%), Tech Debt (11.631%)
**Top Internal Functions/Classes:**
  * `AtapiFindIsaController` (Impact: 3439.1 | O(2^N) | DB: 270)
  * `UniataEnumBusMasterController__` (Impact: 3079.6 | O(2^N) | DB: 447)
  * `AtapiGetIoRange` (Impact: 241.5 | O(2^N) | DB: 15)
  * `UniataEnableIoPCI` (Impact: 93.7 | O(N^6) | DB: 12)
  * `UniataCheckPCISubclass` (Impact: 57.8 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 528`, `structural_boundaries: 66`, `args: 193`, `func_start: 15`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 1961`, `dead_code: 10`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `import: 1`
* *Defense:* `safety: 4`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdafx.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/rpcrt4/ndr_marshall.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.49 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.739 IQR)
- **Top Global Matches:** file_cluster_8: 14.49, file_cluster_13: 14.634, file_cluster_7: 14.645
- **Magnitude:** 8727.62 | **LOC:** 7307 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 182
- **Risk Profile:** Cognitive Load (77.7337%), Tech Debt (67.909%)
**Top Internal Functions/Classes:**
  * `NdrPointerBufferSize` (Impact: 1033.6 | O(N^6) | DB: 182)
  * `ComplexStructMemorySize` (Impact: 369.6 | O(N^6) | DB: 26)
  * `ComplexUnmarshall` (Impact: 344.6 | O(N^6) | DB: 55)
  * `ComplexBufferSize` (Impact: 307.9 | O(N^6) | DB: 27)
  * `ComplexStructSize` (Impact: 133.8 | O(N^2) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1188`, `structural_boundaries: 286`, `args: 53`, `func_start: 115`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 3204`, `dead_code: 13`, `planned_debt: 17`, `fragile_debt: 57`, `orphaned_logic: 12`
* *Architecture:* `api: 1241`, `import: 16`
* *Defense:* `safety: 2`, `doc: 97`, `test: 1`, `immutability_locks: 212`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` poppack.h, limits.h, string.h, ndrtypes.h, winbase.h, pshpack1.h, winerror.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/ctf/cicero/cicuif.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.204 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.693 IQR)
- **Top Global Matches:** file_cluster_8: 15.204, file_cluster_7: 15.343, file_cluster_1: 15.559
- **Magnitude:** 8598.34 | **LOC:** 5474 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (34.5877%), Tech Debt (99.5335%)
**Top Internal Functions/Classes:**
  * `CUIFWindow::WindowProc` (Impact: 590.1 | O(N^6) | DB: 38)
  * `CUIFButton2::OnPaintNoTheme` (Impact: 219.1 | O(N^6) | DB: 74)
  * `CUIFMenu::InitShow` (Impact: 186.4 | O(N^3) | DB: 75)
  * `CUIFMenu::OnKeyDown` (Impact: 153.9 | O(N^5) | DB: 18)
  * `CUIFToolTip::RelayEvent` (Impact: 111.5 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 929`, `structural_boundaries: 459`, `args: 619`, `func_start: 267`
* *Risk/State:* `state_mutation: 3923`, `fragile_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 227`
* *Architecture:* `import: 2`
* *Defense:* `doc: 709`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cicuif.h, precomp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/services/umpnpmgr/rpcserver.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.22 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.662 IQR)
- **Top Global Matches:** file_cluster_8: 13.22, file_cluster_7: 13.578, file_cluster_13: 13.67
- **Magnitude:** 8433.94 | **LOC:** 5676 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (75.5236%), Tech Debt (29.5669%)
**Top Internal Functions/Classes:**
  * `PNP_GetDeviceRegProp` (Impact: 657.7 | O(2^N) | DB: 69)
  * `PNP_SetDeviceRegProp` (Impact: 335.9 | O(2^N) | DB: 24)
  * `PNP_AddEmptyLogConf` (Impact: 248.7 | O(2^N) | DB: 81)
  * `PNP_RegisterNotification` (Impact: 224.3 | O(2^N) | DB: 17)
  * `PNP_GetClassRegProp` (Impact: 202.2 | O(2^N) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 751`, `structural_boundaries: 211`, `func_start: 98`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1813`, `fragile_debt: 12`, `orphaned_logic: 27`
* *Architecture:* `io: 12`, `api: 1164`, `import: 2`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` debug.h, precomp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/bus/acpi_new/uacpi/source/interpreter.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.54 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.898 IQR)
- **Top Global Matches:** file_cluster_8: 14.54, file_cluster_13: 14.741, file_cluster_7: 14.834
- **Magnitude:** 8416.64 | **LOC:** 6052 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 392
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (23.2483%)
**Top Internal Functions/Classes:**
  * `resolve_name_string` (Impact: 2803.2 | O(N^6) | DB: 392)
    * *Intent:* // Only used if the method is serialized
  * `handle_create_buffer_field` (Impact: 1557.4 | O(N^6) | DB: 144)
  * `handle_mutex_ctl` (Impact: 114.8 | O(N^4) | DB: 15)
  * `uacpi_execute_control_method` (Impact: 95.1 | O(N^6) | DB: 12)
  * `handle_binary_logic` (Impact: 87.4 | O(N^4) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 845`, `structural_boundaries: 380`, `args: 57`, `func_start: 78`, `class_start: 97`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2160`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 23`
* *Architecture:* `io: 2`, `api: 767`, `import: 19`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` opcodes.h, notify.h, event.h, stdlib.h, resources.h, kernel_api.h, mutex.h, namespace.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `drivers/ksfilter/ks/misc.c` (C) | Magnitude: 91.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, api: 43, pointers: 26, state_mutation: 22
- `dll/opengl/mesa/clip.c` (C) | Magnitude: 486.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 306, pointers: 160, indent_spaces: 105, branch: 43
- `dll/directx/ddraw/Ddraw/ddraw_setcooperativelevel.c` (C) | Magnitude: 144.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 93, state_mutation: 55, pointers: 30, branch: 20
- `drivers/multimedia/audio/sndblst.old/dma.c` (C) | Magnitude: 67.86 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, pointers: 42, api: 20, state_mutation: 20
- `modules/rosapps/applications/sysutils/pedump/pedump.c` (C) | Magnitude: 1231.02 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 624, indent_spaces: 465, api: 294, pointers: 159

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `dll/win32/rsaenh/rsa.c` (C) | Magnitude: 379.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: pointers: 98, state_mutation: 68, indent_spaces: 67, branch: 36
- `dll/opengl/glu32/src/libnurbs/internals/arctess.cc` (CPP) | Magnitude: 825.18 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 570, indent_spaces: 184, pointers: 109, indent_tabs: 79
- `drivers/bus/acpi/busmgr/bus.c` (C) | Magnitude: 1241.76 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 437, state_mutation: 333, pointers: 180, branch: 172
- `dll/win32/riched20/paint.c` (C) | Magnitude: 140.44 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 105, indent_spaces: 104, pointers: 65, branch: 29
- `dll/opengl/glu32/src/libnurbs/nurbtess/monoChain.cc` (CPP) | Magnitude: 1230.06 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 742, indent_spaces: 280, pointers: 221, branch: 133

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `sdk/include/psdk/d3d.h` (C) | Magnitude: 60.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 993, macros: 810, reflection_metaprogramming: 614, indent_spaces: 307
- `sdk/include/psdk/specstrings.h` (C) | Magnitude: 24.18 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 143, reflection_metaprogramming: 92, branch: 19, indent_spaces: 11
- `sdk/include/psdk/mapival.h` (C) | Magnitude: 27.84 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 102, macros: 74, reflection_metaprogramming: 70, api: 11
- `boot/freeldr/freeldr/include/bytesex.h` (C) | Magnitude: 19.2 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 9, reflection_metaprogramming: 6, bitwise_ops: 6, state_mutation: 4
- `sdk/include/psdk/d3d9.h` (C) | Magnitude: 105.02 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 1664, macros: 1173, reflection_metaprogramming: 985, indent_spaces: 517

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `dll/directx/wine/d3dxof/mszip.c` (C) | Magnitude: 1359.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 596, indent_spaces: 390, branch: 95, api: 68
- `drivers/filesystems/btrfs/zstd/zstd_compress_sequences.h` (C) | Magnitude: 44.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 27, immutability_locks: 24, indent_spaces: 23, safety: 12
- `modules/rostests/tests/event/event.c` (C) | Magnitude: 31.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 21, state_mutation: 11, branch: 6, debug_prints: 6
- `drivers/network/tcpip/lwip/src/include/lwip/tcpbase.h` (C) | Magnitude: 41.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, macros: 15, indent_spaces: 11, api: 5
- `base/applications/network/telnet/src/tncon.cpp` (CPP) | Magnitude: 332.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 144, indent_tabs: 138, doc: 103, branch: 58

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `drivers/network/tcpip/lwip/codespell_check.sh` (SHELL) | Magnitude: 51.52 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 30, structural_boundaries: 13, branch: 11, indent_spaces: 11
- `dll/opengl/glu32/src/libnurbs/nurbtess/polyDBG.cc` (CPP) | Magnitude: 768.54 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 448, indent_spaces: 281, pointers: 214, branch: 127
- `dll/opengl/glu32/src/libnurbs/nurbtess/searchTree.cc` (CPP) | Magnitude: 274.94 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 158, indent_spaces: 122, pointers: 97, branch: 51
- `boot/freeldr/bootsect/fat.S` (ASSEMBLY) | Magnitude: 241.18 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 237, args: 203, structural_boundaries: 108, branch: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `base/applications/mspaint/help/usage.html` (HTML) | Magnitude: 16.72 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 12, structural_boundaries: 10, ui_framework: 8, args: 5
- `modules/rosapps/nukecamp/NSView.m` (OBJECTIVE-C) | Magnitude: 5.34 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: explicit_casts: 4, structural_boundaries: 2, args: 2, func_start: 2
- `modules/rostests/tests/button2/buttontst2.c` (C) | Magnitude: 129.22 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 51, ui_framework: 28, api: 23
- `base/applications/mspaint/help/tools.html` (HTML) | Magnitude: 17.46 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 36, ui_framework: 22, args: 17, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `boot/remaster.sh` (SHELL) | Magnitude: 163.78 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 72, indent_spaces: 46, debug_prints: 41, branch: 33
- `sdk/lib/3rdparty/stlport/src/cxa.c` (C) | Magnitude: 149.88 | Delta: **0.195 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 76, indent_spaces: 69, pointers: 54, structural_boundaries: 40
- `sdk/tools/rgenstat/web/index.html` (HTML) | Magnitude: 0.03 | Delta: **0.708 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 12, indent_tabs: 7, structural_boundaries: 4, io: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `dll/directx/wine/dmusic/clock.c` (C) | Magnitude: 81.7 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
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
- `dll/opengl/glu32/src/libnurbs/internals/varray.cc` (CPP) | Magnitude: 238.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 113, pointers: 38, indent_spaces: 38, branch: 24
- `dll/3rdparty/libtiff/tif_pixarlog.c` (C) | Magnitude: 1970.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 1118, indent_spaces: 673, pointers: 173, branch: 122
- `dll/win32/imaadp32.acm/imaadp32.c` (C) | Magnitude: 1107.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 469, indent_spaces: 418, pointers: 387, branch: 217
- `dll/win32/msrle32/msrle32.c` (C) | Magnitude: 2189.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1208, indent_spaces: 729, pointers: 490, branch: 365
- `dll/win32/qmgr/qmgr.h` (C) | Magnitude: 88.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 66, indent_spaces: 60, pointers: 22, structural_boundaries: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `drivers/filesystems/btrfs/zstd/zstd_compress_literals.h` (C) | Magnitude: 24.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 10, pointers: 10, api: 9, structural_boundaries: 7
- `drivers/network/tcpip/lwip/src/netif/ppp/upap.c` (C) | Magnitude: 11.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ownership: 3, branch: 2, macros: 2, import: 1
- `dll/win32/jscript/regexp.h` (C) | Magnitude: 41.0 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
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

- `dll/win32/winhttp/request.c` -> **winesync** (100.0% isolated ownership) | Magnitude: 12733.26
- `drivers/storage/ide/uniata/id_init.cpp` -> **Serge Gautherie** (100.0% isolated ownership) | Magnitude: 12182.26
- `drivers/storage/ide/uniata/id_ata.cpp` -> **Serge Gautherie** (100.0% isolated ownership) | Magnitude: 11970.58
- `drivers/storage/ide/uniata/id_dma.cpp` -> **Serge Gautherie** (100.0% isolated ownership) | Magnitude: 10145.78
- `dll/win32/msvcrt/file.c` -> **Timo Kreuzer** (100.0% isolated ownership) | Magnitude: 10089.04

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
- `sdk/tools/mkisofs/schilytools/include/schily/stdlib.h` -> **Severity: 1152.046** (Blast Radius: 14.209 * Doc Risk: 81.0786%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
