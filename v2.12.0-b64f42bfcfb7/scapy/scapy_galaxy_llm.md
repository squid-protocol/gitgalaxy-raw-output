# ARCHITECTURAL_BRIEF: scapy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/secdev/scapy.git` |
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
- **Scope:** 405 analyzed artifact(s), 162200 LOC.
- **Load-bearing artifact:** `scapy/packet.py` -- 246 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `scapy/utils.py` -- pulls in 51 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `doc/notebooks/tls/raw_data/pki/srv_key.pem` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 867 |
| Analyzed Artifacts (Scanned) | 405 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 462 |
| Total LOC | 162200 |
| Volatility Index | 0.02 |
| % Scanned of codebase = | 46.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3578 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2626 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 29.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3759 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 380 | 161726 | 93.8% |
| YAML | 7 | 345 | 1.7% |
| PLAINTEXT | 7 | 5 | 1.7% |
| MARKDOWN | 6 | 0 | 1.5% |
| SHELL | 3 | 75 | 0.7% |
| BATCH | 2 | 49 | 0.5% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 400 |
| unknown | unknown | 5 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 28%, Large Core Modules (3) 24%, Data / Markup / Trivial 14%, Declarative / Non-Code 13%, Large Core Modules (2) 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 392 | 96.8% |
| Unknown | 5 | 1.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 2.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 462*

