# ARCHITECTURAL_BRIEF: docutils
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 263 |
| Analyzed Artifacts (Scanned) | 206 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 57 |
| Total LOC | 34602 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 78.3% |
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
| PYTHON | 144 | 31418 | 69.9% |
| PLAINTEXT | 36 | 0 | 17.5% |
| CSS | 24 | 2651 | 11.7% |
| JAVASCRIPT | 1 | 516 | 0.5% |
| MAKEFILE | 1 | 17 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 170 | 82.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 36 | 17.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 57*

**Composition by Extension & Reason:**
- `.el`: 24x Excluded (Unsupported Extension: '.el')
- `.rst`: 15x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 4x Unsupported Format (.undeterminable)
- `.tex`: 4x Excluded (Unsupported Extension: '.tex')
- `.conf`: 2x Excluded (Unsupported Extension: '.conf')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 365 LOC), 1x Excluded (Machine-Generated Source Code Signature: 192 LOC)
- `.sty`: 1x Excluded (Unsupported Extension: '.sty')
- `.odt`: 1x Excluded (Explicitly Denied Extension: '.odt')
- `.txt`: 1x Excluded (Machine-Generated Source Code Signature: 26 LOC)
- `.css`: 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.9 | 17.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 70.0 | 65.0 | 65.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 98.4 | 13.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 13.6 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 59.6 | 69.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.4 | 0.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 54.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 29.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 157 | 34 | 2 | `docutils-0.22.4/docutils/utils/math/math2html.py` |
| cleanup | 32 | 8 | 0 | `docutils-0.22.4/docutils/utils/math/latex2mathml.py` |
| guards | 1186 | 77 | 12 | `docutils-0.22.4/docutils/nodes.py` |
| danger | 1168 | 85 | 11 | `docutils-0.22.4/docutils/nodes.py` |
| concurrency | 38 | 7 | 0 | `docutils-0.22.4/docutils/nodes.py` |
| connectivity | 2682 | 71 | 18 | `docutils-0.22.4/docutils/utils/math/math2html.py` |
| io | 247 | 32 | 3 | `docutils-0.22.4/docutils/utils/_roman_numerals.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 3 | 0 | `docutils-0.22.4/docutils/utils/math/tex2mathml_extern.py` |
| time | 2 | 2 | 0 | `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 100 | 21 | 0 | `docutils-0.22.4/docutils/parsers/rst/states.py` |
| events | 33 | 6 | 0 | `docutils-0.22.4/docutils/frontend.py` |
| tests | 8 | 1 | 0 | `docutils-0.22.4/docutils/utils/smartquotes.py` |
| docs | 1409 | 141 | 15 | `docutils-0.22.4/docutils/nodes.py` |
| debt | 231 | 44 | 2 | `docutils-0.22.4/docutils/writers/latex2e/__init__.py` |
| mutation | 13578 | 145 | 148 | `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` |
| dead_code | 413 | 47 | 2 | `docutils-0.22.4/docutils/writers/manpage.py` |
| credential | 0 | 0 | 0 | - |
| threat | 111 | 31 | 1 | `docutils-0.22.4/docutils/frontend.py` |
| ml_ai | 7 | 4 | 0 | `docutils-0.22.4/docutils/transforms/peps.py` |
| ui | 96 | 20 | 0 | `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `docutils-0.22.4/docutils/utils/_roman_numerals.py` (Hits: 26)
- `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (Hits: 19)
- `docutils-0.22.4/docutils/io.py` (Hits: 18)

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

- `handle_cmd` (@ `docutils-0.22.4/docutils/utils/math/latex2mathml.py`) -> Impact: **165.3** | LOC: 306
  * *Intent:* # math(msub(mi('x'), mtext('in'))) # >>> parse_latex_math(math(), '2⌘') # Traceback (most recent call last): # docutils.utils.math.MathError: Unsuppor...
- `phrase_ref` (@ `docutils-0.22.4/docutils/parsers/rst/states.py`) -> Impact: **83.1** | LOC: 74
  * *Intent:* # `text` is ignored (since 0.16) match = self.patterns.embedded_link.search(escaped) if match: # embedded <URI> or <alias_> text = escaped[:match.star...
