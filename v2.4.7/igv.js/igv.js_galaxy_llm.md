# ARCHITECTURAL_BRIEF: igv.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/igv.js` |
| **Timestamp** | `2026-08-07T04:26:18.719572+00:00` |
| **Scan Duration** | `1.83s` |
| **Git Branch** | `master` |
| **Git Commit** | `020ed83d7371c3b9a361766b68c280592bc1e574` |
| **Git Remote** | `https://github.com/igvteam/igv.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 291 malicious artifacts.

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
| Total Artifacts | 3377 |
| Analyzed Artifacts (Scanned) | 559 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2818 |
| Total LOC | 66595 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 16.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 288 | 33923 | 51.5% |
| HTML | 198 | 28593 | 35.4% |
| CSS | 34 | 3204 | 6.1% |
| PLAINTEXT | 15 | 0 | 2.7% |
| JSON | 10 | 316 | 1.8% |
| XML | 6 | 0 | 1.1% |
| MARKDOWN | 5 | 0 | 0.9% |
| SHELL | 1 | 13 | 0.2% |
| TYPESCRIPT | 1 | 545 | 0.2% |
| BINARY_THREAT | 1 | 1 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.106`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 324 | 58.0% |
| file_cluster_4 | 112 | 20.0% |
| file_cluster_13 | 58 | 10.4% |
| file_cluster_17 | 18 | 3.2% |
| file_cluster_0 | 16 | 2.9% |
| file_cluster_11 | 7 | 1.3% |
| file_cluster_9 | 1 | 0.2% |
| file_cluster_12 | 1 | 0.2% |
| file_cluster_16 | 1 | 0.2% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 20 | 3.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2818*

