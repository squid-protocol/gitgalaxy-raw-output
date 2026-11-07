# ARCHITECTURAL_BRIEF: orjson
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
- **Scope:** 542 analyzed artifact(s), 111087 LOC.
- **Load-bearing artifact:** `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/object.rs` -- 91 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `orjson-3.11.8/src/ffi/mod.rs` -- pulls in 205 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/cfi.rs` at magnitude 1789.12 (structural weight, not risk).
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
| Total Artifacts | 637 |
| Analyzed Artifacts (Scanned) | 542 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 95 |
| Total LOC | 111087 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 85.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7565 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2648 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 34.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.28 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 30 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 429 | 104191 | 79.2% |
| PYTHON | 35 | 5833 | 6.5% |
| MARKDOWN | 32 | 0 | 5.9% |
| PLAINTEXT | 26 | 0 | 4.8% |
| YAML | 13 | 563 | 2.4% |
| SHELL | 5 | 37 | 0.9% |
| JSON | 1 | 398 | 0.2% |
| CSS | 1 | 65 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 542 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 15%, Declarative / Non-Code 15%, Parameter Forwarders Files 14%, State Mutators Files 13%, Generic / Templated Code Files 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 484 | 89.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 58 | 10.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 95*

**Composition by Extension & Reason:**
- `.json`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 22x Excluded (Unsupported Extension: '.toml')
- `.orig`: 15x Excluded (Unsupported Extension: '.orig')
- `.lock`: 14x Excluded (Unsupported Extension: '.lock')
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.0`: 1x Excluded (Unsupported Extension: '.0')
- `.apache2`: 1x Excluded (Unsupported Extension: '.Apache2')
- `.mit`: 1x Excluded (Unsupported Extension: '.MIT')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.c`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (Saturation: Line 11 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.6 | 9.1 | 6.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.1 | 27.7 | 37.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.3 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 37.4 | 34.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 95.6 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 68.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1350 | 178 | 7 | `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/cfi.rs` |
| cleanup | 80 | 15 | 0 | `orjson-3.11.8/include/cargo/portable-atomic-util-0.2.6/tests/arc.rs` |
| guards | 3445 | 362 | 18 | `orjson-3.11.8/test/test_numpy.py` |
| danger | 2111 | 164 | 8 | `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/cfi.rs` |
| concurrency | 668 | 102 | 2 | `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/lib.rs` |
| connectivity | 8903 | 437 | 37 | `orjson-3.11.8/test/test_fragment.py` |
| io | 94 | 37 | 0 | `orjson-3.11.8/test/test_default.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 8 | 8 | 0 | `orjson-3.11.8/include/cargo/find-msvc-tools-0.1.9/src/find_tools.rs` |
| time | 78 | 14 | 0 | `orjson-3.11.8/test/test_datetime.py` |
| serialization | 2 | 1 | 0 | `orjson-3.11.8/include/cargo/target-lexicon-0.13.5/src/lib.rs` |
| regex | 3 | 2 | 0 | `orjson-3.11.8/include/cargo/once_cell-1.21.4/examples/regex.rs` |
| events | 21 | 8 | 0 | `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/detect/auxv.rs` |
| tests | 6025 | 218 | 23 | `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/tests/helper.rs` |
| docs | 18244 | 184 | 58 | `orjson-3.11.8/include/cargo/bytes-1.11.1/src/buf/buf_impl.rs` |
| debt | 728 | 118 | 3 | `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/tests/helper.rs` |
| mutation | 18872 | 407 | 66 | `orjson-3.11.8/include/cargo/gimli-0.32.3/src/arch.rs` |
| dead_code | 1736 | 91 | 3 | `orjson-3.11.8/test/test_fragment.py` |
| credential | 3 | 2 | 0 | `orjson-3.11.8/include/cargo/simdutf8-0.1.5/tests/tests.rs` |
| threat | 12 | 7 | 0 | `orjson-3.11.8/test/test_type.py` |
| ml_ai | 134 | 30 | 0 | `orjson-3.11.8/include/cargo/bytes-1.11.1/src/buf/buf_impl.rs` |
| ui | 1 | 1 | 0 | `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/rustdoc.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `orjson-3.11.8/test/test_default.py` (Hits: 12)
- `orjson-3.11.8/include/cargo/pyo3-build-config-0.28.2/src/lib.rs` (Hits: 9)
- `orjson-3.11.8/include/cargo/bytes-1.11.1/tests/test_take.rs` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **object.rs** (`orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/object.rs`) — 91 inbound connections
2. **common.rs** (`orjson-3.11.8/include/cargo/gimli-0.32.3/src/common.rs`) — 44 inbound connections
3. **lib.rs** (`orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/lib.rs`) — 42 inbound connections
4. **mod.rs** (`orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/mod.rs`) — 36 inbound connections
5. **endianity.rs** (`orjson-3.11.8/include/cargo/gimli-0.32.3/src/endianity.rs`) — 34 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`orjson-3.11.8/src/ffi/mod.rs`) — 205 outbound dependencies
2. **lib.rs** (`orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/lib.rs`) — 117 outbound dependencies
3. **dwarf.rs** (`orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/dwarf.rs`) — 78 outbound dependencies
4. **mod.rs** (`orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/cpython/mod.rs`) — 64 outbound dependencies
5. **mod.rs** (`orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/mod.rs`) — 63 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `write` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/op.rs`) -> Impact: **358.7** | LOC: 242
- `write` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/line.rs`) -> Impact: **215.7** | LOC: 198
  * *Intent:* /// Write the line number program to the given section. /// /// # Panics /// /// Panics if `self.is_none()`.
- `write` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/unit.rs`) -> Impact: **212.8** | LOC: 237
  * *Intent:* /// Write the attribute value to the given sections.
- `evaluate_one_operation` **(Compute Cores)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/op.rs`) -> Impact: **191.0** | LOC: 370
- `write` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/cfi.rs`) -> Impact: **169.0** | LOC: 116
- `main` **(I/O & Config Routines)** (@ `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/build.rs`) -> Impact: **133.9** | LOC: 498
- `parse_attribute` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/unit.rs`) -> Impact: **127.2** | LOC: 224
- `from` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/op.rs`) -> Impact: **127.0** | LOC: 211
  * *Intent:* /// Create an expression from the input expression.