- `from_string` (@ `docutils-0.22.4/docutils/utils/_roman_numerals.py`) -> Impact: **69.1** | LOC: 101
  * *Intent:* """Create a ``RomanNumeral`` from a well-formed string representation. Returns ``RomanNumeral`` or raises ``InvalidRomanNumeralError``. >>> answer = R...
- `__init__` (@ `docutils-0.22.4/docutils/writers/latex2e/__init__.py`) -> Impact: **67.8** | LOC: 195
- `parse_directive_block` (@ `docutils-0.22.4/docutils/parsers/rst/states.py`) -> Impact: **63.5** | LOC: 45
- `starttag` (@ `docutils-0.22.4/docutils/writers/_html_base.py`) -> Impact: **61.5** | LOC: 65
  * *Intent:* """ Construct and return a start tag given a node (id & class attributes are extracted), tag name, and optional attributes. """
- `findall` (@ `docutils-0.22.4/docutils/nodes.py`) -> Impact: **59.9** | LOC: 87
- `keys` (@ `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js`) -> Impact: **59.7** | LOC: 62
  * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
- `educate_tokens` (@ `docutils-0.22.4/docutils/utils/smartquotes.py`) -> Impact: **59.5** | LOC: 111
  * *Intent:* """Return iterator that "educates" the items of `text_tokens`."""
- `set_duplicate_name_id` (@ `docutils-0.22.4/docutils/nodes.py`) -> Impact: **58.7** | LOC: 62

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `docutils-0.22.4/docutils` | 8 | 4857.84 | 34.24% | 14.55% |
| `docutils-0.22.4/docutils/parsers/rst` | 4 | 4689.32 | 38.89% | 5.77% |
| `docutils-0.22.4/docutils/utils/math` | 8 | 4414.48 | 28.97% | 4.5% |
| `docutils-0.22.4/docutils/writers` | 5 | 3869.4 | 38.44% | 56.48% |
| `docutils-0.22.4/docutils/writers/odf_odt` | 3 | 3764.32 | 67.86% | 2.82% |
| `docutils-0.22.4/docutils/writers/latex2e` | 1 | 3479.76 | 71.54% | 14.19% |
| `docutils-0.22.4/docutils/transforms` | 8 | 2031.84 | 38.13% | 44.11% |
| `docutils-0.22.4/docutils/parsers/rst/directives` | 9 | 1981.32 | 40.8% | 19.39% |
| `docutils-0.22.4/docutils/utils` | 7 | 1260.2 | 29.51% | 14.94% |
| `docutils-0.22.4/docutils/writers/html4css1` | 3 | 1159.45 | 28.25% | 33.33% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `docutils-0.22.4/docutils/writers/html4css1/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/writers/html5_polyglot/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/writers/manpage.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/recommonmark_wrapper.py` -> **99.9065%** Exposure
- `docutils-0.22.4/docutils/parsers/rst/languages/pl.py` -> **98.9463%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `docutils-0.22.4/docutils/languages/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/docutils_xml.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/recommonmark_wrapper.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/rst/directives/body.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/rst/directives/images.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `docutils-0.22.4/docutils/writers/manpage.py` -> **164** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/docutils/writers/html4css1/__init__.py` -> **80** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/docutils/writers/html5_polyglot/__init__.py` -> **34** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/docutils/utils/math/math2html.py` -> **18** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/docutils/transforms/peps.py` -> **7** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `466` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `docutils-0.22.4/docutils/writers/html4css1/__init__.py` (PYTHON) -> Cumulative Risk: **731.32**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1157.46 | **LOC:** 965 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.1518%)
- **Heaviest Functions:** `visit_image` (Impact: 58.6), `should_be_compact_paragraph` (Impact: 29.2), `visit_field_list` (Impact: 20.4)

### 2. `docutils-0.22.4/docutils/writers/html5_polyglot/__init__.py` (PYTHON) -> Cumulative Risk: **722.01**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 394.78 | **LOC:** 399 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `visit_inline` (Impact: 21.9), `visit_literal` (Impact: 18.8), `visit_topic` (Impact: 11.2)

### 3. `docutils-0.22.4/docutils/writers/manpage.py` (PYTHON) -> Cumulative Risk: **711.14**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1349.66 | **LOC:** 1354 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.1925%)
- **Heaviest Functions:** `list_start` (Impact: 30.8), `astext` (Impact: 22.9), `depart_document` (Impact: 15.2)

### 4. `docutils-0.22.4/docutils/writers/_html_base.py` (PYTHON) -> Cumulative Risk: **701.2**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2379.92 | **LOC:** 1896 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.614%), Documentation (95.1923%)
- **Heaviest Functions:** `starttag` (Impact: 61.5), `visit_math` (Impact: 45.1), `visit_image` (Impact: 39.6)

### 5. `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (PYTHON) -> Cumulative Risk: **696.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3556.5 | **LOC:** 3462 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.6543%), Documentation (94.8718%)
- **Heaviest Functions:** `make_field_element` (Impact: 50.7), `generate_image` (Impact: 46.5), `visit_image` (Impact: 32.6)

### 6. `docutils-0.22.4/docutils/writers/latex2e/__init__.py` (PYTHON) -> Cumulative Risk: **679.76**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3479.76 | **LOC:** 3418 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.704%), Documentation (87.5764%)
- **Heaviest Functions:** `__init__` (Impact: 67.8), `encode` (Impact: 49.3), `visit_literal_block` (Impact: 45.5)

### 7. `docutils-0.22.4/docutils/transforms/parts.py` (PYTHON) -> Cumulative Risk: **667.24**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 224.74 | **LOC:** 176 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6787%), Tech Debt (93.2655%)
- **Heaviest Functions:** `build_contents` (Impact: 25.6), `apply` (Impact: 15.4), `update_section_numbers` (Impact: 14.4)

### 8. `docutils-0.22.4/docutils/parsers/rst/directives/images.py` (PYTHON) -> Cumulative Risk: **665.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 172.36 | **LOC:** 187 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.401%)
- **Heaviest Functions:** `run` (Impact: 28.4), `run` (Impact: 23.6), `figwidth_value` (Impact: 4.5)

### 9. `docutils-0.22.4/docutils/parsers/rst/directives/body.py` (PYTHON) -> Cumulative Risk: **663.92**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 249.34 | **LOC:** 330 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.5576%)
- **Heaviest Functions:** `run` (Impact: 20.8), `run` (Impact: 12.9), `run` (Impact: 6.6)

### 10. `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` (JAVASCRIPT) -> Cumulative Risk: **655.73**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 604.92 | **LOC:** 559 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.3406%)
- **Heaviest Functions:** `keys` (Impact: 59.7), `go` (Impact: 28.9), `getIncrementals` (Impact: 21.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `docutils-0.22.4/docutils/parsers/rst/states.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3729.0 | **LOC:** 3267 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.6616%), Tech Debt (11.0466%)
**Top Internal Functions/Classes:**
  * `phrase_ref` (Impact: 83.1)
    * *Intent:* # `text` is ignored (since 0.16) match = self.patterns.embedded_link.search(escaped) if match: # emb...
  * `parse_directive_block` (Impact: 63.5)
  * `nested_parse` (Impact: 50.2)
  * `interpreted_or_phrase_ref` (Impact: 42.5)
  * `parse_enumerator` (Impact: 40.7)
    * *Intent:* """ Analyze an enumerator and return the results. :Return: - the enumerator format ('period', 'paren...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 537 instances
* *State Mutation (weighted view):* 1778
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 642`, `structural_boundaries: 433`, `args: 141`, `func_start: 141`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 704`, `dead_code: 4`, `planned_debt: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 162`, `import: 18`
* *Defense:* `safety: 72`, `doc: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, docutils, docutils.nodes, docutils.parsers.rst, docutils.statemachine, docutils.utils, docutils.utils._roman_numerals, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3556.5 | **LOC:** 3462 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.4918%), Tech Debt (8.47%)
**Top Internal Functions/Classes:**
  * `make_field_element` (Impact: 50.7)
  * `generate_image` (Impact: 46.5)
  * `visit_image` (Impact: 32.6)
    * *Intent:* # Capture the image file. source = node['uri'] uri_parts = urllib.parse.urlparse(source) if uri_part...
  * `update_stylesheet` (Impact: 27.0)
    * *Intent:* """Update xml style sheet element with language and region/country."""
  * `add_header_footer` (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 488 instances
* *State Mutation (weighted view):* 1884
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 401`, `structural_boundaries: 496`, `args: 276`, `func_start: 276`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 908`, `dead_code: 3`, `planned_debt: 6`
* *Architecture:* `io: 19`, `api: 275`, `import: 26`
* *Defense:* `safety: 34`, `doc: 18`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .pygmentsformatter, IPython.Shell, __future__, configparser, copy, docutils, docutils.parsers.rst.directives.images, docutils.readers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/latex2e/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3479.76 | **LOC:** 3418 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.5355%), Tech Debt (14.1871%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 67.8)
  * `encode` (Impact: 49.3)
    * *Intent:* """Return text with 'problematic' characters escaped. * Escape the special printing characters ``# $...
  * `visit_literal_block` (Impact: 45.5)
    * *Intent:* """Render a literal block. Corresponding rST elements: literal block, parsed-literal, code. """
  * `depart_docinfo_item` (Impact: 36.7)
  * `visit_entry` (Impact: 34.0)
    * *Intent:* # cell separation if self.active_table.get_entry_number() == 0: self.insert_additional_table_colum_d...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 504 instances
* *State Mutation (weighted view):* 1749
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 558`, `structural_boundaries: 406`, `args: 245`, `func_start: 245`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 741`, `dead_code: 20`, `planned_debt: 30`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 246`, `import: 9`
* *Defense:* `safety: 95`, `doc: 56`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, docutils, docutils.transforms, docutils.utils._roman_numerals, docutils.utils.math, pathlib, re, string...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/math/math2html.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2837.08 | **LOC:** 3167 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.2712%), Tech Debt (24.5094%)
**Top Internal Functions/Classes:**
  * `readoption` (Impact: 18.6)
  * `readtag` (Impact: 16.8)
  * `writepos` (Impact: 16.6)
  * `parseformula` (Impact: 15.6)
  * `read` (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 302 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 1114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 447`, `structural_boundaries: 995`, `args: 305`, `func_start: 293`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 3`, `state_mutation: 510`, `planned_debt: 9`, `unreferenced_by_name: 18`
* *Architecture:* `io: 10`, `api: 337`, `import: 5`
* *Defense:* `safety: 17`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, docutils.utils.math, pathlib, sys, unicodedata
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/_html_base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2379.92 | **LOC:** 1896 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.6367%), Tech Debt (12.0516%)
**Top Internal Functions/Classes:**
  * `starttag` (Impact: 61.5)
    * *Intent:* """ Construct and return a start tag given a node (id & class attributes are extracted), tag name, a...
  * `visit_math` (Impact: 45.1)
    * *Intent:* # Also called from `visit_math_block()`: is_block = isinstance(node, nodes.math_block) format = self...
  * `visit_image` (Impact: 39.6)
    * *Intent:* # reference/embed images (still images and videos) uri = node['uri'] alt = node.get('alt', uri) mime...
  * `prepare_svg` (Impact: 29.0)
    * *Intent:* # Parse SVG source `code` (ignoring comments and preamble code), # add relevant attributes from `nod...
  * `__init__` (Impact: 26.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 337 instances
* *State Mutation (weighted view):* 1245
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 340`, `args: 204`, `func_start: 204`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 571`, `dead_code: 2`, `planned_debt: 10`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 207`, `import: 16`
* *Defense:* `safety: 65`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.000263 | `Ripple Effect (Closeness):` 0.004878
  * `Imports (Out-Degree: 2):` __future__, base64, docutils, docutils.parsers.rst.directives, docutils.parsers.rst.directives.images, docutils.transforms, docutils.utils.math, mimetypes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/nodes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1873.72 | **LOC:** 3342 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.3857%), Tech Debt (10.095%)
**Top Internal Functions/Classes:**
  * `findall` (Impact: 59.9)
  * `set_duplicate_name_id` (Impact: 58.7)
  * `set_id` (Impact: 42.7)
  * `validate_content` (Impact: 32.2)
  * `pformat` (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *Amplified Sql Injection:* 2 instances
* *State Mutation (weighted view):* 609
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 549`, `args: 170`, `func_start: 170`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 251`, `dead_code: 5`, `planned_debt: 9`
* *Architecture:* `io: 5`, `api: 286`, `import: 18`
* *Defense:* `safety: 99`, `doc: 214`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 86.425
  * `Choke Point (Betweenness):` 0.001495 | `Ripple Effect (Closeness):` 0.079423
  * `Imports (Out-Degree: 2):` __future__, collections, collections.abc, dependency, docutils.frontend, docutils.transforms, docutils.utils, docutils.utils._typing...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/manpage.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1349.66 | **LOC:** 1354 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.4391%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `list_start` (Impact: 30.8)
  * `astext` (Impact: 22.9)
    * *Intent:* """Return the final formatted document as a string."""
  * `depart_document` (Impact: 15.2)
  * `_visit_reference_with_macro` (Impact: 13.3)
    * *Intent:* % insert_URI_breakpoints(node['refuri'])) # elif 'refid' in node: # use UR/UE or MT/ME if 'refuri' i...
  * `__init__` (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 537
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 297`, `args: 203`, `func_start: 203`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 275`, `dead_code: 6`, `planned_debt: 6`, `fragile_debt: 4`, `unreferenced_by_name: 164`
* *Architecture:* `api: 196`, `import: 5`
* *Defense:* `safety: 14`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, docutils, docutils.utils._roman_numerals, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/html4css1/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1157.46 | **LOC:** 965 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.7625%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `visit_image` (Impact: 58.6)
  * `should_be_compact_paragraph` (Impact: 29.2)
    * *Intent:* # Omit <p> tags to produce visually compact lists (less vertical # whitespace) as CSS styling requir...
  * `visit_field_list` (Impact: 20.4)
  * `visit_literal` (Impact: 18.8)
    * *Intent:* # use <tt> (not supported by HTML5), # cater for limited styling options in CSS1 using hard-coded NB...
  * `footnote_backrefs` (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 158 instances
* *State Mutation (weighted view):* 585
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 160`, `args: 95`, `func_start: 95`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 269`, `dead_code: 3`, `planned_debt: 2`, `unreferenced_by_name: 80`
* *Architecture:* `io: 14`, `api: 97`, `import: 6`
* *Defense:* `safety: 35`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, docutils, docutils.writers, docutils.writers._html_base, os.path, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/statemachine.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1123.42 | **LOC:** 1535 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.0278%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_indented` (Impact: 58.5)
  * `run` (Impact: 47.0)
  * `check_line` (Impact: 31.0)
    * *Intent:* """ Examine one line of input for a transition match & execute its method. Parameters: - `context`: ...
  * `__init__` (Impact: 17.2)
  * `get_2D_block` (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 130 instances
* *State Mutation (weighted view):* 443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 222`, `args: 92`, `func_start: 92`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 183`
* *Architecture:* `io: 15`, `api: 103`, `import: 5`
* *Defense:* `safety: 57`, `doc: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.392
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009756
  * `Imports (Out-Degree: 0):` __future__, docutils, re, statemachine, sys, unicodedata
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/utils/math/latex2mathml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 984.06 | **LOC:** 1253 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.5515%), Tech Debt (11.5007%)
**Top Internal Functions/Classes:**
  * `handle_cmd` (Impact: 165.3)
    * *Intent:* # math(msub(mi('x'), mtext('in'))) # >>> parse_latex_math(math(), '2⌘') # Traceback (most recent cal...
  * `parse_latex_math` (Impact: 50.2)
    * *Intent:* # Test: # >>> tex_optarg(' [optional argument] after whitespace') # ('optional argument', ' after wh...
  * `handle_script_or_limit` (Impact: 37.5)
    * *Intent:* # >>> handle_math_alphabet('mathrm', math(), '\\alpha') # (math(mi('α', mathvariant='normal')), '') ...
  * `handle_math_alphabet` (Impact: 23.2)
    * *Intent:* # (mover(mo('_', accent='true'), switch=True, accent='false'), '{981}') # >>> handle_cmd('bar', math...
  * `tex_group` (Impact: 14.2)
    * *Intent:* # Test: # # >>> tex_token('{opening bracket of group}') # ('{', 'opening bracket of group}') # >>> t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 606
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 86`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 220`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `api: 15`, `import: 4`
* *Defense:* `safety: 13`, `doc: 13`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` docutils.utils.math, docutils.utils.math.mathml_elements, latex2mathml, re, unicodedata
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/transforms/references.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 885.14 | **LOC:** 991 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.1923%), Tech Debt (29.0339%)
**Top Internal Functions/Classes:**
  * `apply` (Impact: 38.5)
  * `visit_reference` (Impact: 33.7)
  * `resolve_indirect_target` (Impact: 33.3)
  * `resolve_indirect_references` (Impact: 29.6)
  * `apply` (Impact: 25.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 141 instances
* *State Mutation (weighted view):* 475
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 102`, `args: 26`, `func_start: 26`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 193`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 36`, `import: 3`
* *Defense:* `safety: 53`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, docutils, docutils.transforms
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/frontend.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 753.16 | **LOC:** 1179 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.2875%), Tech Debt (9.0327%)
**Top Internal Functions/Classes:**
  * `populate_from_components` (Impact: 22.3)
  * `make_paths_absolute` (Impact: 21.2)
  * `validate_encoding` (Impact: 18.2)
  * `check_args` (Impact: 18.2)
    * *Intent:* # provisional: argument handling will change, see RELEASE_NOTES source = destination = None if args:...
  * `__init__` (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 158`, `args: 40`, `func_start: 40`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 109`, `planned_debt: 2`
* *Architecture:* `io: 15`, `api: 42`, `import: 16`
* *Defense:* `safety: 38`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.672
  * `Choke Point (Betweenness):` 0.00067 | `Ripple Effect (Closeness):` 0.064816
  * `Imports (Out-Degree: 1):` __future__, codecs, collections.abc, configparser, docutils, docutils.io, optparse, os...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/parsers/rst/directives/misc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 623.02 | **LOC:** 691 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.7629%), Tech Debt (9.9431%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 25.9)
  * `run` (Impact: 23.9)
    * *Intent:* % ((states.Inliner.simplename,) * 2)) """Dynamically create and register a custom interpreted text r...
  * `read_file` (Impact: 16.2)
    * *Intent:* """Read text file at `path`. Clip and return content. Provisional. """
  * `as_literal_block` (Impact: 15.2)
    * *Intent:* """Return list with literal_block containing `text`. Provisional """
  * `parsemeta` (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *Amplified Sql Injection:* 1 instances
* *State Mutation (weighted view):* 383
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 113`, `args: 19`, `func_start: 19`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 161`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 31`, `import: 12`
* *Defense:* `safety: 31`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.609
  * `Choke Point (Betweenness):` 0.000968 | `Ripple Effect (Closeness):` 0.015533
  * `Imports (Out-Degree: 2):` __future__, docutils, docutils.nodes, docutils.parsers.rst, docutils.parsers.rst.directives.body, docutils.transforms, pathlib, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 604.92 | **LOC:** 559 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.8695%), Tech Debt (17.4332%)