**Composition by Extension & Reason:**
- `no_extension`: 2438x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 78x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.txt`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bed`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vcf`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 29 exceeds 500 chars), 1x Excluded (Saturation: Line 26 exceeds 500 chars)
- `.bam`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gz`: 14x Excluded (Explicitly Denied Extension: '.gz')
- `.bai`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.bai')
- `.git-id`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.git-id')
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tbi`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.wig`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bedpe`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 37.4 | 32.2 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 56.1 | 69.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 16.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 13.4 | 4.8 | 4.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 20.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 49.0 | 45.1 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 96.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.3 | 2.1 | 0.2 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.5 | 5.4 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 47.3 | 42.4 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `dev/dev.html` (Hits: 312)
- `examples/index.html` (Hits: 94)
- `js/genome/updateReference.js` (Hits: 76)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **README.md** (`dev/cnvpytor/old/README.md`) — 0 inbound connections
4. **README.md** (`examples/cBio/README.md`) — 0 inbound connections
5. **updating_cram-bundle.md** (`js/cram/updating_cram-bundle.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **browser.js** (`js/browser.js`) — 51 outbound dependencies
2. **trackFactory.js** (`js/trackFactory.js`) — 19 outbound dependencies
3. **index.js** (`js/index.js`) — 15 outbound dependencies
4. **responsiveNavbar.js** (`js/responsiveNavbar.js`) — 15 outbound dependencies
5. **alignmentTrack.js** (`js/bam/alignmentTrack.js`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `loadSessionObject` (@ `js/browser.js`) -> Impact: **396.3** | LOC: 1206
- `url` (@ `js/igv.d.ts`) -> Impact: **255.4** | LOC: 327
- `drawSingleAlignment` (@ `js/bam/alignmentTrack.js`) -> Impact: **233.8** | LOC: 355
- `draw` (@ `js/bam/alignmentTrack.js`) -> Impact: **228.1** | LOC: 518
- `search` (@ `js/bigwig/bwReader.js`) -> Impact: **200.2** | LOC: 470
- `call_2d` (@ `js/cnvpytor/CombinedCaller.js`) -> Impact: **192.2** | LOC: 336
  * *Intent:* /** * Creates an instance of CombinedCaller. * * @param {Array} wigFeatures - An array of arrays containing wig formatted data for each chromosome and...
- `renderAminoAcidSequence` (@ `js/feature/render/renderFeature.js`) -> Impact: **127.0** | LOC: 152
- `handleMessage` (@ `js/websocket/messageHandler.js`) -> Impact: **119.2** | LOC: 167
  * *Intent:* /** * Handles incoming messages from the WebSocket connection. Performs requested actions on the IGV browser instance * and returns a response message...
- `setDecoder` (@ `js/feature/featureParser.js`) -> Impact: **115.2** | LOC: 126
  * *Intent:* // Special hack for bedPE
- `decodeBed` (@ `js/feature/decode/ucsc.js`) -> Impact: **111.8** | LOC: 115
  * *Intent:* /**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `js` | 29 | 9480.25 | 55.34% | 29.35% |
| `js/feature` | 26 | 8138.32 | 62.99% | 50.07% |
| `js/bam` | 25 | 5991.06 | 59.79% | 18.29% |
| `js/cnvpytor` | 7 | 3144.0 | 45.76% | 31.02% |
| `js/genome` | 21 | 2941.22 | 58.27% | 16.63% |
| `js/bigwig` | 9 | 2702.68 | 60.65% | 25.65% |
| `js/ui` | 20 | 2015.4 | 67.93% | 24.78% |
| `js/variant` | 3 | 1614.5 | 75.34% | 12.05% |
| `js/sample` | 8 | 1455.42 | 61.09% | 33.38% |
| `js/ui/components` | 13 | 1261.74 | 58.58% | 39.62% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `js/bam/packedAlignments.js` -> **100.0%** Exposure
- `js/roi/ROISet.js` -> **100.0%** Exposure
- `js/sample/plinkSampleInformation.js` -> **100.0%** Exposure
- `js/ui/components/colorScaleEditor.js` -> **100.0%** Exposure
- `js/ui/components/textbox.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `dev/cnvpytor/old/computeDepthFeatures.js` -> **100.0%** Exposure
- `js/aed/AEDParser.js` -> **100.0%** Exposure
- `js/bam/alignmentContainer.js` -> **100.0%** Exposure
- `js/bam/alignmentTrack.js` -> **100.0%** Exposure
- `js/bam/bamAlignment.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/utils/w3XMLHttpRequest.js` -> **0** Orphaned Functions | **37** Duplicates
- `js/util/colorScale.js` -> **0** Orphaned Functions | **28** Duplicates
- `js/ui/components/colorScaleEditor.js` -> **0** Orphaned Functions | **25** Duplicates
- `dev/sessions/sessionTestHarness.html` -> **0** Orphaned Functions | **20** Duplicates
- `js/bam/alignmentContainer.js` -> **0** Orphaned Functions | **17** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`js/feature/featureParser.js`** -> AI Confidence: **99.48%**
2. **`js/bam/alignmentTrack.js`** -> AI Confidence: **99.35%**
3. **`js/gwas/gwasTrack.js`** -> AI Confidence: **99.34%**
4. **`js/sample/sampleInfoViewport.js`** -> AI Confidence: **99.34%**
5. **`js/bam/bamSource.js`** -> AI Confidence: **99.31%**
6. **`js/bam/bamTrack.js`** -> AI Confidence: **99.31%**
7. **`js/bigwig/bwReader.js`** -> AI Confidence: **99.31%**
8. **`js/browser.js`** -> AI Confidence: **99.31%**
9. **`js/feature/featureSource.js`** -> AI Confidence: **99.31%**
10. **`js/feature/featureTrack.js`** -> AI Confidence: **99.31%**
11. **`js/feature/interactionTrack.js`** -> AI Confidence: **99.31%**
12. **`js/feature/segTrack.js`** -> AI Confidence: **99.31%**
13. **`js/feature/textFeatureSource.js`** -> AI Confidence: **99.31%**
14. **`js/feature/wigTrack.js`** -> AI Confidence: **99.31%**
15. **`js/genome/genome.js`** -> AI Confidence: **99.31%**
16. **`js/responsiveNavbar.js`** -> AI Confidence: **99.31%**
17. **`js/rna/rnaStruct.js`** -> AI Confidence: **99.31%**
18. **`js/sequenceTrack.js`** -> AI Confidence: **99.31%**
19. **`js/trackView.js`** -> AI Confidence: **99.31%**
20. **`js/trackViewport.js`** -> AI Confidence: **99.31%**
21. **`js/variant/variantTrack.js`** -> AI Confidence: **99.31%**
22. **`js/bigwig/bbDecoders.js`** -> AI Confidence: **99.29%**
23. **`js/genome/chromAliasDefaults.js`** -> AI Confidence: **99.29%**
24. **`js/session/igvXmlSession.js`** -> AI Confidence: **99.29%**
25. **`js/util/trackUtils.js`** -> AI Confidence: **99.29%**
26. **`js/feature/featureFileReader.js`** -> AI Confidence: **99.24%**
27. **`js/rulerViewport.js`** -> AI Confidence: **99.24%**
28. **`js/roi/ROIManager.js`** -> AI Confidence: **99.23%**
29. **`js/trackBase.js`** -> AI Confidence: **99.23%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `76` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `190` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/feature/staticFeatureSource.js` (JAVASCRIPT) -> Cumulative Risk: **755.36**
- **Archetype:** `file_cluster_4` (Distance: 22.208 IQR)
- **Magnitude:** 168.82 | **LOC:** 193 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9463%), Tech Debt (98.0069%)
- **Heaviest Functions:** `addFeaturesToDB` (Impact: 20.3), `updateFeatures` (Impact: 7.8), `mapProperties` (Impact: 7.4)

### 2. `js/roi/ROISet.js` (JAVASCRIPT) -> Cumulative Risk: **749.88**
- **Archetype:** `file_cluster_4` (Distance: 13.454 IQR)
- **Magnitude:** 271.84 | **LOC:** 207 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9922%)
- **Heaviest Functions:** `constructor` (Impact: 31.8), `constructor` (Impact: 9.7), `toJSON` (Impact: 8.4)

### 3. `js/sequenceTrack.js` (JAVASCRIPT) -> Cumulative Risk: **747.88**
- **Archetype:** `file_cluster_4` (Distance: 13.249 IQR)
- **Magnitude:** 536.08 | **LOC:** 390 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9313%)
- **Heaviest Functions:** `draw` (Impact: 38.8), `contextMenuItemList` (Impact: 24.5), `constructor` (Impact: 13.5)

### 4. `js/bam/pairedAlignment.js` (JAVASCRIPT) -> Cumulative Risk: **737.33**
- **Archetype:** `file_cluster_4` (Distance: 13.603 IQR)
- **Magnitude:** 363.9 | **LOC:** 196 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.7385%), Cognitive Load (99.4026%)
- **Heaviest Functions:** `getGroupValue` (Impact: 65.5), `alignmentContaining` (Impact: 10.8), `getTag` (Impact: 8.9)

### 5. `js/feature/segParser.js` (JAVASCRIPT) -> Cumulative Risk: **729.5**
- **Archetype:** `file_cluster_4` (Distance: 14.441 IQR)
- **Magnitude:** 378.04 | **LOC:** 188 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9992%), Safety Score (99.746%)
- **Heaviest Functions:** `popupData` (Impact: 17.1), `extractCravatLink` (Impact: 16.5), `parseFeatures` (Impact: 15.7)

### 6. `js/gwas/gwasParser.js` (JAVASCRIPT) -> Cumulative Risk: **727.16**
- **Archetype:** `file_cluster_4` (Distance: 12.957 IQR)
- **Magnitude:** 165.46 | **LOC:** 159 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9968%), Tech Debt (96.8139%)
- **Heaviest Functions:** `parseHeaderLine` (Impact: 28.3), `constructor` (Impact: 9.4), `parseFeatures` (Impact: 7.9)

### 7. `js/tdf/tdfSource.js` (JAVASCRIPT) -> Cumulative Risk: **715.81**
- **Archetype:** `file_cluster_4` (Distance: 12.106 IQR)
- **Magnitude:** 255.44 | **LOC:** 202 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9918%), Cognitive Load (95.7457%)
- **Heaviest Functions:** `_getFeatures` (Impact: 44.4), `getWGValues` (Impact: 17.1), `decodeFixedTile` (Impact: 17.0)

### 8. `js/feature/baseFeatureSource.js` (JAVASCRIPT) -> Cumulative Risk: **714.6**
- **Archetype:** `file_cluster_4` (Distance: 11.77 IQR)
- **Magnitude:** 119.58 | **LOC:** 71 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9988%), Cognitive Load (99.1343%)
- **Heaviest Functions:** `nextFeature` (Impact: 54.0), `compare` (Impact: 14.8), `constructor` (Impact: 1.6)

### 9. `js/roi/ROIMenu.js` (JAVASCRIPT) -> Cumulative Risk: **711.21**
- **Archetype:** `file_cluster_4` (Distance: 12.006 IQR)
- **Magnitude:** 199.76 | **LOC:** 185 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9839%)
- **Heaviest Functions:** `menuItems` (Impact: 25.4), `addCopySequenceMenuItem` (Impact: 7.8), `click` (Impact: 7.6)

### 10. `js/roi/ROIManager.js` (JAVASCRIPT) -> Cumulative Risk: **707.41**
- **Archetype:** `file_cluster_4` (Distance: 13.101 IQR)
- **Magnitude:** 463.0 | **LOC:** 388 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.983%)
- **Heaviest Functions:** `loadROI` (Impact: 16.7), `createRegionElement` (Impact: 10.3), `dispose` (Impact: 9.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/browser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.158 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.961 IQR)
- **Top Global Matches:** file_cluster_4: 15.158, file_cluster_13: 15.32, file_cluster_17: 15.547
- **Magnitude:** 2362.7 | **LOC:** 2683 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (49.865%), Tech Debt (23.3267%)
**Top Internal Functions/Classes:**
  * `loadSessionObject` (Impact: 396.3)
  * `keyUpHandler` (Impact: 46.0)
    * *Intent:* // Zoom out by a factor of 2, keeping the same center location if possible
  * `toJSON` (Impact: 31.8)
  * `_validateAndWarnResources` (Impact: 30.5)
  * `loadSessionFile` (Impact: 27.6)
    * *Intent:* // TODO: deprecated
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 200`, `args: 107`, `func_start: 89`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 1110`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `api: 25`, `concurrency: 218`, `import: 51`
* *Defense:* `safety: 57`, `doc: 72`, `immutability_locks: 158`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` canvas2svg.js, dataRangeDialog.js, genbankParser.js, ideogramTrack.js, sampleInfoConstants.js, menuUtils.js, menuPopup.js, version.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/interactionTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.078 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.232 IQR)
- **Top Global Matches:** file_cluster_4: 15.078, file_cluster_11: 15.144, file_cluster_13: 15.195
- **Magnitude:** 1473.28 | **LOC:** 1034 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (75.7923%), Tech Debt (87.8426%)
**Top Internal Functions/Classes:**
  * `drawProportional` (Impact: 76.0)
  * `drawNested` (Impact: 58.4)
  * `getWGFeatures` (Impact: 50.9)
  * `menuItemList` (Impact: 39.2)
  * `init` (Impact: 37.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 118`, `args: 47`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 858`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `api: 13`, `concurrency: 30`, `import: 11`
* *Defense:* `safety: 70`, `doc: 11`, `immutability_locks: 109`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, igv-canvas.js, circularViewUtils.js, getChrColor.js, colorPalletes.js, igv-icons.js, trackBase.js, dom-utils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/bigwig/bwReader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.086 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.851 IQR)
- **Top Global Matches:** file_cluster_4: 14.086, file_cluster_13: 14.749, file_cluster_11: 14.856
- **Magnitude:** 1454.28 | **LOC:** 744 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.3892%), Tech Debt (64.3339%)
**Top Internal Functions/Classes:**
  * `search` (Impact: 200.2)
  * `decodeWigData` (Impact: 65.3)
  * `decodeZoomData` (Impact: 59.0)
  * `readFeatures` (Impact: 51.5)
  * `loadHeader` (Impact: 36.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 120`, `args: 29`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 555`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 12`, `api: 8`, `concurrency: 305`, `import: 9`
* *Defense:* `safety: 31`, `doc: 23`, `immutability_locks: 85`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` trix.js, index.js, bpTree.js, binary.js, chromTree.js, bbDecoders.js, igvUtils.js, rpTree.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/cnvpytor/MeanShiftUtil.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.06 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.654 IQR)
- **Top Global Matches:** file_cluster_17: 16.06, file_cluster_11: 16.272, file_cluster_4: 16.293
- **Magnitude:** 1410.74 | **LOC:** 1089 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.6551%), Tech Debt (66.6298%)
**Top Internal Functions/Classes:**
  * `call_mean_shift` (Impact: 101.7)
  * `partition` (Impact: 91.2)
    * *Intent:* // The values are reversed and squared as they will be used to calculate a gradient function. // Thi...
  * `meanShiftCaller` (Impact: 85.4)
  * `cnv_calling` (Impact: 81.2)
  * `cnvCalling` (Impact: 59.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 270`, `args: 47`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 877`, `dead_code: 25`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 2`
* *Defense:* `doc: 4`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` baseCNVpytorVCF.js, GeneralUtil.js, t_dist.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/trackView.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.246 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.465 IQR)
- **Top Global Matches:** file_cluster_13: 15.246, file_cluster_17: 15.253, file_cluster_4: 15.295
- **Magnitude:** 1280.38 | **LOC:** 1030 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (64.6585%), Tech Debt (83.0178%)
**Top Internal Functions/Classes:**
  * `updateViews` (Impact: 67.8)
  * `addTrackDragMouseHandlers` (Impact: 30.0)
  * `presentColorPicker` (Impact: 26.8)
  * `getInViewFeatures` (Impact: 20.7)
  * `setTrackHeight` (Impact: 16.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 74`, `args: 66`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `state_mutation: 826`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 11`, `concurrency: 19`, `import: 11`
* *Defense:* `safety: 75`, `doc: 17`, `immutability_locks: 73`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sampleNameViewport.js, viewportUtils.js, menuUtils.js, menuPopup.js, index.js, dom-utils.js, igvUtils.js, sampleInfoViewport.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/bam/alignmentTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.908 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.159 IQR)
- **Top Global Matches:** file_cluster_13: 13.908, file_cluster_8: 14.011, file_cluster_17: 14.151
- **Magnitude:** 1186.44 | **LOC:** 1587 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (84.92%), Tech Debt (89.6766%)
**Top Internal Functions/Classes:**
  * `drawSingleAlignment` (Impact: 233.8)
  * `draw` (Impact: 228.1)
  * `getAlignmentColor` (Impact: 68.1)
  * `constructor` (Impact: 46.8)
  * `getClickedObject` (Impact: 23.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 78`, `args: 34`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 456`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 9`, `import: 14`
* *Defense:* `safety: 26`, `doc: 8`, `immutability_locks: 66`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` baseModificationRenderer.js, index.js, igv-canvas.js, blatTrack.js, getChrColor.js, colorPalletes.js, baseModificationUtils.js, igv-icons.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/trackViewport.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.864 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.466 IQR)
- **Top Global Matches:** file_cluster_4: 14.864, file_cluster_13: 15.023, file_cluster_8: 15.068
- **Magnitude:** 1182.5 | **LOC:** 1100 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (68.6635%), Tech Debt (32.7318%)
**Top Internal Functions/Classes:**
  * `checkZoomIn` (Impact: 29.4)
  * `loadFeatures` (Impact: 28.8)
  * `addViewportClickHandler` (Impact: 26.3)
  * `repaint` (Impact: 20.6)
  * `containsRange` (Impact: 20.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 82`, `args: 47`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 779`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 14`, `concurrency: 36`, `import: 9`
* *Defense:* `safety: 40`, `doc: 13`, `immutability_locks: 107`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` viewport.js, canvas2svg.js, draggable.js, genomeUtils.js, sequenceTrack.js, index.js, dom-utils.js, icons.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/variant/variantTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 18.663 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.614 IQR)
- **Top Global Matches:** file_cluster_4: 18.663, file_cluster_17: 18.798, file_cluster_11: 18.862
- **Magnitude:** 1160.24 | **LOC:** 1031 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.1023%), Tech Debt (20.067%)
**Top Internal Functions/Classes:**
  * `postInit` (Impact: 45.9)
  * `menuItemList` (Impact: 27.4)
    * *Intent:* // } else if (aNan) { // return 1; // } else if (bNan) { // return -1; // } else { // var a0 = getAl...
  * `getFeatures` (Impact: 21.4)
  * `getColorForFeature` (Impact: 21.1)
  * `clickedFeatures` (Impact: 17.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 74`, `args: 32`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 835`, `dead_code: 23`, `duplicate_logic: 2`
* *Architecture:* `api: 12`, `concurrency: 48`, `import: 12`
* *Defense:* `safety: 64`, `doc: 5`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, igv-canvas.js, sampleUtils.js, circularViewUtils.js, featureSource.js, sampleInfo.js, colorPalletes.js, igv-icons.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/bam/alignmentContainer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.8 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.314 IQR)
- **Top Global Matches:** file_cluster_8: 13.8, file_cluster_17: 13.904, file_cluster_13: 13.914
- **Magnitude:** 1027.54 | **LOC:** 763 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.6289%), Tech Debt (99.2522%)
**Top Internal Functions/Classes:**
  * `packAlignmentRows` (Impact: 58.6)
  * `incCounts` (Impact: 34.5)
  * `getPosCount` (Impact: 27.3)
  * `getNegCount` (Impact: 27.3)
  * `sortRows` (Impact: 24.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 115`, `args: 54`, `func_start: 48`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 552`, `duplicate_logic: 17`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 20`, `doc: 9`, `immutability_locks: 55`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` baseModificationCounts.js, bamAlignmentRow.js, pairedAlignment.js, igvUtils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/segTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.96 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.472 IQR)
- **Top Global Matches:** file_cluster_4: 14.96, file_cluster_13: 15.199, file_cluster_17: 15.228
- **Magnitude:** 991.8 | **LOC:** 760 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (78.3401%), Tech Debt (11.0727%)
**Top Internal Functions/Classes:**
  * `computeRegionScores` (Impact: 28.0)
  * `filter` (Impact: 23.9)
    * *Intent:* /**
  * `getFeatures` (Impact: 22.9)
  * `init` (Impact: 20.6)
  * `sortByValue` (Impact: 20.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 78`, `args: 33`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 678`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 12`, `concurrency: 48`, `import: 11`
* *Defense:* `safety: 44`, `doc: 9`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, igv-canvas.js, sampleUtils.js, sampleInfo.js, colorPalletes.js, igv-icons.js, hicColorScale.js, colorScale.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/trackBase.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.698 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.271 IQR)
- **Top Global Matches:** file_cluster_4: 14.698, file_cluster_13: 14.7, file_cluster_11: 14.746
- **Magnitude:** 833.98 | **LOC:** 721 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (48.9101%), Tech Debt (20.1772%)
**Top Internal Functions/Classes:**
  * `setTrackProperties` (Impact: 93.1)
  * `extractPopupData` (Impact: 42.1)
  * `init` (Impact: 39.7)
  * `getState` (Impact: 30.8)
  * `description` (Impact: 22.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 68`, `args: 35`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 429`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 15`, `concurrency: 13`, `import: 5`
* *Defense:* `safety: 47`, `doc: 37`, `immutability_locks: 42`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sessionResourceValidator.js, index.js, igvUtils.js, igv-icons.js, featureUtils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/genome/genome.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.277 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_4: 14.277, file_cluster_13: 14.648, file_cluster_8: 14.873
- **Magnitude:** 758.34 | **LOC:** 467 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.8555%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 50.1)
  * `getManeTranscriptAt` (Impact: 18.4)
  * `generateGenomeID` (Impact: 17.9)
  * `getAliasRecord` (Impact: 17.0)
  * `getManeTranscript` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 86`, `args: 36`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 383`
* *Architecture:* `api: 15`, `concurrency: 116`, `import: 11`
* *Defense:* `safety: 17`, `doc: 21`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` loadSequence.js, cytobandFile.js, index.js, chromosome.js, chromAliasFile.js, chromAliasBB.js, bwSource.js, chromAliasDefaults.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/bam/bamAlignment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.641 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.195 IQR)
- **Top Global Matches:** file_cluster_4: 14.641, file_cluster_13: 14.685, file_cluster_11: 14.829
- **Magnitude:** 751.76 | **LOC:** 520 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (67.7086%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `popupData` (Impact: 98.1)
  * `getGroupValue` (Impact: 83.1)
  * `getBaseModificationSets` (Impact: 16.5)
  * `readBaseQualityAt` (Impact: 13.6)
  * `softClippedBlocks` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 84`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 408`, `dead_code: 2`
* *Architecture:* `api: 15`, `concurrency: 13`, `import: 6`
* *Defense:* `safety: 31`, `doc: 14`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, clinVar.js, baseModificationUtils.js, hgvs.js, supplementaryAlignment.js, orientationTypes.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/featureParser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.206 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.329 IQR)
- **Top Global Matches:** file_cluster_13: 14.206, file_cluster_4: 14.214, file_cluster_8: 14.35
- **Magnitude:** 744.26 | **LOC:** 413 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.7142%), Tech Debt (12.7273%)
**Top Internal Functions/Classes:**
  * `setDecoder` (Impact: 115.2)
    * *Intent:* // Special hack for bedPE
  * `parseHeader` (Impact: 65.8)
  * `parseFeatures` (Impact: 54.8)
  * `parseTrackLine` (Impact: 43.9)
  * `constructor` (Impact: 11.0)
    * *Intent:* /** * Parser for column style (tab delimited, etc) text file formats (bed, gff, vcf, etc). * * */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 44`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 396`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 24`, `import: 13`
* *Defense:* `safety: 23`, `doc: 5`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bedpe.js, gff.js, ucsc.js, decodeShoebox.js, fusionJuncSpan.js, gffHelper.js, fileFormats.js, decodeError.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/featureFileReader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.927 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.061 IQR)
- **Top Global Matches:** file_cluster_4: 13.927, file_cluster_13: 14.547, file_cluster_17: 14.654
- **Magnitude:** 679.58 | **LOC:** 389 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.5163%), Tech Debt (25.0795%)
**Top Internal Functions/Classes:**
  * `readHeader` (Impact: 32.2)
  * `readFeatures` (Impact: 23.6)
  * `loadFeaturesWithIndex` (Impact: 22.1)
  * `constructor` (Impact: 18.6)
    * *Intent:* /** * Reader for "bed like" files (tab delimited files with 1 feature per line: bed, gff, vcf, etc) ...
  * `getParser` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 85`, `args: 17`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 319`, `fragile_debt: 2`
* *Architecture:* `api: 4`, `concurrency: 199`, `import: 12`
* *Defense:* `safety: 11`, `doc: 6`, `immutability_locks: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bgzLineReader.js, segParser.js, index.js, gwasParser.js, AEDParser.js, bgzBlockLoader.js, vcfParser.js, dataWrapper.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/wigTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.286 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.308 IQR)
- **Top Global Matches:** file_cluster_4: 14.286, file_cluster_13: 14.494, file_cluster_11: 14.618
- **Magnitude:** 616.86 | **LOC:** 575 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (83.8904%), Tech Debt (55.0503%)
**Top Internal Functions/Classes:**
  * `getFeatures` (Impact: 42.5)
  * `drawSVGPath` (Impact: 25.7)
  * `init` (Impact: 24.7)
  * `popupData` (Impact: 21.5)
  * `draw` (Impact: 14.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 53`, `args: 30`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 327`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `concurrency: 42`, `import: 11`
* *Defense:* `safety: 29`, `doc: 4`, `immutability_locks: 39`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, igv-canvas.js, tdfSource.js, colorScaleEditor.js, igv-icons.js, bwSource.js, colorScale.js, wigSummary.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/cnvpytor/CombinedCaller.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.448 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.422 IQR)
- **Top Global Matches:** file_cluster_17: 14.448, file_cluster_4: 14.777, file_cluster_11: 14.827
- **Magnitude:** 608.28 | **LOC:** 521 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.1966%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `call_2d` (Impact: 192.2)
    * *Intent:* /** * Creates an instance of CombinedCaller. * * @param {Array} wigFeatures - An array of arrays con...
  * `normal_merge` (Impact: 9.4)
  * `formatDataStructure` (Impact: 6.8)
  * `likelihood_baf_pval` (Impact: 6.0)
    * *Intent:* /** * Calculates two normal distributions overlap area. * * @param {float} m1 - Mean value of the fi...
  * `likelihood_overlap` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 139`, `args: 35`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 355`, `dead_code: 4`
* *Architecture:* `api: 3`, `concurrency: 7`, `import: 3`
* *Defense:* `safety: 9`, `doc: 33`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` baseCNVpytorVCF.js, GeneralUtil.js, t_dist.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/render/renderFeature.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.535 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.567 IQR)
- **Top Global Matches:** file_cluster_8: 13.535, file_cluster_13: 13.545, file_cluster_11: 13.655
- **Magnitude:** 601.48 | **LOC:** 510 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (43.0306%), Tech Debt (86.7442%)
**Top Internal Functions/Classes:**
  * `renderAminoAcidSequence` (Impact: 127.0)
  * `renderFeature` (Impact: 110.4)
  * `getAminoAcidLetterWithExonGap` (Impact: 55.4)
  * `renderFeatureLabel` (Impact: 53.5)
  * `doPaint` (Impact: 47.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 54`, `args: 8`, `func_start: 13`
* *Risk/State:* `state_mutation: 166`, `dead_code: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 33`, `doc: 20`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translationDict.js, igv-canvas.js, sequenceUtils.js, exonUtils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/misc/interactive-filtering.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.431 IQR)
- **Top Global Matches:** file_cluster_17: 11.431, file_cluster_8: 11.436, file_cluster_0: 11.632
- **Magnitude:** 600.5 | **LOC:** 1500 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.6703%), Tech Debt (81.6078%)
**Top Internal Functions/Classes:**
  * `updateFilterCounts` (Impact: 37.2)
  * `buildFilter` (Impact: 35.6)
    * *Intent:* /** * Build a filter function taking an igvFeature as an argument and returning true for "pass" (sho...
  * `initFacets` (Impact: 35.3)
    * *Intent:* * // For categorical: number of features satisfying each filter * "countsByFilterName": { * <String>...
  * `handleBrushMove` (Impact: 19.9)
  * `getHistogramBars` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 148`, `args: 70`, `func_start: 57`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 143`, `dead_code: 6`, `planned_debt: 7`, `duplicate_logic: 11`, `orphaned_logic: 1`
* *Architecture:* `io: 20`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 33`, `doc: 35`, `immutability_locks: 267`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` d3.js, favicon.ico, d3-scale.js, popper.min.js, d3-interpolate.js, d3-brush.js, d3-array.js, tippy-bundle.umd.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/textFeatureSource.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.256 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.787 IQR)
- **Top Global Matches:** file_cluster_4: 15.256, file_cluster_13: 15.687, file_cluster_11: 15.919
- **Magnitude:** 587.84 | **LOC:** 281 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (70.4715%), Tech Debt (55.5464%)
**Top Internal Functions/Classes:**
  * `loadFeatures` (Impact: 56.8)
  * `constructor` (Impact: 47.6)
    * *Intent:* /** * feature source for "bed like" files (tab or whitespace delimited files with 1 feature per line...
  * `addFeaturesToDB` (Impact: 22.2)
  * `getHeader` (Impact: 14.8)
  * `trackType` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 44`, `args: 11`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 321`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `concurrency: 85`, `import: 11`
* *Defense:* `safety: 27`, `doc: 7`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gtexReader.js, featureCache.js, featureFileReader.js, genomicInterval.js, baseFeatureSource.js, customServiceReader.js, chromAliasManager.js, ucscServiceReader.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/qtl/qtlTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.544 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.31 IQR)
- **Top Global Matches:** file_cluster_4: 13.544, file_cluster_13: 13.965, file_cluster_8: 13.975
- **Magnitude:** 562.08 | **LOC:** 343 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.7213%), Tech Debt (15.2827%)
**Top Internal Functions/Classes:**
  * `drawEqtls` (Impact: 41.0)
  * `draw` (Impact: 37.6)
  * `dialogPresentationHandler` (Impact: 36.6)
  * `callback` (Impact: 34.5)
  * `menuItemList` (Impact: 32.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 50`, `args: 22`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 235`, `planned_debt: 3`
* *Architecture:* `api: 9`, `concurrency: 49`, `import: 5`
* *Defense:* `safety: 14`, `doc: 1`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, igv-canvas.js, featureSource.js, search.js, trackBase.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/utils/w3XMLHttpRequest.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.545 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_0: 13.545, file_cluster_11: 13.582, file_cluster_8: 13.619
- **Magnitude:** 538.76 | **LOC:** 1295 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.3112%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_classPrivateFieldLooseBase` (Impact: 47.1)
  * `_classPrivateFieldLooseBase` (Impact: 25.0)
    * *Intent:* /** * @deprecated since version 3.0 */ /** * @deprecated since version 3.0 */ /** * @deprecated sinc...
  * `dispatchEvent` (Impact: 17.1)
  * `_classPrivateFieldLooseBase` (Impact: 12.7)
  * `onabort` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 107`, `args: 64`, `func_start: 118`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 246`, `planned_debt: 12`, `duplicate_logic: 37`
* *Architecture:* `io: 44`, `api: 8`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 47`, `doc: 123`, `test: 1`, `immutability_locks: 16`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http, perf_hooks, https
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/sequenceTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.249 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.436 IQR)
- **Top Global Matches:** file_cluster_4: 13.249, file_cluster_13: 13.752, file_cluster_8: 13.896
- **Magnitude:** 536.08 | **LOC:** 390 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (84.5026%), Tech Debt (99.9313%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 38.8)
  * `contextMenuItemList` (Impact: 24.5)
  * `constructor` (Impact: 13.5)
  * `menuItemList` (Impact: 11.4)
  * `click` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 58`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 262`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 9`, `concurrency: 80`, `import: 7`
* *Defense:* `safety: 10`, `doc: 5`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blatTrack.js, loadSequence.js, igv-canvas.js, igvUtils.js, nucleotideColors.js, sequenceUtils.js, translationDict.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/data/misc/BufferedReaderTest.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/aed/AEDParser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.639 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.888 IQR)
- **Top Global Matches:** file_cluster_4: 13.639, file_cluster_8: 13.647, file_cluster_11: 13.877
- **Magnitude:** 497.2 | **LOC:** 472 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.2002%), Tech Debt (10.0879%)
**Top Internal Functions/Classes:**
  * `AedFeature` (Impact: 46.4)
  * `decodeAed` (Impact: 33.8)
  * `parseHeader` (Impact: 32.7)
  * `parseTrackLine` (Impact: 27.6)
    * *Intent:* // Example entry:
  * `parseFeatures` (Impact: 24.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 57`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 239`, `planned_debt: 1`
* *Architecture:* `api: 7`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 29`, `doc: 8`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `js/ui/components/table.js` (JAVASCRIPT) | Magnitude: 30.58 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 15, structural_boundaries: 8, immutability_locks: 7
- `test/utils/w3XMLHttpRequest.js` (JAVASCRIPT) | Magnitude: 538.76 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 578, state_mutation: 246, doc: 123, func_start: 118
- `examples/events/locus-change.html` (HTML) | Magnitude: 27.14 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 22, decorators: 8, globals: 7
- `dev/events/custom-track-click.html` (HTML) | Magnitude: 41.6 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 23, state_mutation: 12, args: 8
- `examples/events/custom-track-popover.html` (HTML) | Magnitude: 37.86 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 21, state_mutation: 10, decorators: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `js/ui/cursorGuide.js` (JAVASCRIPT) | Magnitude: 120.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 57, branch: 17, structural_boundaries: 10
- `js/bam/pairedEndStats.js` (JAVASCRIPT) | Magnitude: 151.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 116, indent_spaces: 49, branch: 21, structural_boundaries: 10
- `js/feature/gff/gffFeature.js` (JAVASCRIPT) | Magnitude: 357.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 243, indent_spaces: 171, branch: 59, structural_boundaries: 32
- `js/feature/intervalTree.js` (JAVASCRIPT) | Magnitude: 250.9 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 170, state_mutation: 115, branch: 48, structural_boundaries: 34
- `js/ui/circularViewControl.js` (JAVASCRIPT) | Magnitude: 47.08 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 28, indent_spaces: 22, args: 6, closures: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `findLarge.sh` (SHELL) | Magnitude: 23.76 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 17, io: 12, structural_boundaries: 10, reflection_metaprogramming: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `dev/events/custom-track-popover.html` (HTML) | Magnitude: 39.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 21, state_mutation: 12, args: 8
- `js/trackView.js` (JAVASCRIPT) | Magnitude: 1280.38 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 826, indent_spaces: 659, branch: 160, safety: 75
- `js/feature/featureParser.js` (JAVASCRIPT) | Magnitude: 744.26 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 396, indent_spaces: 323, branch: 176, structural_boundaries: 44
- `dev/cnvpytor/old/indexed_explicit_update.html` (HTML) | Magnitude: 42.72 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 24, immutability_locks: 17, args: 14
- `js/shoebox/shoeboxColorScale.js` (JAVASCRIPT) | Magnitude: 132.8 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 102, indent_spaces: 55, branch: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `js/igv.d.ts` (TYPESCRIPT) | Magnitude: 42.23 | Delta: **0.219 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 501, structural_boundaries: 239, branch: 231, generics: 115

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `dev/misc/interactive-filtering.html` (HTML) | Magnitude: 600.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1231, immutability_locks: 267, branch: 167, structural_boundaries: 148
- `js/events.js` (JAVASCRIPT) | Magnitude: 73.26 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 35, branch: 13, structural_boundaries: 6
- `js/sample/sampleInfoViewport.js` (JAVASCRIPT) | Magnitude: 495.28 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 290, indent_spaces: 278, branch: 66, immutability_locks: 62
- `js/feature/render/renderSnp.js` (JAVASCRIPT) | Magnitude: 114.36 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 30, branch: 19, structural_boundaries: 17
- `js/feature/gff/gffHelper.js` (JAVASCRIPT) | Magnitude: 240.24 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 167, state_mutation: 128, branch: 55, structural_boundaries: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `js/trackBase.js` (JAVASCRIPT) | Magnitude: 833.98 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 477, state_mutation: 429, branch: 182, structural_boundaries: 68
- `dev/events/locus-change.html` (HTML) | Magnitude: 41.34 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 23, state_mutation: 15, args: 9
- `dev/interact/bedpe-10xSVs.html` (HTML) | Magnitude: 28.92 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 9, args: 6, concurrency: 6
- `js/aed/AEDParser.js` (JAVASCRIPT) | Magnitude: 497.2 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 296, state_mutation: 239, branch: 116, structural_boundaries: 57
- `dev/misc/custom-track.html` (HTML) | Magnitude: 31.36 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 14, state_mutation: 13, immutability_locks: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/events/roi-events.html` (HTML) | Magnitude: 12.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 10, args: 9, listeners: 8
- `examples/roi-api.html` (HTML) | Magnitude: 33.52 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 18, concurrency: 9, globals: 7
- `js/feature/render/renderFeature.js` (JAVASCRIPT) | Magnitude: 601.48 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 336, state_mutation: 166, branch: 107, structural_boundaries: 54
- `examples/igvjs.html` (HTML) | Magnitude: 20.6 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 7, args: 5, api: 4
- `scripts/updateVersion.cjs` (JAVASCRIPT) | Magnitude: 27.44 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 12, io: 8, immutability_locks: 8, indent_spaces: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `js/genome/bpt.js` (JAVASCRIPT) | Magnitude: 10.52 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 18

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `js/trackViewport.js` -> Churn: **70.99%** | Cog Load: 68.6635% | Debt: 32.7318%
- `js/bam/alignmentTrack.js` -> Churn: **60.62%** | Cog Load: 84.92% | Debt: 89.6766%
- `js/feature/render/renderFeature.js` -> Churn: **60.62%** | Cog Load: 43.0306% | Debt: 86.7442%
- `js/igv-create.js` -> Churn: **55.63%** | Cog Load: 75.0279% | Debt: 80.2296%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `js/bigwig/bwReader.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 1454.28
- `js/bam/alignmentTrack.js` -> **jrobinso** (83.3% isolated ownership) | Magnitude: 1186.44
- `js/trackViewport.js` -> **jrobinso** (88.9% isolated ownership) | Magnitude: 1182.5
- `js/variant/variantTrack.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 1160.24
- `js/bam/alignmentContainer.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 1027.54

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `js/bam/bamFilter.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)
- `js/bam/mods/baseModificationSet.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)
- `js/bigwig/bwSource.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)
- `js/binary.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)
- `js/hic/hicColorScale.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
