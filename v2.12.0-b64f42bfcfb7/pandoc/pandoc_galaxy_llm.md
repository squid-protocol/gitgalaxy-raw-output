# ARCHITECTURAL_BRIEF: pandoc
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jgm/pandoc.git` |
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
- **Scope:** 1739 analyzed artifact(s), 105812 LOC.
- **Load-bearing artifact:** `pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Text.hs` -- 292 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `test/test-pandoc.hs` -- pulls in 55 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Text/Pandoc/Writers/Powerpoint/Output.hs` at magnitude 838.02 (structural weight, not risk).
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
| Total Artifacts | 2771 |
| Analyzed Artifacts (Scanned) | 1739 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1032 |
| Total LOC | 105812 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 62.8% |
| Dominant Lang | HASKELL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2867 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2129 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 16.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8131 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 1125 | 0 | 64.7% |
| HASKELL | 363 | 96556 | 20.9% |
| YAML | 130 | 2850 | 7.5% |
| LUA | 46 | 3194 | 2.6% |
| XML | 23 | 0 | 1.3% |
| PLAINTEXT | 17 | 0 | 1.0% |
| HTML | 11 | 1834 | 0.6% |
| SHELL | 9 | 297 | 0.5% |
| MAKEFILE | 3 | 314 | 0.2% |
| NIX | 3 | 74 | 0.2% |
| PERL | 3 | 161 | 0.2% |
| CSV | 2 | 6 | 0.1% |
| CSS | 1 | 200 | 0.1% |
| M4 | 1 | 29 | 0.1% |
| RUBY | 1 | 3 | 0.1% |
| PYTHON | 1 | 294 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1739 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 77%, State Mutators Files 7%, Large Core Modules (3) 6%, Declarative / Non-Code 4%, Large Core Modules (2) 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 597 | 34.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1142 | 65.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1032*

