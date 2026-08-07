# ARCHITECTURAL_BRIEF: pandoc
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pandoc` |
| **Timestamp** | `2026-08-07T05:20:46.104577+00:00` |
| **Scan Duration** | `2.42s` |
| **Git Branch** | `main` |
| **Git Commit** | `7777de6adb166d92b4c9ee4b24054637ab8477b7` |
| **Git Remote** | `https://github.com/jgm/pandoc.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 321 malicious artifacts.

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
| Total Artifacts | 2771 |
| Analyzed Artifacts (Scanned) | 501 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2270 |
| Total LOC | 83524 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 18.1% |
| Dominant Lang | HASKELL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3268 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2607 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 16.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1485 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| HASKELL | 290 | 77565 | 57.9% |
| YAML | 109 | 2233 | 21.8% |
| MARKDOWN | 30 | 0 | 6.0% |
| JSON | 18 | 120 | 3.6% |
| XML | 13 | 0 | 2.6% |
| LUA | 10 | 601 | 2.0% |
| SHELL | 9 | 297 | 1.8% |
| MAKEFILE | 4 | 338 | 0.8% |
| HTML | 4 | 1458 | 0.8% |
| PLAINTEXT | 3 | 0 | 0.6% |
| NIX | 3 | 74 | 0.6% |
| PERL | 2 | 77 | 0.4% |
| JAVASCRIPT | 2 | 237 | 0.4% |
| CSS | 1 | 200 | 0.2% |
| M4 | 1 | 29 | 0.2% |
| PYTHON | 1 | 294 | 0.2% |
| BINARY_THREAT | 1 | 1 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.21`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 299 | 59.7% |
| file_cluster_13 | 114 | 22.8% |
| file_cluster_17 | 47 | 9.4% |
| file_cluster_16 | 2 | 0.4% |
| file_cluster_4 | 2 | 0.4% |
| file_cluster_0 | 2 | 0.4% |
| file_cluster_12 | 1 | 0.2% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 33 | 6.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2270*

**Composition by Extension & Reason:**
- `.md`: 1076x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 301 LOC), 1x Excluded (Machine-Generated Source Code Signature: 169 LOC)
- `.native`: 254x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.docx`: 128x Excluded (Explicitly Denied Extension: '.docx')
- `.pptx`: 107x Excluded (Explicitly Denied Extension: '.pptx')
- `.hs`: 73x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 2102 hex tokens in 1086 LOC)
- `.odt`: 52x Excluded (Explicitly Denied Extension: '.odt')
- `no_extension`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 18x Unsupported Format (.undeterminable), 2x Excluded (Unsupported Extension: '.jats_publishing')
- `.strings`: 48x Excluded (Unsupported Extension: '.strings')
- `.lua`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 33x Excluded (Saturation: Line 2 exceeds 500 chars), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1134 LOC)
- `.csl`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.csl')
- `.rels`: 22x Excluded (Unsupported Extension: '.rels')
- `.yaml`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2238 LOC)
- `.latex`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Unsupported Extension: '.latex')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 17.7 | 9.1 | 9.1 |
| Error & Exception Exposure | 0.0 | 99.9 | 27.3 | 23.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.0 | 2.3 | 2.3 |
| API Exposure | 0.0 | 13.1 | 0.8 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 34.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 25.5 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 93.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.4 | 1.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.9 | 23.7 | 60.8 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `wasm/index.html` (Hits: 44)
- `src/Text/Pandoc/UTF8.hs` (Hits: 39)
- `tools/build-arm.sh` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Text.hs** (`pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Text.hs`) — 242 inbound connections
2. **Options.hs** (`src/Text/Pandoc/Options.hs`) — 133 inbound connections
3. **Shared.hs** (`src/Text/Pandoc/Shared.hs`) — 123 inbound connections
4. **PandocMonad.hs** (`src/Text/Pandoc/Class/PandocMonad.hs`) — 110 inbound connections
5. **Error.hs** (`src/Text/Pandoc/Error.hs`) — 96 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Readers.hs** (`src/Text/Pandoc/Readers.hs`) — 53 outbound dependencies
2. **Writers.hs** (`src/Text/Pandoc/Writers.hs`) — 52 outbound dependencies
3. **HTML.hs** (`src/Text/Pandoc/Writers/HTML.hs`) — 49 outbound dependencies
4. **Output.hs** (`src/Text/Pandoc/Writers/Powerpoint/Output.hs`) — 43 outbound dependencies
5. **OpenXML.hs** (`src/Text/Pandoc/Writers/Docx/OpenXML.hs`) — 42 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `escapeString` (@ `src/Text/Pandoc/Writers/AsciiDoc.hs`) -> Impact: **834.6** | LOC: 773
- `stNotes` (@ `src/Text/Pandoc/Writers/MediaWiki.hs`) -> Impact: **280.8** | LOC: 1078
- `renderImageOmit` (@ `src/Text/Pandoc/Writers/BBCode.hs`) -> Impact: **279.6** | LOC: 623
- `strContentRecursive` (@ `src/Text/Pandoc/Readers/XML.hs`) -> Impact: **191.4** | LOC: 350
- `escapeText` (@ `src/Text/Pandoc/Writers/Markdown/Inline.hs`) -> Impact: **180.3** | LOC: 186
- `disallowedInNode` (@ `src/Text/Pandoc/Writers/Texinfo.hs`) -> Impact: **132.6** | LOC: 270
- `smOn` (@ `src/Text/Pandoc/Readers/Mdoc.hs`) -> Impact: **123.7** | LOC: 594
- `egroup` (@ `src/Text/Pandoc/Readers/LaTeX/Parsing.hs`) -> Impact: **121.5** | LOC: 331
- `parse_polyglossia_value` (@ `tools/update-translations.py`) -> Impact: **121.0** | LOC: 179
- `rule` (@ `src/Text/Pandoc/Writers/ANSI.hs`) -> Impact: **77.9** | LOC: 311

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Text/Pandoc/Writers` | 49 | 41888.37 | 28.65% | 7.13% |
| `src/Text/Pandoc` | 42 | 17921.27 | 13.62% | 0.68% |
| `src/Text/Pandoc/Readers` | 43 | 11298.94 | 22.24% | 6.65% |
| `src/Text/Pandoc/Parsing` | 9 | 9309.78 | 11.52% | 1.17% |
| `src/Text/Pandoc/Readers/LaTeX` | 8 | 7611.05 | 30.12% | 3.48% |
| `src/Text/Pandoc/Readers/Pptx` | 4 | 4822.34 | 8.51% | 0.0% |
| `src/Text/Pandoc/Readers/Typst` | 2 | 4156.64 | 39.22% | 0.0% |
| `src/Text/Pandoc/Readers/HTML` | 4 | 3811.42 | 7.82% | 0.0% |
| `src/Text/Pandoc/Readers/ODT/Generic` | 5 | 3574.95 | 11.14% | 0.0% |
| `pandoc-lua-engine/src/Text/Pandoc/Lua/Module` | 15 | 3505.53 | 8.02% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `man/manfilter.lua` -> **100.0%** Exposure
- `tools/latex-package-dependencies.lua` -> **100.0%** Exposure
- `tools/moduledeps.lua` -> **100.0%** Exposure
- `tools/build-and-upload-api-docs.sh` -> **100.0%** Exposure
- `tools/diff-zip.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/Text/Pandoc/Writers/LaTeX/Caption.hs` -> **100.0%** Exposure
- `data/creole.lua` -> **100.0%** Exposure
- `tools/extract-changes.lua` -> **100.0%** Exposure
- `tools/latex-package-dependencies.lua` -> **100.0%** Exposure
- `tools/moduledeps.lua` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `data/creole.lua` -> **2** Orphaned Functions | **4** Duplicates
- `tools/moduledeps.lua` -> **1** Orphaned Functions | **5** Duplicates
- `wasm/examples/lua-filters/count_words.lua` -> **2** Orphaned Functions | **4** Duplicates
- `man/manfilter.lua` -> **5** Orphaned Functions | **0** Duplicates
- `tools/latex-package-dependencies.lua` -> **1** Orphaned Functions | **3** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/Text/Pandoc/Logging.hs`** -> AI Confidence: **99.48%**
2. **`src/Text/Pandoc/Readers/Docx/Lists.hs`** -> AI Confidence: **99.48%**
3. **`pandoc-lua-engine/src/Text/Pandoc/Lua/Module/JSON.hs`** -> AI Confidence: **99.39%**
4. **`src/Text/Pandoc/Citeproc/BibTeX.hs`** -> AI Confidence: **99.39%**
5. **`src/Text/Pandoc/Error.hs`** -> AI Confidence: **99.39%**
6. **`src/Text/Pandoc/Transforms.hs`** -> AI Confidence: **99.39%**
7. **`src/Text/Pandoc/Writers/LaTeX/Util.hs`** -> AI Confidence: **99.39%**
8. **`src/Text/Pandoc/Writers/Markdown.hs`** -> AI Confidence: **99.39%**
9. **`src/Text/Pandoc/Writers/Markdown/Inline.hs`** -> AI Confidence: **99.39%**
10. **`src/Text/Pandoc/Extensions.hs`** -> AI Confidence: **99.34%**
11. **`pandoc-cli/src/pandoc.hs`** -> AI Confidence: **99.31%**
12. **`pandoc-cli/wasm/PandocWasm.hs`** -> AI Confidence: **99.31%**
13. **`pandoc-lua-engine/src/Text/Pandoc/Lua/Documentation.hs`** -> AI Confidence: **99.31%**
14. **`pandoc-lua-engine/src/Text/Pandoc/Lua/Filter.hs`** -> AI Confidence: **99.31%**
15. **`pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Format.hs`** -> AI Confidence: **99.31%**
16. **`pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Image.hs`** -> AI Confidence: **99.31%**
17. **`pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Structure.hs`** -> AI Confidence: **99.31%**
18. **`pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Text.hs`** -> AI Confidence: **99.31%**
19. **`pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Utils.hs`** -> AI Confidence: **99.31%**
20. **`pandoc-server/src/Text/Pandoc/Server.hs`** -> AI Confidence: **99.31%**
21. **`src/Text/Pandoc/App.hs`** -> AI Confidence: **99.31%**
22. **`src/Text/Pandoc/App/CommandLineOptions.hs`** -> AI Confidence: **99.31%**
23. **`src/Text/Pandoc/App/Input.hs`** -> AI Confidence: **99.31%**
24. **`src/Text/Pandoc/App/Opt.hs`** -> AI Confidence: **99.31%**
25. **`src/Text/Pandoc/App/OutputSettings.hs`** -> AI Confidence: **99.31%**
26. **`src/Text/Pandoc/Chunks.hs`** -> AI Confidence: **99.31%**
27. **`src/Text/Pandoc/Citeproc/Locator.hs`** -> AI Confidence: **99.31%**
28. **`src/Text/Pandoc/Citeproc/MetaValue.hs`** -> AI Confidence: **99.31%**
29. **`src/Text/Pandoc/Citeproc/Name.hs`** -> AI Confidence: **99.31%**
30. **`src/Text/Pandoc/Class/IO.hs`** -> AI Confidence: **99.31%**
31. **`src/Text/Pandoc/Class/IO/HTTP.hs`** -> AI Confidence: **99.31%**
32. **`src/Text/Pandoc/Class/PandocMonad.hs`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4252` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wasm/index.js` (JAVASCRIPT) -> Cumulative Risk: **723.26**
- **Archetype:** `file_cluster_4` (Distance: 13.756 IQR)
- **Magnitude:** 182.28 | **LOC:** 1489 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.0332%)
- **Heaviest Functions:** `displayResults` (Impact: 40.3), `copyToClipboard` (Impact: 5.6), `download` (Impact: 4.7)

