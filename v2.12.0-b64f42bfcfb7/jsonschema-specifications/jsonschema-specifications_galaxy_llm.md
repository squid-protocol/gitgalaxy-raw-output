# ARCHITECTURAL_BRIEF: jsonschema-specifications
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
- **Scope:** 17 analyzed artifact(s), 950 LOC.
- **Load-bearing artifact:** `jsonschema_specifications-2025.9.1/jsonschema_specifications/_core.py` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `jsonschema_specifications-2025.9.1/.github/workflows/ci.yml` -- pulls in 5 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `jsonschema_specifications-2025.9.1/noxfile.py` at magnitude 85.54 (structural weight, not risk).
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
| Total Artifacts | 38 |
| Analyzed Artifacts (Scanned) | 17 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 21 |
| Total LOC | 950 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 44.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 6 | 707 | 35.3% |
| PYTHON | 5 | 144 | 29.4% |
| YAML | 4 | 99 | 23.5% |
| MARKDOWN | 1 | 0 | 5.9% |
| PLAINTEXT | 1 | 0 | 5.9% |

## 4.1 SOURCE ENCODINGS
All 17 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 82%, Declarative / Non-Code 6%, Large Core Modules (2) 6%, Large Core Modules (3) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 15 | 88.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 11.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 21*

**Composition by Extension & Reason:**
- `no_extension`: 15x Unsupported Format (.undeterminable), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 29.1 | 3.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 67.4 | 13.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 83.5 | 6.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.5 | 2.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 20.1 | 3.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 12.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3 | 2 | 0 | `jsonschema_specifications-2025.9.1/noxfile.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 11 | 3 | 1 | `jsonschema_specifications-2025.9.1/jsonschema_specifications/tests/test_jsonschema_specifications.py` |
| danger | 1 | 1 | 0 | `jsonschema_specifications-2025.9.1/noxfile.py` |
| concurrency | 1 | 1 | 0 | `jsonschema_specifications-2025.9.1/jsonschema_specifications/_core.py` |
| connectivity | 15 | 5 | 1 | `jsonschema_specifications-2025.9.1/noxfile.py` |
| io | 4 | 3 | 1 | `jsonschema_specifications-2025.9.1/.github/workflows/ci.yml` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 3 | 2 | 0 | `jsonschema_specifications-2025.9.1/.github/workflows/ci.yml` |
| tests | 8 | 2 | 0 | `jsonschema_specifications-2025.9.1/jsonschema_specifications/tests/test_jsonschema_specifications.py` |
| docs | 14 | 5 | 2 | `jsonschema_specifications-2025.9.1/noxfile.py` |
| debt | 2 | 1 | 0 | `jsonschema_specifications-2025.9.1/.github/workflows/ci.yml` |
| mutation | 50 | 5 | 4 | `jsonschema_specifications-2025.9.1/noxfile.py` |
| dead_code | 7 | 2 | 0 | `jsonschema_specifications-2025.9.1/noxfile.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 1 | 1 | 0 | `jsonschema_specifications-2025.9.1/jsonschema_specifications/__init__.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `jsonschema_specifications-2025.9.1/.github/workflows/ci.yml` (Hits: 2)
- `jsonschema_specifications-2025.9.1/jsonschema_specifications/tests/test_jsonschema_specifications.py` (Hits: 1)
- `jsonschema_specifications-2025.9.1/noxfile.py` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_core.py** (`jsonschema_specifications-2025.9.1/jsonschema_specifications/_core.py`) — 2 inbound connections
2. **__init__.py** (`jsonschema_specifications-2025.9.1/jsonschema_specifications/__init__.py`) — 1 inbound connections
3. **FUNDING.yml** (`jsonschema_specifications-2025.9.1/.github/FUNDING.yml`) — 0 inbound connections
4. **dependabot.yml** (`jsonschema_specifications-2025.9.1/.github/dependabot.yml`) — 0 inbound connections
5. **release.yml** (`jsonschema_specifications-2025.9.1/.github/release.yml`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ci.yml** (`jsonschema_specifications-2025.9.1/.github/workflows/ci.yml`) — 5 outbound dependencies
2. **_core.py** (`jsonschema_specifications-2025.9.1/jsonschema_specifications/_core.py`) — 4 outbound dependencies
3. **test_jsonschema_specifications.py** (`jsonschema_specifications-2025.9.1/jsonschema_specifications/tests/test_jsonschema_specifications.py`) — 4 outbound dependencies
4. **noxfile.py** (`jsonschema_specifications-2025.9.1/noxfile.py`) — 4 outbound dependencies
5. **__init__.py** (`jsonschema_specifications-2025.9.1/jsonschema_specifications/__init__.py`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_schemas` **(Stateful Encapsulated Methods)** (@ `jsonschema_specifications-2025.9.1/jsonschema_specifications/_core.py`) -> Impact: **9.1** | LOC: 22
  * *Intent:* """ All schemas we ship. """