- `parse` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/op.rs`) -> Impact: **124.1** | LOC: 403
  * *Intent:* /// Parse a single DWARF expression operation. /// /// This is useful when examining a DWARF expression for reasons other /// than direct evaluation. ...
- `parse` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/line.rs`) -> Impact: **122.2** | LOC: 141

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read` | 24 | 9461.4 | 7.13% | 23.78% |
| `orjson-3.11.8/test` | 34 | 4529.14 | 8.71% | 0.0% |
| `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write` | 14 | 4368.34 | 6.98% | 15.62% |
| `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src` | 58 | 3566.42 | 1.51% | 2.95% |
| `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/cpython` | 33 | 1835.86 | 1.5% | 1.37% |
| `orjson-3.11.8/include/cargo/gimli-0.32.3/src` | 7 | 1537.5 | 14.4% | 2.48% |
| `orjson-3.11.8/include/cargo/pyo3-build-config-0.28.2/src` | 4 | 1256.26 | 9.26% | 13.78% |
| `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/tests` | 2 | 1176.46 | 12.81% | 0.0% |
| `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/atomic128` | 9 | 1077.66 | 13.52% | 6.64% |
| `orjson-3.11.8/include/cargo/find-msvc-tools-0.1.9/src` | 10 | 1063.34 | 5.55% | 0.79% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `orjson-3.11.8/include/cargo/cfg-if-1.0.4/src/lib.rs` -> **100.0%** Exposure
- `orjson-3.11.8/include/cargo/once_cell-1.21.4/src/lib.rs` -> **100.0%** Exposure
- `orjson-3.11.8/include/cargo/bytes-1.11.1/.github/workflows/ci.yml` -> **100.0%** Exposure
- `orjson-3.11.8/src/serialize/writer/json.rs` -> **99.9996%** Exposure
- `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/dwarf.rs` -> **99.7748%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `orjson-3.11.8/include/cargo/bytecount-0.6.9/src/simd/generic.rs` -> **100.0%** Exposure
- `orjson-3.11.8/include/cargo/gimli-0.32.3/src/arch.rs` -> **100.0%** Exposure
- `orjson-3.11.8/src/serialize/writer/str/avx512.rs` -> **100.0%** Exposure
- `orjson-3.11.8/src/serialize/writer/str/generic.rs` -> **100.0%** Exposure
- `orjson-3.11.8/src/serialize/writer/str/sse2.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `orjson-3.11.8/test/test_fragment.py` -> **335** Orphaned Functions | **0** Duplicates
- `orjson-3.11.8/test/test_parsing.py` -> **318** Orphaned Functions | **0** Duplicates
- `orjson-3.11.8/include/cargo/bytes-1.11.1/tests/test_bytes.rs` -> **110** Orphaned Functions | **0** Duplicates
- `orjson-3.11.8/test/test_numpy.py` -> **106** Orphaned Functions | **0** Duplicates
- `orjson-3.11.8/test/test_type.py` -> **93** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4191` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/cfi.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.135)
- **Top Global Matches:** file_cluster_5: 9.135, file_cluster_12: 10.12, file_cluster_0: 11.463
- **Magnitude:** 1789.12 | **LOC:** 7952 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **50**; blast radius 1.056; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (75.0%), Guard Balance (formerly Safety Score) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (28.9%)
- **Documentation Coverage:** 68.9464% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 110.8)
  * `evaluate` **(Many-Argument Workhorses)** (Impact: 54.5)
    * *Intent:* /// Evaluate one call frame instruction. Return `Ok(true)` if the row is /// complete, `Ok(false)` o...
  * `parse_rest` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `parse` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `parse_encoded_pointer` **(Many-Argument Workhorses)** (Impact: 28.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 28 instances
* *High Risk Execution (weighted view):* 8
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 1715`, `args: 373`, `func_start: 325`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 170`, `high_risk_execution: 10`, `state_mutation: 76`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 23`
* *Architecture:* `api: 249`, `import: 32`
* *Defense:* `safety: 30`, `doc: 975`, `test: 418`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.056
  * `Choke Point (Betweenness):` 0.000607 | `Ripple Effect (Closeness):` 0.040578
  * `Imports (Out-Degree: 10):` alloc::boxed::Box, alloc::vec::Vec, core::cmp::Ordering, core::convert::TryFrom, core::convert::TryInto, core::fmt, core::fmt::Debug, core::iter::FromIterator...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/unit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.144)
- **Top Global Matches:** file_cluster_5: 9.144, file_cluster_12: 10.275, file_cluster_0: 11.398
- **Magnitude:** 1447.92 | **LOC:** 6129 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **55**; blast radius 1.788; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (72.4%), Guard Balance (formerly Safety Score) (52.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (26.4%)
- **Documentation Coverage:** 57.9065% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_attribute` **(Many-Argument Workhorses)** (Impact: 127.2)
  * `value` **(Many-Argument Workhorses)** (Impact: 42.2)
    * *Intent:* /// Get this attribute's normalized value. /// /// Attribute values can potentially be encoded in mu...
  * `parse_unit_header` **(Compute Cores)** (Impact: 42.1)
    * *Intent:* /// Parse a unit header.
  * `skip_attributes` **(Many-Argument Workhorses)** (Impact: 41.4)
  * `next` **(Many-Argument Workhorses)** (Impact: 35.3)
    * *Intent:* /// Move the cursor to the next entry at the specified depth. /// /// Requires `depth <= self.depth ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 46 instances
* *High Risk Execution (weighted view):* 23
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 1180`, `args: 312`, `func_start: 247`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 123`, `high_risk_execution: 24`, `state_mutation: 65`, `planned_debt: 19`, `duplicate_logic: 2`
* *Architecture:* `api: 200`, `import: 18`
* *Defense:* `safety: 35`, `doc: 862`, `test: 232`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.788
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.041997
  * `Imports (Out-Degree: 11):` alloc::vec::Vec, core::cell::Cell, core::ops::Range, core::ops::RangeFrom, core::ops::RangeTo, crate::common::DebugAbbrevOffset, crate::common::DebugAddrBase, crate::common::DebugAddrIndex...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/op.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.208)
- **Top Global Matches:** file_cluster_4: 8.208, file_cluster_12: 9.845, file_cluster_0: 10.052
- **Magnitude:** 1287.22 | **LOC:** 4183 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **27**; blast radius 1.159; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.8%), Guard Balance (formerly Safety Score) (58.5%)
- **Documentation Coverage:** 60.2941% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluate_one_operation` **(Compute Cores)** (Impact: 191.0)
  * `parse` **(Many-Argument Workhorses)** (Impact: 124.1)
    * *Intent:* /// Parse a single DWARF expression operation. /// /// This is useful when examining a DWARF express...
  * `evaluate_internal` **(Compute Cores)** (Impact: 31.1)
  * `check_eval_with_args` **(Many-Argument Workhorses)** (Impact: 25.0)
  * `test_eval_memory` **(I/O & Config Routines)** (Impact: 24.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 130 instances
* *High Risk Execution (weighted view):* 33
* *State Mutation (weighted view):* 403
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 484`, `args: 173`, `func_start: 77`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 35`, `state_mutation: 143`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 72`, `import: 41`
* *Defense:* `safety: 12`, `doc: 493`, `test: 49`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.159
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.041418
  * `Imports (Out-Degree: 10):` alloc::vec::Vec, core::mem, crate::common::DebugAddrIndex, crate::common::DebugInfoOffset, crate::common::Encoding, crate::common::Format, crate::common::Register, crate::constants...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/tests/helper.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.387)