**Top Internal Functions/Classes:**
  * `keys` (Impact: 59.7)
    * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
  * `go` (Impact: 28.9)
  * `getIncrementals` (Impact: 21.5)
  * `clicker` (Impact: 19.2)
  * `fixLinks` (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 133`, `args: 30`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 4`, `state_mutation: 98`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 568.36 | **LOC:** 851 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.1149%), Tech Debt (9.6018%)
**Top Internal Functions/Classes:**
  * `system_message` (Impact: 41.7)
  * `extract_name_value` (Impact: 20.4)
    * *Intent:* """ Return a list of (name, value) from a line of the form "name=value ...". :Exception: `NameValueE...
  * `extract_options` (Impact: 14.4)
  * `get_stylesheet_list` (Impact: 13.4)
    * *Intent:* # Return 'stylesheet' or 'stylesheet_path' arguments as list. # # The original settings arguments ar...
  * `relative_path` (Impact: 13.0)
    * *Intent:* """ Build and return a path to `target`, relative to `source` (both files). The return value is a `s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 127`, `args: 39`, `func_start: 39`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 90`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 45`, `import: 18`
* *Defense:* `safety: 20`, `doc: 46`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, collections.abc, docutils, docutils.frontend, docutils.nodes, docutils.utils, docutils.utils._typing, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 548.98 | **LOC:** 856 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.761%), Tech Debt (9.1852%)
**Top Internal Functions/Classes:**
  * `publish_programmatically` (Impact: 35.4)
  * `publish` (Impact: 29.1)
  * `publish_cmdline` (Impact: 28.7)
    * *Intent:* # TODO: or not to do? cf. https://clig.dev/#help # # Display output on success, but keep it brief. #...
  * `__init__` (Impact: 24.8)
  * `set_destination` (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 53 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 81`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 72`, `planned_debt: 1`
* *Architecture:* `io: 9`, `api: 37`, `import: 11`
* *Defense:* `safety: 15`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.829
  * `Choke Point (Betweenness):` 0.001172 | `Ripple Effect (Closeness):` 0.063415
  * `Imports (Out-Degree: 2):` __future__, docutils, docutils.frontend, docutils.nodes, docutils.readers, locale, os, pprint...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/parsers/rst/directives/tables.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 500.52 | **LOC:** 524 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.441%), Tech Debt (21.7227%)
