# ARCHITECTURAL_BRIEF: igv.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/igvteam/igv.js.git` |
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
- **Scope:** 692 analyzed artifact(s), 79250 LOC.
- **Load-bearing artifact:** `js/index.js` -- 97 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `js/browser.js` -- pulls in 51 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `js/browser.js` at magnitude 1812.74 (structural weight, not risk).
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
| Total Artifacts | 3377 |
| Analyzed Artifacts (Scanned) | 692 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2685 |
| Total LOC | 79250 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 20.5% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5123 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1656 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 20.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.4249 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 45 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 364 | 45799 | 52.6% |
| HTML | 207 | 28864 | 29.9% |
| PLAINTEXT | 50 | 0 | 7.2% |
| CSS | 34 | 3204 | 4.9% |
| JSON | 18 | 794 | 2.6% |
| XML | 9 | 0 | 1.3% |
| MARKDOWN | 5 | 0 | 0.7% |
| CSV | 2 | 13 | 0.3% |
| YAML | 1 | 18 | 0.1% |
| SHELL | 1 | 13 | 0.1% |
| TYPESCRIPT | 1 | 545 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 692 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Declarative / Non-Code 15%, Large Core Modules (3) 13%, Large Core Modules (2) 13%, State Mutators Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 637 | 92.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 55 | 7.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2685*