- **Top Global Matches:** file_cluster_12: 7.387, file_cluster_13: 7.852, file_cluster_16: 8.048
- **Magnitude:** 1098.84 | **LOC:** 3081 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **20**; blast radius 2.87; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.6%), Connectivity (formerly Api Exposure) (37.2%), Complexity Load (formerly Cognitive Load) (18.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `quickcheck_fetch_max` **(Compute Cores)** (Impact: 20.6)
  * `quickcheck_fetch_min` **(Compute Cores)** (Impact: 20.6)
  * `stress_compare_exchange` **(Annotated & Test Methods)** (Impact: 17.7)
  * `fetch_max` **(Annotated & Test Methods)** (Impact: 17.4)
  * `fetch_min` **(Annotated & Test Methods)** (Impact: 17.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 61 instances
* *Concurrency (weighted view):* 28
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 571`, `args: 284`, `func_start: 144`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 96`, `planned_debt: 49`, `fragile_debt: 5`
* *Architecture:* `api: 50`, `concurrency: 13`, `import: 36`
* *Defense:* `safety: 12`, `test: 527`, `sync_locks: 18`, `immutability_locks: 24`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.000315 | `Ripple Effect (Closeness):` 0.024549
  * `Imports (Out-Degree: 1):` core::sync::atomic::Ordering, crabgrind::memcheck, crate::tests::helper, crate::tests::helper::*, crate::tests::helper::catch_unwind_on_non_seqcst_arch, crate::tests::helper::catch_unwind_on_weak_memory_arch, crossbeam_utils::thread, self::*...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/pyo3-build-config-0.28.2/src/impl_.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.895)
- **Top Global Matches:** file_cluster_5: 7.895, file_cluster_12: 8.126, file_cluster_4: 10.333
- **Magnitude:** 1040.52 | **LOC:** 3381 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **35**; blast radius 1.703; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.8%), Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 54.7368% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default_lib_name_windows` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `search_lib_dir` **(Compute Cores)** (Impact: 51.5)
    * *Intent:* /// recursive search for _sysconfigdata, returns all possibilities of sysconfigdata paths
  * `from_interpreter` **(Compute Cores)** (Impact: 32.3)
  * `default_lib_name_unix` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `to_writer` **(Compute Cores)** (Impact: 29.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 28 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 341`, `args: 167`, `func_start: 119`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 84`, `high_risk_execution: 4`, `state_mutation: 94`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 95`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 38`, `doc: 322`, `test: 130`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.703
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.007394
  * `Imports (Out-Degree: 4):` import_lib.rs, PythonImplementation::*, crate::bail, crate::ensure, crate::errors::Context, crate::errors::Error, crate::errors::Result, crate::warn...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/unit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.143)
- **Top Global Matches:** file_cluster_5: 8.143, file_cluster_12: 9.185, file_cluster_7: 10.551
- **Magnitude:** 1026.48 | **LOC:** 3108 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **61**; blast radius 1.876; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.9%), Connectivity (formerly Api Exposure) (58.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 23.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Many-Argument Workhorses)** (Impact: 212.8)
    * *Intent:* /// Write the attribute value to the given sections.
  * `write` **(Many-Argument Workhorses)** (Impact: 68.6)
    * *Intent:* /// Write the unit to the given sections.
  * `from` **(Many-Argument Workhorses)** (Impact: 67.5)
    * *Intent:* /// Create an attribute value by reading the data in the given sections.
  * `write` **(Many-Argument Workhorses)** (Impact: 51.7)
    * *Intent:* /// Write the entry to the given sections.
  * `size` **(Many-Argument Workhorses)** (Impact: 32.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 638`, `args: 101`, `func_start: 75`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 137`, `high_risk_execution: 14`, `state_mutation: 29`, `planned_debt: 7`
* *Architecture:* `api: 83`, `import: 19`
* *Defense:* `safety: 20`, `doc: 233`, `test: 159`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.876
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.028735
  * `Imports (Out-Degree: 16):` alloc::vec::Vec, crate::LittleEndian, crate::common::DebugAbbrevOffset, crate::common::DebugInfoOffset, crate::common::DebugLineOffset, crate::common::DebugMacinfoOffset, crate::common::DebugMacroOffset, crate::common::DebugStrOffset...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/line.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.261)
- **Top Global Matches:** file_cluster_0: 8.261, file_cluster_13: 10.111, file_cluster_12: 10.119
- **Magnitude:** 1025.42 | **LOC:** 3186 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 1.081; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.8%), Mutation Surface (formerly State Flux) (69.9%), Guard Balance (formerly Safety Score) (50.6%)
- **Documentation Coverage:** 47.2441% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 122.2)
  * `parse_attribute` **(Many-Argument Workhorses)** (Impact: 61.1)
    * *Intent:* // TODO: this should be shared with unit::parse_attribute(), but that is hard to do.
  * `parse` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `execute` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* /// Execute the given instruction, and return true if a new row in the /// line number matrix needs ...
  * `parse_file_v5` **(Many-Argument Workhorses)** (Impact: 22.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 584`, `args: 124`, `func_start: 140`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 3`, `state_mutation: 103`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 140`, `import: 21`
* *Defense:* `safety: 6`, `doc: 429`, `test: 127`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.081
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.040854
  * `Imports (Out-Degree: 8):` alloc::vec::Vec, core::num::NonZeroU64, core::num::Wrapping, crate::common::DebugLineOffset, crate::common::DebugLineStrOffset, crate::common::DebugStrOffset, crate::common::DebugStrOffsetsIndex, crate::common::Encoding...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/arch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.469)