**Composition by Extension & Reason:**
- `.uts`: 209x Excluded (Unsupported Extension: '.uts'), 3x Unsupported Format (.uts)
- `.png`: 45x Excluded (Explicitly Denied Extension: '.png')
- `.rst`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gz`: 24x Excluded (Explicitly Denied Extension: '.gz')
- `.raw`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3186 LOC), 1x Excluded (Machine-Generated Source Code Signature: 228 LOC)
- `.pcap`: 15x Excluded (Unsupported Extension: '.pcap'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ipynb`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.utsc`: 7x Excluded (Unsupported Extension: '.utsc')
- `.pem`: 4x Excluded (Unsupported Extension: '.pem'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ps1`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.4 | 35.3 | 35.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.4 | 59.7 | 62.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 26.0 | 9.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 36.5 | 2.6 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 31.9 | 18.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 83.3 | 1.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 81.7 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 82.1 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.8 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.0 | 91.3 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1485 | 173 | 10 | `scapy/modules/ldaphero.py` |
| cleanup | 174 | 51 | 1 | `scapy/automaton.py` |
| guards | 5297 | 282 | 36 | `scapy/utils.py` |
| danger | 3664 | 254 | 24 | `scapy/utils.py` |
| concurrency | 223 | 55 | 2 | `scapy/contrib/diameter.py` |
| connectivity | 12357 | 336 | 77 | `scapy/fields.py` |
| io | 1381 | 120 | 11 | `scapy/layers/inet6.py` |
| crypto | 123 | 42 | 1 | `scapy/layers/ipsec.py` |
| ipc | 85 | 16 | 0 | `scapy/utils.py` |
| time | 121 | 52 | 1 | `scapy/fields.py` |
| serialization | 1 | 1 | 0 | `scapy/data.py` |
| regex | 53 | 29 | 0 | `scapy/asn1/mib.py` |
| events | 303 | 61 | 2 | `scapy/layers/smbserver.py` |
| tests | 26 | 9 | 0 | `scapy/contrib/automotive/gm/gmlan_scanner.py` |
| docs | 3453 | 337 | 24 | `scapy/contrib/scada/iec104/iec104_information_objects.py` |
| debt | 1553 | 187 | 12 | `scapy/layers/inet6.py` |
| mutation | 75409 | 352 | 443 | `scapy/contrib/automotive/bmw/definitions.py` |
| dead_code | 497 | 121 | 4 | `scapy/contrib/automotive/uds_logging.py` |
| credential | 0 | 0 | 0 | - |
| threat | 115 | 32 | 0 | `scapy/contrib/rtps/rtps.py` |
| ml_ai | 6 | 2 | 0 | `scapy/libs/matplot.py` |
| ui | 7 | 2 | 0 | `scapy/tools/UTscapy.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scapy/layers/inet6.py` (Hits: 71)
- `scapy/utils.py` (Hits: 54)
- `scapy/utils6.py` (Hits: 51)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **packet.py** (`scapy/packet.py`) — 246 inbound connections
2. **fields.py** (`scapy/fields.py`) — 211 inbound connections
3. **config.py** (`scapy/config.py`) — 182 inbound connections
4. **compat.py** (`scapy/compat.py`) — 140 inbound connections
5. **error.py** (`scapy/error.py`) — 135 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **utils.py** (`scapy/utils.py`) — 51 outbound dependencies
2. **config.py** (`scapy/config.py`) — 45 outbound dependencies
3. **inet.py** (`scapy/layers/inet.py`) — 39 outbound dependencies
4. **kerberos.py** (`scapy/layers/kerberos.py`) — 37 outbound dependencies
5. **all.py** (`scapy/all.py`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `p0f_impersonate` **(Many-Argument Workhorses)** (@ `scapy/modules/p0f.py`) -> Impact: **287.4** | LOC: 204
- `_run` **(Many-Argument Workhorses)** (@ `scapy/sendrecv.py`) -> Impact: **287.2** | LOC: 219
- `__init__` **(Many-Argument Workhorses)** (@ `scapy/layers/kerberos.py`) -> Impact: **278.6** | LOC: 208
- `p0f_impersonate` **(Many-Argument Workhorses)** (@ `scapy/modules/p0fv2.py`) -> Impact: **276.1** | LOC: 204
- `bind` **(Many-Argument Workhorses)** (@ `scapy/layers/ldap.py`) -> Impact: **200.7** | LOC: 281
- `tcpdump` **(Many-Argument Workhorses)** (@ `scapy/utils.py`) -> Impact: **181.8** | LOC: 269
- `from_cli_arguments` **(Many-Argument Workhorses)** (@ `scapy/layers/spnego.py`) -> Impact: **179.5** | LOC: 182
- `parse_options` **(Many-Argument Workhorses)** (@ `scapy/layers/dns.py`) -> Impact: **179.0** | LOC: 138
- `__init__` **(Many-Argument Workhorses)** (@ `scapy/sendrecv.py`) -> Impact: **150.9** | LOC: 133
- `_bind` **(Many-Argument Workhorses)** (@ `scapy/layers/msrpce/rpcclient.py`) -> Impact: **150.0** | LOC: 207

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `scapy/layers` | 61 | 38711.74 | 39.99% | 28.94% |
| `scapy` | 34 | 24823.6 | 52.95% | 17.2% |
| `test/scapy/layers/tls/pki` | 5 | 20001.0 | 0.0% | 0.0% |
| `scapy/layers/tls` | 18 | 11263.98 | 47.27% | 47.94% |
| `scapy/modules` | 7 | 5782.72 | 50.97% | 39.64% |
| `doc/notebooks/tls/raw_data/pki` | 1 | 5000.0 | 0.0% | 0.0% |
| `scapy/layers/msrpce` | 10 | 3036.96 | 35.35% | 12.38% |
| `scapy/libs` | 7 | 1808.52 | 29.54% | 1.9% |
| `scapy/asn1` | 4 | 1614.5 | 51.57% | 17.72% |
| `scapy/arch/windows` | 3 | 1385.26 | 45.29% | 9.41% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `scapy/contrib/automotive/gm/gmlan_logging.py` -> **100.0%** Exposure
- `scapy/contrib/automotive/uds_logging.py` -> **100.0%** Exposure
- `scapy/contrib/carp.py` -> **100.0%** Exposure
- `scapy/layers/tls/basefields.py` -> **100.0%** Exposure
- `scapy/contrib/opc_da.py` -> **99.9992%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scapy/__init__.py` -> **100.0%** Exposure
- `scapy/ansmachine.py` -> **100.0%** Exposure
- `scapy/arch/bpf/consts.py` -> **100.0%** Exposure
- `scapy/arch/bpf/supersocket.py` -> **100.0%** Exposure
- `scapy/arch/libpcap.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scapy/contrib/automotive/uds_logging.py` -> **43** Orphaned Functions | **0** Duplicates
- `scapy/contrib/dicom.py` -> **10** Orphaned Functions | **31** Duplicates
- `scapy/fields.py` -> **0** Orphaned Functions | **37** Duplicates
- `scapy/layers/inet6.py` -> **0** Orphaned Functions | **36** Duplicates
- `scapy/layers/smb2.py` -> **0** Orphaned Functions | **31** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3308` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `doc/notebooks/tls/raw_data/pki/srv_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/ca_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/cli_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/srv_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/scapy/layers/tls/pki/srv_key_ed25519.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scapy/utils.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.813)
- **Top Global Matches:** file_cluster_12: 7.813, file_cluster_5: 8.886, file_cluster_4: 9.152
- **Magnitude:** 3643.38 | **LOC:** 4186 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **83** in-repo importer(s); it depends on **51**; blast radius 43.893; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (84.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%)
- **Documentation Coverage:** 94.2211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tcpdump` **(Many-Argument Workhorses)** (Impact: 181.8)
  * `hexdiff` **(Many-Argument Workhorses)** (Impact: 112.1)
  * `AutoArgparse` **(Many-Argument Workhorses)** (Impact: 78.6)
  * `do_graph` **(Many-Argument Workhorses)** (Impact: 72.1)
  * `pretty_list` **(Many-Argument Workhorses)** (Impact: 57.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 13 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 490 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 1559
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 585`, `structural_boundaries: 646`, `args: 235`, `func_start: 216`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 82`, `high_risk_execution: 16`, `state_mutation: 579`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 10`
* *Architecture:* `io: 54`, `api: 158`, `concurrency: 6`, `import: 64`
* *Defense:* `safety: 151`, `doc: 106`, `test: 2`, `sync_locks: 3`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 43.893
  * `Choke Point (Betweenness):` 0.073755 | `Ripple Effect (Closeness):` 0.474308
  * `Imports (Out-Degree: 18):` argparse, array, collections, ctypes, decimal, difflib, enum, fcntl...
  * `Imported By (In-Degree: 83):` (Excluded from Brief to save tokens)

### `scapy/layers/kerberos.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.475)
- **Top Global Matches:** file_cluster_4: 4.475, file_cluster_6: 9.16, file_cluster_15: 11.327
- **Magnitude:** 3332.28 | **LOC:** 5679 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **37**; blast radius 1.105; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%)
- **Documentation Coverage:** 72.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 278.6)
  * `GSS_Init_sec_context` **(Many-Argument Workhorses)** (Impact: 118.1)
  * `kpasswd` **(Many-Argument Workhorses)** (Impact: 109.5)
  * `GSS_Accept_sec_context` **(Many-Argument Workhorses)** (Impact: 106.8)
  * `GSS_WrapEx` **(Many-Argument Workhorses)** (Impact: 100.5)
    * *Intent:* """ [MS-KILE] sect 3.4.5.4 - AES: RFC4121 sect 4.2.6.2 and [MS-KILE] sect 3.4.5.4.1 - HMAC-RC4: RFC4...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 365 instances
* *State Mutation (weighted view):* 1503
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 495`, `structural_boundaries: 463`, `args: 117`, `func_start: 96`, `class_start: 114`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 773`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 4`, `duplicate_logic: 10`
* *Architecture:* `io: 8`, `api: 190`, `import: 44`
* *Defense:* `safety: 90`, `doc: 37`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.002082 | `Ripple Effect (Closeness):` 0.039277
  * `Imports (Out-Degree: 26):` collections, cryptography.hazmat.primitives.asymmetric, cryptography.hazmat.primitives.serialization, datetime, enum, os, prompt_toolkit, re...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scapy/fields.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.728)
- **Top Global Matches:** file_cluster_12: 6.728, file_cluster_5: 9.036, file_cluster_15: 9.507
- **Magnitude:** 3264.38 | **LOC:** 4002 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **211** in-repo importer(s); it depends on **27**; blast radius 34.312; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getfield` **(Many-Argument Workhorses)** (Impact: 51.1)
    * *Intent:* # type: (Packet, bytes) -> Tuple[bytes, List[BasePacket]] c = len_pkt = cls = None if self.length_fr...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `_build_config_representation` **(Stateful Encapsulated Methods)** (Impact: 33.3)
    * *Intent:* # type: (Dict[str, Any]) -> None assoc_table = dict() for key in config: value_spec = config[key] va...
  * `getfield` **(Many-Argument Workhorses)** (Impact: 25.8)
  * `any2i` **(Defensive Guards)** (Impact: 23.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 327 instances
* *State Mutation (weighted view):* 1131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 934`, `args: 369`, `func_start: 359`, `class_start: 135`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 477`, `planned_debt: 1`, `fragile_debt: 5`, `duplicate_logic: 37`
* *Architecture:* `io: 8`, `api: 355`, `import: 28`
* *Defense:* `safety: 117`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.312
  * `Choke Point (Betweenness):` 0.028298 | `Ripple Effect (Closeness):` 0.53529
  * `Imports (Out-Degree: 13):` calendar, collections, copy, datetime, enum, inspect, math, scapy.base_classes...
  * `Imported By (In-Degree: 211):` (Excluded from Brief to save tokens)

### `scapy/layers/inet6.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.93)
- **Top Global Matches:** file_cluster_4: 6.93, file_cluster_12: 7.735, file_cluster_15: 8.147
- **Magnitude:** 3248.9 | **LOC:** 4249 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **39** in-repo importer(s); it depends on **25**; blast radius 4.256; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 85.1003% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `answers` **(Defensive Guards)** (Impact: 59.9)
  * `NDP_Attack_NA_Spoofing` **(Many-Argument Workhorses)** (Impact: 50.9)
  * `NDP_Attack_Kill_Default_Router` **(Many-Argument Workhorses)** (Impact: 47.6)
  * `in6_pseudoheader` **(Many-Argument Workhorses)** (Impact: 40.8)
    * *Intent:* # type: (int, IP, int) -> PseudoIPv6 """
  * `hashret` **(Defensive Guards)** (Impact: 39.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 408 instances
* *State Mutation (weighted view):* 1568
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 752`, `args: 240`, `func_start: 179`, `class_start: 135`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 752`, `planned_debt: 23`, `fragile_debt: 18`, `duplicate_logic: 36`
* *Architecture:* `io: 71`, `api: 284`, `import: 26`
* *Defense:* `safety: 75`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.256
  * `Choke Point (Betweenness):` 0.003901 | `Ripple Effect (Closeness):` 0.314216
  * `Imports (Out-Degree: 19):` hashlib, random, scapy.arch, scapy.as_resolvers, scapy.base_classes, scapy.compat, scapy.config, scapy.consts...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `scapy/packet.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.188)
- **Top Global Matches:** file_cluster_4: 8.188, file_cluster_12: 10.27, file_cluster_5: 11.789
- **Magnitude:** 3069.92 | **LOC:** 2687 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **246** in-repo importer(s); it depends on **24**; blast radius 99.956; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.359% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `explore` **(Compute Cores)** (Impact: 82.8)
    * *Intent:* # type: (Optional[str]) -> None """Function used to discover the Scapy layers and protocols. It help...
  * `getlayer` **(Many-Argument Workhorses)** (Impact: 77.0)
  * `canvas_dump` **(Many-Argument Workhorses)** (Impact: 76.7)
    * *Intent:* # type: (int, int) -> pyx.canvas.canvas if PYX == 0: raise ImportError("PyX and its dependencies mus...
  * `_show_or_dump` **(Many-Argument Workhorses)** (Impact: 67.9)
  * `sprintf` **(Many-Argument Workhorses)** (Impact: 60.0)
    * *Intent:* # type: (str, int) -> str """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 444 instances
* *State Mutation (weighted view):* 1417
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 547`, `structural_boundaries: 415`, `args: 174`, `func_start: 161`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 529`, `dead_code: 2`, `planned_debt: 7`, `fragile_debt: 1`
* *Architecture:* `api: 138`, `import: 27`
* *Defense:* `safety: 122`, `doc: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 99.956
  * `Choke Point (Betweenness):` 0.033843 | `Ripple Effect (Closeness):` 0.639152
  * `Imports (Out-Degree: 11):` collections, copy, itertools, json, prompt_toolkit, prompt_toolkit.formatted_text, prompt_toolkit.shortcuts.dialogs, pyx...
  * `Imported By (In-Degree: 246):` (Excluded from Brief to save tokens)

### `scapy/layers/inet.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.543)
- **Top Global Matches:** file_cluster_12: 7.543, file_cluster_4: 8.434, file_cluster_15: 10.045
- **Magnitude:** 2598.72 | **LOC:** 2559 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **103** in-repo importer(s); it depends on **39**; blast radius 10.882; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%)
- **Documentation Coverage:** 85.3175% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_graph` **(Many-Argument Workhorses)** (Impact: 115.1)
  * `trace3D_notebook` **(Compute Cores)** (Impact: 53.9)
    * *Intent:* """Same than trace3D, used when ran from Jupyter notebooks"""
  * `traceroute` **(Many-Argument Workhorses)** (Impact: 44.8)
    * *Intent:* """Instant TCP traceroute :param target: hostnames or IP addresses :param dport: TCP destination por...
  * `fragleak` **(Many-Argument Workhorses)** (Impact: 41.7)
  * `i2m` **(Defensive Guards)** (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 370 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 452`, `structural_boundaries: 478`, `args: 171`, `func_start: 135`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 479`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 18`, `api: 155`, `concurrency: 2`, `import: 37`