- `requirements` **(Compute Cores)** (@ `jsonschema_specifications-2025.9.1/noxfile.py`) -> Impact: **6.5** | LOC: 16
  * *Intent:* """ Update the project's pinned requirements. You should commit the result afterwards. """
- `docs` **(Compute Cores)** (@ `jsonschema_specifications-2025.9.1/noxfile.py`) -> Impact: **6.2** | LOC: 21
  * *Intent:* """ Build the documentation using a specific Sphinx builder. """
- `session` **(Encapsulated Accessors)** (@ `jsonschema_specifications-2025.9.1/noxfile.py`) -> Impact: **4.3** | LOC: 7
- `Install dependencies` **(I/O & Config Routines)** (@ `jsonschema_specifications-2025.9.1/.github/workflows/ci.yml`) -> Impact: **4.2** | LOC: 3
- `Install dependencies` **(I/O & Config Routines)** (@ `jsonschema_specifications-2025.9.1/.github/workflows/ci.yml`) -> Impact: **3.1** | LOC: 3
- `_session` **(Encapsulated Accessors)** (@ `jsonschema_specifications-2025.9.1/noxfile.py`) -> Impact: **3.0** | LOC: 4
- `test_it_copes_with_dotfiles` **(Defensive Guards)** (@ `jsonschema_specifications-2025.9.1/jsonschema_specifications/tests/test_jsonschema_specifications.py`) -> Impact: **2.3** | LOC: 18
  * *Intent:* """ Ignore files like .DS_Store if someone has actually caused one to exist. We test here through the private interface as of course the global has al...
- `docs_style` **(Parameter Forwarders)** (@ `jsonschema_specifications-2025.9.1/noxfile.py`) -> Impact: **1.9** | LOC: 10
  * *Intent:* """ Check the documentation style. """
- `tests` **(Type Conversions)** (@ `jsonschema_specifications-2025.9.1/noxfile.py`) -> Impact: **1.8** | LOC: 7
  * *Intent:* """ Run the test suite with a corresponding Python version. """

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Encapsulated Accessors**: getters/setters and private-scope accessors
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Parameter Forwarders**: thin, many-argument glue that forwards to other code
  * **Stateful Encapsulated Methods**: n/a
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `jsonschema_specifications-2025.9.1` | 2 | 86.54 | 14.54% | 41.77% |
| `jsonschema_specifications-2025.9.1/.github` | 4 | 37.24 | 0.0% | 0.0% |
| `jsonschema_specifications-2025.9.1/jsonschema_specifications` | 2 | 31.56 | 5.56% | 0.0% |
| `jsonschema_specifications-2025.9.1/jsonschema_specifications/tests` | 2 | 21.6 | 0.0% | 0.0% |
| `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft7` | 1 | 18.32 | 0.0% | 0.0% |
| `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft6` | 1 | 18.06 | 0.0% | 0.0% |
| `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft4` | 1 | 17.98 | 0.0% | 0.0% |
| `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft3` | 1 | 17.82 | 0.0% | 0.0% |
| `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft202012` | 1 | 16.14 | 0.0% | 0.0% |
| `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft201909` | 1 | 15.82 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `jsonschema_specifications-2025.9.1/noxfile.py` -> **83.5306%** Exposure
- `jsonschema_specifications-2025.9.1/.github/workflows/ci.yml` -> **12.7273%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `jsonschema_specifications-2025.9.1/noxfile.py` -> **100.0%** Exposure
- `jsonschema_specifications-2025.9.1/jsonschema_specifications/_core.py` -> **91.6827%** Exposure
- `jsonschema_specifications-2025.9.1/jsonschema_specifications/__init__.py` -> **31.0026%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `jsonschema_specifications-2025.9.1/noxfile.py` -> **4** Orphaned Functions | **0** Duplicates
- `jsonschema_specifications-2025.9.1/jsonschema_specifications/tests/test_jsonschema_specifications.py` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `19` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `jsonschema_specifications-2025.9.1/noxfile.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.885)
- **Top Global Matches:** file_cluster_12: 6.885, file_cluster_15: 7.067, file_cluster_13: 8.059
- **Magnitude:** 85.54 | **LOC:** 150 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 52.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (83.5%), Guard Balance (formerly Safety Score) (67.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 12.5921% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `requirements` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* """ Update the project's pinned requirements. You should commit the result afterwards. """
  * `docs` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* """ Build the documentation using a specific Sphinx builder. """
  * `session` **(Encapsulated Accessors)** (Impact: 4.3)
  * `_session` **(Encapsulated Accessors)** (Impact: 3.0)
  * `docs_style` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* """ Check the documentation style. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 22`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `api: 9`, `import: 4`
* *Defense:* `doc: 8`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nox, os, pathlib, tempfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft7/metaschema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.113)
- **Top Global Matches:** file_cluster_2: 2.113, file_cluster_17: 4.926, file_cluster_13: 6.282
- **Magnitude:** 18.32 | **LOC:** 167 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft6/metaschema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.099)
- **Top Global Matches:** file_cluster_2: 2.099, file_cluster_17: 4.921, file_cluster_13: 6.277
- **Magnitude:** 18.06 | **LOC:** 154 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft4/metaschema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.095)
- **Top Global Matches:** file_cluster_2: 2.095, file_cluster_17: 4.919, file_cluster_13: 6.275
- **Magnitude:** 17.98 | **LOC:** 150 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft3/metaschema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.086)
- **Top Global Matches:** file_cluster_2: 2.086, file_cluster_17: 4.915, file_cluster_13: 6.272
- **Magnitude:** 17.82 | **LOC:** 173 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/_core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.908)
- **Top Global Matches:** file_cluster_9: 6.908, file_cluster_16: 11.86, file_cluster_15: 12.806
- **Magnitude:** 16.48 | **LOC:** 39 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 138.305; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (51.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (11.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_schemas` **(Stateful Encapsulated Methods)** (Impact: 9.1)
    * *Intent:* """ All schemas we ship. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 138.305
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.125
  * `Imports (Out-Degree: 0):` importlib.resources, importlib_resources, json, referencing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft202012/metaschema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.998)