- **Top Global Matches:** file_cluster_2: 6.469, file_cluster_13: 6.638, file_cluster_17: 7.675
- **Magnitude:** 961.0 | **LOC:** 1119 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **3**; blast radius 4.771; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.1%), Connectivity (formerly Api Exposure) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_aarch64_registers` **(Annotated & Test Methods)** (Impact: 3.6)
  * `test_power64_registers` **(Annotated & Test Methods)** (Impact: 3.6)
  * `name_to_register` **(Generic / Templated Code)** (Impact: 3.4)
    * *Intent:* /// Converts a register name into a register number.
  * `register_name` **(Generic / Templated Code)** (Impact: 3.2)
    * *Intent:* /// The name of a register, or `None` if the register number is unknown. /// /// Only returns the pr...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 913
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 24`, `args: 6`, `func_start: 4`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 909`
* *Architecture:* `api: 14`, `import: 5`
* *Defense:* `safety: 2`, `doc: 30`, `test: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.771
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.042444
  * `Imports (Out-Degree: 1):` crate::common::Register, self::*, std::collections::HashSet
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/line.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.607)
- **Top Global Matches:** file_cluster_4: 8.607, file_cluster_12: 11.516, file_cluster_6: 11.821
- **Magnitude:** 950.0 | **LOC:** 2166 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **37**; blast radius 1.371; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.1%), Guard Balance (formerly Safety Score) (58.0%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Many-Argument Workhorses)** (Impact: 215.7)
    * *Intent:* /// Write the line number program to the given section. /// /// # Panics /// /// Panics if `self.is_...
  * `from` **(Many-Argument Workhorses)** (Impact: 91.7)
    * *Intent:* /// Create a line number program by reading the data from the given program. /// /// Return the prog...
  * `write` **(Many-Argument Workhorses)** (Impact: 62.6)
    * *Intent:* /// Write the line number instruction to the given section.
  * `generate_row` **(Compute Cores)** (Impact: 34.6)
    * *Intent:* /// Generates the line number information instructions for the current row. /// /// After the instru...
  * `write` **(Many-Argument Workhorses)** (Impact: 28.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 435`, `args: 52`, `func_start: 43`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 2`, `state_mutation: 117`, `planned_debt: 3`
* *Architecture:* `api: 63`, `import: 16`
* *Defense:* `safety: 15`, `doc: 206`, `test: 61`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.371
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.028328
  * `Imports (Out-Degree: 12):` alloc::vec::Vec, crate::LittleEndian, crate::common::DebugLineOffset, crate::common::Encoding, crate::common::Format, crate::common::LineEncoding, crate::common::SectionId, crate::constants...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/test/test_parsing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.953)
- **Top Global Matches:** file_cluster_15: 8.953, file_cluster_11: 10.05, file_cluster_16: 10.382
- **Magnitude:** 899.36 | **LOC:** 1954 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.714; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (25.1%), Connectivity (formerly Api Exposure) (15.1%), Complexity Load (formerly Cognitive Load) (1.5%)
- **Documentation Coverage:** 0.3135% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_run_fail_json` **(Stateful Encapsulated Methods)** (Impact: 8.8)
  * `_run_pass_json` **(Stateful Encapsulated Methods)** (Impact: 8.4)
  * `test_n_object_lone_continuation_byte_in_key_and_trailing_comma` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* """ n_object_lone_continuation_byte_in_key_and_trailing_comma.json """
  * `test_y_array_arraysWithSpace` **(Parameter Forwarders)** (Impact: 1.7)
    * *Intent:* """ y_array_arraysWithSpaces.json """
  * `test_y_array_empty_string` **(Parameter Forwarders)** (Impact: 1.7)
    * *Intent:* """ y_array_empty-string.json """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 330`, `args: 320`, `func_start: 320`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `unreferenced_by_name: 318`
* *Architecture:* `io: 1`, `api: 319`, `import: 3`
* *Defense:* `safety: 2`, `doc: 318`, `test: 323`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .util, orjson, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/test/test_fragment.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.159)
- **Top Global Matches:** file_cluster_15: 8.159, file_cluster_11: 9.333, file_cluster_13: 9.68
- **Magnitude:** 881.52 | **LOC:** 1062 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.714; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (26.7%), Connectivity (formerly Api Exposure) (16.7%), Complexity Load (formerly Cognitive Load) (3.1%)
- **Documentation Coverage:** 99.7028% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_fragment_pandas` **(Defensive Guards)** (Impact: 3.6)
    * *Intent:* """ Fragment pandas.DataFrame.to_json() """
  * `test_fragment_fragment_str_array` **(Defensive Guards)** (Impact: 3.1)
  * `default` **(Defensive Guards)** (Impact: 3.0)
  * `_run_test` **(Encapsulated Accessors)** (Impact: 1.9)
  * `test_fragment_fragment_not_mut` **(Defensive Guards)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 371`, `args: 337`, `func_start: 337`, `class_start: 3`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 335`
* *Architecture:* `io: 1`, `api: 339`, `import: 4`
* *Defense:* `safety: 20`, `doc: 1`, `test: 344`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .util, orjson, pandas, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/op.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.432)
- **Top Global Matches:** file_cluster_4: 7.432, file_cluster_12: 8.969, file_cluster_15: 10.614
- **Magnitude:** 807.8 | **LOC:** 1763 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **33**; blast radius 1.213; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (58.2%), Guard Balance (formerly Safety Score) (51.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 15.3846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Many-Argument Workhorses)** (Impact: 358.7)
  * `from` **(Many-Argument Workhorses)** (Impact: 127.0)
    * *Intent:* /// Create an expression from the input expression.
  * `size` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `test_operation` **(I/O & Config Routines)** (Impact: 32.5)
  * `write` **(Stateful Encapsulated Methods)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 236`, `args: 53`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 44`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 47`, `import: 17`
* *Defense:* `safety: 22`, `doc: 216`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.213
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.028328
  * `Imports (Out-Degree: 13):` alloc::boxed::Box, alloc::vec::Vec, crate::LittleEndian, crate::common::DebugInfoOffset, crate::common::Encoding, crate::common::Format, crate::common::Register, crate::common::UnitSectionOffset...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.157)
- **Top Global Matches:** file_cluster_0: 8.157, file_cluster_13: 9.292, file_cluster_15: 10.591
- **Magnitude:** 790.44 | **LOC:** 5183 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **55**; blast radius 8.175; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (40.2%)
- **Documentation Coverage:** 64.3979% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compare_exchange` **(Many-Argument Workhorses)** (Impact: 17.1)
    * *Intent:* /// /// `compare_exchange` takes two [`Ordering`] arguments to describe the memory /// ordering of t...
  * `fetch_update` **(Generic / Templated Code)** (Impact: 7.9)
    * *Intent:* /// required ordering for loads. These correspond to the success and failure /// orderings of [`comp...
  * `fetch_update` **(Generic / Templated Code)** (Impact: 7.9)
    * *Intent:* /// /// Panics if `fetch_order` is [`Release`], [`AcqRel`]. /// /// # Considerations /// /// This me...
  * `fetch_update` **(Generic / Templated Code)** (Impact: 7.9)
    * *Intent:* # Considerations
  * `fetch_update` **(Generic / Templated Code)** (Impact: 7.9)
    * *Intent:* /// Fetches the value, and applies a function to it that returns an optional /// new value. Returns ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 383`, `args: 179`, `func_start: 176`, `class_start: 31`
