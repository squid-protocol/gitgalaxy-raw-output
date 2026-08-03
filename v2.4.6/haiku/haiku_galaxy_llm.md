# ARCHITECTURAL_BRIEF: haiku
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/OS/haiku` |
| **Timestamp** | `2026-08-03T19:08:04.798400+00:00` |
| **Scan Duration** | `66.85s` |
| **Git Branch** | `master` |
| **Git Commit** | `040fad1a4ab88eae509a1e098fe373b3041a03cf` |
| **Git Remote** | `https://github.com/haiku/haiku.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 15829 malicious artifacts.

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
| Total Artifacts | 26100 |
| Analyzed Artifacts (Scanned) | 16224 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9876 |
| Total LOC | 2368096 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 62.2% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0883 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1186 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 12402 | 1737946 | 76.4% |
| C | 3286 | 591017 | 20.3% |
| ASSEMBLY | 263 | 16519 | 1.6% |
| PLAINTEXT | 89 | 3 | 0.5% |
| SHELL | 85 | 4325 | 0.5% |
| MARKDOWN | 25 | 0 | 0.2% |
| PYTHON | 17 | 2173 | 0.1% |
| MAKEFILE | 16 | 5105 | 0.1% |
| HTML | 11 | 4699 | 0.1% |
| YACC | 7 | 3191 | 0.0% |
| BINARY_THREAT | 6 | 6 | 0.0% |
| XML | 4 | 16 | 0.0% |
| JSON | 3 | 285 | 0.0% |
| DOCKERFILE | 2 | 65 | 0.0% |
| GLSL | 2 | 42 | 0.0% |
| JAVASCRIPT | 2 | 1751 | 0.0% |
| RUBY | 1 | 25 | 0.0% |
| PHP | 1 | 634 | 0.0% |
| SCHEME | 1 | 131 | 0.0% |
| OBJECTIVE-C | 1 | 163 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.287`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 11115 | 68.5% |
| file_cluster_13 | 4614 | 28.4% |
| file_cluster_9 | 198 | 1.2% |
| file_cluster_12 | 81 | 0.5% |
| file_cluster_11 | 30 | 0.2% |
| file_cluster_0 | 24 | 0.1% |
| file_cluster_4 | 14 | 0.1% |
| file_cluster_16 | 11 | 0.1% |
| Unknown | 9 | 0.1% |
| file_cluster_17 | 6 | 0.0% |
| file_cluster_6 | 5 | 0.0% |
| file_cluster_7 | 5 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 111 | 0.7% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9876*

**Composition by Extension & Reason:**
- `.catkeys`: 5283x Excluded (Unsupported Extension: '.catkeys'), 140x Unsupported Format (.catkeys), 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1601x Unsupported Format (.undeterminable), 766x Excluded (Binary Format Detected), 207x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 368x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 101 LOC), 1x Excluded (Embedded Array/Matrix Payload: 2886 commas in 797 LOC)
- `.rdef`: 337x Unsupported Format (.rdef), 1x Excluded (Embedded Array/Matrix Payload: 9733 commas in 2476 LOC), 1x Excluded (Embedded Hex Payload: 1098 hex tokens in 557 LOC)
- `.dox`: 228x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 120x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 2836 commas in 844 LOC), 1x Excluded (Embedded Hex Payload: 12628 hex tokens in 1595 LOC)
- `.png`: 118x Excluded (Explicitly Denied Extension: '.png')
- `.rst`: 112x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.keymap`: 68x Unsupported Format (.keymap)
- `.html`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 44 exceeds 500 chars), 1x Excluded (Saturation: Line 66 exceeds 500 chars)
- `.c`: 7x Excluded (Embedded Hex Payload: 31147 hex tokens in 3937 LOC), 3x Excluded (Embedded Hex Payload: 31146 hex tokens in 3934 LOC), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ld`: 31x Unsupported Format (.ld)
- `.ini`: 2x Unsupported Format (.ini), 1x Excluded (Embedded Hex Payload: 3386 hex tokens in 1537 LOC), 1x Excluded (Embedded Hex Payload: 4064 hex tokens in 1895 LOC)
- `.txt`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 13x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 41.4 | 34.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 33.7 | 18.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.8 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.9 | 3.1 | 1.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 55.3 | 84.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 85.6 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 37.0 | 20.2 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `3rdparty/mmu_man/scripts/HardwareChecker.sh` (Hits: 523)
- `src/add-ons/kernel/network/stack/net_socket.cpp` (Hits: 312)
- `configure` (Hits: 216)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **stdlib.h** (`src/system/libroot/posix/glibc/include/stdlib.h`) — 1725 inbound connections
2. **SupportDefs.h** (`headers/os/support/SupportDefs.h`) — 861 inbound connections
3. **OS.h** (`headers/os/kernel/OS.h`) — 838 inbound connections
4. **Catalog.h** (`headers/os/locale/Catalog.h`) — 718 inbound connections
5. **Application.h** (`headers/os/app/Application.h`) — 648 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **converters.h** (`src/libs/iconv/converters.h`) — 145 outbound dependencies
2. **MainWindow.cpp** (`src/apps/icon-o-matic/MainWindow.cpp`) — 75 outbound dependencies
3. **if_ath.c** (`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/if_ath.c`) — 65 outbound dependencies
4. **iflib.c** (`src/libs/compat/freebsd_iflib/iflib.c`) — 64 outbound dependencies
5. **if_ath_descdma.c** (`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/if_ath_descdma.c`) — 60 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `interpolate` (@ `src/add-ons/kernel/drivers/network/wlan/atheroswifi/contrib/ath_hal/ar9300/ar9300_eeprom.c`) -> Impact: **4641.2** | LOC: 1413
- `tulip_read_macaddr` (@ `src/add-ons/kernel/drivers/network/ether/dec21xxx/dev/de/if_de.c`) -> Impact: **4386.0** | LOC: 1637
- `makeruledecisions` (@ `src/libs/libsolv/solv/solver.c`) -> Impact: **4219.7** | LOC: 1834
- `sis_miibus_statchg` (@ `src/add-ons/kernel/drivers/network/ether/sis900/dev/sis/if_sis.c`) -> Impact: **4000.9** | LOC: 1619
  * *Intent:* /*
- `e1000_init_phy_workarounds_pchlan` (@ `src/add-ons/kernel/drivers/network/ether/ipro1000/dev/e1000/e1000_ich8lan.c`) -> Impact: **3941.6** | LOC: 2192
- `jobtodisablelist` (@ `src/libs/libsolv/solv/rules.c`) -> Impact: **3416.9** | LOC: 1273
- `ABSApp::LoadSaveDatabase` (@ `src/bin/mail_utils/spamdbm.cpp`) -> Impact: **3068.0** | LOC: 1830
  * *Intent:* /* The scrolling display starts at this word. Since we can't use index
- `fAllowWinding` (@ `src/apps/mediaplayer/MainWin.cpp`) -> Impact: **3037.3** | LOC: 2134
- `iflib_tx_desc_free` (@ `src/libs/compat/freebsd_iflib/iflib.c`) -> Impact: **2598.3** | LOC: 2056
- `run_vap_create` (@ `src/add-ons/kernel/drivers/network/wlan/ralinkwifi/dev/usb/wlan/if_run.c`) -> Impact: **2581.3** | LOC: 2072
  * *Intent:* /* stop all USB transfers */

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__init__` (@ `3rdparty/mmu_man/irc/Haiku/plugin.py`) -> **O(2^N) [Recursive]**
  * *Intent:* #log.error("plop") #print "plop" self.fortunes = [] fortunes = open("/home/revol/devel/haiku/trunk/data/system/data/fortunes/Haiku", "r") print fortun...
