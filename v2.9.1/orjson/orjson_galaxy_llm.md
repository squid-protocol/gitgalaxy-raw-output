# ARCHITECTURAL_BRIEF: orjson
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
- **Scope:** 467 analyzed artifact(s), 106565 LOC.
- **Load-bearing artifact:** `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/detect/README.md` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `orjson-3.11.8/src/ffi/mod.rs` -- pulls in 183 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `orjson-3.11.8/include/yyjson/yyjson.c` at magnitude 9182.48 (structural weight, not risk).
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
| Total Artifacts | 576 |
| Analyzed Artifacts (Scanned) | 467 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 109 |
| Total LOC | 106565 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 81.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7653 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1192 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4062 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 402 | 94742 | 86.1% |
| MARKDOWN | 31 | 0 | 6.6% |
| PLAINTEXT | 23 | 0 | 4.9% |
| SHELL | 4 | 26 | 0.9% |
| C | 2 | 11268 | 0.4% |
| PYTHON | 2 | 52 | 0.4% |
| YAML | 1 | 14 | 0.2% |
| JSON | 1 | 398 | 0.2% |
| CSS | 1 | 65 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `1.587`
> **Composition Archetype:** `Mid Flat Project` (z +1.59; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 16%, State Mutators Files 14%, Data / Markup / Trivial 14%, Parameter Forwarders Files 14%, Generic / Templated Code Files 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 413 | 88.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 54 | 11.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 109*

**Composition by Extension & Reason:**
- `.json`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 21x Excluded (Unsupported Extension: '.toml')
- `.rs`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.orig`: 14x Excluded (Unsupported Extension: '.orig')
- `.lock`: 13x Excluded (Unsupported Extension: '.lock')
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.0`: 1x Excluded (Unsupported Extension: '.0')
- `.apache2`: 1x Excluded (Unsupported Extension: '.Apache2')
- `.mit`: 1x Excluded (Unsupported Extension: '.MIT')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.6 | 9.5 | 6.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 28.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 41.6 | 24.4 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.7 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 91.4 | 15.3 | 8.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 15181 | 359 | 64 | `orjson-3.11.8/include/yyjson/yyjson.h` |
| cleanup | 111 | 17 | 0 | `orjson-3.11.8/include/yyjson/yyjson.c` |
| guards | 3685 | 315 | 16 | `orjson-3.11.8/include/yyjson/yyjson.h` |
| danger | 2026 | 131 | 8 | `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/cfi.rs` |
| concurrency | 515 | 94 | 2 | `orjson-3.11.8/include/cargo/portable-atomic-util-0.2.6/src/arc.rs` |
| connectivity | 7171 | 363 | 32 | `orjson-3.11.8/include/yyjson/yyjson.h` |
| io | 47 | 21 | 0 | `orjson-3.11.8/include/cargo/bytes-1.11.1/tests/test_take.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 6 | 6 | 0 | `orjson-3.11.8/include/cargo/find-msvc-tools-0.1.9/src/find_tools.rs` |
| time | 6 | 6 | 0 | `orjson-3.11.8/include/cargo/bytecount-0.6.9/benches/bench.rs` |
| serialization | 0 | 0 | 0 | - |
| regex | 2 | 1 | 0 | `orjson-3.11.8/include/cargo/once_cell-1.21.4/examples/regex.rs` |
| events | 7 | 3 | 0 | `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/detect/auxv.rs` |
| tests | 4273 | 169 | 20 | `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/tests/helper.rs` |
| docs | 14470 | 134 | 52 | `orjson-3.11.8/include/cargo/bytes-1.11.1/src/buf/buf_impl.rs` |
| debt | 505 | 101 | 2 | `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/tests/helper.rs` |
| mutation | 19886 | 349 | 70 | `orjson-3.11.8/include/yyjson/yyjson.c` |
| dead_code | 3743 | 280 | 17 | `orjson-3.11.8/include/cargo/bytes-1.11.1/src/buf/buf_impl.rs` |
| credential | 3 | 2 | 0 | `orjson-3.11.8/include/cargo/simdutf8-0.1.5/tests/tests.rs` |
| threat | 876 | 93 | 2 | `orjson-3.11.8/include/yyjson/yyjson.c` |
| ml_ai | 195 | 24 | 0 | `orjson-3.11.8/include/yyjson/yyjson.c` |
| ui | 1 | 1 | 0 | `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/rustdoc.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `orjson-3.11.8/include/cargo/bytes-1.11.1/tests/test_take.rs` (Hits: 6)
- `orjson-3.11.8/include/yyjson/yyjson.c` (Hits: 6)
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/detect/auxv.rs` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/detect/README.md`) — 2 inbound connections
2. **lookup.rs** (`orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/lookup.rs`) — 2 inbound connections
3. **wasm32-development.md** (`orjson-3.11.8/include/cargo/simdutf8-0.1.5/wasm32-development.md`) — 1 inbound connections
4. **iter.rs** (`orjson-3.11.8/include/cargo/bytes-1.11.1/src/buf/iter.rs`) — 1 inbound connections
5. **constants.rs** (`orjson-3.11.8/include/cargo/gimli-0.32.3/src/constants.rs`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`orjson-3.11.8/src/ffi/mod.rs`) — 183 outbound dependencies
2. **dwarf.rs** (`orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/dwarf.rs`) — 78 outbound dependencies
3. **cfi.rs** (`orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/cfi.rs`) — 69 outbound dependencies
4. **arc.rs** (`orjson-3.11.8/include/cargo/portable-atomic-util-0.2.6/src/arc.rs`) — 69 outbound dependencies
5. **unit.rs** (`orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/unit.rs`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `write` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/op.rs`) -> Impact: **358.7** | LOC: 242
- `read_root_pretty` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/yyjson/yyjson.c`) -> Impact: **299.2** | LOC: 399
  * *Intent:* /** Read JSON document (accept all style, but optimized for pretty). */
