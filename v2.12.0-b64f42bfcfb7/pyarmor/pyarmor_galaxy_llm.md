# ARCHITECTURAL_BRIEF: pyarmor
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dashingsoft/pyarmor.git` |
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
- **Scope:** 86 analyzed artifact(s), 8235 LOC.
- **Load-bearing artifact:** `tests/test-header.sh` -- 9 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/test-pyarmor.py` -- pulls in 13 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/product.key` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 263 |
| Analyzed Artifacts (Scanned) | 86 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 177 |
| Total LOC | 8235 |
| Volatility Index | 0.023 |
| % Scanned of codebase = | 32.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8018 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5271 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.125 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 55 | 3284 | 64.0% |
| SHELL | 15 | 4556 | 17.4% |
| PLAINTEXT | 7 | 3 | 8.1% |
| MARKDOWN | 5 | 0 | 5.8% |
| MAKEFILE | 3 | 332 | 3.5% |
| C | 1 | 60 | 1.2% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 79 |
| unknown | unknown | 3 |
| utf-8 | bom | 3 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, Parameter Forwarders Files 23%, Declarative / Non-Code 15%, Large Core Modules 7%, Large Core Modules (3) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 74 | 86.0% |
| Unknown | 3 | 3.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 10.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 177*

**Composition by Extension & Reason:**
- `.py`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.rst`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bat`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.8`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.9`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.02`: 1x Excluded (Unsupported Extension: '.02')
- `.cfg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tri`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.0 | 18.2 | 11.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.7 | 47.7 | 54.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 52.8 | 9.2 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.7 | 2.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.2 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.9 | 85.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 68.3 | 1.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 12 | 4 | 0 | `gh.py` |
| cleanup | 78 | 21 | 3 | `tests/function-test.sh` |
| guards | 182 | 30 | 4 | `tests/test-sppmode.py` |
| danger | 1858 | 40 | 30 | `tests/function-test.sh` |
| concurrency | 96 | 22 | 3 | `tests/function-test.sh` |
| connectivity | 373 | 47 | 13 | `tests/test-sppmode.py` |
| io | 2232 | 38 | 27 | `tests/function-test.sh` |
| crypto | 1 | 1 | 0 | `plugins/check_multi_mac.py` |
| ipc | 23 | 12 | 1 | `tests.8/Makefile` |
| time | 11 | 5 | 0 | `tests/integration-test.sh` |
| serialization | 2 | 1 | 0 | `tests.8/Makefile` |
| regex | 50 | 9 | 0 | `tests/integration-test.sh` |
| events | 26 | 6 | 0 | `tests/test-sppmode.py` |
| tests | 219 | 18 | 6 | `tests/test-sppmode.py` |
| docs | 224 | 8 | 0 | `tests.9/script_factory.py` |
| debt | 602 | 41 | 12 | `tests/function-test.sh` |
| mutation | 2237 | 58 | 64 | `tests/test-pyarmor.py` |
| dead_code | 213 | 23 | 8 | `tests/test-sppmode.py` |
| credential | 2 | 2 | 0 | `tests/function-test.sh` |
| threat | 1 | 1 | 0 | `plugins/check_multi_mac.py` |
| ml_ai | 9 | 2 | 0 | `tests/test-header.sh` |
| ui | 20 | 2 | 0 | `tests/integration-test.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/function-test.sh` (Hits: 814)
- `tests/integration-test.sh` (Hits: 468)
- `tests/accept-test.sh` (Hits: 218)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **test-header.sh** (`tests/test-header.sh`) — 9 inbound connections
2. **script_factory.py** (`tests.9/script_factory.py`) — 2 inbound connections
3. **pub_foo.py** (`tests/data/pub_foo.py`) — 2 inbound connections
4. **LICENSE.7** (`LICENSE.7`) — 1 inbound connections
5. **check_docker.py** (`plugins/check_docker.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test-pyarmor.py** (`tests/test-pyarmor.py`) — 13 outbound dependencies
2. **test-trial-pyarmor.py** (`tests/test-trial-pyarmor.py`) — 12 outbound dependencies
3. **accept_test.py** (`tests.8/accept_test.py`) — 8 outbound dependencies
4. **test-sppmode.py** (`tests/test-sppmode.py`) — 8 outbound dependencies
5. **gh.py** (`gh.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_list_comp` **(Compute Cores)** (@ `tests/test-sppmode.py`) -> Impact: **21.9** | LOC: 14
- `test_set_comp` **(Compute Cores)** (@ `tests/test-sppmode.py`) -> Impact: **21.9** | LOC: 14
- `do_ud` **(Compute Cores)** (@ `gh.py`) -> Impact: **21.0** | LOC: 39
- `test_boolop` **(Compute Cores)** (@ `tests/test-sppmode.py`) -> Impact: **19.1** | LOC: 14
- `test_dict_comp` **(Compute Cores)** (@ `tests/test-sppmode.py`) -> Impact: **19.0** | LOC: 12
- `query_interface_mac_address` **(Stateful Encapsulated Methods)** (@ `plugins/extra_hdinfo.c`) -> Impact: **13.9** | LOC: 38
  * *Intent:* #include <stdio.h> #include <string.h> #include <unistd.h> #include <sys/ioctl.h> #include <sys/socket.h> #include <net/if.h>
- `do_cii` **(Compute Cores)** (@ `gh.py`) -> Impact: **12.9** | LOC: 15
- `test_with_statement` **(Compute Cores)** (@ `tests/test-sppmode.py`) -> Impact: **12.6** | LOC: 83
- `_generate_ndarray_function_code` **(Stateful Encapsulated Methods)** (@ `tests/data/no_wrap.py`) -> Impact: **12.5** | LOC: 26
  * *Intent:* """Generate function for ndarray op by handle and function op_name."""
- `test_raise_in_while` **(Defensive Guards)** (@ `tests/test-sppmode.py`) -> Impact: **12.0** | LOC: 43

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 3 | 15000.0 | 0.0% | 0.0% |
| `tests` | 18 | 2762.2 | 22.85% | 0.0% |
| `tests.8` | 5 | 465.04 | 38.83% | 66.69% |
| `__monolith__` | 7 | 353.96 | 6.81% | 14.26% |
| `plugins` | 9 | 353.74 | 30.34% | 8.39% |
| `tests.9` | 5 | 286.38 | 29.61% | 43.55% |
| `tests.8/samples` | 5 | 72.82 | 18.47% | 0.0% |
| `tests.8/samples/pyfeatures` | 4 | 46.66 | 7.65% | 20.44% |
| `tests.8/samples/joker` | 3 | 29.8 | 4.41% | 0.0% |
| `scripts` | 1 | 1.81 | 17.36% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `tests.8/test_pack.py` -> **99.9859%** Exposure
- `tests.9/accept_test.py` -> **99.9797%** Exposure
- `tests.8/accept_test.py` -> **99.9776%** Exposure
- `tests.9/accept_test_nogil.py` -> **99.972%** Exposure
- `tests.8/test_pyfeatures.py` -> **99.9166%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `gh.py` -> **100.0%** Exposure
- `plugins/check_multi_mac.py` -> **100.0%** Exposure
- `tests.8/test_pyfeatures.py` -> **100.0%** Exposure
- `tests.8/accept_test.py` -> **99.9992%** Exposure
- `plugins/check_gpu.py` -> **99.9986%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test-sppmode.py` -> **48** Orphaned Functions | **4** Duplicates
- `tests.8/accept_test.py` -> **35** Orphaned Functions | **0** Duplicates
- `tests/test-pyarmor.py` -> **24** Orphaned Functions | **0** Duplicates
- `gh.py` -> **14** Orphaned Functions | **0** Duplicates
- `tests.9/accept_test.py` -> **11** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/system-test.sh` -> **68.2759%** Exposure
- `tests/function-test.sh` -> **13.9011%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `153` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/product.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/public.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pyshield.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test-sppmode.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.784)
- **Top Global Matches:** file_cluster_12: 5.784, file_cluster_15: 8.411, file_cluster_7: 9.128
- **Magnitude:** 612.2 | **LOC:** 741 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 8.464; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (43.3%), Connectivity (formerly Api Exposure) (13.1%)
- **Documentation Coverage:** 98.7879% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_list_comp` **(Compute Cores)** (Impact: 21.9)
  * `test_set_comp` **(Compute Cores)** (Impact: 21.9)
  * `test_boolop` **(Compute Cores)** (Impact: 19.1)
  * `test_dict_comp` **(Compute Cores)** (Impact: 19.0)
  * `test_with_statement` **(Compute Cores)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 218`, `args: 94`, `func_start: 93`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 111`, `fragile_debt: 3`, `duplicate_logic: 4`, `unreferenced_by_name: 48`
* *Architecture:* `io: 6`, `api: 80`, `import: 10`
* *Defense:* `safety: 45`, `doc: 1`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` decimal, gc, os, os.path, sys, tempfile, unittest, weakref
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/function-test.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 4.891)
- **Top Global Matches:** file_cluster_14: 4.891, file_cluster_7: 11.362, file_cluster_5: 14.979
- **Magnitude:** 418.2 | **LOC:** 2161 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.8%), Credential Material (formerly Secrets Risk) (13.9%), Complexity Load (formerly Cognitive Load) (6.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 313`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 901`, `state_mutation: 95`, `fragile_debt: 1`
* *Architecture:* `io: 814`, `concurrency: 5`, `import: 1`
* *Defense:* `test: 6`, `sync_locks: 22`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-header.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/integration-test.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.37)
- **Top Global Matches:** file_cluster_7: 8.37, file_cluster_12: 9.824, file_cluster_14: 9.829
- **Magnitude:** 397.36 | **LOC:** 1109 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (21.6%), Dead Code Surface (formerly Dead Code) (14.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `csih_stacktrace` **(I/O & Config Routines)** (Impact: 7.1)
    * *Intent:* # ====================================================================== # Routine: csih_stacktrace ...
  * `next_month` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* # ====================================================================== # Routine: next_month # Pri...
  * `csih_error_multi` **(Defensive Guards)** (Impact: 5.0)
    * *Intent:* # ====================================================================== # Routine: csih_error_multi...
  * `csih_error` **(Defensive Guards)** (Impact: 3.4)
    * *Intent:* # ====================================================================== # Routine: csih_error # Pri...
  * `csih_error_recoverable` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* # ====================================================================== # Routine: csih_error_recov...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 392`, `args: 8`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 85`, `state_mutation: 54`, `dead_code: 15`, `fragile_debt: 2`
* *Architecture:* `io: 468`
* *Defense:* `safety: 7`, `test: 20`, `sync_locks: 2`, `immutability_locks: 24`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gh.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.09)
- **Top Global Matches:** file_cluster_12: 6.09, file_cluster_15: 8.587, file_cluster_7: 8.744
- **Magnitude:** 310.06 | **LOC:** 512 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 8.464; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_ud` **(Compute Cores)** (Impact: 21.0)
  * `do_cii` **(Compute Cores)** (Impact: 12.9)
  * `do_vd` **(Compute Cores)** (Impact: 11.8)
  * `do_ld` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* '''List discussions'''
  * `_find_discussion` **(Stateful Encapsulated Methods)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 47`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 80`, `fragile_debt: 1`, `unreferenced_by_name: 14`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `safety: 4`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cmd, configparser, datetime, json, shlex, string, subprocess
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests.8/accept_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.667)
- **Top Global Matches:** file_cluster_15: 5.667, file_cluster_11: 7.201, file_cluster_13: 7.398
- **Magnitude:** 291.22 | **LOC:** 398 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.1%), Complexity Load (formerly Cognitive Load) (78.0%)
- **Documentation Coverage:** 96.583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify_dist_foo_fail` **(Compute Cores)** (Impact: 6.3)
  * `wrap` **(Compute Cores)** (Impact: 6.2)
  * `test_mp` **(Compute Cores)** (Impact: 4.8)
  * `test_mp_with_bcc` **(Compute Cores)** (Impact: 4.8)
  * `test_thread` **(Compute Cores)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 84`, `args: 49`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `state_mutation: 75`, `unreferenced_by_name: 35`
