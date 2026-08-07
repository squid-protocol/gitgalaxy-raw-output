# ARCHITECTURAL_BRIEF: ruamel-yaml
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/ruamel-yaml` |
| **Timestamp** | `2026-08-07T05:26:16.312964+00:00` |
| **Scan Duration** | `0.34s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 34 malicious artifacts.

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
| Total Artifacts | 42 |
| Analyzed Artifacts (Scanned) | 37 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 11964 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2581 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2362 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 21.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9849 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 34 | 11964 | 91.9% |
| PLAINTEXT | 2 | 0 | 5.4% |
| MARKDOWN | 1 | 0 | 2.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 4`
> **Architectural Drift Z-Score:** `5.747`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 13 | 35.1% |
| file_cluster_0 | 6 | 16.2% |
| file_cluster_8 | 5 | 13.5% |
| file_cluster_16 | 5 | 13.5% |
| file_cluster_11 | 5 | 13.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 8.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 94.4 | 39.4 | 37.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 84.0 | 91.0 | 77.6 |
| Tech Debt Exposure | 0.0 | 100.0 | 73.2 | 98.2 | 100.0 |
| Testing Exposure | 0.2 | 80.0 | 43.4 | 80.0 | 80.0 |
| API Exposure | 0.0 | 9.3 | 3.5 | 3.3 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 69.7 | 89.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 67.6 | 8.7 | 6.2 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.1 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 3.2 | 93.1 | 27.0 | 14.8 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ruamel.yaml-0.19.1/setup.py` (Hits: 77)
- `ruamel.yaml-0.19.1/main.py` (Hits: 29)
- `ruamel.yaml-0.19.1/compat.py` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **compat.py** (`ruamel.yaml-0.19.1/compat.py`) — 17 inbound connections
2. **error.py** (`ruamel.yaml-0.19.1/error.py`) — 12 inbound connections
3. **anchor.py** (`ruamel.yaml-0.19.1/anchor.py`) — 7 inbound connections
4. **nodes.py** (`ruamel.yaml-0.19.1/nodes.py`) — 6 inbound connections
5. **tag.py** (`ruamel.yaml-0.19.1/tag.py`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.py** (`ruamel.yaml-0.19.1/main.py`) — 25 outbound dependencies
2. **constructor.py** (`ruamel.yaml-0.19.1/constructor.py`) — 24 outbound dependencies
3. **representer.py** (`ruamel.yaml-0.19.1/representer.py`) — 17 outbound dependencies
4. **setup.py** (`ruamel.yaml-0.19.1/setup.py`) — 14 outbound dependencies
5. **comments.py** (`ruamel.yaml-0.19.1/comments.py`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `debug` (@ `ruamel.yaml-0.19.1/setup.py`) -> Impact: **407.0** | LOC: 797
- `represent_double_quoted_scalarstring` (@ `ruamel.yaml-0.19.1/representer.py`) -> Impact: **374.7** | LOC: 531
- `scan_flow_scalar` (@ `ruamel.yaml-0.19.1/scanner.py`) -> Impact: **214.2** | LOC: 370
  * *Intent:* # Note that we loose indentation rules for quoted scalars. Quoted # scalars don't need to adhere indentation because " and ' clearly # mark the beginn...
- `check_simple_key` (@ `ruamel.yaml-0.19.1/emitter.py`) -> Impact: **178.5** | LOC: 175
- `scan_anchor` (@ `ruamel.yaml-0.19.1/scanner.py`) -> Impact: **160.5** | LOC: 301
  * *Intent:* # aliases. This may lead to problems, for instance, the document: # [ *alias, value ] # can be interpteted in two ways, as # [ "value" ] # and # [ *al...
- `fetch_more_tokens` (@ `ruamel.yaml-0.19.1/scanner.py`) -> Impact: **133.5** | LOC: 487
- `analyze_scalar` (@ `ruamel.yaml-0.19.1/emitter.py`) -> Impact: **102.4** | LOC: 177
  * *Intent:* # Empty scalar is a special case. if not scalar: return ScalarAnalysis( scalar=scalar, empty=True, multiline=False, allow_flow_plain=False, allow_bloc...
- `write_double_quoted` (@ `ruamel.yaml-0.19.1/emitter.py`) -> Impact: **95.1** | LOC: 102
  * *Intent:* """ a newline, as written by self.write_indent(), might need to be escaped with a backslash as on reading this will produce a possibly unwanted space....
- `parse_node` (@ `ruamel.yaml-0.19.1/parser.py`) -> Impact: **93.9** | LOC: 158
- `scan_to_next_token` (@ `ruamel.yaml-0.19.1/scanner.py`) -> Impact: **92.7** | LOC: 191
  * *Intent:* # If we find a line break in the block context, we set the flag # `allow_simple_key` on. # The byte order mark is stripped if it's the first character...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `ruamel.yaml-0.19.1` | 35 | 49691.77 | 38.01% | 71.09% |
| `ruamel.yaml-0.19.1/clibz` | 2 | 26.3 | 5.19% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `ruamel.yaml-0.19.1/anchor.py` -> **100.0%** Exposure
- `ruamel.yaml-0.19.1/comments.py` -> **100.0%** Exposure
- `ruamel.yaml-0.19.1/docinfo.py` -> **100.0%** Exposure
- `ruamel.yaml-0.19.1/error.py` -> **100.0%** Exposure
- `ruamel.yaml-0.19.1/events.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ruamel.yaml-0.19.1/reader.py` -> **100.0%** Exposure
- `ruamel.yaml-0.19.1/error.py` -> **99.9997%** Exposure
- `ruamel.yaml-0.19.1/emitter.py` -> **99.9979%** Exposure
- `ruamel.yaml-0.19.1/tag.py` -> **99.9967%** Exposure
- `ruamel.yaml-0.19.1/parser.py` -> **99.9916%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ruamel.yaml-0.19.1/comments.py` -> **0** Orphaned Functions | **85** Duplicates
- `ruamel.yaml-0.19.1/main.py` -> **0** Orphaned Functions | **40** Duplicates
- `ruamel.yaml-0.19.1/scanner.py` -> **7** Orphaned Functions | **26** Duplicates
- `ruamel.yaml-0.19.1/events.py` -> **1** Orphaned Functions | **18** Duplicates
- `ruamel.yaml-0.19.1/error.py` -> **0** Orphaned Functions | **16** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`ruamel.yaml-0.19.1/emitter.py`** -> AI Confidence: **99.34%**
2. **`ruamel.yaml-0.19.1/composer.py`** -> AI Confidence: **99.31%**
3. **`ruamel.yaml-0.19.1/constructor.py`** -> AI Confidence: **99.31%**
4. **`ruamel.yaml-0.19.1/main.py`** -> AI Confidence: **99.31%**
5. **`ruamel.yaml-0.19.1/parser.py`** -> AI Confidence: **99.31%**
6. **`ruamel.yaml-0.19.1/reader.py`** -> AI Confidence: **99.31%**
7. **`ruamel.yaml-0.19.1/representer.py`** -> AI Confidence: **99.31%**
8. **`ruamel.yaml-0.19.1/resolver.py`** -> AI Confidence: **99.31%**
9. **`ruamel.yaml-0.19.1/scanner.py`** -> AI Confidence: **99.31%**
10. **`ruamel.yaml-0.19.1/serializer.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `236` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ruamel.yaml-0.19.1/events.py` (PYTHON) -> Cumulative Risk: **689.69**
- **Archetype:** `file_cluster_0` (Distance: 11.488 IQR)
- **Magnitude:** 188.7 | **LOC:** 267 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9855%), Safety Score (97.7097%)
- **Heaviest Functions:** `__repr__` (Impact: 22.3), `compact_repr` (Impact: 14.6), `compact_repr` (Impact: 12.4)

### 2. `ruamel.yaml-0.19.1/tokens.py` (PYTHON) -> Cumulative Risk: **680.54**
- **Archetype:** `file_cluster_0` (Distance: 14.815 IQR)
- **Magnitude:** 254.08 | **LOC:** 385 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.999%), State Flux (99.6832%), Documentation (93.0989%)
- **Heaviest Functions:** `move_old_comment` (Impact: 29.4), `move_new_comment` (Impact: 21.4), `__repr__` (Impact: 13.1)

### 3. `ruamel.yaml-0.19.1/parser.py` (PYTHON) -> Cumulative Risk: **658.1**
- **Archetype:** `file_cluster_11` (Distance: 12.931 IQR)
- **Magnitude:** 616.38 | **LOC:** 863 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9916%), Safety Score (93.0027%), Tech Debt (91.5753%)
- **Heaviest Functions:** `parse_node` (Impact: 93.9), `process_directives` (Impact: 28.1), `parse_flow_mapping_key` (Impact: 24.3)

### 4. `ruamel.yaml-0.19.1/scanner.py` (PYTHON) -> Cumulative Risk: **650.82**
- **Archetype:** `file_cluster_11` (Distance: 12.981 IQR)
- **Magnitude:** 1612.9 | **LOC:** 2391 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6328%), Tech Debt (98.2295%), Safety Score (87.5543%)
- **Heaviest Functions:** `scan_flow_scalar` (Impact: 214.2), `scan_anchor` (Impact: 160.5), `fetch_more_tokens` (Impact: 133.5)

### 5. `ruamel.yaml-0.19.1/error.py` (PYTHON) -> Cumulative Risk: **646.31**
- **Archetype:** `file_cluster_13` (Distance: 13.938 IQR)
- **Magnitude:** 238.88 | **LOC:** 329 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9997%), Safety Score (98.1798%)
- **Heaviest Functions:** `__str__` (Impact: 18.6), `__str__` (Impact: 18.6), `__str__` (Impact: 18.4)

### 6. `ruamel.yaml-0.19.1/comments.py` (PYTHON) -> Cumulative Risk: **637.36**
- **Archetype:** `file_cluster_0` (Distance: 13.407 IQR)
- **Magnitude:** 948.56 | **LOC:** 1209 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Safety Score (96.6808%), State Flux (81.4763%)
- **Heaviest Functions:** `comment_token` (Impact: 39.1), `dump_comments` (Impact: 29.9), `insert` (Impact: 28.6)

### 7. `ruamel.yaml-0.19.1/emitter.py` (PYTHON) -> Cumulative Risk: **610.26**
- **Archetype:** `file_cluster_11` (Distance: 13.484 IQR)
- **Magnitude:** 1797.58 | **LOC:** 1803 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9979%), Cognitive Load (94.3883%), Safety Score (84.0776%)
- **Heaviest Functions:** `check_simple_key` (Impact: 178.5), `analyze_scalar` (Impact: 102.4), `write_double_quoted` (Impact: 95.1)

### 8. `ruamel.yaml-0.19.1/scalarfloat.py` (PYTHON) -> Cumulative Risk: **596.04**
- **Archetype:** `file_cluster_13` (Distance: 10.597 IQR)
- **Magnitude:** 70.92 | **LOC:** 106 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Safety Score (97.5917%), State Flux (87.0574%)
- **Heaviest Functions:** `yaml_anchor` (Impact: 7.2), `__iadd__` (Impact: 5.5), `__ifloordiv__` (Impact: 5.5)

### 9. `ruamel.yaml-0.19.1/reader.py` (PYTHON) -> Cumulative Risk: **595.06**
- **Archetype:** `file_cluster_0` (Distance: 13.325 IQR)
- **Magnitude:** 248.5 | **LOC:** 278 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.8445%), Cognitive Load (84.2399%)
- **Heaviest Functions:** `__str__` (Impact: 66.2), `update` (Impact: 20.6), `_get_non_printable_regex` (Impact: 10.6)

### 10. `ruamel.yaml-0.19.1/representer.py` (PYTHON) -> Cumulative Risk: **585.77**
- **Archetype:** `file_cluster_11` (Distance: 13.213 IQR)
- **Magnitude:** 787.14 | **LOC:** 1140 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (80.0%), Verification (80.0%), State Flux (75.7873%)
- **Heaviest Functions:** `represent_double_quoted_scalarstring` (Impact: 374.7), `represent_object` (Impact: 46.5), `represent_mapping` (Impact: 32.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ruamel.yaml-0.19.1/constructor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.054 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.53 IQR)
- **Top Global Matches:** file_cluster_13: 12.054, file_cluster_11: 12.126, file_cluster_0: 12.182
- **Magnitude:** 40087.23 | **LOC:** 1725 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.5433%), Tech Debt (9.4694%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 275`, `args: 74`, `func_start: 74`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 213`, `state_mutation: 112`, `dead_code: 10`, `planned_debt: 6`
* *Architecture:* `io: 5`, `api: 80`, `import: 38`
* *Defense:* `safety: 98`, `doc: 28`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.692
  * `Choke Point (Betweenness):` 0.0411 | `Ripple Effect (Closeness):` 0.120773
  * `Imports (Out-Degree: 14):` ruamel.yaml.timestamp, typing, ruamel.yaml.compat, ruamel.yaml.scalarstring, binascii, ruamel.yaml.tag, base64, ruamel.yaml.util...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/emitter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.484 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.879 IQR)
- **Top Global Matches:** file_cluster_11: 13.484, file_cluster_0: 13.589, file_cluster_13: 13.697
- **Magnitude:** 1797.58 | **LOC:** 1803 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.3883%), Tech Debt (34.1882%)
**Top Internal Functions/Classes:**
  * `check_simple_key` (Impact: 178.5)
  * `analyze_scalar` (Impact: 102.4)
    * *Intent:* # Empty scalar is a special case. if not scalar: return ScalarAnalysis( scalar=scalar, empty=True, m...
  * `write_double_quoted` (Impact: 95.1)
    * *Intent:* """ a newline, as written by self.write_indent(), might need to be escaped with a backslash as on re...
  * `prepare_tag_prefix` (Impact: 69.4)
  * `write_plain` (Impact: 67.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 631`, `structural_boundaries: 175`, `args: 76`, `func_start: 76`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 91`, `state_mutation: 491`, `dead_code: 14`, `planned_debt: 3`, `duplicate_logic: 5`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 77`, `import: 7`
* *Defense:* `safety: 88`, `doc: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.221
  * `Choke Point (Betweenness):` 0.000595 | `Ripple Effect (Closeness):` 0.086182
  * `Imports (Out-Degree: 3):` __future__, sys, ruamel.yaml.events, ruamel.yaml.error, typing, ruamel.yaml.compat
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/scanner.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 12.981 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.213 IQR)
- **Top Global Matches:** file_cluster_11: 12.981, file_cluster_0: 13.088, file_cluster_13: 13.132
- **Magnitude:** 1612.9 | **LOC:** 2391 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5177%), Tech Debt (98.2295%)
**Top Internal Functions/Classes:**
  * `scan_flow_scalar` (Impact: 214.2)
    * *Intent:* # Note that we loose indentation rules for quoted scalars. Quoted # scalars don't need to adhere ind...
  * `scan_anchor` (Impact: 160.5)
    * *Intent:* # aliases. This may lead to problems, for instance, the document: # [ *alias, value ] # can be inter...
  * `fetch_more_tokens` (Impact: 133.5)
  * `scan_to_next_token` (Impact: 92.7)
    * *Intent:* # If we find a line break in the block context, we set the flag # `allow_simple_key` on. # The byte ...
  * `assign_eol` (Impact: 41.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 520`, `structural_boundaries: 315`, `args: 115`, `func_start: 115`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 181`, `state_mutation: 338`, `dead_code: 21`, `planned_debt: 4`, `duplicate_logic: 26`, `orphaned_logic: 7`
* *Architecture:* `io: 1`, `api: 113`, `import: 12`
* *Defense:* `safety: 54`, `doc: 6`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.336
  * `Choke Point (Betweenness):` 0.001323 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 4):` __future__, ruamel.yaml.docinfo, ruamel.yaml.tokens, typing, sys, ruamel.yaml.error, ruamel.yaml.compat, inspect
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/comments.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.407 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.999 IQR)
- **Top Global Matches:** file_cluster_0: 13.407, file_cluster_11: 13.452, file_cluster_16: 13.515
- **Magnitude:** 948.56 | **LOC:** 1209 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.8683%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `comment_token` (Impact: 39.1)
  * `dump_comments` (Impact: 29.9)
  * `insert` (Impact: 28.6)
  * `__contains__` (Impact: 27.0)
  * `_yaml_get_column` (Impact: 22.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 327`, `args: 146`, `func_start: 146`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 256`, `state_mutation: 84`, `dead_code: 15`, `planned_debt: 1`, `duplicate_logic: 85`
* *Architecture:* `io: 1`, `api: 94`, `import: 16`
* *Defense:* `safety: 71`, `doc: 40`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.523
  * `Choke Point (Betweenness):` 0.015272 | `Ripple Effect (Closeness):` 0.223545
  * `Imports (Out-Degree: 6):` copy, __future__, ruamel.yaml.anchor, .tokens, ruamel.yaml.tokens, sys, typing, collections.abc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/main.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.042 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.561 IQR)
- **Top Global Matches:** file_cluster_11: 15.042, file_cluster_0: 15.059, file_cluster_13: 15.163
- **Magnitude:** 855.24 | **LOC:** 1519 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.5273%), Tech Debt (99.9012%)
**Top Internal Functions/Classes:**
  * `Xdump_all` (Impact: 48.9)
  * `get_constructor_parser` (Impact: 25.2)
    * *Intent:* # if skip is None: # skip = [] # elif isinstance(skip, int): # skip = [skip] self.doc_infos.append(D...
  * `get_serializer_representer_emitter` (Impact: 20.2)
  * `emitter` (Impact: 19.0)
  * `teardown_output` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 213`, `args: 80`, `func_start: 80`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 235`, `state_mutation: 264`, `dead_code: 22`, `duplicate_logic: 40`
* *Architecture:* `io: 29`, `api: 86`, `import: 26`
* *Defense:* `safety: 142`, `doc: 80`, `test: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 30.052
  * `Choke Point (Betweenness):` 0.111308 | `Ripple Effect (Closeness):` 0.132275
  * `Imports (Out-Degree: 12):` io, ruamel.yaml.docinfo, ruamel.yaml.tokens, ruamel.yaml.dumper, typing, ruamel.yaml.events, importlib, ruamel.yaml.compat...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/representer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.213 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.573 IQR)
