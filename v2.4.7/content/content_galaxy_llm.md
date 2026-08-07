# ARCHITECTURAL_BRIEF: content
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/content` |
| **Timestamp** | `2026-08-07T04:23:26.941916+00:00` |
| **Scan Duration** | `24.08s` |
| **Git Branch** | `main` |
| **Git Commit** | `3d49f18251e1f3493ef2e3a70519603345f8b7dc` |
| **Git Remote** | `https://github.com/mdn/content.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 17 malicious artifacts.

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
| Total Artifacts | 15935 |
| Analyzed Artifacts (Scanned) | 14185 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1750 |
| Total LOC | 8392 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.0% |
| Dominant Lang | MARKDOWN |

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
| MARKDOWN | 13964 | 0 | 98.4% |
| XML | 167 | 450 | 1.2% |
| YAML | 27 | 3897 | 0.2% |
| JAVASCRIPT | 17 | 1849 | 0.1% |
| JSON | 7 | 2192 | 0.0% |
| PLAINTEXT | 2 | 1 | 0.0% |
| HTML | 1 | 3 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.257`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 95 | 0.7% |
| file_cluster_4 | 5 | 0.0% |
| file_cluster_13 | 3 | 0.0% |
| file_cluster_17 | 2 | 0.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13965 | 98.4% |
| Static: Minified & Vendor Opaque Mass | 114 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1750*

**Composition by Extension & Reason:**
- `.png`: 1165x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 198x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Machine-Generated Source Code Signature: 147 LOC), 3x Excluded (Machine-Generated Source Code Signature: 46 LOC)
- `.jpg`: 126x Excluded (Explicitly Denied Extension: '.jpg')
- `.gif`: 63x Excluded (Explicitly Denied Extension: '.gif')
- `.yml`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 126708 LOC exceeds safe regex boundaries), 1x Excluded (Massive Static Asset Blob: 2678 LOC)
- `.svg`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1797 LOC)
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 17495 LOC)
- `.jpeg`: 5x Excluded (Explicitly Denied Extension: '.jpeg')
- `.jsonc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 85.5 | 3.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 92.2 | 1.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.3 | 0.4 | 0.0 | 0.0 |
| API Exposure | 0.0 | 11.6 | 0.3 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.8 | 2.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.8 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| Instability Exposure | 0.0 | 7.6 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 61.3 | 1.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 98.7 | 8.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/content/release-firefox.js` (Hits: 26)
- `scripts/filecheck/checker.js` (Hits: 26)
- `scripts/log-url-issues.js` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections
2. **LICENSE.md** (`LICENSE.md`) — 0 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **REVIEWING.md** (`REVIEWING.md`) — 0 inbound connections
5. **SECURITY.md** (`SECURITY.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **checker.js** (`scripts/filecheck/checker.js`) — 19 outbound dependencies
2. **analyze-pr-build.js** (`scripts/analyze-pr-build.js`) — 10 outbound dependencies
3. **front-matter_linter.js** (`scripts/front-matter_linter.js`) — 9 outbound dependencies
4. **front-matter_utils.js** (`scripts/front-matter_utils.js`) — 8 outbound dependencies
5. **index.js** (`scripts/filecheck/index.js`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `postAboutDangerousContent` (@ `scripts/analyze-pr-build.js`) -> Impact: **87.0** | LOC: 100
- `postAboutFlaws` (@ `scripts/analyze-pr-build.js`) -> Impact: **54.6** | LOC: 88
- `analyzePR` (@ `scripts/analyze-pr-build.js`) -> Impact: **46.5** | LOC: 99
  * *Intent:* /** * @import { Doc } from "@mdn/rari" */
- `checkFrontMatter` (@ `scripts/front-matter_utils.js`) -> Impact: **40.1** | LOC: 74
- `yargs` (@ `scripts/analyze-pr-build.js`) -> Impact: **35.8** | LOC: 75
- `main` (@ `scripts/content/release-firefox.js`) -> Impact: **32.3** | LOC: 86
- `getDeletedSlugs` (@ `scripts/log-url-issues.js`) -> Impact: **26.7** | LOC: 43
- `equalsIgnoreCase` (@ `scripts/sort_and_unique_file_lines.js`) -> Impact: **26.0** | LOC: 35
- `updateReleaseNotes` (@ `scripts/content/release-firefox.js`) -> Impact: **25.5** | LOC: 70
- `resolveDirectory` (@ `scripts/front-matter_linter.js`) -> Impact: **23.1** | LOC: 23

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 8 | 5041.4 | 0.0% | 0.0% |
| `scripts` | 10 | 1119.24 | 50.8% | 17.86% |
| `files/sidebars` | 27 | 479.44 | 4.09% | 0.0% |
| `scripts/filecheck` | 6 | 229.48 | 18.04% | 0.0% |
| `scripts/content` | 2 | 143.64 | 26.36% | 32.17% |
| `files/jsondata` | 5 | 104.74 | 1.0% | 0.0% |
| `files/en-us/web/api/ui_events/keyboard_event_key_values` | 1 | 93.34 | 0.0% | 0.0% |
| `files/en-us/web/api/ui_events/keyboard_event_code_values` | 1 | 67.08 | 0.0% | 0.0% |
| `files/en-us/web/api/keyboardevent/keycode` | 1 | 66.06 | 0.0% | 0.0% |
| `files/en-us/web/css/guides/backgrounds_and_borders/scaling_svg_backgrounds` | 5 | 55.22 | 4.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/analyze-pr-build.js` -> **92.2066%** Exposure
- `scripts/log-url-issues.js` -> **86.3872%** Exposure
- `scripts/content/release-firefox.js` -> **64.3339%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/analyze-pr-build.js` -> **99.8089%** Exposure
- `scripts/filecheck/utils.js` -> **98.532%** Exposure
- `scripts/update-moved-file-links.js` -> **94.2932%** Exposure
- `scripts/front-matter_utils.js` -> **83.5902%** Exposure
- `scripts/log-url-issues.js` -> **82.1178%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scripts/analyze-pr-build.js` -> **0** Orphaned Functions | **6** Duplicates
- `scripts/filecheck/checker.test.js` -> **0** Orphaned Functions | **6** Duplicates
- `scripts/log-url-issues.js` -> **0** Orphaned Functions | **3** Duplicates
- `scripts/content/release-firefox.js` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`scripts/analyze-pr-build.js`** -> AI Confidence: **99.31%**
2. **`scripts/filecheck/checker.js`** -> AI Confidence: **99.31%**
3. **`scripts/front-matter_utils.js`** -> AI Confidence: **99.31%**
4. **`scripts/front-matter_linter.js`** -> AI Confidence: **99.23%**
5. **`scripts/linkify-logs.js`** -> AI Confidence: **99.17%**
6. **`scripts/filecheck/index.js`** -> AI Confidence: **99.13%**
7. **`scripts/content/release-firefox.js`** -> AI Confidence: **99.09%**
8. **`scripts/update-moved-file-links.js`** -> AI Confidence: **99.09%**
9. **`scripts/log-url-issues.js`** -> AI Confidence: **99.06%**
10. **`scripts/sort_and_unique_file_lines.js`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `104` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `64` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scripts/analyze-pr-build.js` (JAVASCRIPT) -> Cumulative Risk: **532.52**
- **Archetype:** `file_cluster_4` (Distance: 12.47 IQR)
- **Magnitude:** 602.16 | **LOC:** 620 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9922%), State Flux (99.8089%), Tech Debt (92.2066%)
- **Heaviest Functions:** `postAboutDangerousContent` (Impact: 87.0), `postAboutFlaws` (Impact: 54.6), `analyzePR` (Impact: 46.5)