- **Top Global Matches:** file_cluster_2: 1.998, file_cluster_17: 4.882, file_cluster_13: 6.238
- **Magnitude:** 16.14 | **LOC:** 59 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/schemas/draft201909/metaschema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.993)
- **Top Global Matches:** file_cluster_2: 1.993, file_cluster_17: 4.881, file_cluster_13: 6.235
- **Magnitude:** 15.82 | **LOC:** 43 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.322)
- **Top Global Matches:** file_cluster_2: 4.322, file_cluster_17: 5.322, file_cluster_13: 5.682
- **Magnitude:** 15.08 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 74.759; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (31.0%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 74.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 1):` jsonschema_specifications._core, referencing.jsonschema
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `jsonschema_specifications-2025.9.1/.github/workflows/ci.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.279)
- **Top Global Matches:** file_cluster_2: 5.279, file_cluster_15: 6.444, file_cluster_17: 6.623
- **Magnitude:** 13.44 | **LOC:** 101 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 52.462; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (12.7%), Complexity Load (formerly Cognitive Load) (6.7%), Connectivity (formerly Api Exposure) (3.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Install dependencies` **(I/O & Config Routines)** (Impact: 4.2)
  * `Install dependencies` **(I/O & Config Routines)** (Impact: 3.1)
  * `run` **(I/O & Config Routines)** (Impact: 1.2)
  * `Run nox` **(I/O & Config Routines)** (Impact: 1.1)
  * `Build our distributions` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 10`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 9`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v5, setup-python@v5, setup-uv@v6, v1, action-gh-release@v2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/.github/dependabot.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.62)
- **Top Global Matches:** file_cluster_2: 3.62, file_cluster_17: 5.751, file_cluster_13: 6.91
- **Magnitude:** 13.12 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/.github/release.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.266)
- **Top Global Matches:** file_cluster_2: 2.266, file_cluster_17: 5.005, file_cluster_13: 6.316
- **Magnitude:** 12.6 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/tests/test_jsonschema_specifications.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.452)
- **Top Global Matches:** file_cluster_13: 7.452, file_cluster_15: 8.146, file_cluster_11: 8.264
- **Magnitude:** 11.08 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 52.462; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.6%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_it_copes_with_dotfiles` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* """ Ignore files like .DS_Store if someone has actually caused one to exist. We test here through th...
  * `test_it_contains_metaschemas` **(Defensive Guards)** (Impact: 1.2)
  * `test_it_is_crawled` **(Defensive Guards)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 3`, `import: 5`
* *Defense:* `safety: 7`, `doc: 1`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` collections.abc, jsonschema_specifications, pathlib, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/.github/FUNDING.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 10.52 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/jsonschema_specifications/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/.github/SECURITY.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jsonschema_specifications-2025.9.1/COPYING` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 52.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `jsonschema_specifications-2025.9.1/jsonschema_specifications/_core.py` -> **Severity: 6.393** (Embedded: 0.125 * Error Risk: 51.1427%)
- `jsonschema_specifications-2025.9.1/jsonschema_specifications/__init__.py` -> **Severity: 3.205** (Embedded: 0.0625 * Error Risk: 51.2854%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `jsonschema_specifications-2025.9.1/jsonschema_specifications/tests/test_jsonschema_specifications.py` -> **Severity: 3497.468** (Blast Radius: 52.462 * Doc Risk: 66.6667%)
- `jsonschema_specifications-2025.9.1/noxfile.py` -> **Severity: 660.607** (Blast Radius: 52.462 * Doc Risk: 12.5921%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 49 call pairs -- scoped 6.1%, unique 0.0%, ambiguous 0.0%, external 93.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 49 | 6.1% | 0.0% | 0.0% | 93.9% |

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