**Composition by Extension & Reason:**
- `no_extension`: 2436x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.FusionJuncSpan'), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.bed`: 28x Excluded (Unsupported Extension: '.bed')
- `.vcf`: 20x Excluded (Unsupported Extension: '.vcf')
- `.bam`: 14x Excluded (Unsupported Extension: '.bam')
- `.gz`: 14x Excluded (Explicitly Denied Extension: '.gz')
- `.bai`: 13x Excluded (Unsupported Extension: '.bai')
- `.git-id`: 10x Excluded (Unsupported Extension: '.git-id')
- `.tbi`: 8x Excluded (Unsupported Extension: '.tbi')
- `.html`: 2x Excluded (Saturation: Line 29 exceeds 500 chars), 1x Excluded (Saturation: Line 30 exceeds 500 chars), 1x Excluded (Saturation: Line 27 exceeds 500 chars)
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.wig`: 7x Excluded (Unsupported Extension: '.wig')
- `.bedpe`: 7x Excluded (Unsupported Extension: '.bedpe')
- `.gff3`: 7x Excluded (Unsupported Extension: '.gff3')
- `.bedgraph`: 6x Excluded (Unsupported Extension: '.bedgraph')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 27.1 | 7.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.0 | 35.5 | 50.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 84.5 | 17.4 | 7.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 24.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.6 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 91.2 | 6.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.3 | 16.7 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 90 | 48 | 0 | `js/feature/decode/ucsc.js` |
| cleanup | 98 | 25 | 0 | `js/trackView.js` |
| guards | 2621 | 301 | 9 | `js/browser.js` |
| danger | 601 | 154 | 2 | `dev/dev.html` |
| concurrency | 1829 | 368 | 8 | `js/browser.js` |
| connectivity | 2018 | 489 | 7 | `js/igv.d.ts` |
| io | 876 | 124 | 2 | `dev/dev.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 4 | 0 | `dev/ucsc/localFile/file-picker.html` |
| time | 49 | 19 | 0 | `dev/misc/interactive-filtering.html` |
| serialization | 39 | 25 | 0 | `dev/ucsc/localFile/trackJS_additions.js` |
| regex | 355 | 114 | 2 | `js/feature/featureParser.js` |
| events | 716 | 193 | 4 | `test/utils/w3XMLHttpRequest.js` |
| tests | 1282 | 73 | 1 | `test/testBaseMods.js` |
| docs | 842 | 386 | 2 | `test/utils/w3XMLHttpRequest.js` |
| debt | 486 | 238 | 2 | `test/testDynseq.js` |
| mutation | 20277 | 566 | 72 | `js/cnvpytor/MeanShiftUtil.js` |
| dead_code | 574 | 107 | 1 | `js/feature/intervalTree.js` |
| credential | 209 | 76 | 1 | `dev/misc/functional-url.html` |
| threat | 16 | 6 | 0 | `test/utils/mockObjects.js` |
| ml_ai | 2 | 2 | 0 | `findLarge.sh` |
| ui | 906 | 238 | 3 | `css/_navbar.scss` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `dev/dev.html` (Hits: 312)
- `examples/index.html` (Hits: 94)
- `test/utils/w3XMLHttpRequest.js` (Hits: 44)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.js** (`js/index.js`) — 97 inbound connections
2. **dom-utils.js** (`js/ui/utils/dom-utils.js`) — 46 inbound connections
3. **igvUtils.js** (`js/util/igvUtils.js`) — 46 inbound connections
4. **featureSource.js** (`js/feature/featureSource.js`) — 28 inbound connections
5. **igv-canvas.js** (`js/igv-canvas.js`) — 27 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **browser.js** (`js/browser.js`) — 51 outbound dependencies
2. **trackFactory.js** (`js/trackFactory.js`) — 18 outbound dependencies
3. **index.js** (`js/index.js`) — 15 outbound dependencies
4. **responsiveNavbar.js** (`js/responsiveNavbar.js`) — 15 outbound dependencies
5. **alignmentTrack.js** (`js/bam/alignmentTrack.js`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `renderJunction` **(Many-Argument Workhorses)** (@ `js/feature/spliceJunctionTrack.js`) -> Impact: **273.0** | LOC: 221
  * *Intent:* /** * */
- `draw` **(Compute Cores)** (@ `js/bam/alignmentTrack.js`) -> Impact: **176.1** | LOC: 467
- `drawSingleAlignment` **(Many-Argument Workhorses)** (@ `js/bam/alignmentTrack.js`) -> Impact: **171.2** | LOC: 303
- `call_2d` **(Many-Argument Workhorses)** (@ `js/cnvpytor/CombinedCaller.js`) -> Impact: **166.7** | LOC: 336
- `search` **(Many-Argument Workhorses)** (@ `js/genome/hgvs.js`) -> Impact: **152.5** | LOC: 244
  * *Intent:* /** * Searches for the given HGVS notation in the provided genome. * Returns a SearchResult with the corresponding chromosome and position if found, *...
- `renderAminoAcidSequence` **(Many-Argument Workhorses)** (@ `js/feature/render/renderFeature.js`) -> Impact: **127.0** | LOC: 152
- `createHGVSAnnotation` **(Many-Argument Workhorses)** (@ `js/genome/hgvs.js`) -> Impact: **117.3** | LOC: 141
  * *Intent:* /** * Returns HGVS annotation for the position, for ref and alt bases. If a MANE transcript is available that is * used with coding notation (c.), oth...
- `decodeBed` **(Many-Argument Workhorses)** (@ `js/feature/decode/ucsc.js`) -> Impact: **107.8** | LOC: 115
  * *Intent:* /** * Decode the UCSC bed format. Only the first 3 columns (chr, start, end) are required. The remaining columns * must follow standard bed order, but...
- `readAlignments` **(Many-Argument Workhorses)** (@ `js/cram/cramReader.js`) -> Impact: **100.5** | LOC: 210
- `renderFeature` **(Many-Argument Workhorses)** (@ `js/feature/render/renderFeature.js`) -> Impact: **99.8** | LOC: 144
  * *Intent:* /** * */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `js` | 29 | 7544.81 | 56.09% | 7.1% |
| `js/feature` | 26 | 6804.02 | 66.36% | 6.12% |
| `js/bam` | 25 | 5670.02 | 64.34% | 5.99% |
| `js/cnvpytor` | 8 | 3165.96 | 65.48% | 2.13% |
| `js/genome` | 21 | 2638.66 | 54.68% | 2.59% |
| `test` | 62 | 2368.24 | 9.16% | 0.0% |
| `examples` | 36 | 1989.43 | 4.33% | 0.0% |
| `js/bigwig` | 9 | 1655.3 | 74.12% | 2.36% |
| `js/variant` | 3 | 1397.18 | 82.6% | 2.87% |
| `js/ui` | 20 | 1395.58 | 55.92% | 5.48% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `js/ui/igvTable.js` -> **99.9665%** Exposure
- `js/igv.d.ts` -> **97.8757%** Exposure
- `dev/cbio/cbio.js` -> **97.0688%** Exposure
- `js/bam/packedAlignments.js` -> **97.0688%** Exposure
- `js/sample/sampleInfoViewport.js` -> **58.775%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `dev/cbio/cbio.js` -> **100.0%** Exposure
- `js/aed/AEDParser.js` -> **100.0%** Exposure
- `js/bam/alignmentContainer.js` -> **100.0%** Exposure
- `js/bam/bamIndex.js` -> **100.0%** Exposure
- `js/bam/bamReaderNonIndexed.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/testDynseq.js` -> **3** Orphaned Functions | **24** Duplicates
- `js/igv.d.ts` -> **22** Orphaned Functions | **0** Duplicates
- `test/testSearch.js` -> **5** Orphaned Functions | **0** Duplicates
- `test/old/testTribble.js` -> **4** Orphaned Functions | **0** Duplicates
- `dev/cbio/cbio.js` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `58` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `266` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `js/browser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.12)
- **Top Global Matches:** file_cluster_4: 7.12, file_cluster_15: 8.599, file_cluster_16: 9.597
- **Magnitude:** 1812.74 | **LOC:** 2683 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **51**; blast radius 10.117; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (74.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.8%)
- **Documentation Coverage:** 61.4035% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadSessionObject` **(Defensive Guards)** (Impact: 79.0)
    * *Intent:* /** * Note: public API function */
  * `createTrack` **(Compute Cores)** (Impact: 47.7)
    * *Intent:* /** * Create a Track object. */
  * `loadGenome` **(Defensive Guards)** (Impact: 38.1)
    * *Intent:* /** * Load a genome, defined by a string ID or a json-like configuration object. This includes a fas...
  * `keyUpHandler` **(Defensive Guards)** (Impact: 33.6)
    * *Intent:* /** * Handle keyup event, used for navigating feature tracks with hot keys. This will get bound to t...
  * `_validateAndWarnResources` **(Compute Cores)** (Impact: 30.5)
    * *Intent:* /** * Validate reference genome and warn about problematic resources in the session. * * Reference g...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 183 instances
* *Concurrency (weighted view):* 279
* *State Mutation (weighted view):* 614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 308`, `args: 162`, `func_start: 123`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 248`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 4`
* *Architecture:* `api: 36`, `concurrency: 89`, `import: 51`
* *Defense:* `safety: 117`, `doc: 43`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.117
  * `Choke Point (Betweenness):` 0.052531 | `Ripple Effect (Closeness):` 0.120987
  * `Imports (Out-Degree: 50):` index.js, blatTrack.js, canvas2svg.js, embedCss.js, events.js, featureSource.js, genbankParser.js, genome.js...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `js/bam/alignmentTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.463)
- **Top Global Matches:** file_cluster_4: 6.463, file_cluster_6: 10.135, file_cluster_15: 12.152
- **Magnitude:** 1489.76 | **LOC:** 1587 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.912; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.6%)
- **Documentation Coverage:** 89.5833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `draw` **(Compute Cores)** (Impact: 176.1)
  * `drawSingleAlignment` **(Many-Argument Workhorses)** (Impact: 171.2)
  * `drawBlock` **(Many-Argument Workhorses)** (Impact: 79.9)
  * `contextMenuItemList` **(Defensive Guards)** (Impact: 77.1)
  * `getAlignmentColor` **(Defensive Guards)** (Impact: 56.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 152 instances
* *State Mutation (weighted view):* 517
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 169`, `args: 85`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 213`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 19`, `concurrency: 7`, `import: 14`
* *Defense:* `safety: 70`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.912
  * `Choke Point (Betweenness):` 0.002146 | `Ripple Effect (Closeness):` 0.064084
  * `Imports (Out-Degree: 16):` index.js, blatTrack.js, igv-canvas.js, igv-icons.js, trackBase.js, dom-utils.js, colorPalletes.js, getChrColor.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/cnvpytor/MeanShiftUtil.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.941)
- **Top Global Matches:** file_cluster_8: 7.941, file_cluster_6: 14.295, file_cluster_4: 22.609
- **Magnitude:** 1056.44 | **LOC:** 1089 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.091; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.6%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `meanShiftCaller` **(Compute Cores)** (Impact: 68.1)
  * `call_mean_shift` **(Compute Cores)** (Impact: 60.6)
  * `cnv_calling` **(Compute Cores)** (Impact: 57.3)
  * `cnvCalling` **(Compute Cores)** (Impact: 57.1)
  * `partition` **(Compute Cores)** (Impact: 55.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 208 instances
* *State Mutation (weighted view):* 659
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 302`, `args: 47`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 243`, `dead_code: 31`, `planned_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 2`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.000671 | `Ripple Effect (Closeness):` 0.052647
  * `Imports (Out-Degree: 2):` baseCNVpytorVCF.js, t_dist.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/feature/interactionTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.708)
- **Top Global Matches:** file_cluster_6: 6.708, file_cluster_4: 10.613, file_cluster_8: 15.452
- **Magnitude:** 1005.98 | **LOC:** 1034 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 1.168; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.7%), Guard Balance (formerly Safety Score) (68.9%)
- **Documentation Coverage:** 85.2459% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawProportional` **(Defensive Guards)** (Impact: 70.4)
  * `drawNested` **(Compute Cores)** (Impact: 55.6)
  * `getWGFeatures` **(Compute Cores)** (Impact: 42.3)
    * *Intent:* /** * Called in the context of FeatureSource (i.e. this == the feature source (a TextFeatureSource) ...
  * `init` **(Defensive Guards)** (Impact: 34.3)
  * `popupData` **(Defensive Guards)** (Impact: 30.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 150 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 469
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 129`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `state_mutation: 169`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 16`, `concurrency: 5`, `import: 11`
* *Defense:* `safety: 70`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.168
  * `Choke Point (Betweenness):` 0.000649 | `Ripple Effect (Closeness):` 0.082105
  * `Imports (Out-Degree: 12):` index.js, igv-canvas.js, igv-icons.js, circularViewUtils.js, trackBase.js, dom-utils.js, colorPalletes.js, getChrColor.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `js/bam/bamUtils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.924)
- **Top Global Matches:** file_cluster_8: 7.924, file_cluster_3: 17.559, file_cluster_6: 19.553
- **Magnitude:** 879.72 | **LOC:** 700 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 2.248; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.0%), Complexity Load (formerly Cognitive Load) (68.9%), Connectivity (formerly Api Exposure) (38.0%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bam_tag2cigar` **(Defensive Guards)** (Impact: 90.2)
  * `decodeBamRecords` **(Many-Argument Workhorses)** (Impact: 84.5)
    * *Intent:* /** * * */
  * `decodeSamRecords` **(Many-Argument Workhorses)** (Impact: 61.9)
  * `decodeBamTags` **(Defensive Guards)** (Impact: 51.1)
    * *Intent:* /** * Decode bam tags from the supplied UInt8Array * * A [!-~] Printable character * i [-+]?[0-9]+ S...
  * `makeBlocks` **(Many-Argument Workhorses)** (Impact: 33.7)
    * *Intent:* /** * Split the alignment record into blocks as specified in the cigarArray. Each aligned block cont...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 107`, `args: 16`, `func_start: 14`
* *Risk/State:* `state_mutation: 169`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 67`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.248
  * `Choke Point (Betweenness):` 0.000969 | `Ripple Effect (Closeness):` 0.046869
  * `Imports (Out-Degree: 4):` index.js, alignmentBlock.js, bamAlignment.js, bamFilter.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `js/canvas2svg.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.845)
- **Top Global Matches:** file_cluster_4: 6.845, file_cluster_15: 7.325, file_cluster_12: 8.635
- **Magnitude:** 878.08 | **LOC:** 1398 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); blast radius 9.231; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.2%), Connectivity (formerly Api Exposure) (59.4%)
- **Documentation Coverage:** 29.8077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `arcTo` **(Many-Argument Workhorses)** (Impact: 38.6)
    * *Intent:* /** * Adds the arcTo to the current path * */
  * `__applyStyleToCurrentElement` **(Defensive Guards)** (Impact: 35.7)
    * *Intent:* /** * Apples the current styles to the current SVG element. On "ctx.fill" or "ctx.stroke" */
  * `arc` **(Many-Argument Workhorses)** (Impact: 28.7)
    * *Intent:* /** * Arc command! */
  * `drawImage` **(I/O & Config Routines)** (Impact: 26.2)
    * *Intent:* /** * Draws a canvas, image or mock context to this canvas. * Note that all svg dom manipulation use...
  * `__parseFont` **(Compute Cores)** (Impact: 25.6)
    * *Intent:* /** * Parses the font string and returns svg mapping */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 415
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 108`, `args: 70`, `func_start: 69`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 173`, `dead_code: 3`, `planned_debt: 5`
* *Architecture:* `api: 33`
* *Defense:* `safety: 49`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.096821
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `js/variant/variantTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.831)
- **Top Global Matches:** file_cluster_4: 7.831, file_cluster_15: 8.819, file_cluster_11: 9.65
- **Magnitude:** 848.22 | **LOC:** 1031 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 1.255; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Complexity Load (formerly Cognitive Load) (82.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 76.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `draw` **(Defensive Guards)** (Impact: 74.7)
  * `postInit` **(Defensive Guards)** (Impact: 27.6)
  * `sortSamplesByGenotype` **(Defensive Guards)** (Impact: 24.2)
  * `getFeatures` **(Defensive Guards)** (Impact: 21.4)
  * `getColorForFeature` **(Defensive Guards)** (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 108 instances
* *Concurrency (weighted view):* 79
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 113`, `args: 52`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 121`, `dead_code: 27`
* *Architecture:* `api: 17`, `concurrency: 14`, `import: 12`
* *Defense:* `safety: 79`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.255
  * `Choke Point (Betweenness):` 0.000622 | `Ripple Effect (Closeness):` 0.082341
  * `Imports (Out-Degree: 13):` index.js, featureSource.js, featureUtils.js, igv-canvas.js, igv-icons.js, circularViewUtils.js, sampleInfo.js, sampleUtils.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/cnvpytor/cnvpytorTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.585)
- **Top Global Matches:** file_cluster_4: 7.585, file_cluster_6: 10.521, file_cluster_12: 11.635
- **Magnitude:** 841.98 | **LOC:** 699 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `draw` **(Compute Cores)** (Impact: 48.9)
  * `paintAxis` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `postInit` **(I/O & Config Routines)** (Impact: 26.1)
  * `getFeatures` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `recreate_tracks` **(Compute Cores)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 115 instances
* *Concurrency (weighted view):* 132
* *State Mutation (weighted view):* 373
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 119`, `args: 43`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 143`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `api: 12`, `concurrency: 27`, `import: 7`
* *Defense:* `safety: 21`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.068
  * `Choke Point (Betweenness):` 0.00309 | `Ripple Effect (Closeness):` 0.08187
  * `Imports (Out-Degree: 7):` featureSource.js, igv-canvas.js, igv-icons.js, trackBase.js, trackClassRegistry.js, HDF5IndexedReader.js, cnvpytorVCF.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/bigwig/bwReader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.492)
- **Top Global Matches:** file_cluster_4: 6.492, file_cluster_6: 8.519, file_cluster_15: 12.946
- **Magnitude:** 817.8 | **LOC:** 744 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **9**; blast radius 3.263; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 65.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readFeatures` **(Many-Argument Workhorses)** (Impact: 51.5)
  * `decodeWigData` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `decodeZoomData` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `loadHeader` **(I/O & Config Routines)** (Impact: 23.5)
    * *Intent:* /** * The BB header consists of * (1) the common header * (2) the zoom headers * (3) autosql * (4) t...
  * `search` **(Compute Cores)** (Impact: 18.6)
    * *Intent:* /** * Search the extended BP tree for the search term, and return any matching features. This only w...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 94 instances
* *Concurrency (weighted view):* 178
* *State Mutation (weighted view):* 300
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 144`, `args: 31`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 112`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 7`, `concurrency: 58`, `import: 9`
* *Defense:* `safety: 32`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.263
  * `Choke Point (Betweenness):` 0.004114 | `Ripple Effect (Closeness):` 0.061468
  * `Imports (Out-Degree: 9):` index.js, binary.js, igvUtils.js, ucscUtils.js, bbDecoders.js, bpTree.js, chromTree.js, rpTree.js...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `js/bam/alignmentContainer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.448)
- **Top Global Matches:** file_cluster_4: 6.448, file_cluster_15: 8.13, file_cluster_9: 9.308
- **Magnitude:** 718.34 | **LOC:** 763 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 2.248; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (72.0%), Guard Balance (formerly Safety Score) (69.1%), Connectivity (formerly Api Exposure) (45.6%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `packAlignmentRows` **(Many-Argument Workhorses)** (Impact: 58.9)
  * `incCounts` **(Compute Cores)** (Impact: 31.6)
  * `getPosCount` **(Compute Cores)** (Impact: 27.3)
  * `getNegCount` **(Compute Cores)** (Impact: 27.3)
  * `sortRows` **(Defensive Guards)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 118`, `args: 54`, `func_start: 42`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 132`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 20`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.248
  * `Choke Point (Betweenness):` 0.000941 | `Ripple Effect (Closeness):` 0.046907
  * `Imports (Out-Degree: 4):` igvUtils.js, bamAlignmentRow.js, baseModificationCounts.js, pairedAlignment.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `dev/misc/interactive-filtering.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.539)
- **Top Global Matches:** file_cluster_15: 6.539, file_cluster_10: 8.095, file_cluster_4: 8.347
- **Magnitude:** 641.74 | **LOC:** 1500 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.821; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.4%), Complexity Load (formerly Cognitive Load) (38.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateFilterCounts` **(Many-Argument Workhorses)** (Impact: 33.7)
    * *Intent:* /** Get counts for each filter, in each facet */
  * `buildFilter` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* /** * Build a filter function taking an igvFeature as an argument and returning true for "pass" (sho...
  * `initFacets` **(Defensive Guards)** (Impact: 25.3)
    * *Intent:* * // For integer or float: numeric values observed for this facet * "filterNumbers": [<Number>], * *...
  * `handleBrushMove` **(Many-Argument Workhorses)** (Impact: 17.9)
    * *Intent:* /** Handle slider move event (i.e., drag or resize) */
  * `getInputStyle` **(Many-Argument Workhorses)** (Impact: 15.5)
    * *Intent:* /** * Get width and font size for input, to help keep full value glanceable */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 148`, `args: 69`, `func_start: 58`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 106`, `dead_code: 1`, `planned_debt: 7`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 33`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` popper.min.js, crossfilter2@1.5.4, d3-array.js, d3-brush.js, d3-dispatch.js, d3-interpolate.js, d3-scale.js, d3-selection.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/segTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.696)
