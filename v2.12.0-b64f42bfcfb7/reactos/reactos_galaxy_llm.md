# ARCHITECTURAL_BRIEF: reactos
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/reactos/reactos.git` |
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
- **Scope:** 16082 analyzed artifact(s), 5388955 LOC.
- **Load-bearing artifact:** `sdk/include/psdk/windef.h` -- 1702 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `sdk/lib/drivers/wdf/shared/inc/private/common/fxmin.hpp` -- pulls in 151 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `base/setup/reactos/treelist.c` at magnitude 17408.08 (structural weight, not risk).
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
| Total Artifacts | 28403 |
| Analyzed Artifacts (Scanned) | 16082 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 12321 |
| Total LOC | 5388955 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 56.6% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6479 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0888 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 964 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 11227 | 4596983 | 69.8% |
| CPP | 2849 | 730427 | 17.7% |
| PLAINTEXT | 1466 | 0 | 9.1% |
| ASSEMBLY | 328 | 29837 | 2.0% |
| XML | 58 | 0 | 0.4% |
| MAKEFILE | 26 | 716 | 0.2% |
| MARKDOWN | 23 | 0 | 0.1% |
| BATCH | 20 | 1840 | 0.1% |
| YACC | 19 | 16599 | 0.1% |
| HTML | 14 | 985 | 0.1% |
| SHELL | 11 | 337 | 0.1% |
| JAVASCRIPT | 11 | 7222 | 0.1% |
| PYTHON | 10 | 2316 | 0.1% |
| YAML | 9 | 443 | 0.1% |
| CSHARP | 3 | 62 | 0.0% |
| PERL | 2 | 1078 | 0.0% |
| RUST | 2 | 48 | 0.0% |
| OBJECTIVE-C | 2 | 14 | 0.0% |
| M4 | 1 | 1 | 0.0% |
| CSS | 1 | 47 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 231 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 15842 |
| cp1252 | cp1252-fallback | 227 |
| utf-8 | bom | 9 |
| latin-1 | latin-1-fallback | 4 |

> 2 guessed file(s) read as double-byte text that decodes strictly as shift_jis: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `base/setup/usetup/lang/ja-JP.h`, `base/setup/usetup/lang/uk-UA.h`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 25%, Data / Markup / Trivial 16%, Many-Argument Workhorses Files 14%, Large Core Modules (3) 11%, Parameter Forwarders Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 14593 | 90.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1489 | 9.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 12321*

**Composition by Extension & Reason:**
- `.rc`: 5033x Excluded (Unsupported Extension: '.rc'), 97x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.rc)
- `.bmp`: 1298x Excluded (Explicitly Denied Extension: '.bmp'), 1x Excluded (Explicitly Denied Extension: '.BMP')
- `.c`: 973x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 59x Excluded (Machine-Generated Source Code Signature: 13 LOC), 19x Excluded (Machine-Generated Source Code Signature: 15 LOC)
- `.ico`: 833x Excluded (Explicitly Denied Extension: '.ico')
- `.h`: 690x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Lexical Monotony: High structural repetition detected in 2658 LOC)
- `.spec`: 557x Excluded (Unsupported Extension: '.spec'), 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 187x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 139x Unsupported Format (.undeterminable), 1x Excluded (Lexical Monotony: High structural repetition detected in 2494 LOC)
- `.idl`: 330x Excluded (Unsupported Extension: '.idl')
- `.cpp`: 274x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 768 hex tokens in 746 LOC)
- `.txt`: 124x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 22x Excluded (Embedded Hex Payload: 1218 hex tokens in 621 LOC), 13x Excluded (Embedded Hex Payload: 1026 hex tokens in 525 LOC)
- `.rgs`: 177x Excluded (Unsupported Extension: '.rgs')
- `.mak`: 171x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nls`: 162x Excluded (Unsupported Extension: '.nls')
- `.inf`: 110x Excluded (Unsupported Extension: '.inf'), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 62x Excluded (Explicitly Denied Extension: '.ttf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 27.3 | 11.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.9 | 39.4 | 54.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 27.8 | 11.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 28.4 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.3 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 77.2 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 50.8 | 55.2 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 44.3 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 83.0 | 1.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 59.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 61.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 24144 | 3030 | 3 | `sdk/include/reactos/msgdump.h` |
| cleanup | 5303 | 786 | 0 | `dll/win32/msi/action.c` |
| guards | 214098 | 7687 | 30 | `dll/win32/wbemprox/builtin.c` |
| danger | 32428 | 3426 | 3 | `sdk/include/reactos/msgdump.h` |
| concurrency | 797 | 185 | 0 | `sdk/lib/drivers/wdf/shared/irphandlers/io/fxioqueue.cpp` |
| connectivity | 147603 | 10338 | 21 | `sdk/include/wine/winternl.h` |
| io | 2163 | 348 | 0 | `modules/rostests/winetests/msvcrt/file.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2517 | 268 | 0 | `modules/rostests/winetests/ws2_32/sock.c` |
| time | 336 | 93 | 0 | `sdk/include/ucrt/time.h` |
| serialization | 6 | 2 | 0 | `modules/rostests/winetests/jscript/api.js` |
| regex | 179 | 16 | 0 | `modules/rostests/winetests/jscript/regexp.js` |
| events | 4773 | 565 | 0 | `modules/rostests/winetests/dplayx/dplayx.c` |
| tests | 4163 | 240 | 0 | `modules/rostests/apitests/ntdll/RtlLocale.c` |
| docs | 39985 | 3202 | 3 | `sdk/include/reactos/x86x64/Intel/ArchitecturalMsr.h` |
| debt | 36895 | 4214 | 4 | `dll/win32/dbgeng/dbgeng.c` |
| mutation | 1230271 | 9546 | 196 | `modules/rostests/winetests/msxml3/domdoc.c` |
| dead_code | 53172 | 7699 | 8 | `modules/rosapps/applications/net/tsclient/porting-tools/rdesktop-core-tester/activex.cpp` |
| credential | 203 | 68 | 0 | `modules/rostests/winetests/msi/action.c` |
| threat | 409 | 48 | 0 | `modules/rostests/apitests/kernel32/MultiByteToWideChar.c` |
| ml_ai | 6776 | 935 | 0 | `sdk/include/vcruntime/xmmintrin.h` |
| ui | 441 | 126 | 0 | `modules/rostests/winetests/jscript/api.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `modules/rostests/winetests/msvcrt/file.c` (Hits: 247)
- `modules/rostests/winetests/ws2_32/sock.c` (Hits: 202)
- `modules/rostests/winetests/wininet/http.c` (Hits: 100)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **windef.h** (`sdk/include/psdk/windef.h`) — 1702 inbound connections
2. **except.c** (`dll/win32/kernel32/client/except.c`) — 1567 inbound connections
3. **heapmem.c** (`dll/win32/kernel32/client/heapmem.c`) — 1266 inbound connections
4. **isoboot.S** (`boot/freeldr/bootsect/isoboot.S`) — 1154 inbound connections
5. **debug.h** (`sdk/include/wine/debug.h`) — 1122 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **fxmin.hpp** (`sdk/lib/drivers/wdf/shared/inc/private/common/fxmin.hpp`) — 151 outbound dependencies
2. **muilanguages.h** (`base/setup/lib/muilanguages.h`) — 136 outbound dependencies
3. **fx.hpp** (`sdk/lib/drivers/wdf/kmdf/inc/private/fx.hpp`) — 117 outbound dependencies
4. **precomp.h** (`dll/win32/shell32/precomp.h`) — 87 outbound dependencies
5. **win32kp.h** (`win32ss/win32kp.h`) — 76 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `TreeListProc` **(Many-Argument Workhorses)** (@ `base/setup/reactos/treelist.c`) -> Impact: **1473.9** | LOC: 2645
  * *Intent:* //***************************************************************************** //* //* TreeListProc //* //*******************************************...
- `EDIT_EM_ReplaceSel` **(Many-Argument Workhorses)** (@ `dll/win32/comctl32/edit.c`) -> Impact: **1453.3** | LOC: 2344
  * *Intent:* /********************************************************************* * * EM_REPLACESEL * * FIXME: handle ES_NUMBER and ES_OEMCONVERT here * */
- `Ext2NtStatusToString` **(Compute Cores)** (@ `drivers/filesystems/ext2/src/debug.c`) -> Impact: **1396.3** | LOC: 1847
- `Ext2StatusToString` **(Compute Cores)** (@ `sdk/lib/fslib/ext2lib/Disk.c`) -> Impact: **1350.3** | LOC: 927
  * *Intent:* * PROGRAMMER: Matt Wu <mattwu@163.com> * HOMEPAGE: http://ext2.yeah.net */ /* INCLUDES **************************************************************/...
- `CreateProcessInternalW` **(Many-Argument Workhorses)** (@ `dll/win32/kernel32/client/proc.c`) -> Impact: **1239.0** | LOC: 2353
  * *Intent:* /* * @implemented */
- `main` **(Many-Argument Workhorses)** (@ `sdk/tools/mkisofs/schilytools/mkisofs/mkisofs.c`) -> Impact: **1031.0** | LOC: 1984
- `recv_udp` **(Many-Argument Workhorses)** (@ `drivers/network/tcpip/lwip/src/api/api_msg.c`) -> Impact: **952.9** | LOC: 1961
  * *Intent:* #endif /* LWIP_RAW*/ #if LWIP_UDP /** * Receive callback function for UDP netconns. * Posts the packet to conn->recvmbox or deletes it on memory error...
- `AtapiDmaInit` **(Many-Argument Workhorses)** (@ `drivers/storage/ide/uniata/id_dma.cpp`) -> Impact: **934.4** | LOC: 1384
- `shader_get_registers_used` **(Many-Argument Workhorses)** (@ `dll/directx/wine/wined3d/shader.c`) -> Impact: **912.3** | LOC: 836
  * *Intent:* /* Note that this does not count the loop register as an address register. */
- `insert_file_entry` **(Many-Argument Workhorses)** (@ `sdk/tools/mkisofs/schilytools/mkisofs/tree.c`) -> Impact: **844.4** | LOC: 1555
  * *Intent:* /* * Function: insert_file_entry * * Purpose: Insert one entry into our directory node. * * Note: * This function inserts a single entry into the dire...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `drivers/filesystems/btrfs` | 44 | 74012.88 | 56.07% | 19.3% |
| `dll/win32/comctl32` | 43 | 71779.06 | 54.1% | 30.6% |
| `dll/directx/wine/wined3d` | 32 | 61200.42 | 57.68% | 52.12% |
| `win32ss/user/ntuser` | 95 | 56378.3 | 37.81% | 35.54% |
| `dll/win32/msvcrt` | 50 | 52424.47 | 32.44% | 55.85% |
| `dll/opengl/mesa` | 115 | 51415.26 | 31.76% | 20.98% |
| `dll/win32/msi` | 47 | 48325.84 | 60.14% | 31.06% |
| `modules/rostests/winetests/kernel32` | 38 | 40152.32 | 52.99% | 12.41% |
| `modules/rostests/winetests/user32` | 27 | 39368.6 | 53.22% | 11.35% |
| `dll/win32/kernelbase/wine` | 19 | 38847.48 | 41.28% | 72.32% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `base/applications/mspaint/miniature.cpp` -> **100.0%** Exposure
- `base/ctf/msctf/context.cpp` -> **100.0%** Exposure
- `base/ctf/msctf/displayattributemgr.cpp` -> **100.0%** Exposure
- `base/ctf/msctf/langbarmgr.cpp` -> **100.0%** Exposure
- `base/ctf/msctf/range.cpp` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `sdk/lib/ucrt/string/amd64/strncat.s` -> **100.0%** Exposure
- `sdk/lib/ucrt/string/amd64/strncpy.s` -> **100.0%** Exposure
- `base/applications/atactl/atactl.cpp` -> **100.0%** Exposure
- `base/applications/charmap_new/GridView.cpp` -> **100.0%** Exposure
- `base/applications/drwtsn32/drwtsn32.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `modules/rosapps/applications/net/tsclient/porting-tools/rdesktop-core-tester/activex.cpp` -> **356** Orphaned Functions | **17** Duplicates
- `modules/rostests/winetests/gdi32/generated.c` -> **1** Orphaned Functions | **346** Duplicates
- `dll/opengl/mesa/api.c` -> **340** Orphaned Functions | **0** Duplicates
- `modules/rosapps/applications/net/tsclient/porting-tools/mstscax/mstscax.cpp` -> **283** Orphaned Functions | **12** Duplicates
- `dll/win32/browseui/shellbrowser.cpp` -> **267** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `modules/rostests/winetests/crypt32/base64.c` -> **60.9523%** Exposure
- `dll/win32/crypt32/base64.c` -> **31.1111%** Exposure
- `dll/win32/crypt32/rootstore.c` -> **26.5832%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `101` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `46620` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `base/setup/reactos/treelist.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.519)
- **Top Global Matches:** file_cluster_3: 11.519, file_cluster_8: 32.298, file_cluster_1: 38.246
- **Magnitude:** 17408.08 | **LOC:** 13734 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TreeListProc` **(Many-Argument Workhorses)** (Impact: 1473.9)
    * *Intent:* //***************************************************************************** //* //* TreeListProc...
  * `TreeListDraw` **(Many-Argument Workhorses)** (Impact: 538.6)
    * *Intent:* //***************************************************************************** //* //* TreeListDraw...
  * `TreeListMouseClick` **(Many-Argument Workhorses)** (Impact: 450.2)
    * *Intent:* //***************************************************************************** //* //* TreeListMous...
  * `TreeListKeyDown` **(Many-Argument Workhorses)** (Impact: 304.5)
    * *Intent:* //***************************************************************************** //* //* TreeListKeyD...
  * `TreeListInsertItem` **(Many-Argument Workhorses)** (Impact: 241.8)
    * *Intent:* //***************************************************************************** //* //* TreeListInse...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3363 instances
* *State Mutation (weighted view):* 10467
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2931`, `structural_boundaries: 834`, `args: 247`, `func_start: 66`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 3741`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 17`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 27):` malloc.h, reactos.h, stdio.h, string.h, tchar.h, treelist.h, windows.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dll/opengl/glu32/src/libutil/mipmap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.677)
- **Top Global Matches:** file_cluster_8: 9.677, file_cluster_6: 11.216, file_cluster_4: 19.04
- **Magnitude:** 14732.62 | **LOC:** 8943 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gluBuild3DMipmapLevelsCore` **(Many-Argument Workhorses)** (Impact: 795.2)
    * *Intent:* } /* for dd */ } /* halveImagePackedPixel3D() */
  * `gluBuild2DMipmapLevelsCore` **(Many-Argument Workhorses)** (Impact: 711.7)
    * *Intent:* /* To make swapping images less error prone */ #define __GLU_INIT_SWAP_IMAGE void *tmpImage #define ...
  * `empty_image` **(Many-Argument Workhorses)** (Impact: 313.8)
    * *Intent:* } /* else */ } /* fill_image() */ /* ** Insert array into user's data applying all pixel store modes...
  * `emptyImage3D` **(Many-Argument Workhorses)** (Impact: 290.3)
    * *Intent:* } /* for j */ } /* for i */ } /* for d */ } /* scaleInternal3D() */
  * `scale_internal_uint` **(Many-Argument Workhorses)** (Impact: 256.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 55 instances
* *Amplified Cascading Flux:* 2705 instances
* *Memory Alloc (weighted view):* 59
* *State Mutation (weighted view):* 8340
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1742`, `structural_boundaries: 738`, `args: 337`, `func_start: 103`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 246`, `state_mutation: 2930`, `dead_code: 18`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 188`, `doc: 2`, `immutability_locks: 533`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 6):` glu.h, assert.h, dlfcn.h, gluos.h, math.h, types.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dll/win32/msvcrt/scanf.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.794)
- **Top Global Matches:** file_cluster_17: 3.794, file_cluster_2: 5.807, file_cluster_15: 6.689
- **Magnitude:** 13538.97 | **LOC:** 744 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.026; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.0%), Guard Balance (formerly Safety Score) (77.0%), Debt Markers (formerly Tech Debt) (12.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 49`, `args: 32`, `func_start: 1`, `class_start: 6`
* *Risk/State:* `state_mutation: 150`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 4`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dll/win32/oleaut32/typelib.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.215)
- **Top Global Matches:** file_cluster_4: 8.215, file_cluster_6: 8.57, file_cluster_16: 14.972
- **Magnitude:** 10507.58 | **LOC:** 11652 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **20**; blast radius 0.157; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.2%)
- **Documentation Coverage:** 87.4644% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ITypeInfo_fnInvoke` **(Many-Argument Workhorses)** (Impact: 443.5)
  * `WMSFT_compile_typeinfo_aux` **(Many-Argument Workhorses)** (Impact: 172.5)
  * `DispCallFunc` **(Many-Argument Workhorses)** (Impact: 161.9)
  * `DispCallFunc` **(Many-Argument Workhorses)** (Impact: 123.2)
  * `DispCallFunc` **(Many-Argument Workhorses)** (Impact: 113.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1596 instances
* *State Mutation (weighted view):* 5115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1868`, `structural_boundaries: 993`, `args: 564`, `func_start: 301`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 1923`, `planned_debt: 28`, `fragile_debt: 84`, `unreferenced_by_name: 6`
* *Architecture:* `io: 4`, `api: 51`, `import: 20`
* *Defense:* `doc: 19`, `immutability_locks: 182`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 31):` ctype.h, lzexpand.h, objbase.h, stdarg.h, stdio.h, stdlib.h, string.h, typelib.h...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `dll/win32/comctl32/listview.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.371)
- **Top Global Matches:** file_cluster_6: 6.371, file_cluster_4: 10.951, file_cluster_8: 15.039
- **Magnitude:** 10349.02 | **LOC:** 12174 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (60.8%)
- **Documentation Coverage:** 34.0909% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LISTVIEW_WindowProc` **(Many-Argument Workhorses)** (Impact: 393.9)
    * *Intent:* /*** * DESCRIPTION: * Window procedure of the listview control. * */
  * `LISTVIEW_GetItemMetrics` **(Many-Argument Workhorses)** (Impact: 192.5)
    * *Intent:* * [I] lpLVItem : item to compute the measures for * [O] lprcBox : ptr to Box rectangle * Same as LVM...
  * `LISTVIEW_GetItemT` **(Many-Argument Workhorses)** (Impact: 189.1)
    * *Intent:* * lpLVItem->pszText to point to the text string. Please note * that this is not always possible (e.g...
  * `set_main_item` **(Many-Argument Workhorses)** (Impact: 145.7)
    * *Intent:* * DESCRIPTION: * Helper for LISTVIEW_SetItemT and LISTVIEW_InsertItemT: sets item attributes. * * PA...
  * `LISTVIEW_DrawItemPart` **(Many-Argument Workhorses)** (Impact: 139.3)
    * *Intent:* /* Draw main item or subitem */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1571 instances
* *State Mutation (weighted view):* 4958
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2153`, `structural_boundaries: 822`, `args: 350`, `func_start: 238`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 1816`, `planned_debt: 3`, `fragile_debt: 17`, `unreferenced_by_name: 2`
* *Architecture:* `api: 12`, `import: 16`
* *Defense:* `safety: 39`, `doc: 174`, `immutability_locks: 145`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 37):` assert.h, comctl32.h, commctrl.h, ctype.h, stdarg.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dll/win32/kernelbase/wine/locale.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.434)
- **Top Global Matches:** file_cluster_6: 7.434, file_cluster_4: 11.0, file_cluster_8: 16.14
- **Magnitude:** 9709.7 | **LOC:** 8377 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.1%), Complexity Load (formerly Cognitive Load) (64.3%), Debt Markers (formerly Tech Debt) (62.1%)
- **Documentation Coverage:** 33.0097% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_locale_info` **(Many-Argument Workhorses)** (Impact: 590.9)
    * *Intent:* /* get locale information from the locale.nls file */
  * `get_calendar_info` **(Many-Argument Workhorses)** (Impact: 269.8)
    * *Intent:* /* get calendar information from the locale.nls file */
  * `GetFileMUIInfo` **(Many-Argument Workhorses)** (Impact: 119.7)
    * *Intent:* /****************************************************************************** * GetFileMUIInfo (ke...
  * `format_number` **(Many-Argument Workhorses)** (Impact: 116.1)
    * *Intent:* /* format a positive number with decimal part; helper for get_number_format */
  * `get_date_format` **(Many-Argument Workhorses)** (Impact: 114.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1213 instances
* *State Mutation (weighted view):* 3729
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2052`, `structural_boundaries: 1210`, `args: 586`, `func_start: 237`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 1303`, `planned_debt: 2`, `fragile_debt: 23`, `unreferenced_by_name: 98`
* *Architecture:* `api: 130`, `import: 11`
* *Defense:* `doc: 129`, `immutability_locks: 403`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 22):` kernelbase.h, ntstatus.h, stdarg.h, stdlib.h, winbase.h, windef.h, debug.h, winnls.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dll/directx/wine/wined3d/glsl_shader.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.646)
- **Top Global Matches:** file_cluster_4: 7.646, file_cluster_6: 8.843, file_cluster_16: 13.986
- **Magnitude:** 9304.5 | **LOC:** 11981 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%)
- **Documentation Coverage:** 91.3183% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shader_glsl_get_register_name` **(Many-Argument Workhorses)** (Impact: 338.6)
    * *Intent:* /** Writes the GLSL variable name that corresponds to the register that the * DX opcode parameter is...
  * `shader_glsl_generate_ffp_fragment_shader` **(Many-Argument Workhorses)** (Impact: 302.0)
    * *Intent:* /* Context activation is done by the caller. */
  * `set_glsl_shader_program` **(Many-Argument Workhorses)** (Impact: 252.0)
    * *Intent:* /* Context activation is done by the caller. */
  * `shader_generate_glsl_declarations` **(Many-Argument Workhorses)** (Impact: 246.7)
    * *Intent:* /** Generate the variable & register declarations for the GLSL output target */
  * `shader_glsl_generate_pshader` **(Many-Argument Workhorses)** (Impact: 207.4)
    * *Intent:* /* Context activation is done by the caller. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1107 instances
* *State Mutation (weighted view):* 3589
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2134`, `structural_boundaries: 2081`, `args: 586`, `func_start: 304`, `class_start: 450`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 1375`, `planned_debt: 5`, `fragile_debt: 84`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 2`, `doc: 28`, `immutability_locks: 665`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` config.h, float.h, limits.h, stdio.h, port.h, wined3d_private.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/storage/ide/uniata/id_ata.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.652)
- **Top Global Matches:** file_cluster_8: 6.652, file_cluster_6: 11.763, file_cluster_4: 20.312
- **Magnitude:** 8897.06 | **LOC:** 11726 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 0.037; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AtapiInterrupt__` **(Many-Argument Workhorses)** (Impact: 642.2)
  * `AtapiStartIo__` **(Many-Argument Workhorses)** (Impact: 586.2)
  * `IssueIdentify` **(Many-Argument Workhorses)** (Impact: 434.1)
    * *Intent:* --*/
  * `AtapiSendCommand` **(Many-Argument Workhorses)** (Impact: 409.6)
    * *Intent:* --*/
  * `IdeSendCommand` **(Many-Argument Workhorses)** (Impact: 399.2)
    * *Intent:* #define SetCheckPoint(cp) { check_point = (cp) ; } #else #define SetCheckPoint(cp) #endif
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 1166 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 3911
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2151`, `structural_boundaries: 381`, `args: 484`, `func_start: 70`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 1579`, `dead_code: 182`, `planned_debt: 9`, `fragile_debt: 9`, `unreferenced_by_name: 13`
* *Architecture:* `io: 7`, `import: 1`
* *Defense:* `safety: 11`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 16):` stdafx.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `dll/directx/wine/d3dx9_36/mesh.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.792)
- **Top Global Matches:** file_cluster_6: 5.792, file_cluster_4: 10.102, file_cluster_8: 15.416
- **Magnitude:** 8526.86 | **LOC:** 7688 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.7%), Guard Balance (formerly Safety Score) (82.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 88.169% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `D3DXLoadMeshFromXInMemory` **(Many-Argument Workhorses)** (Impact: 280.4)
  * `D3DXLoadSkinMeshFromXof` **(Many-Argument Workhorses)** (Impact: 214.5)
  * `D3DXCreateTextW` **(Many-Argument Workhorses)** (Impact: 208.9)
  * `D3DXComputeTangentFrameEx` **(Many-Argument Workhorses)** (Impact: 204.8)
    * *Intent:* /************************************************************************* * D3DXComputeTangentFrame...
  * `d3dx9_mesh_OptimizeInplace` **(Many-Argument Workhorses)** (Impact: 155.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1414 instances
* *State Mutation (weighted view):* 4515
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1325`, `structural_boundaries: 908`, `args: 307`, `func_start: 158`, `class_start: 159`
* *Risk/State:* `safety_bypasses: 87`, `state_mutation: 1687`, `planned_debt: 5`, `fragile_debt: 36`, `unreferenced_by_name: 26`
* *Architecture:* `api: 45`, `import: 9`
* *Defense:* `safety: 4`, `doc: 14`, `immutability_locks: 151`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 20):` assert.h, d3dx9_private.h, dxfile.h, float.h, precomp.h, rmxfguid.h, rmxftmpl.h, list.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dll/win32/urlmon/uri.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.48)
- **Top Global Matches:** file_cluster_6: 6.48, file_cluster_4: 9.237, file_cluster_16: 16.349
- **Magnitude:** 8174.08 | **LOC:** 7329 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **6**; blast radius 0.061; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.8%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Uri_GetPropertyBSTR` **(Many-Argument Workhorses)** (Impact: 220.3)
  * `canonicalize_path_hierarchical` **(Many-Argument Workhorses)** (Impact: 195.8)
    * *Intent:* * start with a '/' then one is appended. * Ex: file://c:/test.mp3 -> file:///c:/test.mp3 * * 5). Dot...
  * `combine_uri` **(Many-Argument Workhorses)** (Impact: 177.2)
  * `Uri_GetPropertyLength` **(Many-Argument Workhorses)** (Impact: 143.2)
  * `compare_uris` **(Many-Argument Workhorses)** (Impact: 130.8)
    * *Intent:* /* Checks if the two Uri's are logically equivalent. It's a simple * comparison, since they are both...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1227 instances
* *State Mutation (weighted view):* 3762
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1684`, `structural_boundaries: 690`, `args: 296`, `func_start: 200`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1308`, `planned_debt: 2`, `fragile_debt: 22`, `unreferenced_by_name: 4`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `doc: 11`, `immutability_locks: 196`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 7):` limits.h, shlwapi.h, strsafe.h, urlmon_main.h, wchar.h, debug.h
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `dll/win32/gdiplus/graphics.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.361)
- **Top Global Matches:** file_cluster_4: 5.361, file_cluster_6: 9.988, file_cluster_16: 11.932
- **Magnitude:** 8148.84 | **LOC:** 7523 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **18**; blast radius 0.039; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (86.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.8%)
- **Documentation Coverage:** 94.8649% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GdipDrawImagePointsRect` **(Many-Argument Workhorses)** (Impact: 337.3)
  * `brush_fill_pixels` **(Many-Argument Workhorses)** (Impact: 226.6)
  * `gdip_format_string` **(Many-Argument Workhorses)** (Impact: 176.5)
  * `SOFTWARE_GdipDrawThinPath` **(Many-Argument Workhorses)** (Impact: 161.2)
  * `apply_image_attributes` **(Many-Argument Workhorses)** (Impact: 152.1)
    * *Intent:* /* returns preferred pixel format for the applied attributes */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1151 instances
* *State Mutation (weighted view):* 3772
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1348`, `structural_boundaries: 655`, `args: 244`, `func_start: 207`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 1470`, `planned_debt: 3`, `fragile_debt: 46`, `unreferenced_by_name: 97`
* *Architecture:* `api: 152`, `import: 18`
* *Defense:* `doc: 9`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 35):` gdiplus.h, gdiplus_private.h, limits.h, math.h, objbase.h, ocidl.h, ole2.h, olectl.h...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `drivers/filesystems/btrfs/flushthread.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.023)
- **Top Global Matches:** file_cluster_3: 9.023, file_cluster_8: 16.038, file_cluster_6: 28.78
- **Magnitude:** 8147.6 | **LOC:** 7947 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **6**; blast radius 0.037; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flush_fcb` **(Many-Argument Workhorses)** (Impact: 344.4)
  * `drop_chunk` **(Many-Argument Workhorses)** (Impact: 215.9)
  * `update_tree_extents` **(Many-Argument Workhorses)** (Impact: 210.0)
  * `try_tree_amalgamate` **(Many-Argument Workhorses)** (Impact: 151.7)
  * `rationalize_extents` **(Many-Argument Workhorses)** (Impact: 137.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1283 instances
* *State Mutation (weighted view):* 4173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1563`, `structural_boundaries: 802`, `args: 582`, `func_start: 75`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 1607`, `fragile_debt: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 21`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 32):` ata.h, btrfs_drv.h, crc32c.h, ntddscsi.h, ntddstor.h, xxhash.h
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `modules/rostests/winetests/user32/msg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.608)
- **Top Global Matches:** file_cluster_4: 7.608, file_cluster_6: 7.767, file_cluster_16: 14.166
- **Magnitude:** 7447.54 | **LOC:** 21055 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.021; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.4%), Complexity Load (formerly Cognitive Load) (30.0%)
- **Documentation Coverage:** 98.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ok_sequence_` **(Many-Argument Workhorses)** (Impact: 126.0)
  * `MsgCheckProc` **(Many-Argument Workhorses)** (Impact: 98.3)
    * *Intent:* /************* window procedures ********************/
  * `subtest_swp_paint_regions_` **(Many-Argument Workhorses)** (Impact: 98.1)
    * *Intent:* #define subtest_swp_paint_regions(w,p,c) subtest_swp_paint_regions_(__LINE__,w,p,c)
  * `test_PeekMessage` **(I/O & Config Routines)** (Impact: 86.1)
  * `add_message_` **(Many-Argument Workhorses)** (Impact: 73.8)
    * *Intent:* #define add_message(msg) add_message_(__LINE__,msg);
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 891 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 3966
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1406`, `structural_boundaries: 1041`, `args: 1650`, `func_start: 220`, `class_start: 82`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 2184`, `dead_code: 2`, `planned_debt: 30`, `fragile_debt: 18`
* *Architecture:* `io: 1`, `api: 7`, `import: 13`
* *Defense:* `safety: 3`, `doc: 20`, `immutability_locks: 466`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 57):` commctrl.h, dbt.h, imm.h, limits.h, stdarg.h, stdbool.h, stdio.h, winbase.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dll/win32/oleaut32/variant.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.157)
- **Top Global Matches:** file_cluster_3: 6.157, file_cluster_8: 23.423, file_cluster_6: 36.358
- **Magnitude:** 7242.78 | **LOC:** 5933 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **145** in-repo importer(s); it depends on **9**; blast radius 0.347; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.3%)
- **Documentation Coverage:** 5.098% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VARIANT_Coerce` **(Many-Argument Workhorses)** (Impact: 791.3)
    * *Intent:* /* Convert a variant from one type to another */
  * `VarSub` **(Many-Argument Workhorses)** (Impact: 368.4)
    * *Intent:* /********************************************************************** * VarSub [OLEAUT32.159] * * ...
  * `VarNumFromParseNum` **(Many-Argument Workhorses)** (Impact: 358.3)
    * *Intent:* * NOTES * - The smallest favoured type present in dwVtBits that can represent the * number in pNumpr...
  * `VarParseNumFromStr` **(Many-Argument Workhorses)** (Impact: 343.4)
    * *Intent:* * DISP_E_TYPEMISMATCH, if the string is not a number or is formatted * incorrectly. * DISP_E_OVERFLO...
  * `VarImp` **(Many-Argument Workhorses)** (Impact: 336.0)
    * *Intent:* /********************************************************************** * VarImp [OLEAUT32.154] * * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 771 instances
* *State Mutation (weighted view):* 2349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2131`, `structural_boundaries: 597`, `args: 373`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 807`, `planned_debt: 1`, `fragile_debt: 16`, `unreferenced_by_name: 25`
* *Architecture:* `api: 36`, `import: 9`
* *Defense:* `safety: 1`, `doc: 37`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.347
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 9):` resource.h, stdarg.h, stdlib.h, string.h, variant.h, winbase.h, windef.h, debug.h...
  * `Imported By (In-Degree: 145):` (Excluded from Brief to save tokens)

### `drivers/filesystems/btrfs/btrfs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.758)
- **Top Global Matches:** file_cluster_8: 5.758, file_cluster_6: 15.309, file_cluster_3: 21.666
- **Magnitude:** 7105.22 | **LOC:** 6555 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **13**; blast radius 0.054; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.3%), Guard Balance (formerly Safety Score) (78.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_debug_message` **(Many-Argument Workhorses)** (Impact: 789.6)
    * *Intent:* #define DEBUG_MESSAGE_LEN 1024 #ifdef DEBUG_LONG_MESSAGES
  * `_free_fcb` **(Many-Argument Workhorses)** (Impact: 633.3)
    * *Intent:* #ifdef DEBUG_FCB_REFCOUNTS
  * `mount_vol` **(Many-Argument Workhorses)** (Impact: 263.6)
  * `drv_cleanup` **(Many-Argument Workhorses)** (Impact: 115.5)
  * `load_chunk_root` **(Many-Argument Workhorses)** (Impact: 104.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 907 instances
* *State Mutation (weighted view):* 3032
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1114`, `structural_boundaries: 688`, `args: 502`, `func_start: 89`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 1218`, `dead_code: 10`, `planned_debt: 2`, `fragile_debt: 22`, `unreferenced_by_name: 13`
* *Architecture:* `api: 44`, `import: 15`
* *Defense:* `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.054
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 68):` ata.h, btrfs.h, btrfs_drv.h, cpuid.h, crc32c.h, initguid.h, intrin.h, ntdddisk.h...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `modules/rostests/winetests/ws2_32/sock.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.186)
- **Top Global Matches:** file_cluster_6: 6.186, file_cluster_4: 10.512, file_cluster_8: 15.299
- **Magnitude:** 6775.24 | **LOC:** 11861 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.021; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.2%), Complexity Load (formerly Cognitive Load) (66.4%)
- **Documentation Coverage:** 95.8647% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_events` **(Many-Argument Workhorses)** (Impact: 133.2)
    * *Intent:* #define ok_event_seq (winetest_set_location(__FILE__, __LINE__), 0) ? (void)0 : ok_event_sequence
  * `test_AcceptEx` **(I/O & Config Routines)** (Impact: 101.3)
  * `test_completion_port` **(I/O & Config Routines)** (Impact: 101.3)
  * `test_set_getsockopt` **(I/O & Config Routines)** (Impact: 65.8)
    * *Intent:* /* optname = SO_RCVTIMEO, SOSNDTIMEO */ #define SOCKTIMEOUT1 63000 /* 63 seconds. Do not test fracti...
  * `get_event_details` **(Stateful Encapsulated Methods)** (Impact: 47.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1062 instances
* *State Mutation (weighted view):* 4704
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 936`, `structural_boundaries: 773`, `args: 755`, `func_start: 120`, `class_start: 91`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 2580`, `planned_debt: 2`, `fragile_debt: 8`
* *Architecture:* `io: 202`, `api: 53`, `import: 12`
* *Defense:* `doc: 10`, `test: 7`, `immutability_locks: 51`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 32):` iphlpapi.h, mstcpip.h, mswsock.h, ntstatus.h, stdio.h, windows.h, test.h, winsock2.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/filesystems/btrfs/fsctl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.619)
- **Top Global Matches:** file_cluster_3: 10.619, file_cluster_8: 14.157, file_cluster_6: 26.798
- **Magnitude:** 6740.7 | **LOC:** 5958 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.4%), Guard Balance (formerly Safety Score) (81.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fsctl_oplock` **(Many-Argument Workhorses)** (Impact: 460.2)
  * `fsctl_request` **(Many-Argument Workhorses)** (Impact: 302.6)
  * `duplicate_extents` **(Many-Argument Workhorses)** (Impact: 301.1)
  * `fsctl_set_xattr` **(Many-Argument Workhorses)** (Impact: 221.7)
  * `mknod` **(Many-Argument Workhorses)** (Impact: 209.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 993 instances
* *State Mutation (weighted view):* 3201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1171`, `structural_boundaries: 698`, `args: 384`, `func_start: 53`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 1215`, `planned_debt: 71`, `fragile_debt: 11`, `unreferenced_by_name: 2`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 42):` btrfs_drv.h, btrfsioctl.h, crc32c.h, ntdddisk.h, ntddstor.h, stat.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `drivers/filesystems/btrfs/fileinfo.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.059)
- **Top Global Matches:** file_cluster_3: 9.059, file_cluster_8: 16.161, file_cluster_6: 28.88
- **Magnitude:** 6707.5 | **LOC:** 6067 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **2**; blast radius 0.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.5%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drv_set_information` **(Many-Argument Workhorses)** (Impact: 602.5)
  * `set_rename_information` **(Many-Argument Workhorses)** (Impact: 338.3)
  * `move_across_subvols` **(Many-Argument Workhorses)** (Impact: 269.2)
  * `rename_file_to_stream` **(Many-Argument Workhorses)** (Impact: 191.0)
  * `set_link_information` **(Many-Argument Workhorses)** (Impact: 181.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1009 instances
* *State Mutation (weighted view):* 3341
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1058`, `structural_boundaries: 479`, `args: 260`, `func_start: 44`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 1323`, `fragile_debt: 14`, `unreferenced_by_name: 4`
* *Architecture:* `api: 24`, `import: 2`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 24):` btrfs_drv.h, crc32c.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `win32ss/gdi/ntgdi/freetype.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 4.878)
- **Top Global Matches:** file_cluster_6: 4.878, file_cluster_4: 10.364, file_cluster_8: 14.244
- **Magnitude:** 6686.24 | **LOC:** 7659 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **6**; blast radius 0.113; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.2%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 94.0828% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IntExtTextOutW` **(Many-Argument Workhorses)** (Impact: 318.3)
  * `ftGdiGetGlyphOutline` **(Many-Argument Workhorses)** (Impact: 300.4)
    * *Intent:* /* * Based on WineEngGetGlyphOutline */
  * `GetFontPenalty` **(Many-Argument Workhorses)** (Impact: 171.2)
    * *Intent:* #define GOT_PENALTY(name, value) Penalty += (value) // NOTE: See Table 1. of https://learn.microsoft...
  * `FillTM` **(Many-Argument Workhorses)** (Impact: 162.6)
  * `IntGdiGetFontResourceInfo` **(Many-Argument Workhorses)** (Impact: 151.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1112 instances
* *State Mutation (weighted view):* 3590
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1109`, `structural_boundaries: 380`, `args: 600`, `func_start: 116`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 1366`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 17`, `unreferenced_by_name: 22`
* *Architecture:* `api: 55`, `import: 6`
* *Defense:* `doc: 8`, `test: 34`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 35):` debug.h, font.h, ftcalc.h, floatobj.h, utils.h, win32k.h
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `dll/win32/ole32/storage32.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.287)
- **Top Global Matches:** file_cluster_4: 5.287, file_cluster_16: 9.016, file_cluster_12: 10.051
- **Magnitude:** 6621.34 | **LOC:** 10426 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **15**; blast radius 0.077; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.4%), Complexity Load (formerly Cognitive Load) (57.0%)
- **Documentation Coverage:** 47.1471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `StgOpenStorage` **(Many-Argument Workhorses)** (Impact: 109.8)
    * *Intent:* /****************************************************************************** * StgOpenStorage [OL...
  * `OLECONVERT_LoadOLE10` **(Many-Argument Workhorses)** (Impact: 77.5)
    * *Intent:* * PARAMS * pOleStream [I] The OLESTREAM * pData [I] Data Structure for the OLESTREAM Data * * RETURN...
  * `StorageImpl_GrabLocks` **(Compute Cores)** (Impact: 75.1)
  * `StorageBaseImpl_CreateStorage` **(Many-Argument Workhorses)** (Impact: 70.8)
    * *Intent:* /************************************************************************ * StorageBaseImpl_CreateSt...
  * `StorageBaseImpl_CreateStream` **(Many-Argument Workhorses)** (Impact: 68.1)
    * *Intent:* /************************************************************************ * StorageBaseImpl_CreateSt...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 994 instances
* *State Mutation (weighted view):* 3228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1124`, `structural_boundaries: 616`, `args: 739`, `func_start: 247`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 70`, `state_mutation: 1240`, `planned_debt: 14`, `fragile_debt: 17`, `unreferenced_by_name: 16`
* *Architecture:* `api: 49`, `import: 15`
* *Defense:* `safety: 15`, `doc: 117`, `immutability_locks: 89`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 21):` assert.h, compobj_private.h, ole2.h, stdarg.h, stdio.h, stdlib.h, storage32.h, string.h...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `dll/win32/msi/action.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.517)
- **Top Global Matches:** file_cluster_4: 5.517, file_cluster_6: 10.652, file_cluster_16: 10.676
- **Magnitude:** 6573.0 | **LOC:** 7854 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **18**; blast radius 0.048; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.3%), Complexity Load (formerly Cognitive Load) (72.9%)
- **Documentation Coverage:** 99.0712% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MSI_SetFeatureStates` **(Compute Cores)** (Impact: 109.3)
  * `ITERATE_WriteEnvironmentString` **(Many-Argument Workhorses)** (Impact: 92.7)
  * `parse_prop` **(Many-Argument Workhorses)** (Impact: 84.6)
  * `ITERATE_RemoveEnvironmentString` **(Many-Argument Workhorses)** (Impact: 65.7)
  * `env_parse_flags` **(Many-Argument Workhorses)** (Impact: 59.9)
    * *Intent:* #define ENV_ACT_SETALWAYS 0x1 #define ENV_ACT_SETABSENT 0x2 #define ENV_ACT_REMOVE 0x4 #define ENV_A...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 205 instances
* *Amplified Cascading Flux:* 1142 instances
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 3590
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1229`, `structural_boundaries: 648`, `args: 275`, `func_start: 217`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1306`, `planned_debt: 1`, `fragile_debt: 32`, `unreferenced_by_name: 3`
* *Architecture:* `api: 29`, `import: 18`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 97`, `cleanup: 173`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.048
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 46):` imagehlp.h, mscoree.h, msidefs.h, msipriv.h, objbase.h, odbcinst.h, resource.h, shlobj.h...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `dll/win32/cryptui/main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.574)
- **Top Global Matches:** file_cluster_6: 6.574, file_cluster_4: 6.92, file_cluster_16: 14.231
- **Magnitude:** 6519.66 | **LOC:** 7608 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **19**; blast radius 0.035; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.1%), Complexity Load (formerly Cognitive Load) (67.4%)
- **Documentation Coverage:** 94.4206% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cert_mgr_dlg_proc` **(Many-Argument Workhorses)** (Impact: 92.1)
  * `add_cert_to_list` **(Many-Argument Workhorses)** (Impact: 84.8)
  * `save_pfx` **(Many-Argument Workhorses)** (Impact: 80.0)
  * `select_cert_dlg_proc` **(Many-Argument Workhorses)** (Impact: 72.4)
  * `export_format_dlg_proc` **(Many-Argument Workhorses)** (Impact: 63.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 997 instances
* *State Mutation (weighted view):* 3346
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1175`, `structural_boundaries: 647`, `args: 595`, `func_start: 201`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 1352`, `planned_debt: 2`, `fragile_debt: 18`, `unreferenced_by_name: 9`
* *Architecture:* `api: 27`, `import: 19`
* *Defense:* `doc: 6`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.035
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 49):` commctrl.h, commdlg.h, cryptuiapi.h, cryptuires.h, hlink.h, ole2.h, richedit.h, richole.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `dll/win32/winhttp/request.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.206)
- **Top Global Matches:** file_cluster_4: 7.206, file_cluster_6: 8.164, file_cluster_16: 13.759
- **Magnitude:** 6482.16 | **LOC:** 6172 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **17**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 93.8144% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `query_headers` **(Many-Argument Workhorses)** (Impact: 173.3)
    * *Intent:* #define QUERY_MODIFIER_MASK (WINHTTP_QUERY_FLAG_REQUEST_HEADERS | WINHTTP_QUERY_FLAG_SYSTEMTIME | WI...
  * `send_request` **(Many-Argument Workhorses)** (Impact: 120.9)
  * `do_authorization` **(Many-Argument Workhorses)** (Impact: 113.4)
  * `open_connection` **(Compute Cores)** (Impact: 56.7)
  * `receive_response` **(Compute Cores)** (Impact: 56.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 141 instances
* *Amplified Cascading Flux:* 1055 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 3311
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1228`, `structural_boundaries: 944`, `args: 283`, `func_start: 193`, `class_start: 123`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1201`, `fragile_debt: 31`, `unreferenced_by_name: 11`
* *Architecture:* `api: 24`, `import: 17`
* *Defense:* `safety: 21`, `doc: 9`, `immutability_locks: 52`, `cleanup: 102`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 31):` assert.h, httprequest.h, httprequestid.h, inet_ntop.c, initguid.h, ntsecapi.h, ole2.h, schannel.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `sdk/lib/rtl/actctx.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.935)
- **Top Global Matches:** file_cluster_6: 6.935, file_cluster_4: 8.433, file_cluster_16: 15.899
- **Magnitude:** 6444.68 | **LOC:** 6482 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **7**; blast radius 0.25; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.3%), Complexity Load (formerly Cognitive Load) (70.3%)
- **Documentation Coverage:** 81.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RtlQueryInformationActivationContext` **(Many-Argument Workhorses)** (Impact: 235.9)
    * *Intent:* /*********************************************************************** * RtlQueryInformationActiva...
  * `RtlCreateActivationContext` **(Many-Argument Workhorses)** (Impact: 150.6)
    * *Intent:* /*********************************************************************** * RtlCreateActivationContex...
  * `parse_assembly_elem` **(Many-Argument Workhorses)** (Impact: 123.8)
  * `add_comserver_record` **(Many-Argument Workhorses)** (Impact: 93.0)
  * `parse_com_class_elem` **(Many-Argument Workhorses)** (Impact: 78.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 961 instances
* *State Mutation (weighted view):* 3172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1181`, `structural_boundaries: 933`, `args: 354`, `func_start: 158`, `class_start: 272`
* *Risk/State:* `safety_bypasses: 61`, `state_mutation: 1250`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 50`, `unreferenced_by_name: 14`
* *Architecture:* `api: 32`, `import: 7`
* *Defense:* `doc: 15`, `immutability_locks: 161`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.25
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 25):` compat_undoc.h, ntstrsafe.h, rtl.h, stdlib.h, debug.h, exception.h, unicode.h
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `dll/win32/samsrv/samrpc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.996)
- **Top Global Matches:** file_cluster_6: 5.996, file_cluster_4: 9.338, file_cluster_8: 16.147
- **Magnitude:** 6388.96 | **LOC:** 9825 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 0.034; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SampQueryUserAll` **(Many-Argument Workhorses)** (Impact: 160.9)
  * `SamrCreateUser2InDomain` **(Many-Argument Workhorses)** (Impact: 139.4)
    * *Intent:* /* Function 50 */
  * `SamrChangePasswordUser` **(Many-Argument Workhorses)** (Impact: 135.1)
    * *Intent:* /* Function 38 */
  * `SamrLookupIdsInDomain` **(Many-Argument Workhorses)** (Impact: 119.4)
    * *Intent:* /* Function 18 */
  * `SamrCreateUserInDomain` **(Many-Argument Workhorses)** (Impact: 110.7)
    * *Intent:* /* Function 12 */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 981 instances
