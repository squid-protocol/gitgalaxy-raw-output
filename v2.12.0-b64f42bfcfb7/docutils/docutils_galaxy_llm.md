# ARCHITECTURAL_BRIEF: docutils
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 466 analyzed artifact(s), 72500 LOC.
- **Load-bearing artifact:** `docutils-0.22.4/docutils/utils/__init__.py` -- 121 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` -- pulls in 25 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `docutils-0.22.4/docutils/parsers/rst/states.py` at magnitude 3733.7 (structural weight, not risk).
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
| Total Artifacts | 673 |
| Analyzed Artifacts (Scanned) | 466 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 207 |
| Total LOC | 72500 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.42 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0342 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8424 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 349 | 45414 | 74.9% |
| CSS | 43 | 4643 | 9.2% |
| PLAINTEXT | 39 | 0 | 8.4% |
| HTML | 22 | 20792 | 4.7% |
| XML | 6 | 0 | 1.3% |
| JAVASCRIPT | 3 | 1548 | 0.6% |
| SHELL | 1 | 81 | 0.2% |
| MARKDOWN | 1 | 0 | 0.2% |
| CSV | 1 | 5 | 0.2% |
| MAKEFILE | 1 | 17 | 0.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 465 |
| utf-16-be | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 29%, Compute Cores Files 24%, Data / Markup / Trivial 22%, Parameter Forwarders Files 7%, Generic / Templated Code Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 426 | 91.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 40 | 8.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 207*

**Composition by Extension & Reason:**
- `.rst`: 124x Excluded (Unsupported Extension: '.rst')
- `.el`: 24x Excluded (Unsupported Extension: '.el')
- `.tex`: 21x Excluded (Unsupported Extension: '.tex')
- `.odt`: 14x Excluded (Explicitly Denied Extension: '.odt')
- `.html`: 1x Excluded (Saturation: Line 61 exceeds 500 chars), 1x Excluded (Saturation: Line 15 exceeds 500 chars), 1x Excluded (Saturation: Line 22 exceeds 500 chars)
- `no_extension`: 4x Unsupported Format (.undeterminable)
- `.conf`: 3x Excluded (Unsupported Extension: '.conf')
- `.css`: 3x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.sty`: 1x Excluded (Unsupported Extension: '.sty')
- `.txt`: 1x Excluded (Machine-Generated Source Code Signature: 26 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.xml`: 1x Excluded (Static Asset Blob without Intent: 1770 LOC)
- `.man`: 1x Excluded (Unsupported Extension: '.man')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.1 | 13.3 | 5.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.0 | 50.8 | 53.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.4 | 3.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 15.6 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 13.5 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 47.7 | 33.9 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 409 | 182 | 2 | `docutils-0.22.4/test/test_nodes.py` |
| cleanup | 41 | 11 | 0 | `docutils-0.22.4/docutils/utils/math/latex2mathml.py` |
| guards | 1336 | 122 | 5 | `docutils-0.22.4/docutils/nodes.py` |
| danger | 1478 | 237 | 4 | `docutils-0.22.4/docutils/nodes.py` |
| concurrency | 48 | 13 | 0 | `docutils-0.22.4/docutils/nodes.py` |
| connectivity | 4567 | 251 | 16 | `docutils-0.22.4/test/functional/expected/standalone_rst_html5.html` |
| io | 2448 | 204 | 5 | `docutils-0.22.4/test/functional/expected/standalone_rst_html5.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 16 | 4 | 0 | `docutils-0.22.4/docutils/utils/math/tex2mathml_extern.py` |
| time | 4 | 4 | 0 | `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` |
| serialization | 2 | 2 | 0 | `docutils-0.22.4/test/test_pickle.py` |
| regex | 116 | 27 | 0 | `docutils-0.22.4/docutils/parsers/rst/states.py` |
| events | 113 | 31 | 0 | `docutils-0.22.4/docutils/frontend.py` |
| tests | 1175 | 152 | 5 | `docutils-0.22.4/test/test_nodes.py` |
| docs | 4370 | 322 | 25 | `docutils-0.22.4/docutils/nodes.py` |
| debt | 325 | 79 | 1 | `docutils-0.22.4/docutils/writers/latex2e/__init__.py` |
| mutation | 26323 | 363 | 87 | `docutils-0.22.4/test/functional/expected/mathematics_mathml_blahtexml.html` |
| dead_code | 870 | 191 | 2 | `docutils-0.22.4/docutils/writers/manpage.py` |
| credential | 2 | 2 | 0 | `docutils-0.22.4/test/test_writers/test_html5_polyglot.py` |
| threat | 34 | 6 | 0 | `docutils-0.22.4/docutils/utils/punctuation_chars.py` |
| ml_ai | 6995 | 11 | 0 | `docutils-0.22.4/test/functional/expected/mathematics_mathml.html` |
| ui | 387 | 43 | 0 | `docutils-0.22.4/test/functional/expected/standalone_rst_html5.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `docutils-0.22.4/test/functional/expected/standalone_rst_html5.html` (Hits: 609)
- `docutils-0.22.4/test/functional/expected/standalone_rst_html4css1.html` (Hits: 452)
- `docutils-0.22.4/test/functional/expected/mathematics_mathml.html` (Hits: 250)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`docutils-0.22.4/docutils/utils/__init__.py`) — 121 inbound connections
2. **__init__.py** (`docutils-0.22.4/docutils/parsers/__init__.py`) — 115 inbound connections
3. **frontend.py** (`docutils-0.22.4/docutils/frontend.py`) — 109 inbound connections
4. **__init__.py** (`docutils-0.22.4/docutils/parsers/rst/__init__.py`) — 101 inbound connections
5. **__init__.py** (`docutils-0.22.4/docutils/__init__.py`) — 90 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`docutils-0.22.4/docutils/writers/odf_odt/__init__.py`) — 25 outbound dependencies
2. **buildhtml.py** (`docutils-0.22.4/tools/buildhtml.py`) — 17 outbound dependencies
3. **nodes.py** (`docutils-0.22.4/docutils/nodes.py`) — 16 outbound dependencies
4. **__init__.py** (`docutils-0.22.4/docutils/utils/__init__.py`) — 15 outbound dependencies
5. **_html_base.py** (`docutils-0.22.4/docutils/writers/_html_base.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `handle_cmd` **(Many-Argument Workhorses)** (@ `docutils-0.22.4/docutils/utils/math/latex2mathml.py`) -> Impact: **165.3** | LOC: 306
  * *Intent:* # math(msub(mi('x'), mtext('in'))) # >>> parse_latex_math(math(), '2⌘') # Traceback (most recent call last): # docutils.utils.math.MathError: Unsuppor...
- `phrase_ref` **(Many-Argument Workhorses)** (@ `docutils-0.22.4/docutils/parsers/rst/states.py`) -> Impact: **83.1** | LOC: 74
  * *Intent:* # `text` is ignored (since 0.16) match = self.patterns.embedded_link.search(escaped) if match: # embedded <URI> or <alias_> text = escaped[:match.star...
- `from_string` **(Many-Argument Workhorses)** (@ `docutils-0.22.4/docutils/utils/_roman_numerals.py`) -> Impact: **69.1** | LOC: 101
  * *Intent:* """Create a ``RomanNumeral`` from a well-formed string representation. Returns ``RomanNumeral`` or raises ``InvalidRomanNumeralError``. >>> answer = R...
- `__init__` **(Many-Argument Workhorses)** (@ `docutils-0.22.4/docutils/writers/latex2e/__init__.py`) -> Impact: **67.8** | LOC: 195
- `parse_directive_block` **(Many-Argument Workhorses)** (@ `docutils-0.22.4/docutils/parsers/rst/states.py`) -> Impact: **63.5** | LOC: 45
- `starttag` **(Many-Argument Workhorses)** (@ `docutils-0.22.4/docutils/writers/_html_base.py`) -> Impact: **61.5** | LOC: 65
  * *Intent:* """ Construct and return a start tag given a node (id & class attributes are extracted), tag name, and optional attributes. """
- `findall` **(Many-Argument Workhorses)** (@ `docutils-0.22.4/docutils/nodes.py`) -> Impact: **59.9** | LOC: 87
- `keys` **(Compute Cores)** (@ `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js`) -> Impact: **59.7** | LOC: 62
  * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
- `keys` **(Compute Cores)** (@ `docutils-0.22.4/test/functional/expected/ui/default/slides.js`) -> Impact: **59.7** | LOC: 62
  * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
- `keys` **(Compute Cores)** (@ `docutils-0.22.4/test/functional/expected/ui/small-black/slides.js`) -> Impact: **59.7** | LOC: 62
  * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `docutils-0.22.4/docutils` | 8 | 4858.14 | 34.24% | 10.64% |
| `docutils-0.22.4/docutils/parsers/rst` | 4 | 4694.02 | 38.89% | 4.64% |
| `docutils-0.22.4/docutils/utils/math` | 8 | 4420.98 | 28.97% | 5.81% |
| `docutils-0.22.4/docutils/writers` | 6 | 4030.2 | 37.64% | 56.95% |
| `docutils-0.22.4/docutils/writers/odf_odt` | 3 | 3764.32 | 67.86% | 2.78% |
| `docutils-0.22.4/docutils/writers/latex2e` | 1 | 3479.76 | 71.54% | 13.94% |
| `docutils-0.22.4/docutils/transforms` | 9 | 2350.8 | 38.41% | 26.56% |
| `docutils-0.22.4/test/functional/expected` | 23 | 2237.51 | 0.15% | 0.0% |
| `docutils-0.22.4/docutils/parsers/rst/directives` | 9 | 1981.32 | 40.8% | 13.2% |
| `docutils-0.22.4/test` | 20 | 1815.1 | 13.09% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `docutils-0.22.4/docutils/writers/html4css1/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/writers/html5_polyglot/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/writers/manpage.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/writers/docutils_xml.py` -> **99.5033%** Exposure
- `docutils-0.22.4/docutils/parsers/rst/languages/pl.py` -> **97.8918%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `docutils-0.22.4/docutils/languages/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/docutils_xml.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/recommonmark_wrapper.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/rst/directives/body.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/rst/directives/images.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `docutils-0.22.4/docutils/writers/manpage.py` -> **164** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/docutils/writers/html4css1/__init__.py` -> **80** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/test/test_nodes.py` -> **59** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/docutils/writers/html5_polyglot/__init__.py` -> **34** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/test/test_utils/test__init__.py` -> **26** Orphaned Functions | **2** Duplicates

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
- **Unknown Dependencies:** `1458` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `docutils-0.22.4/docutils/parsers/rst/states.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.425)
- **Top Global Matches:** file_cluster_4: 6.425, file_cluster_12: 9.504, file_cluster_15: 10.85
- **Magnitude:** 3733.7 | **LOC:** 3267 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 3.098; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.8%)
- **Documentation Coverage:** 51.7986% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `phrase_ref` **(Many-Argument Workhorses)** (Impact: 83.1)
    * *Intent:* # `text` is ignored (since 0.16) match = self.patterns.embedded_link.search(escaped) if match: # emb...
  * `parse_directive_block` **(Many-Argument Workhorses)** (Impact: 63.5)
  * `nested_parse` **(Many-Argument Workhorses)** (Impact: 50.2)
  * `interpreted_or_phrase_ref` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `parse_enumerator` **(Many-Argument Workhorses)** (Impact: 40.7)
    * *Intent:* """ Analyze an enumerator and return the results. :Return: - the enumerator format ('period', 'paren...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 537 instances
* *State Mutation (weighted view):* 1778
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 642`, `structural_boundaries: 433`, `args: 141`, `func_start: 141`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 704`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `api: 162`, `import: 18`
* *Defense:* `safety: 72`, `doc: 126`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.098
  * `Choke Point (Betweenness):` 0.000539 | `Ripple Effect (Closeness):` 0.115284
  * `Imports (Out-Degree: 6):` __future__, docutils, docutils.nodes, docutils.parsers.rst, docutils.statemachine, docutils.utils, docutils.utils._roman_numerals, re...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.499)
- **Top Global Matches:** file_cluster_5: 6.499, file_cluster_12: 7.574, file_cluster_0: 9.767
- **Magnitude:** 3556.5 | **LOC:** 3462 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.891; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.5%), Guard Balance (formerly Safety Score) (80.7%), Connectivity (formerly Api Exposure) (77.4%)
- **Documentation Coverage:** 94.8718% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_field_element` **(Many-Argument Workhorses)** (Impact: 50.7)
  * `generate_image` **(Many-Argument Workhorses)** (Impact: 46.5)
  * `visit_image` **(Many-Argument Workhorses)** (Impact: 32.6)
    * *Intent:* # Capture the image file. source = node['uri'] uri_parts = urllib.parse.urlparse(source) if uri_part...
  * `update_stylesheet` **(Many-Argument Workhorses)** (Impact: 27.0)
    * *Intent:* """Update xml style sheet element with language and region/country."""
  * `add_header_footer` **(Compute Cores)** (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 488 instances
* *State Mutation (weighted view):* 1884
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 401`, `structural_boundaries: 496`, `args: 276`, `func_start: 276`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 908`, `dead_code: 3`, `planned_debt: 6`
* *Architecture:* `io: 19`, `api: 275`, `import: 26`
* *Defense:* `safety: 34`, `doc: 18`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.891
  * `Choke Point (Betweenness):` 6.1e-05 | `Ripple Effect (Closeness):` 0.002151
  * `Imports (Out-Degree: 8):` .pygmentsformatter, __future__, configparser, copy, docutils, docutils.parsers.rst.directives.images, docutils.readers, docutils.transforms...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/latex2e/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.464)
- **Top Global Matches:** file_cluster_5: 7.464, file_cluster_12: 8.489, file_cluster_0: 10.286
- **Magnitude:** 3479.76 | **LOC:** 3418 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.891; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.9%), Complexity Load (formerly Cognitive Load) (71.5%), Connectivity (formerly Api Exposure) (70.0%)
- **Documentation Coverage:** 87.5764% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 67.8)
  * `encode` **(Many-Argument Workhorses)** (Impact: 49.3)
    * *Intent:* """Return text with 'problematic' characters escaped. * Escape the special printing characters ``# $...
  * `visit_literal_block` **(Many-Argument Workhorses)** (Impact: 45.5)
    * *Intent:* """Render a literal block. Corresponding rST elements: literal block, parsed-literal, code. """
  * `depart_docinfo_item` **(Defensive Guards)** (Impact: 36.7)
  * `visit_entry` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* # cell separation if self.active_table.get_entry_number() == 0: self.insert_additional_table_colum_d...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 504 instances
* *State Mutation (weighted view):* 1749
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 558`, `structural_boundaries: 406`, `args: 245`, `func_start: 245`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 741`, `dead_code: 9`, `planned_debt: 30`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 246`, `import: 9`
* *Defense:* `safety: 95`, `doc: 56`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.891
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.002151
  * `Imports (Out-Degree: 6):` __future__, docutils, docutils.transforms, docutils.utils._roman_numerals, docutils.utils.math, pathlib, re, string...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/utils/math/math2html.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.281)
