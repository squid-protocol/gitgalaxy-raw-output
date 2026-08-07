# ARCHITECTURAL_BRIEF: alacritty
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/alacritty` |
| **Timestamp** | `2026-08-07T04:04:33.449681+00:00` |
| **Scan Duration** | `1.64s` |
| **Git Branch** | `master` |
| **Git Commit** | `f99dc71708d31d5c32d4b3fa611f9a87bf22657e` |
| **Git Remote** | `https://github.com/alacritty/alacritty.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 100 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 338 |
| Analyzed Artifacts (Scanned) | 259 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 79 |
| Total LOC | 21218 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 76.6% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7347 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6667 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 135 | 135 | 52.1% |
| RUST | 87 | 20074 | 33.6% |
| MARKDOWN | 8 | 0 | 3.1% |
| PLAINTEXT | 8 | 0 | 3.1% |
| XML | 8 | 0 | 3.1% |
| GLSL | 6 | 259 | 2.3% |
| SHELL | 6 | 679 | 2.3% |
| MAKEFILE | 1 | 71 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.28`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 125 | 48.3% |
| file_cluster_13 | 49 | 18.9% |
| file_cluster_16 | 12 | 4.6% |
| file_cluster_0 | 11 | 4.2% |
| file_cluster_12 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 45 | 17.4% |
| Static: Literature & Documentation | 16 | 6.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 79*

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
- `.rs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.manifest`: 1x Excluded (Unsupported Extension: '.manifest')
- `.rc`: 1x Excluded (Unsupported Extension: '.rc')
- `.wxs`: 1x Excluded (Unsupported Extension: '.wxs')
- `.rtf`: 1x Excluded (Unsupported Extension: '.rtf')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.9 | 8.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.8 | 13.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.8 | 0.0 | 0.0 |
| API Exposure | 0.0 | 8.5 | 1.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 24.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.7 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 43.5 | 6.7 | 6.7 |
| Instability Exposure | 0.0 | 6.0 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 46.3 | 1.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `extra/completions/alacritty.bash` (Hits: 40)
- `Makefile` (Hits: 10)
- `alacritty/src/window_context.rs` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **debug.rs** (`alacritty/src/config/debug.rs`) — 2 inbound connections
2. **ipc.rs** (`alacritty/src/polling/ipc.rs`) — 1 inbound connections
3. **platform.rs** (`alacritty/src/renderer/platform.rs`) — 1 inbound connections
4. **glsl3.rs** (`alacritty/src/renderer/text/glsl3.rs`) — 1 inbound connections
5. **serde_replace.rs** (`alacritty_config_derive/src/serde_replace.rs`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **event.rs** (`alacritty/src/event.rs`) — 99 outbound dependencies
2. **mod.rs** (`alacritty/src/display/mod.rs`) — 85 outbound dependencies
3. **mod.rs** (`alacritty/src/input/mod.rs`) — 73 outbound dependencies
4. **mod.rs** (`alacritty_terminal/src/term/mod.rs`) — 63 outbound dependencies
5. **ui_config.rs** (`alacritty/src/config/ui_config.rs`) — 52 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `new` (@ `alacritty/src/event.rs`) -> Impact: **387.3** | LOC: 1261
  * *Intent:* /// Create a new event processor.
- `_alacritty` (@ `extra/completions/alacritty.bash`) -> Impact: **358.6** | LOC: 525
- `spawn_new_instance` (@ `alacritty/src/event.rs`) -> Impact: **230.6** | LOC: 851
  * *Intent:* // SAFETY: The clipboard must be dropped before the event loop, so use the nop clipboard // as a safe placeholder.
- `box_drawing` (@ `alacritty/src/renderer/text/builtin_font.rs`) -> Impact: **192.2** | LOC: 724
- `process_renderer_update` (@ `alacritty/src/display/mod.rs`) -> Impact: **142.7** | LOC: 533
- `trigger_hint` (@ `alacritty/src/event.rs`) -> Impact: **128.2** | LOC: 555
- `migrate` (@ `alacritty/src/migrate/mod.rs`) -> Impact: **124.5** | LOC: 290
  * *Intent:* /// Handle migration.
- `powerline_drawing` (@ `alacritty/src/renderer/text/builtin_font.rs`) -> Impact: **106.9** | LOC: 260
- `deserialize` (@ `alacritty/src/config/bindings.rs`) -> Impact: **90.6** | LOC: 212
- `spawn` (@ `alacritty_terminal/src/event_loop.rs`) -> Impact: **80.0** | LOC: 120

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `alacritty/src` | 11 | 1923.9 | 11.22% | 45.83% |
| `alacritty/src/display` | 9 | 1887.14 | 14.54% | 91.0% |
| `alacritty_terminal/src/term` | 4 | 1691.9 | 14.23% | 96.64% |
| `alacritty/src/config` | 16 | 1375.64 | 4.13% | 56.87% |
| `alacritty/src/renderer/text` | 6 | 1068.84 | 16.05% | 53.28% |
| `alacritty/src/input` | 2 | 942.58 | 15.6% | 57.27% |
| `alacritty_terminal/src` | 8 | 937.84 | 13.36% | 47.87% |
| `extra/completions` | 2 | 768.18 | 53.37% | 43.78% |
| `alacritty_terminal/src/grid` | 5 | 541.38 | 18.78% | 62.53% |
| `alacritty/src/renderer` | 4 | 491.2 | 11.61% | 47.63% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `alacritty_terminal/src/grid/row.rs` -> **100.0%** Exposure
- `alacritty_terminal/src/index.rs` -> **100.0%** Exposure
- `alacritty_terminal/src/term/color.rs` -> **100.0%** Exposure
- `scripts/24-bit-color.sh` -> **100.0%** Exposure
- `scripts/colors.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `alacritty/src/config/mod.rs` -> **100.0%** Exposure
- `alacritty/src/config/serde_utils.rs` -> **100.0%** Exposure
- `extra/completions/alacritty.bash` -> **100.0%** Exposure
- `scripts/create-flamegraph.sh` -> **100.0%** Exposure
- `alacritty_terminal/src/tty/windows/conpty.rs` -> **99.9883%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `alacritty_terminal/src/term/mod.rs` -> **62** Orphaned Functions | **17** Duplicates
- `alacritty/src/config/bindings.rs` -> **21** Orphaned Functions | **27** Duplicates
- `alacritty_terminal/src/index.rs` -> **11** Orphaned Functions | **29** Duplicates
- `alacritty_terminal/src/term/search.rs` -> **35** Orphaned Functions | **2** Duplicates
- `alacritty/src/config/ui_config.rs` -> **9** Orphaned Functions | **11** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`alacritty/src/input/keyboard.rs`** -> AI Confidence: **99.31%**
2. **`alacritty_terminal/src/grid/resize.rs`** -> AI Confidence: **99.31%**
3. **`scripts/24-bit-color.sh`** -> AI Confidence: **99.29%**
4. **`scripts/colors.sh`** -> AI Confidence: **99.29%**
5. **`scripts/create-flamegraph.sh`** -> AI Confidence: **99.29%**
6. **`alacritty/src/config/cursor.rs`** -> AI Confidence: **99.24%**
7. **`alacritty/src/display/hint.rs`** -> AI Confidence: **99.24%**
8. **`alacritty/src/migrate/mod.rs`** -> AI Confidence: **99.24%**
9. **`alacritty/src/polling/mod.rs`** -> AI Confidence: **99.24%**
10. **`alacritty_config_derive/src/serde_replace.rs`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1678` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `alacritty_terminal/src/grid/row.rs` (RUST) -> Cumulative Risk: **524.07**
- **Archetype:** `file_cluster_16` (Distance: 12.12 IQR)
- **Magnitude:** 141.8 | **LOC:** 294 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.95%), Verification (80.0%)
- **Heaviest Functions:** `shrink` (Impact: 7.8), `reset` (Impact: 6.2), `new` (Impact: 5.0)

### 2. `scripts/24-bit-color.sh` (SHELL) -> Cumulative Risk: **514.61**
- **Archetype:** `file_cluster_8` (Distance: 11.373 IQR)
- **Magnitude:** 8.25 | **LOC:** 102 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (98.423%), Safety Score (97.8207%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 39.6), `Anonymous_Block` (Impact: 3.2), `Anonymous_Block` (Impact: 3.2)

### 3. `alacritty_terminal/src/tty/windows/child.rs` (RUST) -> Cumulative Risk: **506.45**
- **Archetype:** `file_cluster_13` (Distance: 13.435 IQR)
- **Magnitude:** 94.78 | **LOC:** 169 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7032%), Concurrency (99.145%), Tech Debt (64.5834%)
- **Heaviest Functions:** `child_exit_callback` (Impact: 9.6), `new` (Impact: 7.8), `event_is_emitted_when_child_exits` (Impact: 2.9)

### 4. `alacritty_terminal/src/event_loop.rs` (RUST) -> Cumulative Risk: **504.86**
- **Archetype:** `file_cluster_13` (Distance: 13.716 IQR)
- **Magnitude:** 348.16 | **LOC:** 487 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8912%), Concurrency (95.7938%), Tech Debt (57.8109%)
- **Heaviest Functions:** `spawn` (Impact: 80.0), `pty_read` (Impact: 58.0), `recv` (Impact: 10.5)

### 5. `scripts/create-flamegraph.sh` (SHELL) -> Cumulative Risk: **498.76**
- **Archetype:** `file_cluster_8` (Distance: 13.015 IQR)
- **Magnitude:** 3.69 | **LOC:** 32 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.701%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 17.8), `Anonymous_Block` (Impact: 6.2), `__global_context__` (Impact: 3.5)

### 6. `alacritty/src/renderer/text/glsl3.rs` (RUST) -> Cumulative Risk: **492.55**
- **Archetype:** `file_cluster_8` (Distance: 10.966 IQR)
- **Magnitude:** 155.86 | **LOC:** 463 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.6011%), Tech Debt (92.6132%), Verification (80.0%)
- **Heaviest Functions:** `new` (Impact: 10.4), `new` (Impact: 8.7), `render_batch` (Impact: 8.0)

### 7. `alacritty/src/display/content.rs` (RUST) -> Cumulative Risk: **490.04**
- **Archetype:** `file_cluster_13` (Distance: 12.765 IQR)
- **Magnitude:** 276.94 | **LOC:** 553 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8317%), Tech Debt (94.9134%), Verification (80.0%)
- **Heaviest Functions:** `new` (Impact: 34.2), `new` (Impact: 24.4), `next` (Impact: 17.2)

### 8. `alacritty_terminal/src/tty/windows/blocking.rs` (RUST) -> Cumulative Risk: **477.96**
- **Archetype:** `file_cluster_13` (Distance: 13.938 IQR)
- **Magnitude:** 175.52 | **LOC:** 277 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9987%), State Flux (99.9548%), Concurrency (85.8259%)
- **Heaviest Functions:** `new` (Impact: 16.3), `new` (Impact: 14.5), `register` (Impact: 11.6)

### 9. `alacritty/src/display/mod.rs` (RUST) -> Cumulative Risk: **472.55**
- **Archetype:** `file_cluster_13` (Distance: 12.788 IQR)
- **Magnitude:** 646.06 | **LOC:** 1635 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.347%), State Flux (95.2617%), Verification (80.0%)
- **Heaviest Functions:** `process_renderer_update` (Impact: 142.7), `draw_ime_preview` (Impact: 69.3), `update_highlighted_hints` (Impact: 43.1)

### 10. `alacritty/src/input/mod.rs` (RUST) -> Cumulative Risk: **468.65**
- **Archetype:** `file_cluster_13` (Distance: 12.267 IQR)
- **Magnitude:** 640.64 | **LOC:** 1560 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (88.5121%), Verification (80.0%), Tech Debt (64.0671%)
- **Heaviest Functions:** `scroll_terminal` (Impact: 68.3), `execute` (Impact: 47.0), `execute` (Impact: 45.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `alacritty/src/event.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.705 IQR)
- **Top Global Matches:** file_cluster_13: 13.705, file_cluster_0: 13.803, file_cluster_8: 13.986
- **Magnitude:** 1401.02 | **LOC:** 2094 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (22.7011%), Tech Debt (48.1033%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 387.3)
    * *Intent:* /// Create a new event processor.
  * `spawn_new_instance` (Impact: 230.6)
    * *Intent:* // SAFETY: The clipboard must be dropped before the event loop, so use the nop clipboard // as a saf...
  * `trigger_hint` (Impact: 128.2)
  * `inline_search` (Impact: 63.0)
  * `handle_event` (Impact: 55.8)
    * *Intent:* *index -= 1;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 293`, `args: 92`, `func_start: 65`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 176`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 56`, `import: 52`
* *Defense:* `safety: 150`, `doc: 87`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::cli::Options, ClipboardType, info, alacritty_terminal::index::Boundary, WindowEvent, crate::config::self, crate::display::hint::HintMatch, ahash::RandomState...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/term/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.838 IQR)
- **Top Global Matches:** file_cluster_0: 12.838, file_cluster_8: 12.893, file_cluster_13: 13.041
- **Magnitude:** 1244.8 | **LOC:** 3303 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.6285%), Tech Debt (86.5676%)
**Top Internal Functions/Classes:**
  * `line_to_string` (Impact: 47.2)
  * `input` (Impact: 33.3)
  * `clear_screen` (Impact: 19.1)
  * `put_tab` (Impact: 18.8)
  * `damage_public_usage` (Impact: 17.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 524`, `args: 164`, `func_start: 141`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 352`, `dead_code: 1`, `duplicate_logic: 17`, `orphaned_logic: 62`
* *Architecture:* `api: 52`, `import: 31`
* *Defense:* `safety: 121`, `doc: 182`, `test: 141`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::vte::ansi::
    self, crate::vi_mode::ViModeCursor, Attr, Range, alacritty_terminal::term::test::mock_term, Direction, ViMotion, base64::engine::general_purpose::STANDARD...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/completions/alacritty.bash` (SHELL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_12` (Drift: 15.344 IQR)
- **Top Global Matches:** file_cluster_12: 15.344, file_cluster_11: 15.413, file_cluster_8: 15.418
- **Magnitude:** 758.72 | **LOC:** 532 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9405%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_alacritty` (Impact: 358.6)
  * `Anonymous_Block` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 72`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 383`
* *Architecture:* `io: 40`
* *Defense:* `safety: 148`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.788 IQR)
- **Top Global Matches:** file_cluster_13: 12.788, file_cluster_0: 13.002, file_cluster_8: 13.049
- **Magnitude:** 646.06 | **LOC:** 1635 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.0475%), Tech Debt (97.347%)
**Top Internal Functions/Classes:**
  * `process_renderer_update` (Impact: 142.7)
  * `draw_ime_preview` (Impact: 69.3)
  * `update_highlighted_hints` (Impact: 43.1)
  * `new` (Impact: 40.4)
  * `handle_update` (Impact: 29.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 293`, `args: 65`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 117`, `fragile_debt: 2`, `duplicate_logic: 9`, `orphaned_logic: 9`
* *Architecture:* `api: 47`, `import: 47`
* *Defense:* `safety: 60`, `doc: 86`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` info, damage_y_to_viewport_y, crate::config::window::StartupMode, crate::string::ShortenDirection, crate::display::hint::HintMatch, std::mem::self, StrShortener, unicode_width::UnicodeWidthChar...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/input/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.267 IQR)
- **Top Global Matches:** file_cluster_13: 12.267, file_cluster_8: 12.298, file_cluster_0: 12.303
- **Magnitude:** 640.64 | **LOC:** 1560 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (22.3616%), Tech Debt (64.0671%)
**Top Internal Functions/Classes:**
  * `scroll_terminal` (Impact: 68.3)
  * `execute` (Impact: 47.0)
  * `execute` (Impact: 45.0)
  * `process_mouse_bindings` (Impact: 39.1)
  * `mouse_input` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 313`, `args: 102`, `func_start: 98`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 149`, `dead_code: 1`, `duplicate_logic: 10`, `orphaned_logic: 10`
* *Architecture:* `api: 22`, `import: 39`
* *Defense:* `safety: 63`, `doc: 31`, `test: 6`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::message_bar::MessageBuffer, alacritty_terminal::index::Boundary, std::ffi::OsStr, Direction, TouchPurpose, alacritty_terminal::term::search::Match, TimerId, WindowEvent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/text/builtin_font.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.78 IQR)
- **Top Global Matches:** file_cluster_8: 11.78, file_cluster_7: 12.162, file_cluster_13: 12.191
- **Magnitude:** 491.62 | **LOC:** 1033 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (14.7194%), Tech Debt (11.8261%)
**Top Internal Functions/Classes:**
  * `box_drawing` (Impact: 192.2)
  * `powerline_drawing` (Impact: 106.9)
  * `draw_rounded_corner` (Impact: 36.2)
  * `draw_line` (Impact: 35.2)
  * `builtin_glyph` (Impact: 8.6)
    * *Intent:* /// Returns the rasterized glyph if the character is part of the built-in font.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 173`, `args: 81`, `func_start: 11`
* *Risk/State:* `state_mutation: 79`, `orphaned_logic: 3`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 31`, `doc: 39`, `test: 7`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ops, mem, super::*, Metrics, crate::config::ui_config::Delta, crossfont::Metrics, RasterizedGlyph, std::cmp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/bindings.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.325 IQR)
- **Top Global Matches:** file_cluster_16: 12.325, file_cluster_8: 12.374, file_cluster_0: 12.409
- **Magnitude:** 418.92 | **LOC:** 1453 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.0033%), Tech Debt (99.5789%)
**Top Internal Functions/Classes:**
  * `deserialize` (Impact: 90.6)
  * `visit_map` (Impact: 69.8)
  * `deserialize` (Impact: 12.8)
  * `deserialize` (Impact: 10.2)
  * `deserialize` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 200`, `args: 55`, `func_start: 54`, `class_start: 17`
* *Risk/State:* `state_mutation: 34`, `dead_code: 1`, `duplicate_logic: 27`, `orphaned_logic: 21`
* *Architecture:* `api: 23`, `import: 16`
* *Defense:* `safety: 174`, `doc: 107`, `test: 51`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ModifiersState, winit::event::MouseButton, winit::keyboard::
    Key, PhysicalKey, winit::keyboard::ModifiersState, NamedKey, serde::Deserialize, Unexpected...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/hint.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.586 IQR)