### 2. `scripts/front-matter_utils.js` (JAVASCRIPT) -> Cumulative Risk: **509.12**
- **Archetype:** `file_cluster_4` (Distance: 11.796 IQR)
- **Magnitude:** 88.44 | **LOC:** 101 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9984%), Cognitive Load (97.8775%), State Flux (83.5902%)
- **Heaviest Functions:** `checkFrontMatter` (Impact: 40.1), `getAjvValidator` (Impact: 3.7), `areAttributesInOrder` (Impact: 2.0)

### 3. `scripts/update-moved-file-links.js` (JAVASCRIPT) -> Cumulative Risk: **457.0**
- **Archetype:** `file_cluster_4` (Distance: 11.185 IQR)
- **Magnitude:** 80.96 | **LOC:** 146 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9997%), State Flux (94.2932%), Cognitive Load (82.8397%)
- **Heaviest Functions:** `movedFiles` (Impact: 19.5), `getImageSlug` (Impact: 11.1)

### 4. `scripts/front-matter_linter.js` (JAVASCRIPT) -> Cumulative Risk: **416.46**
- **Archetype:** `file_cluster_4` (Distance: 10.606 IQR)
- **Magnitude:** 89.96 | **LOC:** 125 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9875%), Cognitive Load (70.0955%), State Flux (57.7518%)
- **Heaviest Functions:** `resolveDirectory` (Impact: 23.1), `lintFrontMatter` (Impact: 19.5), `yargs` (Impact: 9.2)