- **Top Global Matches:** file_cluster_4: 6.696, file_cluster_15: 10.142, file_cluster_9: 10.524
- **Magnitude:** 634.1 | **LOC:** 760 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 1.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (87.3%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 86.9565% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `draw` **(Compute Cores)** (Impact: 55.1)
  * `computeRegionScores` **(Compute Cores)** (Impact: 24.6)
  * `filter` **(Defensive Guards)** (Impact: 23.9)
    * *Intent:* /** * Filter function for sample keys. Applies multiple filters in pipeline fashion. * Each filter m...
  * `getFeatures` **(Defensive Guards)** (Impact: 22.9)
  * `init` **(Compute Cores)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 91 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 94`, `args: 37`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 103`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `api: 15`, `concurrency: 8`, `import: 11`
* *Defense:* `safety: 50`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.068
  * `Choke Point (Betweenness):` 0.000798 | `Ripple Effect (Closeness):` 0.081753
  * `Imports (Out-Degree: 11):` index.js, hicColorScale.js, igv-canvas.js, igv-icons.js, sampleInfo.js, sampleUtils.js, trackBase.js, colorPalletes.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/trackBase.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.978)
- **Top Global Matches:** file_cluster_6: 6.978, file_cluster_4: 9.453, file_cluster_8: 16.846
- **Magnitude:** 621.48 | **LOC:** 721 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **5**; blast radius 9.65; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.4%), Guard Balance (formerly Safety Score) (65.6%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setTrackProperties` **(Defensive Guards)** (Impact: 74.7)
    * *Intent:* /** * Set certain track properties, usually from a "track" line. Not all UCSC properties are support...
  * `extractPopupData` **(Many-Argument Workhorses)** (Impact: 42.1)
    * *Intent:* /** * Default popup text function -- just extracts string and number properties in random order. */
  * `init` **(Defensive Guards)** (Impact: 39.7)
    * *Intent:* /** * Initialize track properties from the config object. This method is typically overriden in subc...
  * `isJSONable` **(Defensive Guards)** (Impact: 29.2)
  * `getState` **(Defensive Guards)** (Impact: 21.5)
    * *Intent:* /** * Used to create session object for bookmarking, sharing. Only simple property values (string, n...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 80 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 81`, `args: 35`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 95`
* *Architecture:* `api: 18`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 47`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.65
  * `Choke Point (Betweenness):` 0.004776 | `Ripple Effect (Closeness):` 0.121759
  * `Imports (Out-Degree: 7):` index.js, featureUtils.js, igv-icons.js, igvUtils.js, sessionResourceValidator.js
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `js/trackViewport.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.313)
- **Top Global Matches:** file_cluster_4: 7.313, file_cluster_15: 7.983, file_cluster_11: 9.154
- **Magnitude:** 619.24 | **LOC:** 1100 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 1.603; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (74.9%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 85.4839% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addViewportClickHandler` **(Compute Cores)** (Impact: 38.5)
  * `checkZoomIn` **(Defensive Guards)** (Impact: 21.5)
    * *Intent:* /** * Test to determine if we are zoomed in far enough to see features. Applicable to tracks with vi...
  * `containsRange` **(Defensive Guards)** (Impact: 20.0)
  * `renderSVGContext` **(Many-Argument Workhorses)** (Impact: 18.8)
  * `repaint` **(I/O & Config Routines)** (Impact: 15.6)
    * *Intent:* /** * Repaint the canvas using the cached features * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 106`, `args: 61`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 101`, `dead_code: 6`, `fragile_debt: 1`
* *Architecture:* `api: 15`, `concurrency: 11`, `import: 9`
* *Defense:* `safety: 54`, `doc: 7`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.603
  * `Choke Point (Betweenness):` 0.001064 | `Ripple Effect (Closeness):` 0.085797
  * `Imports (Out-Degree: 11):` index.js, canvas2svg.js, genomeUtils.js, sequenceTrack.js, popover.js, dom-utils.js, draggable.js, icons.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `js/feature/render/renderFeature.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.334)
- **Top Global Matches:** file_cluster_3: 11.334, file_cluster_8: 32.463, file_cluster_1: 37.792
- **Magnitude:** 615.18 | **LOC:** 510 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.326; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.6%), Guard Balance (formerly Safety Score) (69.0%)
- **Documentation Coverage:** 64.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderAminoAcidSequence` **(Many-Argument Workhorses)** (Impact: 127.0)
  * `renderFeature` **(Many-Argument Workhorses)** (Impact: 99.8)
    * *Intent:* /** * */
  * `getAminoAcidLetterWithExonGap` **(Many-Argument Workhorses)** (Impact: 55.4)
  * `renderFeatureLabel` **(Many-Argument Workhorses)** (Impact: 47.9)
    * *Intent:* /** */
  * `doPaint` **(Many-Argument Workhorses)** (Impact: 47.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 216
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 56`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 78`, `dead_code: 2`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 33`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.326
  * `Choke Point (Betweenness):` 0.000691 | `Ripple Effect (Closeness):` 0.065402
  * `Imports (Out-Degree: 5):` igv-canvas.js, sequenceUtils.js, translationDict.js, exonUtils.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `js/trackView.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.817)
- **Top Global Matches:** file_cluster_15: 7.817, file_cluster_4: 8.165, file_cluster_11: 8.832
- **Magnitude:** 599.18 | **LOC:** 1030 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.993; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (60.4%), Guard Balance (formerly Safety Score) (54.8%), Connectivity (formerly Api Exposure) (44.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateViews` **(Defensive Guards)** (Impact: 41.5)
    * *Intent:* /** * Update viewports to reflect current genomic state, possibly loading additional data. * */
  * `addTrackDragMouseHandlers` **(Defensive Guards)** (Impact: 30.0)
  * `presentColorPicker` **(Defensive Guards)** (Impact: 26.8)
  * `setTrackHeight` **(Defensive Guards)** (Impact: 16.0)
  * `createTrackGearPopup` **(Defensive Guards)** (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 74`, `args: 66`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `state_mutation: 97`, `fragile_debt: 2`
* *Architecture:* `api: 14`, `concurrency: 4`, `import: 11`
* *Defense:* `safety: 75`, `doc: 9`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.993
  * `Choke Point (Betweenness):` 0.001352 | `Ripple Effect (Closeness):` 0.085286
  * `Imports (Out-Degree: 13):` index.js, sampleInfoViewport.js, sampleNameViewport.js, menuPopup.js, menuUtils.js, overlayTrackButton.js, dom-utils.js, icons.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/feature/featureTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.743)
- **Top Global Matches:** file_cluster_6: 6.743, file_cluster_4: 11.355, file_cluster_8: 14.76
- **Magnitude:** 575.42 | **LOC:** 577 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 1.542; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `draw` **(Compute Cores)** (Impact: 46.5)
    * *Intent:* * pixelXOffset, * pixelWidth, * pixelHeight, * pixelTop, * bpStart, * bpEnd: bpEnd, * bpPerPixel, * ...
  * `popupData` **(Defensive Guards)** (Impact: 46.5)
    * *Intent:* /** * Return "popup data" for feature @ genomic location. Data is an array of key-value pairs */
  * `getColorForFeature` **(Defensive Guards)** (Impact: 40.5)
    * *Intent:* /** * Return color for feature. */
  * `init` **(Compute Cores)** (Impact: 39.4)
  * `contextMenuItemList` **(Defensive Guards)** (Impact: 22.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 73`, `args: 26`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `concurrency: 10`, `import: 12`
* *Defense:* `safety: 50`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.002415 | `Ripple Effect (Closeness):` 0.0833
  * `Imports (Out-Degree: 12):` index.js, igv-canvas.js, igv-icons.js, trackBase.js, colorPalletes.js, igvUtils.js, sequenceUtils.js, featureSource.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/feature/wigTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.836)
- **Top Global Matches:** file_cluster_4: 6.836, file_cluster_6: 8.527, file_cluster_15: 13.289
- **Magnitude:** 540.88 | **LOC:** 575 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 1.749; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (94.3%), Complexity Load (formerly Cognitive Load) (92.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 91.8919% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `draw` **(Defensive Guards)** (Impact: 68.1)
  * `yScale` **(Defensive Guards)** (Impact: 67.5)
  * `getFeatures` **(Many-Argument Workhorses)** (Impact: 35.8)
  * `drawSVGPath` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `init` **(Defensive Guards)** (Impact: 24.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 67`, `args: 31`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 59`, `planned_debt: 1`
* *Architecture:* `api: 11`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 37`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.749
  * `Choke Point (Betweenness):` 0.003348 | `Ripple Effect (Closeness):` 0.082817
  * `Imports (Out-Degree: 12):` index.js, bwSource.js, igv-canvas.js, igv-icons.js, tdfSource.js, trackBase.js, colorScaleEditor.js, colorScale.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `js/genome/hgvs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.549)
- **Top Global Matches:** file_cluster_6: 8.549, file_cluster_8: 10.505, file_cluster_4: 16.151
- **Magnitude:** 537.32 | **LOC:** 599 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 1.769; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.8%), Concurrency Surface (formerly Concurrency) (70.8%), Guard Balance (formerly Safety Score) (64.4%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search` **(Many-Argument Workhorses)** (Impact: 152.5)
    * *Intent:* /** * Searches for the given HGVS notation in the provided genome. * Returns a SearchResult with the...
  * `createHGVSAnnotation` **(Many-Argument Workhorses)** (Impact: 117.3)
    * *Intent:* /** * Returns HGVS annotation for the position, for ref and alt bases. If a MANE transcript is avail...
  * `transcriptPositionToGenomicPosition` **(Defensive Guards)** (Impact: 24.8)
    * *Intent:* /** * Convert a transcript position (1-based, from transcription start) to genomic position * for no...
  * `getHGVSPosition` **(Defensive Guards)** (Impact: 23.3)
    * *Intent:* /** * Returns genomic HGVS notation: <RefSeqAccession>:g.<position> * Example: NC_000001.11:g.123456...
  * `codingToGenomePosition` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* /** * Translate a 1-based coding position to a 0-based genomic position. Supports HGVS parsing * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 51 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 88`, `args: 11`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 54`, `dead_code: 19`
* *Architecture:* `api: 1`, `concurrency: 10`, `import: 2`
* *Defense:* `safety: 27`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.769
  * `Choke Point (Betweenness):` 0.000295 | `Ripple Effect (Closeness):` 0.069115
  * `Imports (Out-Degree: 2):` exonUtils.js, searchFeatures.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `js/feature/featureParser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.664)
- **Top Global Matches:** file_cluster_3: 6.664, file_cluster_8: 20.549, file_cluster_6: 33.407
- **Magnitude:** 533.36 | **LOC:** 413 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 1.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setDecoder` **(Compute Cores)** (Impact: 79.8)
  * `parseHeader` **(Defensive Guards)** (Impact: 48.7)
    * *Intent:* /** * Parse metadata from the file. A variety of conventions are in use to supply metadata about fil...
  * `parseFeatures` **(Defensive Guards)** (Impact: 36.7)
  * `parseTrackLine` **(Defensive Guards)** (Impact: 34.9)
  * `constructor` **(Compute Cores)** (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 96 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 78`, `args: 9`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 96`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 4`, `import: 13`
* *Defense:* `safety: 23`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.068
  * `Choke Point (Betweenness):` 0.003764 | `Ripple Effect (Closeness):` 0.050199
  * `Imports (Out-Degree: 13):` gcnvDecoder.js, decodeShoebox.js, fileFormats.js, bedpe.js, custom.js, decodeError.js, fusionJuncSpan.js, gtexGWAS.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/feature/spliceJunctionTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.291)
- **Top Global Matches:** file_cluster_4: 6.291, file_cluster_15: 10.969, file_cluster_6: 11.021
- **Magnitude:** 515.22 | **LOC:** 407 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (93.5%), Complexity Load (formerly Cognitive Load) (86.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderJunction` **(Many-Argument Workhorses)** (Impact: 273.0)
    * *Intent:* /** * */
  * `popupData` **(Defensive Guards)** (Impact: 13.3)
    * *Intent:* /** * Return "popup data" for feature @ genomic location. Data is an array of key-value pairs */
  * `draw` **(Compute Cores)** (Impact: 11.9)
  * `postInit` **(Defensive Guards)** (Impact: 9.1)
  * `init` **(Compute Cores)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 48 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 51`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`, `planned_debt: 2`
* *Architecture:* `api: 9`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 46`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.068
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.08187
  * `Imports (Out-Degree: 5):` igv-canvas.js, trackBase.js, colorPalletes.js, featureSource.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.365)
- **Top Global Matches:** file_cluster_13: 7.365, file_cluster_12: 7.834, file_cluster_10: 8.014
- **Magnitude:** 511.87 | **LOC:** 257 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.7%), Complexity Load (formerly Cognitive Load) (7.4%), Connectivity (formerly Api Exposure) (4.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 28`, `args: 57`, `func_start: 2`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `io: 94`, `api: 2`, `concurrency: 1`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/aed/AEDParser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.169)
- **Top Global Matches:** file_cluster_8: 10.169, file_cluster_3: 15.282, file_cluster_6: 22.152
- **Magnitude:** 498.68 | **LOC:** 472 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.068; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.6%), Guard Balance (formerly Safety Score) (72.8%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AedFeature` **(Defensive Guards)** (Impact: 44.6)
    * *Intent:* /** * AED file feature. * * * Other values are parsed one by one */
  * `parseFeatures` **(Compute Cores)** (Impact: 41.3)
  * `decodeAed` **(Defensive Guards)** (Impact: 33.8)
    * *Intent:* /** * Decode the AED file format */
  * `parseHeader` **(Compute Cores)** (Impact: 25.6)
  * `parseTrackLine` **(Defensive Guards)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 65`, `args: 14`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 85`, `planned_debt: 1`
* *Architecture:* `api: 7`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 33`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.050155
  * `Imports (Out-Degree: 1):` index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/feature/featureFileReader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.548)