### 2. `tools/update-readme.lua` (LUA) -> Cumulative Risk: **587.18**
- **Archetype:** `file_cluster_8` (Distance: 13.854 IQR)
- **Magnitude:** 0.05 | **LOC:** 29 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9313%), Safety Score (98.2699%)
- **Heaviest Functions:** `Div` (Impact: 16.5), `__global_context__` (Impact: 1.5)

### 3. `tools/moduledeps.lua` (LUA) -> Cumulative Risk: **559.48**
- **Archetype:** `file_cluster_17` (Distance: 12.601 IQR)
- **Magnitude:** 0.12 | **LOC:** 78 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (93.1902%)
- **Heaviest Functions:** `add_transitive_deps` (Impact: 16.2), `Anonymous_Block` (Impact: 14.7), `Anonymous_Block` (Impact: 10.5)

### 4. `macos/make_macos_release.sh` (SHELL) -> Cumulative Risk: **555.04**
- **Archetype:** `file_cluster_8` (Distance: 10.155 IQR)
- **Magnitude:** 14.48 | **LOC:** 48 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9794%), Tech Debt (99.9141%), Safety Score (99.3839%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 3.6), `__global_context__` (Impact: 1.2)

### 5. `tools/validate-docx.sh` (SHELL) -> Cumulative Risk: **548.33**
- **Archetype:** `file_cluster_12` (Distance: 14.06 IQR)
- **Magnitude:** 0.05 | **LOC:** 31 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9639%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 17.9), `Anonymous_Block` (Impact: 5.2), `__global_context__` (Impact: 1.4)