- **Top Global Matches:** file_cluster_11: 13.213, file_cluster_13: 13.258, file_cluster_0: 13.278
- **Magnitude:** 787.14 | **LOC:** 1140 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.516%), Tech Debt (65.1355%)
**Top Internal Functions/Classes:**
  * `represent_double_quoted_scalarstring` (Impact: 374.7)
  * `represent_object` (Impact: 46.5)
  * `represent_mapping` (Impact: 32.8)
  * `represent_data` (Impact: 24.1)
  * `represent_float` (Impact: 18.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 182`, `args: 59`, `func_start: 59`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 146`, `state_mutation: 78`, `dead_code: 14`, `planned_debt: 2`, `duplicate_logic: 7`
* *Architecture:* `api: 63`, `import: 18`
* *Defense:* `safety: 103`, `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.454
  * `Choke Point (Betweenness):` 0.022063 | `Ripple Effect (Closeness):` 0.129274
  * `Imports (Out-Degree: 10):` __future__, ruamel.yaml.anchor, base64, ruamel.yaml.scalarfloat, copyreg, ruamel.yaml.timestamp, typing, ruamel.yaml.comments...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 12.931 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.16 IQR)
- **Top Global Matches:** file_cluster_11: 12.931, file_cluster_13: 12.997, file_cluster_0: 13.038
- **Magnitude:** 616.38 | **LOC:** 863 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.0757%), Tech Debt (91.5753%)
**Top Internal Functions/Classes:**
  * `parse_node` (Impact: 93.9)
  * `process_directives` (Impact: 28.1)
  * `parse_flow_mapping_key` (Impact: 24.3)
  * `distribute_comment` (Impact: 21.7)
    * *Intent:* # ToDo, look at indentation of the comment to determine attachment
  * `parse_block_mapping_value` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 142`, `args: 41`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 179`, `dead_code: 9`, `planned_debt: 2`, `duplicate_logic: 5`, `orphaned_logic: 6`
* *Architecture:* `api: 45`, `import: 10`
* *Defense:* `safety: 12`, `doc: 4`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.459
  * `Choke Point (Betweenness):` 0.001587 | `Ripple Effect (Closeness):` 0.086182
  * `Imports (Out-Degree: 7):` __future__, ruamel.yaml.tokens, typing, ruamel.yaml.events, ruamel.yaml.error, ruamel.yaml.comments, ruamel.yaml.compat, ruamel.yaml.scanner...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.088 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.441 IQR)
- **Top Global Matches:** file_cluster_0: 13.088, file_cluster_13: 13.293, file_cluster_11: 13.301
- **Magnitude:** 582.48 | **LOC:** 919 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.9591%), Tech Debt (23.4296%)
**Top Internal Functions/Classes:**
  * `debug` (Impact: 407.0)
  * `debug` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 178`, `args: 47`, `func_start: 45`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 1`, `state_mutation: 119`, `dead_code: 9`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 77`, `api: 41`, `import: 15`
* *Defense:* `safety: 50`, `doc: 34`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wheel, wheel.bdist_wheel, pip, setuptools.command, sys, os, ast, platform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ruamel.yaml-0.19.1/resolver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.949 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.919 IQR)
- **Top Global Matches:** file_cluster_13: 11.949, file_cluster_0: 12.018, file_cluster_16: 12.113
- **Magnitude:** 284.36 | **LOC:** 393 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.1639%), Tech Debt (98.0841%)
**Top Internal Functions/Classes:**
  * `add_path_resolver` (Impact: 49.6)
  * `resolve` (Impact: 32.5)
  * `resolve` (Impact: 32.5)
  * `descend_resolver` (Impact: 23.1)
  * `processing_version` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 70`, `args: 16`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 49`, `dead_code: 1`, `duplicate_logic: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 19`, `import: 9`