- `__merge_adaptive` (@ `headers/cpp/stl_algo.h`) -> **O(2^N) [Recursive]**
- `__merge_adaptive` (@ `headers/cpp/stl_algo.h`) -> **O(2^N) [Recursive]**
- `__merge_without_buffer` (@ `headers/cpp/stl_algo.h`) -> **O(2^N) [Recursive]**
- `__merge_without_buffer` (@ `headers/cpp/stl_algo.h`) -> **O(2^N) [Recursive]**
- `__stable_partition_adaptive` (@ `headers/cpp/stl_algo.h`) -> **O(2^N) [Recursive]**
- `__stable_sort_adaptive` (@ `headers/cpp/stl_algo.h`) -> **O(2^N) [Recursive]**
- `__introsort_loop` (@ `headers/cpp/stl_algo.h`) -> **O(2^N) [Recursive]**
- `__introsort_loop` (@ `headers/cpp/stl_algo.h`) -> **O(2^N) [Recursive]**
- `__stable_sort_adaptive` (@ `headers/cpp/stl_algo.h`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `3rdparty/mmu_man/scripts/HardwareChecker.sh`) -> DB Complexity: **1440**
- `Anonymous_Block_[Truncated]` (@ `configure`) -> DB Complexity: **834**
- `rt2860_rx_intr` (@ `src/add-ons/kernel/drivers/network/wlan/ralinkwifi/dev/ral/rt2860.c`) -> DB Complexity: **622**
- `dosfs_can_page` (@ `src/add-ons/kernel/file_systems/fat/kernel_interface.cpp`) -> DB Complexity: **559**
- `Volume::Unmount` (@ `src/add-ons/kernel/file_systems/userlandfs/kernel_add_on/Volume.cpp`) -> DB Complexity: **555**
- `BPoseView::FSNotification` (@ `src/kits/tracker/PoseView.cpp`) -> DB Complexity: **538**
- `get_file_system` (@ `src/tools/fs_shell/vfs.cpp`) -> DB Complexity: **538**
- `BPoseView::SavePoseLocations` (@ `src/kits/tracker/PoseView.cpp`) -> DB Complexity: **536**
- `nv_general_powerup` (@ `src/add-ons/accelerants/nvidia/engine/nv_general.c`) -> DB Complexity: **531**
- `run_vap_create` (@ `src/add-ons/kernel/drivers/network/wlan/ralinkwifi/dev/usb/wlan/if_run.c`) -> DB Complexity: **524**
  * *Intent:* /* stop all USB transfers */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/kits/interface` | 107 | 55575.4 | 66.09% | 92.86% |
| `src/kits/tracker` | 138 | 48139.37 | 44.45% | 49.45% |
| `headers/libs/agg` | 119 | 47472.4 | 55.7% | 76.56% |
| `src/libs/libsolv/solv` | 65 | 37724.12 | 44.8% | 22.4% |
| `src/add-ons/kernel/drivers/network/ether/ipro1000/dev/e1000` | 41 | 36010.78 | 35.94% | 7.63% |
| `src/add-ons/kernel/file_systems/ntfs/libntfs` | 73 | 34383.7 | 43.66% | 20.44% |
| `src/libs/compat/freebsd_wlan/net80211` | 78 | 30790.4 | 47.77% | 48.64% |
| `src/system/libroot/posix/glibc/stdio-common` | 37 | 28039.5 | 43.88% | 19.15% |
| `src/libs/iconv` | 180 | 24950.19 | 55.91% | 2.11% |
| `src/servers/app` | 95 | 20365.2 | 41.36% | 49.47% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `3rdparty/cloud/sysprep-gce.sh` -> **100.0%** Exposure
- `3rdparty/docker/bootstrap/bootstrap.sh` -> **100.0%** Exposure
- `3rdparty/docker/bootstrap/crosstools.sh` -> **100.0%** Exposure
- `3rdparty/docker/bootstrap/haikuports_chroot.sh` -> **100.0%** Exposure
- `3rdparty/docker/bootstrap/prep.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `3rdparty/kallisti5/mksysroot.sh` -> **100.0%** Exposure
- `3rdparty/kallisti5/validateBootstrapRepo` -> **100.0%** Exposure
- `3rdparty/kallisti5/validateRepoFile` -> **100.0%** Exposure
- `3rdparty/mmu_man/scripts/bepo/gen-bepo.sh` -> **100.0%** Exposure
- `3rdparty/mmu_man/scripts/bepo/parse_linux_keymap.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/system/libroot/stubbed/libroot_stubs.c` -> **246** Orphaned Functions | **4** Duplicates
- `src/system/libroot/stubbed/libroot_stubs_legacy.c` -> **246** Orphaned Functions | **4** Duplicates
- `src/kits/debugger/dwarf/DebugInfoEntries.cpp` -> **246** Orphaned Functions | **2** Duplicates
- `src/kits/support/String.cpp` -> **58** Orphaned Functions | **139** Duplicates
- `src/kits/interface/View.cpp` -> **94** Orphaned Functions | **84** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/add-ons/accelerants/intel_extreme/Pipes.cpp`** -> AI Confidence: **99.48%**
2. **`src/add-ons/accelerants/intel_extreme/pll.cpp`** -> AI Confidence: **99.48%**
3. **`src/add-ons/accelerants/radeon_hd/connector.cpp`** -> AI Confidence: **99.48%**
4. **`src/add-ons/accelerants/radeon_hd/display.cpp`** -> AI Confidence: **99.48%**
5. **`src/add-ons/accelerants/radeon_hd/encoder.cpp`** -> AI Confidence: **99.48%**
6. **`src/add-ons/accelerants/radeon_hd/pll.cpp`** -> AI Confidence: **99.48%**
7. **`src/add-ons/control_look/BeControlLook/BeControlLook.cpp`** -> AI Confidence: **99.48%**
8. **`src/add-ons/control_look/FlatControlLook/FlatControlLook.cpp`** -> AI Confidence: **99.48%**
9. **`src/add-ons/decorators/BeDecorator/BeDecorator.cpp`** -> AI Confidence: **99.48%**
10. **`src/add-ons/decorators/FlatDecorator/FlatDecorator.cpp`** -> AI Confidence: **99.48%**
11. **`src/add-ons/input_server/devices/mouse/movement_maker.cpp`** -> AI Confidence: **99.48%**
12. **`src/add-ons/input_server/devices/wacom/TabletDevice.cpp`** -> AI Confidence: **99.48%**
13. **`src/add-ons/input_server/filters/minimize_all/MinimizeAllInputFilter.cpp`** -> AI Confidence: **99.48%**
14. **`src/add-ons/input_server/filters/shortcut_catcher/CommandActuators.cpp`** -> AI Confidence: **99.48%**
15. **`src/add-ons/input_server/filters/shortcut_catcher/KeyCommandMap.cpp`** -> AI Confidence: **99.48%**
16. **`src/add-ons/input_server/filters/switch_workspace/SwitchWorkspaceInputFilter.cpp`** -> AI Confidence: **99.48%**
17. **`src/add-ons/input_server/methods/pen/DumpMessage.cpp`** -> AI Confidence: **99.48%**
18. **`src/add-ons/input_server/methods/pen/PenInputLooper.cpp`** -> AI Confidence: **99.48%**
19. **`src/add-ons/input_server/methods/pen/PenInputServerMethod.cpp`** -> AI Confidence: **99.48%**
20. **`src/add-ons/kernel/bus_managers/acpi/EmbeddedController.cpp`** -> AI Confidence: **99.48%**
21. **`src/add-ons/kernel/bus_managers/acpi/acpica/include/platform/acenv.h`** -> AI Confidence: **99.48%**
22. **`src/add-ons/kernel/busses/agp_gart/intel_gart.cpp`** -> AI Confidence: **99.48%**
23. **`src/add-ons/kernel/drivers/audio/echo/generic/CMonaDspCommObject.cpp`** -> AI Confidence: **99.48%**
24. **`src/add-ons/kernel/drivers/bluetooth/h2/h2generic/h2upper.cpp`** -> AI Confidence: **99.48%**
25. **`src/add-ons/kernel/drivers/graphics/intel_extreme/intel_extreme.cpp`** -> AI Confidence: **99.48%**
26. **`src/add-ons/kernel/drivers/graphics/vesa/patch.cpp`** -> AI Confidence: **99.48%**
27. **`src/add-ons/kernel/drivers/input/hid_shared/HIDCollection.cpp`** -> AI Confidence: **99.48%**
28. **`src/add-ons/kernel/drivers/input/hid_shared/HIDParser.cpp`** -> AI Confidence: **99.48%**
29. **`src/add-ons/kernel/drivers/input/hid_shared/KeyboardProtocolHandler.cpp`** -> AI Confidence: **99.48%**
30. **`src/add-ons/kernel/drivers/input/hid_shared/TabletProtocolHandler.cpp`** -> AI Confidence: **99.48%**
31. **`src/add-ons/kernel/file_systems/bfs/system_dependencies.h`** -> AI Confidence: **99.48%**
32. **`src/add-ons/kernel/file_systems/netfs/netfs_server_prefs/NetFSServerPrefs.cpp`** -> AI Confidence: **99.48%**
33. **`src/add-ons/kernel/file_systems/netfs/server/NodeMonitor.cpp`** -> AI Confidence: **99.48%**
34. **`src/add-ons/kernel/file_systems/ramfs/DataContainer.cpp`** -> AI Confidence: **99.48%**
35. **`src/add-ons/kernel/file_systems/ramfs/Directory.cpp`** -> AI Confidence: **99.48%**
36. **`src/add-ons/kernel/file_systems/ramfs/IndexDirectory.cpp`** -> AI Confidence: **99.48%**
37. **`src/add-ons/kernel/file_systems/reiserfs/Iterators.cpp`** -> AI Confidence: **99.48%**
38. **`src/add-ons/kernel/file_systems/reiserfs/Volume.cpp`** -> AI Confidence: **99.48%**
39. **`src/add-ons/kernel/file_systems/ufs2/system_dependencies.h`** -> AI Confidence: **99.48%**
40. **`src/add-ons/kernel/file_systems/userlandfs/server/UserlandFSServer.cpp`** -> AI Confidence: **99.48%**
41. **`src/add-ons/kernel/network/ppp/ipcp/Protocol.cpp`** -> AI Confidence: **99.48%**
42. **`src/add-ons/kernel/network/protocols/ipv6/ipv6_utils.cpp`** -> AI Confidence: **99.48%**
43. **`src/add-ons/kernel/network/protocols/unix/UnixStreamEndpoint.cpp`** -> AI Confidence: **99.48%**
44. **`src/add-ons/kernel/partitioning_systems/intel/PartitionMapParser.cpp`** -> AI Confidence: **99.48%**
45. **`src/add-ons/media/media-add-ons/dvb/DVBMediaNode.cpp`** -> AI Confidence: **99.48%**
46. **`src/add-ons/media/media-add-ons/dvb/TransportStreamDemux.cpp`** -> AI Confidence: **99.48%**
47. **`src/add-ons/media/media-add-ons/mixer/AudioMixer.cpp`** -> AI Confidence: **99.48%**
48. **`src/add-ons/media/media-add-ons/usb_vision/Producer.cpp`** -> AI Confidence: **99.48%**
49. **`src/add-ons/media/plugins/ape_reader/MAClib/APEDecompress.cpp`** -> AI Confidence: **99.48%**
50. **`src/add-ons/media/plugins/ape_reader/MAClib/APESimple.cpp`** -> AI Confidence: **99.48%**
51. **`src/add-ons/media/plugins/au_reader/au_reader.cpp`** -> AI Confidence: **99.48%**
52. **`src/add-ons/media/plugins/raw_decoder/RawDecoderPlugin.cpp`** -> AI Confidence: **99.48%**
53. **`src/add-ons/print/drivers/preview/JobSetupWindow.cpp`** -> AI Confidence: **99.48%**
54. **`src/add-ons/print/drivers/preview/PageSetupWindow.cpp`** -> AI Confidence: **99.48%**
55. **`src/add-ons/print/transports/shared/DbgMsg.cpp`** -> AI Confidence: **99.48%**
56. **`src/add-ons/screen_savers/ifs/IFS.cpp`** -> AI Confidence: **99.48%**
57. **`src/add-ons/screen_savers/spider/SpiderView.cpp`** -> AI Confidence: **99.48%**
58. **`src/add-ons/tracker/zipomatic/ZipOMatic.cpp`** -> AI Confidence: **99.48%**
59. **`src/add-ons/tracker/zipomatic/ZipOMaticWindow.cpp`** -> AI Confidence: **99.48%**
60. **`src/add-ons/translators/avif/ConfigView.cpp`** -> AI Confidence: **99.48%**
61. **`src/add-ons/translators/gif/GIFView.cpp`** -> AI Confidence: **99.48%**
62. **`src/add-ons/translators/png/PNGTranslator.cpp`** -> AI Confidence: **99.48%**
63. **`src/add-ons/translators/ppm/PPMTranslator.cpp`** -> AI Confidence: **99.48%**
64. **`src/add-ons/translators/ppm/colorspace.cpp`** -> AI Confidence: **99.48%**
65. **`src/add-ons/translators/raw/ConfigView.cpp`** -> AI Confidence: **99.48%**
66. **`src/add-ons/translators/raw/main.cpp`** -> AI Confidence: **99.48%**
67. **`src/add-ons/translators/sgi/SGITranslator.cpp`** -> AI Confidence: **99.48%**
68. **`src/add-ons/translators/wonderbrush/Layer.cpp`** -> AI Confidence: **99.48%**
69. **`src/apps/cortex/DiagramView/DiagramView.cpp`** -> AI Confidence: **99.48%**
70. **`src/apps/cortex/InfoView/AppNodeInfoView.cpp`** -> AI Confidence: **99.48%**
71. **`src/apps/cortex/InfoView/ConnectionInfoView.cpp`** -> AI Confidence: **99.48%**
72. **`src/apps/cortex/InfoView/DormantNodeInfoView.cpp`** -> AI Confidence: **99.48%**
73. **`src/apps/cortex/InfoView/FileNodeInfoView.cpp`** -> AI Confidence: **99.48%**
74. **`src/apps/cortex/InfoView/LiveNodeInfoView.cpp`** -> AI Confidence: **99.48%**
75. **`src/apps/cortex/MediaRoutingView/MediaNodePanel.cpp`** -> AI Confidence: **99.48%**
76. **`src/apps/cortex/MediaRoutingView/MediaRoutingView.cpp`** -> AI Confidence: **99.48%**
77. **`src/apps/cortex/ParameterView/ParameterWindow.cpp`** -> AI Confidence: **99.48%**
78. **`src/apps/cortex/support/MediaIcon.cpp`** -> AI Confidence: **99.48%**
79. **`src/apps/debuganalyzer/gui/thread_window/ActivityPage.cpp`** -> AI Confidence: **99.48%**
80. **`src/apps/debugger/user_interface/gui/inspector_window/MemoryView.cpp`** -> AI Confidence: **99.48%**
81. **`src/apps/debugger/user_interface/gui/utility_windows/WatchPromptWindow.cpp`** -> AI Confidence: **99.48%**
82. **`src/apps/deskbar/BarApp.cpp`** -> AI Confidence: **99.48%**
83. **`src/apps/deskbar/PreferencesWindow.cpp`** -> AI Confidence: **99.48%**
84. **`src/apps/deskbar/ScreenCornerSelector.cpp`** -> AI Confidence: **99.48%**
85. **`src/apps/deskbar/WindowMenu.cpp`** -> AI Confidence: **99.48%**
86. **`src/apps/deskbar/WindowMenuItem.cpp`** -> AI Confidence: **99.48%**
87. **`src/apps/deskcalc/CalcView.cpp`** -> AI Confidence: **99.48%**
88. **`src/apps/devices/DevicePCI.cpp`** -> AI Confidence: **99.48%**
89. **`src/apps/devices/DeviceUSB.cpp`** -> AI Confidence: **99.48%**
90. **`src/apps/devices/DevicesView.cpp`** -> AI Confidence: **99.48%**
91. **`src/apps/diskprobe/OpenWindow.cpp`** -> AI Confidence: **99.48%**
92. **`src/apps/diskusage/App.cpp`** -> AI Confidence: **99.48%**
93. **`src/apps/expander/ExpanderPreferences.cpp`** -> AI Confidence: **99.48%**
94. **`src/apps/expander/ExpanderWindow.cpp`** -> AI Confidence: **99.48%**
95. **`src/apps/fontdemo/ControlView.cpp`** -> AI Confidence: **99.48%**
96. **`src/apps/fontdemo/FontDemoView.cpp`** -> AI Confidence: **99.48%**
97. **`src/apps/glteapot/ObjectView.cpp`** -> AI Confidence: **99.48%**
98. **`src/apps/haikudepot/server/AbstractSingleFileServerProcess.cpp`** -> AI Confidence: **99.48%**
99. **`src/apps/haikudepot/server/ServerHelper.cpp`** -> AI Confidence: **99.48%**
100. **`src/apps/haikudepot/ui/MainWindow.cpp`** -> AI Confidence: **99.48%**
101. **`src/apps/icon-o-matic/IconEditorApp.cpp`** -> AI Confidence: **99.48%**
102. **`src/apps/icon-o-matic/document/SetPropertiesCommand.cpp`** -> AI Confidence: **99.48%**
103. **`src/apps/icon-o-matic/generic/gui/IconButton.cpp`** -> AI Confidence: **99.48%**
104. **`src/apps/icon-o-matic/generic/gui/panel/color_picker/ColorPickerView.cpp`** -> AI Confidence: **99.48%**
105. **`src/apps/icon-o-matic/generic/gui/panel/color_picker/ColorSlider.cpp`** -> AI Confidence: **99.48%**
106. **`src/apps/icon-o-matic/generic/support/support.cpp`** -> AI Confidence: **99.48%**
107. **`src/apps/icon-o-matic/generic/support/support_settings.cpp`** -> AI Confidence: **99.48%**
108. **`src/apps/icon-o-matic/generic/support/support_ui.cpp`** -> AI Confidence: **99.48%**
109. **`src/apps/icon-o-matic/gui/GradientControl.cpp`** -> AI Confidence: **99.48%**
110. **`src/apps/icon-o-matic/gui/SwatchGroup.cpp`** -> AI Confidence: **99.48%**
111. **`src/apps/icon-o-matic/import_export/svg/DocumentBuilder.cpp`** -> AI Confidence: **99.48%**
112. **`src/apps/icon-o-matic/import_export/svg/SVGExporter.cpp`** -> AI Confidence: **99.48%**
113. **`src/apps/icon-o-matic/shape/commands/FreezeTransformationCommand.cpp`** -> AI Confidence: **99.48%**
114. **`src/apps/icon-o-matic/transformable/TransformBoxStates.cpp`** -> AI Confidence: **99.48%**
115. **`src/apps/installer/EULAWindow.cpp`** -> AI Confidence: **99.48%**
116. **`src/apps/launchbox/LaunchButton.cpp`** -> AI Confidence: **99.48%**
117. **`src/apps/launchbox/MainWindow.cpp`** -> AI Confidence: **99.48%**
118. **`src/apps/launchbox/NamePanel.cpp`** -> AI Confidence: **99.48%**
119. **`src/apps/launchbox/support.cpp`** -> AI Confidence: **99.48%**
120. **`src/apps/login/DesktopWindow.cpp`** -> AI Confidence: **99.48%**
121. **`src/apps/login/LoginView.cpp`** -> AI Confidence: **99.48%**
122. **`src/apps/mail/Content.cpp`** -> AI Confidence: **99.48%**
123. **`src/apps/mail/Enclosures.cpp`** -> AI Confidence: **99.48%**
124. **`src/apps/mail/LabelWindow.cpp`** -> AI Confidence: **99.48%**
125. **`src/apps/mail/MailWindow.cpp`** -> AI Confidence: **99.48%**
126. **`src/apps/mail/Prefs.cpp`** -> AI Confidence: **99.48%**
127. **`src/apps/mail/Signature.cpp`** -> AI Confidence: **99.48%**
128. **`src/apps/mail/Status.cpp`** -> AI Confidence: **99.48%**
129. **`src/apps/mandelbrot/FractalEngine.cpp`** -> AI Confidence: **99.48%**
130. **`src/apps/mediaconverter/MediaConverterApp.cpp`** -> AI Confidence: **99.48%**
131. **`src/apps/mediaplayer/MainWin.cpp`** -> AI Confidence: **99.48%**
132. **`src/apps/mediaplayer/playlist/PlaylistFileReader.cpp`** -> AI Confidence: **99.48%**
133. **`src/apps/mediaplayer/playlist/RemovePLItemsCommand.cpp`** -> AI Confidence: **99.48%**
134. **`src/apps/midiplayer/MidiPlayerWindow.cpp`** -> AI Confidence: **99.48%**
135. **`src/apps/packageinstaller/PackageInfo.cpp`** -> AI Confidence: **99.48%**
136. **`src/apps/packageinstaller/PackageView.cpp`** -> AI Confidence: **99.48%**
137. **`src/apps/pairs/PairsWindow.cpp`** -> AI Confidence: **99.48%**
138. **`src/apps/patchbay/PatchView.cpp`** -> AI Confidence: **99.48%**
139. **`src/apps/people/PeopleApp.cpp`** -> AI Confidence: **99.48%**
140. **`src/apps/people/PersonWindow.cpp`** -> AI Confidence: **99.48%**
141. **`src/apps/poorman/PoorManApplication.cpp`** -> AI Confidence: **99.48%**
142. **`src/apps/poorman/PoorManPreferencesWindow.cpp`** -> AI Confidence: **99.48%**
143. **`src/apps/powerstatus/ExtendedInfoWindow.cpp`** -> AI Confidence: **99.48%**
144. **`src/apps/powerstatus/PowerStatusView.cpp`** -> AI Confidence: **99.48%**
145. **`src/apps/processcontroller/KernelMemoryBarMenuItem.cpp`** -> AI Confidence: **99.48%**
146. **`src/apps/processcontroller/MemoryBarMenu.cpp`** -> AI Confidence: **99.48%**
147. **`src/apps/processcontroller/MemoryBarMenuItem.cpp`** -> AI Confidence: **99.48%**
148. **`src/apps/processcontroller/ProcessController.cpp`** -> AI Confidence: **99.48%**
149. **`src/apps/processcontroller/TeamBarMenu.cpp`** -> AI Confidence: **99.48%**
150. **`src/apps/processcontroller/TeamBarMenuItem.cpp`** -> AI Confidence: **99.48%**
151. **`src/apps/pulse/ConfigView.cpp`** -> AI Confidence: **99.48%**
152. **`src/apps/pulse/NormalPulseView.cpp`** -> AI Confidence: **99.48%**
153. **`src/apps/pulse/PulseApp.cpp`** -> AI Confidence: **99.48%**
154. **`src/apps/pulse/PulseView.cpp`** -> AI Confidence: **99.48%**
155. **`src/apps/pulse/PulseWindow.cpp`** -> AI Confidence: **99.48%**
156. **`src/apps/screenshot/Screenshot.cpp`** -> AI Confidence: **99.48%**
157. **`src/apps/screenshot/ScreenshotApp.cpp`** -> AI Confidence: **99.48%**
158. **`src/apps/screenshot/SelectAreaView.cpp`** -> AI Confidence: **99.48%**
159. **`src/apps/serialconnect/SerialWindow.cpp`** -> AI Confidence: **99.48%**
160. **`src/apps/showimage/ProgressWindow.cpp`** -> AI Confidence: **99.48%**
161. **`src/apps/softwareupdater/SoftwareUpdaterWindow.cpp`** -> AI Confidence: **99.48%**
162. **`src/apps/sudoku/ProgressWindow.cpp`** -> AI Confidence: **99.48%**
163. **`src/apps/sudoku/SudokuGenerator.cpp`** -> AI Confidence: **99.48%**
164. **`src/apps/switcher/LaunchButton.cpp`** -> AI Confidence: **99.48%**
165. **`src/apps/switcher/PanelWindow.cpp`** -> AI Confidence: **99.48%**
166. **`src/apps/terminal/AppearPrefView.cpp`** -> AI Confidence: **99.48%**
167. **`src/apps/terminal/Colors.cpp`** -> AI Confidence: **99.48%**
168. **`src/apps/terminal/FindWindow.cpp`** -> AI Confidence: **99.48%**
169. **`src/apps/terminal/TermParse.cpp`** -> AI Confidence: **99.48%**
170. **`src/apps/terminal/TermView.cpp`** -> AI Confidence: **99.48%**
171. **`src/apps/text_search/GrepWindow.cpp`** -> AI Confidence: **99.48%**
172. **`src/apps/text_search/Grepper.cpp`** -> AI Confidence: **99.48%**
173. **`src/apps/webpositive/AuthenticationPanel.cpp`** -> AI Confidence: **99.48%**
174. **`src/apps/webpositive/BookmarkBar.cpp`** -> AI Confidence: **99.48%**
175. **`src/apps/webpositive/BrowserWindow.cpp`** -> AI Confidence: **99.48%**
176. **`src/apps/webpositive/ConsoleWindow.cpp`** -> AI Confidence: **99.48%**
177. **`src/apps/webpositive/SettingsWindow.cpp`** -> AI Confidence: **99.48%**
178. **`src/bin/badblocks.cpp`** -> AI Confidence: **99.48%**
179. **`src/bin/bfs_tools/bfsinfo.cpp`** -> AI Confidence: **99.48%**
180. **`src/bin/bfs_tools/lib/dump.cpp`** -> AI Confidence: **99.48%**
181. **`src/bin/copyattr.cpp`** -> AI Confidence: **99.48%**
182. **`src/bin/df.cpp`** -> AI Confidence: **99.48%**
183. **`src/bin/diskimage.cpp`** -> AI Confidence: **99.48%**
184. **`src/bin/fdinfo.cpp`** -> AI Confidence: **99.48%**
185. **`src/bin/findpaths.cpp`** -> AI Confidence: **99.48%**
186. **`src/bin/getarch.cpp`** -> AI Confidence: **99.48%**
187. **`src/bin/hey.cpp`** -> AI Confidence: **99.48%**
188. **`src/bin/installsound.cpp`** -> AI Confidence: **99.48%**
189. **`src/bin/keymap/Keymap.cpp`** -> AI Confidence: **99.48%**
190. **`src/bin/keymap/main.cpp`** -> AI Confidence: **99.48%**
191. **`src/bin/launch_roster.cpp`** -> AI Confidence: **99.48%**
192. **`src/bin/listattr.cpp`** -> AI Confidence: **99.48%**
193. **`src/bin/listdev/listdev.cpp`** -> AI Confidence: **99.48%**
194. **`src/bin/locale/collectcatkeys.cpp`** -> AI Confidence: **99.48%**
195. **`src/bin/locale/linkcatkeys.cpp`** -> AI Confidence: **99.48%**
196. **`src/bin/locale/locale.cpp`** -> AI Confidence: **99.48%**
197. **`src/bin/mail_utils/mail2mbox.cpp`** -> AI Confidence: **99.48%**
198. **`src/bin/mail_utils/mbox2mail.cpp`** -> AI Confidence: **99.48%**
199. **`src/bin/mail_utils/spamdbm.cpp`** -> AI Confidence: **99.48%**
200. **`src/bin/makebootable/platform/bios_ia32/makebootable.cpp`** -> AI Confidence: **99.48%**
201. **`src/bin/mimeset.cpp`** -> AI Confidence: **99.48%**
202. **`src/bin/mkindex.cpp`** -> AI Confidence: **99.48%**
203. **`src/bin/multiuser/groupadd.cpp`** -> AI Confidence: **99.48%**
204. **`src/bin/multiuser/su.cpp`** -> AI Confidence: **99.48%**
205. **`src/bin/network/netstat/netstat.cpp`** -> AI Confidence: **99.48%**
206. **`src/bin/network/route/route.cpp`** -> AI Confidence: **99.48%**
207. **`src/bin/open.cpp`** -> AI Confidence: **99.48%**
208. **`src/bin/resattr.cpp`** -> AI Confidence: **99.48%**
209. **`src/bin/screenmode/screenmode.cpp`** -> AI Confidence: **99.48%**
210. **`src/bin/setmime.cpp`** -> AI Confidence: **99.48%**
211. **`src/bin/shutdown.cpp`** -> AI Confidence: **99.48%**
212. **`src/bin/top.cpp`** -> AI Confidence: **99.48%**
213. **`src/kits/app/Roster.cpp`** -> AI Confidence: **99.48%**
214. **`src/kits/debugger/arch/Architecture.cpp`** -> AI Confidence: **99.48%**
215. **`src/kits/debugger/debug_managers/BreakpointManager.cpp`** -> AI Confidence: **99.48%**
216. **`src/kits/debugger/dwarf/DwarfExpressionEvaluator.cpp`** -> AI Confidence: **99.48%**
217. **`src/kits/debugger/jobs/ExpressionEvaluationJob.cpp`** -> AI Confidence: **99.48%**
218. **`src/kits/debugger/source_language/c_family/CLanguageExpressionEvaluator.cpp`** -> AI Confidence: **99.48%**
219. **`src/kits/interface/HaikuControlLook.cpp`** -> AI Confidence: **99.48%**
220. **`src/kits/interface/Window.cpp`** -> AI Confidence: **99.48%**
221. **`src/kits/mail/mail_util.cpp`** -> AI Confidence: **99.48%**
222. **`src/kits/network/libnetservices/FileRequest.cpp`** -> AI Confidence: **99.48%**
223. **`src/kits/package/PackageInfoParser.cpp`** -> AI Confidence: **99.48%**
224. **`src/kits/shared/StringForSize.cpp`** -> AI Confidence: **99.48%**
225. **`src/kits/storage/AppFileInfo.cpp`** -> AI Confidence: **99.48%**
226. **`src/kits/storage/NodeInfo.cpp`** -> AI Confidence: **99.48%**
227. **`src/kits/storage/mime/AppMetaMimeCreator.cpp`** -> AI Confidence: **99.48%**
228. **`src/kits/storage/sniffer/Parser.cpp`** -> AI Confidence: **99.48%**
229. **`src/kits/tracker/DirMenu.cpp`** -> AI Confidence: **99.48%**
230. **`src/kits/tracker/FilePanelPriv.cpp`** -> AI Confidence: **99.48%**
231. **`src/kits/tracker/LiveMenu.cpp`** -> AI Confidence: **99.48%**
232. **`src/kits/tracker/NavMenu.cpp`** -> AI Confidence: **99.48%**
233. **`src/kits/tracker/Navigator.cpp`** -> AI Confidence: **99.48%**
234. **`src/kits/tracker/PoseView.cpp`** -> AI Confidence: **99.48%**
235. **`src/kits/tracker/PoseViewScripting.cpp`** -> AI Confidence: **99.48%**
236. **`src/kits/tracker/TextWidget.cpp`** -> AI Confidence: **99.48%**
237. **`src/kits/tracker/TrashWatcher.cpp`** -> AI Confidence: **99.48%**
238. **`src/kits/tracker/infowindow/AttributesView.cpp`** -> AI Confidence: **99.48%**
239. **`src/kits/tracker/infowindow/FilePermissionsView.cpp`** -> AI Confidence: **99.48%**
240. **`src/kits/tracker/infowindow/GeneralInfoView.cpp`** -> AI Confidence: **99.48%**
241. **`src/kits/tracker/infowindow/InfoWindow.cpp`** -> AI Confidence: **99.48%**
242. **`src/libs/compat/freebsd_network/compat/sys/param.h`** -> AI Confidence: **99.48%**
243. **`src/libs/compat/freebsd_wlan/net80211/ieee80211_var.h`** -> AI Confidence: **99.48%**
244. **`src/libs/glut/glutInit.cpp`** -> AI Confidence: **99.48%**
245. **`src/libs/icon/IconUtils.cpp`** -> AI Confidence: **99.48%**
246. **`src/libs/print/libprint/DbgMsg.cpp`** -> AI Confidence: **99.48%**
247. **`src/libs/print/libprint/Halftone.cpp`** -> AI Confidence: **99.48%**
248. **`src/libs/print/libprint/JobData.cpp`** -> AI Confidence: **99.48%**
249. **`src/preferences/appearance/AppearanceWindow.cpp`** -> AI Confidence: **99.48%**
250. **`src/preferences/appearance/FontSelectionView.cpp`** -> AI Confidence: **99.48%**
251. **`src/preferences/backgrounds/BackgroundsView.cpp`** -> AI Confidence: **99.48%**
252. **`src/preferences/bluetooth/BluetoothSettingsView.cpp`** -> AI Confidence: **99.48%**
253. **`src/preferences/bluetooth/BluetoothWindow.cpp`** -> AI Confidence: **99.48%**
254. **`src/preferences/datatranslations/DataTranslationsWindow.cpp`** -> AI Confidence: **99.48%**
255. **`src/preferences/filetypes/ApplicationTypesWindow.cpp`** -> AI Confidence: **99.48%**
256. **`src/preferences/filetypes/AttributeWindow.cpp`** -> AI Confidence: **99.48%**
257. **`src/preferences/filetypes/FileTypeWindow.cpp`** -> AI Confidence: **99.48%**
258. **`src/preferences/filetypes/FileTypesWindow.cpp`** -> AI Confidence: **99.48%**
259. **`src/preferences/filetypes/IconView.cpp`** -> AI Confidence: **99.48%**
260. **`src/preferences/filetypes/NewFileTypeWindow.cpp`** -> AI Confidence: **99.48%**
261. **`src/preferences/filetypes/TypeListWindow.cpp`** -> AI Confidence: **99.48%**
262. **`src/preferences/input/Input.cpp`** -> AI Confidence: **99.48%**
263. **`src/preferences/input/InputKeyboard.cpp`** -> AI Confidence: **99.48%**
264. **`src/preferences/input/InputMouse.cpp`** -> AI Confidence: **99.48%**
265. **`src/preferences/input/InputTouchpadPrefView.cpp`** -> AI Confidence: **99.48%**
266. **`src/preferences/input/InputWindow.cpp`** -> AI Confidence: **99.48%**
267. **`src/preferences/locale/LocaleWindow.cpp`** -> AI Confidence: **99.48%**
268. **`src/preferences/mail/AutoConfigWindow.cpp`** -> AI Confidence: **99.48%**
269. **`src/preferences/network/InterfaceListItem.cpp`** -> AI Confidence: **99.48%**
270. **`src/preferences/network/InterfaceView.cpp`** -> AI Confidence: **99.48%**
271. **`src/preferences/repositories/RepositoriesView.cpp`** -> AI Confidence: **99.48%**
272. **`src/preferences/repositories/RepositoriesWindow.cpp`** -> AI Confidence: **99.48%**
273. **`src/preferences/screen/AlertWindow.cpp`** -> AI Confidence: **99.48%**
274. **`src/preferences/screen/RefreshWindow.cpp`** -> AI Confidence: **99.48%**
275. **`src/preferences/screen/ScreenWindow.cpp`** -> AI Confidence: **99.48%**
276. **`src/preferences/screensaver/PasswordWindow.cpp`** -> AI Confidence: **99.48%**
277. **`src/preferences/screensaver/ScreenCornerSelector.cpp`** -> AI Confidence: **99.48%**
278. **`src/preferences/shortcuts/ShortcutsSpec.cpp`** -> AI Confidence: **99.48%**
279. **`src/preferences/shortcuts/ShortcutsWindow.cpp`** -> AI Confidence: **99.48%**
280. **`src/preferences/sounds/HWindow.cpp`** -> AI Confidence: **99.48%**
281. **`src/preferences/sounds/SoundFilePanel.cpp`** -> AI Confidence: **99.48%**
282. **`src/preferences/time/ClockView.cpp`** -> AI Confidence: **99.48%**
283. **`src/preferences/time/TimeWindow.cpp`** -> AI Confidence: **99.48%**
284. **`src/servers/app/ServerApp.cpp`** -> AI Confidence: **99.48%**
285. **`src/servers/app/ServerWindow.cpp`** -> AI Confidence: **99.48%**
286. **`src/servers/app/decorator/DefaultDecorator.cpp`** -> AI Confidence: **99.48%**
287. **`src/servers/app/decorator/DefaultWindowBehaviour.cpp`** -> AI Confidence: **99.48%**
288. **`src/servers/app/decorator/TabDecorator.cpp`** -> AI Confidence: **99.48%**
289. **`src/servers/app/drawing/Painter/drawing_modes/PixelFormat.cpp`** -> AI Confidence: **99.48%**
290. **`src/servers/mail/DeskbarView.cpp`** -> AI Confidence: **99.48%**
291. **`src/servers/media/NotificationManager.cpp`** -> AI Confidence: **99.48%**
292. **`src/servers/notification/NotificationView.cpp`** -> AI Confidence: **99.48%**
293. **`src/servers/print/ConfigWindow.cpp`** -> AI Confidence: **99.48%**
294. **`src/servers/print/PrintServerApp.R5.cpp`** -> AI Confidence: **99.48%**
295. **`src/servers/print/PrintServerApp.Scripting.cpp`** -> AI Confidence: **99.48%**
296. **`src/servers/print/Printer.Scripting.cpp`** -> AI Confidence: **99.48%**
297. **`src/servers/print/Transport.Scripting.cpp`** -> AI Confidence: **99.48%**
298. **`src/servers/registrar/MIMEManager.cpp`** -> AI Confidence: **99.48%**
299. **`src/servers/registrar/MessageRunnerManager.cpp`** -> AI Confidence: **99.48%**
300. **`src/servers/registrar/Registrar.cpp`** -> AI Confidence: **99.48%**
301. **`src/servers/registrar/TRoster.cpp`** -> AI Confidence: **99.48%**
302. **`src/servers/registrar/mime/MimeUpdateThread.cpp`** -> AI Confidence: **99.48%**
303. **`src/servers/syslog_daemon/syslog_output.cpp`** -> AI Confidence: **99.48%**
304. **`src/system/boot/arch/arm/arch_cpu.cpp`** -> AI Confidence: **99.48%**
305. **`src/system/boot/loader/main.cpp`** -> AI Confidence: **99.48%**
306. **`src/system/boot/platform/efi/arch/arm64/arch_acpi.cpp`** -> AI Confidence: **99.48%**
307. **`src/system/boot/platform/efi/arch/x86_64/arch_mmu.cpp`** -> AI Confidence: **99.48%**
308. **`src/system/kernel/arch/riscv64/arch_smp.cpp`** -> AI Confidence: **99.48%**
309. **`src/system/kernel/arch/riscv64/arch_timer.cpp`** -> AI Confidence: **99.48%**
310. **`src/system/kernel/arch/x86/paging/64bit/X86VMTranslationMap64Bit.cpp`** -> AI Confidence: **99.48%**
311. **`src/system/kernel/vm/VMTranslationMap.cpp`** -> AI Confidence: **99.48%**
312. **`src/system/libroot/add-ons/icu/ICUTimeData.cpp`** -> AI Confidence: **99.48%**
313. **`src/system/libroot/os/find_directory.cpp`** -> AI Confidence: **99.48%**
314. **`src/system/libroot/os/parsedate.cpp`** -> AI Confidence: **99.48%**
315. **`src/system/libroot/posix/crypt/crypto_scrypt.cpp`** -> AI Confidence: **99.48%**
316. **`src/system/libroot/posix/sys/wait.cpp`** -> AI Confidence: **99.48%**
317. **`src/system/libroot/posix/wchar/wcsrtombs.cpp`** -> AI Confidence: **99.48%**
318. **`src/system/runtime_loader/elf_haiku_version.cpp`** -> AI Confidence: **99.48%**
319. **`src/system/runtime_loader/elf_load_image.cpp`** -> AI Confidence: **99.48%**
320. **`src/tests/add-ons/kernel/drivers/tty/posix_openpt_test.cpp`** -> AI Confidence: **99.48%**
321. **`src/tests/add-ons/kernel/file_systems/bfs/btree/test.cpp`** -> AI Confidence: **99.48%**
322. **`src/tests/add-ons/kernel/file_systems/bfs/dump_log/dump_log.cpp`** -> AI Confidence: **99.48%**
323. **`src/tests/add-ons/kernel/file_systems/shared/fragmenter.cpp`** -> AI Confidence: **99.48%**
324. **`src/tests/add-ons/print/ppd/ui/PrinterSelection.cpp`** -> AI Confidence: **99.48%**
325. **`src/tests/kits/device/stickit_BJoystick/StickItWindow.cpp`** -> AI Confidence: **99.48%**
326. **`src/tests/kits/game/chart/ChartWindow.cpp`** -> AI Confidence: **99.48%**
327. **`src/tests/kits/game/direct_window_test/StarWindow.cpp`** -> AI Confidence: **99.48%**
328. **`src/tests/kits/game/file_game_sound_test/FileSoundWindow.cpp`** -> AI Confidence: **99.48%**
329. **`src/tests/kits/interface/balert/alert_manual_test/AlertTestWindow.cpp`** -> AI Confidence: **99.48%**
330. **`src/tests/kits/interface/bbitmap/BBitmapTester.cpp`** -> AI Confidence: **99.48%**
331. **`src/tests/kits/interface/bshelf/ShelfInspector/InfoWindow.cpp`** -> AI Confidence: **99.48%**
332. **`src/tests/kits/interface/bwindowstack/WindowStackTest.cpp`** -> AI Confidence: **99.48%**
333. **`src/tests/kits/interface/flatten_picture/PictureTestWindow.cpp`** -> AI Confidence: **99.48%**
334. **`src/tests/kits/interface/menu/menuworld/ViewLayoutFactory.cpp`** -> AI Confidence: **99.48%**
335. **`src/tests/kits/locale/collatorTest.cpp`** -> AI Confidence: **99.48%**
336. **`src/tests/kits/mail/header_test.cpp`** -> AI Confidence: **99.48%**
337. **`src/tests/kits/media/nodetest/main.cpp`** -> AI Confidence: **99.48%**
338. **`src/tests/kits/net/NetEndpointTest.cpp`** -> AI Confidence: **99.48%**
339. **`src/tests/kits/net/link_echo.cpp`** -> AI Confidence: **99.48%**
340. **`src/tests/kits/net/service/UrlTest.cpp`** -> AI Confidence: **99.48%**
341. **`src/tests/kits/opengl/glinfo/InfoView.cpp`** -> AI Confidence: **99.48%**
342. **`src/tests/kits/storage/FindDirectoryTest.cpp`** -> AI Confidence: **99.48%**
343. **`src/tests/kits/storage/testapps/PathMonitorTest2.cpp`** -> AI Confidence: **99.48%**
344. **`src/tests/servers/input/msgspy/MsgSpy.cpp`** -> AI Confidence: **99.48%**
345. **`src/tests/system/boot/loader/platform_menu.cpp`** -> AI Confidence: **99.48%**
346. **`src/tests/system/kernel/disk_device_manager/DiskDeviceManagerTest.cpp`** -> AI Confidence: **99.48%**
347. **`src/tests/system/kernel/wait_for_objects_test.cpp`** -> AI Confidence: **99.48%**
348. **`src/tests/system/libroot/posix/fseek_test.cpp`** -> AI Confidence: **99.48%**
349. **`src/tests/system/libroot/posix/locale_test.cpp`** -> AI Confidence: **99.48%**
350. **`src/tests/system/libroot/posix/wcs_test.cpp`** -> AI Confidence: **99.48%**
351. **`src/tests/system/network/ipv46_client.cpp`** -> AI Confidence: **99.48%**
352. **`src/tests/system/network/ipv46_server.cpp`** -> AI Confidence: **99.48%**
353. **`src/tests/system/network/ipv6/multicast_sender.cpp`** -> AI Confidence: **99.48%**
354. **`src/tests/system/network/ipv6/raw_client.cpp`** -> AI Confidence: **99.48%**
355. **`src/tests/system/network/ipv6/tcp_udp_client.cpp`** -> AI Confidence: **99.48%**
356. **`src/tests/system/network/ipv6/tcp_udp_server.cpp`** -> AI Confidence: **99.48%**
357. **`src/tests/system/network/ipv6/udp_client.cpp`** -> AI Confidence: **99.48%**
358. **`src/tests/system/network/ipv6/udp_server.cpp`** -> AI Confidence: **99.48%**
359. **`src/tests/system/network/tcp_connection_test.cpp`** -> AI Confidence: **99.48%**
360. **`src/tools/create_image.cpp`** -> AI Confidence: **99.48%**
361. **`src/tools/data_to_source.cpp`** -> AI Confidence: **99.48%**
362. **`src/tools/get_package_dependencies/get_package_dependencies.cpp`** -> AI Confidence: **99.48%**
363. **`src/tools/locale/collectcatkeys.cpp`** -> AI Confidence: **99.48%**
364. **`src/tools/locale/linkcatkeys.cpp`** -> AI Confidence: **99.48%**
365. **`src/tools/remote_disk_server/remote_disk_server.cpp`** -> AI Confidence: **99.48%**
366. **`src/tools/restest/restest.cpp`** -> AI Confidence: **99.48%**
367. **`src/tools/translation/inspector/ImageWindow.cpp`** -> AI Confidence: **99.48%**
368. **`src/tools/translation/inspector/InspectorApp.cpp`** -> AI Confidence: **99.48%**
369. **`src/tools/translation/pnginfo/pnginfo.cpp`** -> AI Confidence: **99.48%**
370. **`src/tools/vmdkimage/vmdkimage.cpp`** -> AI Confidence: **99.48%**
371. **`src/add-ons/accelerants/et6x00/InitAccelerant.c`** -> AI Confidence: **99.48%**
372. **`src/add-ons/accelerants/matrox/acc_std.h`** -> AI Confidence: **99.48%**
373. **`src/add-ons/accelerants/neomagic/acc_std.h`** -> AI Confidence: **99.48%**
374. **`src/add-ons/accelerants/nvidia/acc_std.h`** -> AI Confidence: **99.48%**
375. **`src/add-ons/accelerants/radeon/dpms.c`** -> AI Confidence: **99.48%**
376. **`src/add-ons/accelerants/radeon/flat_panel.c`** -> AI Confidence: **99.48%**
377. **`src/add-ons/accelerants/radeon/monitor_routing.c`** -> AI Confidence: **99.48%**
378. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dsfield.c`** -> AI Confidence: **99.48%**
379. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dsmethod.c`** -> AI Confidence: **99.48%**
380. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dsobject.c`** -> AI Confidence: **99.48%**
381. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dsopcode.c`** -> AI Confidence: **99.48%**
382. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dspkginit.c`** -> AI Confidence: **99.48%**
383. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dsutils.c`** -> AI Confidence: **99.48%**
384. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dswexec.c`** -> AI Confidence: **99.48%**
385. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dswload.c`** -> AI Confidence: **99.48%**
386. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dswload2.c`** -> AI Confidence: **99.48%**
387. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exconfig.c`** -> AI Confidence: **99.48%**
388. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exoparg1.c`** -> AI Confidence: **99.48%**
389. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/namespace/nsparse.c`** -> AI Confidence: **99.48%**
390. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/parser/psargs.c`** -> AI Confidence: **99.48%**
391. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/parser/psloop.c`** -> AI Confidence: **99.48%**
392. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/parser/psparse.c`** -> AI Confidence: **99.48%**
393. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/parser/psxface.c`** -> AI Confidence: **99.48%**
394. **`src/add-ons/kernel/busses/scsi/usb/proto_common.c`** -> AI Confidence: **99.48%**
395. **`src/add-ons/kernel/busses/scsi/usb/transform_procs.c`** -> AI Confidence: **99.48%**
396. **`src/add-ons/kernel/drivers/graphics/radeon/CP_setup.c`** -> AI Confidence: **99.48%**
397. **`src/add-ons/kernel/drivers/graphics/radeon/bios.c`** -> AI Confidence: **99.48%**
398. **`src/add-ons/kernel/drivers/network/ether/3com/dev/xl/if_xl.c`** -> AI Confidence: **99.48%**
399. **`src/add-ons/kernel/drivers/network/ether/dec21xxx/dev/de/if_de.c`** -> AI Confidence: **99.48%**
400. **`src/add-ons/kernel/drivers/network/ether/pcnet/dev/mii/nsphyter.c`** -> AI Confidence: **99.48%**
401. **`src/add-ons/kernel/drivers/network/ether/sis900/dev/mii/icsphy.c`** -> AI Confidence: **99.48%**
402. **`src/add-ons/kernel/drivers/network/ether/sis900/dev/mii/nsphyter.c`** -> AI Confidence: **99.48%**
403. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/contrib/ath_hal/ar9300/ar9300_attach.c`** -> AI Confidence: **99.48%**
404. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar9002/ar9285_btcoex.c`** -> AI Confidence: **99.48%**
405. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar9002/ar9285_diversity.c`** -> AI Confidence: **99.48%**
406. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/if_ath_lna_div.c`** -> AI Confidence: **99.48%**
407. **`src/add-ons/kernel/drivers/network/wlan/realtekwifi/dev/rtwn/if_rtwn_fw.c`** -> AI Confidence: **99.48%**
408. **`src/add-ons/kernel/drivers/network/wlan/realtekwifi/dev/rtwn/rtl8812a/r12a_chan.c`** -> AI Confidence: **99.48%**
409. **`src/add-ons/kernel/file_systems/ntfs/libntfs/acls.c`** -> AI Confidence: **99.48%**
410. **`src/add-ons/kernel/file_systems/ntfs/libntfs/attrib.c`** -> AI Confidence: **99.48%**
411. **`src/add-ons/kernel/file_systems/ntfs/libntfs/bitmap.c`** -> AI Confidence: **99.48%**
412. **`src/add-ons/kernel/file_systems/ntfs/libntfs/bootsect.c`** -> AI Confidence: **99.48%**
413. **`src/add-ons/kernel/file_systems/ntfs/libntfs/compress.c`** -> AI Confidence: **99.48%**
414. **`src/add-ons/kernel/file_systems/ntfs/libntfs/dir.c`** -> AI Confidence: **99.48%**
415. **`src/add-ons/kernel/file_systems/ntfs/libntfs/ea.c`** -> AI Confidence: **99.48%**
416. **`src/add-ons/kernel/file_systems/ntfs/libntfs/efs.c`** -> AI Confidence: **99.48%**
417. **`src/add-ons/kernel/file_systems/ntfs/libntfs/inode.c`** -> AI Confidence: **99.48%**
418. **`src/add-ons/kernel/file_systems/ntfs/libntfs/lcnalloc.c`** -> AI Confidence: **99.48%**
419. **`src/add-ons/kernel/file_systems/ntfs/libntfs/mft.c`** -> AI Confidence: **99.48%**
420. **`src/add-ons/kernel/file_systems/ntfs/libntfs/reparse.c`** -> AI Confidence: **99.48%**
421. **`src/add-ons/kernel/file_systems/ntfs/libntfs/runlist.c`** -> AI Confidence: **99.48%**
422. **`src/add-ons/kernel/file_systems/ntfs/libntfs/unistr.c`** -> AI Confidence: **99.48%**
423. **`src/add-ons/kernel/file_systems/ntfs/libntfs/volume.c`** -> AI Confidence: **99.48%**
424. **`src/add-ons/kernel/file_systems/websearchfs/parse_duckduckgo_html.c`** -> AI Confidence: **99.48%**
425. **`src/bin/network/telnet/main.c`** -> AI Confidence: **99.48%**
426. **`src/bin/network/telnet/telnet.c`** -> AI Confidence: **99.48%**
427. **`src/bin/network/telnet/utilities.c`** -> AI Confidence: **99.48%**
428. **`src/bin/network/telnetd/utility.c`** -> AI Confidence: **99.48%**
429. **`src/bin/pcmcia-cs/cardctl.c`** -> AI Confidence: **99.48%**
430. **`src/bin/pcmcia-cs/dump_cis.c`** -> AI Confidence: **99.48%**
431. **`src/bin/pcmcia-cs/dump_cisreg.c`** -> AI Confidence: **99.48%**
432. **`src/bin/pcmcia-cs/pack_cis.c`** -> AI Confidence: **99.48%**
433. **`src/bin/watch.c`** -> AI Confidence: **99.48%**
434. **`src/libs/compat/freebsd_network/dev/mii/ukphy_subr.c`** -> AI Confidence: **99.48%**
435. **`src/libs/compat/freebsd_network/dev/usb/fbsd_usb_lookup.c`** -> AI Confidence: **99.48%**
436. **`src/libs/compat/freebsd_network/mbuf.c`** -> AI Confidence: **99.48%**
437. **`src/libs/compat/freebsd_wlan/net80211/ieee80211_sta.c`** -> AI Confidence: **99.48%**
438. **`src/libs/compat/openbsd_wlan/net80211/ieee80211_ioctl.c`** -> AI Confidence: **99.48%**
439. **`src/libs/iconv/iconv.c`** -> AI Confidence: **99.48%**
440. **`src/libs/iconv/localcharset.c`** -> AI Confidence: **99.48%**
441. **`src/libs/libsolv/ext/testcase.c`** -> AI Confidence: **99.48%**
442. **`src/libs/libsolv/solv/policy.c`** -> AI Confidence: **99.48%**
443. **`src/libs/libsolv/solv/poolarch.c`** -> AI Confidence: **99.48%**
444. **`src/libs/libsolv/solv/poolvendor.c`** -> AI Confidence: **99.48%**
445. **`src/libs/libsolv/solv/problems.c`** -> AI Confidence: **99.48%**
446. **`src/libs/libsolv/solv/repo_solv.c`** -> AI Confidence: **99.48%**
447. **`src/libs/libsolv/solv/repopage.c`** -> AI Confidence: **99.48%**
448. **`src/libs/libsolv/solv/rules.c`** -> AI Confidence: **99.48%**
449. **`src/libs/libsolv/solv/selection.c`** -> AI Confidence: **99.48%**
450. **`src/libs/libsolv/solv/solver.c`** -> AI Confidence: **99.48%**
451. **`src/libs/libsolv/solv/solverdebug.c`** -> AI Confidence: **99.48%**
452. **`src/libs/libsolv/solv/transaction.c`** -> AI Confidence: **99.48%**
453. **`src/libs/util/fparseln.c`** -> AI Confidence: **99.48%**
454. **`src/system/kernel/lib/strtod.c`** -> AI Confidence: **99.48%**
455. **`src/system/kernel/util/inet_ntop.c`** -> AI Confidence: **99.48%**
456. **`src/system/libnetwork/netresolv/inet/inet_cidr_pton.c`** -> AI Confidence: **99.48%**
457. **`src/system/libnetwork/netresolv/inet/inet_net_pton.c`** -> AI Confidence: **99.48%**
458. **`src/system/libnetwork/netresolv/inet/inet_neta.c`** -> AI Confidence: **99.48%**
459. **`src/system/libnetwork/netresolv/inet/nsap_addr.c`** -> AI Confidence: **99.48%**
460. **`src/system/libnetwork/netresolv/isc/assertions.c`** -> AI Confidence: **99.48%**
461. **`src/system/libnetwork/netresolv/nameser/ns_parse.c`** -> AI Confidence: **99.48%**
462. **`src/system/libnetwork/netresolv/nameser/ns_print.c`** -> AI Confidence: **99.48%**
463. **`src/system/libnetwork/netresolv/nameser/ns_ttl.c`** -> AI Confidence: **99.48%**
464. **`src/system/libnetwork/netresolv/resolv/res_query.c`** -> AI Confidence: **99.48%**
465. **`src/system/libroot/os/arch/sparc/fpu_explode.c`** -> AI Confidence: **99.48%**
466. **`src/system/libroot/posix/glibc/arch/generic/ldbl2mpn.c`** -> AI Confidence: **99.48%**
467. **`src/system/libroot/posix/glibc/arch/ppc/ldbl2mpn.c`** -> AI Confidence: **99.48%**
468. **`src/system/libroot/posix/glibc/extensions/getopt.c`** -> AI Confidence: **99.48%**
469. **`src/system/libroot/posix/glibc/iconv/gconv_simple.c`** -> AI Confidence: **99.48%**
470. **`src/system/libroot/posix/glibc/iconv/loop.c`** -> AI Confidence: **99.48%**
471. **`src/system/libroot/posix/glibc/libio/freopen.c`** -> AI Confidence: **99.48%**
472. **`src/system/libroot/posix/glibc/regex/regex.c`** -> AI Confidence: **99.48%**
473. **`src/system/libroot/posix/glibc/stdio-common/fxprintf.c`** -> AI Confidence: **99.48%**
474. **`src/system/libroot/posix/glibc/stdio-common/printf-parsemb.c`** -> AI Confidence: **99.48%**
475. **`src/system/libroot/posix/glibc/stdio-common/printf-prs.c`** -> AI Confidence: **99.48%**
476. **`src/system/libroot/posix/glibc/stdio-common/printf_fp.c`** -> AI Confidence: **99.48%**
477. **`src/system/libroot/posix/glibc/stdio-common/printf_fphex.c`** -> AI Confidence: **99.48%**
478. **`src/system/libroot/posix/glibc/stdio-common/vfprintf.c`** -> AI Confidence: **99.48%**
479. **`src/system/libroot/posix/glibc/stdio-common/vfscanf.c`** -> AI Confidence: **99.48%**
480. **`src/system/libroot/posix/glibc/stdlib/strtod.c`** -> AI Confidence: **99.48%**
481. **`src/system/libroot/posix/musl/time/strftime.c`** -> AI Confidence: **99.48%**
482. **`src/system/libroot/posix/musl/time/strptime.c`** -> AI Confidence: **99.48%**
483. **`src/system/libroot/posix/stdlib/strfmon.c`** -> AI Confidence: **99.48%**
484. **`src/system/libroot/posix/sys/uname.c`** -> AI Confidence: **99.48%**
485. **`src/tests/system/benchmarks/ctxbench.c`** -> AI Confidence: **99.48%**
486. **`src/tests/system/libroot/posix/tst-wprintf2.c`** -> AI Confidence: **99.48%**
487. **`src/tests/system/network/select_test2.c`** -> AI Confidence: **99.48%**
488. **`src/tests/system/network/select_test_big.c`** -> AI Confidence: **99.48%**
489. **`src/tests/system/network/test3.c`** -> AI Confidence: **99.48%**
490. **`src/bin/unzip/unzpriv.h`** -> AI Confidence: **99.44%**
491. **`src/system/libnetwork/netresolv/net/base64.c`** -> AI Confidence: **99.44%**
492. **`src/system/libroot/posix/glibc/stdlib/strtol.c`** -> AI Confidence: **99.44%**
493. **`headers/posix/fenv.h`** -> AI Confidence: **99.43%**
494. **`headers/private/fs_shell/fssh_api_wrapper.h`** -> AI Confidence: **99.42%**
495. **`src/add-ons/kernel/file_systems/ntfs/libntfs/endians.h`** -> AI Confidence: **99.42%**
496. **`src/add-ons/accelerants/intel_extreme/FlexibleDisplayInterface.cpp`** -> AI Confidence: **99.39%**
497. **`src/add-ons/accelerants/intel_extreme/Ports.cpp`** -> AI Confidence: **99.39%**
498. **`src/add-ons/accelerants/intel_extreme/mode.cpp`** -> AI Confidence: **99.39%**
499. **`src/add-ons/accelerants/intel_extreme/overlay.cpp`** -> AI Confidence: **99.39%**
500. **`src/add-ons/accelerants/radeon_hd/displayport.cpp`** -> AI Confidence: **99.39%**
501. **`src/add-ons/decorators/MacDecorator/MacDecorator.cpp`** -> AI Confidence: **99.39%**
502. **`src/add-ons/decorators/WinDecorator/WinDecorator.cpp`** -> AI Confidence: **99.39%**
503. **`src/add-ons/input_server/devices/easypen/EasyPenInputDevice.cpp`** -> AI Confidence: **99.39%**
504. **`src/add-ons/input_server/devices/keyboard/KeyboardInputDevice.cpp`** -> AI Confidence: **99.39%**
505. **`src/add-ons/input_server/devices/keyboard/Keymap.cpp`** -> AI Confidence: **99.39%**
506. **`src/add-ons/input_server/devices/keyboard/TeamMonitorWindow.cpp`** -> AI Confidence: **99.39%**
507. **`src/add-ons/input_server/devices/virtio/VirtioInputDevice.cpp`** -> AI Confidence: **99.39%**
508. **`src/add-ons/input_server/filters/padblocker/PadBlocker.cpp`** -> AI Confidence: **99.39%**
509. **`src/add-ons/input_server/filters/screen_saver/ScreenSaverFilter.cpp`** -> AI Confidence: **99.39%**
510. **`src/add-ons/input_server/filters/shortcut_catcher/ParseCommandLine.cpp`** -> AI Confidence: **99.39%**
511. **`src/add-ons/input_server/filters/shortcut_catcher/ShortcutsServerFilter.cpp`** -> AI Confidence: **99.39%**
512. **`src/add-ons/input_server/methods/pen/PenInputInkWindow.cpp`** -> AI Confidence: **99.39%**
513. **`src/add-ons/kernel/bus_managers/ps2/ps2_dev.cpp`** -> AI Confidence: **99.39%**
514. **`src/add-ons/kernel/bus_managers/usb/PhysicalMemoryAllocator.cpp`** -> AI Confidence: **99.39%**
515. **`src/add-ons/kernel/busses/scsi/ahci/ahci_controller.cpp`** -> AI Confidence: **99.39%**
516. **`src/add-ons/kernel/busses/scsi/ahci/ahci_port.cpp`** -> AI Confidence: **99.39%**
517. **`src/add-ons/kernel/debugger/disasm/x86/disasm_arch.cpp`** -> AI Confidence: **99.39%**
518. **`src/add-ons/kernel/drivers/bluetooth/h2/h2generic/h2generic.cpp`** -> AI Confidence: **99.39%**
519. **`src/add-ons/kernel/drivers/bus/usb/usb_raw.cpp`** -> AI Confidence: **99.39%**
520. **`src/add-ons/kernel/drivers/graphics/radeon_hd/radeon_hd.cpp`** -> AI Confidence: **99.39%**
521. **`src/add-ons/kernel/drivers/input/hid_shared/HIDReport.cpp`** -> AI Confidence: **99.39%**
522. **`src/add-ons/kernel/drivers/input/hid_shared/JoystickProtocolHandler.cpp`** -> AI Confidence: **99.39%**
523. **`src/add-ons/kernel/drivers/input/hid_shared/MouseProtocolHandler.cpp`** -> AI Confidence: **99.39%**
524. **`src/add-ons/kernel/drivers/input/usb_hid/HIDDevice.cpp`** -> AI Confidence: **99.39%**
525. **`src/add-ons/kernel/file_systems/cdda/cdda.cpp`** -> AI Confidence: **99.39%**
526. **`src/add-ons/kernel/file_systems/fat/kernel_interface.cpp`** -> AI Confidence: **99.39%**
527. **`src/add-ons/kernel/file_systems/fat/support.cpp`** -> AI Confidence: **99.39%**
528. **`src/add-ons/kernel/file_systems/iso9660/iso9660.cpp`** -> AI Confidence: **99.39%**
529. **`src/add-ons/kernel/file_systems/netfs/authentication_server/AuthenticationPanel.cpp`** -> AI Confidence: **99.39%**
530. **`src/add-ons/kernel/file_systems/netfs/server/ClientConnection.cpp`** -> AI Confidence: **99.39%**
531. **`src/add-ons/kernel/file_systems/netfs/server/NetFSServer.cpp`** -> AI Confidence: **99.39%**
532. **`src/add-ons/kernel/file_systems/packagefs/volume/Volume.cpp`** -> AI Confidence: **99.39%**
533. **`src/add-ons/kernel/file_systems/ramfs/Node.cpp`** -> AI Confidence: **99.39%**
534. **`src/add-ons/kernel/file_systems/reiserfs/Tree.cpp`** -> AI Confidence: **99.39%**
535. **`src/add-ons/kernel/file_systems/userlandfs/private/RequestAllocator.cpp`** -> AI Confidence: **99.39%**
536. **`src/add-ons/kernel/generic/scsi_periph/io.cpp`** -> AI Confidence: **99.39%**
537. **`src/add-ons/kernel/network/ppp/shared/libkernelppp/KPPPStateMachine.cpp`** -> AI Confidence: **99.39%**
538. **`src/add-ons/kernel/network/protocols/unix/UnixEndpoint.cpp`** -> AI Confidence: **99.39%**
539. **`src/add-ons/kernel/network/protocols/unix/UnixFifo.cpp`** -> AI Confidence: **99.39%**
540. **`src/add-ons/kernel/partitioning_systems/atari/atari.cpp`** -> AI Confidence: **99.39%**
541. **`src/add-ons/media/media-add-ons/demultiplexer/MediaOutputInfo.cpp`** -> AI Confidence: **99.39%**
542. **`src/add-ons/media/media-add-ons/mixer/MixerCore.cpp`** -> AI Confidence: **99.39%**
543. **`src/add-ons/media/media-add-ons/mixer/MixerUtils.cpp`** -> AI Confidence: **99.39%**
544. **`src/add-ons/media/media-add-ons/opensound/OpenSoundAddOn.cpp`** -> AI Confidence: **99.39%**
545. **`src/add-ons/media/media-add-ons/opensound/OpenSoundNode.cpp`** -> AI Confidence: **99.39%**
546. **`src/add-ons/media/media-add-ons/tone_producer_demo/ToneProducer.cpp`** -> AI Confidence: **99.39%**
547. **`src/add-ons/media/media-add-ons/video_producer_demo/Producer.cpp`** -> AI Confidence: **99.39%**
548. **`src/add-ons/media/plugins/dvd_streamer/DVDMediaIO.cpp`** -> AI Confidence: **99.39%**
549. **`src/add-ons/media/plugins/ffmpeg/AVFormatReader.cpp`** -> AI Confidence: **99.39%**
550. **`src/add-ons/network_settings/dialup/DialUpView.cpp`** -> AI Confidence: **99.39%**
551. **`src/add-ons/network_settings/dialup/PPPoEAddon.cpp`** -> AI Confidence: **99.39%**
552. **`src/add-ons/network_settings/dnsclient/DNSSettingsView.cpp`** -> AI Confidence: **99.39%**
553. **`src/add-ons/print/drivers/postscript/PS.cpp`** -> AI Confidence: **99.39%**
554. **`src/add-ons/print/drivers/postscript/SelectPPDDlg.cpp`** -> AI Confidence: **99.39%**
555. **`src/add-ons/print/transports/ipp/IppTransport.cpp`** -> AI Confidence: **99.39%**
556. **`src/add-ons/screen_savers/glife/GLifeConfig.cpp`** -> AI Confidence: **99.39%**
557. **`src/add-ons/screen_savers/glife/GLifeView.cpp`** -> AI Confidence: **99.39%**
558. **`src/add-ons/screen_savers/ifs/IFSSaver.cpp`** -> AI Confidence: **99.39%**
559. **`src/add-ons/tracker/label_as/LabelAs.cpp`** -> AI Confidence: **99.39%**
560. **`src/add-ons/tracker/mark_as/MarkAsRead.cpp`** -> AI Confidence: **99.39%**
561. **`src/add-ons/tracker/opentargetfolder/opentargetfolder.cpp`** -> AI Confidence: **99.39%**
562. **`src/add-ons/translators/bmp/BMPTranslator.cpp`** -> AI Confidence: **99.39%**
563. **`src/add-ons/translators/gif/GIFLoad.cpp`** -> AI Confidence: **99.39%**
564. **`src/add-ons/translators/jpeg/JPEGTranslator.cpp`** -> AI Confidence: **99.39%**
565. **`src/add-ons/translators/jpeg/exif_parser.cpp`** -> AI Confidence: **99.39%**
566. **`src/add-ons/translators/psd/ConfigView.cpp`** -> AI Confidence: **99.39%**
567. **`src/add-ons/translators/sgi/SGIImage.cpp`** -> AI Confidence: **99.39%**
568. **`src/add-ons/translators/webp/ConfigView.cpp`** -> AI Confidence: **99.39%**
569. **`src/apps/activitymonitor/ActivityWindow.cpp`** -> AI Confidence: **99.39%**
570. **`src/apps/activitymonitor/SystemInfoHandler.cpp`** -> AI Confidence: **99.39%**
571. **`src/apps/autoraise/AutoRaiseIcon.cpp`** -> AI Confidence: **99.39%**
572. **`src/apps/bootmanager/BootManagerController.cpp`** -> AI Confidence: **99.39%**
573. **`src/apps/bootmanager/BootManagerWindow.cpp`** -> AI Confidence: **99.39%**
574. **`src/apps/bootmanager/DrivesPage.cpp`** -> AI Confidence: **99.39%**
575. **`src/apps/charactermap/CharacterWindow.cpp`** -> AI Confidence: **99.39%**
576. **`src/apps/clock/cl_view.cpp`** -> AI Confidence: **99.39%**
577. **`src/apps/clock/cl_wind.cpp`** -> AI Confidence: **99.39%**
578. **`src/apps/codycam/VideoConsumer.cpp`** -> AI Confidence: **99.39%**
579. **`src/apps/cortex/DiagramView/DiagramBox.cpp`** -> AI Confidence: **99.39%**
580. **`src/apps/cortex/DiagramView/DiagramEndPoint.cpp`** -> AI Confidence: **99.39%**
581. **`src/apps/cortex/DormantNodeView/DormantNodeView.cpp`** -> AI Confidence: **99.39%**
582. **`src/apps/cortex/DormantNodeView/DormantNodeWindow.cpp`** -> AI Confidence: **99.39%**
583. **`src/apps/cortex/MediaRoutingView/MediaJack.cpp`** -> AI Confidence: **99.39%**
584. **`src/apps/cortex/RouteApp/RouteWindow.cpp`** -> AI Confidence: **99.39%**
585. **`src/apps/cortex/RouteApp/StatusView.cpp`** -> AI Confidence: **99.39%**
586. **`src/apps/cortex/ValControl/NumericValControl.cpp`** -> AI Confidence: **99.39%**
587. **`src/apps/cortex/ValControl/ValControl.cpp`** -> AI Confidence: **99.39%**
588. **`src/apps/cortex/addons/LoggingConsumer/NodeHarnessWin.cpp`** -> AI Confidence: **99.39%**
589. **`src/apps/debuganalyzer/gui/chart/LegendChartAxis.cpp`** -> AI Confidence: **99.39%**
590. **`src/apps/debugger/Debugger.cpp`** -> AI Confidence: **99.39%**
591. **`src/apps/debugger/user_interface/cli/commands/CliDebugReportCommand.cpp`** -> AI Confidence: **99.39%**
592. **`src/apps/debugger/user_interface/cli/commands/CliDumpStringCommand.cpp`** -> AI Confidence: **99.39%**
593. **`src/apps/debugger/user_interface/cli/commands/CliPrintVariableCommand.cpp`** -> AI Confidence: **99.39%**
594. **`src/apps/debugger/user_interface/cli/commands/CliWriteCoreFileCommand.cpp`** -> AI Confidence: **99.39%**
595. **`src/apps/debugger/user_interface/gui/connection_config/config_handlers/NetworkConnectionConfigView.cpp`** -> AI Confidence: **99.39%**
596. **`src/apps/debugger/user_interface/gui/team_settings_window/ImageStopConfigView.cpp`** -> AI Confidence: **99.39%**
597. **`src/apps/debugger/user_interface/gui/team_window/BreakpointsView.cpp`** -> AI Confidence: **99.39%**
598. **`src/apps/debugger/user_interface/gui/team_window/SourceView.cpp`** -> AI Confidence: **99.39%**
599. **`src/apps/debugger/user_interface/gui/team_window/TeamWindow.cpp`** -> AI Confidence: **99.39%**
600. **`src/apps/debugger/user_interface/gui/teams_window/TeamsListView.cpp`** -> AI Confidence: **99.39%**
601. **`src/apps/debugger/user_interface/gui/utility_windows/BreakpointEditWindow.cpp`** -> AI Confidence: **99.39%**
602. **`src/apps/debugger/user_interface/gui/utility_windows/StartTeamWindow.cpp`** -> AI Confidence: **99.39%**
603. **`src/apps/deskbar/BarView.cpp`** -> AI Confidence: **99.39%**
604. **`src/apps/deskbar/BarWindow.cpp`** -> AI Confidence: **99.39%**
605. **`src/apps/deskbar/ExpandoMenuBar.cpp`** -> AI Confidence: **99.39%**
606. **`src/apps/deskbar/StatusView.cpp`** -> AI Confidence: **99.39%**
607. **`src/apps/deskbar/TeamMenu.cpp`** -> AI Confidence: **99.39%**
608. **`src/apps/deskbar/TeamMenuItem.cpp`** -> AI Confidence: **99.39%**
609. **`src/apps/diskusage/PieView.cpp`** -> AI Confidence: **99.39%**
610. **`src/apps/diskusage/Snapshot.cpp`** -> AI Confidence: **99.39%**
611. **`src/apps/drivesetup/AbstractParametersPanel.cpp`** -> AI Confidence: **99.39%**
612. **`src/apps/drivesetup/ChangeParametersPanel.cpp`** -> AI Confidence: **99.39%**
613. **`src/apps/drivesetup/MainWindow.cpp`** -> AI Confidence: **99.39%**
614. **`src/apps/drivesetup/PartitionList.cpp`** -> AI Confidence: **99.39%**
615. **`src/apps/expander/ExpanderRules.cpp`** -> AI Confidence: **99.39%**
616. **`src/apps/haikudepot/server/UserDetailVerifierProcess.cpp`** -> AI Confidence: **99.39%**
617. **`src/apps/haikudepot/tar/TarArchiveService.cpp`** -> AI Confidence: **99.39%**
618. **`src/apps/haikudepot/ui/App.cpp`** -> AI Confidence: **99.39%**
619. **`src/apps/haikudepot/ui/ScreenshotWindow.cpp`** -> AI Confidence: **99.39%**
620. **`src/apps/haikudepot/ui/UserLoginWindow.cpp`** -> AI Confidence: **99.39%**
621. **`src/apps/haikudepot/ui/UserUsageConditionsWindow.cpp`** -> AI Confidence: **99.39%**
622. **`src/apps/haikudepot/util/StorageUtils.cpp`** -> AI Confidence: **99.39%**
623. **`src/apps/icon-o-matic/MainWindow.cpp`** -> AI Confidence: **99.39%**
624. **`src/apps/icon-o-matic/generic/gui/ListViews.cpp`** -> AI Confidence: **99.39%**
625. **`src/apps/icon-o-matic/generic/gui/panel/color_picker/ColorField.cpp`** -> AI Confidence: **99.39%**
626. **`src/apps/icon-o-matic/generic/gui/scrollview/ScrollView.cpp`** -> AI Confidence: **99.39%**
627. **`src/apps/icon-o-matic/generic/property/view/PropertyListView.cpp`** -> AI Confidence: **99.39%**
628. **`src/apps/icon-o-matic/generic/property/view/specific_properties/OptionValueView.cpp`** -> AI Confidence: **99.39%**
629. **`src/apps/icon-o-matic/gui/ShapeListView.cpp`** -> AI Confidence: **99.39%**
630. **`src/apps/icon-o-matic/gui/StyleView.cpp`** -> AI Confidence: **99.39%**
631. **`src/apps/icon-o-matic/shape/commands/RemovePointsCommand.cpp`** -> AI Confidence: **99.39%**
632. **`src/apps/icon-o-matic/shape/commands/SplitPointsCommand.cpp`** -> AI Confidence: **99.39%**
633. **`src/apps/icon-o-matic/transformable/TransformShapesBox.cpp`** -> AI Confidence: **99.39%**
634. **`src/apps/installer/InstallerApp.cpp`** -> AI Confidence: **99.39%**
635. **`src/apps/launchbox/App.cpp`** -> AI Confidence: **99.39%**
636. **`src/apps/launchbox/PadView.cpp`** -> AI Confidence: **99.39%**
637. **`src/apps/login/LoginApp.cpp`** -> AI Confidence: **99.39%**
638. **`src/apps/magnify/Magnify.cpp`** -> AI Confidence: **99.39%**
639. **`src/apps/mail/MailApp.cpp`** -> AI Confidence: **99.39%**
640. **`src/apps/mail/Utilities.cpp`** -> AI Confidence: **99.39%**
641. **`src/apps/mediaconverter/MediaConverterWindow.cpp`** -> AI Confidence: **99.39%**
642. **`src/apps/mediaplayer/InfoWin.cpp`** -> AI Confidence: **99.39%**
643. **`src/apps/mediaplayer/NetworkStreamWin.cpp`** -> AI Confidence: **99.39%**
644. **`src/apps/mediaplayer/VideoView.cpp`** -> AI Confidence: **99.39%**
645. **`src/apps/mediaplayer/media_node_framework/NodeManager.cpp`** -> AI Confidence: **99.39%**
646. **`src/apps/mediaplayer/media_node_framework/audio/AudioProducer.cpp`** -> AI Confidence: **99.39%**
647. **`src/apps/mediaplayer/media_node_framework/video/VideoConsumer.cpp`** -> AI Confidence: **99.39%**
648. **`src/apps/mediaplayer/media_node_framework/video/VideoProducer.cpp`** -> AI Confidence: **99.39%**
649. **`src/apps/mediaplayer/playlist/PlaylistWindow.cpp`** -> AI Confidence: **99.39%**
650. **`src/apps/mediaplayer/settings/SettingsWindow.cpp`** -> AI Confidence: **99.39%**
651. **`src/apps/mediaplayer/support/CommandStack.cpp`** -> AI Confidence: **99.39%**
652. **`src/apps/networkstatus/NetworkStatusView.cpp`** -> AI Confidence: **99.39%**
653. **`src/apps/overlayimage/OverlayView.cpp`** -> AI Confidence: **99.39%**
654. **`src/apps/packageinstaller/PackageItem.cpp`** -> AI Confidence: **99.39%**
655. **`src/apps/people/AttributeTextControl.cpp`** -> AI Confidence: **99.39%**
656. **`src/apps/people/PersonView.cpp`** -> AI Confidence: **99.39%**
657. **`src/apps/poorman/PoorManAdvancedView.cpp`** -> AI Confidence: **99.39%**
658. **`src/apps/poorman/PoorManWindow.cpp`** -> AI Confidence: **99.39%**
659. **`src/apps/processcontroller/AutoIcon.cpp`** -> AI Confidence: **99.39%**
660. **`src/apps/processcontroller/PCWorld.cpp`** -> AI Confidence: **99.39%**
661. **`src/apps/processcontroller/Preferences.cpp`** -> AI Confidence: **99.39%**
662. **`src/apps/processcontroller/Utilities.cpp`** -> AI Confidence: **99.39%**
663. **`src/apps/pulse/DeskbarPulseView.cpp`** -> AI Confidence: **99.39%**
664. **`src/apps/pulse/PrefsWindow.cpp`** -> AI Confidence: **99.39%**
665. **`src/apps/resedit/ResView.cpp`** -> AI Confidence: **99.39%**
666. **`src/apps/screenshot/ScreenshotWindow.cpp`** -> AI Confidence: **99.39%**
667. **`src/apps/serialconnect/SerialApp.cpp`** -> AI Confidence: **99.39%**
668. **`src/apps/showimage/ShowImageApp.cpp`** -> AI Confidence: **99.39%**
669. **`src/apps/showimage/ShowImageView.cpp`** -> AI Confidence: **99.39%**
670. **`src/apps/showimage/ShowImageWindow.cpp`** -> AI Confidence: **99.39%**
671. **`src/apps/softwareupdater/UpdateManager.cpp`** -> AI Confidence: **99.39%**
672. **`src/apps/stylededit/FindWindow.cpp`** -> AI Confidence: **99.39%**
673. **`src/apps/stylededit/ReplaceWindow.cpp`** -> AI Confidence: **99.39%**
674. **`src/apps/stylededit/StatusView.cpp`** -> AI Confidence: **99.39%**
675. **`src/apps/stylededit/StyledEditApp.cpp`** -> AI Confidence: **99.39%**
676. **`src/apps/sudoku/SudokuWindow.cpp`** -> AI Confidence: **99.39%**
677. **`src/apps/terminal/TermViewStates.cpp`** -> AI Confidence: **99.39%**
678. **`src/apps/terminal/TermWindow.cpp`** -> AI Confidence: **99.39%**
679. **`src/apps/terminal/TerminalRoster.cpp`** -> AI Confidence: **99.39%**
680. **`src/apps/terminal/ThemeWindow.cpp`** -> AI Confidence: **99.39%**
681. **`src/apps/tv/MainWin.cpp`** -> AI Confidence: **99.39%**
682. **`src/apps/webpositive/DownloadProgressView.cpp`** -> AI Confidence: **99.39%**
683. **`src/apps/webpositive/DownloadWindow.cpp`** -> AI Confidence: **99.39%**
684. **`src/bin/acpi_call/acpi_call.cpp`** -> AI Confidence: **99.39%**
685. **`src/bin/addattr/addAttr.cpp`** -> AI Confidence: **99.39%**
686. **`src/bin/addattr/main.cpp`** -> AI Confidence: **99.39%**
687. **`src/bin/catattr.cpp`** -> AI Confidence: **99.39%**
688. **`src/bin/desklink/DeskButton.cpp`** -> AI Confidence: **99.39%**
689. **`src/bin/desklink/desklink.cpp`** -> AI Confidence: **99.39%**
690. **`src/bin/filepanel.cpp`** -> AI Confidence: **99.39%**
691. **`src/bin/i2c/i2c.cpp`** -> AI Confidence: **99.39%**
692. **`src/bin/listusb/listusb.cpp`** -> AI Confidence: **99.39%**
693. **`src/bin/network/arp/arp.cpp`** -> AI Confidence: **99.39%**
694. **`src/bin/network/ppp_up/ConnectionView.cpp`** -> AI Confidence: **99.39%**
695. **`src/bin/package/PackageWritingUtils.cpp`** -> AI Confidence: **99.39%**
696. **`src/bin/package/command_add.cpp`** -> AI Confidence: **99.39%**
697. **`src/bin/pkgman/PackageManager.cpp`** -> AI Confidence: **99.39%**
698. **`src/bin/query/query.cpp`** -> AI Confidence: **99.39%**
699. **`src/bin/ramdisk.cpp`** -> AI Confidence: **99.39%**
700. **`src/bin/rc/decompile.cpp`** -> AI Confidence: **99.39%**
701. **`src/bin/screen_blanker/ScreenBlanker.cpp`** -> AI Confidence: **99.39%**
702. **`src/bin/setarch.cpp`** -> AI Confidence: **99.39%**
703. **`src/kits/app/Application.cpp`** -> AI Confidence: **99.39%**
704. **`src/kits/app/PropertyInfo.cpp`** -> AI Confidence: **99.39%**
705. **`src/kits/bluetooth/DiscoveryListener.cpp`** -> AI Confidence: **99.39%**
706. **`src/kits/debugger/controllers/DebugReportGenerator.cpp`** -> AI Confidence: **99.39%**
707. **`src/kits/debugger/controllers/TeamDebugger.cpp`** -> AI Confidence: **99.39%**
708. **`src/kits/debugger/dwarf/DwarfFile.cpp`** -> AI Confidence: **99.39%**
709. **`src/kits/debugger/user_interface/util/UiUtils.cpp`** -> AI Confidence: **99.39%**
710. **`src/kits/debugger/value/ValueWriter.cpp`** -> AI Confidence: **99.39%**
711. **`src/kits/debugger/value/value_nodes/EnumerationValueNode.cpp`** -> AI Confidence: **99.39%**
712. **`src/kits/device/JoystickTweaker.cpp`** -> AI Confidence: **99.39%**
713. **`src/kits/interface/Bitmap.cpp`** -> AI Confidence: **99.39%**
714. **`src/kits/interface/ColorControl.cpp`** -> AI Confidence: **99.39%**
715. **`src/kits/interface/Gradient.cpp`** -> AI Confidence: **99.39%**
716. **`src/kits/interface/ListView.cpp`** -> AI Confidence: **99.39%**
717. **`src/kits/interface/ScrollBar.cpp`** -> AI Confidence: **99.39%**
718. **`src/kits/interface/TextView.cpp`** -> AI Confidence: **99.39%**
719. **`src/kits/mail/MailContainer.cpp`** -> AI Confidence: **99.39%**
720. **`src/kits/mail/ProtocolConfigView.cpp`** -> AI Confidence: **99.39%**
721. **`src/kits/media/MediaDefs.cpp`** -> AI Confidence: **99.39%**
722. **`src/kits/media/SharedBufferList.cpp`** -> AI Confidence: **99.39%**
723. **`src/kits/network/libnetservices/GopherRequest.cpp`** -> AI Confidence: **99.39%**
724. **`src/kits/network/libnetservices/UrlProtocolAsynchronousListener.cpp`** -> AI Confidence: **99.39%**
725. **`src/kits/package/hpkg/ReaderImplBase.cpp`** -> AI Confidence: **99.39%**
726. **`src/kits/package/hpkg/v1/ReaderImplBaseV1.cpp`** -> AI Confidence: **99.39%**
727. **`src/kits/package/manager/PackageManager.cpp`** -> AI Confidence: **99.39%**
728. **`src/kits/print/Jobs.cpp`** -> AI Confidence: **99.39%**
729. **`src/kits/screensaver/ScreenSaverSettings.cpp`** -> AI Confidence: **99.39%**
730. **`src/kits/shared/ExpressionParser.cpp`** -> AI Confidence: **99.39%**
731. **`src/kits/storage/AddOnMonitorHandler.cpp`** -> AI Confidence: **99.39%**
732. **`src/kits/storage/Mime.cpp`** -> AI Confidence: **99.39%**
733. **`src/kits/storage/MimeType.cpp`** -> AI Confidence: **99.39%**
734. **`src/kits/storage/ResourceFile.cpp`** -> AI Confidence: **99.39%**
735. **`src/kits/storage/mime/AssociatedTypes.cpp`** -> AI Confidence: **99.39%**
736. **`src/kits/storage/mime/MimeInfoUpdater.cpp`** -> AI Confidence: **99.39%**
737. **`src/kits/storage/mime/database_support.cpp`** -> AI Confidence: **99.39%**
738. **`src/kits/storage/storage_support.cpp`** -> AI Confidence: **99.39%**
739. **`src/kits/tracker/AutoMounterSettings.cpp`** -> AI Confidence: **99.39%**
740. **`src/kits/tracker/BackgroundImage.cpp`** -> AI Confidence: **99.39%**
741. **`src/kits/tracker/ContainerWindow.cpp`** -> AI Confidence: **99.39%**
742. **`src/kits/tracker/FSUtils.cpp`** -> AI Confidence: **99.39%**
743. **`src/kits/tracker/FindPanel.cpp`** -> AI Confidence: **99.39%**
744. **`src/kits/tracker/Model.cpp`** -> AI Confidence: **99.39%**
745. **`src/kits/tracker/NodePreloader.cpp`** -> AI Confidence: **99.39%**
746. **`src/kits/tracker/Pose.cpp`** -> AI Confidence: **99.39%**
747. **`src/kits/tracker/SettingsViews.cpp`** -> AI Confidence: **99.39%**
748. **`src/kits/tracker/StatusWindow.cpp`** -> AI Confidence: **99.39%**
749. **`src/kits/tracker/WidgetAttributeText.cpp`** -> AI Confidence: **99.39%**
750. **`src/kits/tracker/infowindow/HeaderView.cpp`** -> AI Confidence: **99.39%**
751. **`src/libs/icon/message/MessageImporter.cpp`** -> AI Confidence: **99.39%**
752. **`src/libs/print/libprint/GraphicsDriver.cpp`** -> AI Confidence: **99.39%**
753. **`src/libs/print/libprint/PageSetupDlg.cpp`** -> AI Confidence: **99.39%**
754. **`src/libs/print/libprint/Preview.cpp`** -> AI Confidence: **99.39%**
755. **`src/libs/print/libprint/StatusWindow.cpp`** -> AI Confidence: **99.39%**
756. **`src/preferences/appearance/ColorsView.cpp`** -> AI Confidence: **99.39%**
757. **`src/preferences/appearance/FontView.cpp`** -> AI Confidence: **99.39%**
758. **`src/preferences/appearance/LookAndFeelSettingsView.cpp`** -> AI Confidence: **99.39%**
759. **`src/preferences/backgrounds/BackgroundImage.cpp`** -> AI Confidence: **99.39%**
760. **`src/preferences/backgrounds/ImageFilePanel.cpp`** -> AI Confidence: **99.39%**
761. **`src/preferences/bluetooth/ExtendedLocalDeviceView.cpp`** -> AI Confidence: **99.39%**
762. **`src/preferences/bluetooth/InquiryPanel.cpp`** -> AI Confidence: **99.39%**
763. **`src/preferences/bluetooth/RemoteDevicesView.cpp`** -> AI Confidence: **99.39%**
764. **`src/preferences/filetypes/ApplicationTypeWindow.cpp`** -> AI Confidence: **99.39%**
765. **`src/preferences/filetypes/PreferredAppMenu.cpp`** -> AI Confidence: **99.39%**
766. **`src/preferences/joysticks/JoyWin.cpp`** -> AI Confidence: **99.39%**
767. **`src/preferences/keymap/KeyboardLayoutView.cpp`** -> AI Confidence: **99.39%**
768. **`src/preferences/keymap/Keymap.cpp`** -> AI Confidence: **99.39%**
769. **`src/preferences/keymap/ModifierKeysWindow.cpp`** -> AI Confidence: **99.39%**
770. **`src/preferences/locale/FormatSettingsView.cpp`** -> AI Confidence: **99.39%**
771. **`src/preferences/locale/LanguageListView.cpp`** -> AI Confidence: **99.39%**
772. **`src/preferences/mail/AutoConfigView.cpp`** -> AI Confidence: **99.39%**
773. **`src/preferences/mail/ConfigWindow.cpp`** -> AI Confidence: **99.39%**
774. **`src/preferences/mail/FilterConfigView.cpp`** -> AI Confidence: **99.39%**
775. **`src/preferences/network/InterfaceAddressView.cpp`** -> AI Confidence: **99.39%**
776. **`src/preferences/network/NetworkWindow.cpp`** -> AI Confidence: **99.39%**
777. **`src/preferences/notifications/PrefletWin.cpp`** -> AI Confidence: **99.39%**
778. **`src/preferences/printers/AddPrinterDialog.cpp`** -> AI Confidence: **99.39%**
779. **`src/preferences/printers/JobListView.cpp`** -> AI Confidence: **99.39%**
780. **`src/preferences/printers/PrintersWindow.cpp`** -> AI Confidence: **99.39%**
781. **`src/preferences/repositories/TaskLooper.cpp`** -> AI Confidence: **99.39%**
782. **`src/preferences/screen/RefreshSlider.cpp`** -> AI Confidence: **99.39%**
783. **`src/preferences/time/Time.cpp`** -> AI Confidence: **99.39%**
784. **`src/preferences/time/ZoneView.cpp`** -> AI Confidence: **99.39%**
785. **`src/preferences/virtualmemory/SettingsWindow.cpp`** -> AI Confidence: **99.39%**
786. **`src/servers/app/AppServer.cpp`** -> AI Confidence: **99.39%**
787. **`src/servers/app/Desktop.cpp`** -> AI Confidence: **99.39%**
788. **`src/servers/app/DirectWindowInfo.cpp`** -> AI Confidence: **99.39%**
789. **`src/servers/app/WorkspacesView.cpp`** -> AI Confidence: **99.39%**
790. **`src/servers/app/drawing/HWInterface.cpp`** -> AI Confidence: **99.39%**
791. **`src/servers/app/drawing/Painter/AGGTextRenderer.cpp`** -> AI Confidence: **99.39%**
792. **`src/servers/app/drawing/Painter/bitmap_painter/BitmapPainter.cpp`** -> AI Confidence: **99.39%**
793. **`src/servers/app/font/FontCacheEntry.cpp`** -> AI Confidence: **99.39%**
794. **`src/servers/keystore/AppAccessRequestWindow.cpp`** -> AI Confidence: **99.39%**
795. **`src/servers/mail/MailDaemonApplication.cpp`** -> AI Confidence: **99.39%**
796. **`src/servers/midi/MidiServerApp.cpp`** -> AI Confidence: **99.39%**
797. **`src/servers/net/AutoconfigLooper.cpp`** -> AI Confidence: **99.39%**
798. **`src/servers/net/DHCPClient.cpp`** -> AI Confidence: **99.39%**
799. **`src/servers/net/NetServer.cpp`** -> AI Confidence: **99.39%**
800. **`src/servers/notification/AppGroupView.cpp`** -> AI Confidence: **99.39%**
801. **`src/servers/notification/NotificationWindow.cpp`** -> AI Confidence: **99.39%**
802. **`src/servers/package/CommitTransactionHandler.cpp`** -> AI Confidence: **99.39%**
803. **`src/servers/package/PackageDaemon.cpp`** -> AI Confidence: **99.39%**
804. **`src/servers/package/Volume.cpp`** -> AI Confidence: **99.39%**
805. **`src/servers/print/PrintServerApp.cpp`** -> AI Confidence: **99.39%**
806. **`src/servers/registrar/AuthenticationManager.cpp`** -> AI Confidence: **99.39%**
807. **`src/servers/registrar/ShutdownProcess.cpp`** -> AI Confidence: **99.39%**
808. **`src/system/boot/loader/file_systems/fat/Stream.cpp`** -> AI Confidence: **99.39%**
809. **`src/system/boot/loader/file_systems/fat/Volume.cpp`** -> AI Confidence: **99.39%**
810. **`src/system/boot/platform/efi/acpi.cpp`** -> AI Confidence: **99.39%**
811. **`src/system/boot/platform/efi/arch/arm64/arch_mmu.cpp`** -> AI Confidence: **99.39%**
812. **`src/system/boot/platform/efi/arch/riscv64/arch_mmu.cpp`** -> AI Confidence: **99.39%**
813. **`src/system/boot/platform/efi/dtb.cpp`** -> AI Confidence: **99.39%**
814. **`src/system/boot/platform/generic/video_splash.cpp`** -> AI Confidence: **99.39%**
815. **`src/system/boot/platform/riscv/fdt.cpp`** -> AI Confidence: **99.39%**
816. **`src/system/kernel/arch/arm/arch_debug.cpp`** -> AI Confidence: **99.39%**
817. **`src/system/kernel/arch/arm/paging/32bit/ARMVMTranslationMap32Bit.cpp`** -> AI Confidence: **99.39%**
818. **`src/system/kernel/arch/arm64/arch_debug.cpp`** -> AI Confidence: **99.39%**
819. **`src/system/kernel/arch/m68k/paging/040/M68KVMTranslationMap040.cpp`** -> AI Confidence: **99.39%**
820. **`src/system/kernel/arch/ppc/paging/460/PPCVMTranslationMap460.cpp`** -> AI Confidence: **99.39%**
821. **`src/system/kernel/arch/ppc/paging/classic/PPCVMTranslationMapClassic.cpp`** -> AI Confidence: **99.39%**
822. **`src/system/kernel/arch/x86/arch_cpu.cpp`** -> AI Confidence: **99.39%**
823. **`src/system/kernel/arch/x86/arch_debug.cpp`** -> AI Confidence: **99.39%**
824. **`src/system/kernel/arch/x86/arch_int.cpp`** -> AI Confidence: **99.39%**
825. **`src/system/kernel/arch/x86/arch_system_info.cpp`** -> AI Confidence: **99.39%**
826. **`src/system/kernel/arch/x86/arch_vm.cpp`** -> AI Confidence: **99.39%**
827. **`src/system/kernel/arch/x86/paging/32bit/X86VMTranslationMap32Bit.cpp`** -> AI Confidence: **99.39%**
828. **`src/system/kernel/arch/x86/paging/pae/X86VMTranslationMapPAE.cpp`** -> AI Confidence: **99.39%**
829. **`src/system/kernel/interrupts.cpp`** -> AI Confidence: **99.39%**
830. **`src/system/kernel/low_resource_manager.cpp`** -> AI Confidence: **99.39%**
831. **`src/system/kernel/signal.cpp`** -> AI Confidence: **99.39%**
832. **`src/system/kernel/vm/vm_debug.cpp`** -> AI Confidence: **99.39%**
833. **`src/system/kernel/vm/vm_page.cpp`** -> AI Confidence: **99.39%**
834. **`src/system/libroot/add-ons/icu/ICUCtypeData.cpp`** -> AI Confidence: **99.39%**
835. **`src/system/libroot/posix/locale/LocaleInternal.cpp`** -> AI Confidence: **99.39%**
836. **`src/system/libroot/posix/sys/xsi_sem.cpp`** -> AI Confidence: **99.39%**
837. **`src/system/libroot/posix/time/clock_support.cpp`** -> AI Confidence: **99.39%**
838. **`src/system/runtime_loader/elf_symbol_lookup.cpp`** -> AI Confidence: **99.39%**
839. **`src/system/runtime_loader/runtime_loader.cpp`** -> AI Confidence: **99.39%**
840. **`src/tests/add-ons/kernel/drivers/audio/multi_audio_test.cpp`** -> AI Confidence: **99.39%**
841. **`src/tests/add-ons/kernel/drivers/random/random_test.cpp`** -> AI Confidence: **99.39%**
842. **`src/tests/add-ons/kernel/file_systems/bfs/bfs_attribute_iterator_test.cpp`** -> AI Confidence: **99.39%**
843. **`src/tests/add-ons/kernel/file_systems/shared/random_file_actions.cpp`** -> AI Confidence: **99.39%**
844. **`src/tests/add-ons/print/transports/main.cpp`** -> AI Confidence: **99.39%**
845. **`src/tests/apps/fake_app_server/AppServer.cpp`** -> AI Confidence: **99.39%**
846. **`src/tests/apps/fake_app_server/ServerApp.cpp`** -> AI Confidence: **99.39%**
847. **`src/tests/apps/miniterminal/MiniView.cpp`** -> AI Confidence: **99.39%**
848. **`src/tests/apps/partitioner/Partitioner.cpp`** -> AI Confidence: **99.39%**
849. **`src/tests/kits/game/ParticlesII/particlesII.cpp`** -> AI Confidence: **99.39%**
850. **`src/tests/kits/game/push_game_sound_test/push_game_sound_test.cpp`** -> AI Confidence: **99.39%**
851. **`src/tests/kits/game/simple_game_sound_test/SimpleSoundTest.cpp`** -> AI Confidence: **99.39%**
852. **`src/tests/kits/interface/menu/menuworld/TestMenuBuilder.cpp`** -> AI Confidence: **99.39%**
853. **`src/tests/kits/locale/ICUTest.cpp`** -> AI Confidence: **99.39%**
854. **`src/tests/kits/media/mp3_reader_test/main.cpp`** -> AI Confidence: **99.39%**
855. **`src/tests/kits/media/wav_reader_test/main.cpp`** -> AI Confidence: **99.39%**
856. **`src/tests/kits/midi/synth_file_reader/SynthFileReader.cpp`** -> AI Confidence: **99.39%**
857. **`src/tests/kits/opengl/glinfo/ExtensionsView.cpp`** -> AI Confidence: **99.39%**
858. **`src/tests/kits/storage/MimeTypeTest.cpp`** -> AI Confidence: **99.39%**
859. **`src/tests/kits/storage/disk_device/DiskDeviceTest.cpp`** -> AI Confidence: **99.39%**
860. **`src/tests/kits/storage/virtualdrive/mkvirtualdrive.cpp`** -> AI Confidence: **99.39%**
861. **`src/tests/kits/support/compression_test.cpp`** -> AI Confidence: **99.39%**
862. **`src/tests/kits/translation/multitest/WorkView.cpp`** -> AI Confidence: **99.39%**
863. **`src/tests/servers/app/look_and_feel/LookAndFeel.cpp`** -> AI Confidence: **99.39%**
864. **`src/tests/servers/app/newClipping/MyView.cpp`** -> AI Confidence: **99.39%**
865. **`src/tests/servers/app/newerClipping/ClientLooper.cpp`** -> AI Confidence: **99.39%**
866. **`src/tests/servers/app/newerClipping/WindowLayer.cpp`** -> AI Confidence: **99.39%**
867. **`src/tests/servers/app/playground/ObjectView.cpp`** -> AI Confidence: **99.39%**
868. **`src/tests/servers/app/text_rendering/renderer.cpp`** -> AI Confidence: **99.39%**
869. **`src/tests/servers/registrar/run_test_registrar.cpp`** -> AI Confidence: **99.39%**
870. **`src/tests/system/kernel/file_corruption/fs/BlockAllocator.cpp`** -> AI Confidence: **99.39%**
871. **`src/tests/system/kernel/file_corruption/fs/File.cpp`** -> AI Confidence: **99.39%**
872. **`src/tests/system/kernel/live_query.cpp`** -> AI Confidence: **99.39%**
873. **`src/tests/system/kernel/spinlock_contention.cpp`** -> AI Confidence: **99.39%**
874. **`src/tests/system/kernel/vm/page_fault_cache_merge_test.cpp`** -> AI Confidence: **99.39%**
875. **`src/tests/system/libroot/posix/realtime_sem_test1.cpp`** -> AI Confidence: **99.39%**
876. **`src/tests/system/network/firefox_crash.cpp`** -> AI Confidence: **99.39%**
877. **`src/tests/system/network/ipv6/raw_server.cpp`** -> AI Confidence: **99.39%**
878. **`src/tools/anyboot/anyboot.cpp`** -> AI Confidence: **99.39%**
879. **`src/tools/generate_attribute_stores.cpp`** -> AI Confidence: **99.39%**
880. **`src/tools/generate_boot_screen.cpp`** -> AI Confidence: **99.39%**
881. **`src/tools/mbrtool/mbrtool.cpp`** -> AI Confidence: **99.39%**
882. **`src/tools/opd_to_package_info/opd_to_package_info.cpp`** -> AI Confidence: **99.39%**
883. **`src/tools/restest/ResourceFile.cpp`** -> AI Confidence: **99.39%**
884. **`src/tools/translation/bmpinfo/bmpinfo.cpp`** -> AI Confidence: **99.39%**
885. **`src/tools/translation/tgainfo/tgainfo.cpp`** -> AI Confidence: **99.39%**
886. **`src/tools/update_package_requires/update_package_requires.cpp`** -> AI Confidence: **99.39%**
887. **`headers/libs/zydis/Zydis/Internal/String.h`** -> AI Confidence: **99.39%**
888. **`src/add-ons/accelerants/radeon/SetDisplayMode.c`** -> AI Confidence: **99.39%**
889. **`src/add-ons/accelerants/radeon/monitor_detection.c`** -> AI Confidence: **99.39%**
890. **`src/add-ons/kernel/busses/scsi/53c8xx/53c8xx.c`** -> AI Confidence: **99.39%**
891. **`src/add-ons/kernel/busses/scsi/usb/usb_scsi.c`** -> AI Confidence: **99.39%**
892. **`src/add-ons/kernel/drivers/audio/emuxki/emuxki.c`** -> AI Confidence: **99.39%**
893. **`src/add-ons/kernel/drivers/bus/pcmcia/ds.c`** -> AI Confidence: **99.39%**
894. **`src/add-ons/kernel/drivers/network/ether/dec21xxx/dev/dc/dcphy.c`** -> AI Confidence: **99.39%**
895. **`src/add-ons/kernel/drivers/network/ether/dec21xxx/dev/dc/if_dc.c`** -> AI Confidence: **99.39%**
896. **`src/add-ons/kernel/drivers/network/ether/pcnet/dev/mii/nsphy.c`** -> AI Confidence: **99.39%**
897. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/contrib/ath_hal/ar9300/ar9300_eeprom.c`** -> AI Confidence: **99.39%**
898. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/contrib/ath_hal/ar9300/ar9300_reset.c`** -> AI Confidence: **99.39%**
899. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar5212/ar5212_ani.c`** -> AI Confidence: **99.39%**
900. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar5212/ar5212_attach.c`** -> AI Confidence: **99.39%**
901. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar5212/ar5212_reset.c`** -> AI Confidence: **99.39%**
902. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar5312/ar5312_attach.c`** -> AI Confidence: **99.39%**
903. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar5312/ar5312_reset.c`** -> AI Confidence: **99.39%**
904. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar5416/ar5416_radar.c`** -> AI Confidence: **99.39%**
905. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar9002/ar9280_attach.c`** -> AI Confidence: **99.39%**
906. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar9002/ar9285_reset.c`** -> AI Confidence: **99.39%**
907. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/if_ath_btcoex_mci.c`** -> AI Confidence: **99.39%**
908. **`src/add-ons/kernel/drivers/network/wlan/realtekwifi/dev/rtwn/rtl8192c/pci/r92ce_calib.c`** -> AI Confidence: **99.39%**
909. **`src/add-ons/kernel/drivers/network/wlan/realtekwifi/dev/rtwn/rtl8192c/r92c_calib.c`** -> AI Confidence: **99.39%**
910. **`src/add-ons/kernel/drivers/network/wlan/realtekwifi/dev/rtwn/rtl8821a/r21a_rx.c`** -> AI Confidence: **99.39%**
911. **`src/add-ons/kernel/file_systems/ntfs/libntfs/attrlist.c`** -> AI Confidence: **99.39%**
912. **`src/add-ons/kernel/file_systems/ntfs/libntfs/logfile.c`** -> AI Confidence: **99.39%**
913. **`src/add-ons/kernel/file_systems/ntfs/libntfs/logging.c`** -> AI Confidence: **99.39%**
914. **`src/add-ons/kernel/file_systems/ntfs/libntfs/object_id.c`** -> AI Confidence: **99.39%**
915. **`src/add-ons/kernel/file_systems/ntfs/libntfs/security.c`** -> AI Confidence: **99.39%**
916. **`src/add-ons/kernel/file_systems/ntfs/libntfs/xattrs.c`** -> AI Confidence: **99.39%**
917. **`src/add-ons/kernel/file_systems/ntfs/utils/mkntfs.c`** -> AI Confidence: **99.39%**
918. **`src/add-ons/kernel/file_systems/ntfs/utils/utils.c`** -> AI Confidence: **99.39%**
919. **`src/add-ons/kernel/file_systems/userlandfs/server/beos/fs_cache.c`** -> AI Confidence: **99.39%**
920. **`src/add-ons/kernel/partitioning_systems/session/Debug.h`** -> AI Confidence: **99.39%**
921. **`src/bin/fwcontrol/eui64.c`** -> AI Confidence: **99.39%**
922. **`src/bin/fwcontrol/fwdv.c`** -> AI Confidence: **99.39%**
923. **`src/bin/listimage.c`** -> AI Confidence: **99.39%**
924. **`src/bin/network/ftpd/ftpd.c`** -> AI Confidence: **99.39%**
925. **`src/bin/network/ftpd/popen.c`** -> AI Confidence: **99.39%**
926. **`src/bin/network/ping/ping.c`** -> AI Confidence: **99.39%**
927. **`src/bin/network/ping/ping6.c`** -> AI Confidence: **99.39%**
928. **`src/bin/network/telnet/sys_bsd.c`** -> AI Confidence: **99.39%**
929. **`src/bin/network/telnet/terminal.c`** -> AI Confidence: **99.39%**
930. **`src/bin/network/telnetd/telnetd.c`** -> AI Confidence: **99.39%**
931. **`src/bin/network/traceroute/traceroute.c`** -> AI Confidence: **99.39%**
932. **`src/bin/unzip/beos.c`** -> AI Confidence: **99.39%**
933. **`src/libs/bsd/unvis.c`** -> AI Confidence: **99.39%**
934. **`src/libs/compat/freebsd_wlan/net80211/ieee80211_action.c`** -> AI Confidence: **99.39%**
935. **`src/libs/compat/freebsd_wlan/net80211/ieee80211_adhoc.c`** -> AI Confidence: **99.39%**
936. **`src/libs/compat/freebsd_wlan/net80211/ieee80211_ioctl.c`** -> AI Confidence: **99.39%**
937. **`src/libs/compat/openbsd_wlan/net80211/ieee80211_pae_input.c`** -> AI Confidence: **99.39%**
938. **`src/libs/compat/openbsd_wlan/net80211/ieee80211_proto.c`** -> AI Confidence: **99.39%**
939. **`src/libs/libsolv/solv/pool.c`** -> AI Confidence: **99.39%**
940. **`src/libs/libsolv/solv/repo.c`** -> AI Confidence: **99.39%**
941. **`src/libs/libsolv/solv/repo_write.c`** -> AI Confidence: **99.39%**
942. **`src/libs/libsolv/solv/sha2.c`** -> AI Confidence: **99.39%**
943. **`src/libs/libtelnet/kerberos.c`** -> AI Confidence: **99.39%**
944. **`src/libs/libtelnet/kerberos5.c`** -> AI Confidence: **99.39%**
945. **`src/libs/uuid/gen_uuid.c`** -> AI Confidence: **99.39%**
946. **`src/system/libnetwork/netresolv/inet/inet_cidr_ntop.c`** -> AI Confidence: **99.39%**
947. **`src/system/libnetwork/netresolv/inet/inet_net_ntop.c`** -> AI Confidence: **99.39%**
948. **`src/system/libnetwork/netresolv/nameser/ns_samedomain.c`** -> AI Confidence: **99.39%**
949. **`src/system/libnetwork/netresolv/net/gethnamaddr.c`** -> AI Confidence: **99.39%**
950. **`src/system/libnetwork/netresolv/resolv/res_debug.c`** -> AI Confidence: **99.39%**
951. **`src/system/libroot/posix/glibc/libio/fileops.c`** -> AI Confidence: **99.39%**
952. **`src/system/libroot/posix/glibc/libio/wfileops.c`** -> AI Confidence: **99.39%**
953. **`src/system/libroot/posix/musl/misc/nftw.c`** -> AI Confidence: **99.39%**
954. **`src/tests/system/network/at_client.c`** -> AI Confidence: **99.39%**
955. **`src/add-ons/accelerants/intel_extreme/accelerant.cpp`** -> AI Confidence: **99.35%**
956. **`src/add-ons/kernel/file_systems/ramfs/kernel_interface.cpp`** -> AI Confidence: **99.35%**
957. **`src/add-ons/mail_daemon/inbound_filters/spam_filter/SpamFilterConfig.cpp`** -> AI Confidence: **99.35%**
958. **`src/add-ons/mail_daemon/outbound_protocols/smtp/SMTP.cpp`** -> AI Confidence: **99.35%**
959. **`src/add-ons/tracker/zipomatic/ZipperThread.cpp`** -> AI Confidence: **99.35%**
960. **`src/add-ons/translators/rtf/main.cpp`** -> AI Confidence: **99.35%**
961. **`src/add-ons/translators/tiff/TIFFView.cpp`** -> AI Confidence: **99.35%**
962. **`src/apps/debugger/user_interface/gui/inspector_window/InspectorWindow.cpp`** -> AI Confidence: **99.35%**
963. **`src/apps/debugger/user_interface/gui/utility_windows/SignalDispositionEditWindow.cpp`** -> AI Confidence: **99.35%**
964. **`src/apps/deskcalc/CalcWindow.cpp`** -> AI Confidence: **99.35%**
965. **`src/apps/diskprobe/DiskProbe.cpp`** -> AI Confidence: **99.35%**
966. **`src/apps/mediaplayer/playlist/PlaylistListView.cpp`** -> AI Confidence: **99.35%**
967. **`src/apps/packageinstaller/main.cpp`** -> AI Confidence: **99.35%**
968. **`src/apps/terminal/BasicTerminalBuffer.cpp`** -> AI Confidence: **99.35%**
969. **`src/apps/terminal/ThemeView.cpp`** -> AI Confidence: **99.35%**
970. **`src/apps/webpositive/BrowserApp.cpp`** -> AI Confidence: **99.35%**
971. **`src/bin/desklink/VolumeControl.cpp`** -> AI Confidence: **99.35%**
972. **`src/bin/network/ifconfig/ifconfig.cpp`** -> AI Confidence: **99.35%**
973. **`src/bin/pkgman/command_add_repo.cpp`** -> AI Confidence: **99.35%**
974. **`src/kits/shared/IconButton.cpp`** -> AI Confidence: **99.35%**
975. **`src/kits/storage/mime/InstalledTypes.cpp`** -> AI Confidence: **99.35%**
976. **`src/kits/tracker/DeskWindow.cpp`** -> AI Confidence: **99.35%**
977. **`src/kits/tracker/MountMenu.cpp`** -> AI Confidence: **99.35%**
978. **`src/kits/tracker/TitleView.cpp`** -> AI Confidence: **99.35%**
979. **`src/preferences/media/MidiSettingsView.cpp`** -> AI Confidence: **99.35%**
980. **`src/servers/app/BitmapManager.cpp`** -> AI Confidence: **99.35%**
981. **`src/servers/bluetooth/BluetoothServer.cpp`** -> AI Confidence: **99.35%**
982. **`src/servers/keystore/KeyStoreServer.cpp`** -> AI Confidence: **99.35%**
983. **`src/servers/registrar/RecentApps.cpp`** -> AI Confidence: **99.35%**
984. **`src/system/kernel/arch/riscv64/arch_debug.cpp`** -> AI Confidence: **99.35%**
985. **`src/tests/kits/interface/menu/menuworld/MenuView.cpp`** -> AI Confidence: **99.35%**
986. **`src/tests/servers/app/playground/ObjectWindow.cpp`** -> AI Confidence: **99.35%**
987. **`src/add-ons/kernel/drivers/network/ether/3com/dev/mii/bmtphy.c`** -> AI Confidence: **99.35%**
988. **`src/add-ons/kernel/drivers/network/ether/broadcom440x/dev/mii/bmtphy.c`** -> AI Confidence: **99.35%**
989. **`src/add-ons/kernel/drivers/network/ether/marvell_yukon/dev/msk/if_msk.c`** -> AI Confidence: **99.35%**
990. **`src/add-ons/kernel/drivers/network/ether/nforce/dev/mii/ciphy.c`** -> AI Confidence: **99.35%**
991. **`src/add-ons/kernel/drivers/network/ether/via_rhine/dev/mii/ciphy.c`** -> AI Confidence: **99.35%**
992. **`src/add-ons/kernel/drivers/network/ether/vt612x/dev/mii/ciphy.c`** -> AI Confidence: **99.35%**
993. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar9002/ar9287_reset.c`** -> AI Confidence: **99.35%**
994. **`src/add-ons/kernel/drivers/network/wlan/realtekwifi/dev/rtwn/usb/rtwn_usb_ep.c`** -> AI Confidence: **99.35%**
995. **`src/bin/unzip/ttyio.c`** -> AI Confidence: **99.35%**
996. **`src/libs/bsd/fts.c`** -> AI Confidence: **99.35%**
997. **`src/libs/libsolv/solv/repodata.c`** -> AI Confidence: **99.35%**
998. **`src/system/libnetwork/netresolv/resolv/res_mkquery.c`** -> AI Confidence: **99.35%**
999. **`src/system/libroot/os/arch/sparc/fpu_implode.c`** -> AI Confidence: **99.35%**
1000. **`src/system/libroot/posix/glob.c`** -> AI Confidence: **99.35%**
1001. **`src/tests/system/network/multicast/multisend.c`** -> AI Confidence: **99.35%**
1002. **`src/tools/generate_build_packages_repo.py`** -> AI Confidence: **99.34%**
1003. **`src/add-ons/kernel/bus_managers/acpi/acpica/include/platform/acenvex.h`** -> AI Confidence: **99.34%**
1004. **`src/add-ons/kernel/busses/i2c/pch/pch_i2c.cpp`** -> AI Confidence: **99.34%**
1005. **`src/add-ons/kernel/debugger/qrencode/module.cpp`** -> AI Confidence: **99.34%**
1006. **`src/add-ons/kernel/drivers/audio/echo/generic/CGina24DspCommObject.cpp`** -> AI Confidence: **99.34%**
1007. **`src/add-ons/kernel/drivers/audio/ice1712/multi.cpp`** -> AI Confidence: **99.34%**
1008. **`src/add-ons/kernel/drivers/audio/usb/AudioControlInterface.cpp`** -> AI Confidence: **99.34%**
1009. **`src/add-ons/kernel/file_systems/bfs/Debug.cpp`** -> AI Confidence: **99.34%**
1010. **`src/add-ons/kernel/file_systems/udf/Volume.cpp`** -> AI Confidence: **99.34%**
1011. **`src/add-ons/kernel/file_systems/userlandfs/kernel_add_on/kernel_interface.cpp`** -> AI Confidence: **99.34%**
1012. **`src/add-ons/mail_daemon/inbound_filters/match_header/StringMatcher.cpp`** -> AI Confidence: **99.34%**
1013. **`src/add-ons/media/media-add-ons/radeon/Radeon.cpp`** -> AI Confidence: **99.34%**
1014. **`src/add-ons/media/media-add-ons/radeon/Theater100.cpp`** -> AI Confidence: **99.34%**
1015. **`src/add-ons/media/media-add-ons/usb_webcam/addons/uvc/UVCCamDevice.cpp`** -> AI Confidence: **99.34%**
1016. **`src/add-ons/media/plugins/ape_reader/MAClib/APECompressCore.cpp`** -> AI Confidence: **99.34%**
1017. **`src/add-ons/media/plugins/ffmpeg/AVCodecEncoder.cpp`** -> AI Confidence: **99.34%**
1018. **`src/add-ons/network_settings/dialup/InterfaceUtils.cpp`** -> AI Confidence: **99.34%**
1019. **`src/add-ons/print/transports/shared/Socket.cpp`** -> AI Confidence: **99.34%**
1020. **`src/add-ons/screen_savers/gravity/RainbowItem.cpp`** -> AI Confidence: **99.34%**
1021. **`src/add-ons/screen_savers/icons/IconsSaver.cpp`** -> AI Confidence: **99.34%**
1022. **`src/add-ons/translators/pcx/PCX.cpp`** -> AI Confidence: **99.34%**
1023. **`src/add-ons/translators/shared/TranslatorSettings.cpp`** -> AI Confidence: **99.34%**
1024. **`src/add-ons/translators/tga/TGATranslator.cpp`** -> AI Confidence: **99.34%**
1025. **`src/add-ons/translators/tga/TGAView.cpp`** -> AI Confidence: **99.34%**
1026. **`src/add-ons/translators/wonderbrush/support/bitmap_compression.cpp`** -> AI Confidence: **99.34%**
1027. **`src/apps/codycam/FtpClient.cpp`** -> AI Confidence: **99.34%**
1028. **`src/apps/cortex/InfoView/EndPointInfoView.cpp`** -> AI Confidence: **99.34%**
1029. **`src/apps/cortex/RouteApp/ConnectionIO.cpp`** -> AI Confidence: **99.34%**
1030. **`src/apps/debuganalyzer/gui/chart/BigtimeChartAxisLegendSource.cpp`** -> AI Confidence: **99.34%**
1031. **`src/apps/debuganalyzer/gui/chart/NanotimeChartAxisLegendSource.cpp`** -> AI Confidence: **99.34%**
1032. **`src/apps/debugger/user_interface/gui/util/SignalDispositionMenu.cpp`** -> AI Confidence: **99.34%**
1033. **`src/apps/devices/DeviceACPI.cpp`** -> AI Confidence: **99.34%**
1034. **`src/apps/expander/ExpanderSettings.cpp`** -> AI Confidence: **99.34%**
1035. **`src/apps/glteapot/GLObject.cpp`** -> AI Confidence: **99.34%**
1036. **`src/apps/haikudepot/server/PopulatePkgUserRatingsFromServerProcess.cpp`** -> AI Confidence: **99.34%**
1037. **`src/apps/icon-o-matic/generic/gui/panel/color_picker/AlphaSlider.cpp`** -> AI Confidence: **99.34%**
1038. **`src/apps/icon-o-matic/generic/property/CommonPropertyIDs.cpp`** -> AI Confidence: **99.34%**
1039. **`src/apps/patchbay/EndpointInfo.cpp`** -> AI Confidence: **99.34%**
1040. **`src/apps/processcontroller/NoiseBarMenuItem.cpp`** -> AI Confidence: **99.34%**
1041. **`src/apps/processcontroller/ThreadBarMenuItem.cpp`** -> AI Confidence: **99.34%**
1042. **`src/apps/resedit/NumberEditors.cpp`** -> AI Confidence: **99.34%**
1043. **`src/apps/serialconnect/XModem.cpp`** -> AI Confidence: **99.34%**
1044. **`src/apps/switcher/Switcher.cpp`** -> AI Confidence: **99.34%**
1045. **`src/apps/terminal/Arguments.cpp`** -> AI Confidence: **99.34%**
1046. **`src/apps/terminal/SetTitleDialog.cpp`** -> AI Confidence: **99.34%**
1047. **`src/bin/bfs_tools/lib/BPlusTree.cpp`** -> AI Confidence: **99.34%**
1048. **`src/bin/desklink/VolumeWindow.cpp`** -> AI Confidence: **99.34%**
1049. **`src/bin/dpms.cpp`** -> AI Confidence: **99.34%**
1050. **`src/bin/isvolume.cpp`** -> AI Confidence: **99.34%**
1051. **`src/bin/listfont.cpp`** -> AI Confidence: **99.34%**
1052. **`src/bin/listusb/usb_audio.cpp`** -> AI Confidence: **99.34%**
1053. **`src/bin/mail_utils/mail.cpp`** -> AI Confidence: **99.34%**
1054. **`src/bin/mkfs/main.cpp`** -> AI Confidence: **99.34%**
1055. **`src/bin/multiuser/login.cpp`** -> AI Confidence: **99.34%**
1056. **`src/bin/network/ppp_up/PPPStatusView.cpp`** -> AI Confidence: **99.34%**
1057. **`src/bin/notify.cpp`** -> AI Confidence: **99.34%**
1058. **`src/bin/pidof.cpp`** -> AI Confidence: **99.34%**
1059. **`src/bin/pkgman/command_info.cpp`** -> AI Confidence: **99.34%**
1060. **`src/bin/rc/rc.cpp`** -> AI Confidence: **99.34%**
1061. **`src/bin/settype.cpp`** -> AI Confidence: **99.34%**
1062. **`src/bin/setversion.cpp`** -> AI Confidence: **99.34%**
1063. **`src/bin/setvolume.cpp`** -> AI Confidence: **99.34%**
1064. **`src/bin/waitfor.cpp`** -> AI Confidence: **99.34%**
1065. **`src/kits/debugger/dwarf/DwarfUtils.cpp`** -> AI Confidence: **99.34%**
1066. **`src/kits/debugger/dwarf/LineNumberProgram.cpp`** -> AI Confidence: **99.34%**
1067. **`src/kits/debugger/jobs/LoadSourceCodeJob.cpp`** -> AI Confidence: **99.34%**
1068. **`src/kits/debugger/model/Variable.cpp`** -> AI Confidence: **99.34%**
1069. **`src/kits/interface/RegionSupport.cpp`** -> AI Confidence: **99.34%**
1070. **`src/kits/midi2/MidiRosterLooper.cpp`** -> AI Confidence: **99.34%**
1071. **`src/kits/screensaver/ScreenSaverRunner.cpp`** -> AI Confidence: **99.34%**
1072. **`src/kits/shared/AboutMenuItem.cpp`** -> AI Confidence: **99.34%**
1073. **`src/kits/shared/DateTimeEdit.cpp`** -> AI Confidence: **99.34%**
1074. **`src/kits/storage/Resources.cpp`** -> AI Confidence: **99.34%**
1075. **`src/libs/glut/glutDstr.cpp`** -> AI Confidence: **99.34%**
1076. **`src/libs/glut/glutEvent.cpp`** -> AI Confidence: **99.34%**
1077. **`src/libs/icon/transformer/StrokeTransformer.cpp`** -> AI Confidence: **99.34%**
1078. **`src/preferences/media/Media.cpp`** -> AI Confidence: **99.34%**
1079. **`src/preferences/repositories/AddRepoWindow.cpp`** -> AI Confidence: **99.34%**
1080. **`src/preferences/shortcuts/EditWindow.cpp`** -> AI Confidence: **99.34%**
1081. **`src/preferences/shortcuts/PopUpColumn.cpp`** -> AI Confidence: **99.34%**
1082. **`src/servers/app/RegionPool.cpp`** -> AI Confidence: **99.34%**
1083. **`src/servers/app/drawing/interface/remote/RemoteEventStream.cpp`** -> AI Confidence: **99.34%**
1084. **`src/servers/midi/PortDrivers.cpp`** -> AI Confidence: **99.34%**
1085. **`src/servers/power/power_button_monitor.cpp`** -> AI Confidence: **99.34%**
1086. **`src/servers/registrar/ClipboardHandler.cpp`** -> AI Confidence: **99.34%**
1087. **`src/system/boot/loader/pager.cpp`** -> AI Confidence: **99.34%**
1088. **`src/system/boot/platform/generic/text_menu.cpp`** -> AI Confidence: **99.34%**
1089. **`src/system/kernel/lib/kernel_vsprintf.cpp`** -> AI Confidence: **99.34%**
1090. **`src/system/kernel/locks/lock.cpp`** -> AI Confidence: **99.34%**
1091. **`src/system/kernel/vm/VMUserAddressSpace.cpp`** -> AI Confidence: **99.34%**
1092. **`src/system/libroot/posix/signal/sigqueue.cpp`** -> AI Confidence: **99.34%**
1093. **`src/system/libroot/posix/signal/sigwaitinfo.cpp`** -> AI Confidence: **99.34%**
1094. **`src/system/libroot/posix/wchar/mbsrtowcs.cpp`** -> AI Confidence: **99.34%**
1095. **`src/system/runtime_loader/arch/arm64/arch_relocate.cpp`** -> AI Confidence: **99.34%**
1096. **`src/system/runtime_loader/arch/x86/arch_relocate.cpp`** -> AI Confidence: **99.34%**
1097. **`src/system/runtime_loader/arch/x86_64/arch_relocate.cpp`** -> AI Confidence: **99.34%**
1098. **`src/tests/add-ons/accelerants/intel_extreme/intel_reg.cpp`** -> AI Confidence: **99.34%**
1099. **`src/tests/add-ons/input_server/TeamMonitorTest.cpp`** -> AI Confidence: **99.34%**
1100. **`src/tests/add-ons/kernel/file_systems/shared/random_read.cpp`** -> AI Confidence: **99.34%**
1101. **`src/tests/kits/app/DanoMessageTest.cpp`** -> AI Confidence: **99.34%**
1102. **`src/tests/kits/app/bmessenger/SMRemoteTargetApp.cpp`** -> AI Confidence: **99.34%**
1103. **`src/tests/kits/game/push_game_sound_test/push_game_sound_sine.cpp`** -> AI Confidence: **99.34%**
1104. **`src/tests/kits/interface/bregion/RegionTestcase.cpp`** -> AI Confidence: **99.34%**
1105. **`src/tests/kits/interface/layout/widget_layout_test/tests/BoxTest.cpp`** -> AI Confidence: **99.34%**
1106. **`src/tests/kits/net/NetAddressTest.cpp`** -> AI Confidence: **99.34%**
1107. **`src/tests/kits/net/cookie/cookie_test.cpp`** -> AI Confidence: **99.34%**
1108. **`src/tests/kits/net/netservices2/HttpDebugLogger.cpp`** -> AI Confidence: **99.34%**
1109. **`src/tests/kits/storage/testapps/dump_mime_types.cpp`** -> AI Confidence: **99.34%**
1110. **`src/tests/kits/translation/multitest/MainControlWindow.cpp`** -> AI Confidence: **99.34%**
1111. **`src/tests/libs/gnu/sched_affinity_test.cpp`** -> AI Confidence: **99.34%**
1112. **`src/tests/servers/app/stress_test/main.cpp`** -> AI Confidence: **99.34%**
1113. **`src/tests/system/kernel/fibo_exec.cpp`** -> AI Confidence: **99.34%**
1114. **`src/tests/system/kernel/select_check.cpp`** -> AI Confidence: **99.34%**
1115. **`src/tests/system/kernel/sigint_bug113_test.cpp`** -> AI Confidence: **99.34%**
1116. **`src/tests/system/libroot/os/system_watching_test.cpp`** -> AI Confidence: **99.34%**
1117. **`src/tests/system/libroot/posix/setpgid_test.cpp`** -> AI Confidence: **99.34%**
1118. **`src/tests/system/network/udp_connect.cpp`** -> AI Confidence: **99.34%**
1119. **`src/tools/cppunit/TestListener.cpp`** -> AI Confidence: **99.34%**
1120. **`src/tools/cppunit/TestUtils.cpp`** -> AI Confidence: **99.34%**
1121. **`src/tools/create_repository_config/create_repository_config.cpp`** -> AI Confidence: **99.34%**
1122. **`src/tools/fs_shell/stat_util.cpp`** -> AI Confidence: **99.34%**
1123. **`src/add-ons/accelerants/radeon/ProposeDisplayMode.c`** -> AI Confidence: **99.34%**
1124. **`src/add-ons/accelerants/radeon/impactv.c`** -> AI Confidence: **99.34%**
1125. **`src/add-ons/accelerants/skeleton/acc_std.h`** -> AI Confidence: **99.34%**
1126. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dsargs.c`** -> AI Confidence: **99.34%**
1127. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dscontrol.c`** -> AI Confidence: **99.34%**
1128. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dsinit.c`** -> AI Confidence: **99.34%**
1129. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dsmthdat.c`** -> AI Confidence: **99.34%**
1130. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/events/evregion.c`** -> AI Confidence: **99.34%**
1131. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/events/evxface.c`** -> AI Confidence: **99.34%**
1132. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/excreate.c`** -> AI Confidence: **99.34%**
1133. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exdump.c`** -> AI Confidence: **99.34%**
1134. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exfield.c`** -> AI Confidence: **99.34%**
1135. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exfldio.c`** -> AI Confidence: **99.34%**
1136. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exoparg2.c`** -> AI Confidence: **99.34%**
1137. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exoparg3.c`** -> AI Confidence: **99.34%**
1138. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exoparg6.c`** -> AI Confidence: **99.34%**
1139. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exprep.c`** -> AI Confidence: **99.34%**
1140. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exresnte.c`** -> AI Confidence: **99.34%**
1141. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exresolv.c`** -> AI Confidence: **99.34%**
1142. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exresop.c`** -> AI Confidence: **99.34%**
1143. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exserial.c`** -> AI Confidence: **99.34%**
1144. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exstore.c`** -> AI Confidence: **99.34%**
1145. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/namespace/nsaccess.c`** -> AI Confidence: **99.34%**
1146. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/namespace/nseval.c`** -> AI Confidence: **99.34%**
1147. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/namespace/nsload.c`** -> AI Confidence: **99.34%**
1148. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/parser/psobject.c`** -> AI Confidence: **99.34%**
1149. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/parser/psopinfo.c`** -> AI Confidence: **99.34%**
1150. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/parser/pstree.c`** -> AI Confidence: **99.34%**
1151. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/utilities/utdelete.c`** -> AI Confidence: **99.34%**
1152. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/utilities/utxfinit.c`** -> AI Confidence: **99.34%**
1153. **`src/add-ons/kernel/busses/scsi/usb/fake_device.c`** -> AI Confidence: **99.34%**
1154. **`src/add-ons/kernel/drivers/audio/cmedia/pcm.c`** -> AI Confidence: **99.34%**
1155. **`src/add-ons/kernel/drivers/input/i2c_elan/Driver.h`** -> AI Confidence: **99.34%**
1156. **`src/add-ons/kernel/drivers/input/i2c_hid/Driver.h`** -> AI Confidence: **99.34%**
1157. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/contrib/ath_hal/ar9300/ar9300_interrupts.c`** -> AI Confidence: **99.34%**
1158. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/contrib/ath_hal/ar9300/ar9300_paprd.c`** -> AI Confidence: **99.34%**
1159. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar5212/ar5413.c`** -> AI Confidence: **99.34%**
1160. **`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/ath_hal/ar5416/ar5416_btcoex.c`** -> AI Confidence: **99.34%**
1161. **`src/add-ons/kernel/file_systems/ntfs/libntfs/collate.c`** -> AI Confidence: **99.34%**
1162. **`src/add-ons/kernel/file_systems/ntfs/libntfs/debug.c`** -> AI Confidence: **99.34%**
1163. **`src/add-ons/kernel/file_systems/ntfs/lowntfs.c`** -> AI Confidence: **99.34%**
1164. **`src/apps/poorman/libhttpd/tdate_parse.c`** -> AI Confidence: **99.34%**
1165. **`src/bin/mount.c`** -> AI Confidence: **99.34%**
1166. **`src/bin/network/telnetd/state.c`** -> AI Confidence: **99.34%**
1167. **`src/bin/pc/pc.c`** -> AI Confidence: **99.34%**
1168. **`src/bin/unzip/fileio.c`** -> AI Confidence: **99.34%**
1169. **`src/libs/libsolv/solv/evr.c`** -> AI Confidence: **99.34%**
1170. **`src/libs/util/trimdomain.c`** -> AI Confidence: **99.34%**
1171. **`src/libs/uuid/test_uuid.c`** -> AI Confidence: **99.34%**
1172. **`src/libs/x86emu/debug.c`** -> AI Confidence: **99.34%**
1173. **`src/libs/x86emu/validate.c`** -> AI Confidence: **99.34%**
1174. **`src/libs/zydis/Zydis/Decoder.c`** -> AI Confidence: **99.34%**
1175. **`src/libs/zydis/Zydis/Formatter.c`** -> AI Confidence: **99.34%**
1176. **`src/system/libroot/os/arch/sparc/fpu_compare.c`** -> AI Confidence: **99.34%**
1177. **`src/system/libroot/os/arch/sparc/fpu_mul.c`** -> AI Confidence: **99.34%**
1178. **`src/system/libroot/posix/glibc/arch/generic/dbl2mpn.c`** -> AI Confidence: **99.34%**
1179. **`src/system/libroot/posix/glibc/arch/x86/ldbl2mpn.c`** -> AI Confidence: **99.34%**
1180. **`src/system/libroot/posix/glibc/iconv/skeleton.c`** -> AI Confidence: **99.34%**
1181. **`src/system/libroot/posix/glibc/libio/iogetdelim.c`** -> AI Confidence: **99.34%**
1182. **`src/system/libroot/posix/glibc/stdio-common/_itoa.c`** -> AI Confidence: **99.34%**
1183. **`src/system/libroot/posix/glibc/stdio-common/printf_size.c`** -> AI Confidence: **99.34%**
1184. **`src/system/libroot/posix/musl/regex/fnmatch.c`** -> AI Confidence: **99.34%**
1185. **`src/system/libroot/posix/stdlib/merge.c`** -> AI Confidence: **99.34%**
1186. **`src/system/libroot/posix/sys/priority.c`** -> AI Confidence: **99.34%**
1187. **`src/system/libroot/posix/unistd/dup.c`** -> AI Confidence: **99.34%**
1188. **`src/tests/add-ons/kernel/file_systems/fs_shell/argv.c`** -> AI Confidence: **99.34%**
1189. **`src/tests/system/benchmarks/forkbench.c`** -> AI Confidence: **99.34%**
1190. **`src/tests/system/benchmarks/memspeed.c`** -> AI Confidence: **99.34%**
1191. **`src/tests/system/libroot/posix/gnulib-test-mbrtowc.c`** -> AI Confidence: **99.34%**
1192. **`src/tests/system/libroot/posix/gnulib-test-mbsnrtowcs.c`** -> AI Confidence: **99.34%**
1193. **`src/tests/system/libroot/posix/gnulib-test-mbsrtowcs.c`** -> AI Confidence: **99.34%**
1194. **`src/tests/system/libroot/posix/gnulib-test-wcrtomb.c`** -> AI Confidence: **99.34%**
1195. **`src/tests/system/libroot/posix/gnulib-test-wcsnrtombs.c`** -> AI Confidence: **99.34%**
1196. **`src/tests/system/libroot/posix/gnulib-test-wcsrtombs.c`** -> AI Confidence: **99.34%**
1197. **`src/tests/system/libroot/posix/tst-fgetws.c`** -> AI Confidence: **99.34%**
1198. **`src/tests/system/libroot/posix/tst-ungetwc2.c`** -> AI Confidence: **99.34%**
1199. **`src/tools/hack_coff/hack-coff.c`** -> AI Confidence: **99.34%**
1200. **`src/bin/unzip/unzip.h`** -> AI Confidence: **99.33%**
1201. **`headers/private/kernel/boot/images.h`** -> AI Confidence: **99.32%**
1202. **`headers/private/kernel/kernel.h`** -> AI Confidence: **99.32%**
1203. **`src/add-ons/accelerants/ati/mach64_mode.cpp`** -> AI Confidence: **99.32%**
1204. **`src/add-ons/accelerants/intel_extreme/TigerLakePLL.cpp`** -> AI Confidence: **99.32%**
1205. **`src/add-ons/input_server/devices/wacom/PointingDeviceFactory.cpp`** -> AI Confidence: **99.32%**
1206. **`src/add-ons/kernel/bus_managers/ata/ATATracing.cpp`** -> AI Confidence: **99.32%**
1207. **`src/add-ons/kernel/drivers/audio/echo/generic/CDarla24DspCommObject.cpp`** -> AI Confidence: **99.32%**
1208. **`src/add-ons/kernel/drivers/audio/echo/generic/CIndigoDspCommObject.cpp`** -> AI Confidence: **99.32%**
1209. **`src/add-ons/kernel/drivers/audio/echo/generic/CMiaDspCommObject.cpp`** -> AI Confidence: **99.32%**
1210. **`src/add-ons/kernel/file_systems/netfs/shared/RequestFactory.cpp`** -> AI Confidence: **99.32%**
1211. **`src/add-ons/kernel/network/protocols/tcp/BufferQueue.cpp`** -> AI Confidence: **99.32%**
1212. **`src/add-ons/media/media-add-ons/finepix_webcam/FinePixUSBKitTest/FinePixTest.cpp`** -> AI Confidence: **99.32%**
1213. **`src/add-ons/media/media-add-ons/radeon/CC.cpp`** -> AI Confidence: **99.32%**
1214. **`src/add-ons/media/plugins/ape_reader/MAClib/MACProgressHelper.cpp`** -> AI Confidence: **99.32%**
1215. **`src/add-ons/media/plugins/ape_reader/MAClib/NewPredictor.cpp`** -> AI Confidence: **99.32%**
1216. **`src/add-ons/translators/psd/PSDLoader.cpp`** -> AI Confidence: **99.32%**
1217. **`src/apps/cortex/addons/LoggingConsumer/LogWriter.cpp`** -> AI Confidence: **99.32%**
1218. **`src/apps/debugger/user_interface/cli/commands/CliQuitCommand.cpp`** -> AI Confidence: **99.32%**
1219. **`src/apps/haiku3d/MeshInstance.cpp`** -> AI Confidence: **99.32%**
1220. **`src/apps/haikudepot/icon/PackageIconDefaultRepository.cpp`** -> AI Confidence: **99.32%**
1221. **`src/bin/ffm.cpp`** -> AI Confidence: **99.32%**
1222. **`src/bin/pkgman/DecisionProvider.cpp`** -> AI Confidence: **99.32%**
1223. **`src/kits/debugger/demangler/Demangler.cpp`** -> AI Confidence: **99.32%**
1224. **`src/kits/support/ByteOrder.cpp`** -> AI Confidence: **99.32%**
1225. **`src/libs/agg/src/agg_vcgen_stroke.cpp`** -> AI Confidence: **99.32%**
1226. **`src/libs/print/libprint/HalftoneView.cpp`** -> AI Confidence: **99.32%**
1227. **`src/libs/stdc++/legacy/pfstream.cc`** -> AI Confidence: **99.32%**
1228. **`src/preferences/printers/SpoolFolder.cpp`** -> AI Confidence: **99.32%**
1229. **`src/servers/app/drawing/Painter/drawing_modes/DrawingModeSubtract.h`** -> AI Confidence: **99.32%**
1230. **`src/system/boot/platform/efi/arch/arm/relocation_func.cpp`** -> AI Confidence: **99.32%**
1231. **`src/system/boot/platform/efi/arch/arm64/relocation_func.cpp`** -> AI Confidence: **99.32%**
1232. **`src/system/boot/platform/efi/arch/riscv64/arch_traps.cpp`** -> AI Confidence: **99.32%**
1233. **`src/system/boot/platform/efi/arch/riscv64/relocation_func.cpp`** -> AI Confidence: **99.32%**
1234. **`src/system/boot/platform/efi/arch/x86/relocation_func.cpp`** -> AI Confidence: **99.32%**
1235. **`src/system/boot/platform/efi/arch/x86_64/relocation_func.cpp`** -> AI Confidence: **99.32%**
1236. **`src/system/libnetwork/netresolv/dst/md5_locl.h`** -> AI Confidence: **99.32%**
1237. **`src/tests/add-ons/print/pdf/bezierbounds/BBView.cpp`** -> AI Confidence: **99.32%**
1238. **`src/tests/add-ons/print/pdf/bezierbounds/BezierBounds.cpp`** -> AI Confidence: **99.32%**
1239. **`src/tests/apps/miniterminal/Console.cpp`** -> AI Confidence: **99.32%**
1240. **`src/tests/kits/interface/bfont/DumpFontList.cpp`** -> AI Confidence: **99.32%**
1241. **`src/tests/system/kernel/fifo_poll_test.cpp`** -> AI Confidence: **99.32%**
1242. **`src/tests/system/libroot/os/FindDirectoryTest.cpp`** -> AI Confidence: **99.32%**
1243. **`src/tests/system/libroot/posix/dirent_test.cpp`** -> AI Confidence: **99.32%**
1244. **`src/tests/system/libroot/posix/getsubopt_test.cpp`** -> AI Confidence: **99.32%**
1245. **`src/add-ons/accelerants/common/dump_edid.c`** -> AI Confidence: **99.32%**
1246. **`src/add-ons/accelerants/via/ProposeDisplayMode.c`** -> AI Confidence: **99.32%**
1247. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/dispatcher/dswscope.c`** -> AI Confidence: **99.32%**
1248. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/events/evgpeutil.c`** -> AI Confidence: **99.32%**
1249. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/events/evxfevnt.c`** -> AI Confidence: **99.32%**
1250. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exdebug.c`** -> AI Confidence: **99.32%**
1251. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/executer/exstorob.c`** -> AI Confidence: **99.32%**
1252. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/hardware/hwregs.c`** -> AI Confidence: **99.32%**
1253. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/hardware/hwxface.c`** -> AI Confidence: **99.32%**
1254. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/namespace/nsobject.c`** -> AI Confidence: **99.32%**
1255. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/namespace/nswalk.c`** -> AI Confidence: **99.32%**
1256. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/resources/rsinfo.c`** -> AI Confidence: **99.32%**
1257. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/resources/rslist.c`** -> AI Confidence: **99.32%**
1258. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/resources/rsmisc.c`** -> AI Confidence: **99.32%**
1259. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/tables/tbfind.c`** -> AI Confidence: **99.32%**
1260. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/utilities/utaddress.c`** -> AI Confidence: **99.32%**
1261. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/utilities/utcopy.c`** -> AI Confidence: **99.32%**
1262. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/utilities/uteval.c`** -> AI Confidence: **99.32%**
1263. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/utilities/utids.c`** -> AI Confidence: **99.32%**
1264. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/utilities/utobject.c`** -> AI Confidence: **99.32%**
1265. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/utilities/utownerid.c`** -> AI Confidence: **99.32%**
1266. **`src/add-ons/kernel/bus_managers/acpi/acpica/components/utilities/utstring.c`** -> AI Confidence: **99.32%**
1267. **`src/add-ons/kernel/drivers/graphics/radeon/detect.c`** -> AI Confidence: **99.32%**
1268. **`src/add-ons/kernel/file_systems/ntfs/libntfs/compat.h`** -> AI Confidence: **99.32%**
1269. **`src/apps/serialconnect/libvterm/src/input.c`** -> AI Confidence: **99.32%**
1270. **`src/apps/serialconnect/libvterm/src/parser.c`** -> AI Confidence: **99.32%**
1271. **`src/bin/network/telnetd/global.c`** -> AI Confidence: **99.32%**
1272. **`src/bin/unzip/list.c`** -> AI Confidence: **99.32%**
1273. **`src/bin/unzip/process.c`** -> AI Confidence: **99.32%**
1274. **`src/libs/bsd/strtonum.c`** -> AI Confidence: **99.32%**
1275. **`src/libs/zydis/Zydis/FormatterBase.c`** -> AI Confidence: **99.32%**
1276. **`src/system/libroot/posix/arch/m68k/fenv.c`** -> AI Confidence: **99.32%**
1277. **`src/system/libroot/posix/glibc/arch/generic/divrem.c`** -> AI Confidence: **99.32%**
1278. **`src/system/libroot/posix/glibc/arch/generic/s_clog.c`** -> AI Confidence: **99.32%**
1279. **`src/system/libroot/posix/glibc/arch/generic/s_clog10.c`** -> AI Confidence: **99.32%**
1280. **`src/system/libroot/posix/glibc/arch/generic/s_clog10f.c`** -> AI Confidence: **99.32%**
1281. **`src/system/libroot/posix/glibc/arch/generic/s_clog10l.c`** -> AI Confidence: **99.32%**
1282. **`src/system/libroot/posix/glibc/arch/generic/s_clogf.c`** -> AI Confidence: **99.32%**
1283. **`src/system/libroot/posix/glibc/arch/generic/s_clogl.c`** -> AI Confidence: **99.32%**
1284. **`src/system/libroot/posix/glibc/arch/generic/s_csqrtl.c`** -> AI Confidence: **99.32%**
1285. **`src/system/libroot/posix/glibc/libio/iofsetpos.c`** -> AI Confidence: **99.32%**
1286. **`src/system/libroot/posix/glibc/libio/ioseekoff.c`** -> AI Confidence: **99.32%**
1287. **`src/system/libroot/posix/musl/math/fmaf.c`** -> AI Confidence: **99.32%**
1288. **`src/system/libroot/posix/wchar/wcwidth.c`** -> AI Confidence: **99.32%**
1289. **`src/tests/system/libroot/posix/test_wcfuncs.c`** -> AI Confidence: **99.32%**
1290. **`src/tests/system/libroot/posix/tst-swprintf.c`** -> AI Confidence: **99.32%**
1291. **`src/tests/system/libroot/posix/tst-swscanf2.c`** -> AI Confidence: **99.32%**
1292. **`src/tests/system/libroot/posix/tst-wscanf.c`** -> AI Confidence: **99.32%**
1293. **`configure`** -> AI Confidence: **99.31%**
1294. **`3rdparty/mmu_man/irc/Haiku/plugin.py`** -> AI Confidence: **99.31%**
1295. **`src/tests/kits/net/netservices2/testserver.py`** -> AI Confidence: **99.31%**
1296. **`src/tests/kits/net/service/testserver.py`** -> AI Confidence: **99.31%**
1297. **`3rdparty/proj2make/proj2make.cpp`** -> AI Confidence: **99.31%**
1298. **`headers/libs/zydis/Zycore/LibC.h`** -> AI Confidence: **99.31%**
1299. **`headers/private/util/OpenHashTable.h`** -> AI Confidence: **99.31%**
1300. **`headers/tools/cppunit/cppunit/Portability.h`** -> AI Confidence: **99.31%**
1301. **`src/add-ons/accelerants/radeon_hd/accelerant.cpp`** -> AI Confidence: **99.31%**
1302. **`src/add-ons/accelerants/radeon_hd/gpu.cpp`** -> AI Confidence: **99.31%**
1303. **`src/add-ons/accelerants/radeon_hd/mode.cpp`** -> AI Confidence: **99.31%**
1304. **`src/add-ons/accelerants/vesa/accelerant.cpp`** -> AI Confidence: **99.31%**
1305. **`src/add-ons/accelerants/vesa/mode.cpp`** -> AI Confidence: **99.31%**
1306. **`src/add-ons/disk_systems/bfs/BFSAddOn.cpp`** -> AI Confidence: **99.31%**
1307. **`src/add-ons/disk_systems/bfs/InitializeParameterEditor.cpp`** -> AI Confidence: **99.31%**
1308. **`src/add-ons/disk_systems/fat/InitializeParameterEditor.cpp`** -> AI Confidence: **99.31%**
1309. **`src/add-ons/disk_systems/gpt/GPTDiskAddOn.cpp`** -> AI Confidence: **99.31%**
1310. **`src/add-ons/disk_systems/gpt/GPTPartitionHandle.cpp`** -> AI Confidence: **99.31%**
1311. **`src/add-ons/disk_systems/intel/ExtendedPartitionAddOn.cpp`** -> AI Confidence: **99.31%**
1312. **`src/add-ons/disk_systems/intel/PartitionMapAddOn.cpp`** -> AI Confidence: **99.31%**
1313. **`src/add-ons/disk_systems/intel/PrimaryParameterEditor.cpp`** -> AI Confidence: **99.31%**
1314. **`src/add-ons/input_server/devices/keyboard/TeamListItem.cpp`** -> AI Confidence: **99.31%**
1315. **`src/add-ons/input_server/devices/mouse/MouseInputDevice.cpp`** -> AI Confidence: **99.31%**
1316. **`src/add-ons/input_server/devices/serial_mouse/MouseInputDevice.cpp`** -> AI Confidence: **99.31%**
1317. **`src/add-ons/input_server/devices/tablet/TabletInputDevice.cpp`** -> AI Confidence: **99.31%**
1318. **`src/add-ons/input_server/devices/virtualkeyboard/VirtualKeyboardWindow.cpp`** -> AI Confidence: **99.31%**
1319. **`src/add-ons/input_server/devices/wacom/MasterServerDevice.cpp`** -> AI Confidence: **99.31%**
1320. **`src/add-ons/input_server/filters/shortcut_catcher/CommandExecutor.cpp`** -> AI Confidence: **99.31%**
1321. **`src/add-ons/input_server/filters/shortcut_catcher/KeyInfos.cpp`** -> AI Confidence: **99.31%**
1322. **`src/add-ons/kernel/bluetooth/btCoreData/ConnectionInterface.cpp`** -> AI Confidence: **99.31%**
1323. **`src/add-ons/kernel/bluetooth/hci/acl.cpp`** -> AI Confidence: **99.31%**
1324. **`src/add-ons/kernel/bluetooth/hci/bluetooth.cpp`** -> AI Confidence: **99.31%**
1325. **`src/add-ons/kernel/bus_managers/acpi/ACPICAHaiku.cpp`** -> AI Confidence: **99.31%**
1326. **`src/add-ons/kernel/bus_managers/acpi/BusManager.cpp`** -> AI Confidence: **99.31%**
1327. **`src/add-ons/kernel/bus_managers/acpi/NamespaceDump.cpp`** -> AI Confidence: **99.31%**
1328. **`src/add-ons/kernel/bus_managers/acpi/arch/x86/arch_init.cpp`** -> AI Confidence: **99.31%**
1329. **`src/add-ons/kernel/bus_managers/agp_gart/agp_gart.cpp`** -> AI Confidence: **99.31%**
1330. **`src/add-ons/kernel/bus_managers/fdt/fdt_module.cpp`** -> AI Confidence: **99.31%**
1331. **`src/add-ons/kernel/bus_managers/firewire/firewire.cpp`** -> AI Confidence: **99.31%**
1332. **`src/add-ons/kernel/bus_managers/firewire/firewire_module.cpp`** -> AI Confidence: **99.31%**
1333. **`src/add-ons/kernel/bus_managers/firewire/fwohci.cpp`** -> AI Confidence: **99.31%**
1334. **`src/add-ons/kernel/bus_managers/firewire/fwohci_pci.cpp`** -> AI Confidence: **99.31%**
1335. **`src/add-ons/kernel/bus_managers/pci/pci.cpp`** -> AI Confidence: **99.31%**
1336. **`src/add-ons/kernel/bus_managers/pci/pci_info.cpp`** -> AI Confidence: **99.31%**
1337. **`src/add-ons/kernel/bus_managers/ps2/ps2_keyboard.cpp`** -> AI Confidence: **99.31%**
1338. **`src/add-ons/kernel/bus_managers/usb/Stack.cpp`** -> AI Confidence: **99.31%**
1339. **`src/add-ons/kernel/bus_managers/virtio/VirtioBalloonDevice.cpp`** -> AI Confidence: **99.31%**
1340. **`src/add-ons/kernel/busses/i2c/pch/pch_i2c_pci.cpp`** -> AI Confidence: **99.31%**
1341. **`src/add-ons/kernel/busses/mmc/sdhci.cpp`** -> AI Confidence: **99.31%**
1342. **`src/add-ons/kernel/busses/mmc/sdhci_pci.cpp`** -> AI Confidence: **99.31%**
1343. **`src/add-ons/kernel/busses/usb/ohci.cpp`** -> AI Confidence: **99.31%**
1344. **`src/add-ons/kernel/busses/usb/xhci.cpp`** -> AI Confidence: **99.31%**
1345. **`src/add-ons/kernel/busses/virtio/virtio_mmio/VirtioDevice.cpp`** -> AI Confidence: **99.31%**
1346. **`src/add-ons/kernel/busses/virtio/virtio_mmio/virtio_mmio.cpp`** -> AI Confidence: **99.31%**
1347. **`src/add-ons/kernel/busses/virtio/virtio_pci/virtio_pci.cpp`** -> AI Confidence: **99.31%**
1348. **`src/add-ons/kernel/cpu/x86/generic_x86.cpp`** -> AI Confidence: **99.31%**
1349. **`src/add-ons/kernel/debugger/demangle/gcc2.cpp`** -> AI Confidence: **99.31%**
1350. **`src/add-ons/kernel/debugger/laplinkll/laplinkll.cpp`** -> AI Confidence: **99.31%**
1351. **`src/add-ons/kernel/drivers/audio/echo/echo.cpp`** -> AI Confidence: **99.31%**
1352. **`src/add-ons/kernel/drivers/audio/echo/multi.cpp`** -> AI Confidence: **99.31%**
1353. **`src/add-ons/kernel/drivers/audio/ice1712/ice1712.cpp`** -> AI Confidence: **99.31%**
1354. **`src/add-ons/kernel/drivers/audio/usb/Settings.cpp`** -> AI Confidence: **99.31%**
1355. **`src/add-ons/kernel/drivers/bluetooth/h2/h2generic/h2transactions.cpp`** -> AI Confidence: **99.31%**
1356. **`src/add-ons/kernel/drivers/common/usb_modeswitch.cpp`** -> AI Confidence: **99.31%**
1357. **`src/add-ons/kernel/drivers/disk/mmc/mmc_disk.cpp`** -> AI Confidence: **99.31%**
1358. **`src/add-ons/kernel/drivers/disk/nvme/nvme_disk.cpp`** -> AI Confidence: **99.31%**
1359. **`src/add-ons/kernel/drivers/disk/usb/usb_disk/usb_disk.cpp`** -> AI Confidence: **99.31%**
1360. **`src/add-ons/kernel/drivers/disk/virtual/ram_disk/ram_disk.cpp`** -> AI Confidence: **99.31%**
1361. **`src/add-ons/kernel/drivers/disk/virtual/remote_disk/RemoteDisk.cpp`** -> AI Confidence: **99.31%**
1362. **`src/add-ons/kernel/drivers/graphics/intel_extreme/bios.cpp`** -> AI Confidence: **99.31%**
1363. **`src/add-ons/kernel/drivers/graphics/intel_extreme/device.cpp`** -> AI Confidence: **99.31%**
1364. **`src/add-ons/kernel/drivers/graphics/intel_extreme/driver.cpp`** -> AI Confidence: **99.31%**
1365. **`src/add-ons/kernel/drivers/graphics/s3/driver.cpp`** -> AI Confidence: **99.31%**
1366. **`src/add-ons/kernel/drivers/graphics/vesa/device.cpp`** -> AI Confidence: **99.31%**
1367. **`src/add-ons/kernel/drivers/graphics/vesa/vesa.cpp`** -> AI Confidence: **99.31%**
1368. **`src/add-ons/kernel/drivers/input/hyperv_hid/HIDDevice.cpp`** -> AI Confidence: **99.31%**
1369. **`src/add-ons/kernel/drivers/input/i2c_elan/ELANDevice.cpp`** -> AI Confidence: **99.31%**
1370. **`src/add-ons/kernel/drivers/input/i2c_hid/HIDDevice.cpp`** -> AI Confidence: **99.31%**
1371. **`src/add-ons/kernel/drivers/input/usb_hid/Driver.cpp`** -> AI Confidence: **99.31%**
1372. **`src/add-ons/kernel/drivers/input/virtio_input/virtio_input.cpp`** -> AI Confidence: **99.31%**
1373. **`src/add-ons/kernel/drivers/misc/poke.cpp`** -> AI Confidence: **99.31%**
1374. **`src/add-ons/kernel/drivers/network/ether/usb_davicom/Settings.cpp`** -> AI Confidence: **99.31%**
1375. **`src/add-ons/kernel/drivers/network/ether/virtio/virtio_net.cpp`** -> AI Confidence: **99.31%**
1376. **`src/add-ons/kernel/drivers/ports/pc_serial/Driver.cpp`** -> AI Confidence: **99.31%**
1377. **`src/add-ons/kernel/drivers/ports/pc_serial/Tracing.cpp`** -> AI Confidence: **99.31%**
1378. **`src/add-ons/kernel/drivers/ports/usb_serial/Driver.cpp`** -> AI Confidence: **99.31%**
1379. **`src/add-ons/kernel/drivers/ports/usb_serial/SerialDevice.cpp`** -> AI Confidence: **99.31%**
1380. **`src/add-ons/kernel/drivers/ports/usb_serial/Tracing.cpp`** -> AI Confidence: **99.31%**
1381. **`src/add-ons/kernel/drivers/power/acpi_battery/acpi_battery.cpp`** -> AI Confidence: **99.31%**
1382. **`src/add-ons/kernel/file_cache/log.cpp`** -> AI Confidence: **99.31%**
1383. **`src/add-ons/kernel/file_systems/bfs/Volume.cpp`** -> AI Confidence: **99.31%**
1384. **`src/add-ons/kernel/file_systems/bfs/kernel_interface.cpp`** -> AI Confidence: **99.31%**
1385. **`src/add-ons/kernel/file_systems/bindfs/DebugSupport.cpp`** -> AI Confidence: **99.31%**
1386. **`src/add-ons/kernel/file_systems/bindfs/Volume.cpp`** -> AI Confidence: **99.31%**
1387. **`src/add-ons/kernel/file_systems/btrfs/Volume.cpp`** -> AI Confidence: **99.31%**
1388. **`src/add-ons/kernel/file_systems/cdda/kernel_interface.cpp`** -> AI Confidence: **99.31%**
1389. **`src/add-ons/kernel/file_systems/exfat/Inode.cpp`** -> AI Confidence: **99.31%**
1390. **`src/add-ons/kernel/file_systems/ext2/DirectoryIterator.cpp`** -> AI Confidence: **99.31%**
1391. **`src/add-ons/kernel/file_systems/ext2/HTree.cpp`** -> AI Confidence: **99.31%**
1392. **`src/add-ons/kernel/file_systems/ext2/Inode.cpp`** -> AI Confidence: **99.31%**
1393. **`src/add-ons/kernel/file_systems/ext2/Journal.cpp`** -> AI Confidence: **99.31%**
1394. **`src/add-ons/kernel/file_systems/ext2/Volume.cpp`** -> AI Confidence: **99.31%**
1395. **`src/add-ons/kernel/file_systems/ext2/kernel_interface.cpp`** -> AI Confidence: **99.31%**
1396. **`src/add-ons/kernel/file_systems/fat/debug.cpp`** -> AI Confidence: **99.31%**
1397. **`src/add-ons/kernel/file_systems/fat/mkdos.cpp`** -> AI Confidence: **99.31%**
1398. **`src/add-ons/kernel/file_systems/fat/vcache.cpp`** -> AI Confidence: **99.31%**
1399. **`src/add-ons/kernel/file_systems/iso9660/iso9660_identify.cpp`** -> AI Confidence: **99.31%**
1400. **`src/add-ons/kernel/file_systems/netfs/authentication_server/AuthenticationServer.cpp`** -> AI Confidence: **99.31%**
1401. **`src/add-ons/kernel/file_systems/netfs/client/QueryManager.cpp`** -> AI Confidence: **99.31%**
1402. **`src/add-ons/kernel/file_systems/netfs/client/ServerConnection.cpp`** -> AI Confidence: **99.31%**
1403. **`src/add-ons/kernel/file_systems/netfs/client/ServerManager.cpp`** -> AI Confidence: **99.31%**
1404. **`src/add-ons/kernel/file_systems/netfs/client/ServerVolume.cpp`** -> AI Confidence: **99.31%**
1405. **`src/add-ons/kernel/file_systems/netfs/client/ShareAttrDir.cpp`** -> AI Confidence: **99.31%**
1406. **`src/add-ons/kernel/file_systems/netfs/client/ShareVolume.cpp`** -> AI Confidence: **99.31%**
1407. **`src/add-ons/kernel/file_systems/netfs/netfs_config/netfs_config.cpp`** -> AI Confidence: **99.31%**
1408. **`src/add-ons/kernel/file_systems/netfs/server/FDManager.cpp`** -> AI Confidence: **99.31%**
1409. **`src/add-ons/kernel/file_systems/netfs/server/InsecureConnectionListener.cpp`** -> AI Confidence: **99.31%**
1410. **`src/add-ons/kernel/file_systems/netfs/server/SecurityContext.cpp`** -> AI Confidence: **99.31%**
1411. **`src/add-ons/kernel/file_systems/netfs/server/VolumeManager.cpp`** -> AI Confidence: **99.31%**
1412. **`src/add-ons/kernel/file_systems/netfs/shared/DebugSupport.cpp`** -> AI Confidence: **99.31%**
1413. **`src/add-ons/kernel/file_systems/netfs/shared/InsecureChannel.cpp`** -> AI Confidence: **99.31%**
1414. **`src/add-ons/kernel/file_systems/netfs/shared/InsecureConnection.cpp`** -> AI Confidence: **99.31%**
1415. **`src/add-ons/kernel/file_systems/netfs/shared/NetAddress.cpp`** -> AI Confidence: **99.31%**
1416. **`src/add-ons/kernel/file_systems/netfs/shared/RequestChannel.cpp`** -> AI Confidence: **99.31%**
1417. **`src/add-ons/kernel/file_systems/netfs/shared/RequestConnection.cpp`** -> AI Confidence: **99.31%**
1418. **`src/add-ons/kernel/file_systems/nfs4/Connection.cpp`** -> AI Confidence: **99.31%**
1419. **`src/add-ons/kernel/file_systems/nfs4/FileSystem.cpp`** -> AI Confidence: **99.31%**
1420. **`src/add-ons/kernel/file_systems/nfs4/Inode.cpp`** -> AI Confidence: **99.31%**
1421. **`src/add-ons/kernel/file_systems/nfs4/InodeRegular.cpp`** -> AI Confidence: **99.31%**
1422. **`src/add-ons/kernel/file_systems/nfs4/RPCAuth.cpp`** -> AI Confidence: **99.31%**
1423. **`src/add-ons/kernel/file_systems/nfs4/RequestBuilder.cpp`** -> AI Confidence: **99.31%**
1424. **`src/add-ons/kernel/file_systems/ntfs/kernel_interface.cpp`** -> AI Confidence: **99.31%**
1425. **`src/add-ons/kernel/file_systems/packagefs/package/CachedDataReader.cpp`** -> AI Confidence: **99.31%**
1426. **`src/add-ons/kernel/file_systems/packagefs/package/Package.cpp`** -> AI Confidence: **99.31%**
1427. **`src/add-ons/kernel/file_systems/packagefs/package_links/PackageLinkDirectory.cpp`** -> AI Confidence: **99.31%**
1428. **`src/add-ons/kernel/file_systems/packagefs/util/Version.cpp`** -> AI Confidence: **99.31%**
1429. **`src/add-ons/kernel/file_systems/packagefs/volume/PackageSettings.cpp`** -> AI Confidence: **99.31%**
1430. **`src/add-ons/kernel/file_systems/ramfs/AttributeIndexImpl.cpp`** -> AI Confidence: **99.31%**
1431. **`src/add-ons/kernel/file_systems/ramfs/LastModifiedIndex.cpp`** -> AI Confidence: **99.31%**
1432. **`src/add-ons/kernel/file_systems/ramfs/NameIndex.cpp`** -> AI Confidence: **99.31%**
1433. **`src/add-ons/kernel/file_systems/ramfs/SizeIndex.cpp`** -> AI Confidence: **99.31%**
1434. **`src/add-ons/kernel/file_systems/ramfs/Volume.cpp`** -> AI Confidence: **99.31%**
1435. **`src/add-ons/kernel/file_systems/reiserfs/BlockCache.cpp`** -> AI Confidence: **99.31%**
1436. **`src/add-ons/kernel/file_systems/reiserfs/kernel_interface.cpp`** -> AI Confidence: **99.31%**
1437. **`src/add-ons/kernel/file_systems/shared/DebugSupport.cpp`** -> AI Confidence: **99.31%**
1438. **`src/add-ons/kernel/file_systems/userlandfs/kernel_add_on/FileSystemInitializer.cpp`** -> AI Confidence: **99.31%**
1439. **`src/add-ons/kernel/file_systems/userlandfs/kernel_add_on/KernelDebug.cpp`** -> AI Confidence: **99.31%**
1440. **`src/add-ons/kernel/file_systems/userlandfs/kernel_add_on/KernelRequestHandler.cpp`** -> AI Confidence: **99.31%**
1441. **`src/add-ons/kernel/file_systems/userlandfs/kernel_add_on/Settings.cpp`** -> AI Confidence: **99.31%**
1442. **`src/add-ons/kernel/file_systems/userlandfs/kernel_add_on/UserlandFS.cpp`** -> AI Confidence: **99.31%**
1443. **`src/add-ons/kernel/file_systems/userlandfs/server/UserlandRequestHandler.cpp`** -> AI Confidence: **99.31%**
1444. **`src/add-ons/kernel/file_systems/userlandfs/server/fuse/FUSEFileSystem.cpp`** -> AI Confidence: **99.31%**
1445. **`src/add-ons/kernel/file_systems/userlandfs/server/fuse/FUSEVolume.cpp`** -> AI Confidence: **99.31%**
1446. **`src/add-ons/kernel/file_systems/userlandfs/server/main.cpp`** -> AI Confidence: **99.31%**
1447. **`src/add-ons/kernel/file_systems/userlandfs/shared/Debug.cpp`** -> AI Confidence: **99.31%**
1448. **`src/add-ons/kernel/generic/ata_adapter/ata_adapter.cpp`** -> AI Confidence: **99.31%**
1449. **`src/add-ons/kernel/generic/smbios/smbios.cpp`** -> AI Confidence: **99.31%**
1450. **`src/add-ons/kernel/generic/tty/tty.cpp`** -> AI Confidence: **99.31%**
1451. **`src/add-ons/kernel/network/datalink_protocols/arp/arp.cpp`** -> AI Confidence: **99.31%**
1452. **`src/add-ons/kernel/network/datalink_protocols/ipv6_datagram/ipv6_datagram.cpp`** -> AI Confidence: **99.31%**
1453. **`src/add-ons/kernel/network/devices/dialup/dialup.cpp`** -> AI Confidence: **99.31%**
1454. **`src/add-ons/kernel/network/devices/ethernet/ethernet.cpp`** -> AI Confidence: **99.31%**
1455. **`src/add-ons/kernel/network/devices/tunnel/tunnel.cpp`** -> AI Confidence: **99.31%**
1456. **`src/add-ons/kernel/network/dns_resolver/kernel_add_on/dns_resolver.cpp`** -> AI Confidence: **99.31%**
1457. **`src/add-ons/kernel/network/dns_resolver/server/main.cpp`** -> AI Confidence: **99.31%**
1458. **`src/add-ons/kernel/network/ppp/ipcp/ipcp.cpp`** -> AI Confidence: **99.31%**
1459. **`src/add-ons/kernel/network/ppp/modem/ModemDevice.cpp`** -> AI Confidence: **99.31%**
1460. **`src/add-ons/kernel/network/ppp/pap/Protocol.cpp`** -> AI Confidence: **99.31%**
1461. **`src/add-ons/kernel/network/ppp/pap/pap.cpp`** -> AI Confidence: **99.31%**
1462. **`src/add-ons/kernel/network/ppp/ppp_frame/ppp_frame.cpp`** -> AI Confidence: **99.31%**
1463. **`src/add-ons/kernel/network/ppp/ppp_manager/KPPPManager.cpp`** -> AI Confidence: **99.31%**
1464. **`src/add-ons/kernel/network/ppp/pppoe/PPPoEDevice.cpp`** -> AI Confidence: **99.31%**
1465. **`src/add-ons/kernel/network/ppp/pppoe/pppoe.cpp`** -> AI Confidence: **99.31%**
1466. **`src/add-ons/kernel/network/ppp/shared/libkernelppp/KPPPInterface.cpp`** -> AI Confidence: **99.31%**
1467. **`src/add-ons/kernel/network/ppp/shared/libkernelppp/KPPPLCP.cpp`** -> AI Confidence: **99.31%**
1468. **`src/add-ons/kernel/network/ppp/shared/libppp/MessageDriverSettingsUtils.cpp`** -> AI Confidence: **99.31%**
1469. **`src/add-ons/kernel/network/ppp/shared/libppp/PPPManager.cpp`** -> AI Confidence: **99.31%**
1470. **`src/add-ons/kernel/network/protocols/icmp/icmp.cpp`** -> AI Confidence: **99.31%**
1471. **`src/add-ons/kernel/network/protocols/ipv4/ipv4.cpp`** -> AI Confidence: **99.31%**
1472. **`src/add-ons/kernel/network/protocols/ipv4/ipv4_address.cpp`** -> AI Confidence: **99.31%**
1473. **`src/add-ons/kernel/network/protocols/ipv6/ipv6.cpp`** -> AI Confidence: **99.31%**
1474. **`src/add-ons/kernel/network/protocols/ipv6/ipv6_address.cpp`** -> AI Confidence: **99.31%**
1475. **`src/add-ons/kernel/network/protocols/l2cap/L2capEndpoint.cpp`** -> AI Confidence: **99.31%**
1476. **`src/add-ons/kernel/network/protocols/l2cap/l2cap_address.cpp`** -> AI Confidence: **99.31%**
1477. **`src/add-ons/kernel/network/protocols/l2cap/l2cap_signal.cpp`** -> AI Confidence: **99.31%**
1478. **`src/add-ons/kernel/network/protocols/tcp/TCPEndpoint.cpp`** -> AI Confidence: **99.31%**
1479. **`src/add-ons/kernel/network/protocols/tcp/tcp.cpp`** -> AI Confidence: **99.31%**
1480. **`src/add-ons/kernel/network/protocols/unix/UnixAddress.cpp`** -> AI Confidence: **99.31%**
1481. **`src/add-ons/kernel/network/protocols/unix/unix.cpp`** -> AI Confidence: **99.31%**
1482. **`src/add-ons/kernel/network/stack/datalink.cpp`** -> AI Confidence: **99.31%**
1483. **`src/add-ons/kernel/network/stack/device_interfaces.cpp`** -> AI Confidence: **99.31%**
1484. **`src/add-ons/kernel/network/stack/interfaces.cpp`** -> AI Confidence: **99.31%**
1485. **`src/add-ons/kernel/network/stack/net_buffer.cpp`** -> AI Confidence: **99.31%**
1486. **`src/add-ons/kernel/network/stack/net_socket.cpp`** -> AI Confidence: **99.31%**
1487. **`src/add-ons/kernel/network/stack/routes.cpp`** -> AI Confidence: **99.31%**
1488. **`src/add-ons/kernel/network/stack/utility.cpp`** -> AI Confidence: **99.31%**
1489. **`src/add-ons/kernel/partitioning_systems/amiga/amiga_rdb.cpp`** -> AI Confidence: **99.31%**
1490. **`src/add-ons/kernel/partitioning_systems/apple/apple.cpp`** -> AI Confidence: **99.31%**
1491. **`src/add-ons/kernel/partitioning_systems/gpt/Header.cpp`** -> AI Confidence: **99.31%**
1492. **`src/add-ons/kernel/partitioning_systems/gpt/gpt.cpp`** -> AI Confidence: **99.31%**
1493. **`src/add-ons/kernel/partitioning_systems/intel/PartitionMap.cpp`** -> AI Confidence: **99.31%**
1494. **`src/add-ons/kernel/partitioning_systems/intel/PartitionMapWriter.cpp`** -> AI Confidence: **99.31%**
1495. **`src/add-ons/kernel/partitioning_systems/intel/intel.cpp`** -> AI Confidence: **99.31%**
1496. **`src/add-ons/kernel/partitioning_systems/intel/write_support.cpp`** -> AI Confidence: **99.31%**
1497. **`src/add-ons/kernel/partitioning_systems/session/session.cpp`** -> AI Confidence: **99.31%**
1498. **`src/add-ons/kernel/partitioning_systems/sun/sun.cpp`** -> AI Confidence: **99.31%**
1499. **`src/add-ons/kernel/partitioning_systems/vmdk/vmdk.cpp`** -> AI Confidence: **99.31%**
1500. **`src/add-ons/kernel/power/cpufreq/intel_pstates/intel_pstates.cpp`** -> AI Confidence: **99.31%**
1501. **`src/add-ons/kernel/power/cpuidle/x86_acpi_cstates/acpi_cpuidle.cpp`** -> AI Confidence: **99.31%**
1502. **`src/add-ons/mail_daemon/inbound_filters/match_header/ConfigView.cpp`** -> AI Confidence: **99.31%**
1503. **`src/add-ons/mail_daemon/inbound_filters/match_header/RuleFilter.cpp`** -> AI Confidence: **99.31%**
1504. **`src/add-ons/mail_daemon/inbound_filters/notifier/NotifierConfigView.cpp`** -> AI Confidence: **99.31%**
1505. **`src/add-ons/mail_daemon/inbound_filters/notifier/NotifierFilter.cpp`** -> AI Confidence: **99.31%**
1506. **`src/add-ons/mail_daemon/inbound_filters/spam_filter/SpamFilter.cpp`** -> AI Confidence: **99.31%**
1507. **`src/add-ons/mail_daemon/inbound_protocols/imap/FolderConfigWindow.cpp`** -> AI Confidence: **99.31%**
1508. **`src/add-ons/mail_daemon/inbound_protocols/imap/IMAPFolder.cpp`** -> AI Confidence: **99.31%**
1509. **`src/add-ons/mail_daemon/inbound_protocols/imap/IMAPProtocol.cpp`** -> AI Confidence: **99.31%**
1510. **`src/add-ons/mail_daemon/inbound_protocols/pop3/POP3.cpp`** -> AI Confidence: **99.31%**
1511. **`src/add-ons/media/media-add-ons/AbstractFileInterfaceNode.cpp`** -> AI Confidence: **99.31%**
1512. **`src/add-ons/media/media-add-ons/dvb/DVBCard.cpp`** -> AI Confidence: **99.31%**
1513. **`src/add-ons/media/media-add-ons/dvb/DVBMediaAddon.cpp`** -> AI Confidence: **99.31%**
1514. **`src/add-ons/media/media-add-ons/equalizer/EqualizerNode.cpp`** -> AI Confidence: **99.31%**
1515. **`src/add-ons/media/media-add-ons/esound_sink/ESDSinkAddOn.cpp`** -> AI Confidence: **99.31%**
1516. **`src/add-ons/media/media-add-ons/esound_sink/ESDSinkNode.cpp`** -> AI Confidence: **99.31%**
1517. **`src/add-ons/media/media-add-ons/finepix_webcam/FinePixProducer/Producer.cpp`** -> AI Confidence: **99.31%**
1518. **`src/add-ons/media/media-add-ons/firewire_dv/FireWireDVNode.cpp`** -> AI Confidence: **99.31%**
1519. **`src/add-ons/media/media-add-ons/mixer/MixerInput.cpp`** -> AI Confidence: **99.31%**
1520. **`src/add-ons/media/media-add-ons/mixer/MixerSettings.cpp`** -> AI Confidence: **99.31%**
1521. **`src/add-ons/media/media-add-ons/multi_audio/MultiAudioAddOn.cpp`** -> AI Confidence: **99.31%**
1522. **`src/add-ons/media/media-add-ons/multi_audio/MultiAudioNode.cpp`** -> AI Confidence: **99.31%**
1523. **`src/add-ons/media/media-add-ons/opensound/OpenSoundDevice.cpp`** -> AI Confidence: **99.31%**
1524. **`src/add-ons/media/media-add-ons/opensound/OpenSoundDeviceEngine.cpp`** -> AI Confidence: **99.31%**
1525. **`src/add-ons/media/media-add-ons/radeon/RadeonAddOn.cpp`** -> AI Confidence: **99.31%**
1526. **`src/add-ons/media/media-add-ons/radeon/RadeonProducer.cpp`** -> AI Confidence: **99.31%**
1527. **`src/add-ons/media/media-add-ons/radeon/Theater200.cpp`** -> AI Confidence: **99.31%**
1528. **`src/add-ons/media/media-add-ons/usb_vision/AddOn.cpp`** -> AI Confidence: **99.31%**
1529. **`src/add-ons/media/media-add-ons/usb_webcam/AddOn.cpp`** -> AI Confidence: **99.31%**
1530. **`src/add-ons/media/media-add-ons/usb_webcam/CamDevice.cpp`** -> AI Confidence: **99.31%**
1531. **`src/add-ons/media/media-add-ons/usb_webcam/Producer.cpp`** -> AI Confidence: **99.31%**
1532. **`src/add-ons/media/media-add-ons/usb_webcam/addons/sonix/SonixCamDevice.cpp`** -> AI Confidence: **99.31%**
1533. **`src/add-ons/media/media-add-ons/videowindow/VideoNode.cpp`** -> AI Confidence: **99.31%**
1534. **`src/add-ons/media/media-add-ons/videowindow/VideoView.cpp`** -> AI Confidence: **99.31%**
1535. **`src/add-ons/media/media-add-ons/vst_host/VSTAddOn.cpp`** -> AI Confidence: **99.31%**
1536. **`src/add-ons/media/media-add-ons/vst_host/VSTNode.cpp`** -> AI Confidence: **99.31%**
1537. **`src/add-ons/media/plugins/ape_reader/MAClib/MACLib.cpp`** -> AI Confidence: **99.31%**
1538. **`src/add-ons/media/plugins/ape_reader/MAClib/StdLibFileIO.cpp`** -> AI Confidence: **99.31%**
1539. **`src/add-ons/media/plugins/ffmpeg/AVCodecDecoder.cpp`** -> AI Confidence: **99.31%**
1540. **`src/add-ons/media/plugins/ffmpeg/AVFormatWriter.cpp`** -> AI Confidence: **99.31%**
1541. **`src/add-ons/media/plugins/ffmpeg/gfx_util.cpp`** -> AI Confidence: **99.31%**
1542. **`src/add-ons/network_settings/dialup/GeneralAddon.cpp`** -> AI Confidence: **99.31%**
1543. **`src/add-ons/network_settings/dialup/IPCPAddon.cpp`** -> AI Confidence: **99.31%**
1544. **`src/add-ons/network_settings/dialup/MessageDriverSettingsUtils.cpp`** -> AI Confidence: **99.31%**
1545. **`src/add-ons/network_settings/hostname/HostnameView.cpp`** -> AI Confidence: **99.31%**
1546. **`src/add-ons/network_settings/sshd/SSHServiceAddOn.cpp`** -> AI Confidence: **99.31%**
1547. **`src/add-ons/print/drivers/canon_lips/lips3/Lips3.cpp`** -> AI Confidence: **99.31%**
1548. **`src/add-ons/print/drivers/canon_lips/lips4/Lips4.cpp`** -> AI Confidence: **99.31%**
1549. **`src/add-ons/print/drivers/gutenprint/GPDriver.cpp`** -> AI Confidence: **99.31%**
1550. **`src/add-ons/print/drivers/gutenprint/SelectPrinterDialog.cpp`** -> AI Confidence: **99.31%**
1551. **`src/add-ons/print/drivers/pcl5/PCL5.cpp`** -> AI Confidence: **99.31%**
1552. **`src/add-ons/print/drivers/pcl6/PCL6.cpp`** -> AI Confidence: **99.31%**
1553. **`src/add-ons/print/transports/hp_jetdirect/HPJetDirectTransport.cpp`** -> AI Confidence: **99.31%**
1554. **`src/add-ons/print/transports/hp_jetdirect/SetupWindow.cpp`** -> AI Confidence: **99.31%**
1555. **`src/add-ons/print/transports/ipp/Ipp.cpp`** -> AI Confidence: **99.31%**
1556. **`src/add-ons/print/transports/ipp/IppContent.cpp`** -> AI Confidence: **99.31%**
1557. **`src/add-ons/print/transports/ipp/IppSetupDlg.cpp`** -> AI Confidence: **99.31%**
1558. **`src/add-ons/print/transports/ipp/IppURLConnection.cpp`** -> AI Confidence: **99.31%**
1559. **`src/add-ons/print/transports/lpr/LprSetupDlg.cpp`** -> AI Confidence: **99.31%**
1560. **`src/add-ons/print/transports/lpr/LprTransport.cpp`** -> AI Confidence: **99.31%**
1561. **`src/add-ons/print/transports/lpr/LpsClient.cpp`** -> AI Confidence: **99.31%**
1562. **`src/add-ons/screen_savers/butterfly/Butterfly.cpp`** -> AI Confidence: **99.31%**
1563. **`src/add-ons/screen_savers/gravity/ConfigView.cpp`** -> AI Confidence: **99.31%**
1564. **`src/add-ons/screen_savers/leaves/Leaves.cpp`** -> AI Confidence: **99.31%**
1565. **`src/add-ons/screen_savers/message/Message.cpp`** -> AI Confidence: **99.31%**
1566. **`src/add-ons/screen_savers/nebula/Nebula.cpp`** -> AI Confidence: **99.31%**
1567. **`src/add-ons/screen_savers/shelf/Shelf.cpp`** -> AI Confidence: **99.31%**
1568. **`src/add-ons/screen_savers/slideshowsaver/SlideShowSaver.cpp`** -> AI Confidence: **99.31%**
1569. **`src/add-ons/screen_savers/spider/SpiderSaver.cpp`** -> AI Confidence: **99.31%**
1570. **`src/add-ons/tracker/mark_as/MarkAs.cpp`** -> AI Confidence: **99.31%**
1571. **`src/add-ons/translators/avif/AVIFTranslator.cpp`** -> AI Confidence: **99.31%**
1572. **`src/add-ons/translators/gif/GIFTranslator.cpp`** -> AI Confidence: **99.31%**
1573. **`src/add-ons/translators/hvif/HVIFTranslator.cpp`** -> AI Confidence: **99.31%**
1574. **`src/add-ons/translators/hvif/HVIFView.cpp`** -> AI Confidence: **99.31%**
1575. **`src/add-ons/translators/icns/ICNSTranslator.cpp`** -> AI Confidence: **99.31%**
1576. **`src/add-ons/translators/ico/ICOTranslator.cpp`** -> AI Confidence: **99.31%**
1577. **`src/add-ons/translators/pcx/PCXTranslator.cpp`** -> AI Confidence: **99.31%**
1578. **`src/add-ons/translators/png/PNGView.cpp`** -> AI Confidence: **99.31%**
1579. **`src/add-ons/translators/ppm/PPMMain.cpp`** -> AI Confidence: **99.31%**
1580. **`src/add-ons/translators/psd/PSDTranslator.cpp`** -> AI Confidence: **99.31%**
1581. **`src/add-ons/translators/raw/RAW.cpp`** -> AI Confidence: **99.31%**
1582. **`src/add-ons/translators/raw/RAWTranslator.cpp`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `src/servers/registrar/RosterSettingsCharStream.cpp` -> **99.9997%** Exposure
- `src/add-ons/kernel/drivers/disk/virtual/nbd/nbd-server.py` -> **0.0001%** Exposure
- `src/tests/kits/locale/catalogTest.cpp` -> **0.0001%** Exposure
- `src/tests/kits/locale/catalogTestAddOn.cpp` -> **0.0001%** Exposure
- `src/tests/system/libroot/posix/tst-mbrtowc.c` -> **0.0001%** Exposure
### Exploit Generation Surface
- `3rdparty/kallisti5/configure.py` -> **100.0%** Exposure
- `3rdparty/mmu_man/irc/Haiku/plugin.py` -> **100.0%** Exposure
- `src/add-ons/kernel/drivers/disk/virtual/nbd/nbd-server.py` -> **100.0%** Exposure
- `src/tools/checkstyle/checkstyle.py` -> **100.0%** Exposure
- `src/tools/generate_build_packages_repo.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `3rdparty/kallisti5/unmatched-uboot.sh` -> **100.0%** Exposure
- `3rdparty/mmu_man/scripts/HardwareChecker.sh` -> **100.0%** Exposure
- `src/tests/add-ons/kernel/file_systems/ext2/extents_test.sh` -> **100.0%** Exposure
- `src/tests/add-ons/kernel/file_systems/fat/fat_test.sh` -> **100.0%** Exposure
- `src/tests/system/benchmarks/compile_bench.sh` -> **100.0%** Exposure
### Raw Memory Manipulation
- `src/add-ons/kernel/drivers/graphics/neomagic/driver.c` -> **100.0%** Exposure
- `src/add-ons/kernel/drivers/graphics/via/driver.c` -> **100.0%** Exposure
- `headers/os/drivers/device_manager.h` -> **10.0%** Exposure
- `headers/os/drivers/fs_interface.h` -> **10.0%** Exposure
- `headers/private/fs_shell/fssh_fs_interface.h` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `configure` -> **100.0%** Exposure
- `3rdparty/kallisti5/configure.py` -> **100.0%** Exposure
- `3rdparty/mmu_man/irc/Haiku/plugin.py` -> **100.0%** Exposure
- `src/add-ons/kernel/drivers/disk/virtual/nbd/nbd-server.py` -> **100.0%** Exposure
- `src/tests/kits/net/netservices2/proxy.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `171` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `79183` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/add-ons/kernel/drivers/graphics/via/driver.c` (C) -> Cumulative Risk: **850.57**
- **Archetype:** `file_cluster_11` (Distance: 16.657 IQR)
- **Magnitude:** 930.16 | **LOC:** 976 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `eng_interrupt` (Impact: 309.1), `uninit_driver` (Impact: 18.6), `init_driver` (Impact: 17.4)

### 2. `src/bin/fwcontrol/fwdv.c` (C) -> Cumulative Risk: **842.62**
- **Archetype:** `file_cluster_13` (Distance: 13.883 IQR)
- **Magnitude:** 686.76 | **LOC:** 429 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `dvrecv` (Impact: 182.4), `dvsend` (Impact: 122.2)

### 3. `src/add-ons/kernel/drivers/graphics/neomagic/driver.c` (C) -> Cumulative Risk: **825.07**
- **Archetype:** `file_cluster_11` (Distance: 16.576 IQR)
- **Magnitude:** 726.92 | **LOC:** 1070 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `nm_interrupt` (Impact: 135.7), `init_driver` (Impact: 15.5), `init_hardware` (Impact: 15.0)

### 4. `src/bin/unzip/match.c` (C) -> Cumulative Risk: **812.53**
- **Archetype:** `file_cluster_11` (Distance: 15.11 IQR)
- **Magnitude:** 275.1 | **LOC:** 344 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.8128%)
- **Heaviest Functions:** `iswild` (Impact: 61.4), `main` (Impact: 44.4)

### 5. `src/add-ons/kernel/drivers/disk/nvme/libnvme/nvme_ns.c` (C) -> Cumulative Risk: **802.09**
- **Archetype:** `file_cluster_4` (Distance: 13.862 IQR)
- **Magnitude:** 957.34 | **LOC:** 712 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_nvme_ns_rw` (Impact: 76.5), `_nvme_ns_split_request` (Impact: 49.7), `nvme_ns_identify_update` (Impact: 20.3)

