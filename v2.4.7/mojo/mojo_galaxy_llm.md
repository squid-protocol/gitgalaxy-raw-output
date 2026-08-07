# ARCHITECTURAL_BRIEF: mojo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/mojo` |
| **Timestamp** | `2026-08-07T03:51:58.574017+00:00` |
| **Scan Duration** | `1.25s` |
| **Git Branch** | `main` |
| **Git Commit** | `19fc4f19a0d83204a458ae4a19d192b7eaf4ba81` |
| **Git Remote** | `https://github.com/mojolicious/mojo.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1 malicious artifacts.

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
| Total Artifacts | 405 |
| Analyzed Artifacts (Scanned) | 315 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 90 |
| Total LOC | 52647 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 77.8% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7604 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1172 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2008 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 14 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 280 | 52539 | 88.9% |
| PLAINTEXT | 22 | 12 | 7.0% |
| JSON | 6 | 30 | 1.9% |
| YAML | 4 | 13 | 1.3% |
| MARKDOWN | 1 | 0 | 0.3% |
| MAKEFILE | 1 | 52 | 0.3% |
| HTML | 1 | 1 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.393`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 137 | 43.5% |
| file_cluster_8 | 60 | 19.0% |
| file_cluster_4 | 42 | 13.3% |
| file_cluster_13 | 41 | 13.0% |
| Unknown | 12 | 3.8% |
| file_cluster_17 | 9 | 2.9% |
| file_cluster_2 | 3 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 3.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 90*