**Composition by Extension & Reason:**
- `.native`: 254x Excluded (Unsupported Extension: '.native')
- `.docx`: 128x Excluded (Explicitly Denied Extension: '.docx')
- `.pptx`: 107x Excluded (Explicitly Denied Extension: '.pptx')
- `.odt`: 52x Excluded (Explicitly Denied Extension: '.odt')
- `no_extension`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Unsupported Extension: '.jats_archiving'), 5x Unsupported Format (.undeterminable)
- `.strings`: 48x Excluded (Unsupported Extension: '.strings')
- `.xml`: 33x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Static Asset Blob without Intent: 1134 LOC), 1x Excluded (Static Asset Blob without Intent: 1461 LOC)
- `.csl`: 27x Excluded (Unsupported Extension: '.csl'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rels`: 22x Excluded (Unsupported Extension: '.rels')
- `.json`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.latex`: 17x Excluded (Unsupported Extension: '.latex')
- `.rtf`: 15x Excluded (Unsupported Extension: '.rtf')
- `.fb2`: 14x Excluded (Unsupported Extension: '.fb2')
- `.yaml`: 8x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.epub`: 10x Excluded (Unsupported Extension: '.epub')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 87.2 | 4.2 | 2.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.5 | 15.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.9 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.4 | 6.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 48.8 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 57.3 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.4 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 46.1 | 40.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 204 | 55 | 0 | `src/Text/Pandoc/ImageSize.hs` |
| cleanup | 97 | 29 | 0 | `src/Text/Pandoc/Readers/Pod.hs` |
| guards | 3189 | 358 | 3 | `src/Text/Pandoc/Readers/Markdown.hs` |
| danger | 600 | 125 | 0 | `linux/make_artifacts.sh` |
| concurrency | 38 | 11 | 0 | `src/Text/Pandoc/Process.hs` |
| connectivity | 1162 | 386 | 2 | `Makefile` |
| io | 505 | 81 | 0 | `test/html-reader.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 38 | 11 | 0 | `Makefile` |
| time | 27 | 11 | 0 | `src/Text/Pandoc/Class/PandocMonad.hs` |
| serialization | 72 | 28 | 0 | `pandoc-lua-engine/src/Text/Pandoc/Lua/Module/JSON.hs` |
| regex | 53 | 13 | 0 | `macos/uninstall-pandoc.pl` |
| events | 163 | 33 | 0 | `src/Text/Pandoc/Parsing/General.hs` |
| tests | 1066 | 83 | 0 | `pandoc-lua-engine/test/lua/module/pandoc.lua` |
| docs | 2664 | 258 | 3 | `src/Text/Pandoc/Extensions.hs` |
| debt | 554 | 143 | 0 | `test/Tests/Readers/Org/Block/Header.hs` |
| mutation | 20212 | 426 | 27 | `src/Text/Pandoc/Writers/Powerpoint/Output.hs` |
| dead_code | 145 | 56 | 0 | `pandoc-lua-engine/test/sample.lua` |
| credential | 6 | 3 | 0 | `test/Tests/Readers/JATS.hs` |
| threat | 18 | 5 | 0 | `data/translations/fa.yaml` |
| ml_ai | 81 | 28 | 0 | `src/Text/Pandoc/PDF.hs` |
| ui | 54 | 9 | 0 | `test/html-reader.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/html-reader.html` (Hits: 66)
- `src/Text/Pandoc/UTF8.hs` (Hits: 39)
- `tools/build-arm.sh` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Text.hs** (`pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Text.hs`) — 292 inbound connections
2. **Man.hs** (`src/Text/Pandoc/Readers/Man.hs`) — 159 inbound connections
3. **PandocMonad.hs** (`src/Text/Pandoc/Class/PandocMonad.hs`) — 138 inbound connections
4. **Options.hs** (`src/Text/Pandoc/Options.hs`) — 138 inbound connections
5. **Shared.hs** (`src/Text/Pandoc/Shared.hs`) — 130 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test-pandoc.hs** (`test/test-pandoc.hs`) — 55 outbound dependencies
2. **Readers.hs** (`src/Text/Pandoc/Readers.hs`) — 53 outbound dependencies
3. **Writers.hs** (`src/Text/Pandoc/Writers.hs`) — 52 outbound dependencies
4. **HTML.hs** (`src/Text/Pandoc/Writers/HTML.hs`) — 49 outbound dependencies
5. **Output.hs** (`src/Text/Pandoc/Writers/Powerpoint/Output.hs`) — 43 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inlineToMarkdown` **(Many-Argument Workhorses)** (@ `src/Text/Pandoc/Writers/Markdown/Inline.hs`) -> Impact: **243.1** | LOC: 393
  * *Intent:* -- | Convert Pandoc inline element to markdown.
- `blockToMarkdown'` **(Many-Argument Workhorses)** (@ `src/Text/Pandoc/Writers/Markdown.hs`) -> Impact: **213.9** | LOC: 398
- `blockToLaTeX` **(Compute Cores)** (@ `src/Text/Pandoc/Writers/LaTeX.hs`) -> Impact: **134.5** | LOC: 342
  * *Intent:* -- | Convert Pandoc block element to LaTeX.
- `inlineToLaTeX` **(Compute Cores)** (@ `src/Text/Pandoc/Writers/LaTeX.hs`) -> Impact: **131.6** | LOC: 341
  * *Intent:* -- | Convert inline element to LaTeX
- `inlineToHtml` **(Many-Argument Workhorses)** (@ `src/Text/Pandoc/Writers/HTML.hs`) -> Impact: **131.2** | LOC: 269
  * *Intent:* -- | Convert Pandoc inline element to HTML.
- `blockToAsciiDoc` **(Compute Cores)** (@ `src/Text/Pandoc/Writers/AsciiDoc.hs`) -> Impact: **127.2** | LOC: 257
  * *Intent:* -- | Convert Pandoc block element to asciidoc.
- `obfuscateLink` **(Many-Argument Workhorses)** (@ `src/Text/Pandoc/Writers/HTML.hs`) -> Impact: **124.3** | LOC: 249
  * *Intent:* -- | Obfuscate a "mailto:" link.
- `convertWithOpts'` **(Many-Argument Workhorses)** (@ `src/Text/Pandoc/App.hs`) -> Impact: **99.7** | LOC: 205
- `writeBibtexString` **(Many-Argument Workhorses)** (@ `src/Text/Pandoc/Citeproc/BibTeX.hs`) -> Impact: **89.4** | LOC: 267
  * *Intent:* -- | Write BibTeX or BibLaTeX given given a 'Reference'.
- `blockToOpenXML'` **(Many-Argument Workhorses)** (@ `src/Text/Pandoc/Writers/Docx/OpenXML.hs`) -> Impact: **86.2** | LOC: 199

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/Text/Pandoc/Writers` | 49 | 10982.02 | 7.21% | 14.95% |
| `src/Text/Pandoc/Readers` | 43 | 5566.0 | 6.34% | 13.95% |
| `src/Text/Pandoc` | 42 | 3023.18 | 5.43% | 8.38% |
| `test/command` | 1080 | 1669.0 | 0.0% | 0.0% |
| `data/translations` | 107 | 1645.48 | 0.0% | 0.0% |
| `src/Text/Pandoc/Writers/Powerpoint` | 2 | 1166.94 | 7.85% | 9.41% |
| `src/Text/Pandoc/Readers/Org` | 9 | 1166.19 | 3.93% | 12.0% |
| `__monolith__` | 15 | 1010.48 | 0.41% | 1.3% |
| `src/Text/Pandoc/Readers/LaTeX` | 8 | 843.18 | 6.84% | 4.54% |
| `src/Text/Pandoc/Citeproc` | 7 | 765.24 | 5.44% | 7.32% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmark/benchmark-pandoc.hs` -> **99.9982%** Exposure
- `src/Text/Pandoc/Chunks.hs` -> **99.98%** Exposure
- `man/manfilter.lua` -> **99.593%** Exposure
- `src/Text/Pandoc/Writers/Muse.hs` -> **99.3489%** Exposure
- `xml-light/Text/Pandoc/XML/Light.hs` -> **98.9463%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `tools/moduledeps.lua` -> **100.0%** Exposure
- `macos/uninstall-pandoc.pl` -> **100.0%** Exposure
- `tools/parseTimings.pl` -> **100.0%** Exposure
- `tools/update-translations.py` -> **100.0%** Exposure
- `tools/validate-docx.sh` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pandoc-lua-engine/test/sample.lua` -> **39** Orphaned Functions | **2** Duplicates
- `src/Text/Pandoc/Writers/Muse.hs` -> **0** Orphaned Functions | **19** Duplicates
- `src/Text/Pandoc/Writers/HTML.hs` -> **10** Orphaned Functions | **8** Duplicates
- `src/Text/Pandoc/Chunks.hs` -> **0** Orphaned Functions | **16** Duplicates
- `src/Text/Pandoc/Readers/Markdown.hs` -> **3** Orphaned Functions | **8** Duplicates

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
- **Unknown Dependencies:** `4971` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Text/Pandoc/Writers/Powerpoint/Output.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.515)
- **Top Global Matches:** file_cluster_15: 7.515, file_cluster_0: 7.873, file_cluster_10: 8.831
- **Magnitude:** 838.02 | **LOC:** 2870 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **58** in-repo importer(s); it depends on **43**; blast radius 6.153; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.7%), Debt Markers (formerly Tech Debt) (9.7%)
- **Documentation Coverage:** 97.8261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `graphicToElement` **(Compute Cores)** (Impact: 32.3)
  * `metadataToElement` **(Many-Argument Workhorses)** (Impact: 31.3)
  * `makePicElements` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `presentationToPresentationElement` **(Compute Cores)** (Impact: 23.7)
  * `getContentType` **(Compute Cores)** (Impact: 22.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 446`, `args: 288`, `func_start: 243`, `class_start: 31`
* *Risk/State:* `state_mutation: 4`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `api: 1`, `import: 46`
* *Defense:* `safety: 56`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.153
  * `Choke Point (Betweenness):` 0.003235 | `Ripple Effect (Closeness):` 0.096626
  * `Imports (Out-Degree: 30):` Codec.Archive.Zip, Control.Applicative, Control.Monad, Control.Monad.Except, Control.Monad.Reader, Control.Monad.State, Data.Bifunctor, Data.ByteString.Lazy...
  * `Imported By (In-Degree: 58):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/HTML.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.975)
- **Top Global Matches:** file_cluster_4: 7.975, file_cluster_15: 8.055, file_cluster_12: 9.23
- **Magnitude:** 783.72 | **LOC:** 1825 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **49**; blast radius 0.682; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.4%), Debt Markers (formerly Tech Debt) (33.9%)
- **Documentation Coverage:** 72.0339% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inlineToHtml` **(Many-Argument Workhorses)** (Impact: 131.2)
    * *Intent:* -- | Convert Pandoc inline element to HTML.
  * `obfuscateLink` **(Many-Argument Workhorses)** (Impact: 124.3)
    * *Intent:* -- | Obfuscate a "mailto:" link.
  * `pandocToHtml` **(Many-Argument Workhorses)** (Impact: 56.8)
    * *Intent:* -- result is (title, authors, date, toc, body, new variables)
  * `footnoteSection` **(Many-Argument Workhorses)** (Impact: 38.7)
    * *Intent:* -- | Convert list of Note blocks to a footnote <div>. -- Assumes notes are sorted.
  * `blockListToNote` **(Many-Argument Workhorses)** (Impact: 26.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 422`, `args: 156`, `func_start: 154`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 21`, `duplicate_logic: 8`, `unreferenced_by_name: 10`
* *Architecture:* `api: 1`, `import: 52`
* *Defense:* `safety: 17`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.682
  * `Choke Point (Betweenness):` 0.000498 | `Ripple Effect (Closeness):` 0.067384
  * `Imports (Out-Degree: 41):` Control.Monad, Control.Monad.Except, Control.Monad.State.Strict, Control.Monad.Trans, Data.Char, Data.Containers.ListUtils, Data.List, Data.List.NonEmpty...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/LaTeX.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.244)
- **Top Global Matches:** file_cluster_4: 8.244, file_cluster_15: 8.553, file_cluster_10: 8.629
- **Magnitude:** 723.92 | **LOC:** 1512 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **36**; blast radius 0.479; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.0%), Mutation Surface (formerly State Flux) (30.5%), Debt Markers (formerly Tech Debt) (28.1%)
- **Documentation Coverage:** 86.7347% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blockToLaTeX` **(Compute Cores)** (Impact: 134.5)
    * *Intent:* -- | Convert Pandoc block element to LaTeX.
  * `inlineToLaTeX` **(Compute Cores)** (Impact: 131.6)
    * *Intent:* -- | Convert inline element to LaTeX
  * `pandocToLaTeX` **(Many-Argument Workhorses)** (Impact: 74.8)
  * `sectionHeader` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* -- | Craft the section header, inserting the section reference, if supplied.
  * `showDim` **(Callbacks & Closures)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 318`, `args: 111`, `func_start: 146`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 37`
* *Defense:* `safety: 13`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.479
  * `Choke Point (Betweenness):` 0.000358 | `Ripple Effect (Closeness):` 0.059156
  * `Imports (Out-Degree: 35):` Control.Applicative, Control.Monad, Control.Monad.State.Strict, Crypto.Hash, Data.Attoparsec.Text, Data.Char, Data.Containers.ListUtils, Data.List...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `changelog.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 587.04 | **LOC:** 29352 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.284; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.284
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foo, url, README.html, Simplify, image.jpg, link, me@bar.baz, pandoc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Text/Pandoc/Writers/EPUB.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.394)
- **Top Global Matches:** file_cluster_15: 6.394, file_cluster_10: 7.937, file_cluster_12: 8.292
- **Magnitude:** 578.0 | **LOC:** 1568 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **41**; blast radius 0.546; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.0%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 92.7835% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pandocToEPUB` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `metadataElement` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `createNavEntry` **(Many-Argument Workhorses)** (Impact: 39.4)
  * `addMetadataFromXML` **(Compute Cores)** (Impact: 39.1)
  * `getEPUBMetadata` **(Defensive Guards)** (Impact: 28.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 228`, `args: 133`, `func_start: 141`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 2`, `import: 42`
* *Defense:* `safety: 21`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.546
  * `Choke Point (Betweenness):` 0.000184 | `Ripple Effect (Closeness):` 0.062129
  * `Imports (Out-Degree: 29):` Codec.Archive.Zip, Control.Applicative, Control.Monad, Control.Monad.Except, Control.Monad.State.Strict, Data.ByteString.Lazy, Data.ByteString.Lazy.Char8, Data.Char...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/Markdown.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.166)
- **Top Global Matches:** file_cluster_15: 8.166, file_cluster_4: 8.273, file_cluster_12: 9.642
- **Magnitude:** 569.26 | **LOC:** 969 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **27**; blast radius 0.738; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.4%), Complexity Load (formerly Cognitive Load) (12.2%)
- **Documentation Coverage:** 61.7647% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blockToMarkdown'` **(Many-Argument Workhorses)** (Impact: 213.9)
  * `pandocToMarkdown` **(Defensive Guards)** (Impact: 35.7)
    * *Intent:* -- | Return markdown representation of document.
  * `definitionListItemToMarkdown` **(Compute Cores)** (Impact: 22.4)
    * *Intent:* -- | Convert definition list item (label, list of blocks) to markdown.
  * `blockListToMarkdown` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* -- | Convert list of Pandoc block elements to markdown.
  * `orderedListItemToMarkdown` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* -- | Convert ordered list item (a list of blocks) to markdown.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 220`, `args: 45`, `func_start: 102`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 28`