### 6. `src/add-ons/kernel/drivers/disk/nvme/libnvme/nvme_ctrlr.c` (C) -> Cumulative Risk: **798.74**
- **Archetype:** `file_cluster_4` (Distance: 12.989 IQR)
- **Magnitude:** 1241.32 | **LOC:** 1533 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `nvme_ctrlr_init` (Impact: 83.6), `nvme_ctrlr_map_cmb` (Impact: 44.9), `nvme_ioqp_get` (Impact: 33.4)

### 7. `src/add-ons/accelerants/via/engine/dac.c` (C) -> Cumulative Risk: **797.62**
- **Archetype:** `file_cluster_0` (Distance: 14.493 IQR)
- **Magnitude:** 669.26 | **LOC:** 723 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (98.1394%)
- **Heaviest Functions:** `eng_dac_sys_pll_find` (Impact: 148.7), `cle266_km400_dac_pix_pll_find` (Impact: 80.5), `eng_dac_mode` (Impact: 10.2)

### 8. `src/system/kernel/arch/arm64/arch_int.cpp` (CPP) -> Cumulative Risk: **785.63**
- **Archetype:** `file_cluster_13` (Distance: 13.649 IQR)
- **Magnitude:** 522.02 | **LOC:** 422 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `fixup_entry` (Impact: 87.0), `do_sync_handler` (Impact: 81.0), `InterruptScope` (Impact: 7.6)

