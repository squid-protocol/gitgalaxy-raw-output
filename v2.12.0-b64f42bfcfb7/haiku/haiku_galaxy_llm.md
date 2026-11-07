# ARCHITECTURAL_BRIEF: haiku
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/haiku/haiku.git` |
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
- **Scope:** 15554 analyzed artifact(s), 2806127 LOC.
- **Load-bearing artifact:** `headers/os/app/Message.h` -- 1174 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/libs/iconv/converters.h` -- pulls in 145 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/add-ons/kernel/drivers/network/wlan/idualwifi7260/dev/pci/if_iwm.c` at magnitude 10797.56 (structural weight, not risk).
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
| Total Artifacts | 26100 |
| Analyzed Artifacts (Scanned) | 15554 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10546 |
| Total LOC | 2806127 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 59.6% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7269 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0572 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 7.6519 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 925 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 11767 | 1972354 | 75.7% |
| C | 3333 | 800065 | 21.4% |
| ASSEMBLY | 263 | 13894 | 1.7% |
| PLAINTEXT | 71 | 1 | 0.5% |
| SHELL | 56 | 3048 | 0.4% |
| MARKDOWN | 13 | 0 | 0.1% |
| HTML | 11 | 4279 | 0.1% |
| MAKEFILE | 10 | 4860 | 0.1% |
| PYTHON | 10 | 1437 | 0.1% |
| YACC | 7 | 3919 | 0.0% |
| XML | 4 | 16 | 0.0% |
| JSON | 3 | 285 | 0.0% |
| GLSL | 2 | 42 | 0.0% |
| JAVASCRIPT | 2 | 1751 | 0.0% |
| BMS | 1 | 13 | 0.0% |
| OBJECTIVE-C | 1 | 163 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 3 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 15550 |
| cp1252 | cp1252-fallback | 2 |
| latin-1 | latin-1-fallback | 1 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 32%, Large Core Modules (3) 19%, Parameter Forwarders Files 9%, Interface Declarations Files 8%, Large Core Modules 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 15469 | 99.5% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 83 | 0.5% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10546*

**Composition by Extension & Reason:**
- `.catkeys`: 5250x Excluded (Unsupported Extension: '.catkeys'), 140x Unsupported Format (.catkeys), 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1530x Unsupported Format (.undeterminable), 769x Excluded (Binary Format Detected), 323x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 653x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Zero-Density Threshold (LOC: 51, Signals: 0), 1x Excluded (Lexical Monotony: High structural repetition detected in 3683 LOC)
- `.cpp`: 374x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 59106 hex tokens in 10427 LOC), 1x Excluded (Embedded Hex Payload: 6738 hex tokens in 654 LOC)
- `.rdef`: 319x Unsupported Format (.rdef), 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dox`: 228x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 119x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 5456 hex tokens in 556 LOC)
- `.png`: 118x Excluded (Explicitly Denied Extension: '.png')
- `.rst`: 112x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.keymap`: 69x Unsupported Format (.keymap)
- `.html`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 44 exceeds 500 chars), 1x Excluded (Saturation: Line 66 exceeds 500 chars)
- `.ld`: 31x Unsupported Format (.ld)
- `.sh`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Unsupported Format (.ini), 1x Excluded (Embedded Hex Payload: 3386 hex tokens in 1537 LOC), 1x Excluded (Embedded Hex Payload: 4064 hex tokens in 1895 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 22.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 37.0 | 52.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.6 | 1.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 85.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 62.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 36152 | 4919 | 6 | `src/servers/app/ServerApp.cpp` |
| cleanup | 4691 | 1433 | 0 | `src/add-ons/kernel/file_systems/ntfs/utils/mkntfs.c` |
| guards | 147512 | 11062 | 24 | `src/libs/zydis/Zydis/Generated/FormatterStrings.inc` |
| danger | 31047 | 4629 | 5 | `src/system/boot/platform/amiga_m68k/rom_calls.h` |
| concurrency | 6900 | 1341 | 0 | `src/system/kernel/locks/lock.cpp` |
| connectivity | 48006 | 8019 | 6 | `src/system/libroot/stubbed/libroot_stubs.c` |
| io | 3721 | 544 | 0 | `src/add-ons/kernel/network/stack/net_socket.cpp` |
| crypto | 5 | 3 | 0 | `src/tests/kits/net/netservices2/testserver.py` |
| ipc | 1281 | 476 | 0 | `src/add-ons/kernel/busses/usb/xhci.cpp` |
| time | 187 | 68 | 0 | `src/apps/poorman/libhttpd/libhttpd.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 94 | 26 | 0 | `configure` |
| events | 3560 | 658 | 0 | `src/add-ons/kernel/file_systems/userlandfs/kernel_add_on/Volume.cpp` |
| tests | 699 | 130 | 0 | `src/tests/system/libroot/posix/realtime_sem_test1.cpp` |
| docs | 12992 | 1485 | 0 | `src/libs/x86emu/ops.c` |
| debt | 25788 | 3810 | 4 | `src/tests/system/libroot/posix/wcs_test.cpp` |
| mutation | 574648 | 10065 | 92 | `src/libs/x86emu/ops.c` |
| dead_code | 77193 | 7120 | 13 | `src/system/libroot/stubbed/libroot_stubs.c` |
| credential | 19 | 12 | 0 | `src/tests/kits/net/service/DataTest.cpp` |
| threat | 18 | 11 | 0 | `src/add-ons/kernel/file_systems/fat/encodings.cpp` |
| ml_ai | 1153 | 435 | 0 | `src/tests/kits/opengl/demos/gears/gears.c` |
| ui | 235 | 11 | 0 | `src/add-ons/kernel/drivers/graphics/nvidia/README.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/add-ons/kernel/network/stack/net_socket.cpp` (Hits: 316)
- `configure` (Hits: 228)
- `src/add-ons/kernel/busses/scsi/usb/ReadMe.html` (Hits: 154)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Message.h** (`headers/os/app/Message.h`) — 1174 inbound connections
2. **OS.h** (`headers/os/kernel/OS.h`) — 853 inbound connections
3. **SupportDefs.h** (`headers/os/support/SupportDefs.h`) — 850 inbound connections
4. **Rect.h** (`headers/os/interface/Rect.h`) — 658 inbound connections
5. **Catalog.h** (`headers/os/locale/Catalog.h`) — 632 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **converters.h** (`src/libs/iconv/converters.h`) — 145 outbound dependencies
2. **MainWindow.cpp** (`src/apps/icon-o-matic/MainWindow.cpp`) — 75 outbound dependencies
3. **if_ath.c** (`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/if_ath.c`) — 65 outbound dependencies
4. **iflib.c** (`src/libs/compat/freebsd_iflib/iflib.c`) — 64 outbound dependencies
5. **if_ath_descdma.c** (`src/add-ons/kernel/drivers/network/wlan/atheroswifi/dev/ath/if_ath_descdma.c`) — 60 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_IO_vfscanf_internal` **(Many-Argument Workhorses)** (@ `src/system/libroot/posix/glibc/stdio-common/vfscanf.c`) -> Impact: **1770.3** | LOC: 2714
  * *Intent:* Return the number of assignments made, or -1 for an input error. */ #ifdef COMPILE_WSCANF
- `borrow_from_hole` **(Many-Argument Workhorses)** (@ `src/add-ons/kernel/file_systems/ntfs/libntfs/attrib.c`) -> Impact: **1535.7** | LOC: 2881
  * *Intent:* /* * Borrow space from adjacent hole for appending data * The hole may have to be split so that the end of hole is not * affected by cluster allocatio...
- `ServerApp::_DispatchMessage` **(Many-Argument Workhorses)** (@ `src/servers/app/ServerApp.cpp`) -> Impact: **1147.0** | LOC: 3057
  * *Intent:* */
- `rge_attach` **(Many-Argument Workhorses)** (@ `src/add-ons/kernel/drivers/network/ether/rtl8125/dev/pci/if_rge.c`) -> Impact: **752.0** | LOC: 2079
  * *Intent:* #endif #ifdef __FreeBSD_version
- `PicturePlayer::_Play` **(Many-Argument Workhorses)** (@ `src/kits/interface/PicturePlayer.cpp`) -> Impact: **741.7** | LOC: 792
- `ns_sprintrrf` **(Many-Argument Workhorses)** (@ `src/system/libnetwork/netresolv/nameser/ns_print.c`) -> Impact: **738.0** | LOC: 987
  * *Intent:* /*% * Convert the fields of an RR into presentation format. * * return: *\li Number of characters written to buf, or -1 (check errno). */
- `OutlineView::Draw` **(Many-Argument Workhorses)** (@ `src/kits/interface/ColumnListView.cpp`) -> Impact: **725.7** | LOC: 1956
- `ieee80211_ioctl_set80211` **(Many-Argument Workhorses)** (@ `src/libs/compat/freebsd_wlan/net80211/ieee80211_ioctl.c`) -> Impact: **677.0** | LOC: 819
- `ar9300_attach` **(Many-Argument Workhorses)** (@ `src/add-ons/kernel/drivers/network/wlan/atheroswifi/contrib/ath_hal/ar9300/ar9300_attach.c`) -> Impact: **592.7** | LOC: 1842
  * *Intent:* /* * Attach for an AR9300 part. */
- `big5_2003_wctomb` **(Many-Argument Workhorses)** (@ `src/libs/iconv/big5_2003.h`) -> Impact: **576.1** | LOC: 207

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/kits/interface` | 107 | 52809.98 | 42.66% | 91.77% |
| `src/add-ons/kernel/file_systems/ntfs/libntfs` | 73 | 45322.86 | 31.77% | 16.67% |
| `src/libs/libsolv/solv` | 65 | 37921.84 | 37.9% | 21.82% |
| `src/libs/compat/freebsd_wlan/net80211` | 78 | 37298.92 | 36.71% | 45.63% |
| `headers/libs/agg` | 121 | 28215.38 | 42.68% | 33.9% |
| `src/libs/iconv` | 203 | 27059.54 | 39.31% | 1.37% |
| `src/libs/compat/openbsd_wlan/net80211` | 35 | 19246.36 | 45.06% | 24.79% |
| `src/system/kernel` | 33 | 16937.68 | 39.28% | 63.52% |
| `src/servers/app` | 95 | 16311.44 | 20.5% | 43.31% |
| `src/bin` | 105 | 15936.54 | 50.67% | 31.97% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `headers/cpp/stdiostream.h` -> **100.0%** Exposure
- `headers/cpp/stl_hash_fun.h` -> **100.0%** Exposure
- `headers/cpp/stl_hash_map.h` -> **100.0%** Exposure
- `headers/cpp/stl_hash_set.h` -> **100.0%** Exposure
- `headers/cpp/strstream.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `headers/cpp/std/complext.cc` -> **100.0%** Exposure
- `headers/cpp/stl_algo.h` -> **100.0%** Exposure
- `headers/cpp/stl_numeric.h` -> **100.0%** Exposure
- `headers/libs/agg/agg_blur.h` -> **100.0%** Exposure
- `headers/libs/agg/agg_bounding_rect.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/system/libroot/stubbed/libroot_stubs.c` -> **2534** Orphaned Functions | **0** Duplicates
- `src/system/libroot/stubbed/libroot_stubs_legacy.c` -> **2496** Orphaned Functions | **0** Duplicates
- `src/kits/debugger/dwarf/DebugInfoEntries.cpp` -> **322** Orphaned Functions | **0** Duplicates
- `src/add-ons/kernel/file_systems/udf/UdfStructures.h` -> **0** Orphaned Functions | **234** Duplicates
- `src/kits/interface/View.cpp` -> **222** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/tests/apps/haikudepot/DataIOUtilsTest.cpp` -> **99.9995%** Exposure
- `src/tests/apps/haikudepot/JwtTokenHelperTest.cpp` -> **99.6391%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `97` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `75351` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/add-ons/kernel/drivers/network/wlan/idualwifi7260/dev/pci/if_iwm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.26)
- **Top Global Matches:** file_cluster_4: 6.26, file_cluster_6: 7.817, file_cluster_15: 13.962
- **Magnitude:** 10797.56 | **LOC:** 12375 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iwm_rx_pkt` **(Many-Argument Workhorses)** (Impact: 206.0)
  * `iwm_attach` **(Many-Argument Workhorses)** (Impact: 167.9)
    * *Intent:* #ifdef __FreeBSD_version
  * `iwm_tx` **(Many-Argument Workhorses)** (Impact: 154.2)
    * *Intent:* #define TB0_SIZE 16
  * `iwm_rx_reorder` **(Many-Argument Workhorses)** (Impact: 139.4)
    * *Intent:* /* * Handle re-ordering of frames which were de-aggregated in hardware. * Returns 1 if the MPDU was ...
  * `iwm_read_firmware` **(Compute Cores)** (Impact: 130.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 21 instances
* *Amplified Cascading Flux:* 1734 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 5525
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1803`, `structural_boundaries: 2205`, `args: 698`, `func_start: 268`, `class_start: 472`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 2057`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 24`, `unreferenced_by_name: 1`
* *Architecture:* `api: 525`, `import: 34`
* *Defense:* `safety: 40`, `immutability_locks: 92`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` if_iwmreg.h, if_iwmvar.h, pcireg.h, pcivar.h, bus.h, bpf.h, if.h, if_dl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/wlan/iaxwifi200/dev/pci/if_iwx.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.423)
- **Top Global Matches:** file_cluster_4: 6.423, file_cluster_6: 7.915, file_cluster_15: 14.107
- **Magnitude:** 10570.74 | **LOC:** 12292 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iwx_rx_pkt` **(Many-Argument Workhorses)** (Impact: 244.2)
  * `iwx_attach` **(Many-Argument Workhorses)** (Impact: 201.8)
    * *Intent:* #ifdef __FreeBSD_version
  * `iwx_read_firmware` **(Many-Argument Workhorses)** (Impact: 170.4)
    * *Intent:* #define IWX_FW_ADDR_CACHE_CONTROL 0xC0000000
  * `iwx_rx_reorder` **(Many-Argument Workhorses)** (Impact: 139.4)
    * *Intent:* /* * Handle re-ordering of frames which were de-aggregated in hardware. * Returns 1 if the MPDU was ...
  * `iwx_rx_frame` **(Many-Argument Workhorses)** (Impact: 115.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 22 instances
* *Amplified Cascading Flux:* 1706 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 5469
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1765`, `structural_boundaries: 2188`, `args: 766`, `func_start: 258`, `class_start: 473`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 2057`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 14`, `unreferenced_by_name: 1`
* *Architecture:* `api: 502`, `import: 27`
* *Defense:* `safety: 42`, `immutability_locks: 84`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` if_iwxreg.h, if_iwxvar.h, pcireg.h, pcivar.h, bus.h, bpf.h, if.h, if_dl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libs/x86emu/ops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.69)
- **Top Global Matches:** file_cluster_4: 6.69, file_cluster_16: 9.99, file_cluster_15: 11.534
- **Magnitude:** 8287.56 | **LOC:** 12308 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.3%), Complexity Load (formerly Cognitive Load) (47.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `x86emuOp_opcF7_word_RM` **(Many-Argument Workhorses)** (Impact: 172.5)
    * *Intent:* ****************************************************************************/
  * `x86emuOp_opcFF_word_RM` **(Compute Cores)** (Impact: 127.4)
    * *Intent:* ****************************************************************************/
  * `x86emuOp_opcF6_byte_RM` **(Compute Cores)** (Impact: 73.4)
    * *Intent:* ****************************************************************************/
  * `x86emuOp_opc81_word_RM_IMM` **(Compute Cores)** (Impact: 54.0)
    * *Intent:* ****************************************************************************/
  * `x86emuOp_opc83_word_RM_IMM` **(Compute Cores)** (Impact: 53.5)
    * *Intent:* ****************************************************************************/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1586 instances
