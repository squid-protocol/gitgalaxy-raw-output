# ARCHITECTURAL_BRIEF: alacritty
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/alacritty/alacritty.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 338 |
| Analyzed Artifacts (Scanned) | 260 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 78 |
| Total LOC | 26023 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 76.9% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8047 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.527 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 135 | 135 | 51.9% |
| RUST | 88 | 24789 | 33.8% |
| MARKDOWN | 8 | 0 | 3.1% |
| PLAINTEXT | 8 | 0 | 3.1% |
| XML | 8 | 0 | 3.1% |
| GLSL | 6 | 267 | 2.3% |
| SHELL | 6 | 761 | 2.3% |
| MAKEFILE | 1 | 71 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 199 | 76.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 45 | 17.3% |
| Static: Literature & Documentation | 16 | 6.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 78*

**Composition by Extension & Reason:**
- `.recording`: 45x Excluded (Unsupported Extension: '.recording')
- `.toml`: 5x Unsupported Format (.toml), 1x Excluded (Unsupported Extension: '.toml')
- `.scd`: 5x Excluded (Unsupported Extension: '.scd')
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.manifest`: 1x Excluded (Unsupported Extension: '.manifest')
- `.rc`: 1x Excluded (Unsupported Extension: '.rc')
- `.wxs`: 1x Excluded (Unsupported Extension: '.wxs')
- `.rtf`: 1x Excluded (Unsupported Extension: '.rtf')
- `.info`: 1x Excluded (Unsupported Extension: '.info')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 65.9 | 4.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 18.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 88.4 | 6.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 97.6 | 1.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.7 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 37.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.8 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 39.0 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 22.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1580 | 86 | 20 | `alacritty/src/renderer/text/builtin_font.rs` |
| cleanup | 15 | 6 | 0 | `alacritty/src/display/mod.rs` |
| guards | 510 | 72 | 6 | `alacritty_terminal/src/term/mod.rs` |
| danger | 310 | 45 | 4 | `alacritty_terminal/src/term/search.rs` |
| concurrency | 96 | 19 | 0 | `alacritty_terminal/src/tty/windows/blocking.rs` |
| connectivity | 1278 | 84 | 16 | `alacritty/src/event.rs` |
| io | 87 | 23 | 0 | `extra/completions/alacritty.bash` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 4 | 0 | `alacritty_terminal/src/tty/windows/child.rs` |
| time | 6 | 6 | 0 | `alacritty/src/config/bell.rs` |
| serialization | 24 | 7 | 0 | `alacritty_config_derive/tests/config.rs` |
| regex | 2 | 2 | 0 | `Makefile` |
| events | 191 | 32 | 2 | `alacritty_terminal/src/term/mod.rs` |
| tests | 943 | 35 | 3 | `alacritty_terminal/src/grid/tests.rs` |
| docs | 2026 | 80 | 21 | `alacritty_terminal/src/term/mod.rs` |
| debt | 124 | 28 | 1 | `scripts/fg-bg.sh` |
| mutation | 5102 | 90 | 52 | `alacritty_terminal/src/term/mod.rs` |
| dead_code | 481 | 69 | 5 | `alacritty_terminal/src/term/mod.rs` |
| credential | 4 | 4 | 0 | `extra/logo/alacritty-term+scanlines.svg` |
| threat | 21 | 12 | 0 | `alacritty_terminal/src/tty/windows/blocking.rs` |
| ml_ai | 302 | 29 | 1 | `alacritty/src/renderer/text/builtin_font.rs` |
| ui | 49 | 2 | 0 | `scripts/fg-bg.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `extra/completions/alacritty.bash` (Hits: 40)
- `Makefile` (Hits: 10)
- `alacritty/src/window_context.rs` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 2 inbound connections
2. **INSTALL.md** (`INSTALL.md`) — 2 inbound connections
3. **CHANGELOG.md** (`alacritty_terminal/CHANGELOG.md`) — 2 inbound connections
4. **debug.rs** (`alacritty/src/config/debug.rs`) — 2 inbound connections
5. **ipc.rs** (`alacritty/src/polling/ipc.rs`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **event.rs** (`alacritty/src/event.rs`) — 99 outbound dependencies
2. **mod.rs** (`alacritty/src/display/mod.rs`) — 85 outbound dependencies
3. **mod.rs** (`alacritty/src/input/mod.rs`) — 73 outbound dependencies
4. **mod.rs** (`alacritty_terminal/src/term/mod.rs`) — 63 outbound dependencies
5. **ui_config.rs** (`alacritty/src/config/ui_config.rs`) — 52 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_alacritty` (@ `extra/completions/alacritty.bash`) -> Impact: **194.2** | LOC: 525
- `box_drawing` (@ `alacritty/src/renderer/text/builtin_font.rs`) -> Impact: **121.5** | LOC: 549
- `draw` (@ `alacritty/src/display/mod.rs`) -> Impact: **101.0** | LOC: 273
  * *Intent:* /// Draw the screen. /// /// A reference to Term whose state is being drawn must be provided. /// /// This call may block if vsync is enabled.
- `regex_search_internal` (@ `alacritty_terminal/src/term/search.rs`) -> Impact: **97.4** | LOC: 160
  * *Intent:* /// Find the next regex match. /// /// To automatically log regex complexity errors, use [`Self::regex_search`] instead.
- `shrink_columns` (@ `alacritty_terminal/src/grid/resize.rs`) -> Impact: **87.2** | LOC: 144
  * *Intent:* /// Shrink number of columns in each row, reflowing if necessary.
- `user_event` (@ `alacritty/src/event.rs`) -> Impact: **81.0** | LOC: 180
- `grow_columns` (@ `alacritty_terminal/src/grid/resize.rs`) -> Impact: **73.1** | LOC: 142
  * *Intent:* /// Grow number of columns in each row, reflowing if necessary.
- `visit_map` (@ `alacritty/src/config/bindings.rs`) -> Impact: **69.8** | LOC: 149
- `scroll_terminal` (@ `alacritty/src/input/mod.rs`) -> Impact: **68.3** | LOC: 69
- `deserialize` (@ `alacritty/src/config/bindings.rs`) -> Impact: **67.2** | LOC: 212

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `alacritty_terminal/src/term` | 4 | 2015.52 | 11.87% | 57.05% |
| `alacritty/src` | 11 | 1913.46 | 10.23% | 43.58% |
| `alacritty/src/display` | 9 | 1884.6 | 15.51% | 47.69% |
| `alacritty/src/config` | 16 | 1369.94 | 4.43% | 26.83% |
| `alacritty_terminal/src` | 8 | 1186.94 | 11.56% | 43.89% |
| `alacritty_terminal/src/grid` | 5 | 997.7 | 20.96% | 53.1% |
| `alacritty/src/input` | 2 | 984.76 | 11.08% | 11.14% |
| `alacritty/src/renderer/text` | 6 | 933.94 | 9.8% | 22.81% |
| `extra/completions` | 2 | 576.42 | 35.87% | 0.0% |
| `alacritty/src/renderer` | 4 | 439.12 | 6.47% | 24.34% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `alacritty_config_derive/src/config_deserialize/de_enum.rs` -> **99.9893%** Exposure
- `alacritty_terminal/src/tty/mod.rs` -> **99.8629%** Exposure
- `alacritty_terminal/src/sync.rs` -> **99.593%** Exposure
- `alacritty_terminal/src/tty/windows/mod.rs` -> **99.2767%** Exposure
- `alacritty_config/src/lib.rs` -> **99.2663%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `alacritty/src/config/mod.rs` -> **100.0%** Exposure
- `alacritty/src/config/monitor.rs` -> **100.0%** Exposure
- `alacritty/src/config/serde_utils.rs` -> **100.0%** Exposure
- `alacritty_terminal/src/grid/resize.rs` -> **100.0%** Exposure
- `extra/completions/alacritty.bash` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `alacritty_terminal/src/term/mod.rs` -> **65** Orphaned Functions | **0** Duplicates
- `alacritty_terminal/src/term/search.rs` -> **35** Orphaned Functions | **0** Duplicates
- `alacritty/src/config/bindings.rs` -> **22** Orphaned Functions | **0** Duplicates
- `alacritty_terminal/src/vi_mode.rs` -> **19** Orphaned Functions | **0** Duplicates
- `alacritty_terminal/src/selection.rs` -> **18** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1691` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `alacritty_terminal/src/tty/windows/mod.rs` (RUST) -> Cumulative Risk: **589.5**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 97.84 | **LOC:** 240 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.2767%), State Flux (98.3016%), Documentation (88.8889%)
- **Heaviest Functions:** `push_escaped_arg` (Impact: 16.9), `cmdline` (Impact: 6.5), `test_escape` (Impact: 5.6)