* *Risk/State:* `high_risk_execution: 61`, `state_mutation: 84`, `planned_debt: 12`, `duplicate_logic: 14`, `unreferenced_by_name: 1`
* *Architecture:* `api: 207`, `concurrency: 1`, `import: 50`
* *Defense:* `safety: 4`, `doc: 1451`, `test: 69`, `sync_locks: 142`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.175
  * `Choke Point (Betweenness):` 0.009615 | `Ripple Effect (Closeness):` 0.037716
  * `Imports (Out-Degree: 5):` cfgs, imp, tests, utils, core::fmt, core::hint::*, core::ptr, core::sync::atomic::Ordering...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/dwarf.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.114)
- **Top Global Matches:** file_cluster_0: 6.114, file_cluster_5: 10.272, file_cluster_13: 10.59
- **Magnitude:** 692.88 | **LOC:** 1725 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **78**; blast radius 1.101; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.5%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (55.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 5.4054% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new_with_abbreviations` **(Many-Argument Workhorses)** (Impact: 47.7)
    * *Intent:* /// Construct a new `Unit` from the given unit header and abbreviations. /// /// The abbreviations f...
  * `sections` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /// Return the section contributions of a unit. /// /// This function should only be needed by low l...
  * `die_ranges` **(Defensive Guards)** (Impact: 24.1)
    * *Intent:* /// Return an iterator for the address ranges of a `DebuggingInformationEntry`. /// /// This uses `D...
  * `load` **(Compute Cores)** (Impact: 23.8)
    * *Intent:* /// Try to load the DWARF sections using the given loader function. /// /// `section` loads a DWARF ...
  * `lookup_offset_id` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* /// Call `Reader::lookup_offset_id` for each section, and return the first match. /// /// The first ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 243`, `args: 118`, `func_start: 96`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 37`, `planned_debt: 9`
* *Architecture:* `api: 163`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 26`, `doc: 446`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.101
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.040854
  * `Imports (Out-Degree: 16):` alloc::string::String, alloc::sync::Arc, crate::DebugMacroOffset, crate::Endianity, crate::LittleEndian, crate::common::DebugAddrBase, crate::common::DebugAddrIndex, crate::common::DebugInfoOffset...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/find-msvc-tools-0.1.9/src/find_tools.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.289)
- **Top Global Matches:** file_cluster_0: 7.289, file_cluster_16: 8.461, file_cluster_12: 8.562
- **Magnitude:** 680.48 | **LOC:** 1607 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **38**; blast radius 0.824; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 71.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vs15plus_vc_read_version` **(Compute Cores)** (Impact: 34.0)
  * `vs15plus_vc_paths` **(Many-Argument Workhorses)** (Impact: 25.0)
  * `has_msbuild_version` **(Stateful Encapsulated Methods)** (Impact: 18.9)
  * `find_tool_in_vs15_path` **(Many-Argument Workhorses)** (Impact: 17.9)
    * *Intent:* // While the paths to Visual Studio 2017's devenv and MSBuild could // potentially be retrieved from...
  * `tool_from_vs15plus_instance` **(Many-Argument Workhorses)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 269`, `args: 157`, `func_start: 80`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 54`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 34`, `import: 28`
* *Defense:* `safety: 23`, `doc: 88`, `test: 12`, `sync_locks: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.824
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001848
  * `Imports (Out-Degree: 6):` crate::Tool, crate::com, crate::find_tools::StdEnvGetter, crate::find_tools::find, crate::registry::LOCAL_MACHINE, crate::registry::RegistryKey, crate::setup_config::SetupConfiguration, crate::vs_instances::VsInstances...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/cfi.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.975)
- **Top Global Matches:** file_cluster_6: 6.975, file_cluster_4: 10.485, file_cluster_8: 16.102
- **Magnitude:** 608.72 | **LOC:** 1071 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **29**; blast radius 1.106; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.8%)
- **Documentation Coverage:** 31.5789% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Many-Argument Workhorses)** (Impact: 169.0)
  * `write` **(Many-Argument Workhorses)** (Impact: 103.0)
    * *Intent:* /// Returns the section offset of the CIE.
  * `write` **(Many-Argument Workhorses)** (Impact: 57.4)
  * `write_advance_loc` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `from` **(Many-Argument Workhorses)** (Impact: 25.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 201`, `args: 30`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 24`, `planned_debt: 3`
* *Architecture:* `api: 23`, `import: 15`
* *Defense:* `safety: 15`, `doc: 75`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.106
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.027933
  * `Imports (Out-Degree: 10):` alloc::vec::Vec, crate::LittleEndian, crate::Vendor, crate::arch::X86_64, crate::common::DebugFrameOffset, crate::common::EhFrameOffset, crate::common::Encoding, crate::common::Format...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/portable-atomic-util-0.2.6/src/arc.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.727)
- **Top Global Matches:** file_cluster_0: 6.727, file_cluster_13: 9.866, file_cluster_5: 10.368
- **Magnitude:** 516.24 | **LOC:** 3411 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **47**; blast radius 1.991; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (53.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.0%), Debt Markers (formerly Tech Debt) (38.4%)
- **Documentation Coverage:** 36.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_mut` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* /// ``` /// use portable_atomic_util::Arc; /// /// let mut data = Arc::new(75); /// let weak = Arc::...
  * `alloc_impl` **(Many-Argument Workhorses)** (Impact: 9.2)
  * `downgrade` **(Annotated & Test Methods)** (Impact: 8.9)
    * *Intent:* /// Creates a new [`Weak`] pointer to this allocation. /// /// # Examples /// /// ``` /// use portab...
  * `upgrade` **(Annotated & Test Methods)** (Impact: 8.5)
    * *Intent:* /// /// let five = Arc::new(5); /// /// let weak_five = Arc::downgrade(&five); /// /// let strong_fi...
  * `weak_count` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /// Gets an approximation of the number of `Weak` pointers pointing to this /// allocation. /// /// ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 351`, `args: 151`, `func_start: 136`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 7`, `state_mutation: 17`, `dead_code: 28`, `planned_debt: 20`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 59`, `concurrency: 22`, `import: 24`
