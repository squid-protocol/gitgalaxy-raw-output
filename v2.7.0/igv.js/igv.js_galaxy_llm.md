# ARCHITECTURAL_BRIEF: igv.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/igvteam/igv.js.git` |
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
| Total Artifacts | 3377 |
| Analyzed Artifacts (Scanned) | 687 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2690 |
| Total LOC | 78851 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 20.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.548 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.172 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 19.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4394 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 47 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 360 | 45455 | 52.4% |
| HTML | 206 | 28826 | 30.0% |
| PLAINTEXT | 50 | 0 | 7.3% |
| CSS | 34 | 3204 | 4.9% |
| JSON | 18 | 794 | 2.6% |
| XML | 9 | 0 | 1.3% |
| MARKDOWN | 5 | 0 | 0.7% |
| CSV | 2 | 13 | 0.3% |
| SHELL | 1 | 13 | 0.1% |
| TYPESCRIPT | 1 | 545 | 0.1% |
| BINARY_THREAT | 1 | 1 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 631 | 91.8% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 55 | 8.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2690*

**Composition by Extension & Reason:**
- `no_extension`: 2436x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.FusionJuncSpan'), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.bed`: 28x Excluded (Unsupported Extension: '.bed')
- `.vcf`: 20x Excluded (Unsupported Extension: '.vcf')
- `.bam`: 14x Excluded (Unsupported Extension: '.bam')
- `.gz`: 14x Excluded (Explicitly Denied Extension: '.gz')
- `.bai`: 13x Excluded (Unsupported Extension: '.bai')
- `.js`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.git-id`: 10x Excluded (Unsupported Extension: '.git-id')
- `.html`: 2x Excluded (Saturation: Line 29 exceeds 500 chars), 1x Excluded (Saturation: Line 26 exceeds 500 chars), 1x Excluded (Saturation: Line 30 exceeds 500 chars)
- `.tbi`: 8x Excluded (Unsupported Extension: '.tbi')
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.wig`: 7x Excluded (Unsupported Extension: '.wig')
- `.bedpe`: 7x Excluded (Unsupported Extension: '.bedpe')
- `.gff3`: 7x Excluded (Unsupported Extension: '.gff3')
- `.bedgraph`: 6x Excluded (Unsupported Extension: '.bedgraph')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 27.5 | 8.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 44.3 | 53.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 84.5 | 17.7 | 7.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 24.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 82.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.3 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 96.3 | 5.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 43.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 90 | 48 | 0 | `js/feature/decode/ucsc.js` |
| cleanup | 98 | 25 | 0 | `js/trackView.js` |
| guards | 2605 | 298 | 9 | `js/browser.js` |
| danger | 601 | 154 | 2 | `dev/dev.html` |
| concurrency | 1826 | 365 | 8 | `js/browser.js` |
| connectivity | 2057 | 486 | 7 | `js/igv.d.ts` |
| io | 875 | 123 | 2 | `dev/dev.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 15 | 6 | 0 | `dev/ucsc/localFile/file-picker.html` |
| time | 49 | 19 | 0 | `dev/misc/interactive-filtering.html` |
| serialization | 39 | 25 | 0 | `dev/ucsc/localFile/trackJS_additions.js` |
| regex | 350 | 113 | 2 | `js/feature/featureParser.js` |
| events | 711 | 192 | 4 | `test/utils/w3XMLHttpRequest.js` |
| tests | 1278 | 71 | 1 | `test/testBaseMods.js` |
| docs | 836 | 383 | 2 | `test/utils/w3XMLHttpRequest.js` |
| debt | 478 | 235 | 2 | `test/testDynseq.js` |
| mutation | 20109 | 560 | 70 | `js/cnvpytor/MeanShiftUtil.js` |
| dead_code | 444 | 100 | 1 | `js/feature/intervalTree.js` |
| credential | 190 | 66 | 0 | `dev/misc/functional-url.html` |
| threat | 474 | 252 | 2 | `test/utils/w3XMLHttpRequest.js` |
| ml_ai | 2 | 2 | 0 | `findLarge.sh` |
| ui | 904 | 237 | 3 | `css/_navbar.scss` |

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

1. **index.js** (`js/index.js`) — 96 inbound connections
2. **dom-utils.js** (`js/ui/utils/dom-utils.js`) — 44 inbound connections
3. **featureSource.js** (`js/feature/featureSource.js`) — 28 inbound connections
4. **igv-canvas.js** (`js/igv-canvas.js`) — 27 inbound connections
5. **MockGenome.js** (`test/utils/MockGenome.js`) — 25 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **browser.js** (`js/browser.js`) — 51 outbound dependencies
2. **trackFactory.js** (`js/trackFactory.js`) — 19 outbound dependencies
3. **index.js** (`js/index.js`) — 15 outbound dependencies
4. **responsiveNavbar.js** (`js/responsiveNavbar.js`) — 15 outbound dependencies
5. **alignmentTrack.js** (`js/bam/alignmentTrack.js`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `renderJunction` (@ `js/feature/spliceJunctionTrack.js`) -> Impact: **273.0** | LOC: 221
  * *Intent:* /** * * @param feature * @param bpStart genomic location of the left edge of the current canvas * @param xScale scale in base-pairs per pixel * @param...
- `draw` (@ `js/bam/alignmentTrack.js`) -> Impact: **176.1** | LOC: 467
- `drawSingleAlignment` (@ `js/bam/alignmentTrack.js`) -> Impact: **171.2** | LOC: 303
- `call_2d` (@ `js/cnvpytor/CombinedCaller.js`) -> Impact: **166.7** | LOC: 336
- `search` (@ `js/genome/hgvs.js`) -> Impact: **154.2** | LOC: 244
  * *Intent:* /** * Searches for the given HGVS notation in the provided genome. * Returns a SearchResult with the corresponding chromosome and position if found, *...
- `renderAminoAcidSequence` (@ `js/feature/render/renderFeature.js`) -> Impact: **127.0** | LOC: 152
- `createHGVSAnnotation` (@ `js/genome/hgvs.js`) -> Impact: **117.3** | LOC: 141
  * *Intent:* /** * Returns HGVS annotation for the position, for ref and alt bases. If a MANE transcript is available that is * used with coding notation (c.), oth...
- `decodeBed` (@ `js/feature/decode/ucsc.js`) -> Impact: **107.8** | LOC: 115
  * *Intent:* /** * Decode the UCSC bed format. Only the first 3 columns (chr, start, end) are required. The remaining columns * must follow standard bed order, but...
- `readAlignments` (@ `js/cram/cramReader.js`) -> Impact: **104.5** | LOC: 210
- `renderFeature` (@ `js/feature/render/renderFeature.js`) -> Impact: **99.8** | LOC: 144
  * *Intent:* /** * * @param feature * @param bpStart genomic location of the left edge of the current canvas * @param xScale scale in base-pairs per pixel * @param...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `js` | 29 | 7666.91 | 56.14% | 8.3% |
| `js/feature` | 26 | 6964.92 | 65.76% | 8.89% |
| `js/bam` | 25 | 5779.42 | 64.39% | 7.65% |
| `js/cnvpytor` | 8 | 3168.66 | 65.53% | 2.38% |
| `js/genome` | 21 | 2722.36 | 54.85% | 5.73% |
| `test` | 61 | 2436.76 | 11.16% | 0.0% |
| `examples` | 36 | 2091.86 | 5.37% | 0.0% |
| `js/bigwig` | 9 | 1661.6 | 74.14% | 3.78% |
| `js/ui` | 20 | 1467.38 | 52.6% | 5.66% |
| `js/variant` | 3 | 1402.48 | 82.6% | 3.46% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `js/ui/igvTable.js` -> **99.9965%** Exposure
- `dev/cbio/cbio.js` -> **99.3307%** Exposure
- `js/bam/packedAlignments.js` -> **99.3307%** Exposure
- `js/igv.d.ts` -> **98.0142%** Exposure
- `js/ui/components/textbox.js` -> **73.1059%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `dev/cbio/cbio.js` -> **100.0%** Exposure
- `js/aed/AEDParser.js` -> **100.0%** Exposure
- `js/bam/alignmentContainer.js` -> **100.0%** Exposure
- `js/bam/bamIndex.js` -> **100.0%** Exposure
- `js/bam/bamReaderNonIndexed.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/testDynseq.js` -> **3** Orphaned Functions | **21** Duplicates
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
- **Binary Anomalies (X-Ray):** `63` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `262` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/bam/pairedAlignment.js` (JAVASCRIPT) -> Cumulative Risk: **770.94**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 225.9 | **LOC:** 196 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.9434%)
- **Heaviest Functions:** `getGroupValue` (Impact: 65.5), `alignmentContaining` (Impact: 10.8), `getTag` (Impact: 8.9)