* *State Mutation (weighted view):* 5250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1382`, `structural_boundaries: 700`, `args: 546`, `func_start: 245`
* *Risk/State:* `state_mutation: 2078`, `planned_debt: 1`, `fragile_debt: 13`
* *Architecture:* `import: 1`
* *Defense:* `doc: 247`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` x86emui.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/file_systems/ntfs/libntfs/attrib.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.396)
- **Top Global Matches:** file_cluster_8: 11.396, file_cluster_3: 15.156, file_cluster_6: 23.077
- **Magnitude:** 7850.26 | **LOC:** 7256 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **26**; blast radius 0.075; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.9%)
- **Documentation Coverage:** 40.6015% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `borrow_from_hole` **(Many-Argument Workhorses)** (Impact: 1535.7)
    * *Intent:* /* * Borrow space from adjacent hole for appending data * The hole may have to be split so that the ...
  * `ntfs_attr_pwrite_i` **(Many-Argument Workhorses)** (Impact: 288.9)
    * *Intent:* * @b: data buffer to write to disk * * This function will write @count bytes from data buffer @b to ...
  * `ntfs_non_resident_attr_expand_i` **(Many-Argument Workhorses)** (Impact: 285.9)
    * *Intent:* /** * ntfs_non_resident_attr_expand - expand a non-resident, open ntfs attribute * @na: non-resident...
  * `ntfs_external_attr_find` **(Many-Argument Workhorses)** (Impact: 252.0)
    * *Intent:* * this is the correct place to insert it into, and if there is not enough * space, the attribute sho...
  * `ntfs_attr_update_mapping_pairs_i` **(Many-Argument Workhorses)** (Impact: 175.8)
    * *Intent:* #define NTFS_VCN_DELETE_MARK -2 /** * ntfs_attr_update_mapping_pairs_i - see ntfs_attr_update_mappin...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 26 instances
* *Amplified Cascading Flux:* 962 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 2962
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1239`, `structural_boundaries: 320`, `args: 128`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 1038`, `planned_debt: 5`, `fragile_debt: 23`, `unreferenced_by_name: 22`
* *Architecture:* `io: 1`, `api: 48`, `import: 26`
* *Defense:* `safety: 5`, `doc: 48`, `immutability_locks: 96`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.000609 | `Ripple Effect (Closeness):` 0.031283
  * `Imports (Out-Degree: 34):` attrib.h, attrlist.h, bitmap.h, compat.h, compress.h, config.h, debug.h, device.h...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `src/add-ons/kernel/drivers/network/wlan/iprowifi4965/dev/iwn/if_iwn.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.552)
- **Top Global Matches:** file_cluster_4: 7.552, file_cluster_16: 11.316, file_cluster_6: 12.378
- **Magnitude:** 6892.82 | **LOC:** 9250 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iwn_config_specific` **(Many-Argument Workhorses)** (Impact: 405.0)
    * *Intent:* /* * Define specific configuration based on device id and subdevice id * pid : PCI device id */
  * `iwn_tx_data` **(Many-Argument Workhorses)** (Impact: 110.5)
  * `iwn_scan` **(Many-Argument Workhorses)** (Impact: 78.0)
  * `iwn_read_firmware_tlv` **(Many-Argument Workhorses)** (Impact: 72.2)
    * *Intent:* /* * Extract text and data sections from a TLV firmware image. */
  * `iwn4965_set_txpower` **(Many-Argument Workhorses)** (Impact: 68.1)
    * *Intent:* /* * Set TX power for current channel (each rate has its own power settings). * This function takes ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 1176 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 3853
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1199`, `structural_boundaries: 1513`, `args: 476`, `func_start: 203`, `class_start: 301`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 1501`, `planned_debt: 7`, `fragile_debt: 43`
* *Architecture:* `api: 1`, `import: 40`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 56`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 65):` if_iwn_chip_cfg.h, if_iwn_debug.h, if_iwn_devid.h, if_iwn_ioctl.h, if_iwnreg.h, if_iwnvar.h, pcireg.h, pcivar.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/file_systems/ntfs/libntfs/acls.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.567)
- **Top Global Matches:** file_cluster_3: 8.567, file_cluster_8: 16.521, file_cluster_6: 29.3
- **Magnitude:** 6607.46 | **LOC:** 4521 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.021; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.9%), Complexity Load (formerly Cognitive Load) (84.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ntfs_build_permissions_posix` **(Many-Argument Workhorses)** (Impact: 372.2)
    * *Intent:* #if POSIXACLS /* * Build Posix permissions from an ACL * returns a pointer to the requested permissi...
  * `buildacls_posix` **(Many-Argument Workhorses)** (Impact: 223.2)
    * *Intent:* * - grants to world (unless none) * - full privileges to administrator, always present * - full priv...
  * `buildacls` **(Many-Argument Workhorses)** (Impact: 221.6)
    * *Intent:* #endif /* POSIXACLS */
  * `ntfs_inherit_acl` **(Many-Argument Workhorses)** (Impact: 182.4)
    * *Intent:* /* * Copy the inheritable parts of an ACL * * Returns the size of the new ACL * or zero if nothing i...
  * `build_group_denials_grant` **(Many-Argument Workhorses)** (Impact: 169.8)
    * *Intent:* /* a grant ACE for group */ /* unless group-obj has the same rights as world */ /* but present if gr...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 1262 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 3908
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1029`, `structural_boundaries: 241`, `args: 49`, `func_start: 48`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 1384`, `planned_debt: 6`, `unreferenced_by_name: 16`
* *Architecture:* `api: 29`, `import: 16`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 181`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00026
  * `Imports (Out-Degree: 12):` acls.h, config.h, errno.h, fcntl.h, grp.h, layout.h, misc.h, pwd.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/system/kernel/fs/vfs.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.729)
- **Top Global Matches:** file_cluster_4: 5.729, file_cluster_15: 10.055, file_cluster_12: 10.69
- **Magnitude:** 6569.5 | **LOC:** 10260 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **55**; blast radius 0.086; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (67.0%), Guard Balance (formerly Safety Score) (65.0%)
- **Documentation Coverage:** 90.6344% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `common_fcntl` **(Many-Argument Workhorses)** (Impact: 170.5)
  * `fs_mount` **(Many-Argument Workhorses)** (Impact: 170.1)
    * *Intent:* // #pragma mark - General File System functions
  * `vnode_path_to_vnode` **(Many-Argument Workhorses)** (Impact: 146.6)
    * *Intent:* */
  * `common_file_io_vec_pages` **(Many-Argument Workhorses)** (Impact: 114.1)
    * *Intent:* */
  * `fs_unmount` **(Many-Argument Workhorses)** (Impact: 110.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 663 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 2032
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1539`, `structural_boundaries: 1492`, `args: 396`, `func_start: 331`, `class_start: 207`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 706`, `dead_code: 2`, `planned_debt: 18`, `fragile_debt: 1`, `unreferenced_by_name: 137`
* *Architecture:* `api: 3`, `import: 55`
* *Defense:* `doc: 146`, `test: 5`, `sync_locks: 116`, `immutability_locks: 176`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.086
  * `Choke Point (Betweenness):` 0.003664 | `Ripple Effect (Closeness):` 0.046862
  * `Imports (Out-Degree: 52):` vnode_store.h, AutoDeleter.h, AutoDeleterDrivers.h, EntryCache.h, IORequest.h, KPath.h, NodeMonitor.h, OS.h...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `src/add-ons/kernel/file_systems/ntfs/libntfs/security.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.4)
- **Top Global Matches:** file_cluster_8: 6.4, file_cluster_6: 12.97, file_cluster_4: 21.685
- **Magnitude:** 5760.94 | **LOC:** 5414 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **23**; blast radius 0.023; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%)
- **Documentation Coverage:** 88.2812% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `access_check_posix` **(Many-Argument Workhorses)** (Impact: 129.0)
    * *Intent:* #if POSIXACLS /* * Determine which access types to a file are allowed * according to the relation of...
  * `ntfs_set_posix_acl` **(Many-Argument Workhorses)** (Impact: 86.8)
    * *Intent:* #if POSIXACLS /* * Set a new access or default Posix ACL to a file * (or remove ACL if no input data...
  * `mergesecurityattr` **(Many-Argument Workhorses)** (Impact: 86.1)
    * *Intent:* /* * Merge a new security descriptor into the old one * and assign to designated file * * Returns TR...
  * `ntfs_get_posix_acl` **(Many-Argument Workhorses)** (Impact: 77.0)
    * *Intent:* /* * Get a Posix ACL * * returns size or -errno if there is a problem * if size was too small, no co...
  * `enter_cache` **(Many-Argument Workhorses)** (Impact: 76.0)
    * *Intent:* #else
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 48 instances
* *Amplified Cascading Flux:* 1065 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 3325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 910`, `structural_boundaries: 384`, `args: 100`, `func_start: 75`, `class_start: 72`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 1195`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 34`
* *Architecture:* `io: 8`, `api: 48`, `import: 23`
* *Defense:* `safety: 26`, `doc: 7`, `immutability_locks: 180`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000374
  * `Imports (Out-Degree: 27):` acls.h, attrib.h, bitmap.h, cache.h, compat.h, config.h, dir.h, errno.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/libs/compat/freebsd_iflib/iflib.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.029)