* *Defense:* `safety: 7`, `doc: 1413`, `test: 6`, `sync_locks: 14`, `immutability_locks: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.991
  * `Choke Point (Betweenness):` 0.000308 | `Ripple Effect (Closeness):` 0.005545
  * `Imports (Out-Degree: 2):` alloc::alloc::handle_alloc_error, alloc::borrow::Cow, alloc::borrow::ToOwned, alloc::boxed::Box, alloc::string::String, alloc::vec::Vec, core::alloc::Layout, core::any::Any...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/value.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.758)
- **Top Global Matches:** file_cluster_0: 8.758, file_cluster_13: 8.842, file_cluster_15: 8.894
- **Magnitude:** 492.86 | **LOC:** 1622 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 1.146; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (61.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.6%)
- **Documentation Coverage:** 43.1193% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shra` **(Many-Argument Workhorses)** (Impact: 49.0)
    * *Intent:* /// Perform an arithmetic shift right operation. /// /// This operation requires a signed integral t...
  * `shl` **(Compute Cores)** (Impact: 43.0)
    * *Intent:* /// Perform a shift left operation. /// /// This operation requires integral types. /// If the shift...
  * `shr` **(Compute Cores)** (Impact: 27.1)
    * *Intent:* /// Perform a logical shift right operation. /// /// This operation requires an unsigned integral ty...
  * `parse` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* /// Read a `Value` with the given `value_type` from a `Reader`.
  * `from_entry` **(Defensive Guards)** (Impact: 16.1)
    * *Intent:* /// Construct a `ValueType` from a base type DIE.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 128`, `args: 63`, `func_start: 57`, `class_start: 2`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 1`
* *Architecture:* `api: 54`, `import: 7`
* *Defense:* `safety: 4`, `doc: 192`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.146
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.040854
  * `Imports (Out-Degree: 8):` crate::common::DebugAbbrevOffset, crate::common::DebugInfoOffset, crate::common::Encoding, crate::common::Format, crate::constants, crate::endianity::LittleEndian, crate::read::Abbreviation, crate::read::AttributeSpecification...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/bytes-1.11.1/src/bytes_mut.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.482)
- **Top Global Matches:** file_cluster_0: 7.482, file_cluster_15: 9.615, file_cluster_13: 9.724
- **Magnitude:** 476.14 | **LOC:** 1942 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **32**; blast radius 5.679; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (90.1%), Connectivity (formerly Api Exposure) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.0%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reserve_inner` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* // In separate function to allow the short-circuits in `reserve` and `try_reclaim` to // be inline-a...
  * `put` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* // Specialize these methods so they can skip checking `remaining_mut` // and `advance_mut`.
  * `try_unsplit` **(Compute Cores)** (Impact: 13.1)
  * `test_original_capacity_to_repr` **(Annotated & Test Methods)** (Impact: 11.7)
  * `advance_unchecked` **(Stateful Encapsulated Methods)** (Impact: 10.5)
    * *Intent:* /// Advance the buffer without bounds checking. /// /// # SAFETY /// /// The caller must ensure that...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 285`, `args: 113`, `func_start: 109`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 35`, `planned_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 36`, `concurrency: 4`, `import: 15`
* *Defense:* `safety: 5`, `doc: 521`, `test: 40`, `sync_locks: 2`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.679
  * `Choke Point (Betweenness):` 0.000338 | `Ripple Effect (Closeness):` 0.031044
  * `Imports (Out-Degree: 7):` alloc::borrow::Borrow, alloc::borrow::BorrowMut, alloc::boxed::Box, alloc::string::String, alloc::vec, alloc::vec::Vec, core::cmp, core::fmt...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/bytes-1.11.1/src/bytes.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.729)
- **Top Global Matches:** file_cluster_0: 6.729, file_cluster_12: 9.2, file_cluster_5: 9.231
- **Magnitude:** 406.56 | **LOC:** 1667 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **27**; blast radius 7.2; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (66.0%), Connectivity (formerly Api Exposure) (53.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.4%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `truncate` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* /// effect. /// /// The [split_off](`Self::split_off()`) method can emulate `truncate`, but this cau...
  * `slice` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* /// /// ``` /// use bytes::Bytes; /// /// let a = Bytes::from(&b"hello world"[..]); /// let b = a.sl...
  * `shallow_clone_vec` **(Many-Argument Workhorses)** (Impact: 8.4)
  * `promotable_to_mut` **(Many-Argument Workhorses)** (Impact: 8.1)
  * `promotable_to_vec` **(Many-Argument Workhorses)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 231`, `args: 123`, `func_start: 107`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 16`, `duplicate_logic: 12`
* *Architecture:* `api: 33`, `concurrency: 5`, `import: 13`
* *Defense:* `doc: 376`, `test: 22`, `sync_locks: 2`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.2
  * `Choke Point (Betweenness):` 0.000191 | `Ripple Effect (Closeness):` 0.031835
  * `Imports (Out-Degree: 4):` alloc::alloc::Layout, alloc::alloc::dealloc, alloc::borrow::Borrow, alloc::boxed::Box, alloc::string::String, alloc::vec::Vec, core::cmp, core::fmt...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/target-lexicon-0.13.5/src/targets.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.95)
- **Top Global Matches:** file_cluster_0: 7.95, file_cluster_15: 8.554, file_cluster_13: 9.017
- **Magnitude:** 382.14 | **LOC:** 2216 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **28**; blast radius 7.363; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (62.5%), Connectivity (formerly Api Exposure) (57.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 47.3684% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_str` **(Compute Cores)** (Impact: 43.4)
  * `from_str` **(Defensive Guards)** (Impact: 30.0)
  * `from_str` **(Compute Cores)** (Impact: 20.0)
  * `into_str` **(I/O & Config Routines)** (Impact: 8.6)
    * *Intent:* /// Convert into a string
  * `fmt` **(Defensive Guards)** (Impact: 8.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 195`, `args: 165`, `func_start: 62`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 6`, `planned_debt: 16`, `duplicate_logic: 12`
* *Architecture:* `api: 52`, `import: 45`
* *Defense:* `safety: 15`, `doc: 97`, `test: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.363
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01183
  * `Imports (Out-Degree: 1):` Aarch64Architecture::*, Architecture::*, ArmArchitecture::*, BinaryFormat::*, CleverArchitecture::*, Environment::*, Mips32Architecture::*, Mips64Architecture::*...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/abbrev.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.652)
- **Top Global Matches:** file_cluster_5: 5.652, file_cluster_12: 7.992, file_cluster_7: 9.126
- **Magnitude:** 375.36 | **LOC:** 1099 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **26**; blast radius 1.424; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (63.8%), Mutation Surface (formerly State Flux) (58.9%), Guard Balance (formerly Safety Score) (58.3%)
- **Documentation Coverage:** 58.0357% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `populate` **(Many-Argument Workhorses)** (Impact: 17.8)
    * *Intent:* /// Parse abbreviations and store them in the cache. /// /// This will iterate over the given units ...
  * `insert` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* /// Insert an abbreviation into the set. /// /// Returns `Ok` if it is the first abbreviation in the...
  * `parse` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* /// Parse an attribute specification. Returns `None` for the null attribute /// specification, `Some...
  * `parse` **(Generic / Templated Code)** (Impact: 10.8)
    * *Intent:* /// Parse an abbreviation. Return `None` for the null abbreviation, `Some` /// for an actual abbrevi...
  * `get_attribute_size` **(State Mutators)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 198`, `args: 89`, `func_start: 70`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 7`, `state_mutation: 38`