### 2. `alacritty/src/event.rs` (RUST) -> Cumulative Risk: **550.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 982.1 | **LOC:** 2094 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.657%), Api Exposure (81.6207%), Verification (80.0%)
- **Heaviest Functions:** `user_event` (Impact: 81.0), `handle_event` (Impact: 58.2), `paste` (Impact: 24.1)

### 3. `alacritty/src/display/color.rs` (RUST) -> Cumulative Risk: **547.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 188.16 | **LOC:** 369 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8234%), Documentation (91.4286%), Verification (80.0%)
- **Heaviest Functions:** `fill_cube` (Impact: 22.0), `from_str` (Impact: 12.4), `fill_gray_ramp` (Impact: 8.1)

### 4. `extra/completions/alacritty.bash` (SHELL) -> Cumulative Risk: **544.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 564.96 | **LOC:** 532 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.0953%)
- **Heaviest Functions:** `_alacritty` (Impact: 194.2), `Anonymous_Block` (Impact: 5.2)

### 5. `alacritty_terminal/src/term/search.rs` (RUST) -> Cumulative Risk: **534.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 522.08 | **LOC:** 1252 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.125%), State Flux (92.3725%), Verification (80.0%)
- **Heaviest Functions:** `regex_search_internal` (Impact: 97.4), `bracket_search` (Impact: 31.5), `skip_fullwidth` (Impact: 21.8)