### 9. `src/libs/compat/freebsd_wlan/net80211/ieee80211_ioctl.c` (C) -> Cumulative Risk: **783.69**
- **Archetype:** `file_cluster_13` (Distance: 14.226 IQR)
- **Magnitude:** 2101.76 | **LOC:** 3750 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `ieee80211_ioctl_get80211` (Impact: 493.1), `ieee80211_ioctl_setkey` (Impact: 413.8), `ieee80211_ioctl_getwpaie` (Impact: 36.8)

### 10. `src/bin/network/ping/ping6.c` (C) -> Cumulative Risk: **783.65**
- **Archetype:** `file_cluster_13` (Distance: 14.197 IQR)
- **Magnitude:** 2995.54 | **LOC:** 2831 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.9853%)
- **Heaviest Functions:** `ping6` (Impact: 1001.7), `pr_icmph` (Impact: 320.5), `get_pathmtu` (Impact: 54.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/system/libroot/posix/glibc/stdio-common/vfscanf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.172 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.962 IQR)
- **Top Global Matches:** file_cluster_8: 14.172, file_cluster_13: 14.333, file_cluster_11: 14.422
- **Magnitude:** 24347.76 | **LOC:** 2987 | **CtrlFlow:** 95.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (98.7088%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 26`, `args: 15`, `func_start: 2`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 1114`
* *Architecture:* `api: 193`, `import: 19`
* *Defense:* `safety: 30`, `test: 1`, `immutability_locks: 20`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` stdio_private.h, errno.h, stdarg.h, wchar.h, ctype.h, stdint.h, assert.h, stdio.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `headers/libs/glut/GL/glut.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_12` (Drift: 12.082 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.842 IQR)
- **Top Global Matches:** file_cluster_12: 12.082, file_cluster_8: 12.101, file_cluster_13: 12.625
- **Magnitude:** 11034.55 | **LOC:** 762 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (84.9019%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 205`, `args: 191`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 4`, `state_mutation: 101`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mesa_wgl.h, gl.h, glu.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/wlan/iaxwifi200/dev/pci/if_iwx.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.063 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.874 IQR)
- **Top Global Matches:** file_cluster_8: 15.063, file_cluster_13: 15.229, file_cluster_11: 15.256
- **Magnitude:** 9729.14 | **LOC:** 12292 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 257
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (11.681%)
**Top Internal Functions/Classes:**
  * `iwx_ioctl` (Impact: 987.4 | O(N^2) | DB: 257)
  * `iwx_sta_rx_agg` (Impact: 595.3 | O(N^2) | DB: 138)
  * `iwx_tx` (Impact: 232.0 | O(N^4) | DB: 79)
  * `iwx_add_sta_cmd` (Impact: 228.0 | O(2^N) | DB: 27)
  * `iwx_mld_modify_link_fill` (Impact: 101.9 | O(N^3) | DB: 33)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1276`, `structural_boundaries: 1331`, `args: 384`, `func_start: 138`, `class_start: 291`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 4214`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 11`, `orphaned_logic: 2`
* *Architecture:* `io: 11`, `api: 1338`, `import: 27`
* *Defense:* `safety: 24`, `immutability_locks: 49`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` endian.h, if_ether.h, device.h, if.h, bus.h, pcivar.h, ieee80211_priv.h, if_iwxreg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/kits/tracker/PoseView.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.656 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.849 IQR)
- **Top Global Matches:** file_cluster_8: 15.656, file_cluster_13: 15.767, file_cluster_11: 15.842
- **Magnitude:** 9486.32 | **LOC:** 10637 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 88.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 538
- **Risk Profile:** Cognitive Load (95.0863%), Tech Debt (66.7777%)
**Top Internal Functions/Classes:**
  * `BPoseView::SavePoseLocations` (Impact: 1632.2 | O(N^2) | DB: 536)
  * `BPoseView::FSNotification` (Impact: 1595.8 | O(N^2) | DB: 538)
  * `BPoseView::MoveSelectionInto` (Impact: 159.3 | O(N^1) | DB: 35)
  * `BPoseView::HandleDropCommon` (Impact: 117.4 | O(N^1) | DB: 57)
  * `BPoseView::CheckAutoScroll` (Impact: 77.8 | O(N^1) | DB: 39)
    * *Intent:* // remove last char from the typeahead buffer
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1553`, `structural_boundaries: 437`, `args: 431`, `func_start: 221`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 4897`, `dead_code: 18`, `planned_debt: 15`, `fragile_debt: 1`, `duplicate_logic: 16`, `orphaned_logic: 68`
* *Architecture:* `api: 2`, `import: 59`
* *Defense:* `safety: 1`, `sync_locks: 31`, `immutability_locks: 186`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` NodeMonitor.h, functional, Window.h, VolumeRoster.h, CountView.h, FSUtils.h, FilePanelPriv.h, InfoWindow.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/wlan/iprowifi4965/dev/iwn/if_iwn.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.752 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.757 IQR)
- **Top Global Matches:** file_cluster_8: 14.752, file_cluster_13: 14.971, file_cluster_7: 15.054
- **Magnitude:** 9025.16 | **LOC:** 9250 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 82
- **Risk Profile:** Cognitive Load (99.927%), Tech Debt (31.1736%)
**Top Internal Functions/Classes:**
  * `iwn_config_specific` (Impact: 688.7 | O(N^2) | DB: 71)
  * `iwn_notif_intr` (Impact: 134.9 | O(N^2) | DB: 30)
  * `iwn_tx_data` (Impact: 122.5 | O(N^1) | DB: 67)
    * *Intent:* /* * Process an RX_STATISTICS or BEACON_STATISTICS firmware notification. * The latter is sent by th...
  * `iwn_scan` (Impact: 116.0 | O(N^1) | DB: 82)
  * `iwn_read_firmware_tlv` (Impact: 100.2 | O(N^1) | DB: 26)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1404`, `structural_boundaries: 988`, `args: 205`, `func_start: 184`, `class_start: 258`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 4167`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 40`, `orphaned_logic: 15`
* *Architecture:* `io: 83`, `api: 951`, `import: 40`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 38`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` priv.h, ieee80211_regdomain.h, taskqueue.h, endian.h, if_ether.h, if_iwnvar.h, if.h, queue.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/wlan/idualwifi7260/dev/pci/if_iwm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.924 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.985 IQR)
- **Top Global Matches:** file_cluster_8: 14.924, file_cluster_13: 14.979, file_cluster_11: 15.001
- **Magnitude:** 8161.96 | **LOC:** 12375 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 458
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (13.4048%)
**Top Internal Functions/Classes:**
  * `iwm_check_rfkill` (Impact: 2070.9 | O(2^N) | DB: 458)
  * `iwm_clear_oactive` (Impact: 1174.6 | O(2^N) | DB: 324)
  * `iwm_read_firmware` (Impact: 424.8 | O(N^2) | DB: 71)
  * `iwm_rx_reorder` (Impact: 110.2 | O(N^1) | DB: 24)
  * `iwm_ampdu_tx_done` (Impact: 98.3 | O(N^2) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 877`, `structural_boundaries: 1136`, `args: 386`, `func_start: 123`, `class_start: 209`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 2731`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 8`, `orphaned_logic: 3`
* *Architecture:* `io: 8`, `api: 1075`, `import: 34`
* *Defense:* `safety: 22`, `immutability_locks: 70`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` endian.h, if_ether.h, device.h, if.h, bus.h, pcivar.h, ieee80211_priv.h, if_types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/ether/ipro1000/dev/e1000/e1000_ich8lan.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.213 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.871 IQR)
- **Top Global Matches:** file_cluster_8: 14.213, file_cluster_7: 14.38, file_cluster_13: 14.474
- **Magnitude:** 7461.96 | **LOC:** 6203 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 463
- **Risk Profile:** Cognitive Load (69.692%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `e1000_init_phy_workarounds_pchlan` (Impact: 3941.6 | O(2^N) | DB: 463)
  * `e1000_update_nvm_checksum_ich8lan` (Impact: 1181.5 | O(2^N) | DB: 110)
  * `e1000_phy_is_accessible_pchlan` (Impact: 43.1 | O(N^1) | DB: 18)
  * `e1000_toggle_lanphypc_pch_lpt` (Impact: 25.8 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 664`, `structural_boundaries: 411`, `args: 123`, `func_start: 66`, `class_start: 32`
* *Risk/State:* `state_mutation: 1694`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 527`, `import: 1`
* *Defense:* `doc: 66`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` e1000_api.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/ether/dec21xxx/dev/de/if_de.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.487 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.768 IQR)
- **Top Global Matches:** file_cluster_8: 14.487, file_cluster_13: 14.611, file_cluster_7: 14.796
- **Magnitude:** 6862.1 | **LOC:** 5010 | **CtrlFlow:** 79.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 372
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (10.6178%)
**Top Internal Functions/Classes:**
  * `tulip_read_macaddr` (Impact: 4386.0 | O(2^N) | DB: 372)
  * `tulip_media_poll` (Impact: 483.6 | O(N^3) | DB: 256)
    * *Intent:* /* * Before we are sure this is the right media we need
  * `tulip_dequeue_mbuf` (Impact: 11.2 | O(N^1) | DB: 2)
  * `tulip_dma_map_rxbuf` (Impact: 5.9 | O(N^1) | DB: 5)
  * `tulip_dma_map_addr` (Impact: 5.0 | O(N^1) | DB: 2)
    * *Intent:* /* * This turns on all sort of debugging stuff and make the * driver much larger. */ #define TULIP_D...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 611`, `structural_boundaries: 161`, `args: 22`, `func_start: 38`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 2`, `state_mutation: 1726`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 188`, `import: 35`
