# ARCHITECTURAL_BRIEF: Much-Assembly-Required
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/simon987/Much-Assembly-Required.git` |
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
- **Scope:** 402 analyzed artifact(s), 92776 LOC.
- **Load-bearing artifact:** `Server/src/main/java/net/simon987/server/assembly/Status.java` -- 93 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Server/src/main/resources/static/js/ace/ace.js` -- pulls in 87 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Server/src/main/resources/static/js/phaser.js` at magnitude 55926.3 (structural weight, not risk).
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
| Total Artifacts | 451 |
| Analyzed Artifacts (Scanned) | 402 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 49 |
| Total LOC | 92776 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.1% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5671 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.245 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2229 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 324 | 13001 | 80.6% |
| JAVASCRIPT | 44 | 70735 | 10.9% |
| TYPESCRIPT | 10 | 8647 | 2.5% |
| XML | 8 | 0 | 2.0% |
| PLAINTEXT | 7 | 0 | 1.7% |
| MARKDOWN | 2 | 0 | 0.5% |
| JSON | 2 | 82 | 0.5% |
| DOCKERFILE | 1 | 6 | 0.2% |
| CSS | 1 | 261 | 0.2% |
| RUBY | 1 | 5 | 0.2% |
| SHELL | 1 | 12 | 0.2% |
| YAML | 1 | 27 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 402 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 20%, State Mutators Files 16%, Declarative / Non-Code 15%, Type Conversions Files 13%, Large Core Modules (3) 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 393 | 97.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 2.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 49*

**Composition by Extension & Reason:**
- `.java`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')
- `.vm`: 7x Unsupported Format (.vm)
- `.iml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 2x Excluded (Explicitly Denied Extension: '.ttf')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.json`: 1x Excluded (Massive Static Asset Blob: 12161 LOC)
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')
- `.woff2`: 1x Excluded (Explicitly Denied Extension: '.woff2')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.9 | 42.3 | 52.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.6 | 7.5 | 5.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.0 | 19.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 60.3 | 76.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 348 | 110 | 2 | `Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java` |
| cleanup | 254 | 11 | 0 | `Server/src/main/resources/static/js/phaser.js` |
| guards | 4838 | 217 | 7 | `Server/src/main/resources/static/js/phaser.js` |
| danger | 2209 | 145 | 4 | `Server/src/main/typescript/phaser.d.ts` |
| concurrency | 277 | 16 | 0 | `Server/src/main/resources/static/js/phaser.js` |
| connectivity | 2409 | 371 | 11 | `Server/src/main/resources/static/js/ace/ace.js` |
| io | 59 | 15 | 0 | `Server/src/main/resources/static/js/phaser.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 3 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| time | 118 | 9 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| serialization | 28 | 3 | 0 | `Server/src/main/resources/static/js/phaser.js` |
| regex | 235 | 8 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| events | 615 | 33 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| tests | 288 | 37 | 0 | `Server/src/test/java/net/simon987/server/assembly/OperandTest.java` |
| docs | 6412 | 192 | 4 | `Server/src/main/resources/static/js/phaser.js` |
| debt | 1158 | 56 | 1 | `Server/src/main/typescript/phaser.d.ts` |
| mutation | 33731 | 302 | 26 | `Server/src/main/resources/static/js/phaser.js` |
| dead_code | 2244 | 160 | 4 | `Server/src/main/typescript/phaser.d.ts` |
| credential | 21 | 12 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| threat | 3 | 2 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| ml_ai | 136 | 27 | 0 | `Server/src/main/resources/static/js/phaser.js` |
| ui | 121 | 17 | 0 | `Server/src/main/resources/static/js/phaser.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.4722**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Server/src/main/resources/static/js/phaser.js` (Hits: 9)
- `Server/src/main/java/net/simon987/server/plugin/PluginManager.java` (Hits: 8)
- `Server/src/main/typescript/phaser.d.ts` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Status.java** (`Server/src/main/java/net/simon987/server/assembly/Status.java`) — 93 inbound connections
2. **GameServer.java** (`Server/src/main/java/net/simon987/server/GameServer.java`) — 68 inbound connections
3. **Instruction.java** (`Server/src/main/java/net/simon987/server/assembly/Instruction.java`) — 52 inbound connections
4. **SetccInstruction.java** (`Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java`) — 52 inbound connections
5. **LogManager.java** (`Server/src/main/java/net/simon987/server/logging/LogManager.java`) — 43 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ace.js** (`Server/src/main/resources/static/js/ace/ace.js`) — 87 outbound dependencies
2. **GameServer.java** (`Server/src/main/java/net/simon987/server/GameServer.java`) — 23 outbound dependencies
3. **Cubot.java** (`Plugin Cubot/src/main/java/net/simon987/cubotplugin/Cubot.java`) — 19 outbound dependencies
4. **UserCreationListener.java** (`Plugin Cubot/src/main/java/net/simon987/cubotplugin/event/UserCreationListener.java`) — 16 outbound dependencies
5. **HackedNPC.java** (`Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `escapeHTML` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **348.5** | LOC: 6687
- `copy` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser.js`) -> Impact: **229.6** | LOC: 180
  * *Intent:* */
- `_initialize` **(I/O & Config Routines)** (@ `Server/src/main/resources/static/js/phaser.js`) -> Impact: **205.6** | LOC: 552
  * *Intent:* /** * Internal method to initialize the capability checks. * This function is removed from Phaser.Device once the device is initialized. * */
- `fire` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser.js`) -> Impact: **151.6** | LOC: 191
  * *Intent:* * calculated based on Weapon properties like `bulletSpeed`. * * If you wish to fire multiple bullets in a single game update, then set `Weapon.multiFi...
- `play` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser.js`) -> Impact: **143.1** | LOC: 167
  * *Intent:* /** * Play this sound, or a marked section of it. * */
- `separateCircle` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser.js`) -> Impact: **140.8** | LOC: 136
  * *Intent:* /** * The core separation function to separate two circular physics bodies. * */