- **Top Global Matches:** file_cluster_4: 5.029, file_cluster_16: 9.839, file_cluster_6: 10.803
- **Magnitude:** 5716.4 | **LOC:** 7285 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **64**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (70.7%)
- **Documentation Coverage:** 89.7059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iflib_device_register` **(Many-Argument Workhorses)** (Impact: 101.7)
  * `iflib_if_ioctl` **(Many-Argument Workhorses)** (Impact: 99.2)
  * `iflib_parse_header` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `iflib_encap` **(Many-Argument Workhorses)** (Impact: 67.9)
  * `iflib_fl_refill` **(Many-Argument Workhorses)** (Impact: 57.2)
    * *Intent:* /** * iflib_fl_refill - refill an rxq free-buffer list * @ctx: the iflib context * @fl: the free lis...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 32 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1093 instances
* *Concurrency (weighted view):* 16
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 3470
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 812`, `structural_boundaries: 726`, `args: 254`, `func_start: 174`, `class_start: 139`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 1284`, `fragile_debt: 29`, `unreferenced_by_name: 37`
* *Architecture:* `api: 61`, `concurrency: 6`, `import: 64`
* *Defense:* `safety: 5`, `doc: 14`, `sync_locks: 12`, `immutability_locks: 20`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000193
  * `Imports (Out-Degree: 68):` led.h, netmap_kern.h, pci_iov.h, pci_private.h, pcireg.h, pcivar.h, device_if.h, ifdi_if.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/system/libroot/stubbed/libroot_stubs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.345)
- **Top Global Matches:** file_cluster_11: 5.345, file_cluster_2: 7.429, file_cluster_15: 7.807
- **Magnitude:** 5493.92 | **LOC:** 2710 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.0%), Connectivity (formerly Api Exposure) (19.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_Exit` **(Interface Declarations)** (Impact: 1.1)
  * `_IO_adjust_column` **(Interface Declarations)** (Impact: 1.1)
  * `_IO_adjust_wcolumn` **(Interface Declarations)** (Impact: 1.1)
  * `_IO_cleanup` **(Interface Declarations)** (Impact: 1.1)
  * `_IO_cookie_init` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2588`, `func_start: 2588`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 13`, `unreferenced_by_name: 2534`