* *Defense:* `safety: 9`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.738
  * `Choke Point (Betweenness):` 0.000555 | `Ripple Effect (Closeness):` 0.058768
  * `Imports (Out-Degree: 27):` Control.Monad, Control.Monad.Reader, Control.Monad.State.Strict, Data.Char, Data.Default, Data.List, Data.List.NonEmpty, Data.Map...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/RST.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.279)
- **Top Global Matches:** file_cluster_15: 8.279, file_cluster_4: 8.322, file_cluster_12: 8.816
- **Magnitude:** 565.86 | **LOC:** 991 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 0.78; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.8%), Mutation Surface (formerly State Flux) (13.8%), Debt Markers (formerly Tech Debt) (12.9%)
- **Documentation Coverage:** 77.1739% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blockToRST` **(Compute Cores)** (Impact: 77.1)
    * *Intent:* -- | Convert Pandoc block element to RST.
  * `inlineToRST` **(Compute Cores)** (Impact: 42.7)
    * *Intent:* -- | Convert Pandoc inline element to RST.
  * `escapeText` **(Compute Cores)** (Impact: 41.0)
    * *Intent:* -- | Escape special characters for RST.
  * `simpleTable` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `transformInlines` **(Compute Cores)** (Impact: 23.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 196`, `args: 74`, `func_start: 156`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 10`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.064072
  * `Imports (Out-Degree: 21):` Control.Monad, Control.Monad.State.Strict, Data.Char, Data.List, Data.List.NonEmpty, Data.Maybe, Data.Text, Safe...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/AsciiDoc.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.689)
- **Top Global Matches:** file_cluster_12: 7.689, file_cluster_15: 8.394, file_cluster_4: 8.968
- **Magnitude:** 545.52 | **LOC:** 913 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **24**; blast radius 0.913; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (53.6%), Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (26.4%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blockToAsciiDoc` **(Compute Cores)** (Impact: 127.2)
    * *Intent:* -- | Convert Pandoc block element to asciidoc.
  * `inlineToAsciiDoc` **(Compute Cores)** (Impact: 72.7)
    * *Intent:* -- | Convert Pandoc inline element to asciidoc.
  * `imageArguments` **(Many-Argument Workhorses)** (Impact: 20.8)
    * *Intent:* -- | Provides the arguments for both `image:` and `image::` -- e.g.: sunset.jpg[Sunset,300,200]
  * `escapeString` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* -- | Escape special characters for AsciiDoc.
  * `adjustEmptyRows` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* -- | Adjust empty rows for AsciiDoc. -- -- An empty row without any cells decrements RowSpans that c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 226`, `args: 63`, `func_start: 129`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 20`, `duplicate_logic: 8`