- `runNarrowphase` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser.js`) -> Impact: **130.1** | LOC: 108
  * *Intent:* /** * Runs narrowphase for the shape pair i and j. */
- `setProperty` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser.js`) -> Impact: **123.9** | LOC: 77
  * *Intent:* * - 0: set the existing value to the given value; if force is `true` a new property will be created if needed * - 1: will add the given value to the v...
- `quickDecomp` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser.js`) -> Impact: **108.2** | LOC: 154
  * *Intent:* /** * Quickly decompose the Polygon into convex sub-polygons. */
- `parseTiledJSON` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser.js`) -> Impact: **107.7** | LOC: 401
  * *Intent:* /** * Parses a Tiled JSON file into valid map data. */

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Server/src/main/resources/static/js` | 4 | 61253.92 | 68.27% | 40.89% |
| `Server/src/main/resources/static/js/ace` | 40 | 10596.58 | 4.18% | 1.21% |
| `Server/src/main/typescript` | 11 | 2150.3 | 30.57% | 71.7% |
| `Plugin NPC/src/main/java/net/simon987/npcplugin` | 21 | 1612.34 | 41.27% | 65.06% |
| `Server/src/main/java/net/simon987/server/assembly` | 18 | 1417.04 | 18.97% | 5.52% |
| `Server/src/main/java/net/simon987/server/assembly/instruction` | 76 | 1301.84 | 8.82% | 7.03% |
| `Plugin Cubot/src/main/java/net/simon987/cubotplugin` | 17 | 1071.9 | 39.89% | 63.58% |
| `Server/src/test/java/net/simon987/server/assembly/instruction` | 31 | 560.02 | 0.63% | 0.0% |
| `Server/src/main/java/net/simon987/server/game/world` | 13 | 546.4 | 10.49% | 35.37% |
| `Server/src/main/java/net/simon987/server/game/objects` | 15 | 459.72 | 8.24% | 6.66% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotBattery.java` -> **100.0%** Exposure
- `plugin-contruction/src/main/java/net/simon987/constructionplugin/ConstructionSite.java` -> **100.0%** Exposure
- `Server/src/main/typescript/p2.d.ts` -> **100.0%** Exposure
- `Server/src/main/typescript/phaser.d.ts` -> **100.0%** Exposure
- `Server/src/main/typescript/pixi.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLidar.java` -> **100.0%** Exposure
- `Plugin NPC/src/main/java/net/simon987/npcplugin/HarvestTask.java` -> **100.0%** Exposure
- `Plugin NPC/src/main/java/net/simon987/npcplugin/Settlement.java` -> **100.0%** Exposure
- `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultDimension.java` -> **100.0%** Exposure
- `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultWorldGenerator.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Server/src/main/typescript/phaser.d.ts` -> **919** Orphaned Functions | **469** Duplicates
- `Server/src/main/resources/static/js/phaser.js` -> **478** Orphaned Functions | **128** Duplicates
- `Server/src/main/typescript/pixi.d.ts` -> **92** Orphaned Functions | **109** Duplicates
- `Server/src/main/typescript/p2.d.ts` -> **132** Orphaned Functions | **23** Duplicates
- `Server/src/main/typescript/phaser.plugin.isometric.d.ts` -> **40** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `13` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1258` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Server/src/main/resources/static/js/phaser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 16.248)
- **Top Global Matches:** file_cluster_4: 16.248, file_cluster_15: 17.774, file_cluster_12: 17.88
- **Magnitude:** 55926.3 | **LOC:** 105225 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%), Debt Markers (formerly Tech Debt) (58.6%)
- **Documentation Coverage:** 11.099% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy` **(Many-Argument Workhorses)** (Impact: 229.6)
    * *Intent:* */
  * `_initialize` **(I/O & Config Routines)** (Impact: 205.6)
    * *Intent:* /** * Internal method to initialize the capability checks. * This function is removed from Phaser.De...
  * `fire` **(Many-Argument Workhorses)** (Impact: 151.6)
    * *Intent:* * calculated based on Weapon properties like `bulletSpeed`. * * If you wish to fire multiple bullets...
  * `play` **(Many-Argument Workhorses)** (Impact: 143.1)
    * *Intent:* /** * Play this sound, or a marked section of it. * */
  * `separateCircle` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* /** * The core separation function to separate two circular physics bodies. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 7901 instances
* *Concurrency (weighted view):* 95
* *State Mutation (weighted view):* 29496
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9633`, `structural_boundaries: 6812`, `args: 3410`, `func_start: 3309`
* *Risk/State:* `safety_bypasses: 110`, `state_mutation: 13694`, `dead_code: 77`, `planned_debt: 58`, `fragile_debt: 16`, `duplicate_logic: 128`, `unreferenced_by_name: 478`
* *Architecture:* `io: 9`, `api: 69`, `concurrency: 20`
* *Defense:* `safety: 3127`, `doc: 5606`, `sync_locks: 2`, `cleanup: 187`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/ace/ace.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.937)
- **Top Global Matches:** file_cluster_12: 9.937, file_cluster_4: 10.416, file_cluster_7: 11.613
- **Magnitude:** 9420.84 | **LOC:** 19384 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **87**; blast radius 1.045; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 99.2114% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `escapeHTML` **(Many-Argument Workhorses)** (Impact: 348.5)
  * `onMouseDown` **(Compute Cores)** (Impact: 97.5)
  * `renderChanges` **(Many-Argument Workhorses)** (Impact: 83.3)
  * `normalizeCommandKeys` **(Defensive Guards)** (Impact: 74.7)
  * `addMultiMouseDownListener` **(Many-Argument Workhorses)** (Impact: 47.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 846 instances
* *High Risk Execution (weighted view):* 8
* *Concurrency (weighted view):* 239
* *State Mutation (weighted view):* 5629
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1245`, `structural_boundaries: 3518`, `args: 1668`, `func_start: 1408`
* *Risk/State:* `safety_bypasses: 675`, `high_risk_execution: 11`, `state_mutation: 3937`, `dead_code: 1`, `planned_debt: 19`, `fragile_debt: 2`, `duplicate_logic: 7`, `unreferenced_by_name: 34`
* *Architecture:* `io: 1`, `api: 222`, `concurrency: 49`, `import: 202`
* *Defense:* `safety: 426`, `doc: 3`, `immutability_locks: 7`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lang, oop, range, token_iterator, behaviour, config, hash_handler, dom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/phaser-plugin-isometric.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.557)
- **Top Global Matches:** file_cluster_4: 7.557, file_cluster_10: 9.543, file_cluster_15: 10.045
- **Magnitude:** 2908.14 | **LOC:** 4447 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.3%), Complexity Load (formerly Cognitive Load) (54.2%)
- **Documentation Coverage:** 11.9048% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `separateZ` **(Many-Argument Workhorses)** (Impact: 68.8)
    * *Intent:* /** * The core separation function to separate two physics bodies on the z axis. * */
  * `separateX` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* /** * The core separation function to separate two physics bodies on the x axis. * */
  * `separateY` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* /** * The core separation function to separate two physics bodies on the x axis. * */
  * `computeVelocity` **(Many-Argument Workhorses)** (Impact: 54.7)
    * *Intent:* /** * A tween-like function that takes a starting velocity and some other factors and returns an alt...
  * `topologicalSort` **(Many-Argument Workhorses)** (Impact: 47.6)
    * *Intent:* /** * Perform a volume-based topological sort on all IsoSprites in the passed group or array. Will u...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 432 instances
* *State Mutation (weighted view):* 1580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 504`, `structural_boundaries: 213`, `args: 178`, `func_start: 159`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 716`, `duplicate_logic: 6`, `unreferenced_by_name: 22`
* *Architecture:* None
* *Defense:* `safety: 131`, `doc: 256`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/mar.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.602)
- **Top Global Matches:** file_cluster_12: 7.602, file_cluster_10: 8.442, file_cluster_15: 9.054
- **Magnitude:** 2069.9 | **LOC:** 1946 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initialiseAnimations` **(I/O & Config Routines)** (Impact: 27.2)
  * `handle` **(Compute Cores)** (Impact: 26.5)
  * `createTile` **(Compute Cores)** (Impact: 25.1)
  * `MarGame` **(I/O & Config Routines)** (Impact: 24.6)
  * `handleObjectsUpdate` **(Defensive Guards)** (Impact: 21.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 322 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 1276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 291`, `args: 236`, `func_start: 174`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 2`, `state_mutation: 632`, `duplicate_logic: 12`, `unreferenced_by_name: 28`
* *Architecture:* `io: 1`, `concurrency: 4`
* *Defense:* `safety: 32`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/typescript/GameObject.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.635)
- **Top Global Matches:** file_cluster_15: 6.635, file_cluster_16: 6.912, file_cluster_11: 7.486
- **Magnitude:** 533.76 | **LOC:** 889 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 1.911; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.8%)
- **Documentation Coverage:** 85.8824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateObject` **(Compute Cores)** (Impact: 20.1)
  * `createObject` **(Compute Cores)** (Impact: 19.7)
    * *Intent:* /** * Factory method for GameObjects */
  * `updateHologram` **(Stateful Encapsulated Methods)** (Impact: 19.6)
  * `walkAnimation` **(Compute Cores)** (Impact: 11.9)
  * `walk` **(I/O & Config Routines)** (Impact: 11.8)
    * *Intent:* /** * Initiate the walk animation. Handles multiple calls of this function even if the previous anim...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 50 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 78`, `args: 56`, `func_start: 54`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 162`, `planned_debt: 1`, `duplicate_logic: 12`, `unreferenced_by_name: 1`
* *Architecture:* `api: 34`, `concurrency: 2`
* *Defense:* `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.911
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004988
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/CPU.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.077)
- **Top Global Matches:** file_cluster_4: 7.077, file_cluster_15: 7.964, file_cluster_12: 8.103
- **Magnitude:** 376.82 | **LOC:** 470 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **11**; blast radius 11.197; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.6%), Complexity Load (formerly Cognitive Load) (72.0%), Connectivity (formerly Api Exposure) (52.5%)
- **Documentation Coverage:** 95.3488% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeInstruction` **(Many-Argument Workhorses)** (Impact: 66.0)
  * `executeImmediateValue` **(Stateful Encapsulated Methods)** (Impact: 23.7)
  * `executeSourceIsRegister` **(Stateful Encapsulated Methods)** (Impact: 23.6)
  * `executeImmediateValueMem` **(Stateful Encapsulated Methods)** (Impact: 23.6)
  * `execute` **(I/O & Config Routines)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 102`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 108`, `dead_code: 3`, `planned_debt: 5`
* *Architecture:* `api: 21`, `import: 10`
* *Defense:* `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.197
  * `Choke Point (Betweenness):` 0.025613 | `Ripple Effect (Closeness):` 0.141755
  * `Imports (Out-Degree: 16):` net.simon987.server.GameServer, net.simon987.server.IServerConfiguration, net.simon987.server.assembly.exception.CancelledException, net.simon987.server.assembly.instruction.*, net.simon987.server.event.CpuInitialisationEvent, net.simon987.server.event.GameEvent, net.simon987.server.game.objects.ControllableUnit, net.simon987.server.game.objects.HardwareHost...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `Server/src/main/typescript/phaser.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 10.646)
- **Top Global Matches:** file_cluster_7: 10.646, file_cluster_5: 11.449, file_cluster_14: 11.496
- **Magnitude:** 373.68 | **LOC:** 7686 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (20.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy` **(Compute Cores)** (Impact: 76.4)
  * `button` **(Compute Cores)** (Impact: 36.5)
  * `constructor` **(Compute Cores)** (Impact: 33.2)
  * `button` **(Compute Cores)** (Impact: 31.7)
  * `setSounds` **(Compute Cores)** (Impact: 27.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1711`, `structural_boundaries: 1140`, `args: 2072`, `func_start: 2044`, `class_start: 181`
* *Risk/State:* `safety_bypasses: 731`, `state_mutation: 2`, `duplicate_logic: 469`, `unreferenced_by_name: 919`
* *Architecture:* `io: 8`, `api: 4`
* *Defense:* `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/typescript/MarGame.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.486)
- **Top Global Matches:** file_cluster_6: 7.486, file_cluster_4: 11.076, file_cluster_8: 15.863
- **Magnitude:** 367.6 | **LOC:** 346 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.7%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initialiseAnimations` **(I/O & Config Routines)** (Impact: 28.0)
  * `constructor` **(I/O & Config Routines)** (Impact: 26.7)
  * `update` **(I/O & Config Routines)** (Impact: 17.9)
  * `preload` **(I/O & Config Routines)** (Impact: 6.0)
  * `getMessage` **(I/O & Config Routines)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 10`, `args: 17`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 110`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/editor.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.12)
- **Top Global Matches:** file_cluster_4: 8.12, file_cluster_6: 8.965, file_cluster_12: 13.76
- **Magnitude:** 349.58 | **LOC:** 572 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.933; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (65.3%), Guard Balance (formerly Safety Score) (57.5%), Connectivity (formerly Api Exposure) (32.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getOperandType` **(Defensive Guards)** (Impact: 45.7)
  * `parseInstruction` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `parseDWInstruction` **(Many-Argument Workhorses)** (Impact: 20.8)
  * `checkForORGInstruction` **(Defensive Guards)** (Impact: 17.6)
  * `checkForEQUInstruction` **(Defensive Guards)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 69`, `args: 18`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 59`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 5`
* *Defense:* `safety: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002494
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Plugin Cubot/src/main/java/net/simon987/cubotplugin/Cubot.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.683)
- **Top Global Matches:** file_cluster_5: 6.683, file_cluster_12: 7.661, file_cluster_7: 8.387
- **Magnitude:** 323.48 | **LOC:** 606 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **19**; blast radius 4.271; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.1%), Connectivity (formerly Api Exposure) (66.0%), Complexity Load (formerly Cognitive Load) (41.2%)
- **Documentation Coverage:** 93.578% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(I/O & Config Routines)** (Impact: 9.0)
  * `hardwareInterrupt` **(Compute Cores)** (Impact: 5.7)
  * `jsonSerialise` **(I/O & Config Routines)** (Impact: 5.2)
  * `spendEnergy` **(Type Conversions)** (Impact: 4.8)
  * `chargeShield` **(Compute Cores)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 117`, `args: 55`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 69`
* *Architecture:* `api: 57`, `import: 16`
* *Defense:* `safety: 2`, `doc: 22`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.271
  * `Choke Point (Betweenness):` 0.005301 | `Ripple Effect (Closeness):` 0.045012
  * `Imports (Out-Degree: 17):` java.awt.*, java.util.*, java.util.List, net.simon987.cubotplugin.event.CubotWalkEvent, net.simon987.cubotplugin.event.DeathEvent, net.simon987.server.GameServer, net.simon987.server.IServerConfiguration, net.simon987.server.assembly.CPU...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultWorldGenerator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.827)
- **Top Global Matches:** file_cluster_8: 7.827, file_cluster_6: 17.573, file_cluster_3: 20.548
- **Magnitude:** 275.24 | **LOC:** 266 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.132; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Complexity Load (formerly Cognitive Load) (80.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateVaultWorld` **(Many-Argument Workhorses)** (Impact: 105.3)
  * `hasTileAdjacent` **(Stateful Encapsulated Methods)** (Impact: 9.6)
  * `compare` **(Annotated & Test Methods)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 39`, `args: 3`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 56`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.132
  * `Choke Point (Betweenness):` 0.000109 | `Ripple Effect (Closeness):` 0.01001
  * `Imports (Out-Degree: 4):` java.awt.*, java.util.ArrayList, java.util.Comparator, java.util.Random, net.simon987.server.game.objects.Direction, net.simon987.server.game.world.TileMap, net.simon987.server.game.world.TileVoid, net.simon987.server.game.world.World
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Server/src/main/typescript/GameClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.285)
- **Top Global Matches:** file_cluster_12: 7.285, file_cluster_15: 7.856, file_cluster_11: 8.332
- **Magnitude:** 266.92 | **LOC:** 499 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.6%), Guard Balance (formerly Safety Score) (62.0%)
- **Documentation Coverage:** 77.0833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle` **(I/O & Config Routines)** (Impact: 27.5)
  * `onDownCallback` **(Compute Cores)** (Impact: 12.1)
    * *Intent:* //Handle keypresses
  * `connectToGameServer` **(I/O & Config Routines)** (Impact: 11.9)
    * *Intent:* /** * Connect to the game server */
  * `handle` **(Compute Cores)** (Impact: 10.7)
  * `initGame` **(I/O & Config Routines)** (Impact: 10.5)
    * *Intent:* /** * Called after the connection has been made to the server */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 46`, `args: 39`, `func_start: 38`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 36`, `unreferenced_by_name: 12`
