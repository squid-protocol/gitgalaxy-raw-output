# ARCHITECTURAL_BRIEF: docutils
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/docutils` |
| **Timestamp** | `2026-08-07T05:22:20.340865+00:00` |
| **Scan Duration** | `1.01s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 145 malicious artifacts.

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
| Total Artifacts | 263 |
| Analyzed Artifacts (Scanned) | 205 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 58 |
| Total LOC | 33314 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6071 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2979 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5978 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 143 | 30366 | 69.8% |
| PLAINTEXT | 36 | 0 | 17.6% |
| CSS | 24 | 2418 | 11.7% |
| JAVASCRIPT | 1 | 513 | 0.5% |
| MAKEFILE | 1 | 17 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.871`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 110 | 53.7% |
| file_cluster_13 | 49 | 23.9% |
| file_cluster_16 | 9 | 4.4% |
| file_cluster_11 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 36 | 17.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 58*

**Composition by Extension & Reason:**
- `.el`: 24x Excluded (Unsupported Extension: '.el')
- `.rst`: 15x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 4x Unsupported Format (.undeterminable)
- `.tex`: 4x Excluded (Unsupported Extension: '.tex')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 365 LOC), 1x Excluded (Machine-Generated Source Code Signature: 192 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 2x Excluded (Unsupported Extension: '.conf')
- `.sty`: 1x Excluded (Unsupported Extension: '.sty')
- `.odt`: 1x Excluded (Explicitly Denied Extension: '.odt')
- `.txt`: 1x Excluded (Machine-Generated Source Code Signature: 26 LOC)
- `.css`: 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 91.9 | 9.5 | 5.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 96.1 | 35.2 | 42.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.7 | 2.3 | 2.3 |
| API Exposure | 0.0 | 13.1 | 2.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 15.6 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.4 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 94.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.8 | 24.7 | 11.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `docutils-0.22.4/docutils/utils/_roman_numerals.py` (Hits: 26)
- `docutils-0.22.4/docutils/writers/s5_html/__init__.py` (Hits: 22)
- `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.py** (`docutils-0.22.4/docutils/core.py`) — 13 inbound connections
2. **nodes.py** (`docutils-0.22.4/docutils/nodes.py`) — 9 inbound connections
3. **io.py** (`docutils-0.22.4/docutils/io.py`) — 6 inbound connections
4. **_typing.py** (`docutils-0.22.4/docutils/utils/_typing.py`) — 5 inbound connections
5. **math.css** (`docutils-0.22.4/docutils/writers/html5_polyglot/math.css`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`docutils-0.22.4/docutils/writers/odf_odt/__init__.py`) — 27 outbound dependencies
2. **nodes.py** (`docutils-0.22.4/docutils/nodes.py`) — 18 outbound dependencies
3. **buildhtml.py** (`docutils-0.22.4/tools/buildhtml.py`) — 17 outbound dependencies
4. **__init__.py** (`docutils-0.22.4/docutils/utils/__init__.py`) — 16 outbound dependencies
5. **_html_base.py** (`docutils-0.22.4/docutils/writers/_html_base.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` (@ `docutils-0.22.4/docutils/writers/odf_odt/__init__.py`) -> Impact: **575.5** | LOC: 1915
- `checkskip` (@ `docutils-0.22.4/docutils/utils/math/math2html.py`) -> Impact: **445.1** | LOC: 1351
- `endtag` (@ `docutils-0.22.4/docutils/nodes.py`) -> Impact: **358.6** | LOC: 1179
- `no_match` (@ `docutils-0.22.4/docutils/parsers/rst/states.py`) -> Impact: **325.1** | LOC: 661
- `process` (@ `docutils-0.22.4/docutils/frontend.py`) -> Impact: **276.9** | LOC: 511
- `get_state` (@ `docutils-0.22.4/docutils/statemachine.py`) -> Impact: **262.2** | LOC: 775
  * *Intent:* """Offset of `self.input_lines` from the beginning of the file."""
- `substitution_def` (@ `docutils-0.22.4/docutils/parsers/rst/states.py`) -> Impact: **225.2** | LOC: 382
- `extract_options` (@ `docutils-0.22.4/docutils/utils/__init__.py`) -> Impact: **218.6** | LOC: 392
- `parsebit` (@ `docutils-0.22.4/docutils/utils/math/math2html.py`) -> Impact: **215.7** | LOC: 503
- `symbolize_footnotes` (@ `docutils-0.22.4/docutils/transforms/references.py`) -> Impact: **164.2** | LOC: 374

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `docutils-0.22.4/docutils` | 8 | 3401.62 | 17.42% | 28.34% |
| `docutils-0.22.4/docutils/writers/html5_polyglot` | 8 | 3183.15 | 10.65% | 20.43% |
| `docutils-0.22.4/docutils/utils/math` | 8 | 2451.48 | 15.22% | 26.28% |
| `docutils-0.22.4/docutils/parsers/rst` | 4 | 2049.16 | 18.94% | 21.16% |
| `docutils-0.22.4/docutils/writers/odf_odt` | 3 | 1745.12 | 16.09% | 36.54% |
| `docutils-0.22.4/docutils/transforms` | 8 | 1167.22 | 22.01% | 79.2% |
| `docutils-0.22.4/docutils/parsers/rst/directives` | 9 | 1080.1 | 11.21% | 34.99% |
| `docutils-0.22.4/docutils/writers` | 5 | 1012.24 | 15.45% | 81.65% |
| `docutils-0.22.4/docutils/utils` | 7 | 833.35 | 17.04% | 28.18% |
| `docutils-0.22.4/docutils/writers/html4css1` | 3 | 812.59 | 26.28% | 32.93% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `docutils-0.22.4/docutils/parsers/rst/languages/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/transforms/components.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/null.py` -> **99.9999%** Exposure
- `docutils-0.22.4/docutils/writers/null.py` -> **99.9999%** Exposure
### Highest State Flux (Mutation/Volatility)
- `docutils-0.22.4/docutils/utils/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/utils/code_analyzer.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/utils/math/latex2mathml.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/utils/math/math2html.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/utils/math/mathml_elements.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `docutils-0.22.4/docutils/utils/math/math2html.py` -> **8** Orphaned Functions | **41** Duplicates
- `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` -> **1** Orphaned Functions | **33** Duplicates
- `docutils-0.22.4/docutils/writers/html4css1/__init__.py` -> **25** Orphaned Functions | **2** Duplicates
- `docutils-0.22.4/docutils/writers/manpage.py` -> **23** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/docutils/io.py` -> **0** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`docutils-0.22.4/docutils/core.py`** -> AI Confidence: **99.31%**
2. **`docutils-0.22.4/docutils/frontend.py`** -> AI Confidence: **99.31%**
3. **`docutils-0.22.4/docutils/io.py`** -> AI Confidence: **99.31%**
4. **`docutils-0.22.4/docutils/parsers/recommonmark_wrapper.py`** -> AI Confidence: **99.31%**
5. **`docutils-0.22.4/docutils/parsers/rst/directives/images.py`** -> AI Confidence: **99.31%**
6. **`docutils-0.22.4/docutils/parsers/rst/directives/misc.py`** -> AI Confidence: **99.31%**
7. **`docutils-0.22.4/docutils/parsers/rst/directives/tables.py`** -> AI Confidence: **99.31%**
8. **`docutils-0.22.4/docutils/parsers/rst/states.py`** -> AI Confidence: **99.31%**
9. **`docutils-0.22.4/docutils/utils/smartquotes.py`** -> AI Confidence: **99.31%**
10. **`docutils-0.22.4/docutils/writers/latex2e/__init__.py`** -> AI Confidence: **99.31%**
11. **`docutils-0.22.4/docutils/writers/odf_odt/prepstyles.py`** -> AI Confidence: **99.31%**
12. **`docutils-0.22.4/docutils/writers/s5_html/__init__.py`** -> AI Confidence: **99.31%**
13. **`docutils-0.22.4/docutils/utils/__init__.py`** -> AI Confidence: **99.24%**
14. **`docutils-0.22.4/docutils/writers/odf_odt/__init__.py`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `456` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `docutils-0.22.4/docutils/writers/html4css1/__init__.py` (PYTHON) -> Cumulative Risk: **711.44**
- **Archetype:** `file_cluster_11` (Distance: 13.693 IQR)
- **Magnitude:** 810.6 | **LOC:** 965 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.7845%), Documentation (95.6325%)
- **Heaviest Functions:** `visit_footnote_reference` (Impact: 67.2), `visit_entry` (Impact: 46.6), `should_be_compact_paragraph` (Impact: 29.2)

