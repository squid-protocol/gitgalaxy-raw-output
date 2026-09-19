# ARCHITECTURAL_BRIEF: rsa
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 15 analyzed artifact(s), 1085 LOC.
- **Load-bearing artifact:** `rsa-4.9.1/rsa/key.py` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `rsa-4.9.1/rsa/key.py` -- pulls in 14 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `rsa-4.9.1/rsa/key.py` at magnitude 337.62 (structural weight, not risk).
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
| Total Artifacts | 20 |
| Analyzed Artifacts (Scanned) | 15 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 1085 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 75.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3044 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5972 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5588 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 13 | 1085 | 86.7% |
| MARKDOWN | 2 | 0 | 13.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 40%, Data / Markup / Trivial 13%, Declarative / Non-Code 13%, Large Core Modules (2) 13%, Compute Cores Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 13 | 86.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 13.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 101 LOC)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 48.8 | 27.8 | 34.2 | 22.8 |
| Guard Balance (formerly Error & Exception Exposure) | 55.1 | 98.2 | 81.4 | 88.1 | 79.5 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 96.6 | 29.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 14.5 | 2.5 | 2.3 |
| Connectivity (formerly API Exposure) | 3.0 | 51.3 | 27.2 | 32.9 | 23.3 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 60.5 | 8.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 16.8 | 100.0 | 85.9 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 53.8 | 18.7 | 14.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 14.7 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5 | 2 | 1 | `rsa-4.9.1/rsa/key.py` |
| cleanup | 2 | 1 | 0 | `rsa-4.9.1/rsa/parallel.py` |
| guards | 58 | 9 | 12 | `rsa-4.9.1/rsa/key.py` |
| danger | 38 | 7 | 10 | `rsa-4.9.1/rsa/key.py` |
| concurrency | 9 | 4 | 2 | `rsa-4.9.1/rsa/key.py` |
| connectivity | 80 | 13 | 15 | `rsa-4.9.1/rsa/key.py` |
| io | 33 | 4 | 8 | `rsa-4.9.1/rsa/cli.py` |
| crypto | 2 | 1 | 0 | `rsa-4.9.1/rsa/pkcs1.py` |
| ipc | 2 | 1 | 0 | `rsa-4.9.1/rsa/parallel.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 1 | 1 | 0 | `rsa-4.9.1/rsa/parallel.py` |
| tests | 0 | 0 | 0 | - |
| docs | 106 | 13 | 17 | `rsa-4.9.1/rsa/key.py` |
| debt | 38 | 7 | 11 | `rsa-4.9.1/rsa/cli.py` |
| mutation | 543 | 13 | 127 | `rsa-4.9.1/rsa/cli.py` |
| dead_code | 6 | 3 | 2 | `rsa-4.9.1/rsa/cli.py` |
| credential | 3 | 2 | 1 | `rsa-4.9.1/rsa/pem.py` |
| threat | 17 | 3 | 4 | `rsa-4.9.1/rsa/key.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.6667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `rsa-4.9.1/rsa/cli.py` (Hits: 21)
- `rsa-4.9.1/rsa/util.py` (Hits: 8)
- `rsa-4.9.1/rsa/pkcs1.py` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **key.py** (`rsa-4.9.1/rsa/key.py`) — 3 inbound connections
2. **randnum.py** (`rsa-4.9.1/rsa/randnum.py`) — 3 inbound connections
3. **common.py** (`rsa-4.9.1/rsa/common.py`) — 2 inbound connections
4. **pkcs1.py** (`rsa-4.9.1/rsa/pkcs1.py`) — 2 inbound connections
5. **prime.py** (`rsa-4.9.1/rsa/prime.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **key.py** (`rsa-4.9.1/rsa/key.py`) — 14 outbound dependencies
2. **pkcs1.py** (`rsa-4.9.1/rsa/pkcs1.py`) — 8 outbound dependencies
3. **cli.py** (`rsa-4.9.1/rsa/cli.py`) — 7 outbound dependencies
4. **parallel.py** (`rsa-4.9.1/rsa/parallel.py`) — 6 outbound dependencies
5. **prime.py** (`rsa-4.9.1/rsa/prime.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_pem_lines` **(Stateful Encapsulated Methods)** (@ `rsa-4.9.1/rsa/pem.py`) -> Impact: **24.1** | LOC: 43
  * *Intent:* """Generator over PEM lines between pem_start and pem_end."""
- `miller_rabin_primality_testing` **(Compute Cores)** (@ `rsa-4.9.1/rsa/prime.py`) -> Impact: **19.9** | LOC: 51
  * *Intent:* """Calculates whether n is composite (which is always correct) or prime (which theoretically is incorrect with error probability 4**-k), by applying M...
- `__eq__` **(Defensive Guards)** (@ `rsa-4.9.1/rsa/key.py`) -> Impact: **18.2** | LOC: 17
- `find_p_q` **(Many-Argument Workhorses)** (@ `rsa-4.9.1/rsa/key.py`) -> Impact: **15.9** | LOC: 78
- `newkeys` **(Many-Argument Workhorses)** (@ `rsa-4.9.1/rsa/key.py`) -> Impact: **13.9** | LOC: 54
- `keygen` **(I/O & Config Routines)** (@ `rsa-4.9.1/rsa/cli.py`) -> Impact: **13.2** | LOC: 65
  * *Intent:* """Key generator."""
- `private_to_public` **(I/O & Config Routines)** (@ `rsa-4.9.1/rsa/util.py`) -> Impact: **11.8** | LOC: 75
  * *Intent:* """Reads a private key and outputs the corresponding public key."""
- `compute_hash` **(Defensive Guards)** (@ `rsa-4.9.1/rsa/pkcs1.py`) -> Impact: **11.7** | LOC: 26
  * *Intent:* """Returns the message digest. :param message: the signed message. Can be an 8-bit string or a file-like object. If ``message`` has a ``read()`` metho...
- `_pad_for_encryption` **(Stateful Encapsulated Methods)** (@ `rsa-4.9.1/rsa/pkcs1.py`) -> Impact: **10.8** | LOC: 43
- `_load_pkcs1_der` **(Many-Argument Workhorses)** (@ `rsa-4.9.1/rsa/key.py`) -> Impact: **9.8** | LOC: 57
  * *Intent:* """Loads a key in PKCS#1 DER format. :param keyfile: contents of a DER-encoded file that contains the private key. :type keyfile: bytes :return: a Pri...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `rsa-4.9.1/rsa` | 13 | 1161.1 | 27.77% | 29.05% |
| `rsa-4.9.1` | 2 | 7.2 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `rsa-4.9.1/rsa/key.py` -> **96.5813%** Exposure
- `rsa-4.9.1/rsa/transform.py` -> **92.4142%** Exposure
- `rsa-4.9.1/rsa/asn1.py` -> **81.7574%** Exposure
- `rsa-4.9.1/rsa/cli.py` -> **59.8339%** Exposure
- `rsa-4.9.1/rsa/util.py` -> **47.0273%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `rsa-4.9.1/rsa/cli.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/common.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/pem.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/pkcs1.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/prime.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `rsa-4.9.1/rsa/key.py` -> **0** Orphaned Functions | **4** Duplicates
- `rsa-4.9.1/rsa/cli.py` -> **3** Orphaned Functions | **0** Duplicates
- `rsa-4.9.1/rsa/transform.py` -> **2** Orphaned Functions | **0** Duplicates
- `rsa-4.9.1/rsa/util.py` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `rsa-4.9.1/rsa/pem.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/key.py` -> **91.6126%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `54` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `rsa-4.9.1/rsa/key.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 337.62 | **LOC:** 859 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 121.45; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.6%), Credential Material (formerly Secrets Risk) (91.6%), Guard Balance (formerly Safety Score) (88.1%)
- **Documentation Coverage:** 38.0952% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__eq__` **(Defensive Guards)** (Impact: 18.2)
  * `find_p_q` **(Many-Argument Workhorses)** (Impact: 15.9)
  * `newkeys` **(Many-Argument Workhorses)** (Impact: 13.9)
  * `_load_pkcs1_der` **(Many-Argument Workhorses)** (Impact: 9.8)
    * *Intent:* """Loads a key in PKCS#1 DER format. :param keyfile: contents of a DER-encoded file that contains th...
  * `calculate_keys_custom_exponent` **(Defensive Guards)** (Impact: 9.6)
    * *Intent:* """Calculates an encryption and a decryption key given p, q and an exponent, and returns them as a t...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 135`, `args: 46`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 70`, `planned_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 20`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 11`, `doc: 36`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 121.45
  * `Choke Point (Betweenness):` 0.098901 | `Ripple Effect (Closeness):` 0.214286
  * `Imports (Out-Degree: 6):` base64, doctest, pyasn1.codec.der, pyasn1.type, rsa, rsa.asn1, rsa.common, rsa.core...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/pkcs1.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 204.08 | **LOC:** 486 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 83.216; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compute_hash` **(Defensive Guards)** (Impact: 11.7)
    * *Intent:* """Returns the message digest. :param message: the signed message. Can be an 8-bit string or a file-...
  * `_pad_for_encryption` **(Stateful Encapsulated Methods)** (Impact: 10.8)
  * `decrypt` **(Many-Argument Workhorses)** (Impact: 8.7)
  * `_pad_for_signing` **(Stateful Encapsulated Methods)** (Impact: 8.5)
  * `yield_fixedblocks` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* """Generator, yields each block of ``blocksize`` bytes in the input file. :param infile: file to rea...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 38`, `args: 11`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 56`
* *Architecture:* `io: 2`, `api: 12`, `import: 7`
* *Defense:* `safety: 5`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 83.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142857
  * `Imports (Out-Degree: 0):` , doctest, hashlib, hmac, os, rsa, sys, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/cli.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 170.44 | **LOC:** 322 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 44.981; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.9%), Debt Markers (formerly Tech Debt) (59.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 53.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keygen` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* """Key generator."""
  * `write_outfile` **(Generic / Templated Code)** (Impact: 6.5)
    * *Intent:* """Write the output file"""
  * `parse_cli` **(Generic / Templated Code)** (Impact: 5.6)
    * *Intent:* """Parse the CLI options :returns: (cli_opts, cli_args) """
  * `perform_operation` **(Defensive Guards)** (Impact: 5.0)
  * `read_infile` **(Generic / Templated Code)** (Impact: 4.0)
    * *Intent:* """Read the input file"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 62`, `args: 12`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 61`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 21`, `api: 15`, `import: 7`
* *Defense:* `safety: 12`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` abc, optparse, rsa, rsa.key, rsa.pkcs1, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/common.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 92.02 | **LOC:** 185 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 96.741; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.9%), Connectivity (formerly Api Exposure) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extended_gcd` **(Generic / Templated Code)** (Impact: 8.0)
    * *Intent:* """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb"""
  * `__init__` **(Generic / Templated Code)** (Impact: 7.6)
  * `crt` **(Compute Cores)** (Impact: 6.8)
    * *Intent:* """Chinese Remainder Theorem. Calculates x such that x = a[i] (mod m[i]) for each i. :param a_values...
  * `ceil_div` **(Generic / Templated Code)** (Impact: 4.6)
    * *Intent:* """ Returns the ceiling function of a division between `num` and `div`. Usage:: >>> ceil_div(100, 7)...
  * `inverse` **(Generic / Templated Code)** (Impact: 4.2)
    * *Intent:* """Returns the inverse of x % n under multiplication, a.k.a x^-1 (mod n) >>> inverse(7, 4) 3 >>> (in...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 20`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 2`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 96.741
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.257143
  * `Imports (Out-Degree: 0):` doctest, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/pem.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 90.64 | **LOC:** 135 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 62.187; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Credential Material (formerly Secrets Risk) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_pem_lines` **(Stateful Encapsulated Methods)** (Impact: 24.1)
    * *Intent:* """Generator over PEM lines between pem_start and pem_end."""
  * `load_pem` **(Defensive Guards)** (Impact: 6.4)
    * *Intent:* """Loads a PEM file. :param contents: the contents of the file to interpret :param pem_marker: the m...
  * `save_pem` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* """Saves a PEM file. :param contents: the contents to encode in PEM format :param pem_marker: the ma...
  * `_markers` **(Stateful Encapsulated Methods)** (Impact: 3.4)
    * *Intent:* """ Returns the start and end PEM markers, as bytes. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 2`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 0):` base64, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/prime.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 80.18 | **LOC:** 199 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 81.304; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (47.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `miller_rabin_primality_testing` **(Compute Cores)** (Impact: 19.9)
    * *Intent:* """Calculates whether n is composite (which is always correct) or prime (which theoretically is inco...
  * `get_primality_testing_rounds` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* """Returns minimum number of rounds for Miller-Rabing primality testing, based on number bitsize. Ac...
  * `is_prime` **(Compute Cores)** (Impact: 5.4)
    * *Intent:* """Returns True if the number is prime, and False otherwise. >>> is_prime(2) True >>> is_prime(42) F...
  * `getprime` **(Defensive Guards)** (Impact: 5.4)
    * *Intent:* """Returns a prime number that can be stored in 'nbits' bits. >>> p = getprime(128) >>> is_prime(p-1...
  * `gcd` **(Generic / Templated Code)** (Impact: 4.0)
    * *Intent:* """Returns the greatest common divisor of p and q >>> gcd(48, 180) 12 """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 27`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 1`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 81.304
  * `Choke Point (Betweenness):` 0.005495 | `Ripple Effect (Closeness):` 0.223214
  * `Imports (Out-Degree: 2):` doctest, rsa, rsa.common, rsa.randnum
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/randnum.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 41.7 | **LOC:** 96 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 115.858; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (44.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `randint` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* """Returns a random integer x with 1 <= x <= maxvalue May take a very long time in specific situatio...
  * `read_random_bits` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* """Reads 'nbits' random bits. If nbits isn't a whole number of bytes, an extra byte will be appended...
  * `read_random_int` **(Generic / Templated Code)** (Impact: 2.0)
    * *Intent:* """Reads a random integer of approximately nbits bits."""
  * `read_random_odd_int` **(Generic / Templated Code)** (Impact: 2.0)
    * *Intent:* """Reads a random odd integer of approximately nbits bits. >>> read_random_odd_int(512) & 1 1 """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 2`, `api: 4`, `import: 3`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 115.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.285714
  * `Imports (Out-Degree: 0):` os, rsa, struct
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/parallel.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 31.08 | **LOC:** 97 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 44.981; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (73.0%), Concurrency Surface (formerly Concurrency) (53.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getprime` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* """Returns a prime number that can be stored in 'nbits' bits. Works in multiple threads at the same ...
  * `_find_prime` **(Stateful Encapsulated Methods)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 2`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` doctest, multiprocessing, multiprocessing.connection, rsa, rsa.prime, rsa.randnum
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 30.06 | **LOC:** 98 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 44.981; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (47.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `private_to_public` **(I/O & Config Routines)** (Impact: 11.8)
    * *Intent:* """Reads a private key and outputs the corresponding public key."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 17`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 1`, `import: 3`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` optparse, rsa.key, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 28.64 | **LOC:** 61 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 44.981; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (79.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (23.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` doctest, rsa.key, rsa.pkcs1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/asn1.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 21.38 | **LOC:** 53 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 62.187; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Guard Balance (formerly Safety Score) (63.8%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `class_start: 3`
* *Risk/State:* `state_mutation: 3`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 19.28 | **LOC:** 54 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 62.187; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (39.4%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encrypt_int` **(Generic / Templated Code)** (Impact: 8.7)
    * *Intent:* """Encrypts a message using encryption key 'ekey', working modulo n"""
  * `assert_int` **(Defensive Guards)** (Impact: 3.7)
  * `decrypt_int` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* """Decrypts a cypher text using the decryption key 'dkey', working modulo n"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 1`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/transform.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 13.98 | **LOC:** 73 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 44.981; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (92.4%), Guard Balance (formerly Safety Score) (63.4%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `int2bytes` **(Compute Cores)** (Impact: 6.7)
    * *Intent:* """ Convert an unsigned integer to bytes (big-endian):: Does not preserve leading zeros if you don't...
  * `bytes2int` **(Generic / Templated Code)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` doctest, math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.04 | **LOC:** 252 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.16 | **LOC:** 108 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `rsa-4.9.1/rsa/key.py` -> **Severity: 9.89** (Bridge: 0.0989 * Flux: 99.9998%)
- `rsa-4.9.1/rsa/prime.py` -> **Severity: 0.549** (Bridge: 0.0055 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `rsa-4.9.1/rsa/randnum.py` -> **Severity: 25.333** (Embedded: 0.2857 * Error Risk: 88.6667%)
- `rsa-4.9.1/rsa/common.py` -> **Severity: 24.917** (Embedded: 0.2571 * Error Risk: 96.8995%)
- `rsa-4.9.1/rsa/prime.py` -> **Severity: 19.759** (Embedded: 0.2232 * Error Risk: 88.5224%)
- `rsa-4.9.1/rsa/key.py` -> **Severity: 18.88** (Embedded: 0.2143 * Error Risk: 88.1043%)
- `rsa-4.9.1/rsa/pem.py` -> **Severity: 16.033** (Embedded: 0.1633 * Error Risk: 98.2014%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rsa-4.9.1/rsa/key.py` -> **Severity: 4626.662** (Blast Radius: 121.45 * Doc Risk: 38.0952%)
- `rsa-4.9.1/rsa/cli.py` -> **Severity: 2422.056** (Blast Radius: 44.981 * Doc Risk: 53.8462%)
- `rsa-4.9.1/rsa/transform.py` -> **Severity: 2249.05** (Blast Radius: 44.981 * Doc Risk: 50.0%)
- `rsa-4.9.1/rsa/core.py` -> **Severity: 2072.898** (Blast Radius: 62.187 * Doc Risk: 33.3333%)
- `rsa-4.9.1/rsa/pkcs1.py` -> **Severity: 1664.32** (Blast Radius: 83.216 * Doc Risk: 20.0%)

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