### 2. `js/feature/baseFeatureSource.js` (JAVASCRIPT) -> Cumulative Risk: **770.94**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 117.58 | **LOC:** 71 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.6106%)
- **Heaviest Functions:** `nextFeature` (Impact: 51.8), `compare` (Impact: 22.5), `constructor` (Impact: 1.6)

### 3. `js/roi/ROIManager.js` (JAVASCRIPT) -> Cumulative Risk: **761.08**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 252.3 | **LOC:** 388 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9937%), Concurrency (99.95%)
- **Heaviest Functions:** `loadROI` (Impact: 16.7), `renderROISet` (Impact: 16.3), `createRegionElement` (Impact: 10.3)

### 4. `js/cnvpytor/cnvpytorTrack.js` (JAVASCRIPT) -> Cumulative Risk: **755.47**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 842.68 | **LOC:** 699 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.3738%)
- **Heaviest Functions:** `draw` (Impact: 48.9), `paintAxis` (Impact: 42.3), `postInit` (Impact: 26.1)

### 5. `js/feature/wigTrack.js` (JAVASCRIPT) -> Cumulative Risk: **750.67**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 543.08 | **LOC:** 575 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Concurrency (94.3251%), Cognitive Load (92.7117%)
- **Heaviest Functions:** `draw` (Impact: 68.1), `yScale` (Impact: 67.5), `getFeatures` (Impact: 38.0)