### 2. `docutils-0.22.4/docutils/writers/manpage.py` (PYTHON) -> Cumulative Risk: **690.09**
- **Archetype:** `file_cluster_16` (Distance: 13.221 IQR)
- **Magnitude:** 876.94 | **LOC:** 1354 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.8169%), Tech Debt (96.1648%)
- **Heaviest Functions:** `comment_begin` (Impact: 81.4), `visit_option_argument` (Impact: 79.8), `visit_citation` (Impact: 43.2)

### 3. `docutils-0.22.4/docutils/utils/math/math2html.py` (PYTHON) -> Cumulative Risk: **652.33**
- **Archetype:** `file_cluster_8` (Distance: 11.6 IQR)
- **Magnitude:** 1850.58 | **LOC:** 3167 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.7933%), Documentation (96.5557%)
- **Heaviest Functions:** `checkskip` (Impact: 445.1), `parsebit` (Impact: 215.7), `readoption` (Impact: 27.9)

### 4. `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` (JAVASCRIPT) -> Cumulative Risk: **651.2**
- **Archetype:** `file_cluster_8` (Distance: 12.146 IQR)
- **Magnitude:** 790.56 | **LOC:** 559 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (96.0975%)
- **Heaviest Functions:** `keys` (Impact: 82.8), `toggle` (Impact: 46.7), `go` (Impact: 35.0)