### 5. `scripts/content/release-firefox.js` (JAVASCRIPT) -> Cumulative Risk: **403.12**
- **Archetype:** `file_cluster_8` (Distance: 9.736 IQR)
- **Magnitude:** 141.96 | **LOC:** 282 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (64.3339%), Cognitive Load (52.7264%)
- **Heaviest Functions:** `main` (Impact: 32.3), `updateReleaseNotes` (Impact: 25.5), `deactivatePreviousStable` (Impact: 11.5)

### 6. `scripts/log-url-issues.js` (JAVASCRIPT) -> Cumulative Risk: **399.56**
- **Archetype:** `file_cluster_17` (Distance: 10.442 IQR)
- **Magnitude:** 99.18 | **LOC:** 219 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (86.3872%), State Flux (82.1178%), Safety Score (66.7862%)
- **Heaviest Functions:** `getDeletedSlugs` (Impact: 26.7), `getFragmentDetails` (Impact: 18.4), `getFragmentDetails` (Impact: 6.5)

### 7. `scripts/filecheck/utils.js` (JAVASCRIPT) -> Cumulative Risk: **397.99**
- **Archetype:** `file_cluster_13` (Distance: 10.889 IQR)
- **Magnitude:** 36.34 | **LOC:** 43 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.532%), Documentation (97.2477%), Safety Score (56.2824%)
- **Heaviest Functions:** `correctContentPathFromEnv` (Impact: 11.2), `parseEnvValue` (Impact: 5.6), `correctPathFromEnv` (Impact: 3.9)

### 8. `scripts/update-interface-data.js` (JAVASCRIPT) -> Cumulative Risk: **374.18**
- **Archetype:** `file_cluster_4` (Distance: 9.663 IQR)
- **Magnitude:** 42.6 | **LOC:** 36 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (99.979%), Safety Score (51.0498%)

### 9. `scripts/utils.js` (JAVASCRIPT) -> Cumulative Risk: **341.92**
- **Archetype:** `file_cluster_13` (Distance: 9.619 IQR)
- **Magnitude:** 49.32 | **LOC:** 92 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (94.243%), Safety Score (56.3714%), Concurrency (43.6386%)
- **Heaviest Functions:** `getLocations` (Impact: 9.9), `walkSync` (Impact: 8.5), `stringToFragment` (Impact: 5.5)