* *Architecture:* `io: 1`, `api: 17`, `concurrency: 1`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/typescript/World.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.955)
- **Top Global Matches:** file_cluster_15: 6.955, file_cluster_16: 7.391, file_cluster_0: 7.511
- **Magnitude:** 264.04 | **LOC:** 484 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.341; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.0%), Complexity Load (formerly Cognitive Load) (56.7%)
- **Documentation Coverage:** 63.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createTile` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* /** * Factory method to create a Tile */
  * `handleObjectsUpdate` **(I/O & Config Routines)** (Impact: 22.5)
    * *Intent:* /** * Update, create or delete the current objects based on a list received from the server */
  * `setTerrain` **(Stateful Encapsulated Methods)** (Impact: 8.5)
    * *Intent:* /** * Load terrain data from array and create Tiles */
  * `updateTerrain` **(State Mutators)** (Impact: 5.9)
    * *Intent:* /** * Delete current ojects and tiles and replace them with provided terrain */
  * `getObject` **(Stateful Encapsulated Methods)** (Impact: 4.7)
    * *Intent:* /** * Get object by id */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 40`, `args: 28`, `func_start: 25`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 100`, `unreferenced_by_name: 4`
* *Architecture:* `api: 12`
* *Defense:* `doc: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002494
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/Assembler.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.637)
- **Top Global Matches:** file_cluster_12: 6.637, file_cluster_5: 8.214, file_cluster_16: 8.483
- **Magnitude:** 263.12 | **LOC:** 607 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **11**; blast radius 2.662; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.7%), Complexity Load (formerly Cognitive Load) (26.3%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseInstruction` **(Many-Argument Workhorses)** (Impact: 41.1)
    * *Intent:* /** * Parse an instruction and encode it * * @param line Line to parse * @param currentLine Current ...
  * `parseDWInstruction` **(Many-Argument Workhorses)** (Impact: 32.2)
    * *Intent:* /** * Parse the DW instruction (Define word). Handles DUP operator * * @param line Current line. ass...
  * `parseDUPOperator16` **(Stateful Encapsulated Methods)** (Impact: 14.2)
    * *Intent:* /** * Parse the dup operator * * @param valueTokens Value tokens e.g. {"8", "DUP(12)"} * @param labe...
  * `parse` **(Defensive Guards)** (Impact: 11.0)
    * *Intent:* /** * Parses a text and assembles it. The assembler splits the text in * lines and parses them one b...
  * `encodeInstructions` **(Stateful Encapsulated Methods)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 77`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 36`, `dead_code: 1`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 32`, `doc: 15`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.662
  * `Choke Point (Betweenness):` 0.003043 | `Ripple Effect (Closeness):` 0.115676
  * `Imports (Out-Degree: 6):` java.io.ByteArrayOutputStream, java.io.DataOutputStream, java.io.IOException, java.nio.charset.StandardCharsets, java.util.HashMap, java.util.regex.Matcher, java.util.regex.Pattern, net.simon987.server.IServerConfiguration...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/game/world/World.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.712)