### 6. `tools/diff-zip.sh` (SHELL) -> Cumulative Risk: **547.27**
- **Archetype:** `file_cluster_8` (Distance: 12.235 IQR)
- **Magnitude:** 0.04 | **LOC:** 34 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (98.8393%)
- **Heaviest Functions:** `__global_context__` (Impact: 6.9), `Anonymous_Block` (Impact: 6.2), `Anonymous_Block` (Impact: 3.1)

### 7. `tools/latex-package-dependencies.lua` (LUA) -> Cumulative Risk: **545.69**
- **Archetype:** `file_cluster_17` (Distance: 12.513 IQR)
- **Magnitude:** 0.03 | **LOC:** 27 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (95.0139%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 6.0), `Anonymous_Block` (Impact: 6.0), `Anonymous_Block` (Impact: 4.2)

### 8. `src/Text/Pandoc/Writers/LaTeX.hs` (HASKELL) -> Cumulative Risk: **537.99**
- **Archetype:** `file_cluster_17` (Distance: 14.192 IQR)
- **Magnitude:** 480.7 | **LOC:** 1512 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 55.6%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9988%), Cognitive Load (86.4578%), Verification (80.0%)
- **Heaviest Functions:** `pandocToLaTeX` (Impact: 50.7), `processPdfStandard` (Impact: 4.6), `writeBeamer` (Impact: 3.9)

### 9. `wasm/pandoc.js` (JAVASCRIPT) -> Cumulative Risk: **509.03**
- **Archetype:** `file_cluster_8` (Distance: 8.833 IQR)
- **Magnitude:** 84.56 | **LOC:** 168 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.3919%), Tech Debt (77.1397%)
- **Heaviest Functions:** `convert` (Impact: 28.8), `query` (Impact: 5.0), `memory_data_view` (Impact: 2.5)