### 6. `alacritty_terminal/src/grid/row.rs` (RUST) -> Cumulative Risk: **527.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 113.6 | **LOC:** 294 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (95.4978%), Tech Debt (92.4142%), Verification (80.0%)
- **Heaviest Functions:** `shrink` (Impact: 7.8), `reset` (Impact: 6.2), `grow` (Impact: 3.9)

### 7. `alacritty_terminal/src/selection.rs` (RUST) -> Cumulative Risk: **504.76**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 321.98 | **LOC:** 669 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.53%), Verification (80.0%), Tech Debt (78.5409%)
- **Heaviest Functions:** `rotate` (Impact: 38.5), `contains_cell` (Impact: 28.3), `range_simple` (Impact: 21.8)

### 8. `alacritty_terminal/src/tty/windows/conpty.rs` (RUST) -> Cumulative Risk: **501.25**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 83.98 | **LOC:** 317 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (88.8889%), State Flux (83.4499%), Verification (80.0%)
- **Heaviest Functions:** `new` (Impact: 22.3), `convert_custom_env` (Impact: 11.8), `load_conpty` (Impact: 5.9)

### 9. `alacritty_terminal/src/term/mod.rs` (RUST) -> Cumulative Risk: **493.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1349.74 | **LOC:** 3303 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.5124%), Verification (80.0%), Safety Score (67.8558%)
- **Heaviest Functions:** `line_to_string` (Impact: 43.3), `input` (Impact: 31.6), `clear_screen` (Impact: 19.1)