* *Architecture:* `api: 51`, `import: 18`
* *Defense:* `safety: 7`, `doc: 96`, `test: 52`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.424
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.041418
  * `Imports (Out-Degree: 8):` alloc::collections::btree_map, alloc::sync::Arc, alloc::vec::Vec, core::convert::TryFrom, core::fmt, core::fmt::Debug, core::iter::FromIterator, core::ops::Deref...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/test/test_numpy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.116)
- **Top Global Matches:** file_cluster_15: 7.116, file_cluster_11: 8.438, file_cluster_13: 8.685
- **Magnitude:** 374.78 | **LOC:** 1155 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.714; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (34.9%), Connectivity (formerly Api Exposure) (13.3%), Complexity Load (formerly Cognitive Load) (3.3%)
- **Documentation Coverage:** 98.1735% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_numpy_array_dimension_zero` **(Compute Cores)** (Impact: 4.5)
  * `test_numpy_array_dimension_max` **(I/O & Config Routines)** (Impact: 3.7)
  * `test_numpy_array_dimension_zero` **(Defensive Guards)** (Impact: 3.3)
  * `test_numpy_repeated` **(Defensive Guards)** (Impact: 3.3)
  * `numpy_default` **(Defensive Guards)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 242`, `args: 110`, `func_start: 110`, `class_start: 3`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 106`
* *Architecture:* `io: 1`, `api: 112`, `import: 4`
* *Defense:* `safety: 117`, `doc: 2`, `test: 121`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .util, orjson, pytest, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/bytes-1.11.1/src/buf/buf_impl.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.253)
- **Top Global Matches:** file_cluster_13: 7.253, file_cluster_15: 7.548, file_cluster_0: 8.111
- **Magnitude:** 373.7 | **LOC:** 2963 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **13**; blast radius 13.632; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (28.3%), Connectivity (formerly Api Exposure) (19.7%)
- **Documentation Coverage:** 51.6484% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chunks_vectored` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* /// /// This is a lower level function. Most operations are done with other /// functions. /// /// #...
  * `try_copy_to_slice` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* /// assert_eq!(Ok(()), buf.try_copy_to_slice(&mut dst)); /// assert_eq!(&b"hello"[..], &dst); /// as...
  * `get_uint_ne` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* /// ``` /// use bytes::Buf; /// /// let mut buf: &[u8] = match cfg!(target_endian = "big") { /// tru...
  * `get_int_ne` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* /// ``` /// use bytes::Buf; /// /// let mut buf: &[u8] = match cfg!(target_endian = "big") { /// tru...
  * `try_get_uint_ne` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* /// ``` /// use bytes::{Buf, TryGetError}; /// /// let mut buf: &[u8] = match cfg!(target_endian = "...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 226`, `args: 188`, `func_start: 180`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 2`, `api: 3`, `import: 7`
* *Defense:* `safety: 7`, `doc: 1918`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.632
  * `Choke Point (Betweenness):` 0.000776 | `Ripple Effect (Closeness):` 0.033545
  * `Imports (Out-Degree: 5):` alloc::boxed::Box, crate::TryGetError, crate::buf::Chain, crate::buf::Reader, crate::buf::Take, crate::buf::reader, crate::buf::take, crate::min_u64_usize...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/loclists.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.948)
- **Top Global Matches:** file_cluster_5: 7.948, file_cluster_0: 8.209, file_cluster_12: 9.093
- **Magnitude:** 371.2 | **LOC:** 1127 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **33**; blast radius 1.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.1%), Connectivity (formerly Api Exposure) (51.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 67.2)
    * *Intent:* /// Parse a location list entry from `.debug_loclists`
  * `convert_raw` **(Many-Argument Workhorses)** (Impact: 19.3)
    * *Intent:* /// Convert a raw location into a location, and update the state of the iterator. /// /// The raw lo...
  * `parse_data` **(Generic / Templated Code)** (Impact: 14.4)
  * `test_loclists` **(I/O & Config Routines)** (Impact: 11.7)
  * `get_offset` **(Generic / Templated Code)** (Impact: 9.7)
    * *Intent:* /// Returns the `.debug_loclists` offset at the given `base` and `index`. /// /// The `base` must be...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 177`, `args: 40`, `func_start: 35`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 80`, `duplicate_logic: 4`