### 6. `js/variant/variantTrack.js` (JAVASCRIPT) -> Cumulative Risk: **750.17**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 853.52 | **LOC:** 1031 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.8702%), Safety Score (82.9462%)
- **Heaviest Functions:** `draw` (Impact: 74.7), `postInit` (Impact: 27.6), `sortSamplesByGenotype` (Impact: 24.2)

### 7. `js/sequenceTrack.js` (JAVASCRIPT) -> Cumulative Risk: **736.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 368.68 | **LOC:** 390 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (90.0979%)
- **Heaviest Functions:** `draw` (Impact: 36.0), `contextMenuItemList` (Impact: 21.7), `constructor` (Impact: 13.5)

### 8. `js/ucsc/hub/hub.js` (JAVASCRIPT) -> Cumulative Risk: **733.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 367.74 | **LOC:** 422 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9983%), Safety Score (92.072%)
- **Heaviest Functions:** `getTrackConfig` (Impact: 44.1), `getGenomeConfig` (Impact: 33.8), `loadHub` (Impact: 20.4)

### 9. `js/qtl/qtlTrack.js` (JAVASCRIPT) -> Cumulative Risk: **728.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 427.88 | **LOC:** 343 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9569%), Safety Score (94.0181%)
- **Heaviest Functions:** `draw` (Impact: 34.8), `drawEqtls` (Impact: 31.4), `dialogPresentationHandler` (Impact: 30.5)