### 10. `alacritty_config_derive/src/config_deserialize/de_struct.rs` (RUST) -> Cumulative Risk: **491.32**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 89.76 | **LOC:** 195 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.0037%), Verification (80.0%), Tech Debt (76.3385%)
- **Heaviest Functions:** `field_deserializer` (Impact: 26.9), `derive_deserialize` (Impact: 17.5), `visit_map` (Impact: 10.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `alacritty_terminal/src/term/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1349.74 | **LOC:** 3303 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.4144%), Tech Debt (55.1338%)
**Top Internal Functions/Classes:**
  * `line_to_string` (Impact: 43.3)
    * *Intent:* /// Convert a single line in the grid to a String.
  * `input` (Impact: 31.6)
    * *Intent:* /// A character to be displayed.
  * `clear_screen` (Impact: 19.1)
  * `put_tab` (Impact: 18.8)
    * *Intent:* /// Insert tab at cursor position.
  * `write_at_cursor` (Impact: 15.7)
    * *Intent:* /// Write `c` to the cell at the cursor position.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 105 instances
* *State Mutation (weighted view):* 480
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 574`, `args: 183`, `func_start: 156`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 4`, `state_mutation: 270`, `dead_code: 1`, `unreferenced_by_name: 65`
* *Architecture:* `api: 73`, `import: 29`
* *Defense:* `safety: 24`, `doc: 182`, `test: 141`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Attr, Boundary, CharsetIndex, Color, Column, CursorShape, CursorStyle, Direction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/event.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 982.1 | **LOC:** 2094 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (20.4957%), Tech Debt (8.2927%)
**Top Internal Functions/Classes:**
  * `user_event` (Impact: 81.0)
  * `handle_event` (Impact: 58.2)
    * *Intent:* /// Handle events from winit.
  * `paste` (Impact: 24.1)
    * *Intent:* /// Paste a text into the terminal.
  * `semantic_word` (Impact: 21.4)
    * *Intent:* /// Get the semantic word at the specified point.
  * `scroll` (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 71 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 402`, `args: 131`, `func_start: 96`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 120`, `fragile_debt: 1`
* *Architecture:* `api: 98`, `import: 52`
* *Defense:* `safety: 42`, `doc: 87`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ActionContext, ClipboardType, Column, ControlFlow, DeviceEvents, Dimensions, Direction, Event...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/input/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 652.42 | **LOC:** 1560 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (14.9131%), Tech Debt (13.319%)
**Top Internal Functions/Classes:**
  * `scroll_terminal` (Impact: 68.3)
  * `execute` (Impact: 45.0)
  * `mouse_moved` (Impact: 39.6)
  * `normal_mouse_report` (Impact: 23.6)
  * `mouse_input` (Impact: 20.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 349`, `args: 111`, `func_start: 105`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 33`, `dead_code: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 22`, `import: 39`
* *Defense:* `safety: 17`, `doc: 31`, `test: 6`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BindingMode, Column, Direction, Event, EventType, Handler, InlineSearchState, Instant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 644.24 | **LOC:** 1635 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.9493%), Tech Debt (39.5161%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 101.0)
    * *Intent:* /// Draw the screen. /// /// A reference to Term whose state is being drawn must be provided. /// //...
  * `update_highlighted_hints` (Impact: 40.1)
    * *Intent:* /// Update the mouse/vi mode cursor hint highlighting. /// /// This will return whether the highligh...
  * `new` (Impact: 38.4)
  * `handle_update` (Impact: 28.2)
    * *Intent:* // XXX: this function must not call to any `OpenGL` related tasks. Renderer updates are // performed...
  * `draw_ime_preview` (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 373`, `args: 90`, `func_start: 58`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 63`, `fragile_debt: 2`, `unreferenced_by_name: 13`
* *Architecture:* `api: 60`, `import: 47`
* *Defense:* `safety: 22`, `doc: 86`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Direction, EventType, Formatter, GlyphCache, HintState, Instant, Line, LineDamageBounds...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/completions/alacritty.bash` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 564.96 | **LOC:** 532 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.9056%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_alacritty` (Impact: 194.2)
  * `Anonymous_Block` (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 270`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 147`
* *Architecture:* `io: 40`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/term/search.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 522.08 | **LOC:** 1252 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.0811%), Tech Debt (99.125%)
**Top Internal Functions/Classes:**
  * `regex_search_internal` (Impact: 97.4)
    * *Intent:* /// Find the next regex match. /// /// To automatically log regex complexity errors, use [`Self::reg...
  * `bracket_search` (Impact: 31.5)
    * *Intent:* /// Find next matching bracket.
  * `skip_fullwidth` (Impact: 21.8)
    * *Intent:* /// Advance a grid iterator over fullwidth characters.
  * `inline_search_right` (Impact: 19.3)
    * *Intent:* /// Searching to the right, find the next character contained in `needles`.
  * `next_match_right` (Impact: 16.5)
    * *Intent:* /// Find the next match to the right of the origin.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 482`, `args: 68`, `func_start: 55`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 46`, `dead_code: 4`, `fragile_debt: 7`, `unreferenced_by_name: 35`
* *Architecture:* `api: 16`, `import: 18`
* *Defense:* `safety: 9`, `doc: 31`, `test: 87`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cache, Column, Config, DFA, Dimensions, Direction, Flags, GridIterator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/bindings.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 427.56 | **LOC:** 1453 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.1502%), Tech Debt (36.5947%)
**Top Internal Functions/Classes:**
  * `visit_map` (Impact: 69.8)
  * `deserialize` (Impact: 67.2)
  * `triggers_match` (Impact: 18.4)
  * `deserialize` (Impact: 18.1)
  * `deserialize` (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 208`, `args: 58`, `func_start: 60`, `class_start: 19`
* *Risk/State:* `state_mutation: 18`, `dead_code: 1`, `unreferenced_by_name: 22`
* *Architecture:* `api: 32`, `import: 16`
* *Defense:* `safety: 11`, `doc: 107`, `test: 52`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Debug, Deserializer, Display, Error, KeyCode, KeyLocation, MapAccess, ModifiersState...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/vi_mode.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 425.7 | **LOC:** 894 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.9902%), Tech Debt (59.8871%)
**Top Internal Functions/Classes:**
  * `semantic` (Impact: 34.0)
    * *Intent:* /// Move by semantically separated word, like w/b/e/ge in vi.
  * `motion` (Impact: 31.7)
    * *Intent:* /// Move vi mode cursor.
  * `word` (Impact: 26.5)
    * *Intent:* /// Move by whitespace separated word, like W/B/E/gE in vi.
  * `first_occupied` (Impact: 24.7)
    * *Intent:* /// Find next non-empty cell to move to.
  * `is_boundary` (Impact: 12.3)
    * *Intent:* /// Check if point is at screen boundary.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 214`, `args: 46`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `state_mutation: 133`, `unreferenced_by_name: 19`
* *Architecture:* `api: 6`, `import: 13`
* *Defense:* `safety: 12`, `doc: 36`, `test: 105`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Column, Direction, GridCell, Line, Point, Serialize, Side, Term...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/text/builtin_font.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 355.96 | **LOC:** 1033 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (8.6269%), Tech Debt (11.9007%)
**Top Internal Functions/Classes:**
  * `box_drawing` (Impact: 121.5)
  * `draw_rounded_corner` (Impact: 36.2)
    * *Intent:* /// Draws a quarter of a circle centered in `(0., self.height - radius)` with radius /// `self.width...
  * `draw_line` (Impact: 35.2)
    * *Intent:* /// Xiaolin Wu's line drawing from (`from_x`, `from_y`) to (`to_x`, `to_y`).
  * `powerline_drawing` (Impact: 29.6)
  * `put_pixel` (Impact: 13.9)
    * *Intent:* /// Put pixel into buffer with the given color if the color is brighter than the one buffer /// alre...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 236`, `args: 97`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 19`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 2`, `doc: 39`, `test: 7`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Metrics, RasterizedGlyph, crate::config::ui_config::Delta, crossfont::BitmapBuffer, crossfont::Metrics, mem, ops, std::cmp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/hint.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 339.34 | **LOC:** 704 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.3434%), Tech Debt (43.9973%)
**Top Internal Functions/Classes:**
  * `hint_post_processing` (Impact: 37.5)
    * *Intent:* /// Apply some hint post processing heuristics. /// /// This will check the end of the hint and make...
  * `update_matches` (Impact: 21.9)
    * *Intent:* /// Update the visible hint matches and key labels.
  * `keyboard_input` (Impact: 20.1)
    * *Intent:* /// Handle keyboard input during hint selection.
  * `highlighted_at` (Impact: 19.6)
    * *Intent:* /// Check if there is a hint highlighted at the specified point.
  * `hyperlink_at` (Impact: 18.6)
    * *Intent:* /// Retrieve the hyperlink with its range, if there is one at the specified point. /// /// This will...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 153`, `args: 53`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`, `dead_code: 1`, `unreferenced_by_name: 11`
* *Architecture:* `api: 19`, `import: 18`
* *Defense:* `safety: 12`, `doc: 64`, `test: 40`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Column, Dimensions, Direction, HintAction, Line, Point, RegexIter, RegexSearch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/grid/resize.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 338.58 | **LOC:** 390 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.2573%), Tech Debt (10.8486%)
**Top Internal Functions/Classes:**
  * `shrink_columns` (Impact: 87.2)
    * *Intent:* /// Shrink number of columns in each row, reflowing if necessary.
  * `grow_columns` (Impact: 73.1)
    * *Intent:* /// Grow number of columns in each row, reflowing if necessary.
  * `resize` (Impact: 7.9)
    * *Intent:* /// Resize the grid's width and/or height.
  * `grow_lines` (Impact: 4.8)
    * *Intent:* /// Add lines to the visible area. /// /// Alacritty keeps the cursor at the bottom of the terminal ...
  * `shrink_lines` (Impact: 4.5)
    * *Intent:* /// Remove lines from the visible area. /// /// The behavior in Terminal.app and iTerm.app is to kee...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 80`, `args: 10`, `func_start: 5`