- `read_root_minify` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/yyjson/yyjson.c`) -> Impact: **246.1** | LOC: 365
  * *Intent:* /** Read JSON document (accept all style, but optimized for minify). */
- `read_number` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/yyjson/yyjson.c`) -> Impact: **236.8** | LOC: 576
  * *Intent:* */
- `write` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/line.rs`) -> Impact: **215.7** | LOC: 198
  * *Intent:* /// Write the line number program to the given section. /// /// # Panics /// /// Panics if `self.is_none()`.
- `write` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/unit.rs`) -> Impact: **212.8** | LOC: 237
  * *Intent:* /// Write the attribute value to the given sections.
- `evaluate_one_operation` **(Compute Cores)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/op.rs`) -> Impact: **191.0** | LOC: 370
- `unsafe_yyjson_mut_ptr_putx` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/yyjson/yyjson.c`) -> Impact: **177.7** | LOC: 138
- `write` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/cfi.rs`) -> Impact: **169.0** | LOC: 116
- `write_string` **(Many-Argument Workhorses)** (@ `orjson-3.11.8/include/yyjson/yyjson.c`) -> Impact: **151.8** | LOC: 285
  * *Intent:* */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `orjson-3.11.8/include/yyjson` | 2 | 12713.36 | 49.11% | 7.15% |
| `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read` | 24 | 9150.5 | 7.15% | 62.81% |
| `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write` | 14 | 4356.04 | 7.06% | 23.72% |
| `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src` | 57 | 3490.86 | 1.48% | 76.4% |
| `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/cpython` | 33 | 1832.86 | 1.5% | 77.15% |
| `orjson-3.11.8/include/cargo/gimli-0.32.3/src` | 6 | 1509.64 | 16.8% | 18.57% |
| `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/tests` | 2 | 1151.46 | 12.81% | 0.0% |
| `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/atomic128` | 9 | 1075.66 | 13.52% | 17.52% |
| `orjson-3.11.8/include/cargo/find-msvc-tools-0.1.9/src` | 9 | 1034.02 | 6.19% | 43.65% |
| `orjson-3.11.8/include/cargo/bytes-1.11.1/src` | 4 | 916.9 | 9.96% | 66.35% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/abstract_.rs` -> **100.0%** Exposure
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/bytesobject.rs` -> **100.0%** Exposure
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/ceval.rs` -> **100.0%** Exposure
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/codecs.rs` -> **100.0%** Exposure
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/context.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `orjson-3.11.8/include/cargo/bytecount-0.6.9/src/simd/generic.rs` -> **100.0%** Exposure
- `orjson-3.11.8/include/cargo/gimli-0.32.3/src/arch.rs` -> **100.0%** Exposure
- `orjson-3.11.8/src/serialize/writer/str/avx512.rs` -> **100.0%** Exposure
- `orjson-3.11.8/src/serialize/writer/str/generic.rs` -> **100.0%** Exposure
- `orjson-3.11.8/src/serialize/writer/str/sse2.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/cfi.rs` -> **147** Orphaned Functions | **23** Duplicates
- `orjson-3.11.8/include/cargo/bytes-1.11.1/tests/test_bytes.rs` -> **110** Orphaned Functions | **0** Duplicates
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/abstract_.rs` -> **88** Orphaned Functions | **0** Duplicates
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/unicodeobject.rs` -> **82** Orphaned Functions | **0** Duplicates
- `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/pyerrors.rs` -> **64** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `3790` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `orjson-3.11.8/include/yyjson/yyjson.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9182.48 | **LOC:** 9290 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 2.088; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.0%)
- **Documentation Coverage:** 27.4126% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_root_pretty` **(Many-Argument Workhorses)** (Impact: 299.2)
    * *Intent:* /** Read JSON document (accept all style, but optimized for pretty). */
  * `read_root_minify` **(Many-Argument Workhorses)** (Impact: 246.1)
    * *Intent:* /** Read JSON document (accept all style, but optimized for minify). */
  * `read_number` **(Many-Argument Workhorses)** (Impact: 236.8)
    * *Intent:* */
  * `unsafe_yyjson_mut_ptr_putx` **(Many-Argument Workhorses)** (Impact: 177.7)
  * `write_string` **(Many-Argument Workhorses)** (Impact: 151.8)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 40 instances
* *Amplified Cascading Flux:* 1532 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 4809
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1707`, `structural_boundaries: 1061`, `args: 374`, `func_start: 199`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 172`, `state_mutation: 1745`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `io: 6`, `api: 209`, `import: 7`
* *Defense:* `safety: 11`, `doc: 142`, `immutability_locks: 275`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` endian.h, intrin.h, endian.h, math.h, endian.h, types.h, yyjson.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/yyjson/yyjson.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3530.88 | **LOC:** 7925 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.863; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.9%), Guard Balance (formerly Safety Score) (68.1%)
- **Documentation Coverage:** 92.4242% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `yyjson_mut_doc_ptr_setx` **(Many-Argument Workhorses)** (Impact: 42.0)
  * `yyjson_mut_doc_ptr_addx` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `yyjson_ptr_ctx_append` **(Many-Argument Workhorses)** (Impact: 36.6)
  * `yyjson_mut_doc_ptr_replacex` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `yyjson_mut_ptr_setx` **(Many-Argument Workhorses)** (Impact: 25.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 295 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 949
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 719`, `structural_boundaries: 1216`, `args: 744`, `func_start: 329`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 359`
* *Architecture:* `api: 660`, `import: 8`
* *Defense:* `safety: 289`, `doc: 504`, `immutability_locks: 402`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002146
  * `Imports (Out-Degree: 0):` float.h, limits.h, stdbool.h, stddef.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/cfi.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1650.52 | **LOC:** 7952 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **69**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (94.2%), Guard Balance (formerly Safety Score) (50.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (17.8%)
- **Documentation Coverage:** 57.8947% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 110.8)
  * `evaluate` **(Many-Argument Workhorses)** (Impact: 54.5)
    * *Intent:* /// Evaluate one call frame instruction. Return `Ok(true)` if the row is /// complete, `Ok(false)` o...
  * `parse_rest` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `parse` **(Many-Argument Workhorses)** (Impact: 39.9)
  * `parse_encoded_pointer` **(Many-Argument Workhorses)** (Impact: 28.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 28 instances
* *High Risk Execution (weighted view):* 8
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 1715`, `args: 373`, `func_start: 325`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 170`, `high_risk_execution: 10`, `state_mutation: 76`, `dead_code: 42`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 23`, `unreferenced_by_name: 147`
* *Architecture:* `api: 108`, `import: 32`
* *Defense:* `safety: 30`, `doc: 975`, `test: 418`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ArrayVec, AugmentationData, Debug, DwEhPe, EhFrame, EhFrameOffset, Encoding, EndianSlice...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/unit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1447.92 | **LOC:** 6129 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **59**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (75.8%), Guard Balance (formerly Safety Score) (57.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (26.4%)
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
* *Risk/State:* `safety_bypasses: 123`, `high_risk_execution: 24`, `state_mutation: 65`, `dead_code: 61`, `planned_debt: 19`, `duplicate_logic: 2`
* *Architecture:* `api: 200`, `import: 18`
* *Defense:* `safety: 35`, `doc: 862`, `test: 232`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Abbreviations, AttributeSpecification, DebugAbbrev, DebugAddrBase, DebugAddrIndex, DebugInfo, DebugInfoOffset, DebugLineOffset...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/op.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1254.22 | **LOC:** 4183 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 47.5728% of unit weight undocumented
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
* *Structure:* `branch: 334`, `structural_boundaries: 484`, `args: 173`, `func_start: 77`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 35`, `state_mutation: 143`, `dead_code: 21`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 36`
* *Architecture:* `api: 39`, `import: 41`
* *Defense:* `safety: 12`, `doc: 493`, `test: 49`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ArrayVec, DebugInfoOffset, Encoding, Error, EvaluationResult, Expression, Reader, ReaderOffset...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/tests/helper.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1073.84 | **LOC:** 3081 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.0%), Complexity Load (formerly Cognitive Load) (18.9%), Concurrency Surface (formerly Concurrency) (12.2%)
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
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 96`, `dead_code: 5`, `planned_debt: 49`, `fragile_debt: 5`, `unreferenced_by_name: 29`
* *Architecture:* `api: 25`, `concurrency: 13`, `import: 36`
* *Defense:* `safety: 12`, `test: 527`, `sync_locks: 18`, `immutability_locks: 24`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` *, Ordering, core::sync::atomic::Ordering, crabgrind::memcheck, crate::tests::helper, crate::tests::helper::catch_unwind_on_non_seqcst_arch, crate::tests::helper::catch_unwind_on_weak_memory_arch, crate::tests::helper::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/unit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1026.48 | **LOC:** 3108 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **62**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%), Connectivity (formerly Api Exposure) (61.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
* *Structure:* `branch: 249`, `structural_boundaries: 638`, `args: 101`, `func_start: 75`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 137`, `high_risk_execution: 14`, `state_mutation: 29`, `planned_debt: 7`
* *Architecture:* `api: 83`, `import: 19`
* *Defense:* `safety: 20`, `doc: 233`, `test: 159`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbbreviationTable, Address, AttributeSpecification, BaseId, ConvertError, ConvertResult, DebugInfoOffset, DebugLineOffset...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/line.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 974.42 | **LOC:** 3186 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (90.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.9%), Guard Balance (formerly Safety Score) (51.7%)
- **Documentation Coverage:** 34.4828% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 3`, `state_mutation: 103`, `dead_code: 22`, `planned_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 59`
* *Architecture:* `api: 89`, `import: 21`
* *Defense:* `safety: 6`, `doc: 429`, `test: 127`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DebugLineOffset, DebugLineStrOffset, DebugStrOffset, DebugStrOffsetsIndex, Encoding, EndianSlice, Error, Format...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/arch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 959.0 | **LOC:** 1119 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.7%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
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
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 909`, `unreferenced_by_name: 3`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 2`, `doc: 30`, `test: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::common::Register, std::collections::HashSet, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/line.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 942.0 | **LOC:** 2166 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 2`, `state_mutation: 117`, `planned_debt: 3`, `unreferenced_by_name: 8`
* *Architecture:* `api: 55`, `import: 16`
* *Defense:* `safety: 15`, `doc: 206`, `test: 61`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ConvertError, ConvertResult, DebugLineStrOffsets, DebugStrOffsets, DerefMut, Dwarf, Encoding, EndianVec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/op.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 802.8 | **LOC:** 1763 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (34.2%)
- **Documentation Coverage:** 10.4651% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 44`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 42`, `import: 17`
* *Defense:* `safety: 22`, `doc: 216`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ConvertResult, DebugInfoReference, DwOp, Dwarf, EndianVec, Error, Format, LineProgram...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/dwarf.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 692.88 | **LOC:** 1725 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **78**; blast radius 2.088; role: Isolated/Orphan
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
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 37`, `dead_code: 15`, `planned_debt: 9`
* *Architecture:* `api: 163`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 26`, `doc: 446`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbbreviationsCache, AbbreviationsCacheStrategy, AttributeValue, DebugAbbrev, DebugAddr, DebugAddrIndex, DebugAranges, DebugCuIndex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/find-msvc-tools-0.1.9/src/find_tools.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 686.58 | **LOC:** 1607 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 71.2963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vs15plus_vc_read_version` **(Compute Cores)** (Impact: 34.0)
  * `vs15plus_vc_paths` **(Many-Argument Workhorses)** (Impact: 25.0)
  * `has_msbuild_version` **(Stateful Encapsulated Methods)** (Impact: 18.9)
  * `find_tool_in_vs15_path` **(Many-Argument Workhorses)** (Impact: 17.9)
    * *Intent:* // While the paths to Visual Studio 2017's devenv and MSBuild could // potentially be retrieved from...
  * `find_vs_version` **(I/O & Config Routines)** (Impact: 17.4)
    * *Intent:* /// Find the most recent installed version of Visual Studio /// /// This is used by the cmake crate ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 269`, `args: 157`, `func_start: 80`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 54`, `dead_code: 4`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 4`, `api: 32`, `import: 28`
* *Defense:* `safety: 23`, `doc: 88`, `test: 12`, `sync_locks: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GetProcAddress, HMODULE, IMAGE_FILE_MACHINE_AMD64, LOCAL_MACHINE, LoadLibraryA, MACHINE_ATTRIBUTES, Ordering, OsString...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/write/cfi.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 606.72 | **LOC:** 1071 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.3%), Mutation Surface (formerly State Flux) (36.0%)
- **Documentation Coverage:** 27.7778% of unit weight undocumented
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
* *Structure:* `branch: 212`, `structural_boundaries: 201`, `args: 30`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 24`, `planned_debt: 3`, `unreferenced_by_name: 4`
* *Architecture:* `api: 21`, `import: 15`
* *Defense:* `safety: 15`, `doc: 75`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BaseId, ConvertResult, DerefMut, EhFrameOffset, Encoding, Error, Expression, Format...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/portable-atomic-util-0.2.6/src/arc.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 519.04 | **LOC:** 3411 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **69**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (99.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
* *Structure:* `branch: 117`, `structural_boundaries: 351`, `args: 151`, `func_start: 136`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 7`, `state_mutation: 17`, `dead_code: 275`, `planned_debt: 20`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 59`, `concurrency: 22`, `import: 24`
* *Defense:* `safety: 7`, `doc: 1413`, `test: 6`, `sync_locks: 14`, `immutability_locks: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Hasher, ManuallyDrop, MaybeUninit, NonNull, Ordering::Acquire, Relaxed, Release, ToOwned...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/value.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 492.86 | **LOC:** 1622 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (66.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.0%)
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
* *Risk/State:* `state_mutation: 2`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 54`, `import: 7`
* *Defense:* `safety: 4`, `doc: 192`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AttributeSpecification, DebugInfoOffset, DebuggingInformationEntry, Encoding, EndianSlice, Format, Reader, Result...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/bytes-1.11.1/src/bytes_mut.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 468.64 | **LOC:** 1942 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Test Surface (formerly Verification) (80.0%), Dead Code Surface (formerly Dead Code) (57.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 65.3846% of unit weight undocumented
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
* *Structure:* `branch: 140`, `structural_boundaries: 285`, `args: 113`, `func_start: 109`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 35`, `dead_code: 63`, `planned_debt: 1`, `duplicate_logic: 12`, `unreferenced_by_name: 19`
* *Architecture:* `api: 22`, `concurrency: 4`, `import: 15`
* *Defense:* `safety: 5`, `doc: 521`, `test: 40`, `sync_locks: 2`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicUsize, BorrowMut, BufMut, Bytes, DerefMut, ManuallyDrop, MaybeUninit, NonNull...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/bytes-1.11.1/src/bytes.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 410.16 | **LOC:** 1667 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (66.0%), Connectivity (formerly Api Exposure) (61.7%), Dead Code Surface (formerly Dead Code) (60.2%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `truncate` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* /// effect. /// /// The [split_off](`Self::split_off()`) method can emulate `truncate`, but this cau...
  * `slice` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* /// /// ``` /// use bytes::Bytes; /// /// let a = Bytes::from(&b"hello world"[..]); /// let b = a.sl...
  * `shallow_clone_vec` **(Many-Argument Workhorses)** (Impact: 8.4)
  * `split_off` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /// /// ``` /// use bytes::Bytes; /// /// let mut a = Bytes::from(&b"hello world"[..]); /// let b = ...
  * `split_to` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /// /// ``` /// use bytes::Bytes; /// /// let mut a = Bytes::from(&b"hello world"[..]); /// let b = ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 231`, `args: 123`, `func_start: 107`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 16`, `dead_code: 56`, `duplicate_logic: 12`
* *Architecture:* `api: 33`, `concurrency: 5`, `import: 13`
* *Defense:* `doc: 376`, `test: 22`, `sync_locks: 2`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicUsize, BytesMut, Layout, ManuallyDrop, Ordering, RangeBounds, alloc::
    alloc::dealloc, borrow::Borrow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/target-lexicon-0.13.5/src/targets.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 375.14 | **LOC:** 2216 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (77.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.6%)
- **Documentation Coverage:** 43.1818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_str` **(Compute Cores)** (Impact: 43.4)
  * `from_str` **(Defensive Guards)** (Impact: 30.0)
  * `from_str` **(Compute Cores)** (Impact: 20.0)
  * `into_str` **(I/O & Config Routines)** (Impact: 8.6)
    * *Intent:* /// Convert into a string
  * `fmt` **(Defensive Guards)** (Impact: 8.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 195`, `args: 165`, `func_start: 62`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 6`, `planned_debt: 16`, `duplicate_logic: 12`, `unreferenced_by_name: 9`
* *Architecture:* `api: 45`, `import: 45`
* *Defense:* `safety: 15`, `doc: 97`, `test: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Aarch64Architecture::*, Architecture::*, ArmArchitecture::*, BinaryFormat::*, CleverArchitecture::*, Environment::*, Hasher, Mips32Architecture::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/bytes-1.11.1/src/buf/buf_impl.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 371.7 | **LOC:** 2963 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (99.7%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (9.7%)
- **Documentation Coverage:** 51.6667% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 3`, `dead_code: 274`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 7`
* *Defense:* `safety: 7`, `doc: 1918`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Buf, BufMut, Chain, Reader, Take, TryGetError, alloc::boxed::Box, bytes::Buf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/loclists.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 370.2 | **LOC:** 1127 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 26.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 67.2)
    * *Intent:* /// Parse a location list entry from `.debug_loclists`
  * `convert_raw` **(Many-Argument Workhorses)** (Impact: 19.3)
    * *Intent:* /// Convert a raw location into a location, and update the state of the iterator. /// /// The raw lo...
  * `parse_data` **(Generic / Templated Code)** (Impact: 14.4)
  * `test_loclists` **(I/O & Config Routines)** (Impact: 13.7)
  * `test_location_list` **(I/O & Config Routines)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 177`, `args: 40`, `func_start: 35`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 80`, `dead_code: 6`, `duplicate_logic: 4`, `unreferenced_by_name: 8`
* *Architecture:* `api: 28`, `import: 12`
* *Defense:* `safety: 1`, `doc: 144`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DebugAddr, DebugAddrIndex, DebugLocListsBase, DebugLocListsIndex, DwarfFileType, Encoding, EndianSlice, Error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/abbrev.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 352.36 | **LOC:** 1099 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.2%), Debt Markers (formerly Tech Debt) (65.2%), Mutation Surface (formerly State Flux) (58.9%)
- **Documentation Coverage:** 47.191% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 7`, `state_mutation: 38`, `dead_code: 3`, `unreferenced_by_name: 27`
* *Architecture:* `api: 28`, `import: 18`
* *Defense:* `safety: 7`, `doc: 96`, `test: 52`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Debug, Encoding, EndianSlice, Error, LittleEndian, Reader, ReaderOffset, Result...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/pyo3-ffi-0.28.2/src/object.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 343.88 | **LOC:** 748 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.3%)
- **Documentation Coverage:** 98.6301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyObject_TypeCheck` **(Annotated & Test Methods)** (Impact: 3.7)
  * `PyType_FromMetaclass` **(Parameter Forwarders)** (Impact: 2.6)
  * `PyType_FromModuleAndSpec` **(Parameter Forwarders)** (Impact: 2.4)
  * `PyObject_GetOptionalAttr` **(Parameter Forwarders)** (Impact: 2.4)
  * `PyObject_GetOptionalAttrString` **(Parameter Forwarders)** (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 286`, `args: 76`, `func_start: 76`, `class_start: 9`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 60`
* *Architecture:* `api: 194`, `import: 8`
* *Defense:* `doc: 15`, `test: 3`, `sync_locks: 3`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicU32, Py_ssize_t, c_int, c_uint, c_ulong, c_void, crate::PyMutex, crate::cpython::object::PyTypeObject...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/bytes-1.11.1/tests/test_bytes.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 320.14 | **LOC:** 1723 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (20.2%), Concurrency Surface (formerly Concurrency) (12.9%), Complexity Load (formerly Cognitive Load) (9.1%)
- **Documentation Coverage:** 98.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stress` **(Annotated & Test Methods)** (Impact: 8.9)
  * `advance_bytes_mut_remaining_capacity` **(I/O & Config Routines)** (Impact: 7.7)
    * *Intent:* // Ensures BytesMut::advance reduces always capacity // // See https://github.com/tokio-rs/bytes/iss...
  * `as_ref` **(State Mutators)** (Impact: 4.5)
  * `split_off_to_loop` **(Annotated & Test Methods)** (Impact: 4.2)
  * `split_off_to_at_gt_len` **(Annotated & Test Methods)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 9
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 497`, `args: 134`, `func_start: 127`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 30`, `dead_code: 1`, `unreferenced_by_name: 110`
* *Architecture:* `api: 4`, `concurrency: 4`, `import: 11`
* *Defense:* `doc: 4`, `test: 382`, `sync_locks: 5`, `immutability_locks: 9`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AssertUnwindSafe, Barrier, BufMut, Bytes, BytesMut, Ordering, bytes::Buf, std::fmt::Write...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/rnglists.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 312.9 | **LOC:** 1045 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 2.088; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.9%), Guard Balance (formerly Safety Score) (59.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 22.9508% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 44.6)
    * *Intent:* /// Parse a range entry from `.debug_rnglists`
  * `convert_raw` **(Compute Cores)** (Impact: 18.4)
    * *Intent:* /// Convert a raw range into a range, and update the state of the iterator. /// /// The raw range sh...
  * `test_rnglists` **(I/O & Config Routines)** (Impact: 12.9)
  * `get_offset` **(Generic / Templated Code)** (Impact: 9.7)
    * *Intent:* /// Returns the `.debug_rnglists` offset at the given `base` and `index`. /// /// The `base` must be...
  * `test_ranges` **(I/O & Config Routines)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 173`, `args: 44`, `func_start: 39`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 54`, `dead_code: 5`, `duplicate_logic: 4`, `unreferenced_by_name: 9`
* *Architecture:* `api: 36`, `import: 11`
* *Defense:* `safety: 1`, `doc: 147`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DebugAddr, DebugAddrIndex, DebugRngListsBase, DebugRngListsIndex, DwarfFileType, Encoding, EndianSlice, Error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/detect/aarch64_apple.rs` -> **Severity: 0.232** (Embedded: 0.0039 * Error Risk: 60.0315%)
- `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/lookup.rs` -> **Severity: 0.219** (Embedded: 0.0043 * Error Risk: 51.0343%)
- `orjson-3.11.8/src/serialize/writer/json.rs` -> **Severity: 0.212** (Embedded: 0.0021 * Error Risk: 98.8887%)
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/detect/auxv.rs` -> **Severity: 0.184** (Embedded: 0.0039 * Error Risk: 47.5139%)
- `orjson-3.11.8/include/cargo/portable-atomic-1.13.1/src/imp/atomic128/intrinsics.rs` -> **Severity: 0.183** (Embedded: 0.0021 * Error Risk: 85.1732%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `orjson-3.11.8/src/deserialize/backend/ffi.rs` -> **Severity: 448.1** (Blast Radius: 4.481 * Doc Risk: 100.0%)
- `orjson-3.11.8/include/cargo/unwinding-0.2.8/src/panic.rs` -> **Severity: 386.3** (Blast Radius: 3.863 * Doc Risk: 100.0%)
- `orjson-3.11.8/src/serialize/writer/json.rs` -> **Severity: 386.3** (Blast Radius: 3.863 * Doc Risk: 100.0%)
- `orjson-3.11.8/include/yyjson/yyjson.h` -> **Severity: 357.035** (Blast Radius: 3.863 * Doc Risk: 92.4242%)
- `orjson-3.11.8/include/cargo/gimli-0.32.3/src/read/lookup.rs` -> **Severity: 303.585** (Blast Radius: 5.638 * Doc Risk: 53.8462%)

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
