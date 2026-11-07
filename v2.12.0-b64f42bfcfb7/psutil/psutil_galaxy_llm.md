# ARCHITECTURAL_BRIEF: psutil
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 183 analyzed artifact(s), 35614 LOC.
- **Load-bearing artifact:** `psutil-7.2.2/psutil/arch/all/init.h` -- 87 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `psutil-7.2.2/tests/test_process.py` -- pulls in 52 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `psutil-7.2.2/psutil/_pslinux.py` at magnitude 1855.76 (structural weight, not risk).
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
| Total Artifacts | 192 |
| Analyzed Artifacts (Scanned) | 183 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9 |
| Total LOC | 35614 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 95.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5686 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4283 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8299 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 103 | 16237 | 56.3% |
| PYTHON | 71 | 19011 | 38.8% |
| MARKDOWN | 4 | 0 | 2.2% |
| PLAINTEXT | 2 | 0 | 1.1% |
| YAML | 1 | 52 | 0.5% |
| MAKEFILE | 1 | 255 | 0.5% |
| SHELL | 1 | 59 | 0.5% |

## 4.1 SOURCE ENCODINGS
All 183 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 21%, Large Core Modules (2) 19%, Compute Cores Files 17%, Large Core Modules (3) 9%, Declarative / Non-Code 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 177 | 96.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 3.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `.jsonc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 95.8 | 44.3 | 43.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.3 | 53.1 | 60.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.5 | 14.2 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.7 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.3 | 5.3 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 60.7 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 71.1 | 100.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 17.4 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 83.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 896 | 107 | 13 | `psutil-7.2.2/psutil/_pslinux.py` |
| cleanup | 265 | 53 | 5 | `psutil-7.2.2/psutil/_psutil_aix.c` |
| guards | 3208 | 128 | 33 | `psutil-7.2.2/tests/test_linux.py` |
| danger | 911 | 100 | 14 | `psutil-7.2.2/psutil/_pslinux.py` |
| concurrency | 92 | 24 | 1 | `psutil-7.2.2/tests/__init__.py` |
| connectivity | 2273 | 174 | 44 | `psutil-7.2.2/tests/test_linux.py` |
| io | 937 | 70 | 11 | `psutil-7.2.2/tests/test_linux.py` |
| crypto | 2 | 2 | 0 | `psutil-7.2.2/scripts/internal/install_pip.py` |
| ipc | 126 | 33 | 2 | `psutil-7.2.2/tests/__init__.py` |
| time | 86 | 22 | 1 | `psutil-7.2.2/tests/test_process.py` |
| serialization | 7 | 3 | 0 | `psutil-7.2.2/tests/test_misc.py` |
| regex | 60 | 13 | 0 | `psutil-7.2.2/tests/test_linux.py` |
| events | 19 | 2 | 0 | `psutil-7.2.2/tests/test_system.py` |
| tests | 1507 | 22 | 5 | `psutil-7.2.2/tests/test_linux.py` |
| docs | 585 | 71 | 5 | `psutil-7.2.2/psutil/__init__.py` |
| debt | 282 | 81 | 5 | `psutil-7.2.2/tests/test_process.py` |
| mutation | 11668 | 157 | 168 | `psutil-7.2.2/psutil/_pslinux.py` |
| dead_code | 919 | 112 | 9 | `psutil-7.2.2/tests/test_linux.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 15 | 7 | 0 | `psutil-7.2.2/psutil/arch/freebsd/proc_socks.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `psutil-7.2.2/tests/test_linux.py` (Hits: 144)
- `psutil-7.2.2/tests/__init__.py` (Hits: 100)
- `psutil-7.2.2/psutil/_pslinux.py` (Hits: 83)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **init.h** (`psutil-7.2.2/psutil/arch/all/init.h`) — 87 inbound connections
2. **errors.c** (`psutil-7.2.2/psutil/arch/all/errors.c`) — 64 inbound connections
3. **__init__.py** (`psutil-7.2.2/psutil/__init__.py`) — 56 inbound connections
4. **_common.py** (`psutil-7.2.2/psutil/_common.py`) — 32 inbound connections
5. **str.c** (`psutil-7.2.2/psutil/arch/all/str.c`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_process.py** (`psutil-7.2.2/tests/test_process.py`) — 52 outbound dependencies
2. **test_linux.py** (`psutil-7.2.2/tests/test_linux.py`) — 37 outbound dependencies
3. **test_testutils.py** (`psutil-7.2.2/tests/test_testutils.py`) — 35 outbound dependencies
4. **test_system.py** (`psutil-7.2.2/tests/test_system.py`) — 33 outbound dependencies
5. **test_windows.py** (`psutil-7.2.2/tests/test_windows.py`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `psutil_net_connections` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/windows/socks.c`) -> Impact: **139.4** | LOC: 363
  * *Intent:* /* * Return a list of network connections opened by a process */
- `psutil_net_connections` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/sunos/net.c`) -> Impact: **129.6** | LOC: 306
  * *Intent:* /* * Return TCP and UDP connections opened by process. * UNIX sockets are excluded. * * Thanks to: * https://github.com/DavidGriffith/finx/blob/master...
- `psutil_get_process_data` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/windows/proc_info.c`) -> Impact: **121.9** | LOC: 336
  * *Intent:* /* * Get data from the process with the given pid. The data is returned * in the pdata output member as a nul terminated string which must be * freed ...
- `run` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/scripts/procinfo.py`) -> Impact: **109.8** | LOC: 187
- `psutil_gather_inet` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c`) -> Impact: **101.2** | LOC: 171
  * *Intent:* // Reference: // https://github.com/freebsd/freebsd/blob/master/usr.bin/sockstat/sockstat.c
- `psutil_net_if_flags` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/posix/net.c`) -> Impact: **95.8** | LOC: 183
  * *Intent:* /* * Get all of the NIC flags and return them. */