### 10. `tools/build-arm.sh` (SHELL) -> Cumulative Risk: **507.52**
- **Archetype:** `file_cluster_8` (Distance: 11.549 IQR)
- **Magnitude:** 0.04 | **LOC:** 111 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9824%), Tech Debt (99.9757%), Safety Score (99.8824%)
- **Heaviest Functions:** `__global_context__` (Impact: 8.7), `Anonymous_Block` (Impact: 7.5), `Anonymous_Block` (Impact: 6.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Text/Pandoc/Writers/Textile.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.763 IQR)
- **Top Global Matches:** file_cluster_13: 13.763, file_cluster_8: 13.857, file_cluster_17: 13.956
- **Magnitude:** 6431.74 | **LOC:** 498 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.8352%), Tech Debt (12.2421%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 65`, `args: 27`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 121`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 15`
* *Defense:* `safety: 66`, `doc: 18`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.016
  * `Imports (Out-Degree: 10):` Control.Monad.State.Strict, Text.Pandoc.Templates, Text.Pandoc.Shared, Text.Pandoc.Class.PandocMonad, Text.DocLayout, Text.Pandoc.Writers.Shared, Data.Text, Text.Pandoc.Definition...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/DocBook.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.098 IQR)
- **Top Global Matches:** file_cluster_17: 12.098, file_cluster_13: 12.225, file_cluster_8: 12.25
- **Magnitude:** 6211.76 | **LOC:** 526 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.39%), Tech Debt (10.8964%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 66`, `args: 27`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 56`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 24`
* *Defense:* `safety: 52`, `doc: 13`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.016
  * `Imports (Out-Degree: 13):` Text.Pandoc.Highlighting, Text.Pandoc.Templates, Text.Pandoc.Shared, Text.TeXMath, Text.Pandoc.Builder, Text.Pandoc.URI, Text.Pandoc.Options, Data.Generics...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/PDF.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.471 IQR)
- **Top Global Matches:** file_cluster_13: 13.471, file_cluster_8: 13.591, file_cluster_17: 13.635
- **Magnitude:** 6039.43 | **LOC:** 681 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.3275%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 93`, `args: 32`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 90`
* *Architecture:* `io: 14`, `api: 1`, `import: 43`
* *Defense:* `safety: 158`, `doc: 28`, `immutability_locks: 44`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.602
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.007511
  * `Imports (Out-Degree: 16):` Data.Text.Lazy.Encoding, Text.Pandoc.Shared, Data.Text.Lazy, Text.Pandoc.Error, System.Exit, System.IO, Text.Pandoc.SelfContained, Text.Pandoc.Definition...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/DokuWiki.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.904 IQR)
- **Top Global Matches:** file_cluster_13: 12.904, file_cluster_8: 13.051, file_cluster_11: 13.141
- **Magnitude:** 5317.61 | **LOC:** 497 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5303%), Tech Debt (29.5024%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 57`, `args: 29`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `state_mutation: 94`, `planned_debt: 6`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 21`
* *Defense:* `safety: 43`, `doc: 19`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.016
  * `Imports (Out-Degree: 10):` Text.Pandoc.Templates, Text.Pandoc.Shared, Text.Pandoc.URI, Text.Pandoc.Definition, Text.Pandoc.Options, Data.Default, Text.Pandoc.Extensions, Text.Pandoc.Class.PandocMonad...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Parsing/General.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.816 IQR)