* *Architecture:* `io: 23`, `api: 50`, `import: 7`
* *Defense:* `safety: 3`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` joker, logging, os, shutil, struct, test.support, time, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test-header.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.987)
- **Top Global Matches:** file_cluster_7: 7.987, file_cluster_12: 9.294, file_cluster_14: 10.01
- **Magnitude:** 257.78 | **LOC:** 433 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); blast radius 73.215; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (81.0%), Connectivity (formerly Api Exposure) (52.8%), Complexity Load (formerly Cognitive Load) (31.1%), Dead Code Surface (formerly Dead Code) (7.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_file_content` **(Compute Cores)** (Impact: 10.3)
    * *Intent:* # ====================================================================== # Routine: check_file_conte...
  * `csih_stacktrace` **(I/O & Config Routines)** (Impact: 7.1)
    * *Intent:* # ====================================================================== # Routine: csih_stacktrace ...
  * `next_month` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* # ====================================================================== # Routine: next_month # Pri...
  * `csih_error_multi` **(Defensive Guards)** (Impact: 5.0)
    * *Intent:* # ====================================================================== # Routine: csih_error_multi...
  * `update_pytransform_hash256` **(Compute Cores)** (Impact: 4.5)
    * *Intent:* # ====================================================================== # Routine: update_pytransfo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 122`, `args: 25`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 69`, `dead_code: 2`, `fragile_debt: 5`