- **Top Global Matches:** file_cluster_13: 13.586, file_cluster_16: 13.638, file_cluster_0: 13.724
- **Magnitude:** 368.5 | **LOC:** 704 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.9175%), Tech Debt (87.1217%)
**Top Internal Functions/Classes:**
  * `hint_post_processing` (Impact: 37.5)
    * *Intent:* /// Apply some hint post processing heuristics. /// /// This will check the end of the hint and make...
  * `update_matches` (Impact: 21.9)
    * *Intent:* /// Update the visible hint matches and key labels.
  * `visible_unique_hyperlinks_iter` (Impact: 21.8)
  * `highlighted_at` (Impact: 21.3)
  * `keyboard_input` (Impact: 20.1)
    * *Intent:* /// Handle keyboard input during hint selection.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 154`, `args: 53`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 86`, `dead_code: 1`, `duplicate_logic: 5`, `orphaned_logic: 10`
* *Architecture:* `api: 19`, `import: 18`
* *Defense:* `safety: 86`, `doc: 64`, `test: 40`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::config::UiConfig, alacritty_terminal::term::test::mock_term, alacritty_terminal::index::Boundary, Direction, alacritty_terminal::term::search::Match, std::iter, winit::keyboard::ModifiersState, Column...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/term/search.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.867 IQR)
- **Top Global Matches:** file_cluster_0: 12.867, file_cluster_13: 13.183, file_cluster_11: 13.35
- **Magnitude:** 355.46 | **LOC:** 1252 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.8712%), Tech Debt (99.9842%)
**Top Internal Functions/Classes:**
  * `next_match_left` (Impact: 34.9)
  * `skip_fullwidth` (Impact: 21.8)
  * `next` (Impact: 19.1)
  * `new` (Impact: 10.9)
    * *Intent:* /// Build the forward and backward search DFAs.
  * `end_on_fullwidth` (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 386`, `args: 45`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 149`, `dead_code: 4`, `fragile_debt: 7`, `duplicate_logic: 2`, `orphaned_logic: 35`
* *Architecture:* `api: 6`, `import: 18`
* *Defense:* `safety: 84`, `doc: 31`, `test: 87`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` regex_automata::Anchored, Direction, Config, Column, std::mem, MatchKind, Dimensions, crate::grid::BidirectionalIterator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/event_loop.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.716 IQR)
- **Top Global Matches:** file_cluster_13: 13.716, file_cluster_0: 13.782, file_cluster_4: 13.855
- **Magnitude:** 348.16 | **LOC:** 487 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.4491%), Tech Debt (57.8109%)
**Top Internal Functions/Classes:**
  * `spawn` (Impact: 80.0)
  * `pty_read` (Impact: 58.0)
  * `recv` (Impact: 10.5)
  * `new` (Impact: 6.3)
    * *Intent:* /// Create a new event loop.
  * `drain_recv_channel` (Impact: 5.7)
    * *Intent:* /// Drain the channel. /// /// Returns `false` when a shutdown message was received.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 109`, `args: 24`, `func_start: 22`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 91`, `duplicate_logic: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 3`, `api: 12`, `concurrency: 30`, `import: 17`
* *Defense:* `safety: 69`, `doc: 22`, `sync_locks: 3`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TryRecvError, std::time::Instant, std::thread::JoinHandle, crate::sync::FairMutex, vte::ansi, Write, crate::term::Term, Poller...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/input/keyboard.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.092 IQR)
- **Top Global Matches:** file_cluster_13: 12.092, file_cluster_0: 12.185, file_cluster_8: 12.245
- **Magnitude:** 301.94 | **LOC:** 719 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (8.8337%), Tech Debt (50.4723%)
**Top Internal Functions/Classes:**
  * `key_release` (Impact: 74.7)
  * `build_sequence` (Impact: 43.5)
    * *Intent:* // Match `Alt` bindings without `Alt` being applied, otherwise they use the // composed chars, which...
  * `process_key_bindings` (Impact: 32.9)
  * `should_build_sequence` (Impact: 23.5)
  * `alt_send_esc` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 82`, `args: 30`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`, `dead_code: 3`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `safety: 37`, `doc: 30`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ModifiersState, NamedKey, alacritty_terminal::event::EventListener, winit::platform::modifier_supplement::KeyEventExtModifierSupplement, winit::keyboard::Key, winit::event::ElementState, alacritty_terminal::term::TermMode, Processor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/migrate/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.245 IQR)
- **Top Global Matches:** file_cluster_13: 13.245, file_cluster_8: 13.39, file_cluster_0: 13.449
- **Magnitude:** 294.84 | **LOC:** 335 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.0893%), Tech Debt (16.8108%)
**Top Internal Functions/Classes:**
  * `migrate` (Impact: 124.5)
    * *Intent:* /// Handle migration.
  * `migrate_imports` (Impact: 28.9)
  * `move_value` (Impact: 24.6)
  * `migrate_toml` (Impact: 21.3)
  * `write_results` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 67`, `args: 19`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 52`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 46`, `doc: 12`, `test: 5`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::cli::MigrateOptions, tempfile::NamedTempFile, mem, super::*, std::fs, Item, std::fmt::Debug, toml_edit::DocumentMut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/selection.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.632 IQR)