- **Top Global Matches:** file_cluster_13: 12.816, file_cluster_8: 12.949, file_cluster_17: 12.949
- **Magnitude:** 5314.31 | **LOC:** 763 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.3211%), Tech Debt (10.5488%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 62`, `args: 56`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 84`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 1`, `import: 31`
* *Defense:* `safety: 76`, `doc: 57`, `immutability_locks: 32`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.298
  * `Choke Point (Betweenness):` 0.000432 | `Ripple Effect (Closeness):` 0.1674
  * `Imports (Out-Degree: 15):` Control.Monad.Except, Text.Pandoc.Shared, Data.Text.Lazy, Text.Pandoc.Builder, Text.Pandoc.Error, Text.Pandoc.URI, Text.Pandoc.Sources, Text.Pandoc.Options...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/Pptx/Shapes.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.449 IQR)
- **Top Global Matches:** file_cluster_8: 12.449, file_cluster_13: 12.541, file_cluster_17: 12.656
- **Magnitude:** 4523.52 | **LOC:** 331 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.2766%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 52`, `args: 35`, `func_start: 19`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`
* *Architecture:* `import: 13`
* *Defense:* `safety: 64`, `doc: 19`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.65
  * `Choke Point (Betweenness):` 6e-05 | `Ripple Effect (Closeness):` 0.011879
  * `Imports (Out-Degree: 5):` Data.Maybe, Codec.Archive.Zip, Text.Pandoc.Class.PandocMonad, Data.List, Data.Text, Text.Pandoc.Readers.OOXML.Shared, Text.Read, Text.Pandoc.XML.Light...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/Man.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.374 IQR)
- **Top Global Matches:** file_cluster_13: 13.374, file_cluster_8: 13.558, file_cluster_17: 13.578
- **Magnitude:** 4178.88 | **LOC:** 380 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (37.683%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 64`, `args: 24`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`
* *Architecture:* `api: 1`, `import: 24`
* *Defense:* `safety: 58`, `doc: 19`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.016
  * `Imports (Out-Degree: 11):` Text.Pandoc.Highlighting, Text.Pandoc.Templates, Text.Pandoc.Shared, Text.Pandoc.Writers.Roff, Text.Pandoc.Builder, Text.Pandoc.URI, Control.Monad.Trans, Text.Pandoc.Options...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/Typst/Math.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.104 IQR)
- **Top Global Matches:** file_cluster_17: 14.104, file_cluster_13: 14.63, file_cluster_8: 14.661
- **Magnitude:** 4151.24 | **LOC:** 422 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.43%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 79`, `args: 18`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 150`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `safety: 157`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.626
  * `Choke Point (Betweenness):` 0.000228 | `Ripple Effect (Closeness):` 0.014019
  * `Imports (Out-Degree: 5):` Data.Maybe, Typst.Types, Data.Map, Text.Pandoc.Class, Data.Vector, Data.List, Data.Text, Text.Pandoc.Parsing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/Vimdoc.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.116 IQR)
- **Top Global Matches:** file_cluster_13: 13.116, file_cluster_8: 13.356, file_cluster_17: 13.389
- **Magnitude:** 3766.27 | **LOC:** 616 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.579%), Tech Debt (11.9203%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 71`, `args: 19`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 95`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 29`
* *Defense:* `safety: 64`, `doc: 9`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.016
  * `Imports (Out-Degree: 11):` Text.Pandoc.Templates, Text.Pandoc.Chunks, Text.Pandoc.Shared, Text.Pandoc.Error, Text.Pandoc.URI, Text.Pandoc.Definition, Text.Pandoc.Options, Text.Read...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/RTF.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.785 IQR)
- **Top Global Matches:** file_cluster_13: 12.785, file_cluster_8: 12.84, file_cluster_17: 13.001
- **Magnitude:** 3515.46 | **LOC:** 410 | **CtrlFlow:** 51.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.7737%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 54`, `args: 30`, `func_start: 22`
* *Risk/State:* `state_mutation: 48`
* *Architecture:* `api: 1`, `import: 21`
* *Defense:* `safety: 56`, `doc: 42`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.016
  * `Imports (Out-Degree: 11):` Text.Pandoc.Templates, Control.Monad.Except, Text.Pandoc.Shared, Text.Pandoc.Error, Text.Pandoc.Options, Data.ByteString, Text.Pandoc.Class.PandocMonad, Text.Pandoc.Logging...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/ODT/Generic/XMLConverter.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.203 IQR)
- **Top Global Matches:** file_cluster_8: 11.203, file_cluster_13: 11.492, file_cluster_7: 11.692
- **Magnitude:** 3442.41 | **LOC:** 782 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.0938%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 57`, `args: 74`, `func_start: 64`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `dead_code: 6`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 43`, `doc: 38`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.975
  * `Choke Point (Betweenness):` 0.00016 | `Ripple Effect (Closeness):` 0.016822
  * `Imports (Out-Degree: 7):` Data.Maybe, Prelude, Data.List.NonEmpty, Control.Applicative, Data.Map, Data.Either, Data.Default, Text.Pandoc.Readers.ODT.Generic.Fallible...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Parsing/GridTable.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.125 IQR)
- **Top Global Matches:** file_cluster_8: 11.125, file_cluster_13: 11.249, file_cluster_7: 11.516
- **Magnitude:** 3137.56 | **LOC:** 309 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (7.0534%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 32`, `args: 38`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `import: 14`
* *Defense:* `safety: 15`, `doc: 34`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.3
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.16336
  * `Imports (Out-Degree: 5):` Data.Array, Data.Maybe, Text.Pandoc.Parsing.General, Safe, Text.Pandoc.Builder, Text.Parsec, Data.Text, Text.Pandoc.Sources...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Logging.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.161 IQR)
- **Top Global Matches:** file_cluster_8: 8.161, file_cluster_7: 9.196, file_cluster_13: 9.307
- **Magnitude:** 2842.44 | **LOC:** 506 | **CtrlFlow:** 81.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (11.9452%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 22`, `args: 6`, `func_start: 4`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 1`, `import: 12`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.974
  * `Choke Point (Betweenness):` 0.001775 | `Ripple Effect (Closeness):` 0.242118
  * `Imports (Out-Degree: 2):` GHC.Generics, Data.Typeable, Data.Data, Text.Parsec.Pos, Text.Pandoc.Shared, Data.Aeson, Data.Text, Text.Pandoc.Definition...
  * `Imported By (In-Degree: 83):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/LaTeX/SIunitx.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.649 IQR)
- **Top Global Matches:** file_cluster_8: 11.649, file_cluster_17: 11.893, file_cluster_13: 11.925
- **Magnitude:** 2791.01 | **LOC:** 472 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.19%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 31`, `args: 27`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 69`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 42`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.611
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.104275
  * `Imports (Out-Degree: 6):` Control.Applicative, Data.Map, Text.Pandoc.Class.PandocMonad, Text.Pandoc.Builder, Text.Pandoc.Parsing, Data.Text, Data.List, Text.Pandoc.Walk...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/HTML/Table.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.224 IQR)