* *State Mutation (weighted view):* 3219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1077`, `structural_boundaries: 323`, `args: 1310`, `func_start: 130`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1257`, `dead_code: 1`, `fragile_debt: 16`, `unreferenced_by_name: 58`
* *Architecture:* `api: 84`, `import: 1`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 20):` samsrv.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `sdk/include/c++/stlport/stl/msl_string.h` (CPP) | Magnitude: 15.54 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, macros: 6, class_start: 2, generics: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `sdk/lib/ucrt/locale/localeconv.cpp` (CPP) | Magnitude: 0.0 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 30, closures: 4, structural_boundaries: 3, import: 3
- `modules/rostests/winetests/jscript/regexp.js` (JAVASCRIPT) | Magnitude: 201.6 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: safety: 377, state_mutation: 144, core_var_decl: 123, design_snake_case: 123

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `dll/opengl/glu32/src/libnurbs/internals/trimregion.cc` (CPP) | Magnitude: 34.24 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 25, indent_spaces: 25, structural_boundaries: 10, args: 8
- `sdk/include/c++/stlport/stl/_raw_storage_iter.h` (CPP) | Magnitude: 14.44 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 27, indent_spaces: 22, func_start: 6, state_mutation: 4
- `modules/rostests/win32/smss/movefile/movefile.cpp` (CPP) | Magnitude: 108.5 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 161, core_var_decl: 26, branch: 21, structural_boundaries: 21
- `dll/shellext/cabview/cabview.cpp` (CPP) | Magnitude: 26.14 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, args: 10, structural_boundaries: 9, branch: 7
- `dll/win32/devmgr/devmgmt/ResourceNode.cpp` (CPP) | Magnitude: 26.98 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 45, pointers: 19, branch: 8, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `modules/rostests/winetests/imagehlp/image.c` (C) | Magnitude: 218.32 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 346, pointers: 120, structural_boundaries: 64, state_mutation: 49
- `drivers/network/tcpip/lwip/test/unit/lwip_unittests.c` (C) | Magnitude: 61.24 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, import: 21, macros: 11, pointers: 11
- `modules/rostests/apitests/atl/CHeapPtrList.cpp` (CPP) | Magnitude: 45.84 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 35, args: 20, func_start: 18
- `modules/rostests/winetests/msi/package.c` (C) | Magnitude: 3083.18 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 6920, state_mutation: 1685, core_var_decl: 1599, design_snake_case: 1591
- `sdk/include/reactos/ui/CWaitCursor.h` (CPP) | Magnitude: 29.4 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 6, args: 5, state_mutation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `dll/win32/wmiutils/wmiutils_private.h` (C) | Magnitude: 10.8 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 4, args: 3, api: 3, pointers: 3
- `dll/opengl/glu32/src/libnurbs/internals/bufpool.h` (CPP) | Magnitude: 44.3 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 49, indent_spaces: 32, args: 16, safety_bypasses: 15
- `modules/rostests/apitests/crt/strcpy.c` (C) | Magnitude: 1.7 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: import: 2, func_start: 1, safety_bypasses: 1, unreferenced_by_name: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `modules/rostests/apitests/browseui/IACLHistory.cpp` (CPP) | Magnitude: 12.24 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 26, pointers: 8, state_mutation: 7, core_var_decl: 7
- `base/applications/cmdutils/clip/clip.c` (C) | Magnitude: 68.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 65, branch: 15, args: 12, state_mutation: 11
- `dll/keyboard/kbdsp/kbdsp.c` (C) | Magnitude: 12.06 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 412, args: 48, bitwise_ops: 18, macros: 14
- `sdk/include/ucrt/stdlib.h` (C) | Magnitude: 152.46 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 689, args: 203, macros: 133, api: 116
- `dll/directx/ddraw/main.c` (C) | Magnitude: 180.44 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 175, branch: 30, core_var_decl: 27, pointers: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `drivers/multimedia/audio/sndblst_sys/sndblst.c` (C) | Magnitude: 134.0 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 185, state_mutation: 38, pointers: 36, args: 34
- `ntoskrnl/fsrtl/largemcb.c` (C) | Magnitude: 614.26 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 558, pointers: 285, state_mutation: 131, branch: 83
- `dll/win32/crypt32/crypt32_private.h` (C) | Magnitude: 102.58 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: pointers: 137, structural_boundaries: 132, api: 89, args: 84
- `dll/win32/netapi32/dssetup.c` (C) | Magnitude: 57.62 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 72, branch: 9, args: 9, state_mutation: 9
- `modules/rostests/apitests/setupapi/devclass.c` (C) | Magnitude: 62.96 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 220, args: 68, pointers: 40, core_var_decl: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `sdk/lib/drivers/wdf/shared/inc/private/km/fxtypedefskm.hpp` (CPP) | Magnitude: 15.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: pointers: 10, structural_boundaries: 9, indent_spaces: 8, macros: 1
- `dll/win32/msvcrt/include/conio.h` (C) | Magnitude: 45.88 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 29, api: 29, structural_boundaries: 17, macros: 12
- `sdk/lib/drivers/wdf/shared/inc/primitives/km/mxmemorykm.h` (C) | Magnitude: 15.4 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, args: 4, structural_boundaries: 1, import: 1
- `win32ss/printing/include/marshalling/jobs.h` (C) | Magnitude: 16.22 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 112, indent_spaces: 53, globals: 4, immutability_locks: 4
- `modules/rosapps/applications/sysutils/utils/sdkparse/safestr.h` (CPP) | Magnitude: 36.32 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 13, branch: 7, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `sdk/include/reactos/dll/newdevp.h` (C) | Magnitude: 19.62 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 13, api: 4, macros: 4, args: 3
- `sdk/include/asm/ksx.template.h` (CPP) | Magnitude: 30.02 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: args: 541, macros: 66, fragile_debt: 16, doc: 14
- `sdk/lib/drivers/wdf/shared/core/um/fxrequestapium.cpp` (CPP) | Magnitude: 54.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 235, pointers: 54, args: 29, structural_boundaries: 16
- `win32ss/printing/include/marshalling/printprocessors.h` (C) | Magnitude: 15.28 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 10, args: 6, globals: 2, immutability_locks: 2
- `boot/freeldr/freeldr/arch/realmode/pnp.inc` (ASSEMBLY) | Magnitude: 9.9 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 42, indent_spaces: 42, args: 29, pointers: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_3
- `win32ss/drivers/font/ftfd/sprintf.c` (C) | Magnitude: 1340.36 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 501, state_mutation: 233, branch: 228, pointers: 105

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `dll/win32/rpcrt4/ndr_marshall.c` (C) | Magnitude: 6126.2 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 5092, pointers: 1734, branch: 1163, state_mutation: 1042
- `modules/rostests/winetests/riched20/editor.c` (C) | Magnitude: 3726.18 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 6844, state_mutation: 1887, core_var_decl: 1082, design_snake_case: 877
- `modules/rostests/kmtests/kmtest_drv/kmtest_standalone.c` (C) | Magnitude: 262.9 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 223, state_mutation: 52, branch: 49, pointers: 36
- `modules/rostests/winetests/gdiplus/image.c` (C) | Magnitude: 2705.02 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 4263, state_mutation: 1163, core_var_decl: 945, args: 917
- `subsystems/csr/csrsrv/procsup.c` (C) | Magnitude: 590.48 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 538, pointers: 141, state_mutation: 112, args: 95

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `drivers/network/tcpip/lwip/src/netif/ppp/fsm.c` (C) | Magnitude: 660.94 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 341, indent_spaces: 216, indent_tabs: 200, branch: 177
- `drivers/wdm/audio/drivers/CMIDriver/adapter.cpp` (CPP) | Magnitude: 312.74 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 257, pointers: 121, state_mutation: 79, branch: 50
- `base/system/diskpart/list.c` (C) | Magnitude: 352.2 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 323, pointers: 109, state_mutation: 68, branch: 65
- `modules/rostests/winetests/sti/sti.c` (C) | Magnitude: 150.58 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 177, branch: 39, pointers: 33, core_var_decl: 31
- `drivers/storage/floppy/fdc/fdo.c` (C) | Magnitude: 309.56 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 335, pointers: 137, state_mutation: 83, branch: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `modules/rostests/winetests/netapi32/apibuf.c` (C) | Magnitude: 28.06 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 44, pointers: 15, import: 9, args: 8
- `dll/win32/netcfgx/netcfgclass_iface.c` (C) | Magnitude: 158.12 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 143, pointers: 102, branch: 27, structural_boundaries: 23
- `modules/rostests/winetests/ucrtbase/file.c` (C) | Magnitude: 158.82 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 339, state_mutation: 89, pointers: 76, core_var_decl: 74
- `modules/rostests/apitests/atl/CComObject.cpp` (CPP) | Magnitude: 21.96 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 72, pointers: 13, structural_boundaries: 12, args: 11
- `sdk/tools/mkisofs/schilytools/include/schily/string.h` (C) | Magnitude: 0.04 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: immutability_locks: 33, api: 26, pointers: 16, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `base/setup/lib/utils/bldrsup.c` (C) | Magnitude: 922.16 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 912, pointers: 213, branch: 197, args: 170

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `dll/win32/ws2_32/src/socklife.c` (C) | Magnitude: 344.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 330, pointers: 55, branch: 53, state_mutation: 52
- `modules/rostests/dibtests/icontest/icontest.c` (C) | Magnitude: 98.22 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 148, state_mutation: 24, branch: 13, args: 13
- `dll/win32/wbemprox/reg.c` (C) | Magnitude: 487.14 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 333, pointers: 124, branch: 86, state_mutation: 86
- `drivers/wdm/audio/sysaudio/deviface.c` (C) | Magnitude: 112.96 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 173, pointers: 65, args: 30, core_var_decl: 25
- `boot/freeldr/freeldr/lib/arcsupp.c` (C) | Magnitude: 38.44 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, branch: 8, args: 6, state_mutation: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `boot/freeldr/freeldr/arch/uefi/uefivid.c` -> Churn: **83.05%** | Cog Load: 85.4724% | Debt: 40.3468%
- `dll/win32/netcfgx/tcpipconf_notify.c` -> Churn: **79.25%** | Cog Load: 67.5811% | Debt: 8.5284%
- `win32ss/gdi/ntgdi/freetype.c` -> Churn: **79.25%** | Cog Load: 67.566% | Debt: 20.9972%
- `boot/freeldr/freeldr/ntldr/winldr.c` -> Churn: **75.0%** | Cog Load: 64.3996% | Debt: 56.9001%
- `boot/freeldr/freeldr/arch/uefi/uefihw.c` -> Churn: **70.18%** | Cog Load: 67.0697% | Debt: 86.1395%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `dll/win32/msvcrt/scanf.h` -> **Timo Kreuzer** (100.0% isolated ownership) | Magnitude: 13538.97
- `dll/win32/comctl32/listview.c` -> **Emanuele Luca Cerea** (100.0% isolated ownership) | Magnitude: 10349.02
- `modules/rostests/winetests/user32/msg.c` -> **Carl J. Bialorucki** (100.0% isolated ownership) | Magnitude: 7447.54
- `win32ss/gdi/ntgdi/freetype.c` -> **Katayama Hirofumi MZ** (100.0% isolated ownership) | Magnitude: 6686.24
- `dll/win32/ole32/storage32.c` -> **Mikhail Tyukin** (100.0% isolated ownership) | Magnitude: 6621.34

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `sdk/lib/rtl/mem.c` -> **Severity: 862.629** (Blast Radius: 10.064 * Doc Risk: 85.7143%)
- `dll/win32/kernel32/client/except.c` -> **Severity: 804.9** (Blast Radius: 8.049 * Doc Risk: 100.0%)
- `modules/rostests/tests/polytest/polytest.cpp` -> **Severity: 663.3** (Blast Radius: 6.633 * Doc Risk: 100.0%)
- `dll/win32/kernel32/client/heapmem.c` -> **Severity: 606.9** (Blast Radius: 6.069 * Doc Risk: 100.0%)
- `modules/rostests/apitests/ntdll/sprintf.c` -> **Severity: 592.0** (Blast Radius: 5.92 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 5464 literal sites + 131 sites through wrappers = 5595
- **`memory_alloc`:** 7978 literal sites + 10945 sites through wrappers = 18923
- **`panics_and_aborts`:** 6023 literal sites + 245 sites through wrappers = 6268

- `HeapFree` (macro, memory_alloc, primitive): 5463 call sites in 961 files -- `dll/win32/dbghelp/compat.h`
- `malloc` (macro, memory_alloc, via _malloc_dbg): 1905 call sites in 428 files -- `sdk/include/ucrt/crtdbg.h`
- `flush_sequence` (function, memory_alloc, primitive): 387 call sites in 1 files -- `modules/rostests/winetests/user32/msg.c`
- `CryptMemFree` (function, memory_alloc, via HeapFree): 276 call sites in 28 files -- `dll/win32/crypt32/main.c`
- `midl_user_free` (function, memory_alloc, via HeapFree): 133 call sites in 1 files -- `dll/win32/samsrv/samrpc.c`
- `cmd_free` (macro, memory_alloc, primitive): 98 call sites in 22 files -- `base/shell/cmd/cmddbg.h`
- `SamFreeMemory` (function, memory_alloc, via midl_user_free): 71 call sites in 4 files -- `dll/win32/samlib/samlib.c`
- `ImmLocalFree` (macro, memory_alloc, via HeapFree): 62 call sites in 11 files -- `win32ss/user/imm32/precomp.h`
- `d3dcompiler_free` (function, memory_alloc, via HeapFree): 61 call sites in 2 files -- `dll/directx/wine/d3dcompiler_43/d3dcompiler_private.h`
- `RpcStringFreeA` (function, memory_alloc, primitive): 59 call sites in 6 files -- `dll/win32/rpcrt4/rpcrt4_main.c`
- `error` (function, debug_prints, primitive): 54 call sites in 1 files -- `sdk/tools/txt2nls/main.cpp`
- `error` (function, panics_and_aborts, primitive): 54 call sites in 1 files -- `sdk/tools/txt2nls/main.cpp`
*(+638 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 707847 call pairs -- scoped 19.7%, unique 25.0%, ambiguous 20.8%, external 34.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 607663 | 19.7% | 26.3% | 19.5% | 34.6% |
| cpp | 97107 | 19.4% | 17.6% | 29.7% | 33.4% |
| yacc | 1407 | 6.9% | 19.5% | 10.2% | 63.4% |
| python | 541 | 28.1% | 0.0% | 0.7% | 71.2% |
| assembly | 500 | 46.0% | 9.0% | 5.0% | 40.0% |
| html | 158 | 46.2% | 0.0% | 0.0% | 53.8% |
| javascript | 157 | 19.7% | 0.0% | 18.5% | 61.8% |
| livecode | 140 | 0.0% | 0.0% | 0.0% | 100.0% |
| perl | 102 | 20.6% | 0.0% | 0.0% | 79.4% |
| shell | 57 | 17.5% | 0.0% | 0.0% | 82.5% |

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