- **Top Global Matches:** file_cluster_0: 7.281, file_cluster_12: 7.675, file_cluster_15: 8.034
- **Magnitude:** 2837.08 | **LOC:** 3167 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.694; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Complexity Load (formerly Cognitive Load) (69.3%)
- **Documentation Coverage:** 99.6409% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readoption` **(Defensive Guards)** (Impact: 18.6)
  * `readtag` **(Compute Cores)** (Impact: 16.8)
  * `writepos` **(Compute Cores)** (Impact: 16.6)
  * `parseformula` **(Compute Cores)** (Impact: 15.6)
  * `read` **(Compute Cores)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 302 instances
* *State Mutation (weighted view):* 1114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 447`, `structural_boundaries: 995`, `args: 305`, `func_start: 293`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 3`, `state_mutation: 510`, `planned_debt: 9`, `unreferenced_by_name: 18`
* *Architecture:* `io: 10`, `api: 337`, `import: 5`
* *Defense:* `safety: 17`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, docutils.utils.math, pathlib, sys, unicodedata
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/_html_base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.54)
- **Top Global Matches:** file_cluster_5: 6.54, file_cluster_12: 8.92, file_cluster_7: 10.462
- **Magnitude:** 2379.92 | **LOC:** 1896 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 1.087; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Connectivity (formerly Api Exposure) (80.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.1923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `starttag` **(Many-Argument Workhorses)** (Impact: 61.5)
    * *Intent:* """ Construct and return a start tag given a node (id & class attributes are extracted), tag name, a...
  * `visit_math` **(Many-Argument Workhorses)** (Impact: 45.1)
    * *Intent:* # Also called from `visit_math_block()`: is_block = isinstance(node, nodes.math_block) format = self...
  * `visit_image` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* # reference/embed images (still images and videos) uri = node['uri'] alt = node.get('alt', uri) mime...
  * `prepare_svg` **(Many-Argument Workhorses)** (Impact: 29.0)
    * *Intent:* # Parse SVG source `code` (ignoring comments and preamble code), # add relevant attributes from `nod...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 26.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 337 instances