**Top Internal Functions/Classes:**
  * `build_table_from_list` (Impact: 23.7)
  * `check_list_content` (Impact: 22.6)
  * `run` (Impact: 21.7)
  * `get_csv_data` (Impact: 20.4)
    * *Intent:* """ Get CSV data from the directive content, from an external file, or from a URL reference. """
  * `check_table_dimensions` (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 83`, `args: 18`, `func_start: 18`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 121`, `planned_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 22`, `import: 11`
* *Defense:* `safety: 15`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, csv, docutils, docutils.io, docutils.parsers.rst, docutils.parsers.rst.directives.misc, docutils.utils, urllib.error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/tableparser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 497.08 | **LOC:** 544 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.6197%), Tech Debt (12.0278%)
**Top Internal Functions/Classes:**
  * `check_columns` (Impact: 19.4)
    * *Intent:* """ Check for text in column margins and text overflow in the last column. Raise TableMarkupError if...
  * `scan_left` (Impact: 15.6)
    * *Intent:* """ Noting column boundaries, look for the bottom-left corner of the cell. It must line up with the ...
  * `find_head_body_sep` (Impact: 15.0)
    * *Intent:* """Look for a head/body row separator line; store the line index."""
  * `structure_from_cells` (Impact: 14.7)
    * *Intent:* """ From the data collected by `scan_cell()`, convert to the final data structure. """
  * `parse_row` (Impact: 14.7)
    * *Intent:* """ Given the text `lines` of a row, parse it and append to `self.table`. The row is parsed accordin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 63`, `args: 21`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 116`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 24`, `import: 5`
* *Defense:* `safety: 6`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, docutils, docutils.utils, re, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/io.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 411.32 | **LOC:** 717 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.1003%), Tech Debt (10.9517%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 35.6)
    * *Intent:* # 'wb' for binary (e.g. OpenOffice) files (see also `BinaryFileOutput`). # (Do not use binary mode (...
  * `decode` (Impact: 30.7)
    * *Intent:* """ Decode `data` if required. Return Unicode `str` instances unchanged (nothing to decode). If `sel...
  * `__init__` (Impact: 19.2)
  * `__init__` (Impact: 19.1)
  * `write` (Impact: 17.8)
    * *Intent:* """Write `data` to a single file, also return it. `data` can be a `str` or `bytes` instance. If writ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 102`, `args: 30`, `func_start: 30`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 54`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 18`, `api: 35`, `import: 11`