* *Defense:* `safety: 21`, `doc: 20`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.359
  * `Choke Point (Betweenness):` 0.012952 | `Ripple Effect (Closeness):` 0.138889
  * `Imports (Out-Degree: 5):` __future__, re, typing, ruamel.yaml.error, ruamel.yaml.compat, ruamel.yaml.nodes, ruamel.yaml.tag, ruamel.yaml.util
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/tokens.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.815 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.794 IQR)
- **Top Global Matches:** file_cluster_0: 14.815, file_cluster_11: 14.967, file_cluster_17: 15.058
- **Magnitude:** 254.08 | **LOC:** 385 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.6035%), Tech Debt (99.999%)
**Top Internal Functions/Classes:**
  * `move_old_comment` (Impact: 29.4)
    * *Intent:* """move a comment from this token to target (normally next token) used to combine e.g. comments befo...
  * `move_new_comment` (Impact: 21.4)
  * `__repr__` (Impact: 13.1)
    * *Intent:* # attributes = [key for key in self.__slots__ if not key.endswith('_mark') and # hasattr('self', key...
  * `add_comment_eol` (Impact: 8.6)
  * `__repr__` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 90`, `args: 26`, `func_start: 26`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 51`, `dead_code: 8`, `duplicate_logic: 14`
* *Architecture:* `api: 46`, `import: 4`
* *Defense:* `safety: 29`, `doc: 6`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.944
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.195312
  * `Imports (Out-Degree: 2):` typing, __future__, ruamel.yaml.compat, .error
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/reader.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.325 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.01 IQR)
- **Top Global Matches:** file_cluster_0: 13.325, file_cluster_11: 13.358, file_cluster_13: 13.448
- **Magnitude:** 248.5 | **LOC:** 278 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.2399%), Tech Debt (41.1651%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 66.2)
  * `update` (Impact: 20.6)
  * `_get_non_printable_regex` (Impact: 10.6)
  * `update_raw` (Impact: 9.2)
  * `check_printable` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 47`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 110`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 15`, `import: 5`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.459
  * `Choke Point (Betweenness):` 0.001455 | `Ripple Effect (Closeness):` 0.079365
  * `Imports (Out-Degree: 3):` __future__, typing, ruamel.yaml.error, psyco, ruamel.yaml.compat, codecs, ruamel.yaml.util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/error.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.938 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.362 IQR)
- **Top Global Matches:** file_cluster_13: 13.938, file_cluster_11: 14.057, file_cluster_16: 14.084
- **Magnitude:** 238.88 | **LOC:** 329 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.1904%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 18.6)
  * `__str__` (Impact: 18.6)
  * `__str__` (Impact: 18.4)
    * *Intent:* # warn is ignored
  * `get_snippet` (Impact: 17.6)
  * `__eq__` (Impact: 9.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 66`, `args: 20`, `func_start: 20`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 87`, `dead_code: 6`, `duplicate_logic: 16`
* *Architecture:* `api: 21`, `import: 6`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.428
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.36
  * `Imports (Out-Degree: 0):` warnings, __future__, typing, textwrap
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/events.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.488 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.498 IQR)
- **Top Global Matches:** file_cluster_0: 11.488, file_cluster_16: 11.51, file_cluster_13: 11.544
- **Magnitude:** 188.7 | **LOC:** 267 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.5545%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 22.3)
  * `compact_repr` (Impact: 14.6)
  * `compact_repr` (Impact: 12.4)
  * `compact_repr` (Impact: 12.4)
  * `tag` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 51`, `args: 20`, `func_start: 20`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 57`, `dead_code: 1`, `duplicate_logic: 18`, `orphaned_logic: 1`
* *Architecture:* `api: 25`, `import: 3`
* *Defense:* `safety: 5`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.423
  * `Choke Point (Betweenness):` 0.001859 | `Ripple Effect (Closeness):` 0.201646
  * `Imports (Out-Degree: 1):` ruamel.yaml.tag, __future__, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/compat.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.686 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.32 IQR)
- **Top Global Matches:** file_cluster_13: 10.686, file_cluster_16: 10.903, file_cluster_0: 11.079
- **Magnitude:** 161.06 | **LOC:** 237 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.764%), Tech Debt (97.7023%)
**Top Internal Functions/Classes:**
  * `__setitem__` (Impact: 21.1)
  * `__call__` (Impact: 17.1)
  * `dbg` (Impact: 12.8)
  * `check_namespace_char` (Impact: 12.5)
  * `insert` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 72`, `args: 19`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 15`, `duplicate_logic: 4`
* *Architecture:* `io: 9`, `api: 21`, `import: 14`
* *Defense:* `safety: 9`, `doc: 4`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 87.046
  * `Choke Point (Betweenness):` 0.011111 | `Ripple Effect (Closeness):` 0.477513
  * `Imports (Out-Degree: 1):` io, __future__, ruamel.yaml.docinfo, traceback, sys, typing, collections.abc, collections...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/serializer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.798 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.845 IQR)
- **Top Global Matches:** file_cluster_13: 11.798, file_cluster_0: 11.946, file_cluster_11: 11.966
- **Magnitude:** 151.96 | **LOC:** 234 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.2764%), Tech Debt (55.215%)
**Top Internal Functions/Classes:**
  * `serialize_node` (Impact: 44.4)
  * `anchor_node` (Impact: 18.3)
  * `serialize` (Impact: 7.9)
    * *Intent:* # def __del__(self): # self.close()
  * `open` (Impact: 7.3)
  * `generate_anchor` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 36`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 34`, `dead_code: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 1`, `api: 12`, `import: 8`
* *Defense:* `safety: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.538
  * `Choke Point (Betweenness):` 0.006283 | `Ripple Effect (Closeness):` 0.106838
  * `Imports (Out-Degree: 5):` __future__, typing, ruamel.yaml.events, ruamel.yaml.error, ruamel.yaml.compat, ruamel.yaml.nodes, ruamel.yaml.util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/composer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.559 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.346 IQR)
- **Top Global Matches:** file_cluster_13: 10.559, file_cluster_0: 10.697, file_cluster_8: 10.716
- **Magnitude:** 141.06 | **LOC:** 247 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.5742%), Tech Debt (45.8001%)
**Top Internal Functions/Classes:**
  * `compose_node` (Impact: 25.9)
  * `compose_sequence_node` (Impact: 19.0)
  * `compose_mapping_node` (Impact: 13.8)
  * `check_end_doc_comment` (Impact: 8.5)
  * `compose_scalar_node` (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 47`, `args: 13`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 15`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 16`, `import: 7`
* *Defense:* `safety: 11`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.459
  * `Choke Point (Betweenness):` 0.000794 | `Ripple Effect (Closeness):` 0.086182
  * `Imports (Out-Degree: 4):` __future__, typing, ruamel.yaml.events, ruamel.yaml.error, warnings, ruamel.yaml.compat, ruamel.yaml.nodes
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/util.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.571 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.459 IQR)
- **Top Global Matches:** file_cluster_13: 15.571, file_cluster_11: 15.685, file_cluster_0: 15.763
- **Magnitude:** 98.02 | **LOC:** 265 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.7711%), Tech Debt (38.8596%)
**Top Internal Functions/Classes:**
  * `load_yaml_guess_indent` (Impact: 67.5)
    * *Intent:* # should do something else instead (or hook this up to the preceding if statement # in reverse # if ...
  * `leading_spaces` (Impact: 6.2)
  * `__getattribute__` (Impact: 3.7)
  * `__init__` (Impact: 2.6)
  * `__setattr__` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 38`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 3`, `dead_code: 11`, `orphaned_logic: 3`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 7`, `doc: 10`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.896
  * `Choke Point (Betweenness):` 0.097354 | `Ripple Effect (Closeness):` 0.173611
  * `Imports (Out-Degree: 3):` __future__, .comments, functools, re, .main, .compat, typing, configobj...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/tag.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.379 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.091 IQR)
- **Top Global Matches:** file_cluster_16: 12.379, file_cluster_13: 12.524, file_cluster_0: 12.581
- **Magnitude:** 83.98 | **LOC:** 127 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.2331%), Tech Debt (99.7341%)
**Top Internal Functions/Classes:**
  * `trval` (Impact: 13.8)
  * `uri_decoded_suffix` (Impact: 11.4)
    * *Intent:* # self._trval = self.handle + self.suffix
  * `__hash__` (Impact: 3.8)
  * `__eq__` (Impact: 3.7)
  * `startswith` (Impact: 3.7)
    * *Intent:* # other should not be a string, but the serializer sometimes provides these if isinstance(other, str...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 36`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 28`, `orphaned_logic: 7`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 9`, `doc: 6`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 73.318
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.272727
  * `Imports (Out-Degree: 0):` __future__, typing
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/scalarstring.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.424 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.453 IQR)
- **Top Global Matches:** file_cluster_13: 10.424, file_cluster_16: 10.449, file_cluster_8: 10.649
- **Magnitude:** 75.58 | **LOC:** 143 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.5632%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `walk_tree` (Impact: 25.6)
    * *Intent:* """ the routine here walks over a simple yaml tree (recursing in dict values and list items) and con...
  * `yaml_anchor` (Impact: 7.2)
  * `__new__` (Impact: 4.3)
  * `anchor` (Impact: 3.7)
  * `replace` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 43`, `args: 12`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 3`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `api: 13`, `import: 5`