* *State Mutation (weighted view):* 1245
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 340`, `args: 204`, `func_start: 204`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 571`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 207`, `import: 16`
* *Defense:* `safety: 65`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.000166 | `Ripple Effect (Closeness):` 0.006452
  * `Imports (Out-Degree: 9):` __future__, base64, docutils, docutils.parsers.rst.directives, docutils.parsers.rst.directives.images, docutils.transforms, docutils.utils.math, mimetypes...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/nodes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.593)
- **Top Global Matches:** file_cluster_5: 6.593, file_cluster_12: 10.005, file_cluster_7: 10.554
- **Magnitude:** 1873.72 | **LOC:** 3342 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **16**; blast radius 126.024; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (98.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 64.9547% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findall` **(Many-Argument Workhorses)** (Impact: 59.9)
  * `set_duplicate_name_id` **(Many-Argument Workhorses)** (Impact: 58.7)
  * `set_id` **(Many-Argument Workhorses)** (Impact: 42.7)
  * `validate_content` **(Defensive Guards)** (Impact: 32.2)
  * `pformat` **(Defensive Guards)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 609
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 549`, `args: 170`, `func_start: 170`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 251`, `dead_code: 3`, `planned_debt: 9`
* *Architecture:* `io: 5`, `api: 286`, `import: 18`
* *Defense:* `safety: 99`, `doc: 214`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 126.024
  * `Choke Point (Betweenness):` 0.001463 | `Ripple Effect (Closeness):` 0.267093
  * `Imports (Out-Degree: 4):` __future__, collections, collections.abc, docutils.frontend, docutils.transforms, docutils.utils, docutils.utils._typing, os...
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/manpage.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.945)
- **Top Global Matches:** file_cluster_5: 6.945, file_cluster_12: 10.746, file_cluster_7: 11.1
- **Magnitude:** 1349.66 | **LOC:** 1354 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.694; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 94.4304% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `list_start` **(Stateful Encapsulated Methods)** (Impact: 30.8)
  * `astext` **(Compute Cores)** (Impact: 22.9)
    * *Intent:* """Return the final formatted document as a string."""
  * `depart_document` **(Compute Cores)** (Impact: 15.2)
  * `_visit_reference_with_macro` **(Stateful Encapsulated Methods)** (Impact: 13.3)
    * *Intent:* % insert_URI_breakpoints(node['refuri'])) # elif 'refid' in node: # use UR/UE or MT/ME if 'refuri' i...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 537
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 297`, `args: 203`, `func_start: 203`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 275`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 4`, `unreferenced_by_name: 164`
* *Architecture:* `api: 196`, `import: 5`
* *Defense:* `safety: 14`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, docutils, docutils.utils._roman_numerals, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/html4css1/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.71)
- **Top Global Matches:** file_cluster_5: 7.71, file_cluster_12: 8.946, file_cluster_0: 9.265
- **Magnitude:** 1157.46 | **LOC:** 965 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.694; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.8%), Guard Balance (formerly Safety Score) (82.9%)
- **Documentation Coverage:** 97.8836% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_image` **(Defensive Guards)** (Impact: 58.6)
  * `should_be_compact_paragraph` **(Defensive Guards)** (Impact: 29.2)
    * *Intent:* # Omit <p> tags to produce visually compact lists (less vertical # whitespace) as CSS styling requir...
  * `visit_field_list` **(Defensive Guards)** (Impact: 20.4)
  * `visit_literal` **(Compute Cores)** (Impact: 18.8)
    * *Intent:* # use <tt> (not supported by HTML5), # cater for limited styling options in CSS1 using hard-coded NB...
  * `footnote_backrefs` **(Compute Cores)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 158 instances