### 10. `scripts/filecheck/checker.js` (JAVASCRIPT) -> Cumulative Risk: **331.61**
- **Archetype:** `file_cluster_13` (Distance: 11.376 IQR)
- **Magnitude:** 118.66 | **LOC:** 399 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9838%), Safety Score (47.3953%), Cognitive Load (26.5764%)
- **Heaviest Functions:** `resolveDirectory` (Impact: 12.8), `runChecker` (Impact: 12.3), `formatSize` (Impact: 5.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/analyze-pr-build.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.47 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.051 IQR)
- **Top Global Matches:** file_cluster_4: 12.47, file_cluster_8: 12.638, file_cluster_13: 12.739
- **Magnitude:** 602.16 | **LOC:** 620 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.12%), Tech Debt (92.2066%)
**Top Internal Functions/Classes:**
  * `postAboutDangerousContent` (Impact: 87.0)
  * `postAboutFlaws` (Impact: 54.6)
  * `analyzePR` (Impact: 46.5)
    * *Intent:* /** * @import { Doc } from "@mdn/rari" */
  * `yargs` (Impact: 35.8)
  * `getBuiltDocs` (Impact: 21.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 73`, `args: 21`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 149`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 12`, `concurrency: 76`, `import: 9`
* *Defense:* `safety: 24`, `doc: 34`, `test: 11`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yargs, promises, rest, node:crypto, node-html-parser, parse-diff, rari, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/content/release-firefox.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.736 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.882 IQR)
- **Top Global Matches:** file_cluster_8: 9.736, file_cluster_4: 9.818, file_cluster_7: 10.251
- **Magnitude:** 141.96 | **LOC:** 282 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (52.7264%), Tech Debt (64.3339%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 32.3)
  * `updateReleaseNotes` (Impact: 25.5)
  * `deactivatePreviousStable` (Impact: 11.5)
  * `createNightlyPage` (Impact: 4.3)
  * `formatDate` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 24`, `args: 6`, `func_start: 10`
* *Risk/State:* `state_mutation: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 26`, `concurrency: 51`, `import: 3`
* *Defense:* `safety: 6`, `doc: 7`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:path, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/filecheck/checker.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.376 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.35 IQR)
- **Top Global Matches:** file_cluster_13: 11.376, file_cluster_4: 11.432, file_cluster_8: 11.62
- **Magnitude:** 118.66 | **LOC:** 399 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.5764%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolveDirectory` (Impact: 12.8)
  * `runChecker` (Impact: 12.3)
  * `formatSize` (Impact: 5.6)
  * `canCheckFile` (Impact: 5.6)
  * `constructor` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 57`, `args: 16`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 24`
* *Architecture:* `io: 26`, `api: 4`, `concurrency: 42`, `import: 20`
* *Defense:* `safety: 14`, `doc: 42`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` imagemin-mozjpeg, fdir, is-svg, file-type, promises, imagemin, cheerio, env.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/log-url-issues.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.442 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.457 IQR)
- **Top Global Matches:** file_cluster_17: 10.442, file_cluster_8: 10.667, file_cluster_13: 11.094
- **Magnitude:** 99.18 | **LOC:** 219 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.2777%), Tech Debt (86.3872%)
**Top Internal Functions/Classes:**
  * `getDeletedSlugs` (Impact: 26.7)
  * `getFragmentDetails` (Impact: 18.4)
  * `getFragmentDetails` (Impact: 6.5)
  * `getFileAnchors` (Impact: 5.8)
  * `getFileContent` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 36`, `args: 25`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 31`, `duplicate_logic: 3`
* *Architecture:* `io: 19`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 5`, `immutability_locks: 27`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/api/ui_events/keyboard_event_key_values/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 93.34 | **LOC:** 4667 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/front-matter_linter.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.606 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.089 IQR)
- **Top Global Matches:** file_cluster_4: 10.606, file_cluster_13: 10.682, file_cluster_8: 10.762
- **Magnitude:** 89.96 | **LOC:** 125 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.0955%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolveDirectory` (Impact: 23.1)
  * `lintFrontMatter` (Impact: 19.5)
    * *Intent:* // lint front matter
  * `yargs` (Impact: 9.2)
  * `async` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 30`, `args: 10`, `func_start: 4`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 2`, `concurrency: 18`, `import: 9`
* *Defense:* `safety: 5`, `test: 3`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yargs, promises, cli-progress, front-matter_utils.js, async, node:path, helpers, fdir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/front-matter_utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.796 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.239 IQR)
- **Top Global Matches:** file_cluster_4: 11.796, file_cluster_17: 12.139, file_cluster_13: 12.15
- **Magnitude:** 88.44 | **LOC:** 101 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.8775%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkFrontMatter` (Impact: 40.1)
  * `getAjvValidator` (Impact: 3.7)
  * `areAttributesInOrder` (Impact: 2.0)
  * `getRelativePath` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 24`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 16`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 5`, `concurrency: 18`, `import: 8`