- **Top Global Matches:** file_cluster_0: 12.632, file_cluster_13: 12.632, file_cluster_8: 12.731
- **Magnitude:** 284.34 | **LOC:** 669 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.6556%), Tech Debt (96.6668%)
**Top Internal Functions/Classes:**
  * `contains_cell` (Impact: 45.9)
    * *Intent:* /// Check if the cell at a point is part of the selection.
  * `range_simple` (Impact: 23.7)
  * `range_block` (Impact: 17.1)
  * `range_semantic` (Impact: 15.0)
  * `contains` (Impact: 14.2)
    * *Intent:* /// Check if a point lies within the selection.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 100`, `args: 36`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 73`, `duplicate_logic: 2`, `orphaned_logic: 18`
* *Architecture:* `api: 10`, `import: 12`
* *Defense:* `safety: 18`, `doc: 83`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GridCell, Range, Column, std::mem, crate::term::Term, Flags, std::ops::Bound, crate::index::Boundary...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/content.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.765 IQR)
- **Top Global Matches:** file_cluster_13: 12.765, file_cluster_16: 12.832, file_cluster_8: 13.021
- **Magnitude:** 276.94 | **LOC:** 553 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.2546%), Tech Debt (94.9134%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 34.2)
    * *Intent:* /// Extra storage with rarely present fields for [`RenderableCell`], to reduce the cell size we /// ...
  * `new` (Impact: 24.4)
  * `next` (Impact: 17.2)
  * `renderable_cursor` (Impact: 15.8)
  * `advance` (Impact: 12.7)
    * *Intent:* /// Advance the hint iterator. /// /// If the point is within a hint, the keyboard shortcut characte...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 121`, `args: 37`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 85`, `duplicate_logic: 8`, `orphaned_logic: 1`