* *State Mutation (weighted view):* 585
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 160`, `args: 95`, `func_start: 95`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 269`, `dead_code: 3`, `planned_debt: 2`, `unreferenced_by_name: 80`
* *Architecture:* `io: 14`, `api: 97`, `import: 6`
* *Defense:* `safety: 35`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, docutils, docutils.writers, docutils.writers._html_base, os.path, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/statemachine.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.664)
- **Top Global Matches:** file_cluster_12: 7.664, file_cluster_5: 7.785, file_cluster_7: 10.26
- **Magnitude:** 1123.42 | **LOC:** 1535 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **5**; blast radius 5.129; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (81.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%)
- **Documentation Coverage:** 39.8876% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_indented` **(Many-Argument Workhorses)** (Impact: 58.5)
  * `run` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `check_line` **(Many-Argument Workhorses)** (Impact: 31.0)
    * *Intent:* """ Examine one line of input for a transition match & execute its method. Parameters: - `context`: ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 17.2)
  * `get_2D_block` **(Many-Argument Workhorses)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 130 instances
* *State Mutation (weighted view):* 443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 222`, `args: 92`, `func_start: 92`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 183`
* *Architecture:* `io: 15`, `api: 103`, `import: 5`
* *Defense:* `safety: 57`, `doc: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.129
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.128204
  * `Imports (Out-Degree: 1):` __future__, docutils, re, sys, unicodedata
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/utils/math/latex2mathml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.8)
- **Top Global Matches:** file_cluster_6: 5.8, file_cluster_8: 11.668, file_cluster_4: 13.089
- **Magnitude:** 990.56 | **LOC:** 1253 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.694; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.6%)
- **Documentation Coverage:** 34.375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_cmd` **(Many-Argument Workhorses)** (Impact: 165.3)
    * *Intent:* # math(msub(mi('x'), mtext('in'))) # >>> parse_latex_math(math(), '2⌘') # Traceback (most recent cal...
  * `parse_latex_math` **(Many-Argument Workhorses)** (Impact: 50.2)
    * *Intent:* # Test: # >>> tex_optarg(' [optional argument] after whitespace') # ('optional argument', ' after wh...
  * `handle_script_or_limit` **(Defensive Guards)** (Impact: 37.5)
    * *Intent:* # >>> handle_math_alphabet('mathrm', math(), '\\alpha') # (math(mi('α', mathvariant='normal')), '') ...
  * `handle_math_alphabet` **(Defensive Guards)** (Impact: 23.2)
    * *Intent:* # (mover(mo('_', accent='true'), switch=True, accent='false'), '{981}') # >>> handle_cmd('bar', math...
  * `tex_group` **(Compute Cores)** (Impact: 14.2)
    * *Intent:* # Test: # # >>> tex_token('{opening bracket of group}') # ('{', 'opening bracket of group}') # >>> t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 606
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 86`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 220`, `dead_code: 1`, `planned_debt: 5`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 4`
* *Defense:* `safety: 13`, `doc: 13`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` docutils.utils.math, docutils.utils.math.mathml_elements, re, unicodedata
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/transforms/references.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.243)
- **Top Global Matches:** file_cluster_6: 8.243, file_cluster_8: 13.599, file_cluster_4: 14.192
- **Magnitude:** 885.14 | **LOC:** 991 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **3**; blast radius 1.526; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Connectivity (formerly Api Exposure) (77.4%)
- **Documentation Coverage:** 81.4815% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `apply` **(Defensive Guards)** (Impact: 38.5)
  * `visit_reference` **(Defensive Guards)** (Impact: 33.7)
  * `resolve_indirect_target` **(Defensive Guards)** (Impact: 33.3)
  * `resolve_indirect_references` **(Defensive Guards)** (Impact: 29.6)
  * `apply` **(Defensive Guards)** (Impact: 25.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 141 instances
* *State Mutation (weighted view):* 475
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 102`, `args: 26`, `func_start: 26`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 193`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `api: 36`, `import: 3`
* *Defense:* `safety: 53`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.526
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.021505
  * `Imports (Out-Degree: 3):` __future__, docutils, docutils.transforms
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/frontend.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.431)
- **Top Global Matches:** file_cluster_5: 7.431, file_cluster_12: 8.261, file_cluster_0: 9.851
- **Magnitude:** 753.16 | **LOC:** 1179 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **109** in-repo importer(s); it depends on **13**; blast radius 52.738; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.6%)
- **Documentation Coverage:** 73.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `populate_from_components` **(Compute Cores)** (Impact: 22.3)
  * `make_paths_absolute` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `validate_encoding` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `check_args` **(Generic / Templated Code)** (Impact: 18.2)
    * *Intent:* # provisional: argument handling will change, see RELEASE_NOTES source = destination = None if args:...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 158`, `args: 40`, `func_start: 40`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 109`, `planned_debt: 2`
* *Architecture:* `io: 15`, `api: 42`, `import: 16`
* *Defense:* `safety: 38`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 52.738
  * `Choke Point (Betweenness):` 0.001021 | `Ripple Effect (Closeness):` 0.284711
  * `Imports (Out-Degree: 3):` __future__, codecs, collections.abc, configparser, docutils, docutils.io, optparse, os...
  * `Imported By (In-Degree: 109):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/parsers/rst/directives/misc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.488)