### 10. `js/feature/textFeatureSource.js` (JAVASCRIPT) -> Cumulative Risk: **727.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 385.2 | **LOC:** 281 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9999%), Safety Score (91.3936%)
- **Heaviest Functions:** `loadFeatures` (Impact: 56.8), `constructor` (Impact: 47.6), `getFeatures` (Impact: 25.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/browser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1838.44 | **LOC:** 2683 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 73.3%
- **Risk Profile:** Cognitive Load (74.7187%), Tech Debt (12.5792%)
**Top Internal Functions/Classes:**
  * `loadSessionObject` (Impact: 79.0)
    * *Intent:* /** * Note: public API function * @param session * @returns {Promise<void>} */
  * `createTrack` (Impact: 50.6)
    * *Intent:* /** * Create a Track object. * @param config * @returns {Promise<*>} */
  * `loadGenome` (Impact: 38.1)
    * *Intent:* /** * Load a genome, defined by a string ID or a json-like configuration object. This includes a fas...
  * `keyUpHandler` (Impact: 33.6)
    * *Intent:* /** * Handle keyup event, used for navigating feature tracks with hot keys. This will get bound to t...
  * `_validateAndWarnResources` (Impact: 30.5)
    * *Intent:* /** * Validate reference genome and warn about problematic resources in the session. * * Reference g...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 183 instances
* *Concurrency (weighted view):* 279
* *State Mutation (weighted view):* 614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 421`, `structural_boundaries: 308`, `args: 162`, `func_start: 123`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 248`, `dead_code: 4`, `planned_debt: 6`, `fragile_debt: 4`
* *Architecture:* `api: 38`, `concurrency: 89`, `import: 51`
* *Defense:* `safety: 117`, `doc: 43`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.040454 | `Ripple Effect (Closeness):` 0.112434
  * `Imports (Out-Degree: 49):` index.js, blatTrack.js, canvas2svg.js, embedCss.js, events.js, featureSource.js, genbankParser.js, genome.js...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `js/bam/alignmentTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1535.56 | **LOC:** 1587 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (89.8346%), Tech Debt (17.3505%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 176.1)
  * `drawSingleAlignment` (Impact: 171.2)
  * `drawBlock` (Impact: 79.9)
  * `contextMenuItemList` (Impact: 77.1)
  * `getAlignmentColor` (Impact: 56.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 152 instances
* *State Mutation (weighted view):* 517
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 169`, `args: 85`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 213`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 20`, `concurrency: 7`, `import: 14`
* *Defense:* `safety: 70`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.001991 | `Ripple Effect (Closeness):` 0.063204
  * `Imports (Out-Degree: 13):` index.js, blatTrack.js, igv-canvas.js, igv-icons.js, trackBase.js, dom-utils.js, colorPalletes.js, getChrColor.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/feature/interactionTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1062.78 | **LOC:** 1034 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (77.7914%), Tech Debt (12.2239%)
**Top Internal Functions/Classes:**
  * `drawProportional` (Impact: 70.4)
  * `drawNested` (Impact: 55.6)
  * `getWGFeatures` (Impact: 42.3)
    * *Intent:* /** * Called in the context of FeatureSource (i.e. this == the feature source (a TextFeatureSource) ...
  * `makeWGFeature` (Impact: 42.2)
  * `init` (Impact: 37.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 149 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 467
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 129`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `state_mutation: 169`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 17`, `concurrency: 5`, `import: 11`
* *Defense:* `safety: 70`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.211
  * `Choke Point (Betweenness):` 0.000507 | `Ripple Effect (Closeness):` 0.08092
  * `Imports (Out-Degree: 11):` index.js, igv-canvas.js, igv-icons.js, circularViewUtils.js, trackBase.js, dom-utils.js, colorPalletes.js, getChrColor.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `js/cnvpytor/MeanShiftUtil.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1056.44 | **LOC:** 1089 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.6465%), Tech Debt (8.8364%)
**Top Internal Functions/Classes:**
  * `meanShiftCaller` (Impact: 68.1)
  * `call_mean_shift` (Impact: 60.6)
  * `cnv_calling` (Impact: 57.3)
  * `cnvCalling` (Impact: 57.1)
  * `partition` (Impact: 55.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 208 instances
* *State Mutation (weighted view):* 659
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 302`, `args: 47`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 243`, `dead_code: 25`, `planned_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 2`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.113
  * `Choke Point (Betweenness):` 0.00035 | `Ripple Effect (Closeness):` 0.051949
  * `Imports (Out-Degree: 3):` GeneralUtil.js, baseCNVpytorVCF.js, t_dist.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/canvas2svg.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 885.48 | **LOC:** 1398 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.4003%), Tech Debt (10.4672%)
**Top Internal Functions/Classes:**
  * `arcTo` (Impact: 38.6)
    * *Intent:* /** * Adds the arcTo to the current path * * @see http://www.w3.org/TR/2015/WD-2dcontext-20150514/#d...
  * `__applyStyleToCurrentElement` (Impact: 35.7)
    * *Intent:* /** * Apples the current styles to the current SVG element. On "ctx.fill" or "ctx.stroke" * @param t...
  * `__parseFont` (Impact: 31.6)
    * *Intent:* /** * Parses the font string and returns svg mapping * @private */
  * `arc` (Impact: 28.7)
    * *Intent:* /** * Arc command! */
  * `drawImage` (Impact: 26.2)
    * *Intent:* /** * Draws a canvas, image or mock context to this canvas. * Note that all svg dom manipulation use...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 415
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 108`, `args: 70`, `func_start: 69`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 173`, `dead_code: 4`, `planned_debt: 5`
* *Architecture:* `api: 33`
* *Defense:* `safety: 49`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.081991
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `js/bam/bamUtils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 879.72 | **LOC:** 700 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.7097%), Tech Debt (9.4683%)
**Top Internal Functions/Classes:**
  * `bam_tag2cigar` (Impact: 90.2)
  * `decodeBamRecords` (Impact: 84.5)
    * *Intent:* /** * * @param ba bytes to decode as an UInt8Array * @param offset offset position of ba array to st...
  * `decodeSamRecords` (Impact: 61.9)
  * `decodeBamTags` (Impact: 51.1)
    * *Intent:* /** * Decode bam tags from the supplied UInt8Array * * A [!-~] Printable character * i [-+]?[0-9]+ S...
  * `makeBlocks` (Impact: 33.7)
    * *Intent:* /** * Split the alignment record into blocks as specified in the cigarArray. Each aligned block cont...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 107`, `args: 16`, `func_start: 14`
* *Risk/State:* `state_mutation: 169`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 67`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.000467 | `Ripple Effect (Closeness):` 0.046307
  * `Imports (Out-Degree: 4):` index.js, alignmentBlock.js, bamAlignment.js, bamFilter.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `js/variant/variantTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 853.52 | **LOC:** 1031 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (82.7638%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 74.7)
  * `postInit` (Impact: 27.6)
  * `sortSamplesByGenotype` (Impact: 24.2)
  * `getFeatures` (Impact: 21.4)
  * `getColorForFeature` (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 108 instances
* *Concurrency (weighted view):* 79
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 113`, `args: 52`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 121`, `dead_code: 23`
* *Architecture:* `api: 18`, `concurrency: 14`, `import: 12`
* *Defense:* `safety: 79`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.3
  * `Choke Point (Betweenness):` 0.000769 | `Ripple Effect (Closeness):` 0.081157
  * `Imports (Out-Degree: 12):` index.js, featureSource.js, featureUtils.js, igv-canvas.js, igv-icons.js, circularViewUtils.js, sampleInfo.js, sampleUtils.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/cnvpytor/cnvpytorTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 842.68 | **LOC:** 699 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.5353%), Tech Debt (10.2267%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 48.9)
  * `paintAxis` (Impact: 42.3)
  * `postInit` (Impact: 26.1)
  * `getFeatures` (Impact: 24.6)
  * `recreate_tracks` (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 115 instances
* *Concurrency (weighted view):* 132
* *State Mutation (weighted view):* 373
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 119`, `args: 43`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 143`, `dead_code: 4`, `planned_debt: 2`
* *Architecture:* `api: 12`, `concurrency: 27`, `import: 7`
* *Defense:* `safety: 21`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.392
  * `Choke Point (Betweenness):` 0.002453 | `Ripple Effect (Closeness):` 0.080684
  * `Imports (Out-Degree: 7):` featureSource.js, igv-canvas.js, igv-icons.js, trackBase.js, trackClassRegistry.js, HDF5IndexedReader.js, cnvpytorVCF.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/bigwig/bwReader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 817.8 | **LOC:** 744 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.1283%), Tech Debt (10.0879%)
**Top Internal Functions/Classes:**
  * `readFeatures` (Impact: 51.5)
  * `decodeWigData` (Impact: 50.4)
  * `decodeZoomData` (Impact: 47.0)
  * `loadHeader` (Impact: 23.5)
    * *Intent:* /** * The BB header consists of * (1) the common header * (2) the zoom headers * (3) autosql * (4) t...
  * `search` (Impact: 18.6)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.445
  * `Choke Point (Betweenness):` 0.001745 | `Ripple Effect (Closeness):` 0.059989
  * `Imports (Out-Degree: 8):` index.js, binary.js, igvUtils.js, ucscUtils.js, bbDecoders.js, bpTree.js, chromTree.js, rpTree.js...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `js/bam/alignmentContainer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 750.24 | **LOC:** 763 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (71.9552%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `packAlignmentRows` (Impact: 58.9)
  * `incCounts` (Impact: 31.6)
  * `packFull` (Impact: 28.5)
  * `getPosCount` (Impact: 27.3)
  * `getNegCount` (Impact: 27.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 118`, `args: 54`, `func_start: 42`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 132`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `safety: 20`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.000766 | `Ripple Effect (Closeness):` 0.046346
  * `Imports (Out-Degree: 3):` igvUtils.js, bamAlignmentRow.js, baseModificationCounts.js, pairedAlignment.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `js/feature/render/renderFeature.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 668.28 | **LOC:** 510 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (74.5572%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderAminoAcidSequence` (Impact: 127.0)
  * `renderFeature` (Impact: 99.8)
    * *Intent:* /** * * @param feature * @param bpStart genomic location of the left edge of the current canvas * @p...
  * `doPaint` (Impact: 99.2)
  * `getAminoAcidLetterWithExonGap` (Impact: 55.4)
  * `renderFeatureLabel` (Impact: 47.9)
    * *Intent:* /** * @param ctx the canvas 2d context * @param feature * @param featureX feature start in pixel coo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 216
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 56`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 78`, `dead_code: 2`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 33`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.79
  * `Choke Point (Betweenness):` 0.000165 | `Ripple Effect (Closeness):` 0.064755
  * `Imports (Out-Degree: 4):` igv-canvas.js, sequenceUtils.js, translationDict.js, exonUtils.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `js/trackViewport.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 651.14 | **LOC:** 1100 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (55.2098%), Tech Debt (9.8818%)
**Top Internal Functions/Classes:**
  * `addViewportClickHandler` (Impact: 38.5)
  * `checkZoomIn` (Impact: 21.5)
    * *Intent:* /** * Test to determine if we are zoomed in far enough to see features. Applicable to tracks with vi...
  * `zoomedOutOfWindow` (Impact: 21.4)
  * `containsRange` (Impact: 20.0)
  * `mu` (Impact: 19.1)
    * *Intent:* // Mouse up
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 106`, `args: 61`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 101`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 18`, `concurrency: 11`, `import: 9`
* *Defense:* `safety: 54`, `doc: 7`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.665
  * `Choke Point (Betweenness):` 0.000746 | `Ripple Effect (Closeness):` 0.081755
  * `Imports (Out-Degree: 8):` index.js, canvas2svg.js, genomeUtils.js, sequenceTrack.js, popover.js, dom-utils.js, draggable.js, icons.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `dev/misc/interactive-filtering.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 649.14 | **LOC:** 1500 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.0727%), Tech Debt (10.0955%)
**Top Internal Functions/Classes:**
  * `updateFilterCounts` (Impact: 33.7)
    * *Intent:* /** Get counts for each filter, in each facet */
  * `buildFilter` (Impact: 28.7)
    * *Intent:* /** * Build a filter function taking an igvFeature as an argument and returning true for "pass" (sho...
  * `initFacets` (Impact: 25.3)
    * *Intent:* * // For integer or float: numeric values observed for this facet * "filterNumbers": [<Number>], * *...
  * `handleBrushMove` (Impact: 17.9)
    * *Intent:* /** Handle slider move event (i.e., drag or resize) */
  * `getInputStyle` (Impact: 15.5)
    * *Intent:* /** * Get width and font size for input, to help keep full value glanceable */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 148`, `args: 69`, `func_start: 58`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 106`, `dead_code: 1`, `planned_debt: 7`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 33`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` popper.min.js, crossfilter2@1.5.4, d3-array.js, d3-brush.js, d3-dispatch.js, d3-interpolate.js, d3-scale.js, d3-selection.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/trackBase.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 649.08 | **LOC:** 721 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (65.0217%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setTrackProperties` (Impact: 74.7)
    * *Intent:* /** * Set certain track properties, usually from a "track" line. Not all UCSC properties are support...
  * `extractPopupData` (Impact: 42.1)
    * *Intent:* /** * Default popup text function -- just extracts string and number properties in random order. * @...
  * `init` (Impact: 39.7)
    * *Intent:* /** * Initialize track properties from the config object. This method is typically overriden in subc...
  * `isJSONable` (Impact: 29.3)
  * `createKeyValueRow` (Impact: 25.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 80 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 81`, `args: 35`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 95`, `dead_code: 2`
* *Architecture:* `api: 19`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 47`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.451
  * `Choke Point (Betweenness):` 0.001065 | `Ripple Effect (Closeness):` 0.119719
  * `Imports (Out-Degree: 4):` index.js, featureUtils.js, igv-icons.js, igvUtils.js, sessionResourceValidator.js
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `js/feature/segTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 637.3 | **LOC:** 760 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.3032%), Tech Debt (11.0351%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 55.1)
  * `computeRegionScores` (Impact: 24.6)
  * `filter` (Impact: 23.9)
    * *Intent:* /** * Filter function for sample keys. Applies multiple filters in pipeline fashion. * Each filter m...
  * `getFeatures` (Impact: 22.9)
  * `init` (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 90 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 94`, `args: 37`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 103`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `api: 15`, `concurrency: 8`, `import: 11`
* *Defense:* `safety: 50`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.111
  * `Choke Point (Betweenness):` 0.000613 | `Ripple Effect (Closeness):` 0.080567
  * `Imports (Out-Degree: 10):` index.js, hicColorScale.js, igv-canvas.js, igv-icons.js, sampleInfo.js, sampleUtils.js, trackBase.js, colorPalletes.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/trackView.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 605.58 | **LOC:** 1030 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (60.3901%), Tech Debt (12.4802%)
**Top Internal Functions/Classes:**
  * `updateViews` (Impact: 41.5)
    * *Intent:* /** * Update viewports to reflect current genomic state, possibly loading additional data. * * @para...
  * `addTrackDragMouseHandlers` (Impact: 30.0)
  * `presentColorPicker` (Impact: 26.8)
  * `setTrackHeight` (Impact: 16.0)
  * `createTrackGearPopup` (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 74`, `args: 66`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `state_mutation: 97`, `fragile_debt: 2`
* *Architecture:* `api: 14`, `concurrency: 4`, `import: 11`
* *Defense:* `safety: 75`, `doc: 9`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.966
  * `Choke Point (Betweenness):` 0.001085 | `Ripple Effect (Closeness):` 0.080802
  * `Imports (Out-Degree: 9):` index.js, sampleInfoViewport.js, sampleNameViewport.js, menuPopup.js, menuUtils.js, overlayTrackButton.js, dom-utils.js, icons.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/feature/featureTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 579.22 | **LOC:** 577 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.8525%), Tech Debt (12.5011%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 46.5)
    * *Intent:* * pixelXOffset, * pixelWidth, * pixelHeight, * pixelTop, * bpStart, * bpEnd: bpEnd, * bpPerPixel, * ...
  * `popupData` (Impact: 46.5)
    * *Intent:* /** * Return "popup data" for feature @ genomic location. Data is an array of key-value pairs */
  * `getColorForFeature` (Impact: 40.5)
    * *Intent:* /** * Return color for feature. * @param feature * @returns {string} */
  * `init` (Impact: 39.4)
  * `contextMenuItemList` (Impact: 22.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 73`, `args: 26`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `concurrency: 10`, `import: 12`
* *Defense:* `safety: 50`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.62
  * `Choke Point (Betweenness):` 0.001435 | `Ripple Effect (Closeness):` 0.082485
  * `Imports (Out-Degree: 10):` index.js, igv-canvas.js, igv-icons.js, trackBase.js, colorPalletes.js, igvUtils.js, sequenceUtils.js, featureSource.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/genome/hgvs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 546.12 | **LOC:** 599 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (78.2654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `search` (Impact: 154.2)
    * *Intent:* /** * Searches for the given HGVS notation in the provided genome. * Returns a SearchResult with the...
  * `createHGVSAnnotation` (Impact: 117.3)
    * *Intent:* /** * Returns HGVS annotation for the position, for ref and alt bases. If a MANE transcript is avail...
  * `transcriptPositionToGenomicPosition` (Impact: 24.8)
    * *Intent:* /** * Convert a transcript position (1-based, from transcription start) to genomic position * for no...
  * `getHGVSPosition` (Impact: 23.3)
    * *Intent:* /** * Returns genomic HGVS notation: <RefSeqAccession>:g.<position> * Example: NC_000001.11:g.123456...
  * `codingToGenomePosition` (Impact: 15.6)
    * *Intent:* /** * Translate a 1-based coding position to a 0-based genomic position. Supports HGVS parsing * * @...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 51 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 88`, `args: 11`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 54`, `dead_code: 23`
* *Architecture:* `api: 1`, `concurrency: 10`, `import: 2`
* *Defense:* `safety: 27`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.924
  * `Choke Point (Betweenness):` 0.000269 | `Ripple Effect (Closeness):` 0.066623
  * `Imports (Out-Degree: 2):` exonUtils.js, searchFeatures.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `js/feature/wigTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 543.08 | **LOC:** 575 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (92.7117%), Tech Debt (9.9286%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 68.1)
  * `yScale` (Impact: 67.5)
  * `getFeatures` (Impact: 38.0)
  * `drawSVGPath` (Impact: 25.7)
  * `init` (Impact: 24.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 67`, `args: 31`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 59`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 11`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 37`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.00199 | `Ripple Effect (Closeness):` 0.081635
  * `Imports (Out-Degree: 11):` index.js, bwSource.js, igv-canvas.js, igv-icons.js, tdfSource.js, trackBase.js, colorScaleEditor.js, colorScale.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `js/feature/featureParser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 533.36 | **LOC:** 413 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.3384%), Tech Debt (13.5469%)
**Top Internal Functions/Classes:**
  * `setDecoder` (Impact: 79.8)
  * `parseHeader` (Impact: 48.7)
    * *Intent:* /** * Parse metadata from the file. A variety of conventions are in use to supply metadata about fil...
  * `parseFeatures` (Impact: 36.7)
  * `parseTrackLine` (Impact: 34.9)
  * `constructor` (Impact: 11.0)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.003275 | `Ripple Effect (Closeness):` 0.049097
  * `Imports (Out-Degree: 13):` gcnvDecoder.js, decodeShoebox.js, fileFormats.js, bedpe.js, custom.js, decodeError.js, fusionJuncSpan.js, gtexGWAS.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/feature/spliceJunctionTrack.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 530.12 | **LOC:** 407 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.9718%), Tech Debt (12.8017%)
**Top Internal Functions/Classes:**
  * `renderJunction` (Impact: 273.0)
    * *Intent:* /** * * @param feature * @param bpStart genomic location of the left edge of the current canvas * @p...
  * `drawArrowhead` (Impact: 14.6)
  * `popupData` (Impact: 13.3)
    * *Intent:* /** * Return "popup data" for feature @ genomic location. Data is an array of key-value pairs */
  * `draw` (Impact: 11.9)
  * `postInit` (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 51`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`, `planned_debt: 2`
* *Architecture:* `api: 10`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 46`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.080684
  * `Imports (Out-Degree: 4):` igv-canvas.js, trackBase.js, colorPalletes.js, featureSource.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 511.87 | **LOC:** 257 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (7.4172%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 28`, `args: 57`, `func_start: 2`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `io: 94`, `api: 2`, `concurrency: 1`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/aed/AEDParser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 500.08 | **LOC:** 472 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.7489%), Tech Debt (10.6095%)
**Top Internal Functions/Classes:**
  * `AedFeature` (Impact: 44.6)
    * *Intent:* /** * AED file feature. * * @param aed link to the AED file object containing file-level metadata an...
  * `parseFeatures` (Impact: 41.3)
  * `decodeAed` (Impact: 33.8)
    * *Intent:* /** * Decode the AED file format * @param tokens * @param ignore * @returns decoded feature, or null...
  * `parseHeader` (Impact: 25.6)
  * `parseTrackLine` (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 65`, `args: 14`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 85`, `planned_debt: 1`
* *Architecture:* `api: 7`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 33`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049053
  * `Imports (Out-Degree: 1):` index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/data/misc/BufferedReaderTest.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/featureFileReader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 477.48 | **LOC:** 389 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.76%), Tech Debt (32.8653%)
**Top Internal Functions/Classes:**
  * `_parse` (Impact: 33.7)
  * `readFeatures` (Impact: 23.6)
    * *Intent:* /** * Return a promise to load features for the genomic interval * @param chr * @param start * @para...
  * `loadFeaturesWithIndex` (Impact: 22.1)
  * `readHeader` (Impact: 20.5)
  * `constructor` (Impact: 18.6)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.525
  * `Choke Point (Betweenness):` 0.006411 | `Ripple Effect (Closeness):` 0.058968
  * `Imports (Out-Degree: 11):` index.js, AEDParser.js, bgzBlockLoader.js, indexFactory.js, gwasParser.js, qtlParser.js, bgzLineReader.js, igvUtils.js...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `js/browser.js` -> Churn: **96.34%** | Cog Load: 74.7187% | Debt: 12.5792%
- `js/feature/render/renderFeature.js` -> Churn: **65.24%** | Cog Load: 74.5572% | Debt: 0.0%
- `js/trackViewport.js` -> Churn: **64.0%** | Cog Load: 55.2098% | Debt: 9.8818%
- `js/bam/alignmentTrack.js` -> Churn: **59.88%** | Cog Load: 89.8346% | Debt: 17.3505%
- `js/bam/bamAlignment.js` -> Churn: **53.52%** | Cog Load: 82.0187% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `js/variant/variantTrack.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 853.52
- `js/cnvpytor/cnvpytorTrack.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 842.68
- `js/bam/alignmentContainer.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 750.24
- `js/trackViewport.js` -> **jrobinso** (83.3% isolated ownership) | Magnitude: 651.14
- `js/feature/segTrack.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 637.3

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `js/browser.js` -> **Severity: 4.045** (Bridge: 0.0405 * Flux: 99.9992%)
- `js/trackFactory.js` -> **Severity: 2.834** (Bridge: 0.0287 * Flux: 98.6166%)
- `js/index.js` -> **Severity: 1.219** (Bridge: 0.0754 * Flux: 16.1747%)
- `js/bam/bamTrack.js` -> **Severity: 0.929** (Bridge: 0.0093 * Flux: 99.9962%)
- `js/feature/textFeatureSource.js` -> **Severity: 0.832** (Bridge: 0.0083 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/index.js` -> **Severity: 11.481** (Embedded: 0.1794 * Error Risk: 63.9995%)
- `js/ui/components/alertDialog.js` -> **Severity: 10.714** (Embedded: 0.1127 * Error Risk: 95.0734%)
- `js/igv-create.js` -> **Severity: 10.552** (Embedded: 0.1102 * Error Risk: 95.7529%)
- `js/trackBase.js` -> **Severity: 10.547** (Embedded: 0.1197 * Error Risk: 88.0962%)
- `js/ucsc/hub/hub.js` -> **Severity: 10.458** (Embedded: 0.1136 * Error Risk: 92.072%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `js/index.js` -> **Severity: 7756.3** (Blast Radius: 77.563 * Doc Risk: 100.0%)
- `js/ui/utils/dom-utils.js` -> **Severity: 2428.985** (Blast Radius: 26.314 * Doc Risk: 92.3077%)
- `js/util/colorPalletes.js` -> **Severity: 1602.8** (Blast Radius: 16.028 * Doc Risk: 100.0%)
- `js/igv-canvas.js` -> **Severity: 1347.9** (Blast Radius: 13.479 * Doc Risk: 100.0%)
- `js/util/sequenceUtils.js` -> **Severity: 881.7** (Blast Radius: 8.817 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