* *Defense:* `safety: 71`, `doc: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.882
  * `Choke Point (Betweenness):` 0.012854 | `Ripple Effect (Closeness):` 0.348967
  * `Imports (Out-Degree: 21):` cartopy., cartopy.crs, collections, geoip2., geoip2.database, geoip2.errors, hashlib, matplotlib...
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

### `scapy/layers/dcerpc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.478)
- **Top Global Matches:** file_cluster_12: 7.478, file_cluster_15: 8.012, file_cluster_16: 8.599
- **Magnitude:** 2083.42 | **LOC:** 3407 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **23**; blast radius 1.717; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.3%), Connectivity (formerly Api Exposure) (81.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 87.8788% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `in_pkt` **(Many-Argument Workhorses)** (Impact: 82.3)
    * *Intent:* # The PDU header, PDU body, and sec_trailer MUST be passed in the input message, in # this order, to...
  * `out_pkt` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `_up_pkt` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* """ Common function to handle the DCE/RPC session: what interfaces are bind, opnums, etc. """
  * `addfield` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `tcp_reassemble` **(Compute Cores)** (Impact: 20.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 225 instances
* *State Mutation (weighted view):* 956
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 482`, `args: 202`, `func_start: 145`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 506`, `planned_debt: 7`, `fragile_debt: 3`, `duplicate_logic: 21`
* *Architecture:* `api: 196`, `import: 24`
* *Defense:* `safety: 72`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.717
  * `Choke Point (Betweenness):` 0.002191 | `Ripple Effect (Closeness):` 0.041634
  * `Imports (Out-Degree: 14):` collections, enum, functools, importlib, inspect, scapy.base_classes, scapy.compat, scapy.config...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `scapy/layers/tls/handshake.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.651)
- **Top Global Matches:** file_cluster_12: 6.651, file_cluster_15: 6.792, file_cluster_16: 8.538
- **Magnitude:** 1744.34 | **LOC:** 1771 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **22**; blast radius 0.828; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.2%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 87.8049% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `tls_session_update` **(Many-Argument Workhorses)** (Impact: 30.7)
    * *Intent:* """ Either for parsing or building, we store the server_random along with the raw string representin...
  * `post_dissection` **(Compute Cores)** (Impact: 25.6)
  * `tls_session_update` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* """ Either for parsing or building, we store the server_random along with the raw string representin...
  * `post_build` **(Many-Argument Workhorses)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 282 instances
* *State Mutation (weighted view):* 930
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 268`, `args: 129`, `func_start: 84`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 366`, `fragile_debt: 6`, `duplicate_logic: 14`
* *Architecture:* `io: 3`, `api: 109`, `import: 23`
* *Defense:* `safety: 29`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.828
  * `Choke Point (Betweenness):` 0.015099 | `Ripple Effect (Closeness):` 0.183791
  * `Imports (Out-Degree: 17):` cryptography.hazmat.backends, cryptography.hazmat.primitives, math, os, scapy.compat, scapy.config, scapy.error, scapy.fields...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `scapy/sendrecv.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.096)
- **Top Global Matches:** file_cluster_6: 9.096, file_cluster_4: 9.113, file_cluster_12: 14.3
- **Magnitude:** 1660.26 | **LOC:** 1568 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **23**; blast radius 6.314; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.1%), Complexity Load (formerly Cognitive Load) (65.9%)
- **Documentation Coverage:** 97.4026% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_run` **(Many-Argument Workhorses)** (Impact: 287.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 150.9)
  * `__sr_loop` **(Many-Argument Workhorses)** (Impact: 90.1)
    * *Intent:* # SEND/RECV LOOP METHODS
  * `__gen_send` **(Many-Argument Workhorses)** (Impact: 62.8)
  * `bridge_and_sniff` **(Many-Argument Workhorses)** (Impact: 61.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 184 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 178`, `args: 51`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 40`, `high_risk_execution: 1`, `state_mutation: 229`, `planned_debt: 1`
* *Architecture:* `io: 26`, `api: 32`, `concurrency: 1`, `import: 26`
* *Defense:* `safety: 53`, `doc: 31`, `sync_locks: 3`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.314
  * `Choke Point (Betweenness):` 0.001563 | `Ripple Effect (Closeness):` 0.364231
  * `Imports (Out-Degree: 14):` itertools, os, re, scapy.automaton, scapy.base_classes, scapy.compat, scapy.config, scapy.data...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `scapy/modules/ticketer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.447)