* *Defense:* `safety: 7`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yaml, promises, gray-matter, ajv, ajv-formats, better-ajv-errors, prettier, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/update-moved-file-links.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.185 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.442 IQR)
- **Top Global Matches:** file_cluster_4: 11.185, file_cluster_17: 11.415, file_cluster_8: 11.564
- **Magnitude:** 80.96 | **LOC:** 146 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.8397%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `movedFiles` (Impact: 19.5)
  * `getImageSlug` (Impact: 11.1)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 29`, `args: 7`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 21`
* *Architecture:* `io: 9`, `api: 1`, `concurrency: 26`, `import: 3`
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, utils.js, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/api/ui_events/keyboard_event_code_values/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 67.08 | **LOC:** 3354 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/api/keyboardevent/keycode/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 66.06 | **LOC:** 3303 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.619 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.455 IQR)
- **Top Global Matches:** file_cluster_13: 9.619, file_cluster_8: 9.695, file_cluster_17: 9.72
- **Magnitude:** 49.32 | **LOC:** 92 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.872%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLocations` (Impact: 9.9)
    * *Intent:* /*
  * `walkSync` (Impact: 8.5)
  * `stringToFragment` (Impact: 5.5)
  * `getRootDir` (Impact: 1.9)
  * `isImagePath` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 24`, `args: 9`, `func_start: 6`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 10`, `api: 11`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:child_process, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/update-interface-data.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.663 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 6.071 IQR)
- **Top Global Matches:** file_cluster_4: 9.663, file_cluster_17: 10.248, file_cluster_8: 10.299
- **Magnitude:** 42.6 | **LOC:** 36 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.979%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 3`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 11`, `concurrency: 26`, `import: 2`
* *Defense:* `safety: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/learn_web_development/extensions/forms/how_to_build_custom_form_controls/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 41.22 | **LOC:** 2061 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/media/guides/formats/video_codecs/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 38.66 | **LOC:** 1933 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/filecheck/utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.889 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.256 IQR)
- **Top Global Matches:** file_cluster_13: 10.889, file_cluster_8: 11.14, file_cluster_0: 11.392
- **Magnitude:** 36.34 | **LOC:** 43 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.9413%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `correctContentPathFromEnv` (Impact: 11.2)
  * `parseEnvValue` (Impact: 5.6)
  * `correctPathFromEnv` (Impact: 3.9)
  * `createRegExpFromExtensions` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 2`, `api: 7`, `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:path, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/sort_and_unique_file_lines.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.2 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.494 IQR)