* *Architecture:* `api: 3`, `import: 27`
* *Defense:* `safety: 6`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.069744
  * `Imports (Out-Degree: 25):` Control.Monad, Control.Monad.State.Strict, Data.Char, Data.List, Data.List.NonEmpty, Data.Map, Data.Maybe, Data.Set...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/Docx/Parse.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.18)
- **Top Global Matches:** file_cluster_15: 7.18, file_cluster_10: 7.879, file_cluster_11: 9.007
- **Magnitude:** 533.74 | **LOC:** 1500 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **23**; blast radius 3.099; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.6%), Guard Balance (formerly Safety Score) (47.1%), Connectivity (formerly Api Exposure) (34.7%)
- **Documentation Coverage:** 97.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elemToParPart'` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `elemToBodyPart` **(Defensive Guards)** (Impact: 32.5)
  * `unwrapElement` **(Compute Cores)** (Impact: 20.1)
  * `elemToRunElem` **(Defensive Guards)** (Impact: 19.9)
  * `childElemToRun` **(Defensive Guards)** (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 278`, `args: 151`, `func_start: 126`, `class_start: 49`
* *Risk/State:* `state_mutation: 10`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `import: 24`
* *Defense:* `safety: 42`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.099
  * `Choke Point (Betweenness):` 0.000899 | `Ripple Effect (Closeness):` 0.07595
  * `Imports (Out-Degree: 21):` Codec.Archive.Zip, Control.Applicative, Control.Monad, Control.Monad.Except, Control.Monad.Reader, Control.Monad.State.Strict, Data.Bits, Data.ByteString.Lazy...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/Org/BlockStarts.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.263)
- **Top Global Matches:** file_cluster_0: 5.263, file_cluster_2: 7.966, file_cluster_13: 8.216
- **Magnitude:** 532.69 | **LOC:** 160 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 0.403; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (9.0%), Complexity Load (formerly Cognitive Load) (5.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 18`, `args: 17`, `func_start: 17`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 16`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.403
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.05829
  * `Imports (Out-Degree: 6):` Control.Monad, Data.Functor, Data.Text, Text.Pandoc.Definition, Text.Pandoc.Extensions, Text.Pandoc.Parsing, Text.Pandoc.Readers.LaTeX.Math, Text.Pandoc.Readers.Org.Parsing...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/OpenDocument.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.814)
- **Top Global Matches:** file_cluster_15: 7.814, file_cluster_0: 8.018, file_cluster_10: 8.609
- **Magnitude:** 508.48 | **LOC:** 955 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **28**; blast radius 1.36; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.8%), Mutation Surface (formerly State Flux) (21.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.0%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blockToOpenDocument` **(Compute Cores)** (Impact: 45.5)
    * *Intent:* -- | Convert a Pandoc block element to OpenDocument.
  * `mkLink` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `inlineToOpenDocument` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* -- | Convert an inline element to OpenDocument.
  * `figure` **(Compute Cores)** (Impact: 14.2)
  * `paraStyle` **(Compute Cores)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 164`, `args: 116`, `func_start: 132`, `class_start: 4`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 2`, `import: 31`
* *Defense:* `safety: 4`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.36
  * `Choke Point (Betweenness):` 0.000183 | `Ripple Effect (Closeness):` 0.070222
  * `Imports (Out-Degree: 22):` Control.Arrow, Control.Monad, Control.Monad.State.Strict, Data.Char, Data.Foldable, Data.List, Data.Map, Data.Ord...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Citeproc/BibTeX.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.82)