* *Risk/State:* `state_mutation: 61`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 6`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Column, Grid, GridCell, Line, ResetDiscriminant, crate::grid::Dimensions, crate::grid::row::Row, crate::index::Boundary...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/input/keyboard.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 332.34 | **LOC:** 719 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (7.2438%), Tech Debt (8.9575%)
**Top Internal Functions/Classes:**
  * `build_sequence` (Impact: 43.5)
    * *Intent:* /// Build a key's keyboard escape sequence based on the given `key`, `mods`, and `mode`. /// /// The...
  * `key_input` (Impact: 35.3)
    * *Intent:* /// Process key input.
  * `try_build_textual` (Impact: 34.4)
    * *Intent:* /// Try building sequence from the event's emitting text.
  * `process_key_bindings` (Impact: 33.0)
    * *Intent:* /// Attempt to find a binding and execute its action. /// /// The provided mode, mods, and key must ...
  * `try_build_control_char_or_mod` (Impact: 25.3)
    * *Intent:* /// Try building escape from control characters (e.g. Enter) and modifiers.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 126`, `args: 35`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 8`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 12`, `doc: 30`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BindingKey, BindingMode, Execute, KeyBinding, KeyEvent, KeyLocation, ModifiersState, NamedKey...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/selection.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 321.98 | **LOC:** 669 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.1352%), Tech Debt (78.5409%)