- **Top Global Matches:** file_cluster_4: 7.488, file_cluster_12: 9.263, file_cluster_9: 9.34
- **Magnitude:** 623.02 | **LOC:** 691 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 1.368; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%), Connectivity (formerly Api Exposure) (64.6%)
- **Documentation Coverage:** 55.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Defensive Guards)** (Impact: 25.9)
  * `run` **(Defensive Guards)** (Impact: 23.9)
    * *Intent:* % ((states.Inliner.simplename,) * 2)) """Dynamically create and register a custom interpreted text r...
  * `read_file` **(Defensive Guards)** (Impact: 16.2)
    * *Intent:* """Read text file at `path`. Clip and return content. Provisional. """
  * `as_literal_block` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* """Return list with literal_block containing `text`. Provisional """
  * `parsemeta` **(Defensive Guards)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *State Mutation (weighted view):* 383
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 113`, `args: 19`, `func_start: 19`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 161`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 31`, `import: 12`
* *Defense:* `safety: 31`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.000108 | `Ripple Effect (Closeness):` 0.004301
  * `Imports (Out-Degree: 8):` __future__, docutils, docutils.nodes, docutils.parsers.rst, docutils.parsers.rst.directives.body, docutils.transforms, pathlib, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/test/functional/expected/ui/default/slides.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 11.325)
- **Top Global Matches:** file_cluster_7: 11.325, file_cluster_12: 11.369, file_cluster_4: 11.788
- **Magnitude:** 599.92 | **LOC:** 559 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.792; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (89.1%), Guard Balance (formerly Safety Score) (83.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (15.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keys` **(Compute Cores)** (Impact: 59.7)
    * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
  * `go` **(Compute Cores)** (Impact: 28.9)
  * `getIncrementals` **(Compute Cores)** (Impact: 21.5)
  * `clicker` **(Compute Cores)** (Impact: 19.2)
  * `slideLabel` **(I/O & Config Routines)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 133`, `args: 30`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 4`, `state_mutation: 98`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.792
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002151
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/test/functional/expected/ui/small-black/slides.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 11.325)
- **Top Global Matches:** file_cluster_7: 11.325, file_cluster_12: 11.369, file_cluster_4: 11.788
- **Magnitude:** 599.92 | **LOC:** 559 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.792; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (89.1%), Guard Balance (formerly Safety Score) (83.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (15.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keys` **(Compute Cores)** (Impact: 59.7)
    * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
  * `go` **(Compute Cores)** (Impact: 28.9)
  * `getIncrementals` **(Compute Cores)** (Impact: 21.5)
  * `clicker` **(Compute Cores)** (Impact: 19.2)
  * `slideLabel` **(I/O & Config Routines)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 133`, `args: 30`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 4`, `state_mutation: 98`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.792
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002151
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 11.326)
- **Top Global Matches:** file_cluster_7: 11.326, file_cluster_12: 11.368, file_cluster_4: 11.786
- **Magnitude:** 598.92 | **LOC:** 559 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.1%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keys` **(Compute Cores)** (Impact: 59.7)
    * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
  * `go` **(Compute Cores)** (Impact: 28.9)
  * `getIncrementals` **(Compute Cores)** (Impact: 21.5)
  * `clicker` **(Compute Cores)** (Impact: 19.2)
  * `slideLabel` **(I/O & Config Routines)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 133`, `args: 30`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 4`, `state_mutation: 98`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.804)
- **Top Global Matches:** file_cluster_5: 6.804, file_cluster_12: 9.853, file_cluster_7: 10.391
- **Magnitude:** 568.36 | **LOC:** 851 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **121** in-repo importer(s); it depends on **15**; blast radius 46.571; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `system_message` **(Many-Argument Workhorses)** (Impact: 41.7)
  * `extract_name_value` **(Compute Cores)** (Impact: 20.4)
    * *Intent:* """ Return a list of (name, value) from a line of the form "name=value ...". :Exception: `NameValueE...
  * `extract_options` **(Defensive Guards)** (Impact: 14.4)
  * `get_stylesheet_list` **(Defensive Guards)** (Impact: 13.4)
    * *Intent:* # Return 'stylesheet' or 'stylesheet_path' arguments as list. # # The original settings arguments ar...
  * `relative_path` **(Many-Argument Workhorses)** (Impact: 13.0)
    * *Intent:* """ Build and return a path to `target`, relative to `source` (both files). The return value is a `s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 127`, `args: 39`, `func_start: 39`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 90`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 45`, `import: 18`
* *Defense:* `safety: 20`, `doc: 46`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 46.571
  * `Choke Point (Betweenness):` 0.000946 | `Ripple Effect (Closeness):` 0.288517
  * `Imports (Out-Degree: 4):` __future__, collections.abc, docutils, docutils.frontend, docutils.nodes, docutils.utils._typing, itertools, os...
  * `Imported By (In-Degree: 121):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/test/test_nodes.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.237)