### 5. `docutils-0.22.4/docutils/transforms/parts.py` (PYTHON) -> Cumulative Risk: **620.86**
- **Archetype:** `file_cluster_13` (Distance: 12.326 IQR)
- **Magnitude:** 135.14 | **LOC:** 176 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Tech Debt (99.9881%), Verification (80.0%)
- **Heaviest Functions:** `build_contents` (Impact: 25.6), `apply` (Impact: 18.6), `update_section_numbers` (Impact: 13.0)

### 6. `docutils-0.22.4/docutils/utils/math/mathml_elements.py` (PYTHON) -> Cumulative Risk: **588.87**
- **Archetype:** `file_cluster_13` (Distance: 13.288 IQR)
- **Magnitude:** 208.02 | **LOC:** 483 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.956%), Verification (80.0%)
- **Heaviest Functions:** `__setitem__` (Impact: 14.6), `__repr__` (Impact: 12.7), `append` (Impact: 9.4)

### 7. `docutils-0.22.4/docutils/parsers/rst/directives/images.py` (PYTHON) -> Cumulative Risk: **542.12**
- **Archetype:** `file_cluster_13` (Distance: 10.332 IQR)
- **Magnitude:** 101.22 | **LOC:** 187 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9781%), State Flux (80.6685%), Verification (80.0%)
- **Heaviest Functions:** `run` (Impact: 37.5), `run` (Impact: 26.6), `figwidth_value` (Impact: 5.4)

### 8. `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (PYTHON) -> Cumulative Risk: **541.85**
- **Archetype:** `file_cluster_8` (Distance: 11.917 IQR)
- **Magnitude:** 1657.2 | **LOC:** 3462 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (92.027%), Documentation (90.8433%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 575.5), `visit_reference` (Impact: 22.2), `visit_title` (Impact: 21.2)

### 9. `docutils-0.22.4/docutils/io.py` (PYTHON) -> Cumulative Risk: **532.02**
- **Archetype:** `file_cluster_13` (Distance: 13.235 IQR)
- **Magnitude:** 257.4 | **LOC:** 717 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9987%), State Flux (99.1846%), Verification (80.0%)
- **Heaviest Functions:** `__repr__` (Impact: 55.2), `write` (Impact: 22.5), `write` (Impact: 13.5)

### 10. `docutils-0.22.4/docutils/utils/__init__.py` (PYTHON) -> Cumulative Risk: **529.69**
- **Archetype:** `file_cluster_13` (Distance: 12.638 IQR)
- **Magnitude:** 417.34 | **LOC:** 851 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Verification (80.0%), Safety Score (66.6803%)
- **Heaviest Functions:** `extract_options` (Impact: 218.6), `system_message` (Impact: 44.0), `__init__` (Impact: 11.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `docutils-0.22.4/docutils/writers/html5_polyglot/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.212 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.555 IQR)
- **Top Global Matches:** file_cluster_16: 12.212, file_cluster_8: 12.326, file_cluster_13: 12.385
- **Magnitude:** 3175.15 | **LOC:** 399 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.9858%), Tech Debt (10.6381%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 63`, `args: 37`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 101`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 37`, `import: 4`
* *Defense:* `safety: 11`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pathlib, __future__, docutils, docutils.writers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/math/math2html.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.6 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.625 IQR)
- **Top Global Matches:** file_cluster_8: 11.6, file_cluster_16: 11.773, file_cluster_11: 11.986
- **Magnitude:** 1850.58 | **LOC:** 3167 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.1055%), Tech Debt (98.7933%)
**Top Internal Functions/Classes:**
  * `checkskip` (Impact: 445.1)
  * `parsebit` (Impact: 215.7)
  * `readoption` (Impact: 27.9)
  * `settag` (Impact: 11.6)
  * `pop` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 466`, `structural_boundaries: 975`, `args: 305`, `func_start: 293`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 384`, `planned_debt: 9`, `duplicate_logic: 41`, `orphaned_logic: 8`