- **Top Global Matches:** file_cluster_15: 6.82, file_cluster_10: 8.645, file_cluster_16: 8.912
- **Magnitude:** 507.12 | **LOC:** 1374 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **30**; blast radius 0.53; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.5%), Connectivity (formerly Api Exposure) (28.4%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeBibtexString` **(Many-Argument Workhorses)** (Impact: 89.4)
    * *Intent:* -- | Write BibTeX or BibLaTeX given given a 'Reference'.
  * `itemToReference` **(Many-Argument Workhorses)** (Impact: 82.0)
  * `transformKey` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* -- transformKey source target key -- derived from Appendix C of bibtex manual
  * `getContentsFor` **(Compute Cores)** (Impact: 16.3)
  * `getOldDate` **(Defensive Guards)** (Impact: 10.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 168`, `args: 94`, `func_start: 148`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 32`
* *Defense:* `safety: 28`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.53
  * `Choke Point (Betweenness):` 0.000314 | `Ripple Effect (Closeness):` 0.055536
  * `Imports (Out-Degree: 29):` Citeproc.Pandoc, Citeproc.Types, Control.Applicative, Control.Monad, Control.Monad.RWS, Data.Char, Data.Default, Data.List...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/Markdown/Inline.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.817)
- **Top Global Matches:** file_cluster_4: 6.817, file_cluster_15: 9.079, file_cluster_16: 10.175
- **Magnitude:** 503.02 | **LOC:** 738 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.7%), Complexity Load (formerly Cognitive Load) (20.7%)
- **Documentation Coverage:** 80.4878% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inlineToMarkdown` **(Many-Argument Workhorses)** (Impact: 243.1)
    * *Intent:* -- | Convert Pandoc inline element to markdown.
  * `escapeText` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* -- | Escape special characters for Markdown.
  * `go` **(Compute Cores)** (Impact: 23.3)
  * `getReference` **(Defensive Guards)** (Impact: 18.4)
    * *Intent:* -- | Get reference for target; if none exists, create unique one and return. -- Prefer label if poss...
  * `attrsToMarkua` **(Compute Cores)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 167`, `args: 33`, `func_start: 69`
* *Risk/State:* `state_mutation: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 25`
* *Defense:* `safety: 7`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.307
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.045667
  * `Imports (Out-Degree: 26):` Control.Monad, Control.Monad.Reader, Control.Monad.State.Strict, Data.Char, Data.Coerce, Data.List, Data.List.NonEmpty, Data.Map...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/RST.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.501)
- **Top Global Matches:** file_cluster_0: 7.501, file_cluster_15: 8.384, file_cluster_12: 8.958
- **Magnitude:** 478.68 | **LOC:** 1877 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **26**; blast radius 0.464; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (61.1%), Guard Balance (formerly Safety Score) (43.2%), Connectivity (formerly Api Exposure) (15.7%)
- **Documentation Coverage:** 91.9643% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `csvTableDirective` **(Defensive Guards)** (Impact: 33.5)
  * `resolveReferences` **(Defensive Guards)** (Impact: 21.2)
  * `unicodeTransform` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* -- Can contain character codes as decimal numbers or -- hexadecimal numbers, prefixed by 0x, x, \x, ...
  * `listTableDirective` **(Defensive Guards)** (Impact: 15.7)
    * *Intent:* -- TODO: :stub-columns:. -- Only the first row becomes the header even if header-rows: > 1, -- since...
  * `addNewRole` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* -- TODO: -- - Only supports :format: fields with a single format for :raw: roles, -- change Text.Pan...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 370`, `args: 182`, `func_start: 220`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `planned_debt: 9`, `duplicate_logic: 10`
* *Architecture:* `api: 3`, `import: 28`
* *Defense:* `safety: 111`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.464
  * `Choke Point (Betweenness):` 0.000205 | `Ripple Effect (Closeness):` 0.063336
  * `Imports (Out-Degree: 41):` Control.Arrow, Control.Monad, Control.Monad.Except, Control.Monad.Identity, Data.Char, Data.List, Data.Map, Data.Maybe...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/LaTeX/Parsing.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.174)