* *Architecture:* `io: 10`, `api: 2588`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 4`, `sync_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` symbol_versioning.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/system/libroot/stubbed/libroot_stubs_legacy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.402)
- **Top Global Matches:** file_cluster_11: 5.402, file_cluster_2: 7.467, file_cluster_15: 7.844
- **Magnitude:** 5411.02 | **LOC:** 2705 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.0%), Connectivity (formerly Api Exposure) (19.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AddArray__Q28BPrivate8KMessagePCcUlPCvll` **(Interface Declarations)** (Impact: 1.1)
  * `AddData__Q28BPrivate8KMessagePCcUlPCvlb` **(Interface Declarations)** (Impact: 1.1)
  * `AddElement__Q28BPrivate13KMessageFieldPCvl` **(Interface Declarations)** (Impact: 1.1)
  * `AddElements__Q28BPrivate13KMessageFieldPCvll` **(Interface Declarations)** (Impact: 1.1)
  * `AddField__Q28BPrivate8KMessagePCcUllPQ28BPrivate13KMessageField` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2550`, `func_start: 2550`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 13`, `unreferenced_by_name: 2496`
* *Architecture:* `io: 10`, `api: 2550`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 4`, `sync_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` symbol_versioning.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/add-ons/kernel/drivers/network/wlan/ralinkwifi/dev/usb/wlan/if_run.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.496)
- **Top Global Matches:** file_cluster_6: 5.496, file_cluster_4: 10.493, file_cluster_8: 14.635
- **Magnitude:** 5036.28 | **LOC:** 6444 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_read_eeprom` **(Many-Argument Workhorses)** (Impact: 102.2)
  * `run_init_locked` **(Many-Argument Workhorses)** (Impact: 89.0)
  * `run_select_chan_group` **(Many-Argument Workhorses)** (Impact: 85.1)
  * `run_rx_frame` **(Many-Argument Workhorses)** (Impact: 85.0)
  * `run_rt3593_set_chan` **(Many-Argument Workhorses)** (Impact: 84.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 862 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 2741
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1012`, `structural_boundaries: 884`, `args: 466`, `func_start: 123`, `class_start: 172`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1017`, `planned_debt: 12`, `fragile_debt: 12`
* *Architecture:* `import: 43`
* *Defense:* `immutability_locks: 46`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 69):` usb.h, usb_debug.h, usbdi.h, if_runreg.h, if_runvar.h, bpf.h, ethernet.h, if.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/trust_db/haiku-2019.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/system/kernel/vm/vm.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.291)
- **Top Global Matches:** file_cluster_4: 7.291, file_cluster_6: 8.668, file_cluster_12: 13.686
- **Magnitude:** 4857.26 | **LOC:** 7007 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 95.5%
- **Blast Radius:** changing it is visible to **97** in-repo importer(s); it depends on **44**; blast radius 0.326; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%)
- **Documentation Coverage:** 93.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vm_create_anonymous_area` **(Many-Argument Workhorses)** (Impact: 365.6)
    * *Intent:* */
  * `vm_soft_fault` **(Many-Argument Workhorses)** (Impact: 168.5)
    * *Intent:* */
  * `_vm_map_file` **(Many-Argument Workhorses)** (Impact: 136.6)
    * *Intent:* */
  * `cut_area` **(Many-Argument Workhorses)** (Impact: 132.8)
    * *Intent:* */
  * `map_backing_store` **(Many-Argument Workhorses)** (Impact: 124.3)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 458 instances
* *State Mutation (weighted view):* 1459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1132`, `structural_boundaries: 601`, `args: 162`, `func_start: 180`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 543`, `dead_code: 2`, `planned_debt: 22`, `fragile_debt: 2`, `unreferenced_by_name: 74`
* *Architecture:* `api: 6`, `import: 44`
* *Defense:* `safety: 1`, `doc: 40`, `test: 7`, `sync_locks: 60`, `immutability_locks: 97`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.326
  * `Choke Point (Betweenness):` 0.002484 | `Ripple Effect (Closeness):` 0.04646
  * `Imports (Out-Degree: 50):` AutoDeleterDrivers.h, IORequest.h, KernelExport.h, OS.h, VMAddressSpaceLocking.h, VMAnonymousCache.h, VMAnonymousNoSwapCache.h, algorithm...
  * `Imported By (In-Degree: 97):` (Excluded from Brief to save tokens)

### `src/add-ons/kernel/drivers/network/ether/broadcom570x/dev/bge/if_bge.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.937)
- **Top Global Matches:** file_cluster_6: 5.937, file_cluster_4: 10.515, file_cluster_8: 15.024
- **Magnitude:** 4703.48 | **LOC:** 6864 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **39**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.9%), Guard Balance (formerly Safety Score) (72.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bge_attach` **(Many-Argument Workhorses)** (Impact: 269.8)
  * `bge_blockinit` **(Many-Argument Workhorses)** (Impact: 211.3)
  * `bge_ioctl` **(Many-Argument Workhorses)** (Impact: 105.9)
  * `bge_reset` **(Many-Argument Workhorses)** (Impact: 91.8)
  * `bge_encap` **(Many-Argument Workhorses)** (Impact: 82.0)
    * *Intent:* /* * Encapsulate an mbuf chain in the tx ring by coupling the mbuf data * pointers to descriptors. *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 747 instances
* *State Mutation (weighted view):* 2413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1096`, `structural_boundaries: 659`, `args: 217`, `func_start: 106`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 919`, `planned_debt: 2`, `fragile_debt: 32`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 39`
* *Defense:* `safety: 3`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 6.4e-05
  * `Imports (Out-Degree: 49):` if_bgereg.h, brgphyreg.h, mii.h, miivar.h, pcireg.h, pcivar.h, bus.h, resource.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/libs/libsolv/solv/solver.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.771)
