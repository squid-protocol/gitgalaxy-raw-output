# ARCHITECTURAL_BRIEF: proto-plus
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
- **Scope:** 67 analyzed artifact(s), 4482 LOC.
- **Load-bearing artifact:** `proto_plus-1.27.2/proto/__init__.py` -- 37 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `proto_plus-1.27.2/proto/message.py` -- pulls in 13 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `proto_plus-1.27.2/proto/message.py` at magnitude 572.04 (structural weight, not risk).
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
| Total Artifacts | 72 |
| Analyzed Artifacts (Scanned) | 67 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 4482 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 93.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3718 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3833 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.397 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 66 | 4482 | 98.5% |
| PLAINTEXT | 1 | 0 | 1.5% |

## 4.1 SOURCE ENCODINGS
All 67 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 46%, Declarative / Non-Code 12%, Data / Markup / Trivial 9%, Interface Declarations Files 9%, Parameter Forwarders Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 66 | 98.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 1.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 63.6 | 12.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.5 | 47.3 | 49.8 | 50.7 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 58.4 | 16.4 | 11.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 5.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 72.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 43 | 12 | 2 | `proto_plus-1.27.2/tests/test_message.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 917 | 53 | 31 | `proto_plus-1.27.2/tests/test_message.py` |
| danger | 50 | 18 | 2 | `proto_plus-1.27.2/proto/message.py` |
| concurrency | 5 | 2 | 0 | `proto_plus-1.27.2/tests/test_fields_enum.py` |
| connectivity | 697 | 63 | 20 | `proto_plus-1.27.2/tests/test_message.py` |
| io | 12 | 4 | 0 | `proto_plus-1.27.2/tests/test_modules.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 33 | 4 | 0 | `proto_plus-1.27.2/tests/test_marshal_types_dates.py` |
| serialization | 1 | 1 | 0 | `proto_plus-1.27.2/tests/test_message_pickling.py` |
| regex | 3 | 3 | 0 | `proto_plus-1.27.2/proto/datetime_helpers.py` |
| events | 0 | 0 | 0 | - |
| tests | 319 | 35 | 13 | `proto_plus-1.27.2/tests/test_message.py` |
| docs | 96 | 24 | 3 | `proto_plus-1.27.2/proto/message.py` |
| debt | 12 | 8 | 1 | `proto_plus-1.27.2/proto/marshal/rules/struct.py` |
| mutation | 2643 | 64 | 117 | `proto_plus-1.27.2/tests/test_message.py` |
| dead_code | 257 | 41 | 10 | `proto_plus-1.27.2/tests/test_message.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `proto_plus-1.27.2/tests/test_modules.py` (Hits: 7)
- `proto_plus-1.27.2/tests/test_fields_composite_string_ref.py` (Hits: 2)
- `proto_plus-1.27.2/tests/test_fields_enum.py` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`proto_plus-1.27.2/proto/__init__.py`) — 37 inbound connections
2. **fields.py** (`proto_plus-1.27.2/proto/fields.py`) — 33 inbound connections
3. **marshal.py** (`proto_plus-1.27.2/proto/marshal/marshal.py`) — 10 inbound connections
4. **primitives.py** (`proto_plus-1.27.2/proto/primitives.py`) — 6 inbound connections
5. **__init__.py** (`proto_plus-1.27.2/proto/marshal/__init__.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **message.py** (`proto_plus-1.27.2/proto/message.py`) — 13 outbound dependencies
2. **test_fields_enum.py** (`proto_plus-1.27.2/tests/test_fields_enum.py`) — 9 outbound dependencies
3. **__init__.py** (`proto_plus-1.27.2/proto/__init__.py`) — 7 outbound dependencies
4. **marshal.py** (`proto_plus-1.27.2/proto/marshal/marshal.py`) — 6 outbound dependencies
5. **conftest.py** (`proto_plus-1.27.2/tests/conftest.py`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__new__` **(Many-Argument Workhorses)** (@ `proto_plus-1.27.2/proto/message.py`) -> Impact: **90.2** | LOC: 238
  * *Intent:* # Do not do any special behavior for Message itself. if not bases: return super().__new__(mcls, name, bases, attrs) # Get the essential information ab...
- `__init__` **(Many-Argument Workhorses)** (@ `proto_plus-1.27.2/proto/message.py`) -> Impact: **35.0** | LOC: 73
- `__new__` **(Many-Argument Workhorses)** (@ `proto_plus-1.27.2/proto/enums.py`) -> Impact: **33.4** | LOC: 86
  * *Intent:* # Do not do any special behavior for `proto.Enum` itself. if bases[0] == enum.IntEnum: return super().__new__(mcls, name, bases, attrs) # Get the esse...
- `__setitem__` **(Many-Argument Workhorses)** (@ `proto_plus-1.27.2/proto/marshal/collections/repeated.py`) -> Impact: **32.6** | LOC: 53
  * *Intent:* # The underlying protocol buffer does not define __setitem__, so we # have to implement all the operations on our own. # If ``key`` is an integer, as ...
- `to_proto` **(Many-Argument Workhorses)** (@ `proto_plus-1.27.2/proto/marshal/marshal.py`) -> Impact: **26.9** | LOC: 46
  * *Intent:* # The protos in google/protobuf/struct.proto are exceptional cases, # because they can and should represent themselves as lists and dicts. # These cas...
- `descriptor` **(Stateful Encapsulated Methods)** (@ `proto_plus-1.27.2/proto/fields.py`) -> Impact: **22.0** | LOC: 45
  * *Intent:* """Return the descriptor for the field."""
- `_message_to_map` **(Many-Argument Workhorses)** (@ `proto_plus-1.27.2/proto/message.py`) -> Impact: **21.9** | LOC: 42
- `pytest_runtest_setup` **(Compute Cores)** (@ `proto_plus-1.27.2/tests/conftest.py`) -> Impact: **21.8** | LOC: 69
- `generate_file_pb` **(Many-Argument Workhorses)** (@ `proto_plus-1.27.2/proto/_file_info.py`) -> Impact: **19.2** | LOC: 64
  * *Intent:* """Generate the descriptors for all protos in the file. This method takes the file descriptor attached to the parent message and generates the immutab...
- `to_python` **(Many-Argument Workhorses)** (@ `proto_plus-1.27.2/proto/marshal/rules/struct.py`) -> Impact: **17.7** | LOC: 34
  * *Intent:* """Coerce the given value to the appropriate Python type. Note that both NullValue and absent fields return None. In order to disambiguate between the...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `proto_plus-1.27.2/tests` | 39 | 2166.26 | 6.7% | 0.0% |
| `proto_plus-1.27.2/proto` | 11 | 1240.9 | 30.93% | 10.95% |
| `proto_plus-1.27.2/proto/marshal/rules` | 9 | 283.68 | 14.92% | 49.45% |
| `proto_plus-1.27.2/proto/marshal` | 3 | 191.22 | 19.23% | 4.97% |
| `proto_plus-1.27.2/proto/marshal/collections` | 3 | 173.46 | 18.67% | 34.72% |
| `proto_plus-1.27.2` | 2 | 12.04 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `proto_plus-1.27.2/proto/marshal/rules/stringy_numbers.py` -> **99.9665%** Exposure
- `proto_plus-1.27.2/proto/marshal/rules/struct.py` -> **99.7808%** Exposure
- `proto_plus-1.27.2/proto/_package_info.py` -> **88.0797%** Exposure
- `proto_plus-1.27.2/proto/marshal/rules/bytes.py` -> **81.7574%** Exposure
- `proto_plus-1.27.2/proto/marshal/rules/field_mask.py` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `proto_plus-1.27.2/proto/_file_info.py` -> **100.0%** Exposure
- `proto_plus-1.27.2/proto/datetime_helpers.py` -> **100.0%** Exposure
- `proto_plus-1.27.2/proto/enums.py` -> **100.0%** Exposure
- `proto_plus-1.27.2/proto/fields.py` -> **100.0%** Exposure
- `proto_plus-1.27.2/proto/message.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `proto_plus-1.27.2/tests/test_message.py` -> **26** Orphaned Functions | **0** Duplicates
- `proto_plus-1.27.2/tests/test_datetime_helpers.py` -> **25** Orphaned Functions | **0** Duplicates
- `proto_plus-1.27.2/tests/test_marshal_types_struct.py` -> **24** Orphaned Functions | **0** Duplicates
- `proto_plus-1.27.2/tests/test_fields_enum.py` -> **21** Orphaned Functions | **0** Duplicates
- `proto_plus-1.27.2/tests/test_fields_repeated_composite.py` -> **19** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `171` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `proto_plus-1.27.2/proto/message.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.611)
- **Top Global Matches:** file_cluster_12: 7.611, file_cluster_4: 8.654, file_cluster_5: 8.743
- **Magnitude:** 572.04 | **LOC:** 963 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 21.99; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 44.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__new__` **(Many-Argument Workhorses)** (Impact: 90.2)
    * *Intent:* # Do not do any special behavior for Message itself. if not bases: return super().__new__(mcls, name...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 35.0)
  * `_message_to_map` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `_raise_if_print_fields_values_are_set_and_differ` **(Stateful Encapsulated Methods)** (Impact: 13.3)
  * `copy_from` **(Defensive Guards)** (Impact: 11.4)
    * *Intent:* """Equivalent for protobuf.Message.CopyFrom Args: instance: An instance of this message type other: ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 110`, `args: 32`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 98`, `dead_code: 1`
* *Architecture:* `api: 18`, `import: 18`
* *Defense:* `safety: 21`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.99
  * `Choke Point (Betweenness):` 0.023388 | `Ripple Effect (Closeness):` 0.295659
  * `Imports (Out-Degree: 6):` collections, collections.abc, copy, google.protobuf, google.protobuf.json_format, proto, proto.fields, proto.marshal...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `proto_plus-1.27.2/tests/test_message.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.185)
- **Top Global Matches:** file_cluster_11: 7.185, file_cluster_12: 7.638, file_cluster_15: 7.877
- **Magnitude:** 266.12 | **LOC:** 503 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (43.1%), Guard Balance (formerly Safety Score) (34.8%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_serialize_to_dict_float_precision` **(Defensive Guards)** (Impact: 12.4)
  * `test_serialize_to_dict` **(I/O & Config Routines)** (Impact: 10.7)
  * `test_dir` **(I/O & Config Routines)** (Impact: 4.3)
  * `test_copy_from` **(Defensive Guards)** (Impact: 2.1)
  * `test_unknown_field_deserialize_keep_fields` **(Defensive Guards)** (Impact: 2.0)
    * *Intent:* # This is a somewhat common setup: a client uses an older proto definition, # while the server sends...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 164`, `args: 26`, `func_start: 26`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 113`, `unreferenced_by_name: 26`
* *Architecture:* `api: 61`, `import: 3`
* *Defense:* `safety: 110`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` itertools, proto, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_fields_enum.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.294)
- **Top Global Matches:** file_cluster_11: 6.294, file_cluster_15: 7.645, file_cluster_2: 7.951
- **Magnitude:** 220.22 | **LOC:** 394 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.0%), Complexity Load (formerly Cognitive Load) (25.2%), Connectivity (formerly Api Exposure) (13.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_nested_enum_from_string` **(I/O & Config Routines)** (Impact: 2.2)
  * `test_unwrapped_enum_fields` **(Interface Declarations)** (Impact: 2.2)
    * *Intent:* # The dayofweek_pb2 module apparently does some things that are deprecated # in the protobuf API. # ...
  * `test_outer_enum_unset` **(Defensive Guards)** (Impact: 1.9)
  * `test_outer_enum_write_int` **(Defensive Guards)** (Impact: 1.9)
  * `test_outer_enum_write_str` **(Defensive Guards)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 148`, `args: 21`, `func_start: 21`, `class_start: 39`
* *Risk/State:* `state_mutation: 117`, `fragile_debt: 1`, `unreferenced_by_name: 21`
* *Architecture:* `io: 2`, `api: 60`, `import: 9`
* *Defense:* `safety: 85`, `test: 23`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` clam, google.type, mollusc, os, proto, pytest, sys, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_fields_repeated_composite.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.776)
- **Top Global Matches:** file_cluster_12: 6.776, file_cluster_11: 8.669, file_cluster_7: 9.259
- **Magnitude:** 168.0 | **LOC:** 289 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.8%), Complexity Load (formerly Cognitive Load) (40.7%), Connectivity (formerly Api Exposure) (14.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_repeated_composite_marshaled` **(Defensive Guards)** (Impact: 4.2)
  * `test_repeated_composite_init` **(Defensive Guards)** (Impact: 1.6)
  * `test_repeated_composite_outer_write` **(Defensive Guards)** (Impact: 1.6)
  * `test_repeated_composite_append` **(Defensive Guards)** (Impact: 1.6)
  * `test_repeated_composite_insert` **(Defensive Guards)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 119`, `args: 19`, `func_start: 19`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 73`, `unreferenced_by_name: 19`
* *Architecture:* `api: 57`, `import: 6`
* *Defense:* `safety: 51`, `test: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, enum, google.protobuf, proto, proto.datetime_helpers, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/proto/datetime_helpers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.955)
- **Top Global Matches:** file_cluster_16: 6.955, file_cluster_15: 7.126, file_cluster_13: 8.974
- **Magnitude:** 164.9 | **LOC:** 225 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 14.353; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.5%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 22.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `replace` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* # pylint: disable=arguments-differ """Return a date with the same value, except for those parameters...
  * `from_rfc3339` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* """Parse RFC3339-compliant timestamp, preserving nanoseconds. Args: stamp (str): RFC3339 stamp, with...
  * `__new__` **(Compute Cores)** (Impact: 10.4)
    * *Intent:* # pylint: disable=arguments-differ
  * `timestamp_pb` **(Type Conversions)** (Impact: 6.4)
    * *Intent:* """Return a timestamp message. Returns: (:class:`~google.protobuf.timestamp_pb2.Timestamp`): Timesta...
  * `_to_rfc3339` **(Stateful Encapsulated Methods)** (Impact: 6.0)
    * *Intent:* """Convert a datetime to an RFC3339 timestamp string. Args: value (datetime.datetime): The datetime ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 24`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 35`
* *Architecture:* `api: 8`, `import: 3`
* *Defense:* `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.060606
  * `Imports (Out-Degree: 0):` datetime, google.protobuf, re
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `proto_plus-1.27.2/proto/marshal/marshal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.428)
- **Top Global Matches:** file_cluster_12: 6.428, file_cluster_15: 7.982, file_cluster_16: 8.064
- **Magnitude:** 150.64 | **LOC:** 296 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **6**; blast radius 65.84; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (58.4%), Guard Balance (formerly Safety Score) (56.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 62.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_proto` **(Many-Argument Workhorses)** (Impact: 26.9)
    * *Intent:* # The protos in google/protobuf/struct.proto are exceptional cases, # because they can and should re...
  * `to_python` **(Many-Argument Workhorses)** (Impact: 16.8)
    * *Intent:* # Internal protobuf has its own special type for lists of values. # Return a view around it that imp...
  * `register` **(Many-Argument Workhorses)** (Impact: 14.4)
    * *Intent:* """Register a rule against the given ``proto_type``. This function expects a ``proto_type`` (the des...
  * `get_rule` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* # Rules are needed to convert values between proto-plus and pb. # Retrieve the rule for the specifie...
  * `__subclasshook__` **(Defensive Guards)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 76`, `args: 12`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `planned_debt: 2`
* *Architecture:* `api: 15`, `import: 17`
* *Defense:* `safety: 11`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 65.84
  * `Choke Point (Betweenness):` 0.046426 | `Ripple Effect (Closeness):` 0.273945
  * `Imports (Out-Degree: 6):` abc, google.protobuf, proto.marshal, proto.marshal.collections, proto.marshal.rules, proto.primitives
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `proto_plus-1.27.2/tests/test_marshal_types_struct.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.89)
- **Top Global Matches:** file_cluster_11: 5.89, file_cluster_15: 7.662, file_cluster_2: 7.966
- **Magnitude:** 146.36 | **LOC:** 269 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.3%), Connectivity (formerly Api Exposure) (14.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_struct_nested` **(Defensive Guards)** (Impact: 2.0)
  * `test_value_primitives_rmw` **(Defensive Guards)** (Impact: 1.8)
  * `test_list_value_pb` **(Interface Declarations)** (Impact: 1.7)
  * `test_struct_pb` **(Interface Declarations)** (Impact: 1.6)
  * `test_value_primitives_read` **(Defensive Guards)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 92`, `args: 24`, `func_start: 24`, `class_start: 25`
* *Risk/State:* `state_mutation: 60`, `unreferenced_by_name: 24`
* *Architecture:* `api: 49`, `import: 3`
* *Defense:* `safety: 38`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` google.protobuf, proto, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_json.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.99)
- **Top Global Matches:** file_cluster_11: 5.99, file_cluster_15: 7.239, file_cluster_2: 7.946
- **Magnitude:** 135.92 | **LOC:** 282 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.9%), Complexity Load (formerly Cognitive Load) (37.2%), Connectivity (formerly Api Exposure) (11.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_json_float_precision` **(Defensive Guards)** (Impact: 12.5)
  * `test_json_default_values` **(I/O & Config Routines)** (Impact: 9.4)
  * `test_json_stringy_enums` **(I/O & Config Routines)** (Impact: 2.0)
  * `test_json_default_enums` **(Defensive Guards)** (Impact: 2.0)
  * `test_json_unknown_field` **(Defensive Guards)** (Impact: 1.8)
    * *Intent:* # Note that 'lengthCm' is unknown in the local definition. # This could happen if the client is usin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 65`, `args: 12`, `func_start: 12`, `class_start: 14`
* *Risk/State:* `state_mutation: 62`, `unreferenced_by_name: 12`
* *Architecture:* `api: 26`, `import: 4`
* *Defense:* `safety: 31`, `doc: 1`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` google.protobuf.json_format, proto, pytest, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/proto/marshal/collections/repeated.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.378)
- **Top Global Matches:** file_cluster_15: 6.378, file_cluster_16: 6.914, file_cluster_11: 8.28
- **Magnitude:** 124.94 | **LOC:** 190 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 24.48; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 40.7407% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__setitem__` **(Many-Argument Workhorses)** (Impact: 32.6)
    * *Intent:* # The underlying protocol buffer does not define __setitem__, so we # have to implement all the oper...
  * `__eq__` **(Type Conversions)** (Impact: 9.1)
  * `_pb_type` **(Stateful Encapsulated Methods)** (Impact: 8.4)
    * *Intent:* """Return the protocol buffer type for this sequence."""
  * `__eq__` **(Type Conversions)** (Impact: 7.1)
  * `__init__` **(Encapsulated Accessors)** (Impact: 2.8)
    * *Intent:* """Initialize a wrapper around a protobuf repeated field. Args: sequence: A protocol buffers repeate...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 45`, `args: 17`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `state_mutation: 15`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `safety: 8`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.48
  * `Choke Point (Betweenness):` 0.001243 | `Ripple Effect (Closeness):` 0.218182
  * `Imports (Out-Degree: 1):` collections, copy, proto.utils, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `proto_plus-1.27.2/proto/_file_info.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.735)
- **Top Global Matches:** file_cluster_12: 7.735, file_cluster_9: 9.802, file_cluster_16: 10.08
- **Magnitude:** 123.58 | **LOC:** 197 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 7.852; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.7%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_file_pb` **(Many-Argument Workhorses)** (Impact: 19.2)
    * *Intent:* """Generate the descriptors for all protos in the file. This method takes the file descriptor attach...
  * `ready` **(Compute Cores)** (Impact: 17.6)
    * *Intent:* """Return True if a file descriptor may added, False otherwise. This determine if all the messages t...
  * `_calculate_salt` **(Stateful Encapsulated Methods)** (Impact: 12.6)
  * `unresolved_fields` **(Defensive Guards)** (Impact: 10.3)
    * *Intent:* """Return fields with referencing message types as strings."""
  * `maybe_add_descriptor` **(Many-Argument Workhorses)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 31`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 19`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 6`, `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.852
  * `Choke Point (Betweenness):` 0.000233 | `Ripple Effect (Closeness):` 0.015152
  * `Imports (Out-Degree: 1):` collections, google.protobuf, inspect, logging, proto.marshal.rules.message
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `proto_plus-1.27.2/tests/test_marshal_types_dates.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.348)
- **Top Global Matches:** file_cluster_11: 6.348, file_cluster_15: 7.729, file_cluster_2: 7.969
- **Magnitude:** 123.18 | **LOC:** 327 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (22.0%), Connectivity (formerly Api Exposure) (12.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_timestamp_read` **(Defensive Guards)** (Impact: 1.9)
  * `test_timestamp_write` **(Defensive Guards)** (Impact: 1.9)
  * `test_timestamp_rmw_nanos` **(Defensive Guards)** (Impact: 1.9)
  * `test_duration_write_string_nested` **(Defensive Guards)** (Impact: 1.9)
  * `test_timestamp_write_init` **(Defensive Guards)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 129`, `args: 19`, `func_start: 19`, `class_start: 18`
* *Risk/State:* `state_mutation: 49`, `unreferenced_by_name: 19`
* *Architecture:* `api: 37`, `import: 8`
* *Defense:* `safety: 97`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` datetime, google.protobuf, proto, proto.datetime_helpers, proto.marshal.marshal
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/proto/enums.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.529)
- **Top Global Matches:** file_cluster_15: 6.529, file_cluster_16: 7.195, file_cluster_11: 8.298
- **Magnitude:** 120.8 | **LOC:** 166 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 19.389; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (63.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__new__` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* # Do not do any special behavior for `proto.Enum` itself. if bases[0] == enum.IntEnum: return super(...
  * `__eq__` **(Type Conversions)** (Impact: 3.7)
  * `__ne__` **(Type Conversions)** (Impact: 3.7)
  * `__lt__` **(Type Conversions)** (Impact: 3.7)
  * `__le__` **(Type Conversions)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 41`, `args: 11`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `state_mutation: 19`, `fragile_debt: 1`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.389
  * `Choke Point (Betweenness):` 0.021057 | `Ripple Effect (Closeness):` 0.287879
  * `Imports (Out-Degree: 3):` enum, google.protobuf, proto, proto.marshal.rules.enums
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `proto_plus-1.27.2/tests/test_datetime_helpers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.811)
- **Top Global Matches:** file_cluster_11: 6.811, file_cluster_15: 7.848, file_cluster_13: 8.084
- **Magnitude:** 120.34 | **LOC:** 290 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (33.2%), Connectivity (formerly Api Exposure) (11.0%)
- **Documentation Coverage:** 98.0392% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_replace` **(Defensive Guards)** (Impact: 2.2)
  * `test_from_rfc3339_test_nanoseconds` **(Defensive Guards)** (Impact: 2.0)
  * `_to_seconds` **(Encapsulated Accessors)** (Impact: 2.0)
    * *Intent:* """Convert a datetime to seconds since the unix epoch. Args: value (datetime.datetime): The datetime...
  * `test_from_timestamp_pb_wo_nanos` **(Defensive Guards)** (Impact: 1.7)
  * `test_from_timestamp_pb_w_nanos` **(Defensive Guards)** (Impact: 1.7)
    * *Intent:* # assert _to_seconds(when) == _to_seconds(stamp) # assert stamp.microsecond == 0 # assert stamp.nano...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 88`, `args: 26`, `func_start: 26`
* *Risk/State:* `state_mutation: 55`, `unreferenced_by_name: 25`
* *Architecture:* `api: 25`, `import: 6`
* *Defense:* `safety: 49`, `doc: 1`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` calendar, datetime, google.protobuf, proto, pytest, pytz
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/proto/fields.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.383)
- **Top Global Matches:** file_cluster_15: 7.383, file_cluster_0: 7.734, file_cluster_16: 7.911
- **Magnitude:** 118.5 | **LOC:** 166 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **4**; blast radius 94.629; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (41.9%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `descriptor` **(Stateful Encapsulated Methods)** (Impact: 22.0)
    * *Intent:* """Return the descriptor for the field."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 14.1)
  * `pb_type` **(Defensive Guards)** (Impact: 6.4)
    * *Intent:* """Return the composite type of the field, or the primitive type if a primitive."""
  * `__init__` **(Parameter Forwarders)** (Impact: 2.8)
  * `name` **(Generic / Templated Code)** (Impact: 1.6)
    * *Intent:* """Return the name of the field."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 25`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 7`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 94.629
  * `Choke Point (Betweenness):` 0.003419 | `Ripple Effect (Closeness):` 0.500988
  * `Imports (Out-Degree: 1):` enum, google.protobuf, google.protobuf.internal.enum_type_wrapper, proto.primitives
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `proto_plus-1.27.2/proto/marshal/rules/struct.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.893)
- **Top Global Matches:** file_cluster_16: 7.893, file_cluster_15: 8.22, file_cluster_0: 8.8
- **Magnitude:** 89.04 | **LOC:** 144 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.8%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 46.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_python` **(Many-Argument Workhorses)** (Impact: 17.7)
    * *Intent:* """Coerce the given value to the appropriate Python type. Note that both NullValue and absent fields...
  * `to_proto` **(Defensive Guards)** (Impact: 14.9)
    * *Intent:* """Return a protobuf Value object representing this value."""
  * `to_proto` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* # We got a proto, or else something we sent originally. # Preserve the instance we have. if isinstan...
  * `to_proto` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* # We got a proto, or else something we sent originally. # Preserve the instance we have. if isinstan...
  * `to_python` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* """Coerce the given value to a Python sequence."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 40`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `state_mutation: 5`, `duplicate_logic: 3`
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `safety: 10`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` collections.abc, google.protobuf, proto.marshal.collections
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_fields_int.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.434)
- **Top Global Matches:** file_cluster_13: 7.434, file_cluster_2: 7.996, file_cluster_15: 8.048
- **Magnitude:** 67.06 | **LOC:** 139 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.4%), Connectivity (formerly Api Exposure) (11.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_int64_dict_round_trip` **(I/O & Config Routines)** (Impact: 3.1)
    * *Intent:* # When converting a message to other types, protobuf turns int64 fields # into decimal coded strings...
  * `test_int_rmw` **(Defensive Guards)** (Impact: 1.8)
  * `test_int_init` **(Defensive Guards)** (Impact: 1.6)
  * `test_int_size` **(Annotated & Test Methods)** (Impact: 1.6)
  * `test_int_unsigned` **(Annotated & Test Methods)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 45`, `args: 7`, `func_start: 7`, `class_start: 10`
* *Risk/State:* `state_mutation: 36`, `unreferenced_by_name: 7`
* *Architecture:* `api: 17`, `import: 2`
* *Defense:* `safety: 21`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` proto, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_fields_repeated_scalar.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.17)
- **Top Global Matches:** file_cluster_12: 7.17, file_cluster_11: 7.411, file_cluster_15: 8.992
- **Magnitude:** 61.28 | **LOC:** 116 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.4%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_repeated_scalar_append` **(Interface Declarations)** (Impact: 1.4)
  * `test_repeated_scalar_iadd` **(Interface Declarations)** (Impact: 1.4)
  * `test_repeated_scalar_setitem` **(Defensive Guards)** (Impact: 1.4)
  * `test_repeated_scalar_overwrite` **(Interface Declarations)** (Impact: 1.4)
  * `test_repeated_scalar_eq_ne` **(Defensive Guards)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 41`, `args: 10`, `func_start: 10`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `unreferenced_by_name: 10`