- **Top Global Matches:** file_cluster_4: 7.548, file_cluster_9: 10.727, file_cluster_6: 11.311
- **Magnitude:** 477.48 | **LOC:** 389 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **12**; blast radius 3.483; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `readFeatures` **(Defensive Guards)** (Impact: 23.6)
    * *Intent:* /** * Return a promise to load features for the genomic interval */
  * `loadFeaturesWithIndex` **(Many-Argument Workhorses)** (Impact: 22.1)
  * `readHeader` **(I/O & Config Routines)** (Impact: 20.5)
  * `constructor` **(Defensive Guards)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 164
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 96`, `args: 20`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 50`, `fragile_debt: 3`
* *Architecture:* `api: 4`, `concurrency: 39`, `import: 12`
* *Defense:* `safety: 13`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.483
  * `Choke Point (Betweenness):` 0.010861 | `Ripple Effect (Closeness):` 0.06043
  * `Imports (Out-Degree: 12):` index.js, AEDParser.js, bgzBlockLoader.js, indexFactory.js, gwasParser.js, qtlParser.js, bgzLineReader.js, igvUtils.js...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `js/bam/bamAlignment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.268)
- **Top Global Matches:** file_cluster_4: 6.268, file_cluster_15: 8.136, file_cluster_16: 9.89
- **Magnitude:** 463.46 | **LOC:** 520 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 1.552; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.5%)
- **Documentation Coverage:** 78.7234% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `popupData` **(Many-Argument Workhorses)** (Impact: 98.1)
    * *Intent:* /** * Return data to show in the popup. Elements are either strings (for raw HTML) or * objects with...
  * `getGroupValue` **(Compute Cores)** (Impact: 83.1)
  * `readBaseQualityAt` **(Defensive Guards)** (Impact: 13.6)
  * `getBaseModificationSets` **(Defensive Guards)** (Impact: 11.9)
  * `readBaseAt` **(Defensive Guards)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 84`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `dead_code: 1`