- **Top Global Matches:** file_cluster_8: 5.771, file_cluster_6: 15.807, file_cluster_3: 21.096
- **Magnitude:** 4648.58 | **LOC:** 4234 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 0.035; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.7%)
- **Documentation Coverage:** 97.561% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `solver_run_sat` **(Many-Argument Workhorses)** (Impact: 571.5)
    * *Intent:* /*------------------------------------------------------------------- * * solver_run_sat * * all rul...
  * `solver_solve` **(Many-Argument Workhorses)** (Impact: 358.3)
    * *Intent:* /* * * solve job queue * */
  * `solver_get_recommendations` **(Many-Argument Workhorses)** (Impact: 138.0)
  * `makeruledecisions` **(Compute Cores)** (Impact: 120.8)
    * *Intent:* /* * make assertion rules into decisions * * Go through rules and add direct assertions to the decis...
  * `analyze` **(Many-Argument Workhorses)** (Impact: 106.5)
    * *Intent:* /********************************************************************/ /* Analysis */ /*------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 731 instances
* *State Mutation (weighted view):* 2238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1067`, `structural_boundaries: 369`, `args: 164`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 776`, `fragile_debt: 11`, `unreferenced_by_name: 19`
* *Architecture:* `api: 27`, `import: 13`
* *Defense:* `safety: 20`, `doc: 9`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.035
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000393
  * `Imports (Out-Degree: 23):` assert.h, bitmap.h, policy.h, pool.h, poolarch.h, solver.h, solver_private.h, solverdebug.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/add-ons/kernel/drivers/network/ether/dec21xxx/dev/de/if_de.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.337)
- **Top Global Matches:** file_cluster_6: 6.337, file_cluster_8: 11.253, file_cluster_4: 13.822
- **Magnitude:** 4598.94 | **LOC:** 5010 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tulip_srom_decode` **(Compute Cores)** (Impact: 124.1)
  * `tulip_media_poll` **(Many-Argument Workhorses)** (Impact: 123.5)
  * `tulip_read_macaddr` **(Compute Cores)** (Impact: 89.2)
    * *Intent:* /* * This deals with the vagaries of the address roms and the * brain-deadness that various vendors ...
  * `tulip_pci_attach` **(Compute Cores)** (Impact: 73.6)
  * `tulip_rx_intr` **(Compute Cores)** (Impact: 65.9)
    * *Intent:* #define DESC_STATUS(di) (((volatile tulip_desc_t *)((di)->di_desc))->d_status) #define DESC_FLAG(di)...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 905 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 2896
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 824`, `structural_boundaries: 356`, `args: 217`, `func_start: 82`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 1086`, `dead_code: 1`, `fragile_debt: 6`
* *Architecture:* `api: 7`, `import: 35`
* *Defense:* `safety: 3`, `immutability_locks: 152`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` ddb.h, dc21040reg.h, if_devar.h, pcireg.h, pcivar.h, bus.h, bus_dma.h, resource.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/kits/interface/TextView.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.162)
- **Top Global Matches:** file_cluster_4: 6.162, file_cluster_6: 8.496, file_cluster_15: 13.353
- **Magnitude:** 4581.48 | **LOC:** 6184 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **32**; blast radius 0.047; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.4%), Complexity Load (formerly Cognitive Load) (86.8%), Guard Balance (formerly Safety Score) (70.0%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BTextView::_HandleArrowKey` **(Many-Argument Workhorses)** (Impact: 164.5)
    * *Intent:* //! Handles when an arrow key is pressed.
  * `BTextView::_HandlePageKey` **(Many-Argument Workhorses)** (Impact: 124.7)
    * *Intent:* //! Handles when the Page Up, Page Down, Home, or End key is pressed.
  * `BTextView::MessageReceived` **(Compute Cores)** (Impact: 118.3)
  * `BTextView::_DrawLine` **(Many-Argument Workhorses)** (Impact: 105.2)
  * `BTextView::_FindLineBreak` **(Many-Argument Workhorses)** (Impact: 81.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 581 instances
* *State Mutation (weighted view):* 1859
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1229`, `structural_boundaries: 352`, `args: 255`, `func_start: 207`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 697`, `dead_code: 2`, `planned_debt: 12`, `fragile_debt: 1`, `unreferenced_by_name: 176`
* *Architecture:* `api: 2`, `import: 31`
* *Defense:* `doc: 30`, `sync_locks: 6`, `immutability_locks: 154`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 8.2e-05 | `Ripple Effect (Closeness):` 0.001442
  * `Imports (Out-Degree: 32):` Alignment.h, Application.h, Beep.h, Bitmap.h, Clipboard.h, ControlLook.h, Debug.h, Entry.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/bin/mail_utils/spamdbm.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.74)
- **Top Global Matches:** file_cluster_8: 7.74, file_cluster_6: 10.666, file_cluster_4: 18.827
- **Magnitude:** 4548.06 | **LOC:** 7856 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **47**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.7%)
- **Documentation Coverage:** 82.7957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ABSApp::ProcessScriptingMessage` **(Many-Argument Workhorses)** (Impact: 342.5)
    * *Intent:* with an "error" number and an "message" string with a description. */
  * `ABSApp::LoadSaveDatabase` **(Many-Argument Workhorses)** (Impact: 132.7)
    * *Intent:* */
  * `ABSApp::RecursivelyTokenizeMailComponent` **(Many-Argument Workhorses)** (Impact: 121.6)
    * *Intent:* their contents, up to the maximum depth specified. */
  * `CommanderLooper::ProcessArgs` **(Compute Cores)** (Impact: 99.3)
    * *Intent:* (so we can print the result). */
  * `ABSApp::AddPositionIOToDatabase` **(Many-Argument Workhorses)** (Impact: 93.5)
    * *Intent:* user. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 662 instances
* *State Mutation (weighted view):* 2267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1056`, `structural_boundaries: 328`, `args: 679`, `func_start: 92`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 943`, `dead_code: 1`, `fragile_debt: 13`, `unreferenced_by_name: 72`
* *Architecture:* `io: 7`, `api: 9`, `import: 47`
* *Defense:* `safety: 1`, `doc: 24`, `sync_locks: 8`, `immutability_locks: 117`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 50):` Alert.h, Application.h, Beep.h, Button.h, CheckBox.h, Cursor.h, Directory.h, Entry.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/libs/libsolv/solv/repodata.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.766)
- **Top Global Matches:** file_cluster_6: 6.766, file_cluster_4: 6.985, file_cluster_16: 14.955
- **Magnitude:** 4368.42 | **LOC:** 3328 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **15**; blast radius 0.031; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.4%)
- **Documentation Coverage:** 94.0639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dataiterator_step` **(Compute Cores)** (Impact: 174.1)
  * `repodata_serialize_key` **(Many-Argument Workhorses)** (Impact: 121.2)
    * *Intent:* /*********************************/ /* internalalize some key into incore/vincore data */
  * `repodata_search` **(Many-Argument Workhorses)** (Impact: 98.3)
    * *Intent:* /* search a specific repodata */
  * `repodata_set_deltalocation` **(Many-Argument Workhorses)** (Impact: 81.8)
    * *Intent:* /* XXX: medianr is currently not stored */
  * `repodata_set_location` **(Many-Argument Workhorses)** (Impact: 69.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 717 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 2311
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 799`, `structural_boundaries: 377`, `args: 111`, `func_start: 108`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 877`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 51`
* *Architecture:* `api: 86`, `import: 15`
* *Defense:* `safety: 4`, `doc: 11`, `immutability_locks: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.001069
  * `Imports (Out-Degree: 24):` assert.h, chksum.h, fnmatch.h, hash.h, pool.h, poolid_private.h, regex.h, repo.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/libs/compat/freebsd_wlan/net80211/ieee80211_ioctl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.827)