* *Architecture:* `io: 11`, `api: 337`, `import: 5`
* *Defense:* `safety: 20`, `doc: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unicodedata, docutils.utils.math, __future__, sys, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.917 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.709 IQR)
- **Top Global Matches:** file_cluster_8: 11.917, file_cluster_16: 11.991, file_cluster_13: 12.138
- **Magnitude:** 1657.2 | **LOC:** 3462 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.322%), Tech Debt (12.6206%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 575.5)
  * `visit_reference` (Impact: 22.2)
  * `visit_title` (Impact: 21.2)
    * *Intent:* # # I don't know how to implement targets in ODF. # How do we create a target in oowriter? A cross-r...
  * `visit_table` (Impact: 18.7)
  * `get_table_style` (Impact: 17.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 491`, `args: 276`, `func_start: 276`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 345`, `dead_code: 3`, `planned_debt: 6`, `duplicate_logic: 3`
* *Architecture:* `io: 21`, `api: 329`, `import: 26`
* *Defense:* `safety: 36`, `doc: 33`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` warnings, itertools, docutils, .pygmentsformatter, pathlib, xml.etree, docutils.transforms, configparser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/states.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.923 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.805 IQR)
- **Top Global Matches:** file_cluster_8: 11.923, file_cluster_7: 12.137, file_cluster_13: 12.178
- **Magnitude:** 1547.06 | **LOC:** 3267 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.9324%), Tech Debt (41.4323%)
**Top Internal Functions/Classes:**
  * `no_match` (Impact: 325.1)
  * `substitution_def` (Impact: 225.2)
  * `footnote` (Impact: 89.6)
  * `footnote_reference` (Impact: 86.0)
  * `isolate_simple_table` (Impact: 33.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 665`, `structural_boundaries: 430`, `args: 141`, `func_start: 141`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 200`, `dead_code: 4`, `planned_debt: 4`, `duplicate_logic: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 162`, `import: 18`
* *Defense:* `safety: 75`, `doc: 252`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` warnings, docutils.utils, docutils.parsers.rst, docutils.utils._roman_numerals, docutils.statemachine, __future__, docutils, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/nodes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.883 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.8 IQR)
- **Top Global Matches:** file_cluster_16: 12.883, file_cluster_13: 13.115, file_cluster_11: 13.21
- **Magnitude:** 1148.3 | **LOC:** 3342 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4685%), Tech Debt (69.0378%)
**Top Internal Functions/Classes:**
  * `endtag` (Impact: 358.6)
  * `walk` (Impact: 76.2)
  * `unknown_departure` (Impact: 70.1)
    * *Intent:* """Describtion of a command-line option."""
  * `pformat` (Impact: 27.4)
    * *Intent:* # Body Elements # ============= # General # ------- # # Miscellaneous Body Elements and related Body...
  * `__init__` (Impact: 18.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 543`, `args: 170`, `func_start: 170`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 131`, `dead_code: 5`, `planned_debt: 9`, `duplicate_logic: 12`
* *Architecture:* `io: 5`, `api: 282`, `import: 18`
* *Defense:* `safety: 108`, `doc: 428`, `test: 6`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 86.685
  * `Choke Point (Betweenness):` 0.001509 | `Ripple Effect (Closeness):` 0.079812
  * `Imports (Out-Degree: 2):` warnings, docutils.utils, unicodedata, docutils.transforms, os, docutils.frontend, xml.dom.minidom, __future__...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/manpage.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.221 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.705 IQR)
- **Top Global Matches:** file_cluster_16: 13.221, file_cluster_11: 13.454, file_cluster_13: 13.541
- **Magnitude:** 876.94 | **LOC:** 1354 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.7986%), Tech Debt (96.1648%)
**Top Internal Functions/Classes:**
  * `comment_begin` (Impact: 81.4)
  * `visit_option_argument` (Impact: 79.8)
  * `visit_citation` (Impact: 43.2)
  * `visit_option` (Impact: 9.2)
  * `visit_list_item` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 295`, `args: 203`, `func_start: 203`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 388`, `dead_code: 6`, `planned_debt: 6`, `fragile_debt: 4`, `orphaned_logic: 23`
* *Architecture:* `api: 196`, `import: 5`
* *Defense:* `safety: 14`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` re, docutils.utils._roman_numerals, __future__, docutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/html4css1/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.693 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.706 IQR)
- **Top Global Matches:** file_cluster_11: 13.693, file_cluster_16: 13.716, file_cluster_13: 13.772
- **Magnitude:** 810.6 | **LOC:** 965 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.8475%), Tech Debt (98.7845%)
**Top Internal Functions/Classes:**
  * `visit_footnote_reference` (Impact: 67.2)
  * `visit_entry` (Impact: 46.6)
    * *Intent:* # use table for docinfo def visit_docinfo(self, node) -> None: self.context.append(len(self.body)) s...
  * `should_be_compact_paragraph` (Impact: 29.2)
    * *Intent:* # add newline after wrapper tags, don't use <code> for code def visit_literal_block(self, node) -> N...
  * `visit_label` (Impact: 27.8)
  * `visit_table` (Impact: 22.4)
    * *Intent:* # <sup> not allowed in <pre> in HTML 4 def visit_superscript(self, node) -> None: if isinstance(node...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 157`, `args: 95`, `func_start: 95`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 386`, `dead_code: 3`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 25`