- **Top Global Matches:** file_cluster_5: 5.712, file_cluster_12: 6.95, file_cluster_7: 8.487
- **Magnitude:** 232.92 | **LOC:** 443 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **16**; blast radius 16.21; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.7%), Connectivity (formerly Api Exposure) (68.7%)
- **Documentation Coverage:** 64.5161% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getRandomTileWithAdjacent` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* /** * Get a random tile with N adjacent non-blocked tile * * @param n Number of adjacent tiles of ty...
  * `update` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* /** * Update this World and its GameObjects * <br> * The update is handled by plugins first */
  * `getNeighbouringLoadedWorlds` **(Stateful Encapsulated Methods)** (Impact: 7.1)
  * `getRandomPassableTile` **(I/O & Config Routines)** (Impact: 6.2)
    * *Intent:* /** * Get a random tile that is empty and passable * The function ensures that a object spawned ther...
  * `getMapInfo` **(I/O & Config Routines)** (Impact: 6.1)
    * *Intent:* /** * Get a binary representation of the map as an array of 16-bit bit fields, one word for each * t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 66`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 47`, `dead_code: 1`
* *Architecture:* `api: 31`, `import: 15`
* *Defense:* `safety: 2`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.21
  * `Choke Point (Betweenness):` 0.015989 | `Ripple Effect (Closeness):` 0.188203
  * `Imports (Out-Degree: 10):` java.awt.*, java.util.ArrayList, java.util.Collection, java.util.List, java.util.Random, java.util.concurrent.ConcurrentHashMap, net.simon987.server.GameServer, net.simon987.server.event.GameEvent...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `Server/src/main/resources/static/js/ace/ext-searchbox.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.94)