**Top Internal Functions/Classes:**
  * `rotate` (Impact: 38.5)
  * `contains_cell` (Impact: 28.3)
    * *Intent:* /// Check if the cell at a point is part of the selection.
  * `range_simple` (Impact: 21.8)
  * `is_empty` (Impact: 21.4)
  * `range_block` (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 123`, `args: 41`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 30`, `unreferenced_by_name: 18`
* *Architecture:* `api: 17`, `import: 12`
* *Defense:* `safety: 1`, `doc: 83`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Column, Flags, GridCell, Indexed, Line, Point, Range, RangeBounds...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/grid/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 265.32 | **LOC:** 657 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.4326%), Tech Debt (73.5192%)
**Top Internal Functions/Classes:**
  * `scroll_up` (Impact: 24.8)
    * *Intent:* /// Move lines at the bottom toward the top. /// /// This is the performance-sensitive part of scrol...
  * `scroll_down` (Impact: 22.9)
  * `clear_viewport` (Impact: 9.7)
  * `reset_region` (Impact: 8.1)
    * *Intent:* /// Reset a visible region within the grid.
  * `eq` (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 110`, `args: 48`, `func_start: 48`, `class_start: 9`
* *Risk/State:* `state_mutation: 21`, `unreferenced_by_name: 15`
* *Architecture:* `api: 36`, `import: 8`
* *Defense:* `safety: 1`, `doc: 81`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Deref, Index, IndexMut, Line, Point, Range, RangeBounds, ResetDiscriminant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/content.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 258.74 | **LOC:** 553 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.3685%), Tech Debt (11.7079%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 39.2)
  * `new` (Impact: 27.0)
  * `compute_fg_rgb` (Impact: 16.2)
    * *Intent:* /// Get the RGB color from a cell's foreground color.
  * `renderable_cursor` (Impact: 15.8)
    * *Intent:* /// Assemble the information required to render the terminal cursor.
  * `advance` (Impact: 12.7)
    * *Intent:* /// Advance the regex tracker to the next point. /// /// This will return `true` if the point passed...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *Amplified Sql Injection:* 1 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 131`, `args: 40`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`, `unreferenced_by_name: 2`
* *Architecture:* `api: 25`, `import: 17`
* *Defense:* `safety: 8`, `doc: 45`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CursorShape, DIM_FACTOR, Flags, HintState, Hyperlink, Indexed, Line, List...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/event_loop.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 230.0 | **LOC:** 487 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (17.5772%), Tech Debt (9.7112%)
**Top Internal Functions/Classes:**
  * `spawn` (Impact: 56.9)
  * `pty_read` (Impact: 41.5)
  * `pty_write` (Impact: 17.1)
  * `recv` (Impact: 7.6)
  * `new` (Impact: 5.9)
    * *Intent:* /// Create a new event loop.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 113`, `args: 25`, `func_start: 23`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 11`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 12`, `concurrency: 10`, `import: 17`
* *Defense:* `safety: 11`, `doc: 22`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Display, ErrorKind, Event, EventListener, Events, Formatter, PollMode, Poller...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/ui_config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 229.06 | **LOC:** 738 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7701%), Tech Debt (50.224%)
**Top Internal Functions/Classes:**
  * `visit_map` (Impact: 15.9)
  * `deserialize` (Impact: 15.6)
  * `deserialize_bindings` (Impact: 10.2)
  * `deserialize` (Impact: 8.1)
  * `compiled` (Impact: 6.9)
    * *Intent:* /// Get a reference to the compiled regex. /// /// If the regex is not already compiled, this will c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 141`, `args: 42`, `func_start: 37`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 8`, `unreferenced_by_name: 14`