* *Defense:* `safety: 40`, `doc: 50`, `immutability_locks: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.373
  * `Choke Point (Betweenness):` 0.000239 | `Ripple Effect (Closeness):` 0.052701
  * `Imports (Out-Degree: 1):` __future__, codecs, docutils, docutils.nodes, locale, os, re, sys...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/html5_polyglot/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 394.78 | **LOC:** 399 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.4079%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `visit_inline` (Impact: 21.9)
    * *Intent:* # Use `supported_inline_tags` if found in class values
  * `visit_literal` (Impact: 18.8)
    * *Intent:* # <figcaption> closed in visit_figure() # use HTML5 text-level tags if matching class value found
  * `visit_topic` (Impact: 11.2)
    * *Intent:* # Use new HTML5 element <aside> or <nav> # Add class value to <body>, if there is a ToC in the docum...
  * `visit_container` (Impact: 9.3)
    * *Intent:* # If there is exactly one of the "supported block tags" in # the list of class values, use it as tag...
  * `section_title_tags` (Impact: 7.5)
    * *Intent:* # append self-link
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 206
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 64`, `args: 37`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 98`, `planned_debt: 1`, `unreferenced_by_name: 34`
* *Architecture:* `io: 1`, `api: 37`, `import: 4`
* *Defense:* `safety: 9`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, docutils, docutils.writers, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/smartquotes.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 384.6 | **LOC:** 1007 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.9912%), Tech Debt (81.9666%)
**Top Internal Functions/Classes:**
  * `educate_tokens` (Impact: 59.5)
    * *Intent:* """Return iterator that "educates" the items of `text_tokens`."""
  * `processEscapes` (Impact: 10.2)
  * `educateQuotes` (Impact: 9.8)
    * *Intent:* """ Parameter: - text string (unicode or bytes). - language (`BCP 47` language tag.) Returns: The `t...
  * `tokenize` (Impact: 6.9)
    * *Intent:* """ Parameter: String containing HTML markup. Returns: An iterator that yields the tokens comprising...
  * `smartyPants` (Impact: 4.2)
    * *Intent:* """Main function for "traditional" use."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 42`, `args: 16`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 120`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 6`, `api: 18`, `import: 7`
