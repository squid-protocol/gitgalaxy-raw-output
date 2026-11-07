# ARCHITECTURAL_BRIEF: RaspberryPi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/PeterLemon/RaspberryPi.git` |
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
- **Scope:** 604 analyzed artifact(s), 244540 LOC.
- **Load-bearing artifact:** `LIB/FASMARM.INC` -- 172 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `EMU/GameBoy/kernel.asm` -- pulls in 6 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `EMU/GameBoy/CPU.ASM` at magnitude 1435.84 (structural weight, not risk).
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
| Total Artifacts | 959 |
| Analyzed Artifacts (Scanned) | 604 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 355 |
| Total LOC | 244540 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 63.0% |
| Dominant Lang | ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2841 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3115 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 599 | 244540 | 99.2% |
| MARKDOWN | 4 | 0 | 0.7% |
| PLAINTEXT | 1 | 0 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 604 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 56%, Large Core Modules 27%, Large Core Modules (3) 7%, Parameter Forwarders Files 6%, State Mutators Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 599 | 99.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 355*

**Composition by Extension & Reason:**
- `.img`: 255x Excluded (Unsupported Extension: '.img')
- `.bin`: 69x Excluded (Unsupported Extension: '.bin')
- `.gb`: 13x Excluded (Unsupported Extension: '.gb')
- `.asm`: 8x Excluded (Embedded Array/Matrix Payload: 5323 commas in 957 LOC)
- `.lz`: 3x Excluded (Unsupported Extension: '.lz')
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.huff`: 2x Excluded (Unsupported Extension: '.huff')
- `.bmp`: 1x Excluded (Explicitly Denied Extension: '.bmp')
- `.inc`: 1x Zero-Density Threshold (LOC: 76, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 55.7 | 18.4 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.2 | 35.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 81.8 | 14.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 4.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 39.0 | 0.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.1 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 0 | 0 | 0 | - |
| guards | 0 | 0 | 0 | - |
| danger | 0 | 0 | 0 | - |
| concurrency | 504 | 252 | 2 | `Compress/HUFFMAN/HUFFMANDecode/LIB/R_PI.INC` |
| connectivity | 10 | 2 | 0 | `EMU/GameBoy/IOPORT.ASM` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 26 | 5 | 0 | `SMP/SMPINIT/kernel7.asm` |
| mutation | 307947 | 423 | 1534 | `Compress/HUFFMAN/HUFFMANDecode/LIB/R_PI.INC` |
| dead_code | 818 | 256 | 5 | `SMP/SMPINIT/kernel7.asm` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 106 | 4 | 0 | `VFP/Fractal/Julia/Double/kernel8.asm` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Compress/HUFFMAN/HUFFMANDecode/kernel.asm` (Hits: 0)
- `Compress/HUFFMAN/HUFFMANDecode/kernel7.asm` (Hits: 0)
- `Compress/HUFFMAN/HUFFMANDecode/kernel8.asm` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **FASMARM.INC** (`LIB/FASMARM.INC`) — 172 inbound connections
2. **R_PI2.INC** (`LIB/R_PI2.INC`) — 171 inbound connections
3. **V3D.INC** (`LIB/V3D.INC`) — 117 inbound connections
4. **CONTROL_LIST.INC** (`LIB/CONTROL_LIST.INC`) — 114 inbound connections
5. **R_PI.INC** (`LIB/R_PI.INC`) — 84 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **kernel.asm** (`EMU/GameBoy/kernel.asm`) — 6 outbound dependencies
2. **kernel.asm** (`V3D/ControlList/Clear_Color/kernel.asm`) — 4 outbound dependencies
3. **kernel7.asm** (`V3D/ControlList/Clear_Color/kernel7.asm`) — 4 outbound dependencies
4. **kernel.asm** (`V3D/ControlList/Multi_Sample/kernel.asm`) — 4 outbound dependencies
5. **kernel7.asm** (`V3D/ControlList/Multi_Sample/kernel7.asm`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `FB_Init` **(Many-Argument Workhorses)** (@ `V3D/V3DINIT/kernel8.asm`) -> Impact: **117.0** | LOC: 2243
- `FB_Init` **(Many-Argument Workhorses)** (@ `V3D/V3DINIT/kernel.asm`) -> Impact: **110.1** | LOC: 2105
- `FB_Init` **(Many-Argument Workhorses)** (@ `V3D/V3DINIT/kernel7.asm`) -> Impact: **110.1** | LOC: 2105
- `FB_Init` **(Many-Argument Workhorses)** (@ `TagsChannel/kernel8.asm`) -> Impact: **23.5** | LOC: 389
- `FB_Init` **(Many-Argument Workhorses)** (@ `TagsChannel/kernel.asm`) -> Impact: **17.7** | LOC: 284
- `FB_Init` **(Many-Argument Workhorses)** (@ `TagsChannel/kernel7.asm`) -> Impact: **17.7** | LOC: 284
- `LoopInputData` **(Many-Argument Workhorses)** (@ `Input/SNES/Mouse/GFXDemo/kernel7.asm`) -> Impact: **15.6** | LOC: 43
- `HuffByteLoop` **(Many-Argument Workhorses)** (@ `Compress/HUFFMAN/HUFFMANDecode/kernel.asm`) -> Impact: **14.0** | LOC: 28
- `HuffByteLoop` **(Many-Argument Workhorses)** (@ `Compress/HUFFMAN/HUFFMANDecode/kernel7.asm`) -> Impact: **14.0** | LOC: 28
- `HuffByteLoop` **(Many-Argument Workhorses)** (@ `Compress/HUFFMAN/HUFFMANGFX/kernel.asm`) -> Impact: **14.0** | LOC: 28

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `LIB` | 5 | 2250.86 | 20.26% | 0.0% |
| `V3D/ControlList/Clear_Color/LIB` | 5 | 2250.86 | 20.26% | 0.0% |
| `V3D/ControlList/Multi_Sample/LIB` | 5 | 2250.86 | 20.26% | 0.0% |
| `V3D/ControlList/NV/Indexed_List/Line/FillColor/LIB` | 5 | 2250.86 | 22.28% | 0.0% |
| `V3D/ControlList/NV/Indexed_List/Line/VertexColor/LIB` | 5 | 2250.86 | 22.28% | 0.0% |
| `V3D/ControlList/NV/Indexed_List/Line_Loop/FillColor/LIB` | 5 | 2250.86 | 22.28% | 0.0% |
| `V3D/ControlList/NV/Indexed_List/Line_Loop/VertexColor/LIB` | 5 | 2250.86 | 22.28% | 0.0% |
| `V3D/ControlList/NV/Indexed_List/Line_Strip/FillColor/LIB` | 5 | 2250.86 | 22.28% | 0.0% |
| `V3D/ControlList/NV/Indexed_List/Line_Strip/VertexColor/LIB` | 5 | 2250.86 | 22.28% | 0.0% |
| `V3D/ControlList/NV/Indexed_List/Point/FillColor/LIB` | 5 | 2250.86 | 22.28% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `SMP/SMPINIT/kernel7.asm` -> **81.8458%** Exposure
- `Compress/HUFFMAN/HUFFMANDecode/kernel.asm` -> **81.7574%** Exposure
- `Compress/LZ77/LZ77Decode/kernel.asm` -> **81.7574%** Exposure
- `Compress/LZ77/LZ77Decode/kernel8.asm` -> **81.7574%** Exposure
- `Compress/LZ77/LZ77Decode/kernel7.asm` -> **80.5584%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Compress/HUFFMAN/HUFFMANDecode/LIB/R_PI.INC` -> **100.0%** Exposure
- `Compress/HUFFMAN/HUFFMANDecode/LIB/R_PI2.INC` -> **100.0%** Exposure
- `Compress/HUFFMAN/HUFFMANGFX/LIB/R_PI.INC` -> **100.0%** Exposure
- `Compress/HUFFMAN/HUFFMANGFX/LIB/R_PI2.INC` -> **100.0%** Exposure
- `Compress/LZ77/LZ77Decode/LIB/R_PI.INC` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `TagsChannel/kernel8.asm` -> **2** Orphaned Functions | **6** Duplicates
- `Video/GRBLZVideo/kernel.asm` -> **6** Orphaned Functions | **0** Duplicates
- `Video/GRBLZVideo/kernel7.asm` -> **6** Orphaned Functions | **0** Duplicates
- `SMP/SMPINIT/kernel7.asm` -> **5** Orphaned Functions | **0** Duplicates
- `SMP/SMPINIT/kernel8.asm` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `668` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `EMU/GameBoy/CPU.ASM` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 11.019)
- **Top Global Matches:** file_cluster_15: 11.019, file_cluster_16: 12.116, file_cluster_11: 12.414
- **Magnitude:** 1435.84 | **LOC:** 5159 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (4.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HEX27` **(Parameter Forwarders)** (Impact: 6.5)
  * `HEX88` **(Many-Argument Workhorses)** (Impact: 4.1)
  * `HEX89` **(Many-Argument Workhorses)** (Impact: 4.1)
  * `HEX8A` **(Many-Argument Workhorses)** (Impact: 4.1)
  * `HEX8B` **(Many-Argument Workhorses)** (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 1654`, `args: 4499`, `func_start: 516`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Compress/HUFFMAN/HUFFMANDecode/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Compress/HUFFMAN/HUFFMANDecode/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Compress/HUFFMAN/HUFFMANGFX/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Compress/HUFFMAN/HUFFMANGFX/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Compress/LZ77/LZ77Decode/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Compress/LZ77/LZ77Decode/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Compress/LZ77/LZ77GFX/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Compress/LZ77/LZ77GFX/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `EMU/GameBoy/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HelloWorld/CPU/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HelloWorld/CPU/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HelloWorld/DMA/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HelloWorld/DMA/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (50.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/GFXDemo/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/TextDemo/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/NES/Controller/TextDemo/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/GFXDemo/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/TextDemo/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Controller/TextDemo/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Mouse/GFXDemo/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Mouse/GFXDemo/LIB/R_PI2.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Input/SNES/Mouse/TextDemo/LIB/R_PI.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.288)
- **Top Global Matches:** file_cluster_2: 3.288, file_cluster_17: 5.374, file_cluster_15: 6.306
- **Magnitude:** 833.56 | **LOC:** 822 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (55.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 76`
* *Risk/State:* `state_mutation: 767`
* *Architecture:* None
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Sound/PWM/12Bit/44100Hz/Mono/CPU/kernel8.asm` (ASSEMBLY) | Magnitude: 15.5 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 54, structural_boundaries: 27, indent_spaces: 17, pointers: 9
- `Sound/PWM/12Bit/48000Hz/Mono/CPU/kernel8.asm` (ASSEMBLY) | Magnitude: 15.5 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 54, structural_boundaries: 27, indent_spaces: 17, pointers: 9
- `Sound/PWM/8BIT/44100Hz/Mono/CPU/kernel8.asm` (ASSEMBLY) | Magnitude: 15.5 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 54, structural_boundaries: 27, indent_spaces: 17, pointers: 9
- `Sound/PWM/8BIT/48000Hz/Mono/CPU/kernel8.asm` (ASSEMBLY) | Magnitude: 15.5 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 54, structural_boundaries: 27, indent_spaces: 17, pointers: 9
- `Sound/PWM/13Bit/44100Hz/Mono/CPU/kernel8.asm` (ASSEMBLY) | Magnitude: 15.62 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 56, structural_boundaries: 27, indent_spaces: 18, pointers: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `LIB/R_PI2.INC` -> **Severity: 24.974** (Embedded: 0.2831 * Error Risk: 88.2107%)
- `LIB/V3D.INC` -> **Severity: 15.872** (Embedded: 0.1937 * Error Risk: 81.9352%)
- `LIB/CONTROL_LIST.INC` -> **Severity: 13.392** (Embedded: 0.1887 * Error Risk: 70.956%)
- `LIB/R_PI.INC` -> **Severity: 12.268** (Embedded: 0.1391 * Error Risk: 88.2107%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Compress/HUFFMAN/HUFFMANDecode/kernel.asm` -> **Severity: 121.7** (Blast Radius: 1.217 * Doc Risk: 100.0%)
- `Compress/HUFFMAN/HUFFMANDecode/kernel7.asm` -> **Severity: 121.7** (Blast Radius: 1.217 * Doc Risk: 100.0%)
- `Compress/HUFFMAN/HUFFMANDecode/kernel8.asm` -> **Severity: 121.7** (Blast Radius: 1.217 * Doc Risk: 100.0%)
- `Compress/HUFFMAN/HUFFMANGFX/kernel.asm` -> **Severity: 121.7** (Blast Radius: 1.217 * Doc Risk: 100.0%)
- `Compress/HUFFMAN/HUFFMANGFX/kernel7.asm` -> **Severity: 121.7** (Blast Radius: 1.217 * Doc Risk: 100.0%)

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