* *Architecture:* `api: 61`, `import: 34`
* *Defense:* `safety: 3`, `doc: 67`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Action, Binding, BindingKey, Deserializer, Formatter, KeyBinding, KeyLocation, MapAccess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/window_context.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 216.0 | **LOC:** 569 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.321%), Tech Debt (37.1756%)
**Top Internal Functions/Classes:**
  * `handle_event` (Impact: 33.8)
    * *Intent:* /// Process events for this terminal window.
  * `submit_display_update` (Impact: 32.7)
    * *Intent:* /// Submit the pending changes to the `Display`.
  * `update_config` (Impact: 21.0)
    * *Intent:* /// Update the terminal window to the latest config.
  * `initial` (Impact: 18.0)
    * *Intent:* /// Create initial window context that does bootstrapping the graphics API we're going to use.
  * `additional` (Impact: 15.5)
    * *Intent:* /// Create additional context with the graphics platform other windows are using.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 144`, `args: 20`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 16`, `unreferenced_by_name: 8`
* *Architecture:* `io: 5`, `api: 14`, `concurrency: 1`, `import: 35`
* *Defense:* `doc: 14`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Event, EventLoopProxy, EventProxy, InlineSearchState, Modifiers, Mouse, Msg, Notifier...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 210.74 | **LOC:** 454 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.3001%), Tech Debt (26.5745%)
**Top Internal Functions/Classes:**
  * `load_imports` (Impact: 19.9)
    * *Intent:* /// Load all referenced configuration files.
  * `imports` (Impact: 17.8)
    * *Intent:* /// Get all import paths for a configuration.
  * `deserialize_config` (Impact: 16.8)
    * *Intent:* /// Deserialize a configuration file.
  * `prune_yaml_nulls` (Impact: 10.0)
    * *Intent:* /// Prune the nulls from the YAML to ensure TOML compatibility.
  * `installed_config` (Impact: 9.8)
    * *Intent:* /// Get the location of the first found default config file paths /// according to the following ord...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 113`, `args: 38`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `unreferenced_by_name: 5`
* *Architecture:* `api: 26`, `import: 16`
* *Defense:* `safety: 8`, `doc: 27`, `test: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BindingKey, BindingMode, Display, Formatter, KeyBinding, MouseAction, MouseEvent, PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/window.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 209.94 | **LOC:** 538 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (5.9169%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 19.1)
    * *Intent:* /// Create a new window. /// /// This creates a window and fully initializes a window.
  * `get_platform_window` (Impact: 7.3)
  * `update_ime_position` (Impact: 7.0)
    * *Intent:* /// Adjust the IME editor position according to the new location of the cursor.
  * `get_platform_window` (Impact: 5.7)
  * `set_fullscreen` (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 71`, `args: 45`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 47`, `import: 18`
* *Defense:* `safety: 6`, `doc: 37`, `test: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ActiveEventLoopExtX11, Display, EventLoopExtStartupNotify, Formatter, Fullscreen, Identity, ImePurpose, NSView...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/message_bar.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 193.38 | **LOC:** 414 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.2575%), Tech Debt (89.1414%)
**Top Internal Functions/Classes:**
  * `text` (Impact: 31.3)
    * *Intent:* /// Formatted message text lines.
  * `remove_target` (Impact: 6.1)
  * `remove_duplicates` (Impact: 4.1)
  * `pop` (Impact: 3.3)
    * *Intent:* /// Remove the currently visible message.
  * `truncates_long_messages` (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 114`, `args: 32`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 45`, `unreferenced_by_name: 14`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 5`, `doc: 17`, `test: 32`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alacritty_terminal::grid::Dimensions, crate::display::SizeInfo, std::collections::VecDeque, super::*, unicode_width::UnicodeWidthChar
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/color.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 188.16 | **LOC:** 369 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.4241%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fill_cube` (Impact: 22.0)
  * `from_str` (Impact: 12.4)
  * `fill_gray_ramp` (Impact: 8.1)
  * `deserialize` (Impact: 7.9)
  * `fill_named` (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 83`, `args: 29`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `api: 15`, `import: 10`
* *Defense:* `safety: 6`, `doc: 4`, `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Deref, Deserializer, Display, Formatter, Index, IndexMut, Mul, Rgb...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/cli.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 172.72 | **LOC:** 568 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.7833%), Tech Debt (87.6743%)
**Top Internal Functions/Classes:**
  * `override_pty_config` (Impact: 9.4)
    * *Intent:* /// Override the [`PtyOptions`]'s fields with the [`TerminalOptions`].
  * `from_options` (Impact: 6.5)
    * *Intent:* /// Parse CLI config overrides.
  * `override_config` (Impact: 6.1)
    * *Intent:* /// Override configuration file with options from the CLI.
  * `override_config` (Impact: 6.0)
    * *Intent:* /// Apply CLI config overrides, removing broken ones.
  * `override_identity_config` (Impact: 5.6)
    * *Intent:* /// Override the [`WindowIdentity`]'s fields with the [`WindowOptions`].
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *Amplified Sql Injection:* 1 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 109`, `args: 30`, `func_start: 27`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 16`, `dead_code: 3`, `unreferenced_by_name: 17`
* *Architecture:* `io: 3`, `api: 51`, `import: 21`
* *Defense:* `safety: 5`, `doc: 64`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Args, DerefMut, Identity, Parser, Serialize, Subcommand, ValueHint, alacritty_config::SerdeReplace...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/rects.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 172.32 | **LOC:** 497 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0317%), Tech Debt (33.0752%)
**Top Internal Functions/Classes:**
  * `update_flag` (Impact: 21.8)
    * *Intent:* /// Update the lines for a specific flag.
  * `update_uniforms` (Impact: 17.6)
  * `draw` (Impact: 13.7)
  * `new` (Impact: 11.5)
  * `push_rects` (Impact: 11.0)
    * *Intent:* /// Push all rects required to draw the cell's line.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 101`, `args: 19`, `func_start: 15`, `class_start: 7`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 18`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 25`, `import: 14`