* *Defense:* `safety: 3`, `doc: 19`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, argparse, itertools, locale, of, re, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/transforms/frontmatter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 340.8 | **LOC:** 549 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.2671%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extract_bibliographic` (Impact: 32.0)
  * `extract_authors` (Impact: 26.1)
  * `check_compound_biblio_field` (Impact: 23.6)
    * *Intent:* # Check that the `field` body contains a single paragraph # (i.e. it must *not* be a compound elemen...
  * `authors_from_one_paragraph` (Impact: 14.8)
    * *Intent:* """Return list of Text nodes with author names in `field`. Author names must be separated by one of ...
  * `authors_from_bullet_list` (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 55`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 58`, `dead_code: 1`
* *Architecture:* `api: 18`, `import: 4`
* *Defense:* `safety: 28`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, docutils, docutils.transforms, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/roles.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 332.04 | **LOC:** 451 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5529%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `role` (Impact: 22.7)
    * *Intent:* """ Locate and return a role function from its language-dependent name, along with a list of system ...
  * `code_role` (Impact: 21.2)
  * `__call__` (Impact: 18.7)
  * `rfc_reference_role` (Impact: 18.1)
  * `raw_role` (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *Amplified Sql Injection:* 1 instances
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 75`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 76`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* `safety: 16`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.612
  * `Choke Point (Betweenness):` 0.000574 | `Ripple Effect (Closeness):` 0.024593
  * `Imports (Out-Degree: 1):` __future__, docutils, docutils.parsers.rst, docutils.parsers.rst.languages, docutils.utils.code_analyzer, warnings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/transforms/peps.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 329.4 | **LOC:** 316 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.9434%), Tech Debt (71.2814%)
**Top Internal Functions/Classes:**
  * `apply` (Impact: 51.7)
  * `mask_email` (Impact: 15.1)
    * *Intent:* """ Mask the email address in `ref` and return a replacement node. `ref` is returned unchanged if it...
  * `apply` (Impact: 12.8)
  * `visit_entry` (Impact: 11.1)
  * `visit_colspec` (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 41`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 79`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 18`, `import: 8`