- **Top Global Matches:** file_cluster_0: 8.174, file_cluster_12: 8.353, file_cluster_5: 9.285
- **Magnitude:** 446.32 | **LOC:** 1183 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **22**; blast radius 0.932; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.8%), Guard Balance (formerly Safety Score) (47.3%), Debt Markers (formerly Tech Debt) (18.2%)
- **Documentation Coverage:** 99.3197% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `totoks` **(Many-Argument Workhorses)** (Impact: 55.1)
  * `tokenize` **(Compute Cores)** (Impact: 48.6)
  * `doMacros'` **(Defensive Guards)** (Impact: 21.7)
  * `rawLaTeXParser` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `handleMacros` **(Many-Argument Workhorses)** (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 203`, `args: 157`, `func_start: 156`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `duplicate_logic: 4`
* *Architecture:* `api: 27`, `import: 24`
* *Defense:* `safety: 43`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.932
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.061019
  * `Imports (Out-Degree: 23):` Control.Applicative, Control.Monad, Control.Monad.Except, Control.Monad.Trans, Data.Char, Data.Default, Data.IntMap, Data.List...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/Shared.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.079)
- **Top Global Matches:** file_cluster_15: 6.079, file_cluster_10: 7.51, file_cluster_11: 7.661
- **Magnitude:** 431.56 | **LOC:** 929 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **28**; blast radius 17.507; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (89.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.9%), Debt Markers (formerly Tech Debt) (22.3%)
- **Documentation Coverage:** 48.2014% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rowAndBottom` **(Compute Cores)** (Impact: 18.9)
  * `gridRows` **(Compute Cores)** (Impact: 17.6)
  * `toLegacyTable` **(Many-Argument Workhorses)** (Impact: 15.1)
    * *Intent:* -- | Convert the relevant components of a new-style table (with block -- caption, row headers, row a...
  * `formatBorder` **(Compute Cores)** (Impact: 13.4)
  * `splitSentences` **(Compute Cores)** (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 100`, `args: 84`, `func_start: 139`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 32`, `import: 30`
* *Defense:* `safety: 5`, `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.507
  * `Choke Point (Betweenness):` 0.002851 | `Ripple Effect (Closeness):` 0.101554
  * `Imports (Out-Degree: 27):` Control.Monad, Data.Aeson, Data.ByteString.Lazy, Data.Char, Data.Either, Data.List, Data.List.NonEmpty, Data.Map...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/JATS.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.359)
- **Top Global Matches:** file_cluster_0: 8.359, file_cluster_15: 8.479, file_cluster_10: 9.179
- **Magnitude:** 417.54 | **LOC:** 785 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **24**; blast radius 0.404; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (45.0%), Mutation Surface (formerly State Flux) (13.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseBlock` **(Defensive Guards)** (Impact: 66.7)
  * `parseMixed` **(Defensive Guards)** (Impact: 58.8)
  * `wrapWithHeader` **(Defensive Guards)** (Impact: 25.6)
  * `parseInline` **(Compute Cores)** (Impact: 23.7)
  * `isBlockElement` **(Compute Cores)** (Impact: 16.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 222`, `args: 67`, `func_start: 82`, `class_start: 2`
* *Risk/State:* `state_mutation: 10`, `planned_debt: 1`
* *Architecture:* `api: 2`, `import: 26`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.404
  * `Choke Point (Betweenness):` 0.000205 | `Ripple Effect (Closeness):` 0.051396
  * `Imports (Out-Degree: 36):` Control.Monad, Control.Monad.Except, Control.Monad.State.Strict, Data.Char, Data.Default, Data.Generics, Data.List, Data.Map...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/Docx/OpenXML.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.41)
- **Top Global Matches:** file_cluster_10: 8.41, file_cluster_15: 8.536, file_cluster_0: 8.548
- **Magnitude:** 417.44 | **LOC:** 1141 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **42**; blast radius 2.106; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.3%), Mutation Surface (formerly State Flux) (21.5%), Complexity Load (formerly Cognitive Load) (11.3%)
- **Documentation Coverage:** 84.507% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blockToOpenXML'` **(Many-Argument Workhorses)** (Impact: 86.2)
  * `inlineToOpenXML'` **(Many-Argument Workhorses)** (Impact: 67.0)
  * `writeOpenXML` **(Compute Cores)** (Impact: 20.2)
    * *Intent:* -- | Convert Pandoc document to rendered document contents plus two lists of -- OpenXML elements (fo...
  * `listItemToOpenXML` **(Callbacks & Closures)** (Impact: 11.1)
  * `generateImgElt` **(I/O & Config Routines)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 206`, `args: 102`, `func_start: 82`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 1`, `import: 44`
* *Defense:* `safety: 20`, `doc: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.106
  * `Choke Point (Betweenness):` 0.001392 | `Ripple Effect (Closeness):` 0.081752
  * `Imports (Out-Degree: 34):` Control.Applicative, Control.Monad, Control.Monad.Except, Control.Monad.Reader, Control.Monad.State, Crypto.Hash, Data.ByteString.Lazy, Data.Char...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/Docx.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.562)
- **Top Global Matches:** file_cluster_15: 8.562, file_cluster_0: 8.625, file_cluster_10: 8.835
- **Magnitude:** 395.7 | **LOC:** 920 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **34**; blast radius 1.022; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.0%), Connectivity (formerly Api Exposure) (30.4%), Mutation Surface (formerly State Flux) (26.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyPartToBlocks` **(Compute Cores)** (Impact: 46.5)
  * `parPartToInlines'` **(Compute Cores)** (Impact: 33.7)
  * `runStyleToTransform` **(Compute Cores)** (Impact: 24.6)
  * `go` **(Compute Cores)** (Impact: 21.2)
  * `parStyleToTransform` **(Compute Cores)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 170`, `args: 100`, `func_start: 110`, `class_start: 3`
* *Risk/State:* `state_mutation: 18`, `duplicate_logic: 4`
* *Architecture:* `api: 7`, `import: 38`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.022
  * `Choke Point (Betweenness):` 0.000758 | `Ripple Effect (Closeness):` 0.068283
  * `Imports (Out-Degree: 32):` Citeproc, Codec.Archive.Zip, Control.Monad, Control.Monad.Except, Control.Monad.Reader, Control.Monad.State.Strict, Data.Aeson, Data.Bifunctor...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Shared.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.508)
- **Top Global Matches:** file_cluster_15: 6.508, file_cluster_12: 7.437, file_cluster_10: 7.979
- **Magnitude:** 395.52 | **LOC:** 853 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **130** in-repo importer(s); it depends on **29**; blast radius 18.407; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.7%)
- **Documentation Coverage:** 36.1842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeSectionsWithOffsets` **(Many-Argument Workhorses)** (Impact: 29.8)
    * *Intent:* -- | Like 'makeSections', but with a parameter for number offsets -- (a list of 'Int's, the first of...
  * `toRomanNumeral` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* -- | Convert number < 4000 to uppercase roman numeral.
  * `textToIdentifier` **(Compute Cores)** (Impact: 20.2)
    * *Intent:* -- | Convert string to plain text identifier.
  * `go` **(Compute Cores)** (Impact: 16.6)
  * `uniqueIdent` **(Callbacks & Closures)** (Impact: 8.6)
    * *Intent:* -- | Generate a unique identifier from a list of inlines. -- Second argument is a list of already us...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 81`, `args: 86`, `func_start: 168`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`
* *Architecture:* `io: 2`, `api: 37`, `import: 31`
* *Defense:* `safety: 1`, `doc: 55`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.407
  * `Choke Point (Betweenness):` 0.004057 | `Ripple Effect (Closeness):` 0.114715
  * `Imports (Out-Degree: 20):` Codec.Archive.Zip, Commonmark, Commonmark.Pandoc, Control.Exception, Control.Monad, Control.Monad.State.Strict, Data.ByteString.Lazy, Data.Char...
  * `Imported By (In-Degree: 130):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/Muse.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.663)
- **Top Global Matches:** file_cluster_12: 7.663, file_cluster_10: 9.732, file_cluster_5: 9.951
- **Magnitude:** 382.22 | **LOC:** 733 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **22**; blast radius 0.493; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.1%), Mutation Surface (formerly State Flux) (30.7%)
- **Documentation Coverage:** 77.5281% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inlineToMuse` **(Callbacks & Closures)** (Impact: 65.7)
    * *Intent:* -- | Convert Pandoc inline element to Muse.
  * `blockToMuse` **(Callbacks & Closures)** (Impact: 24.6)
    * *Intent:* -- | Convert Pandoc block element to Muse.
  * `simpleTable` **(Compute Cores)** (Impact: 19.2)
  * `fixOrEscape` **(Compute Cores)** (Impact: 16.6)
  * `fixOrEscapeStr` **(Compute Cores)** (Impact: 16.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 149`, `args: 100`, `func_start: 98`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 25`, `duplicate_logic: 19`
* *Architecture:* `api: 2`, `import: 23`
* *Defense:* `safety: 1`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.493
  * `Choke Point (Betweenness):` 0.000101 | `Ripple Effect (Closeness):` 0.056277
  * `Imports (Out-Degree: 20):` Control.Monad, Control.Monad.Except, Control.Monad.Reader, Control.Monad.State.Strict, Data.Char, Data.Default, Data.List, Data.List.NonEmpty...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/ConTeXt.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.837)
- **Top Global Matches:** file_cluster_4: 7.837, file_cluster_15: 7.922, file_cluster_12: 8.259
- **Magnitude:** 362.4 | **LOC:** 840 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **25**; blast radius 0.409; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.3%), Connectivity (formerly Api Exposure) (17.6%), Mutation Surface (formerly State Flux) (10.9%)
- **Documentation Coverage:** 72.4138% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blockToConTeXt` **(Compute Cores)** (Impact: 49.2)
    * *Intent:* -- | Convert Pandoc block element to ConTeXt.
  * `inlineToConTeXt` **(Compute Cores)** (Impact: 41.4)
    * *Intent:* -- | Convert inline element to ConTeXt
  * `tableCellToConTeXt` **(Compute Cores)** (Impact: 23.9)
  * `sectionLevelToText` **(Many-Argument Workhorses)** (Impact: 19.2)
    * *Intent:* -- | Generate a textual representation of the section level
  * `pandocToConTeXt` **(Compute Cores)** (Impact: 18.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 198`, `args: 63`, `func_start: 64`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`
* *Architecture:* `api: 3`, `import: 27`
* *Defense:* `safety: 6`, `doc: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.05796
  * `Imports (Out-Degree: 23):` Control.Monad, Control.Monad.State.Strict, Data.Char, Data.List, Data.List.NonEmpty, Data.Map.Strict, Data.Maybe, Data.Monoid...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/ICML.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.464)
- **Top Global Matches:** file_cluster_15: 6.464, file_cluster_0: 7.93, file_cluster_11: 8.312
- **Magnitude:** 361.14 | **LOC:** 695 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.355; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.8%), Connectivity (formerly Api Exposure) (22.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.2%)
- **Documentation Coverage:** 27.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blockToICML` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* -- | Convert a Pandoc block element to ICML.
  * `countSubStrs` **(Compute Cores)** (Impact: 27.2)
  * `imageICML` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* -- | Assemble an ICML Image.
  * `parStylesToDoc` **(Compute Cores)** (Impact: 23.0)
    * *Intent:* -- | Convert a WriterState with its block styles to the ICML listing of Paragraph Styles.
  * `makeStyle` **(Compute Cores)** (Impact: 22.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 136`, `args: 81`, `func_start: 107`, `class_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 4`, `import: 20`
* *Defense:* `safety: 6`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.355
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.058337
  * `Imports (Out-Degree: 18):` Control.Monad, Control.Monad.Except, Control.Monad.State.Strict, Data.List, Data.Maybe, Data.Set, Data.Text, Text.DocLayout...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Readers/DocBook.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.905)
- **Top Global Matches:** file_cluster_15: 7.905, file_cluster_10: 8.659, file_cluster_11: 9.217
- **Magnitude:** 361.04 | **LOC:** 1503 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.314; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.4%), Mutation Surface (formerly State Flux) (14.5%)
- **Documentation Coverage:** 94.2029% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseBlock` **(Defensive Guards)** (Impact: 72.9)
  * `parseInline` **(Compute Cores)** (Impact: 48.3)
  * `getMediaobject` **(Defensive Guards)** (Impact: 12.9)
    * *Intent:* -- function that is used by both mediaobject (in parseBlock) -- and inlinemediaobject (in parseInlin...
  * `addMetadataFromElement` **(Compute Cores)** (Impact: 12.5)
    * *Intent:* --
  * `parseEntry` **(Compute Cores)** (Impact: 10.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 213`, `args: 73`, `func_start: 125`, `class_start: 2`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 2`, `import: 35`
* *Defense:* `safety: 21`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.314
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.050993
  * `Imports (Out-Degree: 32):` Control.Applicative, Control.Monad, Control.Monad.Except, Control.Monad.State.Strict, Data.ByteString, Data.Char, Data.Default, Data.Either...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Text/Pandoc/Writers/Typst.hs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.975)
- **Top Global Matches:** file_cluster_4: 6.975, file_cluster_15: 8.328, file_cluster_11: 9.783
- **Magnitude:** 355.56 | **LOC:** 726 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 0.332; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.6%), Debt Markers (formerly Tech Debt) (14.9%)
- **Documentation Coverage:** 94.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blockToTypst` **(Compute Cores)** (Impact: 59.1)
  * `inlineToTypst` **(Compute Cores)** (Impact: 43.5)
  * `escapeTypst` **(Compute Cores)** (Impact: 38.5)
  * `pandocToTypst` **(Compute Cores)** (Impact: 27.3)
  * `mkImage` **(Many-Argument Workhorses)** (Impact: 23.5)
    * *Intent:* -- see #9104; need box or image is treated as block-level
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 170`, `args: 44`, `func_start: 92`, `class_start: 4`
* *Risk/State:* `state_mutation: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 30`
* *Defense:* `safety: 9`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.332
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.051139
  * `Imports (Out-Degree: 28):` Control.Monad, Control.Monad.State, Data.Bifunctor, Data.ByteString, Data.Char, Data.List, Data.Maybe, Data.Text...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Text/Pandoc/Filter.hs` (HASKELL) | Magnitude: 32.16 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 26, import: 16, func_start: 14
- `pandoc-lua-engine/src/Text/Pandoc/Lua/Module/JSON.hs` (HASKELL) | Magnitude: 157.3 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 13, import: 13, serialization_parsing: 12
- `src/Text/Pandoc/Readers/JATS.hs` (HASKELL) | Magnitude: 417.54 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 574, structural_boundaries: 222, core_var_decl: 178, design_snake_case: 115
- `src/Text/Pandoc/Writers.hs` (HASKELL) | Magnitude: 10.4 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 159, import: 52, core_var_decl: 8, structural_boundaries: 6
- `src/Text/Pandoc/Translations.hs` (HASKELL) | Magnitude: 18.8 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 20, core_var_decl: 14, import: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `pandoc-lua-engine/src/Text/Pandoc/Lua/Writer/Scaffolding.hs` (HASKELL) | Magnitude: 83.5 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 169, core_var_decl: 55, structural_boundaries: 44, args: 42
- `src/Text/Pandoc/Writers/Docx/OpenXML.hs` (HASKELL) | Magnitude: 417.44 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 829, structural_boundaries: 206, core_var_decl: 168, branch: 109

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/Text/Pandoc/Highlighting.hs` (HASKELL) | Magnitude: 42.86 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 219, core_var_decl: 24, design_camel_case: 18, func_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/Tests/Readers/Org/Shared.hs` (HASKELL) | Magnitude: 9.78 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 7, indent_spaces: 7, args: 4, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Text/Pandoc/App/CommandLineOptions.hs` (HASKELL) | Magnitude: 285.72 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 1004, structural_boundaries: 170, core_var_decl: 157, args: 142
- `src/Text/Pandoc/Writers/RST.hs` (HASKELL) | Magnitude: 565.86 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 694, structural_boundaries: 196, core_var_decl: 191, branch: 157
- `pandoc-cli/src/pandoc.hs` (HASKELL) | Magnitude: 15.08 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 33, macros: 14, import: 12, structural_boundaries: 11
- `src/Text/Pandoc/Readers/Pptx/Shapes.hs` (HASKELL) | Magnitude: 135.66 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 188, structural_boundaries: 78, core_var_decl: 55, branch: 46
- `src/Text/Pandoc/Readers/Docx.hs` (HASKELL) | Magnitude: 395.7 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 546, core_var_decl: 199, structural_boundaries: 170, func_start: 110

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/Tests/Writers/HTML.hs` (HASKELL) | Magnitude: 16.76 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 43, core_var_decl: 39, design_snake_case: 31
- `test/Tests/Readers/Txt2Tags.hs` (HASKELL) | Magnitude: 20.98 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 366, structural_boundaries: 21, core_var_decl: 14, import: 9
- `pandoc-lua-engine/src/Text/Pandoc/Lua/Module/Log.hs` (HASKELL) | Magnitude: 56.79 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 49, import: 11, structural_boundaries: 9, args: 5
- `test/Tests/MediaBag.hs` (HASKELL) | Magnitude: 34.18 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 16, import: 9, core_var_decl: 3
- `xml-light/Text/Pandoc/XML/Light/Proc.hs` (HASKELL) | Magnitude: 50.78 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, core_var_decl: 21, args: 20, func_start: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Text/Pandoc/Writers/HTML.hs` (HASKELL) | Magnitude: 783.72 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1408, structural_boundaries: 422, branch: 292, core_var_decl: 251
- `src/Text/Pandoc/Writers/ConTeXt.hs` (HASKELL) | Magnitude: 362.4 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 591, structural_boundaries: 198, core_var_decl: 121, branch: 108
- `src/Text/Pandoc/SelfContained.hs` (HASKELL) | Magnitude: 176.32 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 314, structural_boundaries: 118, branch: 62, core_var_decl: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tools/update-translations.py` (PYTHON) | Magnitude: 0.28 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 266, branch: 82, structural_boundaries: 67, core_var_decl: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `benchmark/benchmark-pandoc.hs` (HASKELL) | Magnitude: 23.84 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, core_var_decl: 14, structural_boundaries: 12, import: 12
- `pandoc-lua-engine/test/Tests/Lua/Reader.hs` (HASKELL) | Magnitude: 2.58 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: import: 12, indent_spaces: 9, structural_boundaries: 4, args: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/ci.yml` -> Churn: **73.39%** | Cog Load: 0.0% | Debt: 75.458%
- `.github/workflows/nightly.yml` -> Churn: **57.82%** | Cog Load: 3.552% | Debt: 95.7628%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Text/Pandoc/Writers/Markdown.hs` -> **John MacFarlane** (100.0% isolated ownership) | Magnitude: 569.26
- `src/Text/Pandoc/Writers/RST.hs` -> **John MacFarlane** (100.0% isolated ownership) | Magnitude: 565.86
- `src/Text/Pandoc/Citeproc/BibTeX.hs` -> **John MacFarlane** (100.0% isolated ownership) | Magnitude: 507.12
- `src/Text/Pandoc/Writers/Markdown/Inline.hs` -> **John MacFarlane** (100.0% isolated ownership) | Magnitude: 503.02
- `src/Text/Pandoc/Readers/RST.hs` -> **John MacFarlane** (100.0% isolated ownership) | Magnitude: 478.68

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Text/Pandoc/Shared.hs` -> **Severity: 0.036** (Bridge: 0.0041 * Flux: 8.8391%)
- `src/Text/Pandoc/Writers/Docx/OpenXML.hs` -> **Severity: 0.03** (Bridge: 0.0014 * Flux: 21.5298%)
- `src/Text/Pandoc/Writers/Powerpoint/Output.hs` -> **Severity: 0.029** (Bridge: 0.0032 * Flux: 8.8397%)
- `src/Text/Pandoc/Writers/Jira.hs` -> **Severity: 0.022** (Bridge: 0.0015 * Flux: 14.259%)
- `src/Text/Pandoc/Readers/Docx.hs` -> **Severity: 0.02** (Bridge: 0.0008 * Flux: 26.6328%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Text/Pandoc/Error.hs` -> **Severity: 6.447** (Embedded: 0.1147 * Error Risk: 56.1991%)
- `src/Text/Pandoc/Shared.hs` -> **Severity: 5.708** (Embedded: 0.1147 * Error Risk: 49.7585%)
- `src/Text/Pandoc/Writers/Shared.hs` -> **Severity: 4.97** (Embedded: 0.1016 * Error Risk: 48.9432%)
- `src/Text/Pandoc/Sources.hs` -> **Severity: 4.892** (Embedded: 0.0972 * Error Risk: 50.355%)
- `src/Text/Pandoc/Writers/Powerpoint/Output.hs` -> **Severity: 4.61** (Embedded: 0.0966 * Error Risk: 47.705%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Text/Pandoc/Error.hs` -> **Severity: 1745.34** (Blast Radius: 29.089 * Doc Risk: 60.0%)
- `src/Text/Pandoc/Readers/Man.hs` -> **Severity: 1574.65** (Blast Radius: 16.554 * Doc Risk: 95.122%)
- `test/Tests/Readers/Org/Block/List.hs` -> **Severity: 1209.2** (Blast Radius: 12.092 * Doc Risk: 100.0%)
- `src/Text/Pandoc/UTF8.hs` -> **Severity: 1050.75** (Blast Radius: 14.01 * Doc Risk: 75.0%)
- `src/Text/Pandoc/Char.hs` -> **Severity: 1008.2** (Blast Radius: 10.082 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 174 literal sites + 6 sites through wrappers = 180
- **`panics_and_aborts`:** 133 literal sites + 1 sites through wrappers = 134

- `codeWith` (function, debug_prints, primitive): 5 call sites in 3 files -- `test/Tests/Writers/JATS.hs`
- `prind` (function, debug_prints, primitive): 1 call sites in 1 files -- `tools/moduledeps.lua`
- `withForkWait` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/Text/Pandoc/Process.hs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 32698 call pairs -- scoped 28.8%, unique 11.9%, ambiguous 6.7%, external 52.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| haskell | 31123 | 30.1% | 12.5% | 7.0% | 50.3% |
| lua | 1333 | 3.2% | 0.8% | 0.6% | 95.4% |
| python | 87 | 13.8% | 0.0% | 0.0% | 86.2% |
| shell | 78 | 3.8% | 0.0% | 0.0% | 96.2% |
| html | 77 | 0.0% | 0.0% | 0.0% | 100.0% |

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