* *Defense:* `safety: 9`, `doc: 15`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Point, ShaderProgram, ShaderVersion, ahash::RandomState, alacritty_terminal::grid::Dimensions, alacritty_terminal::index::Column, alacritty_terminal::term::cell::Flags, crate::display::SizeInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/grid/storage.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 168.96 | **LOC:** 770 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1363%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initialize` (Impact: 6.7)
    * *Intent:* /// Dynamically grow the storage buffer at runtime.
  * `compute_index` (Impact: 6.0)
    * *Intent:* /// Compute actual index in underlying storage given the requested index.
  * `swap` (Impact: 5.2)
    * *Intent:* /// Swap implementation for Row<T>. /// /// Exploits the known size of Row<T> to produce a slightly ...
  * `with_capacity` (Impact: 4.0)
  * `shrink_lines` (Impact: 3.9)
    * *Intent:* /// Shrink the number of lines in the buffer.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 112`, `args: 38`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 26`, `dead_code: 1`
* *Architecture:* `api: 30`, `import: 12`
* *Defense:* `doc: 159`, `test: 70`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.703
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IndexMut, Line, Serialize, Storage, crate::grid::GridCell, crate::grid::row::Row, crate::grid::storage::MAX_CACHE_SIZE, crate::index::Column...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `alacritty/src/config/bindings.rs` -> **Jonas** (100.0% isolated ownership) | Magnitude: 427.56
- `alacritty/src/config/mod.rs` -> **Jonas** (100.0% isolated ownership) | Magnitude: 210.74
- `alacritty/src/config/monitor.rs` -> **Lulu** (100.0% isolated ownership) | Magnitude: 88.64
- `alacritty/src/polling/ipc.rs` -> **Christian Duerr** (100.0% isolated ownership) | Magnitude: 88.32
- `alacritty/src/polling/mod.rs` -> **Christian Duerr** (100.0% isolated ownership) | Magnitude: 68.22

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `alacritty/src/renderer/platform.rs` -> **Severity: 0.242** (Embedded: 0.0039 * Error Risk: 62.7867%)
- `alacritty_config_derive/src/serde_replace.rs` -> **Severity: 0.23** (Embedded: 0.0039 * Error Risk: 59.5096%)
- `alacritty/src/renderer/text/glsl3.rs` -> **Severity: 0.221** (Embedded: 0.0039 * Error Risk: 57.3043%)
- `alacritty_terminal/src/thread.rs` -> **Severity: 0.216** (Embedded: 0.0039 * Error Risk: 55.9714%)
- `alacritty/src/polling/ipc.rs` -> **Severity: 0.149** (Embedded: 0.0039 * Error Risk: 38.5915%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `alacritty/src/config/debug.rs` -> **Severity: 1267.2** (Blast Radius: 12.672 * Doc Risk: 100.0%)
- `alacritty/src/renderer/text/glsl3.rs` -> **Severity: 648.947** (Blast Radius: 6.85 * Doc Risk: 94.7368%)
- `alacritty/src/renderer/platform.rs` -> **Severity: 513.75** (Blast Radius: 6.85 * Doc Risk: 75.0%)
- `alacritty_config_derive/src/serde_replace.rs` -> **Severity: 456.667** (Blast Radius: 6.85 * Doc Risk: 66.6667%)
- `alacritty/src/config/color.rs` -> **Severity: 370.3** (Blast Radius: 3.703 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