* *Architecture:* `api: 20`, `import: 3`
* *Defense:* `safety: 13`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` copy, proto, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.995)
- **Top Global Matches:** file_cluster_15: 6.995, file_cluster_16: 7.822, file_cluster_9: 8.819
- **Magnitude:** 54.48 | **LOC:** 116 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.6%), Connectivity (formerly Api Exposure) (3.1%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pytest_runtest_setup` **(Compute Cores)** (Impact: 21.8)
  * `_register_messages` **(Stateful Encapsulated Methods)** (Impact: 4.5)
    * *Intent:* """Create and register messages from the file descriptor."""
  * `pytest_runtest_teardown` **(Parameter Forwarders)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 24`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `doc: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` google.protobuf, importlib, proto._file_info, proto.marshal, proto.utils, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_marshal_types_enum.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.327)
- **Top Global Matches:** file_cluster_11: 5.327, file_cluster_2: 7.403, file_cluster_15: 7.5
- **Magnitude:** 53.68 | **LOC:** 101 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_enum_append` **(I/O & Config Routines)** (Impact: 1.9)
  * `test_enum_map_insert` **(I/O & Config Routines)** (Impact: 1.9)
  * `test_to_proto` **(Interface Declarations)** (Impact: 1.6)
  * `test_to_python` **(Interface Declarations)** (Impact: 1.5)
  * `test_to_python_unknown_value` **(Interface Declarations)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 25`, `args: 5`, `func_start: 5`, `class_start: 7`
* *Risk/State:* `state_mutation: 32`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `safety: 5`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` proto, proto.marshal.rules.enums, unittest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_fields_composite_string_ref.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.588)
- **Top Global Matches:** file_cluster_15: 7.588, file_cluster_2: 7.626, file_cluster_11: 7.728
- **Magnitude:** 53.26 | **LOC:** 107 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.8%), Connectivity (formerly Api Exposure) (12.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_composite_forward_ref_with_package` **(Defensive Guards)** (Impact: 2.2)
  * `test_composite_multi_ref` **(Defensive Guards)** (Impact: 1.9)
  * `test_composite_forward_ref` **(Defensive Guards)** (Impact: 1.6)
  * `test_composite_backward_ref` **(Defensive Guards)** (Impact: 1.6)
  * `test_composite_self_ref` **(Defensive Guards)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 43`, `args: 5`, `func_start: 5`, `class_start: 11`
* *Risk/State:* `state_mutation: 27`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 16`, `import: 2`
* *Defense:* `safety: 22`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` proto, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_fields_composite.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.968)
- **Top Global Matches:** file_cluster_11: 5.968, file_cluster_15: 7.751, file_cluster_13: 8.092
- **Magnitude:** 52.4 | **LOC:** 94 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.0%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_composite_init` **(Defensive Guards)** (Impact: 1.6)
  * `test_composite_inner_rmw` **(Defensive Guards)** (Impact: 1.6)
  * `test_composite_del` **(Defensive Guards)** (Impact: 1.6)
  * `test_composite_empty_inner_rmw` **(Interface Declarations)** (Impact: 1.5)
  * `test_composite_outer_rmw` **(Interface Declarations)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 31`, `args: 6`, `func_start: 6`, `class_start: 12`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 6`
* *Architecture:* `api: 18`, `import: 1`
* *Defense:* `safety: 12`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` proto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_modules.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.631)
- **Top Global Matches:** file_cluster_15: 7.631, file_cluster_16: 8.279, file_cluster_11: 8.477
- **Magnitude:** 50.78 | **LOC:** 136 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (34.7%), Complexity Load (formerly Cognitive Load) (32.7%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__getattr__` **(Parameter Forwarders)** (Impact: 3.7)
  * `test_module_manifest` **(Defensive Guards)** (Impact: 2.8)
  * `test_module_package_cross_api` **(Defensive Guards)** (Impact: 2.5)
  * `test_module_package_explicit_marshal` **(Defensive Guards)** (Impact: 1.8)
  * `__init__` **(Encapsulated Accessors)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 46`, `args: 7`, `func_start: 6`, `class_start: 8`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 6`
* *Architecture:* `io: 7`, `api: 12`, `import: 5`
* *Defense:* `safety: 24`, `doc: 1`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` google.protobuf, inspect, proto, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_marshal_types_wrappers_bool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.359)
- **Top Global Matches:** file_cluster_11: 6.359, file_cluster_15: 7.418, file_cluster_2: 7.732
- **Magnitude:** 47.18 | **LOC:** 123 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (33.5%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_bool_value_rmw` **(Defensive Guards)** (Impact: 1.7)
  * `test_bool_value_init` **(Defensive Guards)** (Impact: 1.6)
  * `test_bool_value_init_dict` **(Defensive Guards)** (Impact: 1.6)
  * `test_bool_value_distinction_from_bool` **(Defensive Guards)** (Impact: 1.6)
  * `test_bool_value_write_bool_value` **(Interface Declarations)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 43`, `args: 8`, `func_start: 8`, `class_start: 7`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 8`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `safety: 22`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` google.protobuf, proto, proto.marshal.marshal
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/tests/test_fields_map_composite.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.048)
- **Top Global Matches:** file_cluster_2: 7.048, file_cluster_15: 7.194, file_cluster_11: 7.348
- **Magnitude:** 46.34 | **LOC:** 118 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 6.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.8%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_composite_map_dict` **(Defensive Guards)** (Impact: 2.0)
  * `test_composite_map_set` **(Defensive Guards)** (Impact: 2.0)
  * `test_composite_map` **(Defensive Guards)** (Impact: 1.9)
  * `test_composite_map_deep_set` **(Defensive Guards)** (Impact: 1.9)
  * `test_composite_map_del` **(Defensive Guards)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 36`, `args: 5`, `func_start: 5`, `class_start: 10`