* *Defense:* `safety: 3`, `immutability_locks: 71`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` endian.h, if_ether.h, if.h, if_devar.h, pmap.h, bus.h, resource.h, if_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libs/compat/freebsd_iflib/iflib.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.967 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.838 IQR)
- **Top Global Matches:** file_cluster_8: 14.967, file_cluster_13: 14.978, file_cluster_11: 15.174
- **Magnitude:** 6158.58 | **LOC:** 7285 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 513
- **Risk Profile:** Cognitive Load (93.3651%), Tech Debt (35.4802%)
**Top Internal Functions/Classes:**
  * `iflib_tx_desc_free` (Impact: 2598.3 | O(2^N) | DB: 513)
  * `iflib_parse_header` (Impact: 128.0 | O(N^3) | DB: 48)
  * `iflib_rxeof` (Impact: 44.6 | O(N^1) | DB: 44)
  * `iflib_parse_header_partial` (Impact: 43.0 | O(N^1) | DB: 31)
  * `iflib_add_device_sysctl_post` (Impact: 30.7 | O(N^1) | DB: 30)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 640`, `structural_boundaries: 370`, `args: 38`, `func_start: 89`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 2645`, `fragile_debt: 22`, `orphaned_logic: 7`
* *Architecture:* `io: 1`, `api: 422`, `concurrency: 8`, `import: 61`
* *Defense:* `safety: 5`, `doc: 6`, `sync_locks: 6`, `immutability_locks: 12`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` epoch.h, device_if.h, vnet.h, ip6.h, types.h, tcp.h, taskqueue.h, if_ether.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/system/kernel/fs/vfs.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.874 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.949 IQR)
- **Top Global Matches:** file_cluster_8: 14.874, file_cluster_13: 14.94, file_cluster_11: 15.076
- **Magnitude:** 6083.96 | **LOC:** 10260 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 84.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 363
- **Risk Profile:** Cognitive Load (81.7468%), Tech Debt (60.554%)
**Top Internal Functions/Classes:**
  * `get_file_system` (Impact: 1301.4 | O(N^2) | DB: 363)
  * `attr_open` (Impact: 294.5 | O(2^N) | DB: 75)
  * `entry_cache_remove` (Impact: 132.2 | O(N^1) | DB: 52)
  * `common_rename` (Impact: 70.5 | O(2^N) | DB: 11)
  * `publish_vnode` (Impact: 64.8 | O(2^N) | DB: 30)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 986`, `structural_boundaries: 820`, `args: 267`, `func_start: 181`, `class_start: 123`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 30`, `state_mutation: 3073`, `dead_code: 9`, `planned_debt: 12`, `duplicate_logic: 16`, `orphaned_logic: 38`