* *Defense:* `safety: 13`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, docutils, docutils.transforms, os, re, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/math/mathml_elements.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 282.62 | **LOC:** 483 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.9613%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__setitem__` (Impact: 14.6)
  * `__repr__` (Impact: 10.4)
    * *Intent:* """Return full string representation."""
  * `append` (Impact: 9.7)
    * *Intent:* """Append `element` and return new "current node" (insertion point). Append as child element and set...
  * `transfer_attributes` (Impact: 9.3)
    * *Intent:* """Transfer attributes from self to other. "List values" (class, style) are appended to existing val...
  * `unindent_xml` (Impact: 7.6)
    * *Intent:* """Strip whitespace at the end of `text` and `tail` attributes... to revert changes made by the `ind...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 74`, `args: 20`, `func_start: 20`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`
* *Architecture:* `api: 45`, `import: 3`
* *Defense:* `safety: 9`, `doc: 46`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.269
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004878
  * `Imports (Out-Degree: 0):` __future__, mathml_elements, numbers, xml.etree.ElementTree
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 0.149** (Bridge: 0.0015 * Flux: 99.9993%)
- `docutils-0.22.4/docutils/core.py` -> **Severity: 0.117** (Bridge: 0.0012 * Flux: 99.9996%)
- `docutils-0.22.4/docutils/parsers/rst/directives/misc.py` -> **Severity: 0.097** (Bridge: 0.001 * Flux: 100.0%)
- `docutils-0.22.4/docutils/utils/code_analyzer.py` -> **Severity: 0.096** (Bridge: 0.001 * Flux: 100.0%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 0.067** (Bridge: 0.0007 * Flux: 99.9997%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 7.414** (Embedded: 0.0794 * Error Risk: 93.3429%)
- `docutils-0.22.4/docutils/utils/_typing.py` -> **Severity: 5.809** (Embedded: 0.0697 * Error Risk: 83.361%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 5.775** (Embedded: 0.0648 * Error Risk: 89.1047%)
- `docutils-0.22.4/docutils/core.py` -> **Severity: 5.627** (Embedded: 0.0634 * Error Risk: 88.7287%)
- `docutils-0.22.4/docutils/io.py` -> **Severity: 4.336** (Embedded: 0.0527 * Error Risk: 82.2668%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 5613.71** (Blast Radius: 86.425 * Doc Risk: 64.9547%)
- `docutils-0.22.4/docutils/utils/_typing.py` -> **Severity: 5220.4** (Blast Radius: 52.204 * Doc Risk: 100.0%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 4175.831** (Blast Radius: 56.672 * Doc Risk: 73.6842%)
- `docutils-0.22.4/docutils/core.py` -> **Severity: 3211.505** (Blast Radius: 34.829 * Doc Risk: 92.2078%)
- `docutils-0.22.4/docutils/io.py` -> **Severity: 1652.067** (Blast Radius: 58.373 * Doc Risk: 28.3019%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