- `psutil_proc_net_connections` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/osx/proc.c`) -> Impact: **84.2** | LOC: 229
  * *Intent:* /* * Return process TCP and UDP connections as a list of tuples. * Raises NSP in case of zombie process. * See lsof source code: * https://github.com/...
- `psutil_search_tcplist` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/freebsd/proc_socks.c`) -> Impact: **81.1** | LOC: 305
  * *Intent:* #if __FreeBSD_version >= 1200026
- `psutil_get_nic_speed` **(Compute Cores)** (@ `psutil-7.2.2/psutil/arch/posix/net.c`) -> Impact: **80.4** | LOC: 137
  * *Intent:* // net_if_stats() macOS/BSD implementation. #ifdef PSUTIL_HAS_NET_IF_DUPLEX_SPEED
- `process_file` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/aix/net_connections.c`) -> Impact: **79.8** | LOC: 165

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `psutil-7.2.2/tests` | 21 | 8921.44 | 25.51% | 0.0% |
| `psutil-7.2.2/psutil` | 16 | 7812.38 | 35.63% | 14.46% |
| `psutil-7.2.2/psutil/arch/windows` | 19 | 3500.68 | 55.1% | 43.02% |
| `psutil-7.2.2/psutil/arch/osx` | 12 | 1595.06 | 53.66% | 32.66% |
| `psutil-7.2.2/psutil/arch/freebsd` | 9 | 1458.7 | 58.78% | 36.57% |
| `psutil-7.2.2/psutil/arch/sunos` | 8 | 1308.48 | 57.37% | 41.77% |
| `psutil-7.2.2/scripts/internal` | 20 | 1202.29 | 41.86% | 2.98% |
| `psutil-7.2.2/scripts` | 22 | 1103.48 | 36.42% | 0.0% |
| `psutil-7.2.2/psutil/arch/posix` | 7 | 812.7 | 40.61% | 37.44% |
| `psutil-7.2.2/psutil/arch/bsd` | 9 | 659.54 | 42.71% | 50.77% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `psutil-7.2.2/Makefile` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/openbsd/cpu.c` -> **99.9968%** Exposure
- `psutil-7.2.2/psutil/arch/netbsd/cpu.c` -> **99.9901%** Exposure
- `psutil-7.2.2/psutil/arch/windows/mem.c` -> **99.9624%** Exposure
- `psutil-7.2.2/psutil/arch/all/errors.c` -> **99.4995%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `psutil-7.2.2/psutil/__init__.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_common.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_ntuples.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_psaix.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_psbsd.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `psutil-7.2.2/tests/test_linux.py` -> **100** Orphaned Functions | **0** Duplicates
- `psutil-7.2.2/tests/test_process.py` -> **92** Orphaned Functions | **0** Duplicates
- `psutil-7.2.2/tests/test_memleaks.py` -> **70** Orphaned Functions | **0** Duplicates
- `psutil-7.2.2/tests/test_windows.py` -> **52** Orphaned Functions | **6** Duplicates
- `psutil-7.2.2/tests/test_system.py` -> **49** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `955` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `psutil-7.2.2/psutil/_pslinux.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.293)
- **Top Global Matches:** file_cluster_12: 7.293, file_cluster_4: 8.958, file_cluster_15: 10.214
- **Magnitude:** 1855.76 | **LOC:** 2270 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **17**; blast radius 7.583; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.8%), Connectivity (formerly Api Exposure) (54.6%), Complexity Load (formerly Cognitive Load) (50.1%)
- **Documentation Coverage:** 56.9697% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_inet` **(Many-Argument Workhorses)** (Impact: 31.4)
    * *Intent:* """Parse /proc/net/tcp* and /proc/net/udp* files."""
  * `process_unix` **(Many-Argument Workhorses)** (Impact: 28.5)
    * *Intent:* """Parse /proc/net/unix files."""
  * `disk_io_counters` **(Compute Cores)** (Impact: 27.8)
    * *Intent:* """Return disk I/O statistics for every disk installed on the system as a dict of raw tuples. """
  * `sensors_battery` **(I/O & Config Routines)** (Impact: 25.4)
    * *Intent:* """Return battery information. Implementation note: it appears /sys/class/power_supply/BAT0/ directo...
  * `disk_partitions` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* """Return mounted disk partitions as a list of namedtuples."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 321 instances
* *State Mutation (weighted view):* 1101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 396`, `args: 91`, `func_start: 90`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 459`, `dead_code: 3`, `fragile_debt: 7`
* *Architecture:* `io: 83`, `api: 79`, `import: 40`
* *Defense:* `safety: 107`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.583
  * `Choke Point (Betweenness):` 0.000251 | `Ripple Effect (Closeness):` 0.159544
  * `Imports (Out-Degree: 4):` ._common, ._ntuples, ._psposix, ._psutil_linux, base64, collections, enum, errno...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.103)
- **Top Global Matches:** file_cluster_12: 6.103, file_cluster_7: 9.391, file_cluster_15: 9.534
- **Magnitude:** 1629.52 | **LOC:** 2485 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **56** in-repo importer(s); it depends on **22**; blast radius 48.737; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.2%), Connectivity (formerly Api Exposure) (66.9%), Concurrency Surface (formerly Concurrency) (60.3%)
- **Documentation Coverage:** 21.393% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wait_procs` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* """Convenience function which waits for a list of processes to terminate. Return a (gone, alive) tup...
  * `cpu_percent` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* """Return a float representing the current system-wide CPU utilization as a percentage. When *interv...
  * `cpu_times_percent` **(Compute Cores)** (Impact: 27.1)
    * *Intent:* """Same as cpu_percent() but provides utilization percentages for each specific CPU time as is retur...
  * `as_dict` **(Many-Argument Workhorses)** (Impact: 24.3)
    * *Intent:* """Utility method returning process information as a hashable dictionary. If *attrs* is specified it...
  * `children` **(Many-Argument Workhorses)** (Impact: 22.7)
    * *Intent:* """Return the children of this process as a list of Process instances, pre-emptively checking whethe...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 243 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 438`, `args: 106`, `func_start: 103`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 2`, `state_mutation: 300`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 93`, `concurrency: 6`, `import: 86`
* *Defense:* `safety: 95`, `doc: 83`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.737
  * `Choke Point (Betweenness):` 0.01234 | `Ripple Effect (Closeness):` 0.307692
  * `Imports (Out-Degree: 8):` ._common, ._ntuples, ._psaix, ._psbsd, ._pslinux, ._psosx, ._pssunos, ._psutil_windows...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/tests/test_linux.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.776)
- **Top Global Matches:** file_cluster_12: 7.776, file_cluster_15: 8.402, file_cluster_13: 9.693
- **Magnitude:** 1436.88 | **LOC:** 2290 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.8%), Complexity Load (formerly Cognitive Load) (30.4%), Connectivity (formerly Api Exposure) (13.5%)
- **Documentation Coverage:** 86.0369% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open_mock` **(Compute Cores)** (Impact: 31.5)
  * `test_emulate_multi_cpu` **(Defensive Guards)** (Impact: 29.3)
  * `test_flags` **(Defensive Guards)** (Impact: 25.4)
    * *Intent:* # first line looks like this: # "eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500" matches_...
  * `open_mock` **(Compute Cores)** (Impact: 18.9)
  * `test_emulate_data` **(Defensive Guards)** (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 487
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 919`, `args: 158`, `func_start: 154`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 271`, `dead_code: 4`, `fragile_debt: 2`, `unreferenced_by_name: 100`
* *Architecture:* `io: 144`, `api: 181`, `import: 45`
* *Defense:* `safety: 341`, `doc: 20`, `test: 269`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .AARCH64, .GITHUB_ACTIONS, .GLOBAL_TIMEOUT, .HAS_BATTERY, .HAS_CPU_FREQ, .HAS_GETLOADAVG, .HAS_RLIMIT, .PsutilTestCase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.348)
- **Top Global Matches:** file_cluster_12: 6.348, file_cluster_15: 8.638, file_cluster_16: 9.283
- **Magnitude:** 1283.0 | **LOC:** 1737 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **31**; blast radius 20.577; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (61.2%), Guard Balance (formerly Safety Score) (60.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (23.3%)
- **Documentation Coverage:** 50.0783% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `terminate` **(Defensive Guards)** (Impact: 46.1)
    * *Intent:* """Terminate a process and wait() for it. Process can be a PID or an instance of psutil.Process(), s...
  * `check_connection_ntuple` **(Defensive Guards)** (Impact: 24.9)
    * *Intent:* """Check validity of a connection namedtuple."""
  * `assert_proc_zombie` **(Defensive Guards)** (Impact: 18.3)
  * `copyload_shared_lib` **(Defensive Guards)** (Impact: 17.7)
    * *Intent:* """Ctx manager which picks up a random shared DLL lib used by this process, copies it in another loc...
  * `wrapper` **(Defensive Guards)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 168 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 555
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 357`, `args: 95`, `func_start: 93`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 7`, `state_mutation: 219`, `fragile_debt: 3`
* *Architecture:* `io: 100`, `api: 92`, `concurrency: 4`, `import: 46`
* *Defense:* `safety: 171`, `doc: 48`, `test: 15`, `sync_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.577
  * `Choke Point (Betweenness):` 0.000673 | `Ripple Effect (Closeness):` 0.104396
  * `Imports (Out-Degree: 3):` atexit, contextlib, ctypes, enum, errno, functools, importlib, ipaddress...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/tests/test_process.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.123)
- **Top Global Matches:** file_cluster_12: 7.123, file_cluster_15: 7.87, file_cluster_13: 9.316
- **Magnitude:** 1222.26 | **LOC:** 1843 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **52**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.6%), Complexity Load (formerly Cognitive Load) (32.2%), Connectivity (formerly Api Exposure) (12.4%)
- **Documentation Coverage:** 88.924% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_memory_maps` **(Defensive Guards)** (Impact: 25.0)
  * `test_nice` **(Defensive Guards)** (Impact: 20.2)
  * `test_pid_0` **(Defensive Guards)** (Impact: 19.2)
    * *Intent:* # Process(0) is supposed to work on all platforms except Linux if 0 not in psutil.pids(): with pytes...
  * `test_open_files` **(Defensive Guards)** (Impact: 18.8)
    * *Intent:* # TODO: #595
  * `test_cmdline` **(Defensive Guards)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 146 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 530
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 658`, `args: 104`, `func_start: 100`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 2`, `state_mutation: 238`, `planned_debt: 2`, `fragile_debt: 14`, `unreferenced_by_name: 92`
* *Architecture:* `io: 76`, `api: 103`, `import: 63`
* *Defense:* `safety: 320`, `doc: 4`, `test: 244`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .CI_TESTING, .GITHUB_ACTIONS, .GLOBAL_TIMEOUT, .HAS_CPU_AFFINITY, .HAS_ENVIRON, .HAS_IONICE, .HAS_MEMORY_MAPS, .HAS_PROC_CPU_NUM...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_pswindows.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.69)
- **Top Global Matches:** file_cluster_15: 6.69, file_cluster_12: 7.047, file_cluster_11: 7.562
- **Magnitude:** 737.64 | **LOC:** 1097 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **11**; blast radius 7.032; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.8%), Connectivity (formerly Api Exposure) (65.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wait` **(Defensive Guards)** (Impact: 17.6)
  * `cpu_affinity_set` **(Defensive Guards)** (Impact: 11.6)
  * `send_signal` **(Compute Cores)** (Impact: 9.2)
  * `convert_dos_path` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* # ===================================================================== # --- utils # ==============...
  * `net_connections` **(Type Conversions)** (Impact: 8.0)
    * *Intent:* # ===================================================================== # --- network # ============...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 97 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 262`, `args: 84`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 161`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `io: 6`, `api: 79`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 40`, `doc: 40`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.032
  * `Choke Point (Betweenness):` 0.000175 | `Ripple Effect (Closeness):` 0.164103
  * `Imports (Out-Degree: 4):` ._common, ._ntuples, ._psutil_windows, contextlib, enum, functools, os, signal...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/tests/test_system.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.811)
- **Top Global Matches:** file_cluster_12: 7.811, file_cluster_15: 8.784, file_cluster_4: 8.911
- **Magnitude:** 672.52 | **LOC:** 985 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (30.7%), Guard Balance (formerly Safety Score) (30.5%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 88.924% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_net_if_addrs` **(Defensive Guards)** (Impact: 32.0)
  * `test_disk_partitions` **(Defensive Guards)** (Impact: 26.9)
  * `test_os_constants` **(Defensive Guards)** (Impact: 16.5)
  * `test_wait_procs` **(Defensive Guards)** (Impact: 14.2)
  * `test_cpu_freq` **(Defensive Guards)** (Impact: 12.3)
    * *Intent:* # TODO: remove this once 1892 is fixed
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 253
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 416`, `args: 60`, `func_start: 58`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 101`, `dead_code: 7`, `planned_debt: 2`, `unreferenced_by_name: 49`
* *Architecture:* `io: 41`, `api: 65`, `import: 43`
* *Defense:* `safety: 258`, `doc: 1`, `test: 101`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .AARCH64, .ASCII_FS, .CI_TESTING, .GITHUB_ACTIONS, .GLOBAL_TIMEOUT, .HAS_BATTERY, .HAS_CPU_FREQ, .HAS_GETLOADAVG...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/osx/proc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.64)
- **Top Global Matches:** file_cluster_3: 10.64, file_cluster_8: 13.334, file_cluster_6: 26.13
- **Magnitude:** 662.6 | **LOC:** 1050 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `psutil_proc_net_connections` **(Many-Argument Workhorses)** (Impact: 84.2)
    * *Intent:* /* * Return process TCP and UDP connections as a list of tuples. * Raises NSP in case of zombie proc...
  * `psutil_proc_environ` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* // Return process environment as a python string. // On Big Sur this function returns an empty strin...
  * `psutil_proc_memory_uss` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* /* * Returns the USS (unique set size) of the process. Reference: * https://dxr.mozilla.org/mozilla-...
  * `psutil_proc_threads` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* /* * Return process threads */
  * `psutil_proc_open_files` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* /* * Return process open files as a Python tuple. * See lsof source code: * https://github.com/apple...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 93 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 87`, `args: 29`, `func_start: 14`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 105`, `dead_code: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 12`, `import: 18`
* *Defense:* `safety: 15`, `immutability_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` init.h, Python.h, inet.h, errno.h, libproc.h, loader.h, mach.h, mach_vm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/windows/proc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.012)
- **Top Global Matches:** file_cluster_4: 7.012, file_cluster_6: 7.298, file_cluster_9: 13.34
- **Magnitude:** 643.16 | **LOC:** 1230 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.9%), Complexity Load (formerly Cognitive Load) (57.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `psutil_proc_exe` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* /* * Return process executable path. Works for all processes regardless of * privilege. NtQuerySyste...
  * `psutil_proc_threads` **(Many-Argument Workhorses)** (Impact: 34.7)
  * `psutil_proc_username` **(Many-Argument Workhorses)** (Impact: 34.2)
    * *Intent:* /* * Return process username as a "DOMAIN//USERNAME" string. */
  * `psutil_GetProcWsetInformation` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `psutil_proc_memory_maps` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* /* * Return a list of process's memory mappings. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 73 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 111`, `args: 41`, `func_start: 25`
* *Risk/State:* `state_mutation: 80`, `unreferenced_by_name: 22`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` init.h, Psapi.h, Python.h, signal.h, tlhelp32.h, windows.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_common.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.659)
- **Top Global Matches:** file_cluster_12: 5.659, file_cluster_7: 8.138, file_cluster_5: 8.991
- **Magnitude:** 628.14 | **LOC:** 862 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **13**; blast radius 197.588; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (84.2%), Guard Balance (formerly Safety Score) (74.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 38.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `conn_to_ntuple` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* """Convert a raw connection tuple to a proper ntuple."""
  * `print_color` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `run` **(Many-Argument Workhorses)** (Impact: 11.9)
    * *Intent:* """Cache dict and sum numbers which overflow and wrap. Return an updated copy of `input_dict`. """
  * `_infodict` **(Stateful Encapsulated Methods)** (Impact: 9.0)
  * `__str__` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* # invoked on `raise Error` info = self._infodict(("pid", "ppid", "name")) if info: details = "({})"....
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 83 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 163`, `args: 48`, `func_start: 48`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 167`, `duplicate_logic: 2`
* *Architecture:* `io: 37`, `api: 44`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 49`, `doc: 35`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 197.588
  * `Choke Point (Betweenness):` 0.000354 | `Ripple Effect (Closeness):` 0.227167
  * `Imports (Out-Degree: 1):` ._ntuples, collections, ctypes, enum, functools, inspect, ipaddress, os...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/_psbsd.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.685)
- **Top Global Matches:** file_cluster_12: 5.685, file_cluster_15: 8.23, file_cluster_7: 9.113
- **Magnitude:** 607.22 | **LOC:** 905 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 6.001; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%), Connectivity (formerly Api Exposure) (62.4%)
- **Documentation Coverage:** 60.5263% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cmdline` **(Defensive Guards)** (Impact: 15.4)
  * `net_connections` **(Compute Cores)** (Impact: 15.0)
  * `exe` **(Compute Cores)** (Impact: 13.9)
  * `cpu_affinity_set` **(Defensive Guards)** (Impact: 11.6)
    * *Intent:* # Pre-emptively check if CPUs are valid because the C # function has a weird behavior in case of inv...
  * `wrapper` **(Defensive Guards)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 215`, `args: 58`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 123`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `io: 3`, `api: 57`, `import: 24`
* *Defense:* `safety: 33`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.001
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.155232
  * `Imports (Out-Degree: 4):` ._common, ._ntuples, ._psposix, ._psutil_bsd, collections, contextlib, errno, functools...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/tests/test_windows.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.983)
- **Top Global Matches:** file_cluster_15: 6.983, file_cluster_12: 8.343, file_cluster_13: 8.492
- **Magnitude:** 579.5 | **LOC:** 948 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.0%), Complexity Load (formerly Cognitive Load) (39.6%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 86.5527% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_disks` **(Defensive Guards)** (Impact: 14.2)
  * `wmic` **(Compute Cores)** (Impact: 12.8)
    * *Intent:* """Currently not used, but available just in case. Usage: >>> wmic("Win32_OperatingSystem", "FreePhy...
  * `test_win_service_iter` **(Defensive Guards)** (Impact: 9.5)
  * `test_disk_partitions` **(Defensive Guards)** (Impact: 9.1)
  * `setUp` **(Compute Cores)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *Api Near Db Sink:* 2 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 322`, `args: 75`, `func_start: 75`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 163`, `dead_code: 2`, `fragile_debt: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 52`
* *Architecture:* `io: 13`, `api: 84`, `import: 34`
* *Defense:* `safety: 134`, `doc: 6`, `test: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .GITHUB_ACTIONS, .HAS_BATTERY, .IS_64BIT, .PYPY, .PsutilTestCase, .TOLERANCE_DISK_USAGE, .TOLERANCE_SYS_MEM, .pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_psutil_aix.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.985)
- **Top Global Matches:** file_cluster_4: 6.985, file_cluster_16: 8.722, file_cluster_9: 9.26
- **Magnitude:** 536.32 | **LOC:** 1074 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.3%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyInit__psutil_aix` **(Compute Cores)** (Impact: 26.9)
  * `psutil_proc_environ` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* /* * Return process environment variables as a Python dict */
  * `psutil_proc_threads` **(Many-Argument Workhorses)** (Impact: 22.2)
    * *Intent:* #ifdef CURR_VERSION_THREAD /* * Retrieves all threads used by process returning a list of tuples * i...
  * `psutil_net_io_counters` **(Many-Argument Workhorses)** (Impact: 20.8)
    * *Intent:* #if defined(CURR_VERSION_NETINTERFACE) && CURR_VERSION_NETINTERFACE >= 3 /* * Return a list of tuple...
  * `psutil_per_cpu_times` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* /* * Return a Python list of tuple representing per-cpu times */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 20 instances
* *Amplified Cascading Flux:* 78 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 106`, `args: 43`, `func_start: 22`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 78`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 4`, `import: 25`
* *Defense:* `safety: 5`, `immutability_locks: 4`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Python.h, common.h, ifaddrs.h, net_connections.h, init.h, inet.h, fcntl.h, libperfstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_pssunos.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.119)
- **Top Global Matches:** file_cluster_12: 6.119, file_cluster_15: 7.958, file_cluster_16: 8.517
- **Magnitude:** 515.36 | **LOC:** 705 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 6.001; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%), Connectivity (formerly Api Exposure) (55.4%)
- **Documentation Coverage:** 65.5914% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_unix_sockets` **(Stateful Encapsulated Methods)** (Impact: 19.0)
    * *Intent:* """Get UNIX sockets used by process by parsing 'pfiles' output."""
  * `net_connections` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* """Return socket connections. If pid == -1 return system-wide connections (as opposed to connections...
  * `memory_maps` **(Defensive Guards)** (Impact: 15.0)
  * `threads` **(Defensive Guards)** (Impact: 11.5)
  * `open_files` **(Defensive Guards)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 172`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 118`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 26`, `api: 45`, `import: 24`
* *Defense:* `safety: 29`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.001
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.155232
  * `Imports (Out-Degree: 4):` ._common, ._ntuples, ._psposix, ._psutil_sunos, collections, errno, functools, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/arch/windows/proc_info.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.372)
- **Top Global Matches:** file_cluster_6: 5.372, file_cluster_4: 11.868, file_cluster_8: 13.182
- **Magnitude:** 512.54 | **LOC:** 863 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `psutil_get_process_data` **(Many-Argument Workhorses)** (Impact: 121.9)
    * *Intent:* /* * Get data from the process with the given pid. The data is returned * in the pdata output member...
  * `psutil_proc_cmdline` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* /* * Return a Python list representing the arguments for the process * with given pid or NULL on err...
  * `psutil_cmdline_query_proc` **(Many-Argument Workhorses)** (Impact: 30.2)
    * *Intent:* /* * Get process cmdline by using NtQueryInformationProcess. This is a * method alternative to PEB w...
  * `psutil_get_proc_info` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /* * Given a process PID and a PSYSTEM_PROCESS_INFORMATION structure * fills the structure with vari...
  * `psutil_proc_info` **(Many-Argument Workhorses)** (Impact: 15.7)
    * *Intent:* /* * Get various process information by using NtQuerySystemInformation. * We use this as a fallback ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 70 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 43`, `args: 30`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 71`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 4`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.596
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.005495
  * `Imports (Out-Degree: 5):` init.h, Python.h, windows.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/arch/sunos/net.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.326)
- **Top Global Matches:** file_cluster_1: 5.326, file_cluster_3: 48.161, file_cluster_8: 69.996
- **Magnitude:** 494.84 | **LOC:** 567 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `psutil_net_connections` **(Many-Argument Workhorses)** (Impact: 129.6)
    * *Intent:* /* * Return TCP and UDP connections opened by process. * UNIX sockets are excluded. * * Thanks to: *...
  * `psutil_net_if_stats` **(Many-Argument Workhorses)** (Impact: 50.2)
    * *Intent:* // Return stats about a particular network interface. Refs: // * https://github.com/dpaleino/wicd/bl...
  * `psutil_net_io_counters` **(Many-Argument Workhorses)** (Impact: 43.7)
    * *Intent:* #include <sys/types.h> #include <sys/socket.h> #include <sys/sockio.h> #include <netinet/in.h> #incl...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 83 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 33`, `args: 16`, `func_start: 3`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 93`, `fragile_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 3`, `api: 3`, `import: 18`
* *Defense:* `safety: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` init.h, Python.h, inet.h, fcntl.h, mib2.h, kstat.h, if.h, in.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/freebsd/proc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.96)
- **Top Global Matches:** file_cluster_4: 6.96, file_cluster_9: 10.37, file_cluster_6: 10.782
- **Magnitude:** 470.76 | **LOC:** 594 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `psutil_proc_memory_maps` **(Many-Argument Workhorses)** (Impact: 51.7)
  * `psutil_proc_exe` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* /* * Return process pathname executable. * Thanks to Robert N. M. Watson: * http://fxr.googlebit.com...
  * `psutil_proc_setrlimit` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* /* * An emulation of Linux prlimit() (set). */
  * `psutil_proc_cmdline` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* // ============================================================================ // APIS // =========...
  * `psutil_proc_cwd` **(Compute Cores)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 81 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 245
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 69`, `args: 17`, `func_start: 12`, `class_start: 14`
* *Risk/State:* `state_mutation: 83`, `unreferenced_by_name: 11`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 4`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` init.h, Python.h, libutil.h, cpuset.h, sysctl.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_process_all.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.306)
- **Top Global Matches:** file_cluster_12: 6.306, file_cluster_15: 9.026, file_cluster_7: 9.027
- **Magnitude:** 462.38 | **LOC:** 542 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (70.0%), Concurrency Surface (formerly Concurrency) (59.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (23.8%)
- **Documentation Coverage:** 88.924% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_it` **(Defensive Guards)** (Impact: 23.8)
  * `memory_maps` **(Defensive Guards)** (Impact: 23.2)
  * `exe` **(Defensive Guards)** (Impact: 20.9)
  * `open_files` **(Defensive Guards)** (Impact: 15.2)
  * `check` **(Defensive Guards)** (Impact: 14.1)
    * *Intent:* # In case of failure retry up to 3 times in order to avoid # race conditions, especially when runnin...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 253`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 26`, `planned_debt: 1`, `fragile_debt: 6`
* *Architecture:* `io: 13`, `api: 47`, `concurrency: 3`, `import: 29`
* *Defense:* `safety: 200`, `doc: 3`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .CI_TESTING, .PYTEST_PARALLEL, .PsutilTestCase, .VALID_PROC_STATUSES, .check_connection_ntuple, .create_sockets, .is_namedtuple, .is_win_secure_system_proc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_bsd.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.772)
- **Top Global Matches:** file_cluster_12: 7.772, file_cluster_15: 7.894, file_cluster_13: 8.133
- **Magnitude:** 450.2 | **LOC:** 588 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (40.7%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 85.8577% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_ctx_switches` **(Defensive Guards)** (Impact: 9.4)
  * `test_cpu_times` **(Defensive Guards)** (Impact: 9.4)
  * `test_disks` **(Type Conversions)** (Impact: 8.4)
    * *Intent:* # test psutil.disk_usage() and psutil.disk_partitions() # against "df -a" def df(path): out = sh(f'd...
  * `test_sensors_battery` **(Defensive Guards)** (Impact: 6.5)
    * *Intent:* # --- sensors_battery
  * `sysctl` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* """Expects a sysctl command with an argument and parse the result returning only the value of intere...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 182`, `args: 58`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 103`, `planned_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 30`
* *Architecture:* `io: 8`, `api: 63`, `import: 18`
* *Defense:* `safety: 75`, `doc: 4`, `test: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .HAS_BATTERY, .PsutilTestCase, .TOLERANCE_SYS_MEM, .pytest, .retry_on_failure, .sh, .spawn_subproc, .terminate...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_misc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.002)
- **Top Global Matches:** file_cluster_12: 7.002, file_cluster_15: 7.974, file_cluster_13: 9.026
- **Magnitude:** 435.76 | **LOC:** 868 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (32.7%), Complexity Load (formerly Cognitive Load) (27.6%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 83.0447% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_against` **(Defensive Guards)** (Impact: 17.4)
    * *Intent:* # no args for _ in range(2): ret = obj() assert self.calls == [((), {})] if expected_retval is not N...
  * `test__all__` **(Defensive Guards)** (Impact: 14.4)
  * `test_serialization` **(Defensive Guards)** (Impact: 12.3)
  * `test_cache_clear_public_apis` **(Defensive Guards)** (Impact: 9.4)
  * `test_original` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* # This was the original test before I made it dynamic to test it # against different types. Keeping ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 27 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 346`, `args: 60`, `func_start: 60`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 5`, `state_mutation: 120`, `fragile_debt: 1`, `unreferenced_by_name: 45`
* *Architecture:* `io: 23`, `api: 67`, `import: 27`
* *Defense:* `safety: 185`, `doc: 6`, `test: 78`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .HAS_NET_IO_COUNTERS, .PsutilTestCase, .process_namespace, .pytest, .reload_module, .system_namespace, collections, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_connections.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.328)
- **Top Global Matches:** file_cluster_12: 7.328, file_cluster_4: 9.06, file_cluster_15: 9.627
- **Magnitude:** 432.54 | **LOC:** 573 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (28.4%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 82.4568% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_count` **(Defensive Guards)** (Impact: 28.3)
  * `test_combos` **(Defensive Guards)** (Impact: 25.2)
  * `test_unix` **(Defensive Guards)** (Impact: 21.0)
  * `check_conn` **(Many-Argument Workhorses)** (Impact: 16.5)
  * `check_socket` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* """Given a socket, makes sure it matches the one obtained via psutil. It assumes this process create...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 53 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 226`, `args: 26`, `func_start: 26`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 4`, `state_mutation: 77`, `fragile_debt: 3`, `unreferenced_by_name: 19`
* *Architecture:* `io: 11`, `api: 33`, `import: 36`
* *Defense:* `safety: 86`, `doc: 9`, `test: 32`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .AF_UNIX, .HAS_NET_CONNECTIONS_UNIX, .PsutilTestCase, .ROOT_DIR, .SKIP_SYSCONS, .bind_socket, .bind_unix_socket, .check_connection_ntuple...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/posix/net.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 5.736)
- **Top Global Matches:** file_cluster_3: 5.736, file_cluster_8: 20.385, file_cluster_6: 33.369
- **Magnitude:** 430.64 | **LOC:** 680 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%), Guard Balance (formerly Safety Score) (60.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `psutil_net_if_flags` **(Many-Argument Workhorses)** (Impact: 95.8)
    * *Intent:* /* * Get all of the NIC flags and return them. */
  * `psutil_get_nic_speed` **(Compute Cores)** (Impact: 80.4)
    * *Intent:* // net_if_stats() macOS/BSD implementation. #ifdef PSUTIL_HAS_NET_IF_DUPLEX_SPEED
  * `psutil_net_if_addrs` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* /* * Return NICs information a-la ifconfig as a list of tuples. * TODO: on Solaris we won't get any ...
  * `psutil_convert_ipaddr` **(Many-Argument Workhorses)** (Impact: 33.0)
    * *Intent:* #include <sys/sockio.h> #endif #if defined(PSUTIL_AIX) #include <netdb.h> #endif #include "../../arc...
  * `psutil_net_if_duplex_speed` **(Compute Cores)** (Impact: 17.5)
    * *Intent:* /* * Return stats about a particular network interface. * References: * http://www.i-scream.org/libs...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 64`, `args: 65`, `func_start: 8`, `class_start: 8`
* *Risk/State:* `state_mutation: 41`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 5`, `api: 7`, `import: 23`
* *Defense:* `safety: 2`, `immutability_locks: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` init.h, Python.h, ifaddrs.h, errno.h, ifaddrs.h, if_packet.h, types.h, if.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.548)
- **Top Global Matches:** file_cluster_3: 6.548, file_cluster_8: 20.503, file_cluster_6: 33.366
- **Magnitude:** 417.66 | **LOC:** 469 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `psutil_gather_inet` **(Many-Argument Workhorses)** (Impact: 101.2)
    * *Intent:* // Reference: // https://github.com/freebsd/freebsd/blob/master/usr.bin/sockstat/sockstat.c
  * `psutil_gather_unix` **(Many-Argument Workhorses)** (Impact: 50.5)
  * `psutil_net_connections` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `psutil_populate_xfiles` **(C Struct Operations)** (Impact: 11.6)
    * *Intent:* #include <sys/file.h> #include <sys/socketvar.h> // for struct xsocket #include <sys/un.h> #include ...
  * `psutil_get_file_from_sock` **(C Struct Operations)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 64 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 74`, `args: 20`, `func_start: 6`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 69`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 4`, `immutability_locks: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` init.h, Python.h, inet.h, in.h, in_pcb.h, ip.h, tcp_var.h, file.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_posix.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.304)