- **Top Global Matches:** file_cluster_6: 7.827, file_cluster_8: 10.96, file_cluster_4: 15.115
- **Magnitude:** 4265.94 | **LOC:** 3750 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ieee80211_ioctl_set80211` **(Many-Argument Workhorses)** (Impact: 677.0)
  * `ieee80211_ioctl_get80211` **(Many-Argument Workhorses)** (Impact: 321.6)
  * `ieee80211_ioctl` **(Many-Argument Workhorses)** (Impact: 95.3)
  * `setmlme_common` **(Many-Argument Workhorses)** (Impact: 73.8)
  * `ieee80211_ioctl_setchannel` **(Many-Argument Workhorses)** (Impact: 46.0)
    * *Intent:* /* * Old api for setting the current channel; this is * deprecated because channel numbers are ambig...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 661 instances
* *State Mutation (weighted view):* 2020
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 978`, `structural_boundaries: 790`, `args: 78`, `func_start: 69`, `class_start: 103`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 698`, `planned_debt: 8`, `fragile_debt: 57`
* *Architecture:* `api: 5`, `import: 22`
* *Defense:* `safety: 14`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` ethernet.h, if.h, if_dl.h, if_media.h, if_private.h, if_var.h, ieee80211_input.h, ieee80211_ioctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/system/libroot/posix/glibc/regex/regexec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.506)
- **Top Global Matches:** file_cluster_8: 6.506, file_cluster_6: 11.202, file_cluster_4: 19.788
- **Magnitude:** 4211.94 | **LOC:** 4327 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `re_search_internal` **(Many-Argument Workhorses)** (Impact: 329.7)
  * `check_node_accept_bytes` **(Many-Argument Workhorses)** (Impact: 174.4)
    * *Intent:* can only accept one byte. */
  * `group_nodes_into_DFAstates` **(Many-Argument Workhorses)** (Impact: 125.4)
    * *Intent:* /* Group all nodes belonging to STATE into several destinations.
  * `check_arrival` **(Many-Argument Workhorses)** (Impact: 109.6)
    * *Intent:* /* Check whether the node TOP_NODE at TOP_STR can arrive to the node
  * `build_trtable` **(Many-Argument Workhorses)** (Impact: 99.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 610 instances
* *State Mutation (weighted view):* 1850
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 842`, `structural_boundaries: 423`, `args: 147`, `func_start: 62`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 630`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 4`
* *Architecture:* `api: 26`, `import: 2`
* *Defense:* `safety: 38`, `immutability_locks: 168`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 6.4e-05
  * `Imports (Out-Degree: 7):` weight.h, shlib-compat.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/libs/libsolv/solv/rules.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.717)
- **Top Global Matches:** file_cluster_8: 7.717, file_cluster_3: 17.398, file_cluster_6: 19.463
- **Magnitude:** 4196.48 | **LOC:** 3693 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **14**; blast radius 0.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.7%), Guard Balance (formerly Safety Score) (77.3%)
- **Documentation Coverage:** 93.5897% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `solver_createcleandepsmap` **(Many-Argument Workhorses)** (Impact: 361.2)
    * *Intent:* * also remove B, as installing A will have pulled in B. * after this pass, we have a set of still in...
  * `solver_addrpmrulesforsolvable` **(Many-Argument Workhorses)** (Impact: 207.0)
    * *Intent:* * * Algorithm: 'visit all nodes of a graph'. The graph nodes are * solvables, the edges their depend...
  * `jobtodisablelist` **(Many-Argument Workhorses)** (Impact: 161.5)
  * `solver_ruleinfo` **(Many-Argument Workhorses)** (Impact: 125.8)
  * `solver_addchoicerules` **(Compute Cores)** (Impact: 103.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 613 instances
* *State Mutation (weighted view):* 1851
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1021`, `structural_boundaries: 360`, `args: 76`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 625`, `dead_code: 2`, `fragile_debt: 6`, `unreferenced_by_name: 22`
* *Architecture:* `api: 26`, `import: 14`
* *Defense:* `safety: 1`, `doc: 7`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000315
  * `Imports (Out-Degree: 24):` assert.h, bitmap.h, evr.h, policy.h, pool.h, poolarch.h, solver.h, solver_private.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/libs/zydis/Zydis/Decoder.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.908)
- **Top Global Matches:** file_cluster_8: 6.908, file_cluster_6: 11.536, file_cluster_4: 20.034
- **Magnitude:** 4184.3 | **LOC:** 5084 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 0.029; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.7%), Complexity Load (formerly Cognitive Load) (61.9%)
- **Documentation Coverage:** 53.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ZydisSetAVXInformation` **(Many-Argument Workhorses)** (Impact: 384.4)
    * *Intent:* * - Broadcast-factor (static and dynamic) * - Rounding-mode and SAE * - Mask mode * - Compressed 8-b...
  * `ZydisDecodeOperands` **(Many-Argument Workhorses)** (Impact: 293.8)
    * *Intent:* #endif #ifndef ZYDIS_MINIMAL_MODE
  * `ZydisSetOperandSizeAndElementInfo` **(Many-Argument Workhorses)** (Impact: 182.0)
    * *Intent:* #endif #ifndef ZYDIS_MINIMAL_MODE /** * Sets the operand-size and element-specific information for t...
  * `ZydisSetAttributes` **(Many-Argument Workhorses)** (Impact: 155.5)
    * *Intent:* #endif /* ------------------------------------------------------------------------------------------...
  * `ZydisCheckErrorConditions` **(Many-Argument Workhorses)** (Impact: 137.8)
    * *Intent:* /** * Checks for certain post-decode error-conditions. * * @param state A pointer to the `ZydisDecod...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 527 instances
* *State Mutation (weighted view):* 1715
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 977`, `structural_boundaries: 464`, `args: 118`, `func_start: 52`, `class_start: 3`
* *Risk/State:* `state_mutation: 661`, `dead_code: 5`, `planned_debt: 19`, `unreferenced_by_name: 3`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `doc: 60`, `immutability_locks: 142`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000257
  * `Imports (Out-Degree: 8):` LibC.h, Decoder.h, DecoderData.h, SharedData.h, Status.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/add-ons/kernel/file_systems/ntfs/utils/mkntfs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.092)
- **Top Global Matches:** file_cluster_6: 8.092, file_cluster_8: 13.728, file_cluster_4: 14.013
- **Magnitude:** 4110.42 | **LOC:** 4885 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.021; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 5.3435% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mkntfs_create_root_structures` **(I/O & Config Routines)** (Impact: 125.8)
    * *Intent:* /** * mkntfs_create_root_structures - */
  * `insert_positioned_attr_in_mft_record` **(Many-Argument Workhorses)** (Impact: 113.6)
    * *Intent:* /** * insert_positioned_attr_in_mft_record * * Create a non-resident attribute with a predefined on ...
  * `insert_non_resident_attr_in_mft_record` **(Many-Argument Workhorses)** (Impact: 110.4)
    * *Intent:* /** * insert_non_resident_attr_in_mft_record * * Return 0 on success and -errno on error. */
  * `mkntfs_attr_find` **(Many-Argument Workhorses)** (Impact: 85.1)
    * *Intent:* * * ntfs_attr_find() only searches the specified mft record and it ignores the * presence of an attr...
  * `mkntfs_override_vol_params` **(Many-Argument Workhorses)** (Impact: 85.0)
    * *Intent:* /** * mkntfs_override_vol_params - */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 67 instances
* *Amplified Cascading Flux:* 734 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 2436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 664`, `structural_boundaries: 304`, `args: 123`, `func_start: 57`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 968`, `dead_code: 4`, `planned_debt: 7`, `fragile_debt: 61`
* *Architecture:* `io: 6`, `api: 7`, `import: 34`
* *Defense:* `safety: 1`, `doc: 56`, `immutability_locks: 129`, `cleanup: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 8.6e-05
  * `Imports (Out-Degree: 30):` attrdef.h, attrib.h, bitmap.h, boot.h, bootsect.h, config.h, device.h, dir.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/preferences/datatranslations/DataTranslationsSettings.cpp` (CPP) | Magnitude: 20.52 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 24, import: 7, branch: 6, pointers: 6