- **Top Global Matches:** file_cluster_10: 6.94, file_cluster_12: 6.951, file_cluster_15: 9.194
- **Magnitude:** 230.06 | **LOC:** 511 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.045; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.7%), Guard Balance (formerly Safety Score) (65.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Callbacks & Closures)** (Impact: 12.3)
  * `updateCounter` **(I/O & Config Routines)** (Impact: 11.6)
  * `setSearchRange` **(Callbacks & Closures)** (Impact: 6.1)
  * `find` **(Many-Argument Workhorses)** (Impact: 4.8)
  * `syncOptions` **(Callbacks & Closures)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 52`, `args: 48`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 66`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hash_handler, dom, event, keys, lang
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/assembly/Operand.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.469)
- **Top Global Matches:** file_cluster_12: 6.469, file_cluster_5: 7.759, file_cluster_7: 8.451
- **Magnitude:** 203.62 | **LOC:** 277 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **2**; blast radius 9.361; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (49.1%), Connectivity (formerly Api Exposure) (28.9%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Operand` **(Many-Argument Workhorses)** (Impact: 26.5)
    * *Intent:* /** * Creates an Operand from text. If labels is not null, it will be used to parse the * operand. *...
  * `parseRegExpr` **(Many-Argument Workhorses)** (Impact: 26.2)
    * *Intent:* /** * Attempt to parse a register followed by an expression. * The expression has to follow this for...
  * `parseLabel` **(Stateful Encapsulated Methods)** (Impact: 9.4)
    * *Intent:* /** * Attempt to parse a user-defined label * * @param text Text to parse * @param labels Map of lab...
  * `parseReg` **(Stateful Encapsulated Methods)** (Impact: 5.8)
    * *Intent:* /** * Attempt to parse a register * * @param text Text to parse * @return true if successful */
  * `parseImmediate` **(Stateful Encapsulated Methods)** (Impact: 4.1)
    * *Intent:* /** * Attempt to parse an integer * * @param text Text to parse, can be a label or immediate value (...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 30`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 41`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 10`, `doc: 11`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.361
  * `Choke Point (Betweenness):` 0.002874 | `Ripple Effect (Closeness):` 0.178874
  * `Imports (Out-Degree: 2):` java.util.HashMap, net.simon987.server.assembly.exception.InvalidOperandException
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.208)
- **Top Global Matches:** file_cluster_5: 7.208, file_cluster_7: 8.621, file_cluster_12: 9.923
- **Magnitude:** 188.1 | **LOC:** 340 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **16**; blast radius 1.828; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spendEnergy` **(Type Conversions)** (Impact: 6.4)
  * `hardwareInterrupt` **(Compute Cores)** (Impact: 5.7)
  * `jsonSerialise` **(Type Conversions)** (Impact: 5.0)
  * `detachHardware` **(Generic / Templated Code)** (Impact: 4.8)
  * `hardwareQuery` **(Annotated & Test Methods)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 85`, `args: 37`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 38`, `planned_debt: 1`, `unreferenced_by_name: 23`
* *Architecture:* `api: 30`, `concurrency: 6`, `import: 15`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.828
  * `Choke Point (Betweenness):` 0.00198 | `Ripple Effect (Closeness):` 0.011822
  * `Imports (Out-Degree: 16):` java.util.ArrayList, java.util.HashMap, java.util.List, java.util.Map, net.simon987.server.GameServer, net.simon987.server.assembly.*, net.simon987.server.event.ObjectDeathEvent, net.simon987.server.game.item.Item...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.242)
- **Top Global Matches:** file_cluster_16: 8.242, file_cluster_4: 8.398, file_cluster_15: 9.501
- **Magnitude:** 174.48 | **LOC:** 342 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **12**; blast radius 32.654; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (70.8%), Guard Balance (formerly Safety Score) (55.2%), Debt Markers (formerly Tech Debt) (24.4%), Complexity Load (formerly Cognitive Load) (10.8%)
- **Documentation Coverage:** 22.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setcc` **(Stateful Encapsulated Methods)** (Impact: 39.7)
    * *Intent:* * 0x02 SETAE,SETNB,SETNC Above or Equal, Not Below, No Carry CF=0 * 0x03 SETBE, SETNA Below or Equal...
  * `encode` **(Many-Argument Workhorses)** (Impact: 13.6)
    * *Intent:* /** * Encodes the instruction. Writes the result in the outputStream. * Needs one operand of Operand...
  * `seta` **(Encapsulated Accessors)** (Impact: 4.3)
    * *Intent:* /** * SETA, SETNBE Above, Not Below or Equal CF=0 AND ZF=0 */
  * `setae` **(Encapsulated Accessors)** (Impact: 4.3)
    * *Intent:* /** * SETAE,SETNB,SETNC Above or Equal, Not Below, No Carry CF=0 */
  * `setbe` **(Encapsulated Accessors)** (Impact: 4.3)
    * *Intent:* /** * SETBE, SETNA Below or Equal, Not Above CF=1 OR ZF=1 */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 53`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `unreferenced_by_name: 3`
* *Architecture:* `api: 22`, `import: 12`
* *Defense:* `doc: 20`, `sync_locks: 28`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.654
  * `Choke Point (Betweenness):` 0.015118 | `Ripple Effect (Closeness):` 0.129676
  * `Imports (Out-Degree: 9):` java.io.ByteArrayOutputStream, java.util.HashMap, java.util.Map, net.simon987.server.assembly.Instruction, net.simon987.server.assembly.MachineCode, net.simon987.server.assembly.Operand, net.simon987.server.assembly.OperandType, net.simon987.server.assembly.Status...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/Settlement.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.082)
- **Top Global Matches:** file_cluster_7: 8.082, file_cluster_5: 8.189, file_cluster_14: 9.537
- **Magnitude:** 166.66 | **LOC:** 223 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **10**; blast radius 2.208; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Guard Balance (formerly Safety Score) (85.9%), Connectivity (formerly Api Exposure) (36.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Settlement` **(Compute Cores)** (Impact: 24.9)
  * `Settlement` **(Type Conversions)** (Impact: 8.5)
  * `mongoSerialise` **(I/O & Config Routines)** (Impact: 5.2)
  * `addNpc` **(Parameter Forwarders)** (Impact: 1.6)
  * `DifficultyLevel` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 38`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 42`, `planned_debt: 1`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.208
  * `Choke Point (Betweenness):` 0.002263 | `Ripple Effect (Closeness):` 0.024554
  * `Imports (Out-Degree: 9):` java.awt.*, java.util.ArrayList, java.util.List, net.simon987.server.GameServer, net.simon987.server.game.world.TilePlain, net.simon987.server.game.world.World, net.simon987.server.game.world.WorldGenerationException, net.simon987.server.io.MongoSerializable...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/game/GameUniverse.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.036)