- **Top Global Matches:** file_cluster_4: 5.447, file_cluster_16: 8.663, file_cluster_15: 8.731
- **Magnitude:** 1658.2 | **LOC:** 2773 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 0.602; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.7%)
- **Documentation Coverage:** 65.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_build_ticket` **(Many-Argument Workhorses)** (Impact: 91.9)
  * `add_cred` **(Many-Argument Workhorses)** (Impact: 68.3)
  * `edit_ticket` **(Many-Argument Workhorses)** (Impact: 60.0)
    * *Intent:* """ Edit a Kerberos ticket using the GUI """
  * `import_krb` **(Many-Argument Workhorses)** (Impact: 52.9)
    * *Intent:* """ Import the result of krb_[tgs/as]_req or a Ticket into the CCache. :param obj: a KRB_Ticket obje...
  * `show` **(Many-Argument Workhorses)** (Impact: 43.6)
    * *Intent:* """ Show the content of a CCache """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 168 instances
* *State Mutation (weighted view):* 596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 244`, `args: 104`, `func_start: 92`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 260`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `io: 4`, `api: 76`, `import: 25`
* *Defense:* `safety: 30`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.602
  * `Choke Point (Betweenness):` 5e-05 | `Ripple Effect (Closeness):` 0.021912
  * `Imports (Out-Degree: 12):` collections, datetime, enum, platform, prompt_toolkit, random, re, scapy.asn1.asn1...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scapy/automaton.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.118)
- **Top Global Matches:** file_cluster_12: 8.118, file_cluster_5: 9.435, file_cluster_7: 9.447
- **Magnitude:** 1609.82 | **LOC:** 1630 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **26**; blast radius 3.889; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__new__` **(Many-Argument Workhorses)** (Impact: 58.1)
    * *Intent:* # type: (str, Tuple[Any], Dict[str, Any]) -> Type[Automaton] cls = super(Automaton_metaclass, cls)._...
  * `spawn` **(Many-Argument Workhorses)** (Impact: 50.1)
  * `_do_iter` **(Compute Cores)** (Impact: 49.2)
    * *Intent:* # type: () -> Iterator[Union[Automaton.AutomatonException, Automaton.AutomatonStopped, ATMT.NewState...
  * `_do_control` **(Many-Argument Workhorses)** (Impact: 48.5)
    * *Intent:* # type: (threading.Event, Any, Any) -> None with self.started: self.threadid = threading.current_thr...
  * `build_graph` **(Compute Cores)** (Impact: 43.0)
    * *Intent:* # type: () -> str s = 'digraph "%s" {\n' % self.__class__.__name__ se = "" # Keep initial nodes at t...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 177 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 715
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 354`, `args: 130`, `func_start: 127`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 361`, `planned_debt: 1`
* *Architecture:* `io: 23`, `api: 101`, `concurrency: 6`, `import: 26`
* *Defense:* `safety: 47`, `doc: 5`, `sync_locks: 4`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.889
  * `Choke Point (Betweenness):` 0.00115 | `Ripple Effect (Closeness):` 0.325122
  * `Imports (Out-Degree: 11):` collections, ctypes, inspect, itertools, logging, os, random, scapy.arch...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `scapy/layers/dns.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.467)
- **Top Global Matches:** file_cluster_4: 5.467, file_cluster_12: 10.321, file_cluster_15: 10.983
- **Magnitude:** 1590.84 | **LOC:** 2029 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **28**; blast radius 0.981; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.5%), Complexity Load (formerly Cognitive Load) (72.5%)
- **Documentation Coverage:** 71.7742% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_options` **(Many-Argument Workhorses)** (Impact: 179.0)
  * `make_reply` **(Many-Argument Workhorses)** (Impact: 121.8)
    * *Intent:* # Build reply from the request resp = req.copy() if Ether in req: if self.mDNS: resp[Ether].src, res...
  * `dns_resolve` **(Many-Argument Workhorses)** (Impact: 69.9)
    * *Intent:* """ Perform a simple DNS resolution using conf.nameservers with caching :param qname: the name to qu...
  * `dns_get_str` **(Many-Argument Workhorses)** (Impact: 35.8)
    * *Intent:* """This function decompresses a string s, starting from the given pointer. :param s: the string to d...
  * `dns_compress` **(Defensive Guards)** (Impact: 31.0)
    * *Intent:* """This function compresses a DNS packet according to compression rules. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 181 instances
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 326`, `args: 115`, `func_start: 63`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 276`, `duplicate_logic: 7`
* *Architecture:* `io: 16`, `api: 95`, `import: 32`
* *Defense:* `safety: 54`, `doc: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.981
  * `Choke Point (Betweenness):` 0.000634 | `Ripple Effect (Closeness):` 0.03622
  * `Imports (Out-Degree: 20):` abc, collections, itertools, math, operator, scapy.ansmachine, scapy.arch, scapy.base_classes...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `scapy/layers/ldap.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 4.844)
- **Top Global Matches:** file_cluster_6: 4.844, file_cluster_4: 10.305, file_cluster_8: 14.274
- **Magnitude:** 1590.76 | **LOC:** 2506 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **31**; blast radius 0.706; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 87.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bind` **(Many-Argument Workhorses)** (Impact: 200.7)
  * `search` **(Many-Argument Workhorses)** (Impact: 89.5)
  * `dclocator` **(Many-Argument Workhorses)** (Impact: 87.3)
  * `from_rfc2254_string` **(Compute Cores)** (Impact: 79.0)
    * *Intent:* """ Convert a RFC-2254 filter to LDAP_Filter """
  * `connect` **(Many-Argument Workhorses)** (Impact: 52.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 147 instances
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 264`, `args: 37`, `func_start: 35`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 344`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 13`, `api: 102`, `import: 34`
* *Defense:* `safety: 40`, `doc: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.706
  * `Choke Point (Betweenness):` 0.000474 | `Ripple Effect (Closeness):` 0.028912
  * `Imports (Out-Degree: 23):` collections, re, scapy.ansmachine, scapy.arch, scapy.asn1.asn1, scapy.asn1.ber, scapy.asn1fields, scapy.asn1packet...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scapy/layers/tls/cert.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.06)
- **Top Global Matches:** file_cluster_12: 6.06, file_cluster_15: 8.253, file_cluster_16: 8.934
- **Magnitude:** 1575.04 | **LOC:** 1923 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **26**; blast radius 1.17; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%)
- **Documentation Coverage:** 69.0141% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `fill_and_store` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `sign` **(Many-Argument Workhorses)** (Impact: 36.5)
  * `fill_and_store` **(Stateful Encapsulated Methods)** (Impact: 28.4)
  * `import_from_asn1pkt` **(Many-Argument Workhorses)** (Impact: 23.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 210 instances
* *State Mutation (weighted view):* 753
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 308`, `args: 110`, `func_start: 110`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 333`, `planned_debt: 4`, `duplicate_logic: 21`
* *Architecture:* `io: 8`, `api: 102`, `import: 22`
* *Defense:* `safety: 52`, `doc: 59`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.17
  * `Choke Point (Betweenness):` 0.000609 | `Ripple Effect (Closeness):` 0.162034
  * `Imports (Out-Degree: 9):` CRL, CSR, base64, certificate, cryptography.exceptions, cryptography.hazmat.backends, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `scapy/layers/smb2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.012)
- **Top Global Matches:** file_cluster_4: 6.012, file_cluster_15: 8.204, file_cluster_16: 9.446
- **Magnitude:** 1540.46 | **LOC:** 4129 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 0.803; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.0%), Debt Markers (formerly Tech Debt) (75.1%)
- **Documentation Coverage:** 91.8129% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `guess_payload_class` **(Compute Cores)** (Impact: 64.0)
  * `out_pkt` **(Many-Argument Workhorses)** (Impact: 50.3)
    * *Intent:* """ Outgoing SMB packet :param pkt: the packet to send :param Compound: if True, will be stack to be...
  * `_calc_signature` **(Many-Argument Workhorses)** (Impact: 47.5)
  * `recv` **(Compute Cores)** (Impact: 32.1)
    * *Intent:* # note: normal StreamSocket takes care of NBTSession / DirectTCP fragments. # this takes care of spl...
  * `computeSMBSessionKeys` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* # SMB crypto functions """ Compute the SigningKey and EncryptionKey (for SMB 3+) """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 134 instances
