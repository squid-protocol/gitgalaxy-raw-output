# ARCHITECTURAL_BRIEF: igv.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/igv.js` |
| **Timestamp** | `2026-08-03T20:05:29.913450+00:00` |
| **Scan Duration** | `1.93s` |
| **Git Branch** | `master` |
| **Git Commit** | `020ed83d7371c3b9a361766b68c280592bc1e574` |
| **Git Remote** | `https://github.com/igvteam/igv.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 291 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Volatility Index | 0.005 |
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
> **Architectural Drift Z-Score:** `5.129`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 325 | 58.1% |
| file_cluster_4 | 113 | 20.2% |
| file_cluster_13 | 58 | 10.4% |
| file_cluster_17 | 17 | 3.0% |
| file_cluster_0 | 15 | 2.7% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 37.7 | 33.4 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 28.8 | 13.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 27.2 | 2.3 | 80.0 |
| API Exposure | 0.0 | 13.4 | 4.7 | 4.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 49.0 | 45.1 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 96.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.4 | 2.1 | 0.2 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.3 | 5.1 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 71.6 | 99.5 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 47.7 | 17.6 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 42.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `loadSessionObject` (@ `js/browser.js`) -> Impact: **1236.4** | LOC: 1206
- `search` (@ `js/bigwig/bwReader.js`) -> Impact: **1083.5** | LOC: 470
- `draw` (@ `js/bam/alignmentTrack.js`) -> Impact: **733.7** | LOC: 518
- `call_2d` (@ `js/cnvpytor/CombinedCaller.js`) -> Impact: **630.6** | LOC: 336
  * *Intent:* /** * Creates an instance of CombinedCaller. * * @param {Array} wigFeatures - An array of arrays containing wig formatted data for each chromosome and...
- `url` (@ `js/igv.d.ts`) -> Impact: **613.9** | LOC: 327
- `handleMessage` (@ `js/websocket/messageHandler.js`) -> Impact: **396.3** | LOC: 167
  * *Intent:* /** * Handles incoming messages from the WebSocket connection. Performs requested actions on the IGV browser instance * and returns a response message...
- `decodeBed` (@ `js/feature/decode/ucsc.js`) -> Impact: **376.8** | LOC: 115
  * *Intent:* /**
- `renderFeature` (@ `js/feature/render/renderFeature.js`) -> Impact: **368.3** | LOC: 144
- `renderAminoAcidSequence` (@ `js/feature/render/renderFeature.js`) -> Impact: **365.8** | LOC: 152
- `setDecoder` (@ `js/feature/featureParser.js`) -> Impact: **333.0** | LOC: 126
  * *Intent:* // Special hack for bedPE

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `click` (@ `dev/ui/example.html`) -> **O(2^N) [Recursive]**
- `init` (@ `js/feature/featureTrack.js`) -> **O(2^N) [Recursive]**
- `findOverlapping` (@ `js/feature/featureUtils.js`) -> **O(2^N) [Recursive]**
- `popupData` (@ `js/feature/mergedTrack.js`) -> **O(2^N) [Recursive]**
- `popupData` (@ `js/feature/wigTrack.js`) -> **O(2^N) [Recursive]**
- `search` (@ `js/genome/chromAliasBB.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Return the cached canonical chromosome name for the alias. If none found return the alias. * * Note this will only work if a "search" for ths ch...
- `popupData` (@ `js/gwas/gwasTrack.js`) -> **O(2^N) [Recursive]**
- `init` (@ `js/gwas/gwasTrack.js`) -> **O(2^N) [Recursive]**
- `loadStanzas` (@ `js/ucsc/hub/hubParser.js`) -> **O(2^N) [Recursive]**
- `alert` (@ `dev/sessions/sessionTestHarness.html`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `loadSessionObject` (@ `js/browser.js`) -> DB Complexity: **401**
- `search` (@ `js/bigwig/bwReader.js`) -> DB Complexity: **185**
- `call_2d` (@ `js/cnvpytor/CombinedCaller.js`) -> DB Complexity: **130**
  * *Intent:* /** * Creates an instance of CombinedCaller. * * @param {Array} wigFeatures - An array of arrays containing wig formatted data for each chromosome and...
- `draw` (@ `js/bam/alignmentTrack.js`) -> DB Complexity: **116**
- `setDecoder` (@ `js/feature/featureParser.js`) -> DB Complexity: **79**
  * *Intent:* // Special hack for bedPE
- `popupData` (@ `js/bam/bamAlignment.js`) -> DB Complexity: **74**
- `partition` (@ `js/cnvpytor/MeanShiftUtil.js`) -> DB Complexity: **65**
  * *Intent:* // The values are reversed and squared as they will be used to calculate a gradient function. // This optimization is done to speed up the calculation...
- `call_mean_shift` (@ `js/cnvpytor/MeanShiftUtil.js`) -> DB Complexity: **64**
- `meanShiftCaller` (@ `js/cnvpytor/MeanShiftUtil.js`) -> DB Complexity: **61**
- `menuItemList` (@ `js/feature/interactionTrack.js`) -> DB Complexity: **61**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `js` | 29 | 13489.21 | 56.52% | 19.86% |
| `js/feature` | 26 | 13444.92 | 63.11% | 26.94% |
| `js/bam` | 25 | 9243.56 | 59.79% | 14.89% |
| `js/cnvpytor` | 7 | 5001.2 | 43.67% | 25.91% |
| `js/genome` | 21 | 4522.22 | 58.27% | 10.52% |
| `js/bigwig` | 9 | 4239.78 | 60.65% | 10.56% |
| `js/ui` | 20 | 2557.7 | 66.97% | 14.79% |
| `js/variant` | 3 | 2330.5 | 75.41% | 12.05% |
| `js/sample` | 8 | 1849.62 | 61.1% | 23.06% |
| `js/ucsc/hub` | 5 | 1811.46 | 79.5% | 18.75% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `js/bam/packedAlignments.js` -> **100.0%** Exposure
- `js/roi/ROISet.js` -> **100.0%** Exposure
- `js/sample/plinkSampleInformation.js` -> **100.0%** Exposure
- `js/ui/components/textbox.js` -> **100.0%** Exposure
- `js/util/colorScale.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `dev/cnvpytor/old/computeDepthFeatures.js` -> **100.0%** Exposure
- `js/aed/AEDParser.js` -> **100.0%** Exposure
- `js/bam/alignmentContainer.js` -> **100.0%** Exposure
- `js/bam/alignmentTrack.js` -> **100.0%** Exposure
- `js/bam/bamAlignment.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/util/colorScale.js` -> **0** Orphaned Functions | **28** Duplicates
- `test/utils/w3XMLHttpRequest.js` -> **0** Orphaned Functions | **21** Duplicates
- `js/bam/alignmentContainer.js` -> **0** Orphaned Functions | **12** Duplicates
- `js/feature/mergedTrack.js` -> **0** Orphaned Functions | **12** Duplicates
- `js/roi/ROISet.js` -> **0** Orphaned Functions | **10** Duplicates

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

### Exploit Generation Surface
- `dev/alignment/bamCSI.html` -> **100.0%** Exposure
- `dev/alignment/basemods/baseMods.html` -> **100.0%** Exposure
- `dev/cbio/cBio.html` -> **100.0%** Exposure
- `dev/cnvpytor/old/indexed_explicit_update.html` -> **100.0%** Exposure
- `dev/cnvpytor/old/not_indexed.html` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `js/browser.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `dev/cbio/cBio.html` -> **100.0%** Exposure
- `dev/cbio/cBioMut.html` -> **100.0%** Exposure
- `dev/cnvpytor/old/indexed_explicit_update.html` -> **100.0%** Exposure
- `dev/events/track-reorder.html` -> **100.0%** Exposure
- `dev/misc/custom-track.html` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `76` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `190` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/roi/ROISet.js` (JAVASCRIPT) -> Cumulative Risk: **1003.43**
- **Archetype:** `file_cluster_4` (Distance: 13.454 IQR)
- **Magnitude:** 383.64 | **LOC:** 207 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 90.7), `constructor` (Impact: 22.7), `toJSON` (Impact: 22.5)

### 2. `js/feature/segParser.js` (JAVASCRIPT) -> Cumulative Risk: **990.28**
- **Archetype:** `file_cluster_4` (Distance: 14.441 IQR)
- **Magnitude:** 517.24 | **LOC:** 188 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `popupData` (Impact: 48.3), `extractCravatLink` (Impact: 47.6), `parseFeatures` (Impact: 43.4)

### 3. `js/sample/sampleNameViewport.js` (JAVASCRIPT) -> Cumulative Risk: **977.62**
- **Archetype:** `file_cluster_4` (Distance: 13.813 IQR)
- **Magnitude:** 282.4 | **LOC:** 233 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `addMouseHandlers` (Impact: 47.2), `repaint` (Impact: 21.6), `constructor` (Impact: 10.2)

### 4. `js/variant/variantTrack.js` (JAVASCRIPT) -> Cumulative Risk: **975.41**
- **Archetype:** `file_cluster_4` (Distance: 18.696 IQR)
- **Magnitude:** 1615.04 | **LOC:** 1031 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `postInit` (Impact: 110.8), `getFeatures` (Impact: 101.9), `clickedFeatures` (Impact: 95.1)

### 5. `js/sequenceTrack.js` (JAVASCRIPT) -> Cumulative Risk: **970.81**
- **Archetype:** `file_cluster_4` (Distance: 13.298 IQR)
- **Magnitude:** 745.28 | **LOC:** 390 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `draw` (Impact: 123.6), `contextMenuItemList` (Impact: 77.5), `menuItemList` (Impact: 36.1)

### 6. `js/cram/fileHandler.js` (JAVASCRIPT) -> Cumulative Risk: **964.95**
- **Archetype:** `file_cluster_4` (Distance: 12.858 IQR)
- **Magnitude:** 205.56 | **LOC:** 99 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 22.4), `get` (Impact: 18.6), `read` (Impact: 10.9)

### 7. `js/browser.js` (JAVASCRIPT) -> Cumulative Risk: **957.59**
- **Archetype:** `file_cluster_4` (Distance: 15.246 IQR)
- **Magnitude:** 2913.0 | **LOC:** 2683 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Churn (100.0%)
- **Heaviest Functions:** `loadSessionObject` (Impact: 1236.4), `loadSessionFile` (Impact: 79.6), `constructor` (Impact: 46.2)

### 8. `js/gwas/gwasParser.js` (JAVASCRIPT) -> Cumulative Risk: **956.67**
- **Archetype:** `file_cluster_4` (Distance: 12.95 IQR)
- **Magnitude:** 254.56 | **LOC:** 159 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `parseHeaderLine` (Impact: 95.5), `constructor` (Impact: 22.2), `parseFeatures` (Impact: 14.9)

### 9. `js/bam/bamTrack.js` (JAVASCRIPT) -> Cumulative Risk: **954.36**
- **Archetype:** `file_cluster_13` (Distance: 14.245 IQR)
- **Magnitude:** 816.88 | **LOC:** 384 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getFeatures` (Impact: 62.5), `addPairedChordsForViewport` (Impact: 55.6), `init` (Impact: 36.8)

### 10. `js/feature/mergedTrack.js` (JAVASCRIPT) -> Cumulative Risk: **952.82**
- **Archetype:** `file_cluster_4` (Distance: 14.571 IQR)
- **Magnitude:** 888.08 | **LOC:** 506 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `postInit` (Impact: 179.0), `popupData` (Impact: 110.6), `dataRange` (Impact: 63.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/browser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.246 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.963 IQR)
- **Top Global Matches:** file_cluster_4: 15.246, file_cluster_13: 15.41, file_cluster_17: 15.617
- **Magnitude:** 2913.0 | **LOC:** 2683 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 401
- **Risk Profile:** Cognitive Load (49.8915%), Tech Debt (11.2713%)
**Top Internal Functions/Classes:**
  * `loadSessionObject` (Impact: 1236.4 | O(N^6) | DB: 401)
  * `loadSessionFile` (Impact: 79.6 | O(N^5) | DB: 4)
    * *Intent:* // TODO: deprecated
  * `constructor` (Impact: 46.2 | O(N^5) | DB: 40)
  * `initialize` (Impact: 40.8 | O(N^4) | DB: 16)
  * `isMultiLocusWholeGenomeView` (Impact: 18.4 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 200`, `args: 107`, `func_start: 89`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 1146`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `api: 9`, `concurrency: 223`, `import: 51`
* *Defense:* `safety: 57`, `doc: 72`, `immutability_locks: 158`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` trackView.js, circularViewUtils.js, canvas2svg.js, trackROISet.js, fileFormatUtils.js, ideogramTrack.js, ucscUtils.js, trackUtils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/interactionTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.109 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.19 IQR)
- **Top Global Matches:** file_cluster_4: 15.109, file_cluster_11: 15.166, file_cluster_13: 15.219
- **Magnitude:** 2432.48 | **LOC:** 1034 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (76.3195%), Tech Debt (11.8942%)
**Top Internal Functions/Classes:**
  * `drawProportional` (Impact: 249.3 | O(N^6) | DB: 33)
  * `drawNested` (Impact: 185.7 | O(N^6) | DB: 53)
  * `init` (Impact: 172.9 | O(2^N) | DB: 29)
  * `getWGFeatures` (Impact: 167.8 | O(N^6) | DB: 22)
  * `menuItemList` (Impact: 120.5 | O(N^6) | DB: 61)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 118`, `args: 47`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 864`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 8`, `concurrency: 30`, `import: 11`
* *Defense:* `safety: 70`, `doc: 11`, `immutability_locks: 109`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dom-utils.js, igv-canvas.js, index.js, trackBase.js, featureSource.js, circularViewUtils.js, getChrColor.js, colorPalletes.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/cnvpytor/MeanShiftUtil.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.074 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.605 IQR)
- **Top Global Matches:** file_cluster_17: 16.074, file_cluster_11: 16.284, file_cluster_4: 16.308
- **Magnitude:** 2412.14 | **LOC:** 1089 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (76.0868%), Tech Debt (30.9059%)
**Top Internal Functions/Classes:**
  * `call_mean_shift` (Impact: 331.7 | O(N^6) | DB: 64)
  * `partition` (Impact: 296.2 | O(N^6) | DB: 65)
    * *Intent:* // The values are reversed and squared as they will be used to calculate a gradient function. // Thi...
  * `meanShiftCaller` (Impact: 280.3 | O(N^6) | DB: 61)
  * `cnv_calling` (Impact: 261.2 | O(N^6) | DB: 50)
  * `cnvCalling` (Impact: 187.2 | O(N^6) | DB: 52)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 270`, `args: 47`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 877`, `dead_code: 25`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 2`
* *Defense:* `doc: 4`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GeneralUtil.js, baseCNVpytorVCF.js, t_dist.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/bigwig/bwReader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.17 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.818 IQR)
- **Top Global Matches:** file_cluster_4: 14.17, file_cluster_13: 14.83, file_cluster_11: 14.932
- **Magnitude:** 2293.28 | **LOC:** 744 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 185
- **Risk Profile:** Cognitive Load (63.3729%), Tech Debt (9.0074%)
**Top Internal Functions/Classes:**
  * `search` (Impact: 1083.5 | O(2^N) | DB: 185)
  * `readFeatures` (Impact: 146.7 | O(N^5) | DB: 21)
  * `getIdForChr` (Impact: 86.4 | O(N^6) | DB: 11)
  * `readWGFeatures` (Impact: 36.3 | O(N^4) | DB: 7)
  * `constructor` (Impact: 18.1 | O(N^3) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 120`, `args: 29`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 577`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 12`, `api: 4`, `concurrency: 310`, `import: 9`
* *Defense:* `safety: 31`, `doc: 23`, `immutability_locks: 85`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` binary.js, trix.js, index.js, igvUtils.js, rpTree.js, bbDecoders.js, chromTree.js, bpTree.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/trackView.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.257 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.425 IQR)
- **Top Global Matches:** file_cluster_13: 15.257, file_cluster_17: 15.265, file_cluster_4: 15.308
- **Magnitude:** 1847.18 | **LOC:** 1030 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (64.6585%), Tech Debt (34.9272%)
**Top Internal Functions/Classes:**
  * `updateViews` (Impact: 223.7 | O(N^6) | DB: 39)
  * `addTrackDragMouseHandlers` (Impact: 93.6 | O(N^6) | DB: 25)
  * `presentColorPicker` (Impact: 87.5 | O(N^6) | DB: 18)
  * `getInViewFeatures` (Impact: 68.3 | O(N^6) | DB: 6)
  * `paintAxis` (Impact: 52.4 | O(2^N) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 74`, `args: 66`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `state_mutation: 826`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `concurrency: 19`, `import: 11`
* *Defense:* `safety: 75`, `doc: 17`, `immutability_locks: 73`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sampleNameViewport.js, index.js, sampleInfoViewport.js, icons.js, menuUtils.js, menuPopup.js, colorPalletes.js, igvUtils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/trackViewport.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.907 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.462 IQR)
- **Top Global Matches:** file_cluster_4: 14.907, file_cluster_13: 15.063, file_cluster_8: 15.104
- **Magnitude:** 1632.7 | **LOC:** 1100 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (69.3689%), Tech Debt (10.3306%)
**Top Internal Functions/Classes:**
  * `loadFeatures` (Impact: 93.7 | O(N^6) | DB: 26)
  * `checkZoomIn` (Impact: 83.1 | O(N^5) | DB: 26)
  * `addViewportClickHandler` (Impact: 74.4 | O(N^5) | DB: 21)
  * `addMouseHandlers` (Impact: 62.2 | O(N^6) | DB: 27)
  * `getFeatures` (Impact: 59.3 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 82`, `args: 47`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 781`, `fragile_debt: 1`
* *Architecture:* `api: 13`, `concurrency: 36`, `import: 9`
* *Defense:* `safety: 40`, `doc: 13`, `immutability_locks: 107`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` popover.js, canvas2svg.js, index.js, draggable.js, genomeUtils.js, viewport.js, icons.js, dom-utils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/variant/variantTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 18.696 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.614 IQR)
- **Top Global Matches:** file_cluster_4: 18.696, file_cluster_17: 18.822, file_cluster_11: 18.894
- **Magnitude:** 1615.04 | **LOC:** 1031 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (85.3352%), Tech Debt (20.067%)
**Top Internal Functions/Classes:**
  * `postInit` (Impact: 110.8 | O(N^4) | DB: 41)
  * `getFeatures` (Impact: 101.9 | O(2^N) | DB: 18)
  * `clickedFeatures` (Impact: 95.1 | O(2^N) | DB: 20)
  * `menuItemList` (Impact: 80.4 | O(N^6) | DB: 58)
    * *Intent:* // } else if (aNan) { // return 1; // } else if (bNan) { // return -1; // } else { // var a0 = getAl...
  * `init` (Impact: 58.7 | O(2^N) | DB: 16)
    * *Intent:* // Note -- init gets called during base class construction. Confusing
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 74`, `args: 32`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 837`, `dead_code: 23`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `concurrency: 48`, `import: 12`
* *Defense:* `safety: 64`, `doc: 5`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` featureSource.js, dom-utils.js, igv-canvas.js, index.js, trackBase.js, sampleInfo.js, circularViewUtils.js, colorPalletes.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/bam/alignmentContainer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.799 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.177 IQR)
- **Top Global Matches:** file_cluster_8: 13.799, file_cluster_17: 13.908, file_cluster_13: 13.916
- **Magnitude:** 1537.44 | **LOC:** 763 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (67.6289%), Tech Debt (93.9377%)
**Top Internal Functions/Classes:**
  * `packAlignmentRows` (Impact: 193.3 | O(N^6) | DB: 20)
  * `incCounts` (Impact: 112.2 | O(N^6) | DB: 12)
  * `getPosCount` (Impact: 66.3 | O(N^4) | DB: 3)
  * `getNegCount` (Impact: 66.3 | O(N^4) | DB: 3)
  * `addAlignment` (Impact: 62.2 | O(N^5) | DB: 29)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 115`, `args: 54`, `func_start: 48`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 552`, `duplicate_logic: 12`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 20`, `doc: 9`, `immutability_locks: 55`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pairedAlignment.js, bamAlignmentRow.js, igvUtils.js, baseModificationCounts.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/trackBase.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.67 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.279 IQR)
- **Top Global Matches:** file_cluster_4: 14.67, file_cluster_13: 14.736, file_cluster_11: 14.781
- **Magnitude:** 1450.98 | **LOC:** 721 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (49.0343%), Tech Debt (20.1772%)
**Top Internal Functions/Classes:**
  * `setTrackProperties` (Impact: 312.3 | O(N^6) | DB: 15)
  * `extractPopupData` (Impact: 137.3 | O(N^6) | DB: 21)
  * `init` (Impact: 94.9 | O(N^4) | DB: 27)
  * `getState` (Impact: 73.2 | O(N^4) | DB: 15)
  * `description` (Impact: 72.2 | O(N^6) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 68`, `args: 35`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 433`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 15`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 47`, `doc: 37`, `immutability_locks: 42`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` featureUtils.js, index.js, igvUtils.js, igv-icons.js, sessionResourceValidator.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/segTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.982 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.472 IQR)
- **Top Global Matches:** file_cluster_4: 14.982, file_cluster_13: 15.22, file_cluster_17: 15.241
- **Magnitude:** 1447.0 | **LOC:** 760 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 69.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (78.5583%), Tech Debt (11.0727%)
**Top Internal Functions/Classes:**
  * `getFeatures` (Impact: 111.0 | O(2^N) | DB: 18)
  * `init` (Impact: 94.1 | O(2^N) | DB: 24)
  * `filter` (Impact: 69.2 | O(N^5) | DB: 5)
    * *Intent:* /**
  * `computeRegionScores` (Impact: 67.0 | O(N^4) | DB: 6)
  * `menuItemList` (Impact: 53.4 | O(N^6) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 78`, `args: 33`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 678`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 9`, `concurrency: 48`, `import: 11`
* *Defense:* `safety: 44`, `doc: 9`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hicColorScale.js, igv-canvas.js, index.js, trackBase.js, featureSource.js, colorScale.js, sampleInfo.js, colorPalletes.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/bam/alignmentTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.942 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.066 IQR)
- **Top Global Matches:** file_cluster_13: 13.942, file_cluster_8: 14.031, file_cluster_17: 14.184
- **Magnitude:** 1398.84 | **LOC:** 1587 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 116
- **Risk Profile:** Cognitive Load (84.6901%), Tech Debt (10.5801%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 733.7 | O(N^6) | DB: 116)
  * `constructor` (Impact: 111.8 | O(N^4) | DB: 35)
  * `setHighlightedReads` (Impact: 28.2 | O(2^N) | DB: 2)
  * `computePixelHeight` (Impact: 22.0 | O(N^4) | DB: 5)
  * `setTop` (Impact: 7.9 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 78`, `args: 34`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 458`, `fragile_debt: 1`
* *Architecture:* `api: 7`, `import: 14`
* *Defense:* `safety: 26`, `doc: 8`, `immutability_locks: 66`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dom-utils.js, igv-canvas.js, igv-icons.js, index.js, pairedAlignment.js, blatTrack.js, orientationTypes.js, igvUtils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/bam/bamAlignment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.64 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.195 IQR)
- **Top Global Matches:** file_cluster_4: 14.64, file_cluster_13: 14.685, file_cluster_11: 14.829
- **Magnitude:** 1372.76 | **LOC:** 520 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 74
- **Risk Profile:** Cognitive Load (67.7069%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `popupData` (Impact: 324.7 | O(N^6) | DB: 74)
  * `getGroupValue` (Impact: 282.3 | O(N^6) | DB: 24)
  * `getBaseModificationSets` (Impact: 94.3 | O(2^N) | DB: 12)
  * `readBaseQualityAt` (Impact: 39.1 | O(N^5) | DB: 5)
  * `softClippedBlocks` (Impact: 30.5 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 84`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 408`, `dead_code: 2`
* *Architecture:* `api: 15`, `concurrency: 13`, `import: 6`
* *Defense:* `safety: 31`, `doc: 14`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hgvs.js, index.js, clinVar.js, orientationTypes.js, baseModificationUtils.js, supplementaryAlignment.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/featureParser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.211 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.329 IQR)
- **Top Global Matches:** file_cluster_13: 14.211, file_cluster_4: 14.219, file_cluster_8: 14.355
- **Magnitude:** 1322.66 | **LOC:** 413 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 79
- **Risk Profile:** Cognitive Load (83.7142%), Tech Debt (12.7273%)
**Top Internal Functions/Classes:**
  * `setDecoder` (Impact: 333.0 | O(N^5) | DB: 79)
    * *Intent:* // Special hack for bedPE
  * `parseHeader` (Impact: 221.7 | O(N^6) | DB: 14)
  * `parseFeatures` (Impact: 158.7 | O(N^5) | DB: 16)
  * `parseTrackLine` (Impact: 127.1 | O(N^5) | DB: 8)
  * `parseColumnsDirective` (Impact: 22.6 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 44`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 396`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 24`, `import: 13`
* *Defense:* `safety: 23`, `doc: 5`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` longrange.js, gffHelper.js, ucsc.js, gtexGWAS.js, custom.js, fileFormats.js, bedpe.js, fusionJuncSpan.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/misc/interactive-filtering.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.445 IQR)
- **Top Global Matches:** file_cluster_8: 11.445, file_cluster_17: 11.449, file_cluster_0: 11.647
- **Magnitude:** 1254.2 | **LOC:** 1500 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (15.8748%), Tech Debt (28.7%)
**Top Internal Functions/Classes:**
  * `updateFilterCounts` (Impact: 119.4 | O(N^6) | DB: 7)
  * `buildFilter` (Impact: 117.9 | O(N^6) | DB: 3)
    * *Intent:* /** * Build a filter function taking an igvFeature as an argument and returning true for "pass" (sho...
  * `initFacets` (Impact: 113.2 | O(N^6) | DB: 7)
    * *Intent:* * // For categorical: number of features satisfying each filter * "countsByFilterName": { * <String>...
  * `getHistogramBars` (Impact: 48.9 | O(N^5) | DB: 6)
  * `handleBrushMove` (Impact: 46.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 148`, `args: 70`, `func_start: 57`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 143`, `dead_code: 6`, `planned_debt: 7`, `duplicate_logic: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 20`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 33`, `doc: 35`, `immutability_locks: 267`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` d3.js, d3-brush.js, crossfilter2@1.5.4, d3-interpolate.js, tippy-bundle.umd.js, d3-array.js, d3-selection.js, popper.min.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/render/renderFeature.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.586 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.439 IQR)
- **Top Global Matches:** file_cluster_8: 13.586, file_cluster_13: 13.604, file_cluster_11: 13.709
- **Magnitude:** 1179.88 | **LOC:** 510 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (43.0306%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderFeature` (Impact: 368.3 | O(N^6) | DB: 25)
  * `renderAminoAcidSequence` (Impact: 365.8 | O(N^5) | DB: 10)
  * `getAminoAcidLetterWithExonGap` (Impact: 131.3 | O(N^4) | DB: 7)
  * `renderFeatureLabel` (Impact: 129.9 | O(N^4) | DB: 13)
  * `calculateFeatureCoordinates` (Impact: 6.9 | O(N^2) | DB: 3)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 54`, `args: 8`, `func_start: 13`
* *Risk/State:* `state_mutation: 166`, `dead_code: 2`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 33`, `doc: 20`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exonUtils.js, igv-canvas.js, sequenceUtils.js, translationDict.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/wigTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.335 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.305 IQR)
- **Top Global Matches:** file_cluster_4: 14.335, file_cluster_13: 14.54, file_cluster_11: 14.659
- **Magnitude:** 1177.46 | **LOC:** 575 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (83.8904%), Tech Debt (9.9777%)
**Top Internal Functions/Classes:**
  * `getFeatures` (Impact: 243.7 | O(2^N) | DB: 14)
  * `popupData` (Impact: 135.8 | O(2^N) | DB: 9)
  * `init` (Impact: 115.2 | O(2^N) | DB: 16)
  * `drawSVGPath` (Impact: 85.2 | O(N^6) | DB: 1)
  * `drawLetterGlyph` (Impact: 32.2 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 53`, `args: 30`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 335`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 42`, `import: 11`
* *Defense:* `safety: 29`, `doc: 4`, `immutability_locks: 39`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` igv-canvas.js, index.js, tdfSource.js, trackBase.js, featureSource.js, colorScale.js, bwSource.js, wigSummary.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/genome/genome.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.277 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_4: 14.277, file_cluster_13: 14.648, file_cluster_8: 14.873
- **Magnitude:** 1096.44 | **LOC:** 467 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (49.8555%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 143.6 | O(N^5) | DB: 33)
  * `getManeTranscriptAt` (Impact: 61.7 | O(N^6) | DB: 5)
  * `getAliasRecord` (Impact: 48.2 | O(N^5) | DB: 5)
  * `getManeTranscript` (Impact: 40.1 | O(N^4) | DB: 11)
  * `trimSmallChromosomes` (Impact: 27.0 | O(N^4) | DB: 5)
    * *Intent:* /** * Return the Mane transcript overlapping the given position, or null if none found. *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 86`, `args: 36`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 383`
* *Architecture:* `api: 15`, `concurrency: 116`, `import: 11`
* *Defense:* `safety: 17`, `doc: 21`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cytobandFileBB.js, cytobandFile.js, chromAliasDefaults.js, updateReference.js, index.js, chromosome.js, chromAliasBB.js, loadSequence.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/cnvpytor/CombinedCaller.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.448 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.422 IQR)
- **Top Global Matches:** file_cluster_17: 14.448, file_cluster_4: 14.777, file_cluster_11: 14.827
- **Magnitude:** 1069.38 | **LOC:** 521 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 130
- **Risk Profile:** Cognitive Load (47.1966%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `call_2d` (Impact: 630.6 | O(N^6) | DB: 130)
    * *Intent:* /** * Creates an instance of CombinedCaller. * * @param {Array} wigFeatures - An array of arrays con...
  * `formatDataStructure` (Impact: 18.8 | O(N^5) | DB: 2)
  * `normal_merge` (Impact: 13.9 | O(N^2))
  * `likelihood_overlap` (Impact: 8.4 | O(N^2) | DB: 1)
  * `likelihood_of_baf` (Impact: 8.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 139`, `args: 35`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 355`, `dead_code: 4`
* *Architecture:* `api: 3`, `concurrency: 7`, `import: 3`
* *Defense:* `safety: 9`, `doc: 33`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GeneralUtil.js, baseCNVpytorVCF.js, t_dist.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/featureFileReader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.93 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.061 IQR)
- **Top Global Matches:** file_cluster_4: 13.93, file_cluster_13: 14.55, file_cluster_17: 14.657
- **Magnitude:** 966.68 | **LOC:** 389 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (79.5163%), Tech Debt (25.0795%)
**Top Internal Functions/Classes:**
  * `readHeader` (Impact: 101.5 | O(N^6) | DB: 43)
  * `loadFeaturesWithIndex` (Impact: 72.0 | O(N^6) | DB: 9)
  * `_parse` (Impact: 62.3 | O(2^N) | DB: 6)
  * `readFeatures` (Impact: 56.6 | O(N^4) | DB: 15)
  * `getParser` (Impact: 40.0 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 85`, `args: 17`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 319`, `fragile_debt: 2`
* *Architecture:* `api: 4`, `concurrency: 199`, `import: 12`
* *Defense:* `safety: 11`, `doc: 6`, `immutability_locks: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` indexFactory.js, bgzBlockLoader.js, segParser.js, gwasParser.js, index.js, qtlParser.js, igvUtils.js, featureParser.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/gwas/gwasTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.235 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.288 IQR)
- **Top Global Matches:** file_cluster_4: 14.235, file_cluster_13: 14.382, file_cluster_17: 14.514
- **Magnitude:** 889.12 | **LOC:** 258 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (91.7418%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `popupData` (Impact: 171.9 | O(2^N) | DB: 13)
  * `init` (Impact: 140.2 | O(2^N) | DB: 17)
  * `doAutoscale` (Impact: 86.1 | O(2^N) | DB: 11)
  * `postInit` (Impact: 69.2 | O(N^5) | DB: 25)
  * `draw` (Impact: 66.0 | O(N^5) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 30`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 277`, `dead_code: 1`
* *Architecture:* `api: 6`, `concurrency: 18`, `import: 8`
* *Defense:* `safety: 13`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` featureSource.js, igv-canvas.js, index.js, igvUtils.js, trackBase.js, colorScale.js, colorPalletes.js, gwasColors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/mergedTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.571 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.051 IQR)
- **Top Global Matches:** file_cluster_4: 14.571, file_cluster_17: 14.753, file_cluster_13: 14.917
- **Magnitude:** 888.08 | **LOC:** 506 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (57.2031%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `postInit` (Impact: 179.0 | O(2^N) | DB: 28)
  * `popupData` (Impact: 110.6 | O(2^N) | DB: 9)
  * `dataRange` (Impact: 63.0 | O(2^N) | DB: 2)
  * `autoscale` (Impact: 28.0 | O(2^N) | DB: 4)
  * `autoscaleGroup` (Impact: 28.0 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 47`, `args: 31`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 257`, `duplicate_logic: 12`
* *Architecture:* `api: 3`, `concurrency: 36`, `import: 5`
* *Defense:* `safety: 18`, `doc: 10`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dom-utils.js, index.js, igvUtils.js, trackBase.js, paintAxis.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/textFeatureSource.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.296 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.749 IQR)
- **Top Global Matches:** file_cluster_4: 15.296, file_cluster_13: 15.72, file_cluster_11: 15.95
- **Magnitude:** 843.34 | **LOC:** 281 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (70.4715%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadFeatures` (Impact: 137.3 | O(N^4) | DB: 34)
  * `constructor` (Impact: 115.1 | O(N^4) | DB: 24)
    * *Intent:* /** * feature source for "bed like" files (tab or whitespace delimited files with 1 feature per line...
  * `addFeaturesToDB` (Impact: 74.1 | O(N^6) | DB: 9)
  * `getHeader` (Impact: 49.4 | O(N^6) | DB: 9)
  * `defaultVisibilityWindow` (Impact: 21.0 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 44`, `args: 11`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 321`, `dead_code: 1`
* *Architecture:* `api: 5`, `concurrency: 85`, `import: 11`
* *Defense:* `safety: 27`, `doc: 7`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` customServiceReader.js, featureFileReader.js, baseFeatureSource.js, featureCache.js, featureUtils.js, chromAliasManager.js, wigSummary.js, genomicInterval.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/aed/AEDParser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.639 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.888 IQR)
- **Top Global Matches:** file_cluster_4: 13.639, file_cluster_8: 13.647, file_cluster_11: 13.877
- **Magnitude:** 834.2 | **LOC:** 472 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (72.2002%), Tech Debt (10.0879%)
**Top Internal Functions/Classes:**
  * `AedFeature` (Impact: 111.3 | O(N^4) | DB: 24)
  * `parseHeader` (Impact: 110.7 | O(N^6) | DB: 6)
  * `parseFeatures` (Impact: 80.9 | O(N^6) | DB: 11)
  * `decodeAed` (Impact: 80.6 | O(N^4) | DB: 8)
  * `parseTrackLine` (Impact: 53.6 | O(N^3) | DB: 6)
    * *Intent:* // Example entry:
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

### `js/bam/bamTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.245 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.464 IQR)
- **Top Global Matches:** file_cluster_13: 14.245, file_cluster_4: 14.314, file_cluster_11: 14.51
- **Magnitude:** 816.88 | **LOC:** 384 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (52.1016%), Tech Debt (99.4858%)
**Top Internal Functions/Classes:**
  * `getFeatures` (Impact: 62.5 | O(N^4) | DB: 15)
  * `addPairedChordsForViewport` (Impact: 55.6 | O(N^6) | DB: 4)
  * `init` (Impact: 36.8 | O(2^N) | DB: 15)
  * `menuItemList` (Impact: 36.3 | O(2^N) | DB: 22)
  * `hoverText` (Impact: 35.8 | O(2^N) | DB: 4)
    * *Intent:* /** * Return the features (alignment, coverage, downsampled interval) clicked on. Needed for "onclic...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 42`, `args: 34`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 300`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 7`, `concurrency: 12`, `import: 10`
* *Defense:* `safety: 11`, `doc: 12`, `immutability_locks: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` igv-canvas.js, index.js, coverageTrack.js, trackBase.js, circularViewUtils.js, colorPalletes.js, igv-icons.js, pairedEndStats.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/feature/decode/ucsc.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.503 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.622 IQR)
- **Top Global Matches:** file_cluster_8: 12.503, file_cluster_13: 12.742, file_cluster_7: 12.816
- **Magnitude:** 802.12 | **LOC:** 669 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (46.5258%), Tech Debt (22.7251%)
**Top Internal Functions/Classes:**
  * `decodeBed` (Impact: 376.8 | O(N^6) | DB: 6)
    * *Intent:* /**
  * `findUTRs` (Impact: 45.9 | O(N^4) | DB: 1)
  * `decodeWig` (Impact: 27.1 | O(N^2))
  * `decodeExons` (Impact: 23.3 | O(N^3) | DB: 2)
  * `decodeBedGraph` (Impact: 18.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 72`, `args: 28`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 167`, `duplicate_logic: 2`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 18`, `doc: 29`, `immutability_locks: 66`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gffHelper.js, parseAttributeString.js, decodeError.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `test/utils/w3XMLHttpRequest.js` (JAVASCRIPT) | Magnitude: 596.56 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 578, state_mutation: 246, doc: 123, func_start: 118
- `examples/events/locus-change.html` (HTML) | Magnitude: 27.14 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 22, decorators: 8, globals: 7
- `dev/events/custom-track-click.html` (HTML) | Magnitude: 41.6 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 23, state_mutation: 12, args: 8
- `examples/events/custom-track-popover.html` (HTML) | Magnitude: 37.86 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 21, state_mutation: 10, decorators: 8
- `dev/misc/maf_tcga.html` (HTML) | Magnitude: 19.76 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 7, decorators: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `js/ui/cursorGuide.js` (JAVASCRIPT) | Magnitude: 156.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 57, branch: 17, structural_boundaries: 10
- `js/bam/pairedEndStats.js` (JAVASCRIPT) | Magnitude: 217.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 116, indent_spaces: 49, branch: 21, structural_boundaries: 10
- `js/feature/gff/gffFeature.js` (JAVASCRIPT) | Magnitude: 591.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 243, indent_spaces: 171, branch: 59, structural_boundaries: 32
- `js/ui/cursorGuideButton.js` (JAVASCRIPT) | Magnitude: 41.26 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 21, structural_boundaries: 11, args: 4
- `js/feature/intervalTree.js` (JAVASCRIPT) | Magnitude: 384.7 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 170, state_mutation: 115, branch: 48, structural_boundaries: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `findLarge.sh` (SHELL) | Magnitude: 23.76 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 17, io: 12, structural_boundaries: 10, reflection_metaprogramming: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `dev/events/custom-track-popover.html` (HTML) | Magnitude: 39.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 21, state_mutation: 12, args: 8
- `js/feature/featureParser.js` (JAVASCRIPT) | Magnitude: 1322.66 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 396, indent_spaces: 323, branch: 176, structural_boundaries: 44
- `js/trackView.js` (JAVASCRIPT) | Magnitude: 1847.18 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 826, indent_spaces: 659, branch: 160, safety: 75
- `dev/cnvpytor/old/indexed_explicit_update.html` (HTML) | Magnitude: 75.92 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 24, immutability_locks: 17, args: 14
- `js/shoebox/shoeboxColorScale.js` (JAVASCRIPT) | Magnitude: 153.0 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 102, indent_spaces: 55, branch: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `js/igv.d.ts` (TYPESCRIPT) | Magnitude: 75.69 | Delta: **0.219 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 501, structural_boundaries: 239, branch: 231, generics: 115

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `js/events.js` (JAVASCRIPT) | Magnitude: 120.76 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 35, branch: 13, structural_boundaries: 6
- `js/sample/sampleInfoViewport.js` (JAVASCRIPT) | Magnitude: 596.08 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 288, indent_spaces: 278, branch: 66, immutability_locks: 62
- `js/feature/render/renderSnp.js` (JAVASCRIPT) | Magnitude: 158.46 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 30, branch: 19, structural_boundaries: 17
- `js/feature/gff/gffHelper.js` (JAVASCRIPT) | Magnitude: 433.14 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 167, state_mutation: 128, branch: 55, structural_boundaries: 30
- `js/ui/menuUtils.js` (JAVASCRIPT) | Magnitude: 402.46 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 214, state_mutation: 141, branch: 47, immutability_locks: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `dev/events/locus-change.html` (HTML) | Magnitude: 41.34 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 23, state_mutation: 15, args: 9
- `dev/interact/bedpe-10xSVs.html` (HTML) | Magnitude: 28.92 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 9, args: 6, concurrency: 6
- `js/aed/AEDParser.js` (JAVASCRIPT) | Magnitude: 834.2 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 296, state_mutation: 239, branch: 116, structural_boundaries: 57
- `dev/misc/custom-track.html` (HTML) | Magnitude: 42.06 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 14, state_mutation: 13, immutability_locks: 8
- `dev/igvjs.html` (HTML) | Magnitude: 26.58 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, concurrency: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/events/roi-events.html` (HTML) | Magnitude: 24.38 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 10, args: 9, listeners: 8
- `dev/misc/interactive-filtering.html` (HTML) | Magnitude: 1254.2 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1231, immutability_locks: 267, branch: 167, structural_boundaries: 148
- `examples/roi-api.html` (HTML) | Magnitude: 33.52 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 18, concurrency: 9, globals: 7
- `examples/igvjs.html` (HTML) | Magnitude: 20.6 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 7, args: 5, api: 4
- `js/feature/render/renderFeature.js` (JAVASCRIPT) | Magnitude: 1179.88 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 336, state_mutation: 166, branch: 107, structural_boundaries: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `js/genome/bpt.js` (JAVASCRIPT) | Magnitude: 10.52 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 18

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `js/trackViewport.js` -> Churn: **75.37%** | Cog Load: 69.3689% | Debt: 10.3306%
- `js/bam/alignmentTrack.js` -> Churn: **61.56%** | Cog Load: 84.6901% | Debt: 10.5801%
- `js/variant/variantTrack.js` -> Churn: **57.46%** | Cog Load: 85.3352% | Debt: 20.067%
- `js/igv-create.js` -> Churn: **52.73%** | Cog Load: 74.9763% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `js/bigwig/bwReader.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 2293.28
- `js/bam/alignmentContainer.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 1537.44
- `js/bam/alignmentTrack.js` -> **jrobinso** (85.7% isolated ownership) | Magnitude: 1398.84
- `js/feature/featureParser.js` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 1322.66
- `dev/misc/interactive-filtering.html` -> **jrobinso** (100.0% isolated ownership) | Magnitude: 1254.2

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `dev/ucsc/localFile/igvFileHelper.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)
- `dev/ucsc/localFile/trackJS_additions.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)
- `js/aed/AEDParser.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)
- `js/bam/alignmentContainer.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)
- `js/bam/bamAlignment.js` -> **Severity: 178.9** (Blast Radius: 1.789 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