- **Top Global Matches:** file_cluster_13: 12.224, file_cluster_8: 12.245, file_cluster_17: 12.398
- **Magnitude:** 2628.88 | **LOC:** 308 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.5897%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 44`, `args: 32`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 22`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 51`, `doc: 9`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.619
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.103169
  * `Imports (Out-Degree: 7):` Data.Maybe, Text.Pandoc.Readers.HTML.Types, Data.List.NonEmpty, Control.Applicative, Text.HTML.TagSoup, Text.Pandoc.Shared, Data.Either, Text.Pandoc.Builder...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/ODT.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.304 IQR)
- **Top Global Matches:** file_cluster_13: 12.304, file_cluster_8: 12.448, file_cluster_17: 12.573
- **Magnitude:** 2430.9 | **LOC:** 380 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.8352%), Tech Debt (17.3938%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 63`, `args: 21`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 46`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 36`
* *Defense:* `safety: 59`, `doc: 8`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.016
  * `Imports (Out-Degree: 16):` Text.Pandoc.Writers.OpenDocument, Control.Monad.Except, Text.Pandoc.Shared, Text.TeXMath, Data.Text.Lazy, Text.Pandoc.Error, Data.Time, Text.Pandoc.Options...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/LaTeX/Lang.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.982 IQR)
- **Top Global Matches:** file_cluster_17: 13.982, file_cluster_8: 14.045, file_cluster_13: 14.192
- **Magnitude:** 2292.03 | **LOC:** 239 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.792%), Tech Debt (15.6799%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 12`, `args: 96`, `func_start: 9`
* *Risk/State:* `state_mutation: 13`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 124`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.611
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.104275
  * `Imports (Out-Degree: 6):` Text.Pandoc.Translations, Text.Pandoc.Shared, Data.Map, Text.Pandoc.Class, Text.Pandoc.Builder, Text.Pandoc.Parsing, Data.Text, Text.Collate.Lang...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/App/OutputSettings.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.197 IQR)
- **Top Global Matches:** file_cluster_17: 13.197, file_cluster_13: 13.326, file_cluster_8: 13.476
- **Magnitude:** 2286.84 | **LOC:** 344 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.5867%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 40`, `args: 15`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 55`
* *Architecture:* `io: 2`, `import: 25`
* *Defense:* `safety: 83`, `doc: 6`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.602
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.007511
  * `Imports (Out-Degree: 12):` Text.Pandoc.Highlighting, Text.Pandoc.Chunks, Control.Monad.Except, System.Exit, System.IO, Control.Monad.Trans, System.FilePath, Text.DocTemplates...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/Roff.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.844 IQR)
- **Top Global Matches:** file_cluster_17: 12.844, file_cluster_13: 12.849, file_cluster_8: 12.965
- **Magnitude:** 2255.41 | **LOC:** 565 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.102%), Tech Debt (12.7169%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 60`, `args: 42`, `func_start: 20`, `class_start: 11`
* *Risk/State:* `state_mutation: 64`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `import: 16`
* *Defense:* `safety: 50`, `doc: 1`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.014019
  * `Imports (Out-Degree: 8):` Text.Pandoc.Readers.Roff.Escape, Control.Monad.Except, Data.Foldable, Text.Pandoc.Shared, Safe, Data.Map, Text.Pandoc.Class.PandocMonad, Data.Default...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/XML.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.263 IQR)
- **Top Global Matches:** file_cluster_8: 8.263, file_cluster_7: 9.073, file_cluster_1: 9.269
- **Magnitude:** 1929.08 | **LOC:** 523 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.5382%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 20`, `args: 25`, `func_start: 20`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 7`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.608
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.204307
  * `Imports (Out-Degree: 2):` Text.HTML.TagSoup.Entity, Data.Map, Text.DocLayout, Commonmark.Entity, Data.Set, Data.Text, Data.Char, Text.Printf...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `pandoc-lua-engine/src/Text/Pandoc/Lua/Writer/Scaffolding.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.133 IQR)
- **Top Global Matches:** file_cluster_8: 11.133, file_cluster_13: 11.166, file_cluster_17: 11.353
- **Magnitude:** 1822.69 | **LOC:** 312 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.3828%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 40`, `args: 44`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 1`, `import: 23`
* *Defense:* `safety: 26`, `doc: 6`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.741
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004129
  * `Imports (Out-Degree: 9):` Text.Pandoc.Templates, Data.Data, Text.Pandoc.Error, Text.Pandoc.Definition, Text.Pandoc.Options, Data.Default, Data.ByteString, Text.DocTemplates...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/TEI.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.776 IQR)