* *State Mutation (weighted view):* 702
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 374`, `args: 165`, `func_start: 84`, `class_start: 114`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 434`, `planned_debt: 3`, `duplicate_logic: 31`
* *Architecture:* `io: 3`, `api: 188`, `import: 26`
* *Defense:* `safety: 12`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.803
  * `Choke Point (Betweenness):` 0.000203 | `Ripple Effect (Closeness):` 0.02313
  * `Imports (Out-Degree: 13):` collections, cryptography.hazmat.primitives, cryptography.hazmat.primitives.ciphers, cryptography.hazmat.primitives.ciphers.aead, functools, hashlib, os, scapy.automaton...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `scapy/volatile.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.884)
- **Top Global Matches:** file_cluster_12: 6.884, file_cluster_16: 9.014, file_cluster_5: 9.546
- **Magnitude:** 1512.5 | **LOC:** 1425 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **49** in-repo importer(s); it depends on **12**; blast radius 18.583; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.6%), Guard Balance (formerly Safety Score) (82.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 114.3)
  * `_fix` **(Compute Cores)** (Impact: 48.1)
    * *Intent:* # type: () -> str stack = [None] index = [] # Give up on typing this current = stack # type: Any i =...
  * `stack_fix` **(Compute Cores)** (Impact: 27.8)
    * *Intent:* # type: (List[Any], List[Any]) -> str r = "" mul = 1 for e in lst: if isinstance(e, list): if mul !=...
  * `__init__` **(Type Conversions)** (Impact: 20.4)
    * *Intent:* # type: (str) -> None super(RandIP6, self).__init__() self.tmpl = ip6template self.sp = [] # type: L...
  * `_fix` **(Stateful Encapsulated Methods)** (Impact: 19.7)
    * *Intent:* # type: () -> str nbm = self.multi ip = [] # type: List[str] for i, n in enumerate(self.sp): if n ==...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 228 instances
* *State Mutation (weighted view):* 730
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 338`, `args: 144`, `func_start: 144`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 274`, `duplicate_logic: 9`
* *Architecture:* `api: 85`, `import: 12`
* *Defense:* `safety: 17`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.583
  * `Choke Point (Betweenness):` 0.001369 | `Ripple Effect (Closeness):` 0.424593
  * `Imports (Out-Degree: 3):` copy, math, random, re, scapy.base_classes, scapy.compat, scapy.utils, string...
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `scapy/layers/ntlm.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.995)
- **Top Global Matches:** file_cluster_4: 6.995, file_cluster_12: 7.216, file_cluster_15: 7.283
- **Magnitude:** 1503.26 | **LOC:** 2314 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **26**; blast radius 1.514; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%), Connectivity (formerly Api Exposure) (71.0%)
- **Documentation Coverage:** 74.8031% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GSS_Init_sec_context` **(Many-Argument Workhorses)** (Impact: 124.5)
  * `GSS_Accept_sec_context` **(Many-Argument Workhorses)** (Impact: 100.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 63.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 39.4)
  * `GSS_Passive` **(Many-Argument Workhorses)** (Impact: 30.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 636
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 256`, `args: 87`, `func_start: 67`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 284`, `duplicate_logic: 3`
* *Architecture:* `io: 5`, `api: 73`, `import: 30`
* *Defense:* `safety: 58`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.514
  * `Choke Point (Betweenness):` 0.001977 | `Ripple Effect (Closeness):` 0.043368
  * `Imports (Out-Degree: 18):` copy, cryptography.hazmat.decrepit.ciphers, cryptography.hazmat.primitives.ciphers, enum, os, scapy.asn1.asn1, scapy.asn1.mib, scapy.asn1fields...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `scapy/layers/smbserver.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.359)