- **Top Global Matches:** file_cluster_5: 7.036, file_cluster_7: 7.97, file_cluster_12: 8.74
- **Magnitude:** 156.96 | **LOC:** 293 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 4.216; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.8%)
- **Documentation Coverage:** 76.087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getWorld` **(Many-Argument Workhorses)** (Impact: 12.8)
    * *Intent:* /** * Get a world by coordinates, attempts to load from mongoDB if not found. * * @param x the x coo...
  * `getOrCreateUser` **(Defensive Guards)** (Impact: 10.2)
  * `loadWorld` **(Stateful Encapsulated Methods)** (Impact: 6.8)
    * *Intent:* /** * Attempts loading a world from mongoDB by coordinates * * @param x the x coordinate of the worl...
  * `getObject` **(Compute Cores)** (Impact: 4.9)
    * *Intent:* /** * Get an object by id * <br> * ConcurrentModificationException risk when inside game loop * * @p...
  * `removeWorld` **(Parameter Forwarders)** (Impact: 4.3)
    * *Intent:* /** * Removes the world with given coordinates from the universe. * * @param x the x coordinate of t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 58`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 26`
* *Architecture:* `api: 23`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 4`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.216
  * `Choke Point (Betweenness):` 0.008534 | `Ripple Effect (Closeness):` 0.175842
  * `Imports (Out-Degree: 8):` com.mongodb.client.MongoClient, com.mongodb.client.MongoCollection, com.mongodb.client.MongoCursor, com.mongodb.client.MongoDatabase, java.util.Collection, java.util.concurrent.ConcurrentHashMap, net.simon987.server.GameServer, net.simon987.server.IServerConfiguration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/GameServer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.625)