* *Architecture:* `io: 14`, `api: 97`, `import: 6`
* *Defense:* `safety: 36`, `doc: 12`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os.path, __future__, docutils, docutils.writers, re, docutils.writers._html_base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.146 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.713 IQR)
- **Top Global Matches:** file_cluster_8: 12.146, file_cluster_2: 12.307, file_cluster_17: 12.313
- **Magnitude:** 790.56 | **LOC:** 559 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.8552%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `keys` (Impact: 82.8)
    * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
  * `toggle` (Impact: 46.7)
  * `go` (Impact: 35.0)
  * `getIncrementals` (Impact: 25.9)
  * `slideLabel` (Impact: 24.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 118`, `args: 30`, `func_start: 75`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 2`, `state_mutation: 238`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 33`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/statemachine.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.988 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.628 IQR)
- **Top Global Matches:** file_cluster_16: 13.988, file_cluster_13: 13.989, file_cluster_8: 14.014
- **Magnitude:** 752.82 | **LOC:** 1535 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.1015%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_state` (Impact: 262.2)
    * *Intent:* """Offset of `self.input_lines` from the beginning of the file."""
  * `get_indented` (Impact: 57.6)
  * `run` (Impact: 54.0)
  * `get_2D_block` (Impact: 22.2)
    * *Intent:* """ (indented, line_offset, blank_finish ) = self.state_machine.get_known_indented(match.end()) sm =...
  * `get_text_block` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 217`, `args: 92`, `func_start: 92`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 206`
* *Architecture:* `io: 10`, `api: 89`, `import: 5`
* *Defense:* `safety: 60`, `doc: 196`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009804
  * `Imports (Out-Degree: 0):` unicodedata, __future__, sys, docutils, re, statemachine
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/frontend.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.721 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.528 IQR)
- **Top Global Matches:** file_cluster_16: 11.721, file_cluster_8: 11.799, file_cluster_13: 11.81
- **Magnitude:** 656.18 | **LOC:** 1179 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.7102%), Tech Debt (22.1598%)
**Top Internal Functions/Classes:**
  * `process` (Impact: 276.9)
  * `validate_threshold` (Impact: 76.5)
  * `validate_encoding_error_handler` (Impact: 49.8)
  * `make_paths_absolute` (Impact: 23.4)
  * `validate_encoding` (Impact: 22.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 148`, `args: 40`, `func_start: 40`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 57`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 16`, `api: 46`, `import: 16`
* *Defense:* `safety: 47`, `doc: 80`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.842
  * `Choke Point (Betweenness):` 0.000676 | `Ripple Effect (Closeness):` 0.065134
  * `Imports (Out-Degree: 1):` warnings, os, os.path, __future__, configparser, docutils.io, sys, docutils...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/transforms/references.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.603 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.078 IQR)
- **Top Global Matches:** file_cluster_8: 11.603, file_cluster_16: 11.856, file_cluster_13: 11.907
- **Magnitude:** 470.16 | **LOC:** 991 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.5498%), Tech Debt (67.5645%)
**Top Internal Functions/Classes:**
  * `symbolize_footnotes` (Impact: 164.2)
  * `apply` (Impact: 135.2)
  * `apply` (Impact: 30.4)
  * `number_footnote_references` (Impact: 19.1)
  * `number_footnotes` (Impact: 15.1)
    * *Intent:* """ Given:: <paragraph> <reference refname="direct-external"> direct external <target ids="id1" name...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 102`, `args: 26`, `func_start: 26`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 56`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 36`, `import: 3`
* *Defense:* `safety: 57`, `doc: 38`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` docutils.transforms, __future__, docutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.638 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.073 IQR)
- **Top Global Matches:** file_cluster_13: 12.638, file_cluster_16: 12.731, file_cluster_11: 12.968
- **Magnitude:** 417.34 | **LOC:** 851 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.4491%), Tech Debt (45.6506%)
**Top Internal Functions/Classes:**
  * `extract_options` (Impact: 218.6)
  * `system_message` (Impact: 44.0)
  * `__init__` (Impact: 11.9)
  * `debug` (Impact: 4.2)
  * `notify_observers` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 127`, `args: 39`, `func_start: 39`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 59`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 10`, `api: 51`, `import: 18`
* *Defense:* `safety: 23`, `doc: 92`, `test: 2`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` warnings, docutils.utils, unicodedata, os.path, os, itertools, docutils.frontend, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.145 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.743 IQR)
- **Top Global Matches:** file_cluster_8: 11.145, file_cluster_13: 11.229, file_cluster_16: 11.24
- **Magnitude:** 364.66 | **LOC:** 856 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.0435%), Tech Debt (9.1888%)
**Top Internal Functions/Classes:**
  * `debugging_dumps` (Impact: 46.4)
  * `report_SystemMessage` (Impact: 41.1)
  * `publish` (Impact: 31.9)
  * `publish_programmatically` (Impact: 30.8)
    * *Intent:* """ Set up & run a `Publisher` for programmatic use. Return a document tree. Parameters: see `publis...
  * `__init__` (Impact: 24.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 77`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 35`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 39`, `import: 11`
* *Defense:* `safety: 18`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.934
  * `Choke Point (Betweenness):` 0.001183 | `Ripple Effect (Closeness):` 0.063725
  * `Imports (Out-Degree: 2):` warnings, os, docutils.frontend, pprint, __future__, docutils.readers, sys, locale...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/parsers/rst/directives/misc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.793 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.352 IQR)
- **Top Global Matches:** file_cluster_8: 10.793, file_cluster_13: 10.908, file_cluster_7: 11.154
- **Magnitude:** 302.22 | **LOC:** 691 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2175%), Tech Debt (84.4437%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 115.0)
    * *Intent:* # ignored except for 'literal' or 'code': 'number-lines': directives.value_or((None,), int), 'class'...
  * `run` (Impact: 68.9)
  * `run` (Impact: 27.5)
  * `run` (Impact: 11.1)
  * `adapt_path` (Impact: 8.6)
    * *Intent:* # `root_prefix` is prepended to absolute paths (cf. root_prefix setting), # `source` is the `current...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 104`, `args: 19`, `func_start: 19`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 31`, `import: 12`
* *Defense:* `safety: 32`, `doc: 30`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.677
  * `Choke Point (Betweenness):` 0.000978 | `Ripple Effect (Closeness):` 0.015609
  * `Imports (Out-Degree: 2):` docutils.parsers.rst, urllib.error, docutils.transforms, urllib.request, __future__, docutils, re, pathlib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/parsers/rst/directives/tables.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.858 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.521 IQR)
- **Top Global Matches:** file_cluster_8: 10.858, file_cluster_13: 10.948, file_cluster_17: 11.228
- **Magnitude:** 271.7 | **LOC:** 524 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.7%), Tech Debt (19.1363%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 147.3)
  * `check_table_dimensions` (Impact: 32.1)
  * `extend_short_rows_with_empty_cells` (Impact: 8.2)
  * `make_title` (Impact: 5.8)
  * `align` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 78`, `args: 18`, `func_start: 18`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 46`, `planned_debt: 8`
* *Architecture:* `api: 22`, `import: 11`
* *Defense:* `safety: 16`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` warnings, docutils.utils, docutils.parsers.rst, urllib.error, urllib.request, __future__, docutils, csv...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/tableparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.577 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.493 IQR)
- **Top Global Matches:** file_cluster_8: 11.577, file_cluster_13: 11.636, file_cluster_7: 11.786
- **Magnitude:** 269.84 | **LOC:** 544 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.7966%), Tech Debt (43.1932%)
**Top Internal Functions/Classes:**
  * `structure_from_cells` (Impact: 41.9)
  * `init_row` (Impact: 35.3)
  * `find_head_body_sep` (Impact: 31.1)
  * `scan_left` (Impact: 15.5)
  * `scan_down` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 63`, `args: 21`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 53`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 24`, `import: 5`
* *Defense:* `safety: 7`, `doc: 46`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` docutils.utils, __future__, docutils, sys, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/io.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.235 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.971 IQR)
- **Top Global Matches:** file_cluster_13: 13.235, file_cluster_16: 13.396, file_cluster_11: 13.457
- **Magnitude:** 257.4 | **LOC:** 717 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.7976%), Tech Debt (99.9987%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 55.2)
    * *Intent:* """The source of input data."""
  * `write` (Impact: 22.5)
  * `write` (Impact: 13.5)
  * `encode` (Impact: 9.3)
  * `open` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 98`, `args: 30`, `func_start: 30`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 70`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 13`
* *Architecture:* `io: 18`, `api: 35`, `import: 11`
* *Defense:* `safety: 46`, `doc: 100`, `test: 2`, `immutability_locks: 9`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.548
  * `Choke Point (Betweenness):` 0.000241 | `Ripple Effect (Closeness):` 0.05296
  * `Imports (Out-Degree: 1):` warnings, os, __future__, locale, sys, re, codecs, docutils...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/s5_html/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.065 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.406 IQR)
- **Top Global Matches:** file_cluster_13: 12.065, file_cluster_8: 12.314, file_cluster_11: 12.461
- **Magnitude:** 222.8 | **LOC:** 355 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.4987%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `find_theme` (Impact: 100.0)
  * `visit_title` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 41`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 104`, `dead_code: 1`
* *Architecture:* `io: 22`, `api: 12`, `import: 8`
* *Defense:* `safety: 3`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, __future__, sys, docutils, re, docutils.writers, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/transforms/frontmatter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.97 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.945 IQR)
- **Top Global Matches:** file_cluster_13: 11.97, file_cluster_8: 12.004, file_cluster_17: 12.13
- **Magnitude:** 216.1 | **LOC:** 549 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.1974%), Tech Debt (68.2505%)
**Top Internal Functions/Classes:**
  * `extract_bibliographic` (Impact: 79.4)
  * `authors_from_one_paragraph` (Impact: 14.7)
  * `authors_from_bullet_list` (Impact: 10.9)
  * `candidate_index` (Impact: 9.2)
    * *Intent:* """ Transform the following node tree:: <node> <title> <section> <title> ...
  * `set_metadata` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 53`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 18`, `import: 4`