**Composition by Extension & Reason:**
- `.ep`: 11x Excluded (Unsupported Extension: '.ep'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pod`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.epl`: 8x Excluded (Unsupported Extension: '.epl'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.conf`: 6x Excluded (Unsupported Extension: '.conf'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 11 LOC)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.css`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mt`: 2x Excluded (Unsupported Extension: '.mt'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.map`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 39.3 | 40.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 70.7 | 85.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.1 | 0.6 | 0.0 |
| API Exposure | 0.0 | 10.7 | 0.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 23.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 77.2 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.6 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 79.2 | 1.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 98.2 | 27.4 | 19.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/Mojo/UserAgent.pm` (Hits: 84)
- `lib/Mojo/DOM/CSS.pm` (Hits: 57)
- `lib/Test/Mojo.pm` (Hits: 43)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **content.t** (`t/mojo/content.t`) — 10 inbound connections
2. **Mojolicious.pm** (`lib/Mojolicious.pm`) — 7 inbound connections
3. **Config.pm** (`lib/Mojolicious/Plugin/Config.pm`) — 6 inbound connections
4. **URL.pm** (`lib/Mojo/URL.pm`) — 3 inbound connections
5. **path.t** (`t/mojo/path.t`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Util.pm** (`lib/Mojo/Util.pm`) — 31 outbound dependencies
2. **dom.t** (`t/mojo/dom.t`) — 26 outbound dependencies
3. **request.t** (`t/mojo/request.t`) — 26 outbound dependencies
4. **response.t** (`t/mojo/response.t`) — 26 outbound dependencies
5. **commands.t** (`t/mojolicious/commands.t`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `download` (@ `lib/Mojo/UserAgent/Transactor.pm`) -> Impact: **412.6** | LOC: 572
- `_content` (@ `lib/Mojolicious/Plugin/DefaultHelpers.pm`) -> Impact: **397.1** | LOC: 838
- `BUILD_DYNAMIC` (@ `lib/Mojolicious/Routes/Route.pm`) -> Impact: **361.4** | LOC: 627
- `BUILD_DYNAMIC` (@ `lib/Mojolicious/Controller.pm`) -> Impact: **355.4** | LOC: 949
- `clone` (@ `lib/Mojo/URL.pm`) -> Impact: **336.6** | LOC: 510
- `BUILD_DYNAMIC` (@ `lib/Mojolicious.pm`) -> Impact: **320.1** | LOC: 1161
- `_message` (@ `lib/Test/Mojo.pm`) -> Impact: **319.1** | LOC: 925
- `register` (@ `lib/Mojolicious/Plugin/DefaultHelpers.pm`) -> Impact: **306.6** | LOC: 902
- `_development` (@ `lib/Mojolicious/Plugin/DefaultHelpers.pm`) -> Impact: **300.6** | LOC: 812
- `password` (@ `lib/Mojo/URL.pm`) -> Impact: **292.8** | LOC: 453

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t/mojo/certs` | 10 | 50000.0 | 0.0% | 0.0% |
| `lib/Mojo` | 35 | 39719.08 | 43.93% | 22.43% |
| `t/mojo` | 63 | 18047.64 | 61.62% | 8.37% |
| `lib/Mojo/IOLoop/resources` | 2 | 10000.0 | 0.0% | 0.0% |
| `lib/Mojolicious/Routes` | 3 | 5621.12 | 42.71% | 4.13% |
| `lib/Mojo/DOM` | 2 | 5257.38 | 49.08% | 0.0% |
| `lib/Mojo/UserAgent` | 4 | 4493.73 | 48.23% | 0.0% |
| `lib/Mojolicious` | 12 | 4186.59 | 38.57% | 18.64% |
| `t/mojolicious` | 54 | 3565.26 | 29.81% | 0.94% |
| `lib/Mojolicious/Plugin` | 9 | 2949.72 | 39.85% | 38.25% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `lib/Mojo/Asset.pm` -> **100.0%** Exposure
- `lib/Mojo/Cookie.pm` -> **100.0%** Exposure
- `lib/Mojo/Reactor.pm` -> **100.0%** Exposure
- `lib/Mojo/Transaction.pm` -> **100.0%** Exposure
- `lib/Mojolicious/Plugin.pm` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `lib/Mojo/Asset/File.pm` -> **100.0%** Exposure
- `lib/Mojo/Asset/Memory.pm` -> **100.0%** Exposure
- `lib/Mojo/ByteStream.pm` -> **100.0%** Exposure
- `lib/Mojo/Collection.pm` -> **100.0%** Exposure
- `lib/Mojo/Content.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/Mojo/Reactor.pm` -> **0** Orphaned Functions | **24** Duplicates
- `lib/Mojo/Asset.pm` -> **0** Orphaned Functions | **16** Duplicates
- `t/mojolicious/lib/MojoliciousTest/Foo.pm` -> **14** Orphaned Functions | **0** Duplicates
- `lib/Mojo/Promise.pm` -> **12** Orphaned Functions | **0** Duplicates
- `lib/Mojolicious/Plugin/DefaultHelpers.pm` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`lib/Mojolicious/Command/Author/generate/makefile.pm`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1755` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `lib/Mojo/Promise.pm` (PERL) -> Cumulative Risk: **672.52**
- **Archetype:** `file_cluster_4` (Distance: 14.418 IQR)
- **Magnitude:** 1785.78 | **LOC:** 551 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (92.7163%)
- **Heaviest Functions:** `_all` (Impact: 201.3), `AWAIT_GET` (Impact: 193.5), `map` (Impact: 167.0)

### 2. `t/mojolicious/lib/MojoliciousTest/Foo.pm` (PERL) -> Cumulative Risk: **611.19**
- **Archetype:** `file_cluster_2` (Distance: 12.745 IQR)
- **Magnitude:** 85.82 | **LOC:** 113 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (97.0156%)
- **Heaviest Functions:** `suspended` (Impact: 3.4), `stage1` (Impact: 3.3), `index` (Impact: 3.1)

### 3. `lib/Mojo/IOLoop.pm` (PERL) -> Cumulative Risk: **602.74**
- **Archetype:** `file_cluster_4` (Distance: 13.793 IQR)
- **Magnitude:** 1129.56 | **LOC:** 552 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (94.614%)
- **Heaviest Functions:** `client` (Impact: 134.2), `reset` (Impact: 126.3), `_out` (Impact: 101.5)

### 4. `t/mojo/lib/Mojo/TestConnectProxy.pm` (PERL) -> Cumulative Risk: **599.55**
- **Archetype:** `file_cluster_4` (Distance: 11.803 IQR)
- **Magnitude:** 126.78 | **LOC:** 85 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9997%)
- **Heaviest Functions:** `proxy` (Impact: 39.6)

### 5. `lib/Mojo/Base.pm` (PERL) -> Cumulative Risk: **597.22**
- **Archetype:** `file_cluster_13` (Distance: 13.311 IQR)
- **Magnitude:** 358.12 | **LOC:** 382 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Concurrency (92.0857%), Safety Score (81.1217%)
- **Heaviest Functions:** `attr` (Impact: 138.1), `import` (Impact: 86.5), `DESTROY` (Impact: 1.1)

### 6. `lib/Mojolicious/Plugin/DefaultHelpers.pm` (PERL) -> Cumulative Risk: **590.65**
- **Archetype:** `file_cluster_0` (Distance: 14.024 IQR)
- **Magnitude:** 1902.8 | **LOC:** 917 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.3662%), Safety Score (93.3883%)
- **Heaviest Functions:** `_content` (Impact: 397.1), `register` (Impact: 306.6), `_development` (Impact: 300.6)

### 7. `t/mojolicious/external/myapp2.pl` (PERL) -> Cumulative Risk: **586.68**
- **Archetype:** `file_cluster_4` (Distance: 12.6 IQR)
- **Magnitude:** 0.04 | **LOC:** 37 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9723%)

### 8. `lib/Mojolicious/Plugin/JSONConfig.pm` (PERL) -> Cumulative Risk: **567.4**
- **Archetype:** `file_cluster_0` (Distance: 12.611 IQR)
- **Magnitude:** 98.22 | **LOC:** 154 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9989%), Tech Debt (99.157%), Safety Score (83.2913%)
- **Heaviest Functions:** `parse` (Impact: 61.2), `parse` (Impact: 2.7), `render` (Impact: 2.6)

### 9. `t/mojo/tls.t` (PERL) -> Cumulative Risk: **564.36**
- **Archetype:** `file_cluster_4` (Distance: 13.121 IQR)
- **Magnitude:** 126.16 | **LOC:** 66 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)

### 10. `lib/Mojolicious/Plugin/NotYAMLConfig.pm` (PERL) -> Cumulative Risk: **562.68**
- **Archetype:** `file_cluster_0` (Distance: 12.036 IQR)
- **Magnitude:** 98.7 | **LOC:** 140 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9837%), Tech Debt (99.2255%), Verification (80.0%)
- **Heaviest Functions:** `parse` (Impact: 70.3), `parse` (Impact: 2.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `lib/Mojo/DOM.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.775 IQR)
- **Top Global Matches:** file_cluster_17: 12.775, file_cluster_0: 12.935, file_cluster_8: 13.004
- **Magnitude:** 15371.83 | **LOC:** 1109 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.6901%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 269`, `args: 74`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 327`
* *Architecture:* `io: 11`, `import: 9`
* *Defense:* `safety: 2`, `doc: 8`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` more, Scalar::Util, it, overload, Mojo::Collection, Mojo::DOM::HTML, Storable, Mojo::DOM::CSS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/Content.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.864 IQR)
- **Top Global Matches:** file_cluster_0: 13.864, file_cluster_13: 13.97, file_cluster_8: 14.001
- **Magnitude:** 9924.19 | **LOC:** 608 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.4807%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 187`, `args: 42`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `state_mutation: 287`
* *Architecture:* `io: 9`, `import: 7`
* *Defense:* `safety: 4`, `doc: 45`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.382
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004246
  * `Imports (Out-Degree: 0):` Scalar::Util, Mojo::SSE, Carp, Mojo::Headers, Compress::Raw::Zlib, leading, Mojo::Base
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/mojo/util.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.499 IQR)
- **Top Global Matches:** file_cluster_0: 10.499, file_cluster_8: 10.546, file_cluster_13: 10.978
- **Magnitude:** 5084.12 | **LOC:** 691 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.0429%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 156`, `args: 3`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `import: 15`
* *Defense:* `safety: 3`, `doc: 2`, `test: 100`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Mojo::ByteStream, o, Test::More, exception, lib, changes, Mojo::File, Sub::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/IOLoop/resources/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/IOLoop/resources/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/bad.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/bad.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/client.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/domain.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/domain.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojolicious/Routes/Pattern.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.926 IQR)
- **Top Global Matches:** file_cluster_0: 13.926, file_cluster_8: 14.148, file_cluster_13: 14.167
- **Magnitude:** 4422.4 | **LOC:** 371 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.4871%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 97`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 286`
* *Architecture:* `import: 3`
* *Defense:* `safety: 1`, `doc: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojolicious::Routes::Pattern, Carp, Mojo::Base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/DOM/HTML.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.282 IQR)
- **Top Global Matches:** file_cluster_0: 13.282, file_cluster_13: 13.372, file_cluster_17: 13.491
- **Magnitude:** 4386.66 | **LOC:** 377 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.8931%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 88`, `args: 7`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 168`
* *Architecture:* `io: 6`, `api: 2`, `import: 6`
* *Defense:* `doc: 15`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Scalar::Util, Mojo::Base, Mojo::DOM::HTML, Exporter, warnings, Mojo::Util, more
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/UserAgent/CookieJar.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.407 IQR)
- **Top Global Matches:** file_cluster_0: 13.407, file_cluster_13: 13.633, file_cluster_8: 13.713
- **Magnitude:** 3416.73 | **LOC:** 319 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.2729%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 90`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 194`
* *Architecture:* `io: 9`, `import: 6`
* *Defense:* `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Scalar::Util, Mojo::File, Mojo::Path, Mojo::UserAgent::CookieJar, Mojo::Cookie::Request, Mojo::Base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Test/Mojo.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.006 IQR)
- **Top Global Matches:** file_cluster_0: 14.006, file_cluster_4: 14.063, file_cluster_13: 14.114
- **Magnitude:** 2280.98 | **LOC:** 1354 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.5711%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_message` (Impact: 319.1)
  * `_json` (Impact: 292.5)
  * `_request_ok` (Impact: 269.4)
  * `new` (Impact: 265.9)
  * `_sse_ok` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 349`, `args: 112`, `func_start: 84`, `class_start: 1`
* *Risk/State:* `state_mutation: 748`, `planned_debt: 1`
* *Architecture:* `io: 43`, `concurrency: 80`, `import: 30`
* *Defense:* `safety: 1`, `doc: 86`, `test: 13`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` match, similar, Test::More, Mojo::JSON::Pointer, Mojo::File, Mojo::Server, Mojo::IOLoop, value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/URL.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.091 IQR)
- **Top Global Matches:** file_cluster_0: 14.091, file_cluster_13: 14.417, file_cluster_8: 14.516
- **Magnitude:** 2091.48 | **LOC:** 522 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.7405%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `clone` (Impact: 336.6)
  * `password` (Impact: 292.8)
  * `_decode` (Impact: 286.7)
  * `protocol` (Impact: 268.8)
  * `query` (Impact: 267.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 109`, `args: 20`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 272`
* *Architecture:* `import: 6`
* *Defense:* `doc: 32`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009554
  * `Imports (Out-Degree: 0):` overload, Mojo::URL, Mojo::Path, Mojo::Parameters, Mojo::Util, Mojo::Base
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `t/mojo/request.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.887 IQR)
- **Top Global Matches:** file_cluster_0: 13.887, file_cluster_13: 14.182, file_cluster_8: 14.241
- **Magnitude:** 2019.74 | **LOC:** 2178 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.4904%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 527`, `structural_boundaries: 527`, `args: 50`
* *Risk/State:* `state_mutation: 1963`
* *Architecture:* `io: 18`, `import: 90`
* *Defense:* `safety: 17`, `test: 96`, `cleanup: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` URL, progress, Mojo::URL, Test::More, leftovers, headers, body, decompression...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojolicious/Plugin/DefaultHelpers.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.024 IQR)
- **Top Global Matches:** file_cluster_0: 14.024, file_cluster_13: 14.138, file_cluster_4: 14.162
- **Magnitude:** 1902.8 | **LOC:** 917 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3079%), Tech Debt (39.7315%)
**Top Internal Functions/Classes:**
  * `_content` (Impact: 397.1)
  * `register` (Impact: 306.6)
  * `_development` (Impact: 300.6)
  * `_timing_rps` (Impact: 200.4)
  * `_flash` (Impact: 199.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 224`, `args: 48`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 332`, `orphaned_logic: 10`
* *Architecture:* `io: 20`, `concurrency: 47`, `import: 16`
* *Defense:* `safety: 7`, `doc: 58`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::ByteStream, Time::HiRes, Scalar::Util, preference, in, Mojo::Collection, such, Mojo::Asset::File...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/Promise.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.418 IQR)
- **Top Global Matches:** file_cluster_4: 14.418, file_cluster_0: 14.857, file_cluster_17: 14.906
- **Magnitude:** 1785.78 | **LOC:** 551 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (73.028%)
**Top Internal Functions/Classes:**
  * `_all` (Impact: 201.3)
  * `AWAIT_GET` (Impact: 193.5)
  * `map` (Impact: 167.0)
  * `_settle` (Impact: 156.8)
  * `wait` (Impact: 151.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 224`, `args: 47`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 253`, `orphaned_logic: 12`
* *Architecture:* `io: 4`, `concurrency: 270`, `import: 8`
* *Defense:* `safety: 20`, `doc: 34`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Scalar::Util, Carp, Mojo::Exception, Mojo::IOLoop, Mojo::Promise, constant, Mojo::Base, Mojo::UserAgent
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.396 IQR)
- **Top Global Matches:** file_cluster_0: 14.396, file_cluster_13: 14.484, file_cluster_11: 14.785
- **Magnitude:** 1176.92 | **LOC:** 1064 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.2196%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `url_escape` (Impact: 179.3)
  * `unindent` (Impact: 157.3)
  * `class_to_file` (Impact: 147.3)
  * `trim` (Impact: 4.5)
  * `camelize` (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 337`, `args: 42`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 667`
* *Architecture:* `io: 5`, `api: 2`, `import: 35`
* *Defense:* `safety: 11`, `doc: 53`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptX, Mojo::File, MIME::Base64, Data::Dumper, Exporter, Digest::MD5, Digest::SHA, Mojo::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/promise.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.729 IQR)
- **Top Global Matches:** file_cluster_4: 13.729, file_cluster_0: 14.254, file_cluster_17: 14.498
- **Magnitude:** 1161.98 | **LOC:** 558 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 316`, `args: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 321`
* *Architecture:* `concurrency: 816`, `import: 12`
* *Defense:* `safety: 36`, `test: 111`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Scalar::Util, Mojo::Base, Test::More, Mojo::IOLoop, warnings, more
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `lib/Mojolicious/Controller.pm` (PERL) | Magnitude: 858.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 479, indent_spaces: 401, structural_boundaries: 305, encapsulation: 162
- `lib/Mojolicious/Renderer.pm` (PERL) | Magnitude: 499.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 304, structural_boundaries: 190, indent_spaces: 185, branch: 129
- `Makefile.PL` (PERL) | Magnitude: 15.64 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, branch: 12, decorators: 11, structural_boundaries: 5
- `t/mojolicious/rebased_lite_app.t` (PERL) | Magnitude: 40.66 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 38, state_mutation: 20, indent_spaces: 14, structural_boundaries: 13
- `t/mojolicious/tls_lite_app.t` (PERL) | Magnitude: 49.02 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 27, structural_boundaries: 16, decorators: 15, indent_spaces: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/mojolicious/external/myapp.pl` (PERL) | Magnitude: 0.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 38, indent_spaces: 27, structural_boundaries: 25, closures: 12
- `t/mojolicious/log_lite_app.t` (PERL) | Magnitude: 26.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 19, scientific: 12, telemetry: 12
- `lib/Mojo/BaseUtil.pm` (PERL) | Magnitude: 11.56 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 16, decorators: 13, import: 8, indent_spaces: 7
- `t/mojolicious/yaml_config_lite_app.t` (PERL) | Magnitude: 32.5 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 20, pointers: 18, state_mutation: 15
- `lib/Mojo/Template.pm` (PERL) | Magnitude: 805.24 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 346, indent_spaces: 271, branch: 139, structural_boundaries: 123

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/mojo/file.t` (PERL) | Magnitude: 116.58 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 257, structural_boundaries: 102, state_mutation: 95, test: 56
- `t/mojo/collection.t` (PERL) | Magnitude: 68.38 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 82, test: 78, state_mutation: 50
- `t/mojolicious/lib/PluginWithTemplate.pm` (PERL) | Magnitude: 4.22 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 3, args: 2, state_mutation: 2
- `examples/proxy.pl` (PERL) | Magnitude: 20.24 | Delta: **0.139 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 8, state_mutation: 4, encapsulation: 4
- `lib/Mojo/Collection.pm` (PERL) | Magnitude: 321.18 | Delta: **0.156 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 196, structural_boundaries: 166, indent_spaces: 122, comprehensions: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `t/mojolicious/external/lib/MyApp.pm` (PERL) | Magnitude: 0.02 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 13, state_mutation: 12, encapsulation: 6
- `t/mojolicious/lib/MojoliciousTest/Foo.pm` (PERL) | Magnitude: 85.82 | Delta: **0.187 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 45, state_mutation: 41, indent_spaces: 38, args: 22
- `t/mojo/template.t` (PERL) | Magnitude: 280.56 | Delta: **0.206 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 260, ui_framework: 224, decorators: 142, ssr_boundaries: 118

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `t/mojo/prefork.t` (PERL) | Magnitude: 113.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 113, state_mutation: 78, structural_boundaries: 49, decorators: 24
- `t/mojolicious/sse_lite_app.t` (PERL) | Magnitude: 50.54 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 24, concurrency: 18, closures: 13
- `t/mojo/daemon.t` (PERL) | Magnitude: 225.78 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 250, state_mutation: 142, structural_boundaries: 131, decorators: 86
- `examples/microhttpd.pl` (PERL) | Magnitude: 23.52 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 12, sec_reflection_metaprogramming: 10, decorators: 6
- `t/mojo/morbo.t` (PERL) | Magnitude: 122.8 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 83, state_mutation: 69, structural_boundaries: 67, decorators: 59

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/mojo/parameters.t` (PERL) | Magnitude: 62.02 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 159, test: 62, structural_boundaries: 49, decorators: 45
- `t/mojolicious/lite_app.t` (PERL) | Magnitude: 469.7 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 443, state_mutation: 340, structural_boundaries: 216, branch: 139
- `t/mojolicious/exception_lite_app.t` (PERL) | Magnitude: 99.64 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 197, structural_boundaries: 91, state_mutation: 59, closures: 56
- `t/mojolicious/websocket_lite_app.t` (PERL) | Magnitude: 155.1 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 246, state_mutation: 112, structural_boundaries: 110, closures: 64
- `t/mojolicious/lib/PluginWithEmbeddedApp.pm` (PERL) | Magnitude: 3.16 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 6, decorators: 6, class_start: 2, import: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/mojo/util.t` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 5084.12
- `lib/Mojo/UserAgent/CookieJar.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 3416.73
- `lib/Mojo/Util.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 1176.92
- `lib/Mojo/IOLoop.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 1129.56
- `lib/Mojolicious/Controller.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 858.26

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `t/mojo/response.t` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `t/mojo/exception.t` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9987%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/mojo/content.t` -> **Severity: 2.044** (Embedded: 0.0321 * Error Risk: 63.6604%)
- `lib/Mojolicious.pm` -> **Severity: 1.92** (Embedded: 0.0223 * Error Risk: 86.119%)
- `lib/Mojolicious/Plugin/Config.pm` -> **Severity: 1.658** (Embedded: 0.0191 * Error Risk: 86.7507%)
- `lib/Mojo/URL.pm` -> **Severity: 0.94** (Embedded: 0.0096 * Error Risk: 98.3674%)
- `lib/Mojo/Reactor/EV.pm` -> **Severity: 0.601** (Embedded: 0.0064 * Error Risk: 94.422%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/Mojo/URL.pm` -> **Severity: 568.238** (Blast Radius: 6.949 * Doc Risk: 81.7726%)
- `t/mojo/content.t` -> **Severity: 524.199** (Blast Radius: 22.307 * Doc Risk: 23.4993%)
- `lib/Mojolicious/Plugin/Config.pm` -> **Severity: 454.817** (Blast Radius: 16.319 * Doc Risk: 27.8704%)
- `lib/Mojolicious.pm` -> **Severity: 328.213** (Blast Radius: 18.356 * Doc Risk: 17.8804%)
- `t/mojolicious/external/myapp.pl` -> **Severity: 282.336** (Blast Radius: 2.875 * Doc Risk: 98.2037%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