* *Architecture:* `io: 21`, `api: 8`
* *Defense:* `safety: 7`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 73.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.105882
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `tests/test-pyarmor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.592)
- **Top Global Matches:** file_cluster_15: 6.592, file_cluster_11: 7.484, file_cluster_12: 7.762
- **Magnitude:** 235.98 | **LOC:** 455 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 8.464; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.8%), Complexity Load (formerly Cognitive Load) (38.7%), Connectivity (formerly Api Exposure) (11.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_encrypt_files` **(Compute Cores)** (Impact: 4.6)
  * `setupModuleTest` **(I/O & Config Routines)** (Impact: 3.9)
  * `test_do_encrypt_main` **(I/O & Config Routines)** (Impact: 3.0)
  * `test_do_license` **(I/O & Config Routines)** (Impact: 2.9)
  * `test_parse_file_args` **(I/O & Config Routines)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 68`, `args: 31`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 107`, `unreferenced_by_name: 24`
* *Architecture:* `io: 118`, `api: 32`, `import: 14`
* *Defense:* `safety: 4`, `test: 29`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StringIO, io, logging, os, py_compile, shutil, sys, tarfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/check_ntp_time.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.046)
- **Top Global Matches:** file_cluster_12: 6.046, file_cluster_15: 7.034, file_cluster_16: 7.582
- **Magnitude:** 174.84 | **LOC:** 483 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 9.903; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.4%), Connectivity (formerly Api Exposure) (48.9%)
- **Documentation Coverage:** 3.6585% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ref_id_to_text` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* """Convert a reference clock identifier to text according to its stratum. Parameters: ref_id -- refe...
  * `stratum_to_text` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* """Convert a stratum value to text. Parameters: stratum -- NTP stratum Returns: corresponding messag...
  * `request` **(Many-Argument Workhorses)** (Impact: 7.2)
    * *Intent:* """Query a NTP server. Parameters: host -- server name/address version -- NTP version to use port --...
  * `leap_to_text` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* """Convert a leap indicator to text. Parameters: leap -- leap indicator value Returns: corresponding...
  * `mode_to_text` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* """Convert a NTP mode value to text. Parameters: mode -- NTP mode Returns: corresponding message Rai...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 66`, `args: 24`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 52`
* *Architecture:* `io: 6`, `api: 22`, `import: 7`
* *Defense:* `safety: 8`, `doc: 49`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.903
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011765
  * `Imports (Out-Degree: 0):` ctypes, datetime, pytransform, socket, struct, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/accept-test.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 4.644)
- **Top Global Matches:** file_cluster_14: 4.644, file_cluster_7: 11.046, file_cluster_5: 14.734
- **Magnitude:** 117.96 | **LOC:** 579 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.0%), Complexity Load (formerly Cognitive Load) (6.3%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 71`
* *Risk/State:* `safety_bypasses: 235`, `state_mutation: 22`, `fragile_debt: 1`
* *Architecture:* `io: 218`, `api: 1`, `import: 1`
* *Defense:* `sync_locks: 9`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-header.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test-trial-pyarmor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.346)
- **Top Global Matches:** file_cluster_12: 7.346, file_cluster_15: 7.489, file_cluster_11: 8.093
- **Magnitude:** 104.48 | **LOC:** 129 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 8.464; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (72.2%), Complexity Load (formerly Cognitive Load) (41.5%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 91.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_encrypt_files` **(Compute Cores)** (Impact: 4.7)
  * `setupModuleTest` **(I/O & Config Routines)** (Impact: 3.9)
  * `test_make_capsule` **(I/O & Config Routines)** (Impact: 2.1)
    * *Intent:* '''Check all capsules generated are same.'''
  * `test_usage` **(Parameter Forwarders)** (Impact: 1.8)
  * `test_make_license` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 32`, `args: 12`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 36`, `unreferenced_by_name: 9`
* *Architecture:* `io: 27`, `api: 13`, `import: 13`
* *Defense:* `safety: 4`, `doc: 1`, `test: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StringIO, io, os, shutil, subprocess, sys, tarfile, tempfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests.9/accept_test_nogil.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.422)
- **Top Global Matches:** file_cluster_15: 6.422, file_cluster_12: 6.582, file_cluster_16: 8.127
- **Magnitude:** 91.86 | **LOC:** 136 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (64.9%), Guard Balance (formerly Safety Score) (56.1%)
- **Documentation Coverage:** 96.583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iter_scripts` **(Compute Cores)** (Impact: 7.2)
  * `iter_samples` **(Compute Cores)** (Impact: 6.0)
  * `_test_target` **(Encapsulated Accessors)** (Impact: 4.3)
  * `build_v9_script` **(Parameter Forwarders)** (Impact: 2.5)
  * `verify_script_nogil_pass` **(Defensive Guards)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 40`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`, `unreferenced_by_name: 11`
* *Architecture:* `io: 12`, `api: 19`, `import: 7`
* *Defense:* `safety: 1`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` logging, os, script_factory, shutil, subprocess, test.support, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test-merge.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 5.057)
- **Top Global Matches:** file_cluster_14: 5.057, file_cluster_7: 8.034, file_cluster_5: 12.067
- **Magnitude:** 91.66 | **LOC:** 169 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (86.1%), Complexity Load (formerly Cognitive Load) (35.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 77`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 14`, `fragile_debt: 1`
* *Architecture:* `io: 35`, `import: 1`
* *Defense:* `test: 4`, `sync_locks: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-header.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests.9/accept_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.409)
- **Top Global Matches:** file_cluster_15: 6.409, file_cluster_12: 6.623, file_cluster_16: 7.992
- **Magnitude:** 89.7 | **LOC:** 133 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.7%), Complexity Load (formerly Cognitive Load) (62.1%)
- **Documentation Coverage:** 96.583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iter_scripts` **(Compute Cores)** (Impact: 7.2)
  * `iter_samples` **(Compute Cores)** (Impact: 6.0)
  * `_test_target` **(Encapsulated Accessors)** (Impact: 4.3)
  * `build_v9_script` **(Parameter Forwarders)** (Impact: 2.5)
  * `verify_script_pass` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 37`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `unreferenced_by_name: 11`
* *Architecture:* `io: 9`, `api: 19`, `import: 6`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` logging, os, script_factory, shutil, test.support, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests.8/test_pyfeatures.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.533)
- **Top Global Matches:** file_cluster_15: 5.533, file_cluster_11: 6.85, file_cluster_16: 6.983
- **Magnitude:** 84.16 | **LOC:** 99 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 8.464; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (66.6%), Complexity Load (formerly Cognitive Load) (56.8%)
- **Documentation Coverage:** 96.583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify_script_pass` **(Parameter Forwarders)** (Impact: 4.2)
  * `verify_script_fail` **(Parameter Forwarders)** (Impact: 4.2)
  * `test_simple_issues` **(Parameter Forwarders)** (Impact: 3.3)
  * `test_rft_issues` **(Parameter Forwarders)** (Impact: 3.3)
  * `assert_python_ok` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 27`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 20`, `unreferenced_by_name: 7`
* *Architecture:* `io: 2`, `api: 13`, `import: 6`
* *Defense:* `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` glob, logging, os, shutil, test.support, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests.9/script_factory.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_12: 12.383, file_cluster_15: 12.601
- **Magnitude:** 83.56 | **LOC:** 922 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 22.853; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.2%), Guard Balance (formerly Safety Score) (54.7%), Concurrency Surface (formerly Concurrency) (28.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `script_generator` **(Compute Cores)** (Impact: 11.3)
    * *Intent:* """生成用于测试各种 Python 功能的脚本 参数: catalog (str): tpl_catalog 或者 script_catalog 中的分类名称 生成: (name, source) ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 8`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 49`, `dead_code: 3`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 1`, `import: 4`