* *Architecture:* `api: 23`, `import: 17`
* *Defense:* `safety: 26`, `doc: 45`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::config::UiConfig, alacritty_terminal::term::search::Match, RenderableContent, crate::display::hint::self, alacritty_terminal::event::EventListener, Flags, List, crate::display::color::CellRgb...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.071 IQR)
- **Top Global Matches:** file_cluster_13: 13.071, file_cluster_0: 13.228, file_cluster_16: 13.296
- **Magnitude:** 258.6 | **LOC:** 454 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.3742%), Tech Debt (96.3549%)
**Top Internal Functions/Classes:**
  * `load_imports` (Impact: 26.5)
  * `imports` (Impact: 19.7)
  * `deserialize_config` (Impact: 16.8)
  * `installed_config` (Impact: 13.3)
  * `load` (Impact: 12.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 113`, `args: 37`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 61`, `duplicate_logic: 7`, `orphaned_logic: 3`
* *Architecture:* `api: 26`, `import: 16`
* *Defense:* `safety: 60`, `doc: 27`, `test: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::cli::Options, error, info, serde::Deserialize, ViAction, warn, std::env, toml::de::Error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/ui_config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.84 IQR)
- **Top Global Matches:** file_cluster_13: 12.84, file_cluster_0: 12.853, file_cluster_16: 12.874
- **Magnitude:** 242.28 | **LOC:** 738 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2229%), Tech Debt (99.0723%)
**Top Internal Functions/Classes:**
  * `deserialize` (Impact: 20.9)
  * `visit_map` (Impact: 15.9)
  * `deserialize_bindings` (Impact: 11.6)
    * *Intent:* /// Shell startup directory.
  * `compiled` (Impact: 11.2)
  * `deserialize` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 129`, `args: 32`, `func_start: 28`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 37`, `duplicate_logic: 11`, `orphaned_logic: 9`
* *Architecture:* `api: 53`, `import: 34`
* *Defense:* `safety: 78`, `doc: 67`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Shell, std::cell::OnceCell, ModifiersState, Action, alacritty_terminal::term::test::mock_term, crate::config::color::Colors, serde::Deserialize, std::mem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/window.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.77 IQR)
- **Top Global Matches:** file_cluster_0: 11.77, file_cluster_13: 11.955, file_cluster_8: 12.09
- **Magnitude:** 221.8 | **LOC:** 538 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.185%), Tech Debt (66.0283%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 19.1)
    * *Intent:* /// Create a new window. /// /// This creates a window and fully initializes a window.
  * `get_platform_window` (Impact: 8.1)
  * `get_platform_window` (Impact: 5.7)
  * `set_fullscreen` (Impact: 5.5)
  * `set_urgent` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 68`, `args: 44`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 25`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 54`, `import: 18`
* *Defense:* `safety: 39`, `doc: 37`, `test: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::config::UiConfig, objc2::MainThreadMarker, WindowAttributesExtStartupNotify, NSView, ImePurpose, winit::raw_window_handle::HasWindowHandle, png::Decoder, winit::dpi::PhysicalPosition...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.181 IQR)
- **Top Global Matches:** file_cluster_13: 12.181, file_cluster_8: 12.483, file_cluster_16: 12.527
- **Magnitude:** 202.0 | **LOC:** 401 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.8878%), Tech Debt (62.9554%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 34.9)
    * *Intent:* /// Create a new renderer. /// /// This will automatically pick between the GLES2 and GLSL3 renderer...
  * `draw_string` (Impact: 16.8)
    * *Intent:* /// Draw a string in a variable location. Used for printing the render timer, warnings and /// error...
  * `was_context_reset` (Impact: 9.8)
    * *Intent:* /// Get the context reset status.
  * `supports_robustness` (Impact: 9.6)
  * `load_extensions` (Impact: 8.0)
    * *Intent:* /// Load available OpenGL extensions.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 86`, `args: 22`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 16`, `import: 25`
* *Defense:* `safety: 30`, `doc: 19`, `sync_locks: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Ordering, alacritty_terminal::term::cell::Flags, info, CString, text::Gles2Renderer, PossiblyCurrentContext, glutin::display::GetGlDisplay, ahash::RandomState...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/tty/windows/blocking.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.938 IQR)
- **Top Global Matches:** file_cluster_13: 13.938, file_cluster_4: 14.016, file_cluster_16: 14.071
- **Magnitude:** 175.52 | **LOC:** 277 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.3994%), Tech Debt (99.9987%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 16.3)
  * `new` (Impact: 14.5)
  * `register` (Impact: 11.6)
  * `wake_by_ref` (Impact: 10.9)
  * `register` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 69`, `args: 17`, `func_start: 15`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 51`, `duplicate_logic: 10`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 24`, `import: 10`
* *Defense:* `safety: 49`, `doc: 21`, `sync_locks: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Mutex, piper::Reader, Poll, polling::os::iocp::CompletionPacket, std::io::prelude::*, std::marker::PhantomData, Wake, Poller...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/tty/unix.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.571 IQR)
- **Top Global Matches:** file_cluster_13: 12.571, file_cluster_0: 12.856, file_cluster_8: 13.06
- **Magnitude:** 170.82 | **LOC:** 449 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (16.3332%), Tech Debt (99.8724%)
**Top Internal Functions/Classes:**
  * `from_fd` (Impact: 44.1)
    * *Intent:* // Since we use -l, `login` will not change directory to the user's home. However, // `login` only c...
  * `default_shell_command` (Impact: 40.8)
  * `from_env` (Impact: 13.6)
    * *Intent:* /// look for shell, username, longname, and home dir in the respective environment variables /// bef...
  * `get_pw_entry` (Impact: 8.9)
    * *Intent:* /// Return a Passwd struct with pointers into the provided buf. /// /// # Unsafety /// /// If `buf` ...
  * `set_controlling_terminal` (Impact: 6.6)
    * *Intent:* /// Really only needed on BSD, but should be fine elsewhere.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 94`, `args: 14`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 28`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 1`, `import: 25`