- **Top Global Matches:** file_cluster_12: 7.304, file_cluster_15: 7.517, file_cluster_13: 9.119
- **Magnitude:** 408.78 | **LOC:** 472 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 1.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (40.3%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 85.9599% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ps` **(Many-Argument Workhorses)** (Impact: 22.8)
    * *Intent:* """Wrapper for calling the ps command with a little bit of cross-platform support for a narrow range...
  * `test_users` **(Defensive Guards)** (Impact: 19.8)
  * `test_users_started` **(Compute Cores)** (Impact: 18.7)
  * `test_pids` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* # Note: this test might fail if the OS is starting/killing # other processes in the meantime pids_ps...
  * `test_disk_usage` **(Defensive Guards)** (Impact: 11.0)
    * *Intent:* # AIX can return '-' in df output instead of numbers, e.g. for /proc
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 139`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 102`, `unreferenced_by_name: 24`
* *Architecture:* `io: 3`, `api: 33`, `import: 28`
* *Defense:* `safety: 39`, `doc: 4`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .AARCH64, .HAS_NET_IO_COUNTERS, .PYTHON_EXE, .PsutilTestCase, .pytest, .retry_on_failure, .sh, .skip_on_access_denied...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_psaix.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.251)
- **Top Global Matches:** file_cluster_12: 6.251, file_cluster_15: 8.505, file_cluster_11: 9.274
- **Magnitude:** 379.46 | **LOC:** 547 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 6.001; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.8%), Connectivity (formerly Api Exposure) (60.0%)
- **Documentation Coverage:** 69.7674% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exe` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* # there is no way to get executable path in AIX other than to guess, # and guessing is more complex ...
  * `net_connections` **(Compute Cores)** (Impact: 11.6)
    * *Intent:* """Return socket connections. If pid == -1 return system-wide connections (as opposed to connections...
  * `open_files` **(Type Conversions)** (Impact: 9.7)
    * *Intent:* # TODO rewrite without using procfiles (stat /proc/pid/fd/* and then # find matching name of the ino...
  * `disk_partitions` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* """Return system disk partitions."""
  * `net_if_stats` **(I/O & Config Routines)** (Impact: 7.8)
    * *Intent:* """Get NIC stats (isup, duplex, speed, mtu)."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 142`, `args: 44`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 86`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 27`, `api: 43`, `import: 20`
* *Defense:* `safety: 11`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.001
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.155232
  * `Imports (Out-Degree: 4):` ._common, ._ntuples, ._psposix, ._psutil_aix, functools, glob, os, re...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `psutil-7.2.2/tests/test_testutils.py` (PYTHON) | Magnitude: 198.48 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 257, structural_boundaries: 210, safety: 63, core_var_decl: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `psutil-7.2.2/scripts/internal/print_announce.py` (PYTHON) | Magnitude: 67.02 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 44, core_var_decl: 28, state_mutation: 26, design_snake_case: 18
- `psutil-7.2.2/tests/test_bsd.py` (PYTHON) | Magnitude: 450.2 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 412, structural_boundaries: 182, core_var_decl: 123, design_snake_case: 119

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `psutil-7.2.2/scripts/pmap.py` (PYTHON) | Magnitude: 21.34 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 7, state_mutation: 5, debug_prints: 5
- `psutil-7.2.2/tests/test_osx.py` (PYTHON) | Magnitude: 135.24 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 79, core_var_decl: 50, design_snake_case: 50
- `psutil-7.2.2/psutil/arch/all/errors.c` (C) | Magnitude: 22.64 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 45, args: 20, pointers: 8, structural_boundaries: 7
- `psutil-7.2.2/psutil/arch/osx/sys.c` (C) | Magnitude: 8.36 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, import: 3, pointers: 3
- `psutil-7.2.2/scripts/pidof.py` (PYTHON) | Magnitude: 20.3 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, branch: 8, structural_boundaries: 5, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `psutil-7.2.2/psutil/arch/osx/mem.c` (C) | Magnitude: 39.92 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 10, pointers: 9, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `psutil-7.2.2/psutil/arch/bsd/cpu.c` (C) | Magnitude: 26.6 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, pointers: 10, import: 6, state_mutation: 5
- `psutil-7.2.2/psutil/arch/osx/init.h` (C) | Magnitude: 53.9 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: pointers: 97, api: 38, args: 37, structural_boundaries: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `psutil-7.2.2/psutil/__init__.py` -> **Severity: 1.234** (Bridge: 0.0123 * Flux: 100.0%)
- `psutil-7.2.2/psutil/arch/posix/sysctl.c` -> **Severity: 0.063** (Bridge: 0.0006 * Flux: 99.9874%)
- `psutil-7.2.2/psutil/_common.py` -> **Severity: 0.035** (Bridge: 0.0004 * Flux: 100.0%)
- `psutil-7.2.2/psutil/_pslinux.py` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 100.0%)
- `psutil-7.2.2/psutil/arch/windows/init.c` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `psutil-7.2.2/psutil/__init__.py` -> **Severity: 23.741** (Embedded: 0.3077 * Error Risk: 77.158%)
- `psutil-7.2.2/psutil/arch/all/errors.c` -> **Severity: 18.463** (Embedded: 0.3582 * Error Risk: 51.5459%)
- `psutil-7.2.2/psutil/_common.py` -> **Severity: 16.872** (Embedded: 0.2272 * Error Risk: 74.2719%)
- `psutil-7.2.2/psutil/arch/all/str.c` -> **Severity: 14.834** (Embedded: 0.2499 * Error Risk: 59.3619%)
- `psutil-7.2.2/psutil/_ntuples.py` -> **Severity: 12.722** (Embedded: 0.1809 * Error Risk: 70.3145%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `psutil-7.2.2/psutil/_common.py` -> **Severity: 7599.531** (Blast Radius: 197.588 * Doc Risk: 38.4615%)
- `psutil-7.2.2/psutil/arch/all/errors.c` -> **Severity: 3308.0** (Blast Radius: 33.08 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/arch/all/str.c` -> **Severity: 2712.7** (Blast Radius: 27.127 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/arch/posix/sysctl.c` -> **Severity: 1109.1** (Blast Radius: 11.091 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/__init__.py` -> **Severity: 1042.631** (Blast Radius: 48.737 * Doc Risk: 21.393%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 143 literal sites + 7 sites through wrappers = 150
- **`memory_alloc`:** 262 literal sites + 11 sites through wrappers = 273
- **`panics_and_aborts`:** 440 literal sites + 13 sites through wrappers = 453

- `psutil_badargs` (function, panics_and_aborts, primitive): 11 call sites in 3 files -- `psutil-7.2.2/psutil/arch/all/errors.c`
- `sa_dup` (function, memory_alloc, primitive): 4 call sites in 1 files -- `psutil-7.2.2/psutil/arch/aix/ifaddrs.c`
- `freeifaddrs` (function, memory_alloc, primitive): 3 call sites in 2 files -- `psutil-7.2.2/psutil/arch/aix/ifaddrs.c`
- `exit_with` (function, debug_prints, primitive): 2 call sites in 1 files -- `psutil-7.2.2/scripts/internal/git_pre_commit.py`
- `exit_with` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `psutil-7.2.2/scripts/internal/git_pre_commit.py`
- `print_header` (function, debug_prints, primitive): 2 call sites in 1 files -- `psutil-7.2.2/scripts/internal/print_api_speed.py`
- `psutil_kiflist_clear` (function, memory_alloc, primitive): 2 call sites in 1 files -- `psutil-7.2.2/psutil/arch/netbsd/socks.c`
- `psutil_kpcblist_clear` (function, memory_alloc, primitive): 2 call sites in 1 files -- `psutil-7.2.2/psutil/arch/netbsd/socks.c`
- `safe_print` (function, debug_prints, primitive): 2 call sites in 1 files -- `psutil-7.2.2/scripts/pmap.py`
- `print_header` (function, debug_prints, primitive): 1 call sites in 1 files -- `psutil-7.2.2/scripts/internal/print_downloads.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 8509 call pairs -- scoped 27.1%, unique 5.2%, ambiguous 2.6%, external 65.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 6175 | 35.3% | 0.0% | 3.3% | 61.4% |
| c | 2331 | 5.4% | 18.9% | 0.7% | 74.9% |
| shell | 3 | 33.3% | 0.0% | 0.0% | 66.7% |

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