- **Top Global Matches:** file_cluster_12: 6.625, file_cluster_5: 7.209, file_cluster_7: 8.246
- **Magnitude:** 153.56 | **LOC:** 351 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **68** in-repo importer(s); it depends on **23**; blast radius 37.984; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save` **(I/O & Config Routines)** (Impact: 11.4)
  * `tick` **(I/O & Config Routines)** (Impact: 8.1)
  * `load` **(I/O & Config Routines)** (Impact: 7.1)
  * `GameServer` **(I/O & Config Routines)** (Impact: 6.2)
  * `run` **(I/O & Config Routines)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 82`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 44`
* *Architecture:* `api: 18`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.984
  * `Choke Point (Betweenness):` 0.09048 | `Ripple Effect (Closeness):` 0.23646
  * `Imports (Out-Degree: 18):` com.mongodb.MongoClientException, com.mongodb.client.*, com.mongodb.client.model.ReplaceOptions, java.util.ArrayList, net.simon987.server.crypto.CryptoProvider, net.simon987.server.crypto.SecretKeyGenerator, net.simon987.server.event.GameEvent, net.simon987.server.event.GameEventDispatcher...
  * `Imported By (In-Degree: 68):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultDimension.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.484)
- **Top Global Matches:** file_cluster_6: 8.484, file_cluster_4: 9.786, file_cluster_12: 15.861
- **Magnitude:** 148.24 | **LOC:** 262 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 1.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.7%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VaultDimension` **(Compute Cores)** (Impact: 31.7)
  * `attachWorld` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* /** * Update the blueprint's openings to allow traveling to the newly attached world * * @param dire...
  * `worldExists` **(Encapsulated Accessors)** (Impact: 2.0)
  * `coordinatesOf` **(Parameter Forwarders)** (Impact: 1.7)
    * *Intent:* /** * Get the coordinates of a world that would be attached to this world * * @param direction direc...
  * `getHomeWorld` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 43`, `args: 9`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 37`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.223
  * `Choke Point (Betweenness):` 0.001167 | `Ripple Effect (Closeness):` 0.011607
  * `Imports (Out-Degree: 12):` java.awt.*, java.util.ArrayList, java.util.Collection, java.util.HashMap, java.util.Random, net.simon987.npcplugin.world.TileVaultFloor, net.simon987.server.GameServer, net.simon987.server.IServerConfiguration...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Server/src/main/typescript/Console.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.21)
- **Top Global Matches:** file_cluster_15: 6.21, file_cluster_10: 7.381, file_cluster_16: 7.986
- **Magnitude:** 145.24 | **LOC:** 209 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (47.2%), Debt Markers (formerly Tech Debt) (31.1%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleConsoleBufferUpdate` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* /** * Handles a consoleBuffer update */
  * `toggleColor` **(Compute Cores)** (Impact: 5.4)
    * *Intent:* /** * Toggle dark/light theme */
  * `toggleScrolling` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* /** * Toggle auto scrolling. Also initially scrolls to bottom on click */
  * `constructor` **(Many-Argument Workhorses)** (Impact: 3.8)
  * `constructor` **(State Mutators)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 13`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 45`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 7`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/game/objects/GameObject.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.011)
- **Top Global Matches:** file_cluster_12: 6.011, file_cluster_15: 6.803, file_cluster_11: 7.211
- **Magnitude:** 125.16 | **LOC:** 276 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **10**; blast radius 16.685; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.7%), Guard Balance (formerly Safety Score) (57.3%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `incrementLocation` **(I/O & Config Routines)** (Impact: 16.1)
    * *Intent:* /** * Increment the location of the game object by 1 tile * Collision checks happen here */
  * `getAdjacentTile` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* /** * Get the first directly adjacent tile (starting east, going clockwise) */
  * `getFrontTile` **(Compute Cores)** (Impact: 7.6)
  * `getAdjacentTileCount` **(Compute Cores)** (Impact: 6.7)
  * `isAt` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 61`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 21`
* *Architecture:* `api: 26`, `import: 9`
* *Defense:* `safety: 1`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.685
  * `Choke Point (Betweenness):` 0.008248 | `Ripple Effect (Closeness):` 0.156451
  * `Imports (Out-Degree: 5):` java.awt.*, java.util.ArrayList, net.simon987.server.GameServer, net.simon987.server.game.world.Tile, net.simon987.server.game.world.World, net.simon987.server.io.JSONSerializable, net.simon987.server.io.MongoSerializable, org.bson.Document...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Server/src/main/java/net/simon987/server/game/pathfinding/SortedArrayList.java` (JAVA) | Magnitude: 6.18 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 7, doc: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `Server/src/main/resources/static/js/ace/ext-searchbox.js` (JAVASCRIPT) | Magnitude: 230.06 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 323, state_mutation: 66, structural_boundaries: 52, core_var_decl: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Server/src/main/java/net/simon987/server/assembly/Register.java` (JAVA) | Magnitude: 15.12 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 6, api: 6, args: 5
- `Server/src/main/java/net/simon987/server/assembly/Status.java` (JAVA) | Magnitude: 72.46 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 18, api: 17, args: 16
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetaInstructionTest.java` (JAVA) | Magnitude: 21.28 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 14, structural_boundaries: 12, test: 5
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetbeInstructionTest.java` (JAVA) | Magnitude: 21.28 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 14, structural_boundaries: 12, test: 5
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetgeInstructionTest.java` (JAVA) | Magnitude: 21.28 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 14, structural_boundaries: 12, test: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `plugin-contruction/src/main/java/net/simon987/constructionplugin/ConstructionSite.java` (JAVA) | Magnitude: 38.9 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 18, api: 12, args: 9
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/event/CpuInitialisationListener.java` (JAVA) | Magnitude: 22.0 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 23, core_var_decl: 14, state_mutation: 13
- `Server/src/main/java/net/simon987/server/game/world/DayNightCycle.java` (JAVA) | Magnitude: 12.68 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 11, api: 5, args: 4
- `Server/src/main/java/net/simon987/server/game/objects/Direction.java` (JAVA) | Magnitude: 63.5 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 52, branch: 22, structural_boundaries: 17, doc: 7
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotInventory.java` (JAVA) | Magnitude: 95.82 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 24, core_var_decl: 22, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetaeInstructionTest.java` (JAVA) | Magnitude: 14.58 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 12, state_mutation: 8, import: 4
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetbInstructionTest.java` (JAVA) | Magnitude: 14.58 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 12, state_mutation: 8, import: 4
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetcInstructionTest.java` (JAVA) | Magnitude: 14.58 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 12, state_mutation: 8, import: 4
- `Server/src/test/java/net/simon987/server/assembly/instruction/SeteInstructionTest.java` (JAVA) | Magnitude: 14.58 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 12, state_mutation: 8, import: 4
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetnaeInstructionTest.java` (JAVA) | Magnitude: 14.58 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 12, state_mutation: 8, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/event/ChargeShieldCommandListener.java` (JAVA) | Magnitude: 14.76 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, safety_bypasses: 7, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Server/src/main/java/net/simon987/server/assembly/instruction/PushInstruction.java` (JAVA) | Magnitude: 14.88 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 6, api: 5, args: 3
- `Server/src/main/java/net/simon987/server/assembly/instruction/PopInstruction.java` (JAVA) | Magnitude: 10.48 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, api: 4, import: 4
- `Server/src/main/java/net/simon987/server/assembly/instruction/XchgInstruction.java` (JAVA) | Magnitude: 10.0 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, api: 4, import: 4
- `Server/src/main/java/net/simon987/server/crypto/RandomStringGenerator.java` (JAVA) | Magnitude: 0.38 | Delta: **0.149** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 13, api: 7, scientific: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java` (JAVA) | Magnitude: 174.48 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 204, structural_boundaries: 53, core_var_decl: 47, branch: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `Server/src/main/java/net/simon987/server/io/JSONSerializable.java` (JAVA) | Magnitude: 5.32 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, args: 2, func_start: 2
- `Server/src/main/java/net/simon987/server/io/MongoSerializable.java` (JAVA) | Magnitude: 3.2 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, args: 1, func_start: 1
- `Server/src/main/java/net/simon987/server/assembly/exception/IllegalOperandException.java` (JAVA) | Magnitude: 4.02 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, api: 2, args: 1
- `Server/src/main/java/net/simon987/server/assembly/exception/InvalidMnemonicException.java` (JAVA) | Magnitude: 4.02 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, api: 2, args: 1
- `Server/src/main/java/net/simon987/server/assembly/exception/InvalidOperandException.java` (JAVA) | Magnitude: 4.02 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, api: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `Plugin NPC/src/main/java/net/simon987/npcplugin/event/VaultWorldUpdateListener.java` (JAVA) | Magnitude: 27.6 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 18, import: 10, core_var_decl: 8
- `Server/src/main/java/net/simon987/server/assembly/RegisterSet.java` (JAVA) | Magnitude: 89.98 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 35, state_mutation: 16, api: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Server/src/main/java/net/simon987/server/user/UserStats.java` (JAVA) | Magnitude: 48.82 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 22, args: 11, func_start: 11
- `Server/src/main/java/net/simon987/server/websocket/CodeRequestHandler.java` (JAVA) | Magnitude: 20.88 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, state_mutation: 4, import: 4
- `Plugin NPC/src/main/java/net/simon987/npcplugin/Settlement.java` (JAVA) | Magnitude: 166.66 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 150, state_mutation: 42, structural_boundaries: 38, core_var_decl: 27
- `Plugin Radioactive Cloud/src/main/java/net/simon987/pluginradioactivecloud/RadioactiveObstacle.java` (JAVA) | Magnitude: 7.82 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 11, import: 5, api: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 9.046** (Bridge: 0.0905 * Flux: 99.9831%)
- `Server/src/main/java/net/simon987/server/logging/LogManager.java` -> **Severity: 4.056** (Bridge: 0.0417 * Flux: 97.3403%)
- `Server/src/main/java/net/simon987/server/ServerConfiguration.java` -> **Severity: 3.344** (Bridge: 0.0402 * Flux: 83.2018%)
- `Server/src/main/java/net/simon987/server/websocket/SocketServer.java` -> **Severity: 2.928** (Bridge: 0.0305 * Flux: 95.9453%)
- `Server/src/main/java/net/simon987/server/assembly/CPU.java` -> **Severity: 2.561** (Bridge: 0.0256 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 15.675** (Embedded: 0.2365 * Error Risk: 66.2903%)
- `Server/src/main/java/net/simon987/server/logging/LogManager.java` -> **Severity: 14.979** (Embedded: 0.2857 * Error Risk: 52.4267%)
- `Server/src/main/java/net/simon987/server/game/GameUniverse.java` -> **Severity: 14.067** (Embedded: 0.1758 * Error Risk: 80.0%)
- `Server/src/main/java/net/simon987/server/game/objects/GameRegistry.java` -> **Severity: 14.023** (Embedded: 0.1753 * Error Risk: 80.0%)
- `Server/src/main/java/net/simon987/server/user/UserManager.java` -> **Severity: 13.847** (Embedded: 0.1731 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 3798.4** (Blast Radius: 37.984 * Doc Risk: 100.0%)
- `Server/src/main/java/net/simon987/server/io/MongoSerializable.java` -> **Severity: 2540.4** (Blast Radius: 25.404 * Doc Risk: 100.0%)
- `Server/src/main/java/net/simon987/server/ServerConfiguration.java` -> **Severity: 2137.3** (Blast Radius: 21.373 * Doc Risk: 100.0%)
- `Server/src/main/java/net/simon987/server/logging/LogManager.java` -> **Severity: 1968.2** (Blast Radius: 39.364 * Doc Risk: 50.0%)
- `Server/src/main/java/net/simon987/server/game/objects/ControllableUnit.java` -> **Severity: 1558.0** (Blast Radius: 15.58 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 258 literal sites + 3 sites through wrappers = 261
- **`panics_and_aborts`:** 123 literal sites + 1 sites through wrappers = 124

- `sendString` (function, debug_prints, primitive): 3 call sites in 1 files -- `Server/src/main/java/net/simon987/server/websocket/SocketServer.java`
- `SecretKeyGenerator` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `Server/src/main/java/net/simon987/server/crypto/SecretKeyGenerator.java`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 12178 call pairs -- scoped 16.5%, unique 1.0%, ambiguous 10.7%, external 71.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 7902 | 2.4% | 0.0% | 2.6% | 95.1% |
| java | 3872 | 44.1% | 3.2% | 27.2% | 25.5% |
| typescript | 393 | 28.5% | 0.0% | 11.7% | 59.8% |
| shell | 6 | 0.0% | 0.0% | 0.0% | 100.0% |
| ruby | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