* *Defense:* `safety: 43`, `doc: 18`, `test: 3`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CString, std::os::unix::net::UnixStream, crate::tty::ChildEvent, rustix_openpty::rustix::termios::self, Options, std::mem::MaybeUninit, unregister, crate::event::OnResize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/color.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.71 IQR)
- **Top Global Matches:** file_cluster_16: 11.71, file_cluster_0: 11.781, file_cluster_13: 11.799
- **Magnitude:** 163.18 | **LOC:** 369 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.204%), Tech Debt (99.937%)
**Top Internal Functions/Classes:**
  * `fill_cube` (Impact: 23.8)
  * `from_str` (Impact: 17.1)
  * `deserialize` (Impact: 10.2)
  * `fill_gray_ramp` (Impact: 9.8)
  * `deserialize` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 83`, `args: 29`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `state_mutation: 26`, `duplicate_logic: 12`
* *Architecture:* `api: 14`, `import: 10`
* *Defense:* `safety: 31`, `doc: 4`, `test: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::config::color::Colors, std::str::FromStr, serde::Deserialize, log::trace, alacritty_terminal::term::color::COUNT, std::ops::Add, Display, alacritty_terminal::vte::ansi::NamedColor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/text/glsl3.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.966 IQR)
- **Top Global Matches:** file_cluster_8: 10.966, file_cluster_13: 10.972, file_cluster_16: 10.994
- **Magnitude:** 155.86 | **LOC:** 463 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.2807%), Tech Debt (92.6132%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 10.4)
  * `new` (Impact: 8.7)
  * `render_batch` (Impact: 8.0)
  * `add_item` (Impact: 6.2)
  * `drop` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 78`, `args: 24`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `state_mutation: 53`, `duplicate_logic: 7`
* *Architecture:* `api: 17`, `import: 13`
* *Defense:* `safety: 6`, `doc: 10`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.963
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003876
  * `Imports (Out-Degree: 0):` alacritty_terminal::term::cell::Flags, std::mem::size_of, crate::renderer::Error, ShaderVersion, super::atlas::ATLAS_SIZE, TextShader, TextRenderer, Atlas...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `alacritty/src/renderer/rects.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.008 IQR)