- **Top Global Matches:** file_cluster_4: 5.359, file_cluster_6: 10.497, file_cluster_12: 10.595
- **Magnitude:** 1500.78 | **LOC:** 1893 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 0.613; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%), Guard Balance (formerly Safety Score) (72.5%)
- **Documentation Coverage:** 74.8148% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on_negotiate` **(Many-Argument Workhorses)** (Impact: 91.6)
  * `on_setup_andx_request` **(Many-Argument Workhorses)** (Impact: 58.9)
  * `send_query_info_response` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `lookup_file` **(Many-Argument Workhorses)** (Impact: 49.8)
    * *Intent:* """ Lookup the file and build it's SMB2_FILEID """
  * `send_create_file_response` **(Many-Argument Workhorses)** (Impact: 45.4)
    * *Intent:* """ Handle CreateFile request See [MS-SMB2] 3.3.5.9 () """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 209 instances
* *State Mutation (weighted view):* 711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 185`, `args: 71`, `func_start: 70`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 293`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 69`, `import: 22`
* *Defense:* `safety: 19`, `doc: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.613
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.002475
  * `Imports (Out-Degree: 16):` hashlib, pathlib, scapy.arch, scapy.automaton, scapy.config, scapy.consts, scapy.error, scapy.layers.dcerpc...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scapy/layers/smbclient.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.968)
- **Top Global Matches:** file_cluster_4: 6.968, file_cluster_12: 7.432, file_cluster_15: 8.62
- **Magnitude:** 1466.66 | **LOC:** 1886 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 0.661; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.1%)
- **Documentation Coverage:** 44.7674% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 87.1)
  * `create_request` **(Many-Argument Workhorses)** (Impact: 63.9)
  * `receive_session_setup_response` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `receive_negotiate_response` **(Many-Argument Workhorses)** (Impact: 34.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* # Various SMB client arguments self.EXTENDED_SECURITY = kwargs.pop("EXTENDED_SECURITY", True) self.U...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 182 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 241`, `args: 98`, `func_start: 92`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 237`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 28`, `api: 84`, `concurrency: 2`, `import: 23`