* *Defense:* `safety: 7`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.181481
  * `Imports (Out-Degree: 2):` __future__, ruamel.yaml.anchor, typing, collections.abc, ruamel.yaml.compat
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/scalarfloat.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.597 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.624 IQR)
- **Top Global Matches:** file_cluster_13: 10.597, file_cluster_16: 10.614, file_cluster_8: 10.744
- **Magnitude:** 70.92 | **LOC:** 106 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.2967%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `yaml_anchor` (Impact: 7.2)
  * `__iadd__` (Impact: 5.5)
  * `__ifloordiv__` (Impact: 5.5)
  * `__imul__` (Impact: 5.5)
  * `__ipow__` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 44`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 9`, `duplicate_logic: 3`, `orphaned_logic: 7`
* *Architecture:* `io: 1`, `api: 8`, `import: 4`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.125
  * `Imports (Out-Degree: 1):` typing, __future__, sys, ruamel.yaml.anchor
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/nodes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.566 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.61 IQR)
- **Top Global Matches:** file_cluster_0: 13.566, file_cluster_13: 13.644, file_cluster_11: 13.73
- **Magnitude:** 70.6 | **LOC:** 150 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.791%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `dump` (Impact: 16.5)
  * `tag` (Impact: 5.3)
  * `__repr__` (Impact: 4.4)
  * `tag` (Impact: 3.7)
  * `__init__` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 26`, `args: 8`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 25`, `dead_code: 3`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `api: 8`, `import: 4`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.317
  * `Choke Point (Betweenness):` 0.001463 | `Ripple Effect (Closeness):` 0.213384
  * `Imports (Out-Degree: 1):` typing, ruamel.yaml.tag, __future__, sys
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/docinfo.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.553 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.821 IQR)
- **Top Global Matches:** file_cluster_16: 12.553, file_cluster_0: 12.617, file_cluster_11: 12.723
- **Magnitude:** 69.68 | **LOC:** 131 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.883%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__lt__` (Impact: 5.5)
  * `__le__` (Impact: 5.5)
  * `__gt__` (Impact: 5.5)
  * `__ge__` (Impact: 5.5)
  * `__eq__` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 47`, `args: 13`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 19`, `planned_debt: 1`, `duplicate_logic: 3`, `orphaned_logic: 6`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 9`, `doc: 4`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 93.355
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.292398
  * `Imports (Out-Degree: 0):` __future__, typing, dataclasses
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/scalarint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.268 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.171 IQR)
- **Top Global Matches:** file_cluster_16: 10.268, file_cluster_13: 10.485, file_cluster_12: 10.528
- **Magnitude:** 67.3 | **LOC:** 125 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.4445%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `yaml_anchor` (Impact: 7.2)
  * `__iadd__` (Impact: 5.5)
  * `__ifloordiv__` (Impact: 5.5)
  * `__imul__` (Impact: 5.5)
  * `__ipow__` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 46`, `args: 14`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 5`, `duplicate_logic: 6`, `orphaned_logic: 6`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 3`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.125
  * `Imports (Out-Degree: 1):` __future__, typing, ruamel.yaml.anchor
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/cyaml.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.824 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.776 IQR)
- **Top Global Matches:** file_cluster_16: 8.824, file_cluster_8: 8.878, file_cluster_13: 9.118
- **Magnitude:** 37.7 | **LOC:** 205 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.3164%), Tech Debt (99.8665%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1.9)
  * `__init__` (Impact: 1.9)
  * `__init__` (Impact: 1.9)
  * `__init__` (Impact: 1.2)
  * `__init__` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 28`, `args: 6`, `func_start: 6`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 18`, `duplicate_logic: 6`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.316
  * `Choke Point (Betweenness):` 0.005094 | `Ripple Effect (Closeness):` 0.027778
  * `Imports (Out-Degree: 4):` __future__, _ruamel_yaml_clibz, typing, ruamel.yaml.constructor, ruamel.yaml.compat, ruamel.yaml.resolver, ruamel.yaml.representer, _ruamel_yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ruamel.yaml-0.19.1/CHANGES` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 28.5 | **LOC:** 1425 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ruamel.yaml-0.19.1/events.py` (PYTHON) | Magnitude: 188.7 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 186, state_mutation: 57, structural_boundaries: 51, safety_bypasses: 46
- `ruamel.yaml-0.19.1/reader.py` (PYTHON) | Magnitude: 248.5 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 202, state_mutation: 110, branch: 56, structural_boundaries: 47
- `ruamel.yaml-0.19.1/comments.py` (PYTHON) | Magnitude: 948.56 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 836, structural_boundaries: 327, safety_bypasses: 256, encapsulation: 248
- `ruamel.yaml-0.19.1/nodes.py` (PYTHON) | Magnitude: 70.6 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, safety_bypasses: 30, structural_boundaries: 26, state_mutation: 25
- `ruamel.yaml-0.19.1/tokens.py` (PYTHON) | Magnitude: 254.08 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 227, encapsulation: 91, structural_boundaries: 90, safety_bypasses: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `ruamel.yaml-0.19.1/main.py` (PYTHON) | Magnitude: 855.24 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 992, branch: 271, state_mutation: 264, safety_bypasses: 235
- `ruamel.yaml-0.19.1/representer.py` (PYTHON) | Magnitude: 787.14 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 834, branch: 315, structural_boundaries: 182, safety_bypasses: 146
- `ruamel.yaml-0.19.1/parser.py` (PYTHON) | Magnitude: 616.38 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 598, state_mutation: 179, branch: 158, structural_boundaries: 142
- `ruamel.yaml-0.19.1/emitter.py` (PYTHON) | Magnitude: 1797.58 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1492, branch: 631, state_mutation: 491, structural_boundaries: 175
- `ruamel.yaml-0.19.1/scanner.py` (PYTHON) | Magnitude: 1612.9 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1692, branch: 520, state_mutation: 338, structural_boundaries: 315

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ruamel.yaml-0.19.1/scalarfloat.py` (PYTHON) | Magnitude: 70.92 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 78, encapsulation: 56, structural_boundaries: 44, safety_bypasses: 27
- `ruamel.yaml-0.19.1/scalarstring.py` (PYTHON) | Magnitude: 75.58 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 43, safety_bypasses: 22, encapsulation: 20
- `ruamel.yaml-0.19.1/resolver.py` (PYTHON) | Magnitude: 284.36 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 279, branch: 104, structural_boundaries: 70, safety_bypasses: 57
- `ruamel.yaml-0.19.1/constructor.py` (PYTHON) | Magnitude: 40087.23 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1375, branch: 451, structural_boundaries: 275, safety_bypasses: 213
- `ruamel.yaml-0.19.1/util.py` (PYTHON) | Magnitude: 98.02 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 156, branch: 52, structural_boundaries: 38, safety_bypasses: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `ruamel.yaml-0.19.1/cyaml.py` (PYTHON) | Magnitude: 37.7 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 155, encapsulation: 50, safety_bypasses: 31, generics: 31
- `ruamel.yaml-0.19.1/docinfo.py` (PYTHON) | Magnitude: 69.68 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 47, encapsulation: 45, state_mutation: 19
- `ruamel.yaml-0.19.1/tag.py` (PYTHON) | Magnitude: 83.98 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 36, state_mutation: 28, encapsulation: 27
- `ruamel.yaml-0.19.1/scalarint.py` (PYTHON) | Magnitude: 67.3 | Delta: **0.217 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 46, encapsulation: 46, safety_bypasses: 43
- `ruamel.yaml-0.19.1/mergevalue.py` (PYTHON) | Magnitude: 23.38 | Delta: **0.249 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 16, safety_bypasses: 13, generics: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `ruamel.yaml-0.19.1/loader.py` (PYTHON) | Magnitude: 15.38 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 64, encapsulation: 30, structural_boundaries: 26, generics: 12
- `ruamel.yaml-0.19.1/timestamp.py` (PYTHON) | Magnitude: 15.98 | Delta: **0.262 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 44, safety_bypasses: 19, structural_boundaries: 17, branch: 12
- `ruamel.yaml-0.19.1/dumper.py` (PYTHON) | Magnitude: 16.68 | Delta: **0.465 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 192, safety_bypasses: 37, generics: 29, structural_boundaries: 22

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `ruamel.yaml-0.19.1/main.py` -> **Severity: 11.125** (Bridge: 0.1113 * Flux: 99.9508%)
- `ruamel.yaml-0.19.1/constructor.py` -> **Severity: 2.855** (Bridge: 0.0411 * Flux: 69.4765%)
- `ruamel.yaml-0.19.1/representer.py` -> **Severity: 1.672** (Bridge: 0.0221 * Flux: 75.7873%)
- `ruamel.yaml-0.19.1/util.py` -> **Severity: 1.665** (Bridge: 0.0974 * Flux: 17.1044%)
- `ruamel.yaml-0.19.1/loader.py` -> **Severity: 1.352** (Bridge: 0.031 * Flux: 43.6671%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ruamel.yaml-0.19.1/compat.py` -> **Severity: 43.628** (Embedded: 0.4775 * Error Risk: 91.3659%)
- `ruamel.yaml-0.19.1/error.py` -> **Severity: 35.345** (Embedded: 0.36 * Error Risk: 98.1798%)
- `ruamel.yaml-0.19.1/anchor.py` -> **Severity: 22.157** (Embedded: 0.2647 * Error Risk: 83.704%)
- `ruamel.yaml-0.19.1/comments.py` -> **Severity: 21.613** (Embedded: 0.2235 * Error Risk: 96.6808%)
- `ruamel.yaml-0.19.1/tag.py` -> **Severity: 20.941** (Embedded: 0.2727 * Error Risk: 76.7839%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ruamel.yaml-0.19.1/compat.py` -> **Severity: 4418.62** (Blast Radius: 87.046 * Doc Risk: 50.7619%)
- `ruamel.yaml-0.19.1/tokens.py` -> **Severity: 2601.556** (Blast Radius: 27.944 * Doc Risk: 93.0989%)
- `ruamel.yaml-0.19.1/comments.py` -> **Severity: 2288.866** (Blast Radius: 31.523 * Doc Risk: 72.6094%)
- `ruamel.yaml-0.19.1/error.py` -> **Severity: 2092.443** (Blast Radius: 62.428 * Doc Risk: 33.5177%)
- `ruamel.yaml-0.19.1/events.py` -> **Severity: 1872.88** (Blast Radius: 28.423 * Doc Risk: 65.8931%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