- **Top Global Matches:** file_cluster_13: 12.008, file_cluster_0: 12.141, file_cluster_8: 12.189
- **Magnitude:** 152.58 | **LOC:** 497 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.765%), Tech Debt (99.8934%)
**Top Internal Functions/Classes:**
  * `update_flag` (Impact: 19.4)
  * `update_uniforms` (Impact: 17.6)
  * `draw` (Impact: 13.7)
  * `create_rect` (Impact: 7.7)
    * *Intent:* /// Push all rects required to draw the cell's line.
  * `new` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 83`, `args: 16`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `state_mutation: 37`, `fragile_debt: 1`, `duplicate_logic: 5`, `orphaned_logic: 4`
* *Architecture:* `api: 23`, `import: 14`
* *Defense:* `safety: 32`, `doc: 15`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alacritty_terminal::term::cell::Flags, crate::renderer::shader::ShaderError, alacritty_terminal::index::Column, std::collections::HashMap, log::info, crate::display::content::RenderableCell, renderer, crate::gl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/grid/row.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.12 IQR)
- **Top Global Matches:** file_cluster_16: 12.12, file_cluster_0: 12.208, file_cluster_13: 12.421
- **Magnitude:** 141.8 | **LOC:** 294 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.7297%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `shrink` (Impact: 7.8)
    * *Intent:* /// Reduce the number of columns in the row. /// /// This will return all non-empty cells that were ...
  * `reset` (Impact: 6.2)
    * *Intent:* /// Reset all cells in the row to the `template` cell.
  * `new` (Impact: 5.0)
    * *Intent:* /// Create a new terminal row. /// /// Ideally the `template` should be `Copy` in all performance se...
  * `grow` (Impact: 3.9)
    * *Intent:* /// Increase the number of columns in the row.
  * `last_mut` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 85`, `args: 29`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 55`, `duplicate_logic: 14`, `orphaned_logic: 6`
* *Architecture:* `api: 14`, `import: 7`
* *Defense:* `safety: 6`, `doc: 15`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::ops::Index, Serialize, Range, serde::Deserialize, min, RangeFull, RangeToInclusive, crate::grid::GridCell...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/index.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.593 IQR)
- **Top Global Matches:** file_cluster_0: 10.593, file_cluster_8: 10.752, file_cluster_16: 10.76
- **Magnitude:** 139.98 | **LOC:** 468 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8732%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `grid_clamp` (Impact: 11.2)
  * `grid_clamp` (Impact: 9.2)
  * `opposite` (Impact: 3.8)
  * `cmp` (Impact: 3.7)
  * `sub` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 107`, `args: 42`, `func_start: 42`, `class_start: 5`