* *Defense:* `safety: 12`, `doc: 57`, `sync_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.661
  * `Choke Point (Betweenness):` 0.00022 | `Ripple Effect (Closeness):` 0.021684
  * `Imports (Out-Degree: 15):` io, os, pathlib, scapy.automaton, scapy.config, scapy.error, scapy.fields, scapy.layers.dcerpc...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scapy/modules/p0f.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.544)
- **Top Global Matches:** file_cluster_6: 8.544, file_cluster_8: 9.506, file_cluster_4: 16.495
- **Magnitude:** 1463.8 | **LOC:** 961 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.551; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.3%)
- **Documentation Coverage:** 44.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `p0f_impersonate` **(Many-Argument Workhorses)** (Impact: 287.4)
  * `tcp_find_match` **(Many-Argument Workhorses)** (Impact: 87.8)
    * *Intent:* """ Finds the best match for the given signature and direction. If a match is found, returns a tuple...
  * `from_packet` **(Many-Argument Workhorses)** (Impact: 87.4)
    * *Intent:* """ Receives a TCP packet (assuming it's valid), and returns a TCP_Signature object """
  * `http_find_match` **(Many-Argument Workhorses)** (Impact: 51.2)
    * *Intent:* """ Finds the best match for the given signature and direction. If a match is found, returns a tuple...
  * `from_raw_sig` **(Type Conversions)** (Impact: 34.5)
    * *Intent:* """ Parses a TCP sig line and returns a tuple consisting of a TCP_Signature object and bad_ttl as bo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 204 instances
* *State Mutation (weighted view):* 655
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 116`, `args: 30`, `func_start: 30`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 247`, `fragile_debt: 4`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 28`, `import: 12`
* *Defense:* `safety: 8`, `doc: 18`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` random, re, scapy.compat, scapy.config, scapy.data, scapy.error, scapy.layers.http, scapy.layers.inet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `scapy/contrib/automotive/autosar/secoc_pdu.py` (PYTHON) | Magnitude: 0.47 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 33, core_var_decl: 16, design_snake_case: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `scapy/layers/tpm.py` (PYTHON) | Magnitude: 94.86 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 562, core_var_decl: 85, design_snake_case: 77, structural_boundaries: 51
- `scapy/contrib/send.py` (PYTHON) | Magnitude: 0.23 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 39, core_var_decl: 24, design_snake_case: 24, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `.github/workflows/unittests.yml` (YAML) | Magnitude: 34.68 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 18, func_start: 17, import: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scapy/libs/test_pyx.py` (PYTHON) | Magnitude: 15.0 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, core_var_decl: 6, branch: 5
- `scapy/contrib/lldp.py` (PYTHON) | Magnitude: 4.69 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 847, core_var_decl: 186, structural_boundaries: 139, state_mutation: 139
- `scapy/contrib/cansocket_native.py` (PYTHON) | Magnitude: 1.24 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 32, state_mutation: 31, core_var_decl: 25
- `scapy/contrib/automotive/uds_ecu_states.py` (PYTHON) | Magnitude: 0.75 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 17, state_mutation: 13, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `scapy/asn1packet.py` (PYTHON) | Magnitude: 24.76 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 17, safety_bypasses: 6, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `scapy/contrib/nrf_sniffer.py` (PYTHON) | Magnitude: 0.48 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 31, core_var_decl: 14, design_snake_case: 14
- `scapy/layers/radius.py` (PYTHON) | Magnitude: 643.14 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1132, core_var_decl: 222, state_mutation: 195, design_snake_case: 177
- `scapy/contrib/nlm.py` (PYTHON) | Magnitude: 0.82 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 149, core_var_decl: 64, design_snake_case: 64, state_mutation: 40
- `scapy/contrib/ife.py` (PYTHON) | Magnitude: 0.27 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 37, core_var_decl: 29, structural_boundaries: 24, state_mutation: 20
- `scapy/contrib/nfs.py` (PYTHON) | Magnitude: 2.28 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 708, core_var_decl: 177, design_snake_case: 177, args: 123

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `scapy/contrib/isotp/__init__.py` (PYTHON) | Magnitude: 0.35 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 17, import: 9, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scapy/layers/netflow.py` (PYTHON) | Magnitude: 571.76 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1444, core_var_decl: 410, design_snake_case: 403, state_mutation: 124
- `scapy/layers/smb.py` (PYTHON) | Magnitude: 375.48 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 896, core_var_decl: 158, structural_boundaries: 143, design_snake_case: 121

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `scapy/sendrecv.py` (PYTHON) | Magnitude: 1660.26 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1003, core_var_decl: 289, design_snake_case: 271, branch: 264

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `scapy/cbor/cbor.py` (PYTHON) | Magnitude: 364.66 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 251, structural_boundaries: 112, state_mutation: 71, core_var_decl: 70
- `scapy/contrib/automotive/obd/obd.py` (PYTHON) | Magnitude: 0.39 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 32, core_var_decl: 22, design_snake_case: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `scapy/contrib/mpls.py` (PYTHON) | Magnitude: 0.43 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 27, core_var_decl: 17, design_snake_case: 17

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `scapy/layers/msrpce/rpcclient.py` -> Churn: **100.0%** | Cog Load: 67.7707% | Debt: 0.0%
- `scapy/layers/dcerpc.py` -> Churn: **95.27%** | Cog Load: 70.222% | Debt: 79.4435%
- `scapy/layers/windows/registry.py` -> Churn: **90.28%** | Cog Load: 36.3454% | Debt: 67.0461%
- `scapy/layers/smbclient.py` -> Churn: **87.86%** | Cog Load: 52.4451% | Debt: 9.5855%
- `scapy/layers/kerberos.py` -> Churn: **84.38%** | Cog Load: 76.7494% | Debt: 21.2615%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scapy/utils.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 3643.38
- `scapy/layers/tls/handshake.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 1744.34
- `scapy/sendrecv.py` -> **schaap** (100.0% isolated ownership) | Magnitude: 1660.26
- `scapy/layers/tls/cert.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 1575.04
- `scapy/layers/ipsec.py` -> **Gabriel** (100.0% isolated ownership) | Magnitude: 1197.98

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `scapy/utils.py` -> **Severity: 7.375** (Bridge: 0.0738 * Flux: 100.0%)
- `scapy/layers/tls/session.py` -> **Severity: 5.86** (Bridge: 0.0586 * Flux: 100.0%)
- `scapy/config.py` -> **Severity: 5.265** (Bridge: 0.0527 * Flux: 100.0%)
- `scapy/packet.py` -> **Severity: 3.384** (Bridge: 0.0338 * Flux: 100.0%)
- `scapy/layers/tls/record.py` -> **Severity: 2.863** (Bridge: 0.0286 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scapy/packet.py` -> **Severity: 51.879** (Embedded: 0.6392 * Error Risk: 81.1681%)
- `scapy/config.py` -> **Severity: 41.919** (Embedded: 0.5667 * Error Risk: 73.975%)
- `scapy/error.py` -> **Severity: 38.963** (Embedded: 0.5241 * Error Risk: 74.3483%)
- `scapy/fields.py` -> **Severity: 37.823** (Embedded: 0.5353 * Error Risk: 70.6592%)
- `scapy/utils.py` -> **Severity: 35.749** (Embedded: 0.4743 * Error Risk: 75.3707%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scapy/packet.py` -> **Severity: 9931.528** (Blast Radius: 99.956 * Doc Risk: 99.359%)
- `scapy/config.py` -> **Severity: 7887.652** (Blast Radius: 82.096 * Doc Risk: 96.0784%)
- `scapy/compat.py` -> **Severity: 6588.8** (Blast Radius: 65.888 * Doc Risk: 100.0%)
- `scapy/error.py` -> **Severity: 5906.6** (Blast Radius: 59.066 * Doc Risk: 100.0%)
- `scapy/utils.py` -> **Severity: 4135.647** (Blast Radius: 43.893 * Doc Risk: 94.2211%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 416 literal sites + 2 sites through wrappers = 418
- **`panics_and_aborts`:** 1433 literal sites + 25 sites through wrappers = 1458

- `atol` (function, panics_and_aborts, primitive): 13 call sites in 7 files -- `scapy/utils.py`
- `_get_hash` (function, panics_and_aborts, primitive): 12 call sites in 3 files -- `scapy/layers/tls/crypto/pkcs1.py`
- `run_scan` (function, debug_prints, primitive): 1 call sites in 1 files -- `scapy/tools/automotive/obdscanner.py`
- `usage` (function, debug_prints, primitive): 1 call sites in 1 files -- `scapy/tools/check_asdis.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 23479 call pairs -- scoped 47.1%, unique 0.0%, ambiguous 13.3%, external 39.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 23466 | 47.1% | 0.0% | 13.3% | 39.6% |
| shell | 13 | 7.7% | 0.0% | 0.0% | 92.3% |

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