* *Architecture:* `api: 3`, `import: 54`
* *Defense:* `safety: 1`, `doc: 67`, `test: 2`, `sync_locks: 51`, `immutability_locks: 72`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` NodeMonitor.h, unistd.h, fs_interface.h, kernel_args.h, AutoDeleterDrivers.h, fd.h, syscalls.h, resource.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libs/libsolv/solv/solver.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.338 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.047 IQR)
- **Top Global Matches:** file_cluster_8: 14.338, file_cluster_13: 14.438, file_cluster_11: 14.54
- **Magnitude:** 6015.5 | **LOC:** 4234 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 418
- **Risk Profile:** Cognitive Load (95.3455%), Tech Debt (14.8047%)
**Top Internal Functions/Classes:**
  * `makeruledecisions` (Impact: 4219.7 | O(2^N) | DB: 418)
  * `solver_check_installsuppdepq_dep` (Impact: 90.2 | O(2^N) | DB: 9)
  * `autouninstall` (Impact: 37.5 | O(N^2) | DB: 17)
  * `enabledisablelearntrules` (Impact: 35.0 | O(2^N) | DB: 8)
  * `solver_dep_installed` (Impact: 21.4 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 762`, `structural_boundaries: 76`, `args: 2`, `func_start: 30`
* *Risk/State:* `state_mutation: 1370`, `dead_code: 6`, `fragile_debt: 5`, `orphaned_logic: 1`
* *Architecture:* `api: 183`, `import: 13`
* *Defense:* `safety: 8`, `doc: 4`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` unistd.h, poolarch.h, assert.h, stdio.h, stdlib.h, pool.h, util.h, solverdebug.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/system/libroot/posix/wcs_test.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.873 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.483 IQR)
- **Top Global Matches:** file_cluster_8: 14.873, file_cluster_7: 15.277, file_cluster_13: 15.318
- **Magnitude:** 5559.28 | **LOC:** 4043 | **CtrlFlow:** 94.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 149
- **Risk Profile:** Cognitive Load (75.3591%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_wcstok` (Impact: 115.6 | O(N^1) | DB: 133)
  * `test_wcschr` (Impact: 80.3 | O(N^1) | DB: 149)
  * `test_wcscpy` (Impact: 79.3 | O(N^1) | DB: 140)
  * `test_wcpcpy` (Impact: 79.3 | O(N^1) | DB: 140)
  * `test_wcscat` (Impact: 73.9 | O(N^1) | DB: 123)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 703`, `structural_boundaries: 44`, `args: 27`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4446`, `dead_code: 1`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 349`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` errno.h, wchar.h, stdio.h, stdlib.h, string.h, locale.h, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/wlan/ralinkwifi/dev/usb/wlan/if_run.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.384 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.833 IQR)