* *Risk/State:* `state_mutation: 11`, `duplicate_logic: 29`, `orphaned_logic: 11`
* *Architecture:* `api: 16`, `import: 6`
* *Defense:* `safety: 16`, `doc: 21`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ordering, max, Serialize, std::ops::Add, super::*, min, AddAssign, std::fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `alacritty_terminal/src/selection.rs` (RUST) | Magnitude: 284.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 369, structural_boundaries: 100, doc: 83, state_mutation: 73
- `alacritty/src/config/window.rs` (RUST) | Magnitude: 134.28 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 185, structural_boundaries: 44, api: 39, safety: 34
- `alacritty_terminal/src/term/mod.rs` (RUST) | Magnitude: 1244.8 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2318, structural_boundaries: 524, state_mutation: 352, branch: 234
- `alacritty/src/daemon.rs` (RUST) | Magnitude: 65.46 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 37, state_mutation: 19, decorators: 19
- `alacritty_terminal/src/term/cell.rs` (RUST) | Magnitude: 72.42 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 111, structural_boundaries: 34, generics: 26, safety: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `extra/completions/alacritty.bash` (SHELL) | Magnitude: 758.72 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 441, state_mutation: 383, branch: 241, safety: 148

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `alacritty/src/config/general.rs` (RUST) | Magnitude: 7.52 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 13, doc: 12, structural_boundaries: 5, api: 5
- `alacritty/src/config/ui_config.rs` (RUST) | Magnitude: 242.28 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 380, structural_boundaries: 129, generics: 89, safety: 78
- `alacritty/src/display/damage.rs` (RUST) | Magnitude: 110.56 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 73, state_mutation: 34, doc: 27
- `alacritty/src/config/terminal.rs` (RUST) | Magnitude: 9.72 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, generics: 7, api: 5
- `alacritty/src/input/mod.rs` (RUST) | Magnitude: 640.64 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1077, structural_boundaries: 313, state_mutation: 149, branch: 112

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `alacritty/src/config/font.rs` (RUST) | Magnitude: 9.32 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, doc: 21, structural_boundaries: 12, generics: 11
- `alacritty_terminal/src/term/color.rs` (RUST) | Magnitude: 19.22 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, doc: 14, generics: 10
- `alacritty/src/config/bindings.rs` (RUST) | Magnitude: 418.92 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 998, structural_boundaries: 200, safety: 174, generics: 140
- `alacritty/src/config/mouse.rs` (RUST) | Magnitude: 12.7 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, generics: 8, api: 6
- `alacritty/src/display/color.rs` (RUST) | Magnitude: 163.18 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 248, structural_boundaries: 83, generics: 50, branch: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `alacritty/src/renderer/text/glsl3.rs` (RUST) | Magnitude: 155.86 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 295, structural_boundaries: 78, state_mutation: 53, generics: 35
- `alacritty/src/config/bell.rs` (RUST) | Magnitude: 10.82 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, api: 6, doc: 6
- `alacritty/src/config/cursor.rs` (RUST) | Magnitude: 53.6 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 18, decorators: 14, api: 13
- `alacritty/src/panic.rs` (RUST) | Magnitude: 4.8 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, import: 4, args: 2
- `alacritty/src/config/serde_utils.rs` (RUST) | Magnitude: 34.9 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 31, state_mutation: 15, test: 11

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `alacritty/src/display/mod.rs` -> **skewb1k** (100.0% isolated ownership) | Magnitude: 646.06
- `alacritty/src/config/bindings.rs` -> **Jonas** (100.0% isolated ownership) | Magnitude: 418.92
- `alacritty/src/config/mod.rs` -> **Jonas** (100.0% isolated ownership) | Magnitude: 258.6
- `alacritty/src/polling/ipc.rs` -> **Christian Duerr** (100.0% isolated ownership) | Magnitude: 115.76
- `alacritty_terminal/src/tty/windows/child.rs` -> **Smit Barmase** (100.0% isolated ownership) | Magnitude: 94.78

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `alacritty/src/renderer/platform.rs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 56.1452%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `alacritty_terminal/src/thread.rs` -> **Severity: 0.31** (Embedded: 0.0039 * Error Risk: 80.0%)
- `alacritty/src/renderer/text/glsl3.rs` -> **Severity: 0.253** (Embedded: 0.0039 * Error Risk: 65.3819%)
- `alacritty/src/renderer/platform.rs` -> **Severity: 0.092** (Embedded: 0.0039 * Error Risk: 23.6994%)
- `alacritty_config_derive/src/serde_replace.rs` -> **Severity: 0.082** (Embedded: 0.0039 * Error Risk: 21.1415%)
- `alacritty/src/polling/ipc.rs` -> **Severity: 0.046** (Embedded: 0.0039 * Error Risk: 11.8946%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `alacritty/src/config/debug.rs` -> **Severity: 1193.742** (Blast Radius: 12.888 * Doc Risk: 92.6243%)
- `alacritty/src/renderer/platform.rs` -> **Severity: 386.435** (Blast Radius: 6.963 * Doc Risk: 55.4983%)
- `alacritty/src/display/window.rs` -> **Severity: 376.4** (Blast Radius: 3.764 * Doc Risk: 100.0%)
- `alacritty/src/polling/signal.rs` -> **Severity: 376.4** (Blast Radius: 3.764 * Doc Risk: 100.0%)
- `alacritty_terminal/src/lib.rs` -> **Severity: 376.398** (Blast Radius: 3.764 * Doc Risk: 99.9994%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