* *Architecture:* `api: 15`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 31`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.552
  * `Choke Point (Betweenness):` 0.000372 | `Ripple Effect (Closeness):` 0.046678
  * `Imports (Out-Degree: 6):` index.js, clinVar.js, hgvs.js, baseModificationUtils.js, orientationTypes.js, supplementaryAlignment.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `dev/gwas/gwas-specify-columns.html` (HTML) | Magnitude: 49.77 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 28, core_var_decl: 10, design_snake_case: 10, structural_boundaries: 7
- `dev/alignment/groupby.html` (HTML) | Magnitude: 27.74 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 7, core_var_decl: 6, design_snake_case: 6
- `js/ucsc/hub/trackConfigContainer.js` (JAVASCRIPT) | Magnitude: 39.18 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 48, args: 20, structural_boundaries: 17, comprehensions: 13
- `dev/misc/track_load_error.html` (HTML) | Magnitude: 27.76 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 8, core_var_decl: 7, design_snake_case: 6
- `examples/test/tracks-hg38.html` (HTML) | Magnitude: 13.98 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 123, core_var_decl: 23, design_snake_case: 21, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `js/sample/plinkSampleInformation.js` (JAVASCRIPT) | Magnitude: 38.18 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 16, args: 7, func_start: 7
- `test/testBigbed.js` (JAVASCRIPT) | Magnitude: 58.4 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 155, core_var_decl: 63, test: 51, design_snake_case: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `dev/ucsc/localFile/igvFileHelper.js` (JAVASCRIPT) | Magnitude: 139.46 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 131, branch: 26, core_var_decl: 21, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `dev/cnvpytor/old/not_indexed.html` (HTML) | Magnitude: 13.16 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 49, core_var_decl: 19, structural_boundaries: 15, design_snake_case: 13
- `dev/variant/noheader.html` (HTML) | Magnitude: 45.61 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 21, core_var_decl: 10, design_snake_case: 10, structural_boundaries: 5
- `dev/wig/merged.html` (HTML) | Magnitude: 71.34 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 11, core_var_decl: 11, decorators: 10
- `dev/htsget/htsget-bam.html` (HTML) | Magnitude: 47.69 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 24, core_var_decl: 10, design_snake_case: 10, structural_boundaries: 8
- `dev/annotation/bigbed.html` (HTML) | Magnitude: 26.9 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 9, core_var_decl: 7, design_snake_case: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `js/util/getChrColor.js` (JAVASCRIPT) | Magnitude: 16.16 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 5, branch: 4, core_var_decl: 3
- `js/ui/components/genericColorPicker.js` (JAVASCRIPT) | Magnitude: 78.78 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 32, core_var_decl: 24, structural_boundaries: 22
- `js/bam/bamReaderNonIndexed.js` (JAVASCRIPT) | Magnitude: 101.64 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 28, core_var_decl: 21, state_mutation: 17
- `js/bam/bamWebserviceReader.js` (JAVASCRIPT) | Magnitude: 48.96 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 15, core_var_decl: 10, state_mutation: 8
- `js/igv-icons.js` (JAVASCRIPT) | Magnitude: 8.58 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, core_var_decl: 4, design_snake_case: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/testEmbed.html` (HTML) | Magnitude: 15.48 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 5, core_var_decl: 4, design_snake_case: 4
- `dev/gcnv/gcnv.html` (HTML) | Magnitude: 59.41 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, core_var_decl: 11, design_snake_case: 10, structural_boundaries: 7
- `dev/seg/copyNumber.html` (HTML) | Magnitude: 59.03 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 13, core_var_decl: 10, design_snake_case: 9
- `js/ui/viewportCenterLine.js` (JAVASCRIPT) | Magnitude: 40.96 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 39, state_mutation: 12, branch: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `js/qtl/qtlParser.js` (JAVASCRIPT) | Magnitude: 161.86 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 132, branch: 42, state_mutation: 31, core_var_decl: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/testAED.js` (JAVASCRIPT) | Magnitude: 23.6 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 22, test: 8, structural_boundaries: 7, core_var_decl: 6
- `js/cnvpytor/cnvpytorVCF.js` (JAVASCRIPT) | Magnitude: 179.22 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 47, state_mutation: 35, core_var_decl: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `js/util/ucscUtils.js` (JAVASCRIPT) | Magnitude: 33.48 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 34, branch: 12, core_var_decl: 10, design_snake_case: 8
- `js/feature/gff/gffFeature.js` (JAVASCRIPT) | Magnitude: 254.62 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 207, branch: 71, state_mutation: 45, structural_boundaries: 44
- `js/htsget/htsgetBamReader.js` (JAVASCRIPT) | Magnitude: 58.86 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 17, branch: 9, core_var_decl: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `js/browser.js` -> Churn: **69.82%** | Cog Load: 74.7147% | Debt: 12.112%
- `js/bam/alignmentTrack.js` -> Churn: **67.59%** | Cog Load: 90.2838% | Debt: 16.0858%
- `js/bam/bamAlignment.js` -> Churn: **67.55%** | Cog Load: 82.0187% | Debt: 0.0%
- `js/feature/wigTrack.js` -> Churn: **62.23%** | Cog Load: 92.6787% | Debt: 8.455%
- `js/feature/render/renderFeature.js` -> Churn: **57.88%** | Cog Load: 74.5572% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `js/variant/variantTrack.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 848.22
- `js/cnvpytor/cnvpytorTrack.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 841.98
- `js/bam/alignmentContainer.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 718.34
- `js/trackBase.js` -> **Douglass Turner** (100.0% isolated ownership) | Magnitude: 621.48
- `js/genome/hgvs.js` -> **Jim Robinson** (100.0% isolated ownership) | Magnitude: 537.32

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `js/browser.js` -> **Severity: 5.253** (Bridge: 0.0525 * Flux: 99.9992%)
- `js/trackFactory.js` -> **Severity: 3.34** (Bridge: 0.0339 * Flux: 98.6166%)
- `js/index.js` -> **Severity: 1.288** (Bridge: 0.0796 * Flux: 16.1747%)
- `js/bam/bamTrack.js` -> **Severity: 1.147** (Bridge: 0.0115 * Flux: 99.9962%)
- `js/feature/featureFileReader.js` -> **Severity: 1.086** (Bridge: 0.0109 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/index.js` -> **Severity: 9.267** (Embedded: 0.1828 * Error Risk: 50.6849%)
- `js/util/igvUtils.js` -> **Severity: 8.51** (Embedded: 0.126 * Error Risk: 67.5133%)
- `js/ui/utils/dom-utils.js` -> **Severity: 8.406** (Embedded: 0.136 * Error Risk: 61.8115%)
- `js/igv-create.js` -> **Severity: 8.051** (Embedded: 0.112 * Error Risk: 71.8924%)
- `js/ui/components/alertDialog.js` -> **Severity: 8.012** (Embedded: 0.1143 * Error Risk: 70.1266%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `js/index.js` -> **Severity: 6583.8** (Blast Radius: 65.838 * Doc Risk: 100.0%)
- `js/ui/utils/dom-utils.js` -> **Severity: 3672.0** (Blast Radius: 39.78 * Doc Risk: 92.3077%)
- `js/util/igvUtils.js` -> **Severity: 1714.521** (Blast Radius: 19.717 * Doc Risk: 86.9565%)
- `js/ui/utils/icons.js` -> **Severity: 1268.9** (Blast Radius: 12.689 * Doc Risk: 100.0%)
- `js/igv-canvas.js` -> **Severity: 1117.2** (Blast Radius: 11.172 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 312 literal sites + 4 sites through wrappers = 316

- `getParserFor` (function, debug_prints, primitive): 4 call sites in 1 files -- `js/bigwig/bpTree.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 8163 call pairs -- scoped 32.7%, unique 0.0%, ambiguous 26.1%, external 41.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 7773 | 33.5% | 0.0% | 27.4% | 39.1% |
| html | 389 | 16.5% | 0.0% | 0.0% | 83.5% |
| shell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