- **Top Global Matches:** file_cluster_8: 14.384, file_cluster_13: 14.526, file_cluster_7: 14.699
- **Magnitude:** 5327.96 | **LOC:** 6444 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 524
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (12.7592%)
**Top Internal Functions/Classes:**
  * `run_vap_create` (Impact: 2581.3 | O(N^3) | DB: 524)
    * *Intent:* /* stop all USB transfers */
  * `run_init_locked` (Impact: 153.2 | O(N^1) | DB: 27)
  * `run_rt3070_rf_setup` (Impact: 51.9 | O(N^1) | DB: 7)
  * `run_stop` (Impact: 35.2 | O(N^1) | DB: 18)
  * `run_rt5390_rf_init` (Impact: 31.1 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 661`, `structural_boundaries: 572`, `args: 181`, `func_start: 70`, `class_start: 117`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1900`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 9`
* *Architecture:* `io: 2`, `api: 346`, `import: 43`
* *Defense:* `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` if_runreg.h, if_runvar.h, ieee80211_regdomain.h, usbdi.h, endian.h, usb_debug.h, if_ether.h, in_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bin/mail_utils/spamdbm.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.498 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.76 IQR)
- **Top Global Matches:** file_cluster_8: 14.498, file_cluster_13: 14.657, file_cluster_7: 14.82
- **Magnitude:** 5324.46 | **LOC:** 7856 | **CtrlFlow:** 89.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 472
- **Risk Profile:** Cognitive Load (91.7653%), Tech Debt (18.5014%)
**Top Internal Functions/Classes:**
  * `ABSApp::LoadSaveDatabase` (Impact: 3068.0 | O(N^6) | DB: 472)
    * *Intent:* /* The scrolling display starts at this word. Since we can't use index
  * `ABSApp::InstallThings` (Impact: 173.8 | O(N^3) | DB: 46)
  * `ABSApp::EvaluatePositionIO` (Impact: 140.1 | O(N^6) | DB: 40)
  * `ABSApp::AddPositionIOToDatabase` (Impact: 123.3 | O(N^2) | DB: 48)
  * `TokenizerPassGetPlainWords` (Impact: 38.7 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 668`, `structural_boundaries: 76`, `args: 407`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 1710`, `fragile_debt: 6`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `import: 47`
* *Defense:* `doc: 6`, `sync_locks: 7`, `immutability_locks: 48`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` vector, Cursor.h, Mime.h, FindDirectory.h, View.h, Beep.h, string, Path.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libs/libsolv/solv/rules.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.444 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.145 IQR)
- **Top Global Matches:** file_cluster_8: 14.444, file_cluster_13: 14.519, file_cluster_11: 14.649
- **Magnitude:** 5265.6 | **LOC:** 3693 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 323
- **Risk Profile:** Cognitive Load (95.3395%), Tech Debt (11.5515%)
**Top Internal Functions/Classes:**
  * `jobtodisablelist` (Impact: 3416.9 | O(2^N) | DB: 323)
  * `solver_addrule` (Impact: 109.5 | O(2^N) | DB: 23)
  * `solver_addduprules` (Impact: 41.8 | O(N^2) | DB: 10)
    * *Intent:* /****************************************************************************** *** *** rpm rule par...
  * `add_obsoletes` (Impact: 26.2 | O(N^1) | DB: 11)
    * *Intent:* /* * n: Id of solvable * s: Pointer to solvable */
  * `unifyrules_sortcmp` (Impact: 21.9 | O(N^1) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 642`, `structural_boundaries: 80`, `args: 2`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1317`, `dead_code: 5`, `orphaned_logic: 7`
* *Architecture:* `api: 235`, `import: 14`
* *Defense:* `safety: 1`, `doc: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` unistd.h, poolarch.h, evr.h, assert.h, stdio.h, stdlib.h, pool.h, util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/ether/ipro1000/dev/e1000/e1000_phy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.099 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.676 IQR)
- **Top Global Matches:** file_cluster_8: 14.099, file_cluster_7: 14.255, file_cluster_13: 14.352
- **Magnitude:** 5240.4 | **LOC:** 4338 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 325
- **Risk Profile:** Cognitive Load (67.9529%), Tech Debt (13.2798%)
**Top Internal Functions/Classes:**
  * `e1000_phy_force_speed_duplex_m88` (Impact: 1901.5 | O(2^N) | DB: 325)
  * `e1000_copper_link_setup_m88` (Impact: 216.6 | O(2^N) | DB: 29)
    * *Intent:* /** * e1000_read_phy_reg_igp_locked - Read igp PHY register * @hw: pointer to the HW structure * @of...
  * `e1000_phy_setup_autoneg` (Impact: 137.2 | O(2^N) | DB: 19)
  * `e1000_copper_link_setup_igp` (Impact: 136.7 | O(2^N) | DB: 17)
    * *Intent:* /** * e1000_write_kmrn_reg_locked - Write kumeran register * @hw: pointer to the HW structure * @off...
  * `e1000_copper_link_setup_m88_gen2` (Impact: 84.0 | O(2^N) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 521`, `structural_boundaries: 471`, `args: 88`, `func_start: 88`, `class_start: 27`
* *Risk/State:* `state_mutation: 1444`, `fragile_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `io: 12`, `api: 546`, `import: 1`
* *Defense:* `doc: 88`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` e1000_api.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/ether/sis900/dev/sis/if_sis.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.79 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.616 IQR)
- **Top Global Matches:** file_cluster_8: 13.79, file_cluster_13: 13.916, file_cluster_7: 14.137
- **Magnitude:** 5215.0 | **LOC:** 2411 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 306
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (13.0697%)
**Top Internal Functions/Classes:**
  * `sis_miibus_statchg` (Impact: 4000.9 | O(2^N) | DB: 306)
    * *Intent:* /*
  * `sis_miibus_readreg` (Impact: 15.4 | O(N^1) | DB: 5)
  * `sis_read_cmos` (Impact: 13.5 | O(N^1) | DB: 6)
    * *Intent:* /*
  * `sis_miibus_writereg` (Impact: 12.9 | O(N^1) | DB: 3)
    * *Intent:* #endif /* * Read the MII serial port for the MII bit-bang module. */
  * `sis_find_bridge` (Impact: 10.8 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 245`, `args: 59`, `func_start: 47`, `class_start: 61`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 932`, `fragile_debt: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 150`, `concurrency: 1`, `import: 33`
* *Defense:* `sync_locks: 2`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` endian.h, if.h, bus.h, resource.h, if_var.h, pcivar.h, sysctl.h, if_types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/boot/efi/keys/DB.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/boot/efi/keys/DB.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/trust_db/haiku-2019.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/kits/interface/HaikuControlLook.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.729 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.679 IQR)
- **Top Global Matches:** file_cluster_8: 14.729, file_cluster_13: 15.127, file_cluster_7: 15.151
- **Magnitude:** 4915.76 | **LOC:** 3941 | **CtrlFlow:** 79.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (66.1495%), Tech Debt (99.1795%)
**Top Internal Functions/Classes:**
  * `HaikuControlLook::DrawActiveTab` (Impact: 116.4 | O(N^1) | DB: 50)
    * *Intent:* // DrawInactiveTab draws 2px border // draw tab frame wider to align B_PLAIN_BORDER with it
  * `HaikuControlLook::_DrawNonFlatButtonBack` (Impact: 101.5 | O(N^1) | DB: 53)
    * *Intent:* // 2 pixels for the separator
  * `HaikuControlLook::_DrawButtonFrame` (Impact: 97.9 | O(N^1) | DB: 54)
  * `HaikuControlLook::_DrawMenuFieldBackgrou` (Impact: 89.5 | O(N^1) | DB: 55)
  * `HaikuControlLook::DrawSplitter` (Impact: 87.5 | O(N^1) | DB: 46)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 128`, `args: 183`, `func_start: 90`
* *Risk/State:* `state_mutation: 3018`, `planned_debt: 2`, `duplicate_logic: 38`, `orphaned_logic: 51`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 245`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` LayoutUtils.h, Window.h, WindowPrivate.h, HaikuControlLook.h, GradientLinear.h, View.h, Control.h, Bitmap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/kits/net/netservices2/testserver.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.921 IQR)
- **Top Global Matches:** file_cluster_8: 8.707, file_cluster_13: 9.196, file_cluster_7: 9.32
- **Magnitude:** 4855.04 | **LOC:** 542 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.9402%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 74`, `args: 30`, `func_start: 30`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `io: 14`, `api: 27`, `import: 15`
* *Defense:* `safety: 4`, `doc: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` subprocess, hashlib, abc, zlib, http.server, sys, tempfile, ssl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/kits/net/service/testserver.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.921 IQR)
- **Top Global Matches:** file_cluster_8: 8.707, file_cluster_13: 9.196, file_cluster_7: 9.32
- **Magnitude:** 4855.04 | **LOC:** 542 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.9402%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 74`, `args: 30`, `func_start: 30`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `io: 14`, `api: 27`, `import: 15`
* *Defense:* `safety: 4`, `doc: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` subprocess, hashlib, abc, zlib, http.server, sys, tempfile, ssl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/file_systems/ntfs/libntfs/acls.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.99 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.594 IQR)
- **Top Global Matches:** file_cluster_8: 14.99, file_cluster_13: 15.165, file_cluster_11: 15.288
- **Magnitude:** 4528.38 | **LOC:** 4521 | **CtrlFlow:** 88.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 141
- **Risk Profile:** Cognitive Load (85.6991%), Tech Debt (12.745%)
**Top Internal Functions/Classes:**
  * `buildacls_posix` (Impact: 372.1 | O(N^2) | DB: 138)
  * `buildacls` (Impact: 324.7 | O(N^2) | DB: 141)
  * `ntfs_inherit_acl` (Impact: 110.0 | O(N^2) | DB: 63)
  * `ntfs_valid_posix` (Impact: 108.3 | O(N^1) | DB: 45)
  * `build_ownadmin_permissions` (Impact: 101.2 | O(N^2) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 681`, `structural_boundaries: 86`, `args: 22`, `func_start: 31`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 2424`, `dead_code: 1`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 347`, `import: 16`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 138`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` layout.h, acls.h, errno.h, unistd.h, syslog.h, misc.h, grp.h, fcntl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/system/libroot/posix/glibc/extensions/getopt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.462 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.012 IQR)
- **Top Global Matches:** file_cluster_8: 13.462, file_cluster_13: 13.641, file_cluster_11: 13.882
- **Magnitude:** 4448.06 | **LOC:** 818 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.2308%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 31`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 339`
* *Architecture:* `api: 59`, `import: 7`
* *Defense:* `safety: 1`, `test: 1`, `immutability_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` libintl.h, gettext.h, libc-symbols.h, unistd.h, stdio.h, stdlib.h, getopt.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/add-ons/media/plugins/ape_reader/MAClib/StartFilter.h` (CPP) | Magnitude: 221.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 130, indent_tabs: 86, branch: 22, func_start: 4
- `src/add-ons/media/plugins/ape_reader/MAClib/CircleBuffer.h` (CPP) | Magnitude: 22.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 28, state_mutation: 12, structural_boundaries: 8, args: 5
- `src/system/libroot/posix/musl/math/j0f.c` (C) | Magnitude: 269.8 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 186, indent_tabs: 84, indent_spaces: 65, branch: 27
- `src/system/libroot/posix/musl/math/j0.c` (C) | Magnitude: 262.58 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 178, indent_tabs: 84, indent_spaces: 65, branch: 27
- `src/add-ons/kernel/drivers/audio/ac97/auich/multi.c` (C) | Magnitude: 293.94 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 194, state_mutation: 176, pointers: 143, structural_boundaries: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/servers/bluetooth/LocalDeviceImpl.cpp` (CPP) | Magnitude: 1122.52 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 843, state_mutation: 491, pointers: 283, branch: 276
- `src/system/libroot/posix/musl/complex/csqrt.c` (C) | Magnitude: 76.48 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 37, state_mutation: 36, branch: 12, api: 11
- `headers/libs/agg/agg_renderer_scanline.h` (CPP) | Magnitude: 805.94 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 344, state_mutation: 276, structural_boundaries: 81, pointers: 51
- `src/add-ons/kernel/drivers/graphics/via/driver.c` (C) | Magnitude: 930.16 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 422, state_mutation: 421, pointers: 243, branch: 97
- `src/add-ons/translators/bmp/BMPTranslator.cpp` (CPP) | Magnitude: 1608.36 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 809, indent_tabs: 714, branch: 258, pointers: 146

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/add-ons/kernel/drivers/network/ether/pcnet/dev/le/am7990reg.h` (CPP) | Magnitude: 16.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: macros: 50, reflection_metaprogramming: 43, indent_tabs: 22, ownership: 6
- `headers/posix/arpa/nameser.h` (CPP) | Magnitude: 240.76 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 218, indent_tabs: 170, macros: 134, reflection_metaprogramming: 131
- `headers/libs/x86emu/x86emu/regs.h` (CPP) | Magnitude: 28.78 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 104, reflection_metaprogramming: 92, indent_spaces: 34, structural_boundaries: 28
- `headers/private/graphics/intel_extreme/intel_extreme.h` (CPP) | Magnitude: 119.3 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 559, reflection_metaprogramming: 556, indent_tabs: 369, args: 87
- `src/add-ons/kernel/drivers/network/ether/3com/dev/mii/bmtphyreg.h` (CPP) | Magnitude: 17.16 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: macros: 107, reflection_metaprogramming: 106, dead_code: 9, ownership: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/add-ons/kernel/file_systems/netfs/shared/AbstractConnection.cpp` (CPP) | Magnitude: 131.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 69, indent_tabs: 66, structural_boundaries: 18, branch: 17
- `src/add-ons/print/drivers/preview/PageSetupWindow.cpp` (CPP) | Magnitude: 251.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 197, state_mutation: 172, pointers: 79, args: 45
- `src/add-ons/screen_savers/butterfly/Butterfly.cpp` (CPP) | Magnitude: 120.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 77, indent_tabs: 76, branch: 13, pointers: 12
- `src/add-ons/screen_savers/debugnow/DebugNow.cpp` (CPP) | Magnitude: 37.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 38, state_mutation: 21, pointers: 21, args: 7
- `src/add-ons/translators/tga/TGAView.h` (CPP) | Magnitude: 16.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 11, pointers: 9, structural_boundaries: 6, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `headers/cpp/stl_function.h` (CPP) | Magnitude: 297.08 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 471, indent_spaces: 223, state_mutation: 164, immutability_locks: 160
- `headers/cpp/stl_construct.h` (CPP) | Magnitude: 20.42 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 36, func_start: 9, indent_spaces: 9, duplicate_logic: 8
- `headers/cpp/std/std_valarray.h` (CPP) | Magnitude: 276.62 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 371, indent_spaces: 278, state_mutation: 249, immutability_locks: 133
- `headers/cpp/std/gslice_array.h` (CPP) | Magnitude: 86.22 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 81, state_mutation: 68, immutability_locks: 60, indent_spaces: 55
- `src/kits/debugger/util/ArchivingUtils.h` (CPP) | Magnitude: 29.48 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 17, state_mutation: 14, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/add-ons/kernel/busses/scsi/usb/uninstall.sh` (SHELL) | Magnitude: 21.46 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 13, safety_bypasses: 5, branch: 4, structural_boundaries: 2
- `3rdparty/mmu_man/scripts/bootstrap-haiku.sh` (SHELL) | Magnitude: 3.56 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 30, io: 16, state_mutation: 15, structural_boundaries: 10
- `src/add-ons/kernel/drivers/audio/echo/generic/CChannelMask.h` (CPP) | Magnitude: 21.82 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 25, state_mutation: 19, args: 17, structural_boundaries: 15
- `src/tools/restest/OffsetFile.cpp` (CPP) | Magnitude: 0.09 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 48, indent_tabs: 47, branch: 16, func_start: 13
- `src/add-ons/kernel/drivers/audio/echo/generic/CChannelMask.cpp` (CPP) | Magnitude: 181.6 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 92, indent_tabs: 70, structural_boundaries: 16, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/system/libnetwork/netresolv/net/nsdispatch.c` (C) | Magnitude: 324.38 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 170, state_mutation: 141, pointers: 84, branch: 62
- `src/tests/add-ons/kernel/file_systems/fat/fat_test.sh` (SHELL) | Magnitude: 64.66 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 59, reflection_metaprogramming: 42, concurrency: 20, branch: 16
- `src/add-ons/kernel/drivers/disk/nvme/libnvme/nvme_ctrlr.c` (C) | Magnitude: 1241.32 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 637, state_mutation: 441, pointers: 299, structural_boundaries: 226
- `src/system/libnetwork/netresolv/resolv/res_state.c` (C) | Magnitude: 89.38 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 46, state_mutation: 37, pointers: 23, structural_boundaries: 21
- `src/add-ons/kernel/drivers/disk/nvme/libnvme/nvme_ns.c` (C) | Magnitude: 957.34 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 381, indent_tabs: 343, pointers: 290, api: 200

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `headers/os/media/Controllable.h` (CPP) | Magnitude: 20.98 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 44, indent_tabs: 37, args: 21, safety_bypasses: 19
- `3rdparty/mmu_man/scripts/dev-perso` (SHELL) | Magnitude: 122.28 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 102, branch: 59, structural_boundaries: 34, state_mutation: 15
- `src/add-ons/kernel/busses/scsi/usb/transform_procs.c` (C) | Magnitude: 500.96 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 290, branch: 169, api: 155, state_mutation: 144
- `src/system/kernel/arch/x86/64/signals_compat_asm.S` (ASSEMBLY) | Magnitude: 15.88 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 34, structural_boundaries: 27, dead_code: 27, branch: 5
- `src/bin/bfs_tools/lib/makefile` (MAKEFILE) | Magnitude: 15.4 | Delta: **0.228 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 17, dead_code: 9, doc: 6, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/add-ons/translators/gif/LoadPalette.h` (CPP) | Magnitude: 16.34 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 52, indent_tabs: 9, structural_boundaries: 2, args: 2
- `src/add-ons/translators/gif/SFHash.h` (CPP) | Magnitude: 18.52 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 52, indent_tabs: 15, structural_boundaries: 7, args: 3
- `src/add-ons/kernel/drivers/disk/nvme/libnvme/nvme.h` (C) | Magnitude: 222.34 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 411, api: 203, structural_boundaries: 158, pointers: 129
- `headers/libs/zydis/Zycore/Format.h` (C) | Magnitude: 32.12 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 72, api: 23, indent_spaces: 15, macros: 7
- `headers/libs/zydis/Zycore/Bitset.h` (C) | Magnitude: 55.1 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 137, api: 39, immutability_locks: 13, macros: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `headers/libs/agg/agg_rendering_buffer.h` (CPP) | Magnitude: 186.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 102, state_mutation: 91, structural_boundaries: 22, func_start: 18
- `src/add-ons/kernel/file_systems/netfs/client/ShareVolume.cpp` (CPP) | Magnitude: 2385.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 1455, indent_tabs: 1319, pointers: 483, branch: 312
- `src/add-ons/kernel/file_systems/packagefs/util/String.cpp` (CPP) | Magnitude: 30.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 21, indent_tabs: 12, pointers: 7, structural_boundaries: 4
- `src/add-ons/mail_daemon/inbound_protocols/pop3/POP3.h` (CPP) | Magnitude: 22.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 41, structural_boundaries: 10, args: 10, import: 9
- `src/add-ons/network_settings/dialup/MessageDriverSettingsUtils.h` (CPP) | Magnitude: 20.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 6, pointers: 6, state_mutation: 5, reflection_metaprogramming: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/add-ons/media/plugins/ape_reader/MAClib/MACLib.h` (CPP) | Magnitude: 75.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 508, indent_spaces: 72, state_mutation: 71, immutability_locks: 20
- `src/system/libroot/posix/locale/ctype_loc_global.cpp` (CPP) | Magnitude: 0.01 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 9, immutability_locks: 9, structural_boundaries: 4, func_start: 4
- `src/add-ons/kernel/file_systems/reiserfs/VNode.h` (CPP) | Magnitude: 37.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 31, structural_boundaries: 17, func_start: 13, immutability_locks: 12
- `src/tests/system/libroot/posix/dirent_test.cpp` (CPP) | Magnitude: 54.04 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 40, state_mutation: 24, pointers: 16, branch: 14
- `src/system/libnetwork/netresolv/net/protoent.h` (C) | Magnitude: 30.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 16, api: 15, class_start: 7, pointers: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/system/kernel/vm/vm.cpp` -> Churn: **100.0%** | Cog Load: 86.1311% | Debt: 95.9903%
- `src/kits/tracker/PoseView.cpp` -> Churn: **84.16%** | Cog Load: 95.0863% | Debt: 66.7777%
- `src/system/kernel/smp.cpp` -> Churn: **72.51%** | Cog Load: 70.7339% | Debt: 63.0268%
- `src/system/kernel/fs/vfs.cpp` -> Churn: **58.68%** | Cog Load: 81.7468% | Debt: 60.554%
- `src/kits/interface/HaikuControlLook.cpp` -> Churn: **57.79%** | Cog Load: 66.1495% | Debt: 99.1795%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/add-ons/kernel/drivers/network/wlan/iaxwifi200/dev/pci/if_iwx.c` -> **Augustin Cavalier** (100.0% isolated ownership) | Magnitude: 9729.14
- `src/kits/tracker/PoseView.cpp` -> **John Scipione** (88.2% isolated ownership) | Magnitude: 9486.32
- `src/add-ons/kernel/drivers/network/wlan/iprowifi4965/dev/iwn/if_iwn.c` -> **Augustin Cavalier** (100.0% isolated ownership) | Magnitude: 9025.16
- `src/add-ons/kernel/drivers/network/wlan/idualwifi7260/dev/pci/if_iwm.c` -> **Augustin Cavalier** (100.0% isolated ownership) | Magnitude: 8161.96
- `src/libs/compat/freebsd_iflib/iflib.c` -> **Augustin Cavalier** (100.0% isolated ownership) | Magnitude: 6158.58

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `headers/os/support/Archivable.h` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 99.9941%)
- `headers/os/app/Messenger.h` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 81.5795%)
- `headers/os/kernel/OS.h` -> **Severity: 0.004** (Bridge: 0.0001 * Flux: 63.7652%)
- `headers/os/media/MediaDefs.h` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 100.0%)
- `headers/os/media/MediaFormats.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.5668%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `headers/posix/inttypes.h` -> **Severity: 1644.897** (Blast Radius: 34.533 * Doc Risk: 47.6326%)
- `headers/os/support/SupportDefs.h` -> **Severity: 906.551** (Blast Radius: 76.051 * Doc Risk: 11.9203%)
- `headers/os/kernel/OS.h` -> **Severity: 554.829** (Blast Radius: 31.03 * Doc Risk: 17.8804%)
- `headers/os/interface/Rect.h` -> **Severity: 444.816** (Blast Radius: 6.582 * Doc Risk: 67.5806%)
- `headers/os/interface/Size.h` -> **Severity: 432.931** (Blast Radius: 4.536 * Doc Risk: 95.4433%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