* *Architecture:* `api: 33`, `import: 12`
* *Defense:* `safety: 1`, `doc: 144`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.119
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.040854
  * `Imports (Out-Degree: 11):` alloc::vec::Vec, crate::common::DebugAddrBase, crate::common::DebugAddrIndex, crate::common::DebugLocListsBase, crate::common::DebugLocListsIndex, crate::common::DwarfFileType, crate::common::Encoding, crate::common::Format...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `orjson-3.11.8/src/serialize/writer/json.rs` (RUST) | Magnitude: 196.0 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 447, generics: 93, structural_boundaries: 91, args: 71
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/objimpl.rs` (RUST) | Magnitude: 64.42 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 59, indent_spaces: 54, structural_boundaries: 41, decorators: 30
- `orjson-3.11.8/include/cargo/unwinding-0.2.8/src/unwinder/find_fde/gnu_eh_frame_hdr.rs` (RUST) | Magnitude: 17.74 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 19, core_var_decl: 8, design_snake_case: 8
- `orjson-3.11.8/include/cargo/itoap-1.0.1/src/lib.rs` (RUST) | Magnitude: 82.78 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 221, structural_boundaries: 94, doc: 85, decorators: 45
- `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/value.rs` (RUST) | Magnitude: 492.86 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1310, doc: 192, branch: 149, structural_boundaries: 128

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `orjson-3.11.8/include/cargo/unwinding-0.2.8/src/unwinder/arch/riscv32.rs` (RUST) | Magnitude: 32.72 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 212, structural_boundaries: 18, decorators: 10, api: 8
- `orjson-3.11.8/include/cargo/unwinding-0.2.8/src/unwinder/arch/aarch64.rs` (RUST) | Magnitude: 29.74 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 20, branch: 11, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `orjson-3.11.8/include/cargo/unwinding-0.2.8/src/arch.rs` (RUST) | Magnitude: 41.28 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 41, api: 24, structural_boundaries: 20, core_var_decl: 17
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/context.rs` (RUST) | Magnitude: 34.8 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: pointers: 34, structural_boundaries: 26, indent_spaces: 19, api: 15
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/mod.rs` (RUST) | Magnitude: 46.54 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 474, core_var_decl: 97, design_snake_case: 97, decorators: 54
- `orjson-3.11.8/src/alloc.rs` (RUST) | Magnitude: 13.3 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 13, pointers: 8, decorators: 5
- `orjson-3.11.8/include/cargo/unwinding-0.2.8/src/unwinder/arch/riscv64.rs` (RUST) | Magnitude: 32.8 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 216, structural_boundaries: 19, decorators: 12, api: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `orjson-3.11.8/test/test_escape.py` (PYTHON) | Magnitude: 64.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 61, indent_spaces: 33, args: 30, func_start: 30
- `orjson-3.11.8/test/test_canonical.py` (PYTHON) | Magnitude: 9.42 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, api: 4, args: 3
- `orjson-3.11.8/build.rs` (RUST) | Magnitude: 19.32 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 72, debug_prints: 30, branch: 11, decorators: 5
- `orjson-3.11.8/test/test_typeddict.py` (PYTHON) | Magnitude: 6.24 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, safety: 3, api: 3
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/cpython/longobject.rs` (RUST) | Magnitude: 27.6 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, pointers: 18, structural_boundaries: 15, decorators: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/core_atomic.rs` (RUST) | Magnitude: 132.32 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 429, decorators: 100, structural_boundaries: 61, pointers: 57

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `orjson-3.11.8/src/serialize/per_type/mod.rs` (RUST) | Magnitude: 29.56 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 28, api: 14, import: 14, encapsulation: 14
- `orjson-3.11.8/src/serialize/mod.rs` (RUST) | Magnitude: 19.22 | Delta: **0.17** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, api: 4, encapsulation: 4, import: 2
- `orjson-3.11.8/src/serialize/writer/mod.rs` (RUST) | Magnitude: 22.38 | Delta: **0.179** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, api: 7, import: 7, encapsulation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/atomic128/mod.rs` (RUST) | Magnitude: 22.2 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, core_var_decl: 28, design_snake_case: 28, decorators: 9
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/gen/utils.rs` (RUST) | Magnitude: 22.56 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, core_var_decl: 64, design_snake_case: 58, decorators: 14
- `orjson-3.11.8/test/test_fake.py` (PYTHON) | Magnitude: 24.42 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, core_var_decl: 10, state_mutation: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `orjson-3.11.8/include/cargo/simdutf8-0.1.5/src/implementation/algorithm.rs` (RUST) | Magnitude: 199.28 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 498, structural_boundaries: 85, decorators: 58, core_var_decl: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `orjson-3.11.8/include/cargo/portable-atomic-util-0.2.6/tests/arc.rs` (RUST) | Magnitude: 209.58 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 586, structural_boundaries: 220, test: 196, core_var_decl: 117
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/tests/mod.rs` (RUST) | Magnitude: 77.62 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 340, test: 89, decorators: 50, core_var_decl: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `orjson-3.11.8/test/test_circular.py` (PYTHON) | Magnitude: 35.36 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 17, test: 15, state_mutation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/build.rs` (RUST) | Magnitude: 72.88 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 187, branch: 33, structural_boundaries: 24, core_var_decl: 22

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `orjson-3.11.8/src/typeref.rs` -> **Severity: 0.695** (Bridge: 0.0082 * Flux: 84.7115%)
- `orjson-3.11.8/include/cargo/once_cell-1.21.4/src/race.rs` -> **Severity: 0.602** (Bridge: 0.0078 * Flux: 77.6018%)
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/lib.rs` -> **Severity: 0.213** (Bridge: 0.0096 * Flux: 22.117%)
- `orjson-3.11.8/src/serialize/writer/byteswriter.rs` -> **Severity: 0.099** (Bridge: 0.0026 * Flux: 37.866%)
- `orjson-3.11.8/src/ffi/pystrref/pyunicode_new.rs` -> **Severity: 0.082** (Bridge: 0.0008 * Flux: 96.7906%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/object.rs` -> **Severity: 9.281** (Embedded: 0.1865 * Error Risk: 49.7537%)
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/refcount.rs` -> **Severity: 6.306** (Embedded: 0.1237 * Error Risk: 50.9676%)
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/sliceobject.rs` -> **Severity: 4.958** (Embedded: 0.094 * Error Risk: 52.7495%)
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/pyerrors.rs` -> **Severity: 4.953** (Embedded: 0.0988 * Error Risk: 50.1359%)
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/sysmodule.rs` -> **Severity: 4.901** (Embedded: 0.094 * Error Risk: 52.1415%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/object.rs` -> **Severity: 5883.581** (Blast Radius: 59.653 * Doc Risk: 98.6301%)
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/cpython/object.rs` -> **Severity: 1653.8** (Blast Radius: 16.538 * Doc Risk: 100.0%)
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/utils.rs` -> **Severity: 1343.233** (Blast Radius: 14.008 * Doc Risk: 95.8904%)
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/refcount.rs` -> **Severity: 1334.1** (Blast Radius: 13.341 * Doc Risk: 100.0%)
- `orjson-3.11.8/include/cargo/simdutf8-0.1.5/src/implementation/helpers.rs` -> **Severity: 741.7** (Blast Radius: 7.417 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 184 literal sites + 7 sites through wrappers = 191
- **`panics_and_aborts`:** 228 literal sites + 25 sites through wrappers = 253

- `panic_advance` (function, panics_and_aborts, primitive): 17 call sites in 2 files -- `orjson-3.11.8/include/cargo/bytes-1.11.1/src/lib.rs`
- `panic_does_not_fit` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `orjson-3.11.8/include/cargo/bytes-1.11.1/src/lib.rs`
- `not_supported` (function, debug_prints, primitive): 3 call sites in 1 files -- `orjson-3.11.8/build.rs`
- `not_supported` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `orjson-3.11.8/build.rs`
- `foreign_exception` (function, debug_prints, primitive): 2 call sites in 1 files -- `orjson-3.11.8/include/cargo/unwinding-0.2.8/src/panic_handler.rs`
- `drop_panic` (function, debug_prints, primitive): 1 call sites in 1 files -- `orjson-3.11.8/include/cargo/unwinding-0.2.8/src/panic_handler.rs`
- `print_config_and_exit` (function, debug_prints, primitive): 1 call sites in 1 files -- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/build.rs`
- `print_config_and_exit` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/build.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 23834 call pairs -- scoped 25.0%, unique 0.0%, ambiguous 19.2%, external 55.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 21762 | 23.7% | 0.0% | 21.0% | 55.3% |
| python | 2063 | 39.5% | 0.0% | 0.0% | 60.5% |
| shell | 9 | 0.0% | 0.0% | 0.0% | 100.0% |

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