* *Defense:* `safety: 28`, `doc: 22`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, __future__, docutils.transforms, docutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/math/mathml_elements.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.288 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.932 IQR)
- **Top Global Matches:** file_cluster_13: 13.288, file_cluster_16: 13.327, file_cluster_8: 13.432
- **Magnitude:** 208.02 | **LOC:** 483 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.463%), Tech Debt (99.956%)
**Top Internal Functions/Classes:**
  * `__setitem__` (Impact: 14.6)
  * `__repr__` (Impact: 12.7)
  * `append` (Impact: 9.4)
  * `transfer_attributes` (Impact: 9.2)
    * *Intent:* # MathML element classes # ---------------------- class math(MathRow): """Top-level MathML element, ...
  * `unindent_xml` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 74`, `args: 20`, `func_start: 20`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `duplicate_logic: 7`
* *Architecture:* `api: 47`, `import: 3`
* *Defense:* `safety: 11`, `doc: 92`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004902
  * `Imports (Out-Degree: 0):` mathml_elements, __future__, xml.etree.ElementTree, numbers
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/utils/math/latex2mathml.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.464 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.27 IQR)
- **Top Global Matches:** file_cluster_8: 11.464, file_cluster_13: 11.853, file_cluster_7: 11.892
- **Magnitude:** 204.16 | **LOC:** 1253 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.865%), Tech Debt (11.5007%)
**Top Internal Functions/Classes:**
  * `tex2mathml` (Impact: 6.0)
  * `align_attributes` (Impact: 5.7)
  * `tex_equation_columns` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 86`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 156`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `api: 18`, `import: 4`
* *Defense:* `safety: 15`, `doc: 26`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` latex2mathml, unicodedata, docutils.utils.math, docutils.utils.math.mathml_elements, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/directives/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.355 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.828 IQR)
- **Top Global Matches:** file_cluster_13: 12.355, file_cluster_16: 12.395, file_cluster_8: 12.512
- **Magnitude:** 190.62 | **LOC:** 481 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.0991%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `directive` (Impact: 81.2)
  * `single_char_or_unicode` (Impact: 15.4)
  * `encoding` (Impact: 11.4)
  * `positive_int_list` (Impact: 8.4)
  * `parser_name` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 83`, `args: 24`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 24`