* *Risk/State:* `state_mutation: 20`, `unreferenced_by_name: 5`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `safety: 17`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` proto, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proto_plus-1.27.2/proto/marshal/rules/wrappers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.683)
- **Top Global Matches:** file_cluster_15: 6.683, file_cluster_2: 6.878, file_cluster_11: 7.261
- **Magnitude:** 42.78 | **LOC:** 85 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.119; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.8%), Guard Balance (formerly Safety Score) (61.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_python` **(Defensive Guards)** (Impact: 6.3)
  * `to_proto` **(Defensive Guards)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 19`, `args: 2`, `func_start: 2`, `class_start: 10`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 2`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` google.protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `proto_plus-1.27.2/tests/test_fields_oneof.py` (PYTHON) | Magnitude: 20.18 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 17, safety: 12, state_mutation: 12
- `proto_plus-1.27.2/tests/test_fields_composite_string_ref.py` (PYTHON) | Magnitude: 53.26 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 43, state_mutation: 27, core_var_decl: 26
- `proto_plus-1.27.2/tests/test_fields_map_scalar.py` (PYTHON) | Magnitude: 23.34 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 23, safety: 13, state_mutation: 9
- `proto_plus-1.27.2/tests/test_fields_string.py` (PYTHON) | Magnitude: 21.48 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 24, safety: 16, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `proto_plus-1.27.2/tests/test_fields_optional.py` (PYTHON) | Magnitude: 27.28 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 32, safety: 23, state_mutation: 16
- `proto_plus-1.27.2/tests/test_message_pickling.py` (PYTHON) | Magnitude: 30.06 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 13, core_var_decl: 12, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `proto_plus-1.27.2/tests/test_marshal_register.py` (PYTHON) | Magnitude: 18.54 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 16, api: 7, test: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `proto_plus-1.27.2/proto/__init__.py` -> **Severity: 10.058** (Bridge: 0.1006 * Flux: 99.9986%)
- `proto_plus-1.27.2/proto/marshal/marshal.py` -> **Severity: 4.642** (Bridge: 0.0464 * Flux: 99.9851%)
- `proto_plus-1.27.2/proto/message.py` -> **Severity: 2.339** (Bridge: 0.0234 * Flux: 100.0%)
- `proto_plus-1.27.2/proto/enums.py` -> **Severity: 2.106** (Bridge: 0.0211 * Flux: 100.0%)
- `proto_plus-1.27.2/proto/fields.py` -> **Severity: 0.342** (Bridge: 0.0034 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `proto_plus-1.27.2/proto/__init__.py` -> **Severity: 34.829** (Embedded: 0.561 * Error Risk: 62.0848%)
- `proto_plus-1.27.2/proto/fields.py` -> **Severity: 33.953** (Embedded: 0.501 * Error Risk: 67.7724%)
- `proto_plus-1.27.2/proto/primitives.py` -> **Severity: 23.44** (Embedded: 0.3794 * Error Risk: 61.7748%)
- `proto_plus-1.27.2/proto/message.py` -> **Severity: 21.42** (Embedded: 0.2957 * Error Risk: 72.4496%)
- `proto_plus-1.27.2/proto/enums.py` -> **Severity: 19.698** (Embedded: 0.2879 * Error Risk: 68.4242%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `proto_plus-1.27.2/proto/marshal/marshal.py` -> **Severity: 4115.0** (Blast Radius: 65.84 * Doc Risk: 62.5%)
- `proto_plus-1.27.2/proto/utils.py` -> **Severity: 3286.5** (Blast Radius: 52.584 * Doc Risk: 62.5%)
- `proto_plus-1.27.2/proto/marshal/collections/maps.py` -> **Severity: 2015.999** (Blast Radius: 24.48 * Doc Risk: 82.3529%)
- `proto_plus-1.27.2/proto/enums.py` -> **Severity: 1938.9** (Blast Radius: 19.389 * Doc Risk: 100.0%)
- `proto_plus-1.27.2/proto/modules.py` -> **Severity: 1938.9** (Blast Radius: 19.389 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1350 call pairs -- scoped 46.7%, unique 0.0%, ambiguous 6.3%, external 47.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 1350 | 46.7% | 0.0% | 6.3% | 47.0% |

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