- **Top Global Matches:** file_cluster_17: 11.2, file_cluster_8: 11.316, file_cluster_13: 11.62
- **Magnitude:** 36.12 | **LOC:** 64 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.9053%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `equalsIgnoreCase` (Impact: 26.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 10`, `args: 5`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 7`, `import: 1`
* *Defense:* `safety: 6`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/api/webgl_api/webgl_model_view_projection/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 34.06 | **LOC:** 1703 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/learn_web_development/extensions/forms/ui_pseudo-classes/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 29.76 | **LOC:** 1488 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/mozilla/add-ons/webextensions/manifest.json/theme/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 29.52 | **LOC:** 1476 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/html/reference/attributes/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 29.36 | **LOC:** 1468 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/filecheck/checker.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.449 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 7.275 IQR)
- **Top Global Matches:** file_cluster_8: 9.449, file_cluster_4: 9.753, file_cluster_13: 9.758
- **Magnitude:** 29.26 | **LOC:** 57 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.0785%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 4.0)
  * `it` (Impact: 2.1)
  * `it` (Impact: 2.1)
  * `it` (Impact: 2.1)
  * `it` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `args: 13`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 8`, `concurrency: 12`, `import: 5`
* *Defense:* `test: 22`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:test, node:url, strict, checker.js, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/html/reference/elements/input/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 28.76 | **LOC:** 1438 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/media/guides/formats/audio_codecs/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 28.6 | **LOC:** 1430 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/media/guides/formats/image_types/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 28.24 | **LOC:** 1412 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `scripts/filecheck/checker.js` (JAVASCRIPT) | Magnitude: 118.66 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 248, structural_boundaries: 57, branch: 53, doc: 42
- `scripts/utils.js` (JAVASCRIPT) | Magnitude: 49.32 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 24, branch: 17, api: 11
- `scripts/filecheck/utils.js` (JAVASCRIPT) | Magnitude: 36.34 | Delta: **0.251 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 14, branch: 8, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/sort_and_unique_file_lines.js` (JAVASCRIPT) | Magnitude: 36.12 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, branch: 18, immutability_locks: 11, structural_boundaries: 10
- `scripts/log-url-issues.js` (JAVASCRIPT) | Magnitude: 99.18 | Delta: **0.225 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 153, branch: 39, structural_boundaries: 36, state_mutation: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scripts/front-matter_linter.js` (JAVASCRIPT) | Magnitude: 89.96 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 30, branch: 24, concurrency: 18
- `scripts/analyze-pr-build.js` (JAVASCRIPT) | Magnitude: 602.16 | Delta: **0.168 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 478, state_mutation: 149, branch: 142, immutability_locks: 79
- `scripts/update-moved-file-links.js` (JAVASCRIPT) | Magnitude: 80.96 | Delta: **0.23 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 90, branch: 29, structural_boundaries: 29, concurrency: 26
- `scripts/front-matter_utils.js` (JAVASCRIPT) | Magnitude: 88.44 | Delta: **0.343 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 24, branch: 21, concurrency: 18
- `scripts/update-interface-data.js` (JAVASCRIPT) | Magnitude: 42.6 | Delta: **0.585 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: concurrency: 26, indent_spaces: 18, io: 11, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scripts/content/release-firefox.js` (JAVASCRIPT) | Magnitude: 141.96 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 155, concurrency: 51, branch: 28, io: 26
- `scripts/filecheck/index.js` (JAVASCRIPT) | Magnitude: 7.7 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, branch: 17, doc: 16, structural_boundaries: 11
- `scripts/filecheck/checker.test.js` (JAVASCRIPT) | Magnitude: 29.26 | Delta: **0.304 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 26, test: 22, sec_high_risk_execution: 14
- `scripts/up-to-date-check.js` (JAVASCRIPT) | Magnitude: 15.26 | Delta: **0.342 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, safety_bypasses: 3, structural_boundaries: 2, decorators: 2
- `scripts/filecheck/env.js` (JAVASCRIPT) | Magnitude: 17.16 | Delta: **0.403 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 3, immutability_locks: 3, indent_spaces: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/analyze-pr-build.js` -> **Claas Augner** (100.0% isolated ownership) | Magnitude: 602.16
- `scripts/content/release-firefox.js` -> **Vadim Makeev** (100.0% isolated ownership) | Magnitude: 141.96
- `scripts/filecheck/checker.js` -> **Claas Augner** (100.0% isolated ownership) | Magnitude: 118.66
- `scripts/front-matter_linter.js` -> **Claas Augner** (100.0% isolated ownership) | Magnitude: 89.96

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/filecheck/constants.js` -> **Severity: 6.908** (Blast Radius: 0.07 * Doc Risk: 98.682%)
- `scripts/filecheck/utils.js` -> **Severity: 6.807** (Blast Radius: 0.07 * Doc Risk: 97.2477%)
- `scripts/utils.js` -> **Severity: 6.597** (Blast Radius: 0.07 * Doc Risk: 94.243%)
- `scripts/front-matter_utils.js` -> **Severity: 3.832** (Blast Radius: 0.07 * Doc Risk: 54.7497%)
- `scripts/filecheck/env.js` -> **Severity: 3.645** (Blast Radius: 0.07 * Doc Risk: 52.0644%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