* *Defense:* `doc: 143`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023529
  * `Imports (Out-Degree: 0):` itertools, string, sys, textwrap
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/system-test.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 4.589)
- **Top Global Matches:** file_cluster_14: 4.589, file_cluster_7: 9.377, file_cluster_5: 13.251
- **Magnitude:** 82.82 | **LOC:** 704 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (88.7%), Credential Material (formerly Secrets Risk) (68.3%), Complexity Load (formerly Cognitive Load) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 96`
* *Risk/State:* `safety_bypasses: 168`, `state_mutation: 11`, `fragile_debt: 2`
* *Architecture:* `io: 205`, `concurrency: 1`, `import: 1`
* *Defense:* `test: 2`, `sync_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-header.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests.8/test_pack.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.551)
- **Top Global Matches:** file_cluster_15: 5.551, file_cluster_11: 6.761, file_cluster_2: 6.775
- **Magnitude:** 69.36 | **LOC:** 118 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 8.464; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (56.4%), Complexity Load (formerly Cognitive Load) (35.6%)
- **Documentation Coverage:** 96.583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify_bundle` **(Parameter Forwarders)** (Impact: 2.2)
  * `assert_python_ok` **(Parameter Forwarders)** (Impact: 2.0)
  * `assert_python_failure` **(Parameter Forwarders)** (Impact: 2.0)
  * `setUp` **(Parameter Forwarders)** (Impact: 1.9)
  * `pyarmor_cmd` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 27`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 10`
* *Architecture:* `io: 3`, `api: 16`, `import: 6`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` logging, os, shutil, subprocess, test.support, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/vm-test.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 5.738)
- **Top Global Matches:** file_cluster_14: 5.738, file_cluster_7: 13.114, file_cluster_5: 16.581
- **Magnitude:** 64.82 | **LOC:** 59 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.7%), Complexity Load (formerly Cognitive Load) (36.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 40`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 15`
* *Architecture:* `io: 9`
* *Defense:* `safety: 1`, `sync_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/packer-test.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 4.634)
- **Top Global Matches:** file_cluster_14: 4.634, file_cluster_7: 10.713, file_cluster_5: 14.433
- **Magnitude:** 61.4 | **LOC:** 310 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (94.1%), Complexity Load (formerly Cognitive Load) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 56`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 15`, `fragile_debt: 1`
* *Architecture:* `io: 107`, `import: 1`
* *Defense:* `sync_locks: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-header.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.778)
- **Top Global Matches:** file_cluster_9: 7.778, file_cluster_15: 11.511, file_cluster_16: 11.9
- **Magnitude:** 59.98 | **LOC:** 153 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (34.4%), Complexity Load (formerly Cognitive Load) (23.5%), Connectivity (formerly Api Exposure) (6.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unit` **(I/O & Config Routines)** (Impact: 7.4)
  * `trial` **(I/O & Config Routines)** (Impact: 7.4)
  * `test` **(I/O & Config Routines)** (Impact: 7.3)
  * `stest` **(I/O & Config Routines)** (Impact: 7.3)
  * `ftest` **(I/O & Config Routines)** (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 38`, `func_start: 9`
* *Risk/State:* `dead_code: 4`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 4`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cross-test.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 5.988)
- **Top Global Matches:** file_cluster_14: 5.988, file_cluster_7: 10.064, file_cluster_5: 13.465
- **Magnitude:** 54.7 | **LOC:** 266 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (85.9%), Complexity Load (formerly Cognitive Load) (6.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_cross_runtime` **(I/O & Config Routines)** (Impact: 4.6)
    * *Intent:* # ====================================================================== # # Generate runtime packag...
  * `bootstrap` **(I/O & Config Routines)** (Impact: 3.8)
    * *Intent:* # ====================================================================== # # Bootstrap: help and ver...
  * `test_cross_publish` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* # ====================================================================== # # Cross Publish # # =====...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 30`, `args: 1`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 6`, `fragile_debt: 1`
* *Architecture:* `io: 52`, `import: 1`
* *Defense:* `sync_locks: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-header.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/super-test.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 4.175)
- **Top Global Matches:** file_cluster_14: 4.175, file_cluster_7: 9.232, file_cluster_5: 13.052
- **Magnitude:** 53.7 | **LOC:** 91 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 8.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (90.4%), Complexity Load (formerly Cognitive Load) (33.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 47`, `args: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 11`
* *Architecture:* `io: 10`, `import: 1`
* *Defense:* `safety: 3`, `sync_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-header.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/test-trial-pyarmor.py` (PYTHON) | Magnitude: 104.48 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 77, state_mutation: 36, structural_boundaries: 32, core_var_decl: 28

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tests.8/accept_test.py` -> Churn: **81.09%** | Cog Load: 78.0334% | Debt: 99.9776%
- `tests.9/accept_test.py` -> Churn: **78.72%** | Cog Load: 62.1377% | Debt: 99.9797%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests.8/accept_test.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 291.22
- `tests.9/accept_test_nogil.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 91.86
- `tests.9/accept_test.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 89.7
- `tests.9/script_factory.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 83.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tests.8/samples/joker/__init__.py` -> **Severity: 0.005** (Bridge: 0.0003 * Flux: 16.7982%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/test-header.sh` -> **Severity: 8.576** (Embedded: 0.1059 * Error Risk: 80.9974%)
- `tests.9/script_factory.py` -> **Severity: 1.286** (Embedded: 0.0235 * Error Risk: 54.6516%)
- `tests/data/mfoo.py` -> **Severity: 0.904** (Embedded: 0.0157 * Error Risk: 57.6188%)
- `tests.8/samples/joker/fibo.py` -> **Severity: 0.885** (Embedded: 0.0157 * Error Risk: 56.3934%)
- `plugins/check_multi_mac.py` -> **Severity: 0.775** (Embedded: 0.0118 * Error Risk: 65.8618%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/data/pub_foo.py` -> **Severity: 8226.3** (Blast Radius: 82.263 * Doc Risk: 100.0%)
- `tests/test-header.sh` -> **Severity: 7321.5** (Blast Radius: 73.215 * Doc Risk: 100.0%)
- `tests/data/mfoo.py` -> **Severity: 4340.8** (Blast Radius: 43.408 * Doc Risk: 100.0%)
- `tests/data/tfoo.py` -> **Severity: 4340.8** (Blast Radius: 43.408 * Doc Risk: 100.0%)
- `tests.8/samples/benchmark.py` -> **Severity: 1565.8** (Blast Radius: 15.658 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 579 literal sites + 5 sites through wrappers = 584

- `say_after` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/data/t_async.py`
- `hello` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests.8/samples/foo.py`
- `info` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests.8/samples/mp.py`
- `info` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests.8/samples/td.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1508 call pairs -- scoped 30.3%, unique 0.0%, ambiguous 0.2%, external 69.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 977 | 29.3% | 0.0% | 0.3% | 70.4% |
| shell | 521 | 32.4% | 0.0% | 0.0% | 67.6% |
| c | 10 | 20.0% | 0.0% | 0.0% | 80.0% |

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