- **Top Global Matches:** file_cluster_15: 5.237, file_cluster_11: 7.579, file_cluster_2: 7.837
- **Magnitude:** 555.36 | **LOC:** 1313 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.694; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (28.1%), Connectivity (formerly Api Exposure) (12.1%)
- **Documentation Coverage:** 92.2481% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_validate_content` **(I/O & Config Routines)** (Impact: 14.8)
    * *Intent:* """Check, whether an element's children fit into its content model. Return empty lists for valid ele...
  * `test_node_class_names` **(Defensive Guards)** (Impact: 7.6)
  * `test_make_id` **(Compute Cores)** (Impact: 6.2)
  * `test_set_id_custom` **(Compute Cores)** (Impact: 4.9)
    * *Intent:* # Custom prefixes. # Change settings. self.document.settings.id_prefix = 'P-' self.document.settings...
  * `test_set_id_descriptive_auto_id` **(Compute Cores)** (Impact: 4.9)
    * *Intent:* # Use name or tag-name for auto-id. # Change setting. self.document.settings.auto_id_prefix = '%' fo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 445`, `args: 64`, `func_start: 64`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 221`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 59`
* *Architecture:* `io: 1`, `api: 75`, `import: 4`
* *Defense:* `safety: 5`, `doc: 8`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` docutils, pathlib, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.191)
- **Top Global Matches:** file_cluster_0: 7.191, file_cluster_12: 8.247, file_cluster_16: 8.425
- **Magnitude:** 549.28 | **LOC:** 856 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **11**; blast radius 11.471; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.2%)
- **Documentation Coverage:** 92.2078% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `publish_programmatically` **(Many-Argument Workhorses)** (Impact: 35.4)
  * `publish` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `publish_cmdline` **(Many-Argument Workhorses)** (Impact: 28.7)
    * *Intent:* # TODO: or not to do? cf. https://clig.dev/#help # # Display output on success, but keep it brief. #...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `set_destination` **(Many-Argument Workhorses)** (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 81`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 72`, `planned_debt: 1`
* *Architecture:* `io: 9`, `api: 37`, `import: 11`
* *Defense:* `safety: 15`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.471
  * `Choke Point (Betweenness):` 0.000898 | `Ripple Effect (Closeness):` 0.073118
  * `Imports (Out-Degree: 6):` __future__, docutils, docutils.frontend, docutils.nodes, docutils.readers, locale, os, pprint...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/parsers/rst/directives/tables.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.473)
- **Top Global Matches:** file_cluster_12: 7.473, file_cluster_9: 8.023, file_cluster_15: 8.554
- **Magnitude:** 500.52 | **LOC:** 524 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.694; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%), Complexity Load (formerly Cognitive Load) (64.4%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_table_from_list` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `check_list_content` **(Defensive Guards)** (Impact: 22.6)
  * `run` **(Defensive Guards)** (Impact: 21.7)
  * `get_csv_data` **(Defensive Guards)** (Impact: 20.4)
    * *Intent:* """ Get CSV data from the directive content, from an external file, or from a URL reference. """
  * `check_table_dimensions` **(Many-Argument Workhorses)** (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 83`, `args: 18`, `func_start: 18`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 121`, `planned_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 22`, `import: 11`
* *Defense:* `safety: 15`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` __future__, csv, docutils, docutils.io, docutils.parsers.rst, docutils.parsers.rst.directives.misc, docutils.utils, urllib.error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/tableparser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.726)
- **Top Global Matches:** file_cluster_12: 7.726, file_cluster_5: 7.953, file_cluster_7: 9.334
- **Magnitude:** 497.08 | **LOC:** 544 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 1.087; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 21.9512% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_columns` **(Many-Argument Workhorses)** (Impact: 19.4)
    * *Intent:* """ Check for text in column margins and text overflow in the last column. Raise TableMarkupError if...
  * `scan_left` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* """ Noting column boundaries, look for the bottom-left corner of the cell. It must line up with the ...
  * `find_head_body_sep` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* """Look for a head/body row separator line; store the line index."""
  * `structure_from_cells` **(Defensive Guards)** (Impact: 14.7)
    * *Intent:* """ From the data collected by `scan_cell()`, convert to the final data structure. """
  * `parse_row` **(Many-Argument Workhorses)** (Impact: 14.7)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.004301
  * `Imports (Out-Degree: 2):` __future__, docutils, docutils.utils, re, sys
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/test/functional/expected/standalone_rst_html5.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.819)
- **Top Global Matches:** file_cluster_13: 6.819, file_cluster_2: 8.824, file_cluster_11: 9.262
- **Magnitude:** 413.24 | **LOC:** 1939 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.694; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (15.6%), Complexity Load (formerly Cognitive Load) (3.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buttonClick` **(State Mutators)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 1630`, `args: 149`, `func_start: 2`, `class_start: 16`
* *Risk/State:* `planned_debt: 9`, `fragile_debt: 1`
* *Architecture:* `io: 609`, `api: 371`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` minimal.css, plain.css, terms
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/io.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.501)
- **Top Global Matches:** file_cluster_5: 7.501, file_cluster_12: 8.923, file_cluster_7: 10.706
- **Magnitude:** 411.32 | **LOC:** 717 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **10**; blast radius 20.116; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.0%)
- **Documentation Coverage:** 28.3019% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 35.6)
    * *Intent:* # 'wb' for binary (e.g. OpenOffice) files (see also `BinaryFileOutput`). # (Do not use binary mode (...
  * `decode` **(Many-Argument Workhorses)** (Impact: 30.7)
    * *Intent:* """ Decode `data` if required. Return Unicode `str` instances unchanged (nothing to decode). If `sel...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `write` **(Defensive Guards)** (Impact: 17.8)
    * *Intent:* """Write `data` to a single file, also return it. `data` can be a `str` or `bytes` instance. If writ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 102`, `args: 30`, `func_start: 30`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 54`, `planned_debt: 2`
* *Architecture:* `io: 18`, `api: 35`, `import: 11`
* *Defense:* `safety: 40`, `doc: 50`, `immutability_locks: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.116
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.205143
  * `Imports (Out-Degree: 2):` __future__, codecs, docutils, docutils.nodes, locale, os, re, sys...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/writers/html5_polyglot/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.605)
- **Top Global Matches:** file_cluster_0: 6.605, file_cluster_5: 8.016, file_cluster_12: 8.599
- **Magnitude:** 394.78 | **LOC:** 399 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.694; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.4%), Guard Balance (formerly Safety Score) (79.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_inline` **(Defensive Guards)** (Impact: 21.9)
    * *Intent:* # Use `supported_inline_tags` if found in class values
  * `visit_literal` **(Compute Cores)** (Impact: 18.8)
    * *Intent:* # <figcaption> closed in visit_figure() # use HTML5 text-level tags if matching class value found
  * `visit_topic` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* # Use new HTML5 element <aside> or <nav> # Add class value to <body>, if there is a ToC in the docum...
  * `visit_container` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* # If there is exactly one of the "supported block tags" in # the list of class values, use it as tag...
  * `section_title_tags` **(Defensive Guards)** (Impact: 7.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, docutils, docutils.writers, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/smartquotes.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.669)
- **Top Global Matches:** file_cluster_4: 6.669, file_cluster_15: 8.597, file_cluster_12: 10.06
- **Magnitude:** 384.6 | **LOC:** 1007 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.694; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.6%), Guard Balance (formerly Safety Score) (77.4%)
- **Documentation Coverage:** 29.0323% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `educate_tokens` **(Many-Argument Workhorses)** (Impact: 59.5)
    * *Intent:* """Return iterator that "educates" the items of `text_tokens`."""
  * `processEscapes` **(Compute Cores)** (Impact: 10.2)
  * `educateQuotes` **(Many-Argument Workhorses)** (Impact: 9.8)
    * *Intent:* """ Parameter: - text string (unicode or bytes). - language (`BCP 47` language tag.) Returns: The `t...
  * `tokenize` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* """ Parameter: String containing HTML markup. Returns: An iterator that yields the tokens comprising...
  * `smartyPants` **(Parameter Forwarders)** (Impact: 4.2)
    * *Intent:* """Main function for "traditional" use."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 42`, `args: 16`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 120`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 6`, `api: 18`, `import: 7`
* *Defense:* `safety: 3`, `doc: 19`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, argparse, itertools, locale, re, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `docutils-0.22.4/test/test_parsers/test_rst/test_character_level_inline_markup.py` (PYTHON) | Magnitude: 37.94 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 41, state_mutation: 19, indent_spaces: 14, structural_boundaries: 13
- `docutils-0.22.4/tools/buildhtml.py` (PYTHON) | Magnitude: 0.19 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 231, structural_boundaries: 57, core_var_decl: 49, state_mutation: 47
- `docutils-0.22.4/docutils/parsers/rst/directives/parts.py` (PYTHON) | Magnitude: 101.4 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 27, state_mutation: 26, core_var_decl: 25
- `docutils-0.22.4/docutils/statemachine.py` (PYTHON) | Magnitude: 1123.42 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 674, structural_boundaries: 222, state_mutation: 183, branch: 161
- `docutils-0.22.4/test/test_writers/test_pseudoxml.py` (PYTHON) | Magnitude: 31.24 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 12, core_var_decl: 11, design_snake_case: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `docutils-0.22.4/test/test_writers/test_html4css1.py` (PYTHON) | Magnitude: 51.1 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 62, indent_spaces: 38, structural_boundaries: 21, state_mutation: 19
- `docutils-0.22.4/test/test_parsers/test_rst/test_directives/test_images.py` (PYTHON) | Magnitude: 44.74 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 73, indent_spaces: 20, structural_boundaries: 15, state_mutation: 13
- `docutils-0.22.4/test/test_parsers/test_rst/test_targets.py` (PYTHON) | Magnitude: 29.06 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 57, indent_spaces: 14, structural_boundaries: 13, state_mutation: 10
- `docutils-0.22.4/test/test_writers/test_html5_polyglot.py` (PYTHON) | Magnitude: 75.82 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 63, indent_spaces: 59, core_var_decl: 30, state_mutation: 29
- `docutils-0.22.4/test/test_utils/test__roman_numerals.py` (PYTHON) | Magnitude: 125.1 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 46, core_var_decl: 34, design_snake_case: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `docutils-0.22.4/test/test_parsers/test_rst/test_section_headers.py` (PYTHON) | Magnitude: 29.58 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 75, indent_spaces: 15, structural_boundaries: 13, state_mutation: 10
- `docutils-0.22.4/test/test_parsers/test_recommonmark/test_inline_markup.py` (PYTHON) | Magnitude: 35.52 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 73, state_mutation: 14, structural_boundaries: 13, indent_spaces: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` (JAVASCRIPT) | Magnitude: 598.92 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 441, branch: 184, structural_boundaries: 133, core_var_decl: 129
- `docutils-0.22.4/test/functional/expected/ui/default/slides.js` (JAVASCRIPT) | Magnitude: 599.92 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 441, branch: 184, structural_boundaries: 133, core_var_decl: 129
- `docutils-0.22.4/test/functional/expected/ui/small-black/slides.js` (JAVASCRIPT) | Magnitude: 599.92 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 441, branch: 184, structural_boundaries: 133, core_var_decl: 129

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `docutils-0.22.4/docutils/parsers/rst/__init__.py` -> **Severity: 0.193** (Bridge: 0.0019 * Flux: 99.9991%)
- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 0.146** (Bridge: 0.0015 * Flux: 99.9993%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 0.102** (Bridge: 0.001 * Flux: 99.9997%)
- `docutils-0.22.4/docutils/utils/__init__.py` -> **Severity: 0.095** (Bridge: 0.0009 * Flux: 100.0%)
- `docutils-0.22.4/docutils/core.py` -> **Severity: 0.09** (Bridge: 0.0009 * Flux: 99.9996%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `docutils-0.22.4/docutils/utils/__init__.py` -> **Severity: 22.734** (Embedded: 0.2885 * Error Risk: 78.7972%)
- `docutils-0.22.4/docutils/transforms/__init__.py` -> **Severity: 20.241** (Embedded: 0.2569 * Error Risk: 78.7848%)
- `docutils-0.22.4/docutils/__init__.py` -> **Severity: 18.982** (Embedded: 0.2973 * Error Risk: 63.8557%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 18.965** (Embedded: 0.2847 * Error Risk: 66.6099%)
- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 18.852** (Embedded: 0.2671 * Error Risk: 70.5836%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `docutils-0.22.4/docutils/__init__.py` -> **Severity: 14304.085** (Blast Radius: 181.185 * Doc Risk: 78.9474%)
- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 8185.851** (Blast Radius: 126.024 * Doc Risk: 64.9547%)
- `docutils-0.22.4/docutils/utils/_typing.py` -> **Severity: 4051.6** (Blast Radius: 40.516 * Doc Risk: 100.0%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 3885.957** (Blast Radius: 52.738 * Doc Risk: 73.6842%)
- `docutils-0.22.4/docutils/transforms/__init__.py` -> **Severity: 2052.421** (Blast Radius: 123.145 * Doc Risk: 16.6667%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 370 literal sites + 3 sites through wrappers = 373

- `print_mismatch` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `docutils-0.22.4/test/test_CLI.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 10592 call pairs -- scoped 36.5%, unique 0.0%, ambiguous 22.3%, external 41.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 10282 | 36.2% | 0.0% | 22.9% | 40.9% |
| javascript | 282 | 50.0% | 0.0% | 0.0% | 50.0% |
| shell | 27 | 0.0% | 0.0% | 0.0% | 100.0% |
| html | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