- **Top Global Matches:** file_cluster_17: 11.776, file_cluster_13: 11.861, file_cluster_8: 11.931
- **Magnitude:** 1661.88 | **LOC:** 297 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2117%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 40`, `args: 15`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 27`, `doc: 10`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.016
  * `Imports (Out-Degree: 11):` Text.Pandoc.Highlighting, Text.Pandoc.Templates, Text.Pandoc.Shared, Text.Pandoc.Class.PandocMonad, Text.DocLayout, Text.Pandoc.Writers.Shared, Data.Text, Text.Pandoc.URI...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Data.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.148 IQR)
- **Top Global Matches:** file_cluster_17: 13.148, file_cluster_13: 13.237, file_cluster_8: 13.389
- **Magnitude:** 1658.4 | **LOC:** 246 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.1877%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 29`, `args: 11`, `func_start: 8`
* *Risk/State:* `state_mutation: 55`
* *Architecture:* `io: 2`, `api: 1`, `import: 14`
* *Defense:* `safety: 46`, `doc: 7`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.248
  * `Choke Point (Betweenness):` 0.001004 | `Ripple Effect (Closeness):` 0.170704
  * `Imports (Out-Degree: 5):` Codec.Archive.Zip, Control.Monad.Except, Text.Pandoc.Shared, Text.Pandoc.Class, Text.Pandoc.Error, Data.Time.Clock.POSIX, Data.Text, System.Directory...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/Jira.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.346 IQR)
- **Top Global Matches:** file_cluster_8: 9.346, file_cluster_13: 9.841, file_cluster_7: 10.015
- **Magnitude:** 1407.22 | **LOC:** 214 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.555%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 24`, `args: 17`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 12`
* *Defense:* `safety: 10`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.587
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.017558
  * `Imports (Out-Degree: 7):` Control.Monad.Except, Text.Jira.Parser, Text.Pandoc.Shared, Text.Pandoc.Class.PandocMonad, Text.Pandoc.Builder, Text.Pandoc.Error, Data.List, Data.Text...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/LaTeX/Inline.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.763 IQR)
- **Top Global Matches:** file_cluster_8: 11.763, file_cluster_17: 11.93, file_cluster_13: 11.966
- **Magnitude:** 1208.27 | **LOC:** 453 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.9875%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 29`, `args: 31`, `func_start: 27`
* *Risk/State:* `state_mutation: 35`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 65`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.611
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.104275
  * `Imports (Out-Degree: 11):` Text.Pandoc.Highlighting, Data.Maybe, Text.Pandoc.Translations, Text.Pandoc.Shared, Data.Map, Control.Applicative, Text.Pandoc.Builder, Text.Pandoc.Class.PandocMonad...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `macos/uninstall-pandoc.pl` (PERL) | Magnitude: 82.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 66, indent_spaces: 29, branch: 25, structural_boundaries: 13
- `wasm/index.html` (HTML) | Magnitude: 111.98 | Delta: **0.226 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1208, decorators: 522, args: 440, structural_boundaries: 238

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tools/validate-docx.sh` (SHELL) | Magnitude: 0.05 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 18, branch: 15, reflection_metaprogramming: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Text/Pandoc/Writers/Markdown/Inline.hs` (HASKELL) | Magnitude: 395.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 595, branch: 259, state_mutation: 138, safety: 112
- `pandoc-lua-engine/src/Text/Pandoc/Lua/Module/MediaBag.hs` (HASKELL) | Magnitude: 209.23 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 86, import: 17, structural_boundaries: 12, doc: 9
- `src/Text/Pandoc/Writers/JATS/Types.hs` (HASKELL) | Magnitude: 17.84 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, doc: 11, structural_boundaries: 7, import: 7
- `src/Text/Pandoc/Readers/Org/BlockStarts.hs` (HASKELL) | Magnitude: 763.82 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 82, safety: 20, state_mutation: 19, args: 17
- `src/Text/Pandoc/Readers/HTML/Table.hs` (HASKELL) | Magnitude: 2628.88 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 188, safety: 51, structural_boundaries: 44, branch: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/Text/Pandoc/Writers/BBCode.hs` (HASKELL) | Magnitude: 420.08 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 631, safety: 114, args: 111, generics: 100
- `pandoc-lua-engine/src/Text/Pandoc/Lua/Marshal/CommonState.hs` (HASKELL) | Magnitude: 27.76 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4, args: 3, func_start: 3, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Text/Pandoc/Readers/Roff.hs` (HASKELL) | Magnitude: 2255.41 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 229, state_mutation: 64, structural_boundaries: 60, safety: 50
- `src/Text/Pandoc/Writers/LaTeX.hs` (HASKELL) | Magnitude: 480.7 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 922, state_mutation: 387, branch: 347, structural_boundaries: 167
- `src/Text/Pandoc/Readers/Mdoc.hs` (HASKELL) | Magnitude: 258.86 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 396, state_mutation: 92, args: 77, safety: 73
- `src/Text/Pandoc/Readers/Docx.hs` (HASKELL) | Magnitude: 282.74 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 538, state_mutation: 247, branch: 141, safety: 138
- `src/Text/Pandoc/Readers/LaTeX/Citation.hs` (HASKELL) | Magnitude: 129.12 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 156, state_mutation: 31, safety: 27, structural_boundaries: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Text/Pandoc/Process.hs` (HASKELL) | Magnitude: 69.24 | Delta: **0.23 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 48, indent_spaces: 38, safety: 13, io: 12
- `wasm/index.js` (JAVASCRIPT) | Magnitude: 182.28 | Delta: **0.531 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 97, indent_spaces: 85, branch: 29, concurrency: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Pandoc.hs` (HASKELL) | Magnitude: 75.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 375, structural_boundaries: 50, args: 47, branch: 40
- `src/Text/Pandoc/Writers/ConTeXt.hs` (HASKELL) | Magnitude: 212.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 564, branch: 171, safety: 141, state_mutation: 135
- `src/Text/Pandoc/Writers/OOXML.hs` (HASKELL) | Magnitude: 5.06 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, safety: 17, branch: 13, args: 12
- `src/Text/Pandoc/Readers/LaTeX/Parsing.hs` (HASKELL) | Magnitude: 333.48 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 634, branch: 141, state_mutation: 141, safety: 130
- `pandoc-lua-engine/src/Text/Pandoc/Lua/Marshal/Sources.hs` (HASKELL) | Magnitude: 80.4 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 7, args: 6, import: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Text/Pandoc/Readers/Markdown.hs` -> Churn: **63.34%** | Cog Load: 55.6213% | Debt: 0.0%
- `src/Text/Pandoc/Readers/Docx/Parse.hs` -> Churn: **54.69%** | Cog Load: 55.832% | Debt: 8.7218%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Text/Pandoc/Writers/DocBook.hs` -> **John MacFarlane** (100.0% isolated ownership) | Magnitude: 6211.76
- `src/Text/Pandoc/PDF.hs` -> **John MacFarlane** (100.0% isolated ownership) | Magnitude: 6039.43
- `src/Text/Pandoc/Parsing/General.hs` -> **John MacFarlane** (100.0% isolated ownership) | Magnitude: 5314.31
- `src/Text/Pandoc/Readers/Pptx/Shapes.hs` -> **Anton Antich** (100.0% isolated ownership) | Magnitude: 4523.52
- `src/Text/Pandoc/Writers/Vimdoc.hs` -> **reptee** (100.0% isolated ownership) | Magnitude: 3766.27

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Text/Pandoc/Citeproc.hs` -> **Severity: 1.975** (Bridge: 0.0332 * Flux: 59.4951%)
- `src/Text/Pandoc/Citeproc/BibTeX.hs` -> **Severity: 1.571** (Bridge: 0.0164 * Flux: 95.6433%)
- `src/Text/Pandoc/Readers/Markdown.hs` -> **Severity: 1.002** (Bridge: 0.0101 * Flux: 99.4869%)
- `src/Text/Pandoc/Readers/LaTeX.hs` -> **Severity: 1.001** (Bridge: 0.01 * Flux: 99.7799%)
- `src/Text/Pandoc/Writers/LaTeX.hs` -> **Severity: 0.893** (Bridge: 0.0089 * Flux: 99.9988%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Text/Pandoc/Error.hs` -> **Severity: 19.827** (Embedded: 0.3278 * Error Risk: 60.4925%)
- `src/Text/Pandoc/UTF8.hs` -> **Severity: 15.934** (Embedded: 0.267 * Error Risk: 59.6707%)
- `pandoc-lua-engine/src/Text/Pandoc/Lua/PandocLua.hs` -> **Severity: 15.306** (Embedded: 0.2746 * Error Risk: 55.7451%)
- `src/Text/Pandoc/Shared.hs` -> **Severity: 14.317** (Embedded: 0.3083 * Error Risk: 46.4425%)
- `pandoc-lua-engine/src/Text/Pandoc/Lua/Marshal/PandocError.hs` -> **Severity: 14.31** (Embedded: 0.186 * Error Risk: 76.9345%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Text.hs` -> **Severity: 7218.847** (Blast Radius: 159.245 * Doc Risk: 45.3317%)
- `src/Text/Pandoc/Version.hs` -> **Severity: 2174.485** (Blast Radius: 37.243 * Doc Risk: 58.3864%)
- `src/Text/Pandoc/Class.hs` -> **Severity: 1866.891** (Blast Radius: 25.767 * Doc Risk: 72.4528%)
- `src/Text/Pandoc/Error.hs` -> **Severity: 1343.485** (Blast Radius: 61.516 * Doc Risk: 21.8396%)
- `src/Text/Pandoc/Char.hs` -> **Severity: 1205.498** (Blast Radius: 28.395 * Doc Risk: 42.4546%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