- `src/system/boot/platform/next_m68k/devices.cpp` (CPP) | Magnitude: 10.16 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 9, structural_boundaries: 7, import: 7, func_start: 5
- `src/tests/kits/storage/BasicTest.h` (CPP) | Magnitude: 83.78 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 71, structural_boundaries: 28, branch: 20, api: 10
- `src/kits/package/solver/SolverProblemSolution.cpp` (CPP) | Magnitude: 30.96 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 60, immutability_locks: 13, func_start: 12, unreferenced_by_name: 12
- `src/apps/haikudepot/ui/WorkStatusView.cpp` (CPP) | Magnitude: 15.44 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 36, pointers: 18, import: 10, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/add-ons/kernel/file_systems/packagefs/indices/NameIndex.h` (CPP) | Magnitude: 16.62 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 21, indent_tabs: 18, args: 6, class_start: 5
- `src/tests/servers/input/view_input_device/ViewInputDevice.cpp` (CPP) | Magnitude: 59.12 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 59, structural_boundaries: 18, pointers: 18, state_mutation: 14
- `src/system/kernel/arch/arm/arch_timer_generic.cpp` (CPP) | Magnitude: 16.76 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 21, structural_boundaries: 11, func_start: 9, indent_spaces: 9
- `src/tests/add-ons/kernel/file_systems/shared/consistency_check/AdaptiveBuffering.h` (CPP) | Magnitude: 16.7 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 27, structural_boundaries: 7, pointers: 7, args: 2
- `src/apps/tv/VideoNode.h` (CPP) | Magnitude: 17.04 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 39, pointers: 24, structural_boundaries: 15, immutability_locks: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `src/tests/system/boot/loader/platform_mmu.cpp` (CPP) | Magnitude: 16.34 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 11, pointers: 10, safety_bypasses: 6
- `headers/private/kernel/arch/m68k/stage2_priv.h` (CPP) | Magnitude: 15.64 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: args: 22, structural_boundaries: 18, pointers: 14, safety_bypasses: 6
- `headers/private/kernel/arch/ppc/stage2_priv.h` (CPP) | Magnitude: 15.64 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: args: 22, structural_boundaries: 18, pointers: 14, safety_bypasses: 6
- `src/system/boot/loader/file_systems/fat/File.h` (CPP) | Magnitude: 3.68 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 20, indent_tabs: 19, pointers: 14, args: 7
- `src/system/kernel/arch/arm64/PMAPPhysicalPageMapper.h` (CPP) | Magnitude: 13.2 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 32, structural_boundaries: 24, args: 10, safety_bypasses: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/apps/cortex/TransportView/TransportWindow.cpp` (CPP) | Magnitude: 19.74 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 29, import: 8, branch: 6, func_start: 5
- `src/add-ons/kernel/file_systems/packagefs/package_links/PackageLinksDirectory.h` (CPP) | Magnitude: 4.9 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 8, args: 4, class_start: 3
- `src/apps/debugger/user_interface/gui/expression_eval_window/ExpressionEvaluationWindow.cpp` (CPP) | Magnitude: 217.5 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 326, pointers: 118, branch: 78, core_var_decl: 51
- `src/add-ons/kernel/busses/scsi/usb/proto_cbi.c` (C) | Magnitude: 157.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 125, pointers: 67, core_var_decl: 31, design_snake_case: 31
- `headers/libs/agg/agg_span_solid.h` (CPP) | Magnitude: 19.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, func_start: 4, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/add-ons/accelerants/et6x00/SetDisplayMode.c` (C) | Magnitude: 45.0 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 26, pointers: 13, branch: 10, state_mutation: 10
- `src/add-ons/accelerants/radeon/CP.h` (C) | Magnitude: 16.82 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 23, pointers: 18, structural_boundaries: 12, state_mutation: 8
- `src/libs/bsd/daemon.c` (C) | Magnitude: 36.94 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 35, branch: 8, structural_boundaries: 6, pointers: 6
- `src/add-ons/kernel/busses/scsi/usb/proto_bulk.c` (C) | Magnitude: 200.76 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 185, pointers: 114, branch: 40, structural_boundaries: 39
- `src/add-ons/kernel/file_systems/ntfs/libntfs/ntfstime.h` (C) | Magnitude: 28.72 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 12, macros: 12, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `headers/os/arch/m68k/arch_debugger.h` (CPP) | Magnitude: 15.48 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 19, macros: 2, structural_boundaries: 1, class_start: 1
- `src/add-ons/kernel/file_systems/fat/bsd/sys/malloc.h` (C) | Magnitude: 3.96 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: macros: 6, memory_alloc: 5, structural_boundaries: 2, safety: 2
- `headers/os/drivers/pcmcia/ss.h` (CPP) | Magnitude: 16.66 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: macros: 39, reflection_metaprogramming: 38, indent_spaces: 29, structural_boundaries: 18
- `src/add-ons/translators/ico/ConfigView.cpp` (CPP) | Magnitude: 3.62 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 34, import: 9, memory_alloc: 7, args: 5
- `headers/private/kernel/boot/disk_identifier.h` (CPP) | Magnitude: 16.22 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 50, structural_boundaries: 16, macros: 3, reflection_metaprogramming: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/system/libroot/posix/glibc/libio/feof.c` (C) | Magnitude: 4.4 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 7, macros: 3, args: 2, import: 2
- `src/system/libroot/posix/glibc/libio/ferror.c` (C) | Magnitude: 4.4 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 7, macros: 3, args: 2, import: 2
- `headers/private/app/RegistrarDefs.h` (CPP) | Magnitude: 17.66 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 99, core_var_decl: 89, design_upper_case: 89, design_long_vars: 36
- `src/apps/icon-o-matic/style/CurrentColor.cpp` (CPP) | Magnitude: 9.0 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 5, import: 4, func_start: 3, unreferenced_by_name: 3
- `headers/private/package/hpkg/Stacker.h` (CPP) | Magnitude: 14.1 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 21, structural_boundaries: 6, pointers: 5, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/libs/compat/freebsd_network/dev/mii/mii.c` (C) | Magnitude: 486.28 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 318, pointers: 152, state_mutation: 88, structural_boundaries: 80
- `src/add-ons/print/transports/usb_port/USBTransport.cpp` (CPP) | Magnitude: 130.34 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 127, pointers: 86, branch: 41, structural_boundaries: 33
- `src/apps/diskusage/ControlsView.cpp` (CPP) | Magnitude: 188.84 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 208, branch: 58, pointers: 53, core_var_decl: 38
- `src/libs/compat/freebsd_wlan/net80211/ieee80211_action.c` (C) | Magnitude: 225.6 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 160, structural_boundaries: 56, branch: 54, pointers: 50
- `src/kits/debugger/debug_info/DwarfTypes.cpp` (CPP) | Magnitude: 666.02 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 731, pointers: 191, branch: 162, structural_boundaries: 156

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/add-ons/translators/raw/ReadHelper.h` (CPP) | Magnitude: 108.22 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 113, structural_boundaries: 59, branch: 24, func_start: 19
- `src/add-ons/kernel/file_systems/packagefs/indices/IndexImpl.h` (CPP) | Magnitude: 99.26 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 112, structural_boundaries: 85, pointers: 21, args: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/bin/package/command_dump.cpp` (CPP) | Magnitude: 138.44 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 134, branch: 45, structural_boundaries: 25, state_mutation: 15
- `src/add-ons/kernel/drivers/network/wlan/atheroswifi/contrib/ath_hal/ar9300/ar9300_eeprom.c` (C) | Magnitude: 34.59 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 2674, pointers: 759, branch: 663, state_mutation: 639
- `src/apps/icon-o-matic/gui/GradientControl.cpp` (CPP) | Magnitude: 520.48 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 415, branch: 129, state_mutation: 93, core_var_decl: 93
- `src/add-ons/kernel/drivers/graphics/intel_extreme/device.cpp` (CPP) | Magnitude: 195.44 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 224, branch: 46, structural_boundaries: 46, pointers: 41
- `src/preferences/appearance/ColorsView.cpp` (CPP) | Magnitude: 165.02 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 241, pointers: 71, branch: 54, core_var_decl: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/add-ons/kernel/bus_managers/scsi/scsi_internal.h` (CPP) | Magnitude: 19.5 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 92, pointers: 64, structural_boundaries: 47, macros: 18
- `src/add-ons/media/media-add-ons/usb_webcam/CamBufferedFilterInterface.cpp` (CPP) | Magnitude: 33.3 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 26, structural_boundaries: 20, func_start: 12, pointers: 12
- `headers/private/storage/ResourcesContainer.h` (CPP) | Magnitude: 16.64 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 18, immutability_locks: 10, structural_boundaries: 9, pointers: 8
- `src/apps/terminal/Shell.h` (CPP) | Magnitude: 10.7 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 32, structural_boundaries: 18, immutability_locks: 15, args: 10
- `headers/os/storage/Path.h` (CPP) | Magnitude: 17.16 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 45, immutability_locks: 39, structural_boundaries: 20, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/add-ons/kernel/drivers/network/wlan/aironetwifi/dev/an/if_an.c` (C) | Magnitude: 3179.9 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 2309, pointers: 1115, structural_boundaries: 636, state_mutation: 636

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/add-ons/kernel/drivers/network/ether/jmicron2x0/dev/mii/jmphy.c` (C) | Magnitude: 236.16 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 175, structural_boundaries: 54, state_mutation: 48, branch: 47
- `src/libs/libsolv/solv/chksum.c` (C) | Magnitude: 146.72 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 124, pointers: 64, structural_boundaries: 51, branch: 41
- `src/system/libroot/posix/musl/math/sincosl.c` (C) | Magnitude: 82.92 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 45, pointers: 22, scientific: 20, state_mutation: 19
- `src/add-ons/media/plugins/ape_reader/MAClib/NNFilter.cpp` (CPP) | Magnitude: 196.22 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 99, state_mutation: 43, branch: 31, pointers: 23
- `src/add-ons/kernel/drivers/network/wlan/realtekwifi/dev/rtwn/rtl8188e/r88e_chan.c` (C) | Magnitude: 167.0 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 63, state_mutation: 31, pointers: 29, branch: 28

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/system/kernel/vm/vm.cpp` -> Churn: **100.0%** | Cog Load: 76.914% | Debt: 56.3165%
- `src/kits/interface/HaikuControlLook.cpp` -> Churn: **62.06%** | Cog Load: 66.0904% | Debt: 64.9246%
- `src/kits/interface/PicturePlayer.cpp` -> Churn: **57.14%** | Cog Load: 27.7919% | Debt: 99.1427%
- `src/system/kernel/vm/vm_page.cpp` -> Churn: **57.14%** | Cog Load: 81.8994% | Debt: 42.6276%
- `src/system/kernel/vm/VMCache.cpp` -> Churn: **53.54%** | Cog Load: 34.0343% | Debt: 98.6851%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/add-ons/kernel/drivers/network/wlan/idualwifi7260/dev/pci/if_iwm.c` -> **Augustin Cavalier** (100.0% isolated ownership) | Magnitude: 10797.56
- `src/add-ons/kernel/drivers/network/wlan/iaxwifi200/dev/pci/if_iwx.c` -> **Augustin Cavalier** (100.0% isolated ownership) | Magnitude: 10570.74
- `src/add-ons/kernel/drivers/network/wlan/iprowifi4965/dev/iwn/if_iwn.c` -> **Augustin Cavalier** (100.0% isolated ownership) | Magnitude: 6892.82
- `src/libs/compat/freebsd_iflib/iflib.c` -> **Augustin Cavalier** (100.0% isolated ownership) | Magnitude: 5716.4
- `src/add-ons/kernel/drivers/network/wlan/ralinkwifi/dev/usb/wlan/if_run.c` -> **Augustin Cavalier** (100.0% isolated ownership) | Magnitude: 5036.28

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/add-ons/kernel/file_systems/bfs/Inode.cpp` -> **Severity: 0.409** (Bridge: 0.0041 * Flux: 99.9996%)
- `src/kits/app/Handler.cpp` -> **Severity: 0.39** (Bridge: 0.004 * Flux: 98.4601%)
- `src/system/kernel/fs/vfs.cpp` -> **Severity: 0.366** (Bridge: 0.0037 * Flux: 99.9861%)
- `src/system/kernel/thread.cpp` -> **Severity: 0.351** (Bridge: 0.0035 * Flux: 99.9829%)
- `src/system/kernel/locks/lock.cpp` -> **Severity: 0.263** (Bridge: 0.0026 * Flux: 99.9998%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `headers/os/support/SupportDefs.h` -> **Severity: 13.462** (Embedded: 0.2665 * Error Risk: 50.5154%)
- `headers/posix/sys/types.h` -> **Severity: 12.05** (Embedded: 0.235 * Error Risk: 51.2818%)
- `headers/os/kernel/OS.h` -> **Severity: 11.447** (Embedded: 0.2052 * Error Risk: 55.7913%)
- `headers/posix/sys/time.h` -> **Severity: 9.216** (Embedded: 0.1793 * Error Risk: 51.3885%)
- `headers/os/kernel/image.h` -> **Severity: 8.362** (Embedded: 0.1045 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `headers/os/support/SupportDefs.h` -> **Severity: 6119.6** (Blast Radius: 61.196 * Doc Risk: 100.0%)
- `headers/os/interface/Rect.h` -> **Severity: 581.3** (Blast Radius: 5.813 * Doc Risk: 100.0%)
- `headers/os/interface/Point.h` -> **Severity: 537.5** (Blast Radius: 5.375 * Doc Risk: 100.0%)
- `headers/os/support/Referenceable.h` -> **Severity: 484.5** (Blast Radius: 4.845 * Doc Risk: 100.0%)
- `headers/os/interface/GraphicsDefs.h` -> **Severity: 471.2** (Blast Radius: 4.712 * Doc Risk: 100.0%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 14336 literal sites + 422 sites through wrappers = 14758
- **`memory_alloc`:** 21159 literal sites + 19279 sites through wrappers = 40438
- **`panics_and_aborts`:** 3517 literal sites + 294 sites through wrappers = 3811

- `TRACE` (macro, memory_alloc, via PRINT): 4124 call sites in 445 files -- `headers/os/support/Debug.h`
- `LOG` (macro, memory_alloc, via PRINT): 2945 call sites in 102 files -- `headers/private/graphics/common/log_coll.h`
- `free` (macro, memory_alloc, primitive): 1936 call sites in 511 files -- `src/add-ons/kernel/file_systems/fat/bsd/sys/malloc.h`
- `malloc` (macro, memory_alloc, via _malloc): 898 call sites in 455 files -- `src/add-ons/kernel/file_systems/fat/bsd/sys/malloc.h`
- `KASSERT` (macro, memory_alloc, via ASSERT): 729 call sites in 147 files -- `src/add-ons/kernel/file_systems/fat/bsd/sys/kassert.h`
- `PRINT` (macro, memory_alloc, primitive): 696 call sites in 62 files -- `headers/private/bluetooth/debug.h`
- `ERROR` (macro, memory_alloc, via TRACE): 559 call sites in 100 files -- `headers/private/bluetooth/btDebug.h`
- `CALLED` (macro, memory_alloc, via TRACE): 530 call sites in 75 files -- `headers/private/bluetooth/btDebug.h`
- `RETURN_ERROR` (macro, memory_alloc, via TRETURN_ERROR): 508 call sites in 20 files -- `headers/private/file_systems/DebugSupport.h`
- `ASSERT` (macro, memory_alloc, via LOG): 497 call sites in 110 files -- `headers/os/support/Debug.h`
- `FUNCTION` (macro, memory_alloc, via TRACE): 291 call sites in 11 files -- `headers/private/file_systems/DebugSupport.h`
- `T` (macro, memory_alloc, primitive): 222 call sites in 13 files -- `src/add-ons/kernel/file_systems/bfs/BlockAllocator.cpp`
*(+747 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 414632 call pairs -- scoped 24.6%, unique 10.2%, ambiguous 41.1%, external 24.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 314502 | 26.7% | 5.9% | 48.4% | 19.1% |
| c | 98677 | 18.1% | 24.3% | 18.4% | 39.1% |
| python | 426 | 21.1% | 0.0% | 5.2% | 73.7% |
| shell | 379 | 10.8% | 0.0% | 0.0% | 89.2% |
| javascript | 296 | 8.4% | 0.0% | 0.0% | 91.6% |
| yacc | 278 | 0.0% | 21.6% | 39.9% | 38.5% |
| assembly | 74 | 63.5% | 12.2% | 6.8% | 17.6% |

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