* *Architecture:* `api: 27`, `import: 8`
* *Defense:* `safety: 26`, `doc: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` docutils.utils, docutils.parsers.rst, __future__, docutils.parsers.rst.languages, docutils, re, codecs, importlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/transforms/peps.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.862 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.189 IQR)
- **Top Global Matches:** file_cluster_13: 11.862, file_cluster_8: 12.06, file_cluster_16: 12.143
- **Magnitude:** 185.68 | **LOC:** 316 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.12%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `apply` (Impact: 116.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 40`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 47`
* *Architecture:* `io: 1`, `api: 18`, `import: 8`
* *Defense:* `safety: 13`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` docutils.transforms, os, __future__, docutils, re, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/roles.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.815 IQR)
- **Top Global Matches:** file_cluster_13: 11.707, file_cluster_8: 11.754, file_cluster_16: 11.976
- **Magnitude:** 175.96 | **LOC:** 451 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.7661%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `role` (Impact: 105.6)
  * `set_classes` (Impact: 7.4)
  * `normalize_options` (Impact: 5.7)
  * `normalized_role_options` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 72`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 32`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* `safety: 18`, `doc: 28`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.656
  * `Choke Point (Betweenness):` 0.00058 | `Ripple Effect (Closeness):` 0.024714
  * `Imports (Out-Degree: 1):` warnings, docutils.parsers.rst, docutils.utils.code_analyzer, __future__, docutils.parsers.rst.languages, docutils
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/utils/_roman_numerals.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.43 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.708 IQR)
- **Top Global Matches:** file_cluster_13: 10.43, file_cluster_16: 10.448, file_cluster_0: 10.611
- **Magnitude:** 148.52 | **LOC:** 265 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.4763%), Tech Debt (94.8908%)
**Top Internal Functions/Classes:**
  * `from_string` (Impact: 78.8)
  * `__init__` (Impact: 10.4)
  * `to_uppercase` (Impact: 5.7)
  * `to_lowercase` (Impact: 5.7)
  * `__setattr__` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 43`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 26`, `api: 14`, `import: 5`
* *Defense:* `safety: 4`, `doc: 34`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 6e-05 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 1):` __future__, docutils.utils._typing, sys, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `docutils-0.22.4/docutils/writers/html4css1/__init__.py` (PYTHON) | Magnitude: 810.6 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 675, state_mutation: 386, branch: 164, structural_boundaries: 157

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `docutils-0.22.4/tools/rst2html5.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, safety: 2, doc: 2
- `docutils-0.22.4/docutils/utils/_roman_numerals.py` (PYTHON) | Magnitude: 148.52 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 149, branch: 49, structural_boundaries: 43, encapsulation: 36
- `docutils-0.22.4/docutils/parsers/rst/directives/html.py` (PYTHON) | Magnitude: 14.16 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, doc: 2, import: 2
- `docutils-0.22.4/docutils/transforms/frontmatter.py` (PYTHON) | Magnitude: 216.1 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 236, branch: 77, structural_boundaries: 53, safety: 28
- `docutils-0.22.4/docutils/utils/math/mathml_elements.py` (PYTHON) | Magnitude: 208.02 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 143, doc: 92, structural_boundaries: 74, api: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `docutils-0.22.4/docutils/statemachine.py` (PYTHON) | Magnitude: 752.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 669, structural_boundaries: 217, state_mutation: 206, doc: 196
- `docutils-0.22.4/docutils/transforms/__init__.py` (PYTHON) | Magnitude: 77.8 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, doc: 44, state_mutation: 27, structural_boundaries: 22
- `docutils-0.22.4/docutils/utils/math/__init__.py` (PYTHON) | Magnitude: 23.56 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, doc: 8, branch: 5
- `docutils-0.22.4/tools/dev/unicode2rstsubs.py` (PYTHON) | Magnitude: 0.12 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 37, branch: 30, doc: 24
- `docutils-0.22.4/docutils/frontend.py` (PYTHON) | Magnitude: 656.18 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 744, branch: 178, structural_boundaries: 148, doc: 80

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.css` (CSS) | Magnitude: 0.58 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 3, import: 3
- `docutils-0.22.4/tools/docutils-cli.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, encapsulation: 2, import: 1
- `docutils-0.22.4/docutils/parsers/rst/directives/body.py` (PYTHON) | Magnitude: 121.92 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 206, structural_boundaries: 57, branch: 35, api: 24
- `docutils-0.22.4/docutils/parsers/rst/tableparser.py` (PYTHON) | Magnitude: 269.84 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 281, branch: 74, structural_boundaries: 63, state_mutation: 53
- `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (PYTHON) | Magnitude: 1657.2 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 2851, structural_boundaries: 491, branch: 412, state_mutation: 345

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `docutils-0.22.4/docutils/utils/code_analyzer.py` -> **Severity: 0.097** (Bridge: 0.001 * Flux: 100.0%)
- `docutils-0.22.4/docutils/core.py` -> **Severity: 0.078** (Bridge: 0.0012 * Flux: 65.6756%)
- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 0.075** (Bridge: 0.0015 * Flux: 49.9182%)
- `docutils-0.22.4/docutils/parsers/rst/roles.py` -> **Severity: 0.056** (Bridge: 0.0006 * Flux: 96.5578%)
- `docutils-0.22.4/docutils/parsers/rst/directives/images.py` -> **Severity: 0.048** (Bridge: 0.0006 * Flux: 80.6685%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 5.23** (Embedded: 0.0798 * Error Risk: 65.5346%)
- `docutils-0.22.4/docutils/utils/_typing.py` -> **Severity: 5.087** (Embedded: 0.07 * Error Risk: 72.6386%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 3.278** (Embedded: 0.0651 * Error Risk: 50.3265%)
- `docutils-0.22.4/docutils/core.py` -> **Severity: 3.114** (Embedded: 0.0637 * Error Risk: 48.8616%)
- `docutils-0.22.4/docutils/io.py` -> **Severity: 2.447** (Embedded: 0.053 * Error Risk: 46.1997%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 6647.673** (Blast Radius: 86.685 * Doc Risk: 76.6877%)
- `docutils-0.22.4/docutils/utils/_typing.py` -> **Severity: 2520.664** (Blast Radius: 52.361 * Doc Risk: 48.1401%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 1673.508** (Blast Radius: 56.842 * Doc Risk: 29.4414%)
- `docutils-0.22.4/docutils/parsers/rst/directives/body.py` -> **Severity: 1335.157** (Blast Radius: 15.19 * Doc Risk: 87.8971%)
- `docutils-0.22.4/docutils/parsers/rst/directives/misc.py` -> **Severity: 999.79** (Blast Radius: 22.677 * Doc Risk: 44.0883%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
