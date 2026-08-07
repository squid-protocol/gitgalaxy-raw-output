# ARCHITECTURAL_BRIEF: moment
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/moment` |
| **Timestamp** | `2026-08-07T04:26:57.260839+00:00` |
| **Scan Duration** | `2.91s` |
| **Git Branch** | `develop` |
| **Git Commit** | `18aba135ab927ffe7f868ee09276979bed6993a6` |
| **Git Remote** | `https://github.com/moment/moment.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 622 malicious artifacts.

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
| Total Artifacts | 795 |
| Analyzed Artifacts (Scanned) | 634 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 161 |
| Total LOC | 145475 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 79.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5197 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5649 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5764 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 617 | 143143 | 97.3% |
| JSON | 6 | 239 | 0.9% |
| MARKDOWN | 5 | 0 | 0.8% |
| TYPESCRIPT | 4 | 2056 | 0.6% |
| PLAINTEXT | 1 | 0 | 0.2% |
| SHELL | 1 | 37 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.824`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 563 | 88.8% |
| file_cluster_13 | 53 | 8.4% |
| file_cluster_4 | 8 | 1.3% |
| file_cluster_17 | 3 | 0.5% |
| file_cluster_15 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 0.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 161*

**Composition by Extension & Reason:**
- `.js`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 149293 LOC exceeds safe regex boundaries)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 3x Excluded (Unsupported Extension: '.map')
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 12060 LOC)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nuspec`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 15.9 | 7.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 36.9 | 32.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.7 | 2.3 | 0.0 |
| API Exposure | 0.0 | 13.2 | 2.3 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 31.6 | 14.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 40.2 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 95.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.9 | 20.6 | 15.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/locales.js` (Hits: 13)
- `tasks/transpile.js` (Hits: 13)
- `meteor/moment.js` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **qunit.js** (`src/test/qunit.js`) — 192 inbound connections
2. **qunit-locale.js** (`src/test/qunit-locale.js`) — 138 inbound connections
3. **hooks.js** (`src/lib/utils/hooks.js`) — 18 inbound connections
4. **to-int.js** (`src/lib/utils/to-int.js`) — 17 inbound connections
5. **regex.js** (`src/lib/parse/regex.js`) — 16 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **prototype.js** (`src/lib/moment/prototype.js`) — 32 outbound dependencies
2. **from-anything.js** (`src/lib/create/from-anything.js`) — 17 outbound dependencies
3. **month.js** (`src/lib/units/month.js`) — 15 outbound dependencies
4. **offset.js** (`src/lib/units/offset.js`) — 15 outbound dependencies
5. **prototype.js** (`src/lib/locale/prototype.js`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `moment` (@ `moment.d.ts`) -> Impact: **523.3** | LOC: 717
- `moment` (@ `ts3.1-typings/moment.d.ts`) -> Impact: **522.7** | LOC: 705
- `factory` (@ `min/locales.js`) -> Impact: **412.1** | LOC: 1730
- `processRelativeTime` (@ `locale/sl.js`) -> Impact: **225.5** | LOC: 83
  * *Intent:* //! moment.js locale configuration
- `processRelativeTime` (@ `src/locale/sl.js`) -> Impact: **225.5** | LOC: 83
- `factory` (@ `locale/sl.js`) -> Impact: **207.9** | LOC: 174
- `factory` (@ `locale/ru.js`) -> Impact: **171.8** | LOC: 214
- `factory` (@ `locale/mr.js`) -> Impact: **131.5** | LOC: 205
- `factory` (@ `locale/cs.js`) -> Impact: **130.4** | LOC: 184
- `factory` (@ `locale/hi.js`) -> Impact: **126.3** | LOC: 171

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `min` | 2 | 8563.88 | 20.88% | 97.22% |
| `src/test/moment` | 52 | 3346.34 | 4.43% | 0.0% |
| `__monolith__` | 14 | 2526.63 | 10.55% | 13.4% |
| `meteor` | 4 | 2384.96 | 27.17% | 15.17% |
| `src/lib/units` | 21 | 1483.6 | 40.49% | 39.37% |
| `src/lib/moment` | 19 | 1093.68 | 48.91% | 19.43% |
| `src/lib/parse` | 2 | 689.04 | 28.94% | 50.0% |
| `src/lib/create` | 12 | 663.28 | 33.5% | 57.96% |
| `src/lib/duration` | 13 | 496.36 | 37.88% | 0.0% |
| `src/lib/utils` | 27 | 324.82 | 23.48% | 3.7% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `benchmarks/isObjectEmpty.js` -> **100.0%** Exposure
- `benchmarks/query.js` -> **100.0%** Exposure
- `benchmarks/zeroFill.js` -> **100.0%** Exposure
- `src/lib/create/from-array.js` -> **100.0%** Exposure
- `src/lib/create/from-string-and-format.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `meteor/export.js` -> **100.0%** Exposure
- `src/lib/duration/abs.js` -> **100.0%** Exposure
- `src/lib/duration/constructor.js` -> **100.0%** Exposure
- `src/lib/duration/get.js` -> **100.0%** Exposure
- `src/lib/duration/iso-string.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `min/moment-with-locales.js` -> **46** Orphaned Functions | **165** Duplicates
- `min/locales.js` -> **0** Orphaned Functions | **185** Duplicates
- `src/test/locale/sl.js` -> **0** Orphaned Functions | **59** Duplicates
- `src/test/moment/create.js` -> **0** Orphaned Functions | **57** Duplicates
- `src/test/moment/duration.js` -> **0** Orphaned Functions | **51** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/lib/duration/create.js`** -> AI Confidence: **99.39%**
2. **`src/lib/create/from-string.js`** -> AI Confidence: **99.34%**
3. **`src/lib/create/check-overflow.js`** -> AI Confidence: **99.32%**
4. **`src/lib/create/from-anything.js`** -> AI Confidence: **99.31%**
5. **`src/lib/create/from-array.js`** -> AI Confidence: **99.31%**
6. **`src/lib/create/from-string-and-format.js`** -> AI Confidence: **99.31%**
7. **`src/lib/locale/locales.js`** -> AI Confidence: **99.31%**
8. **`src/lib/units/day-of-week.js`** -> AI Confidence: **99.31%**
9. **`src/lib/units/era.js`** -> AI Confidence: **99.31%**
10. **`src/lib/units/month.js`** -> AI Confidence: **99.31%**
11. **`src/lib/utils/is-moment-input.js`** -> AI Confidence: **99.31%**
12. **`Gruntfile.js`** -> AI Confidence: **99.29%**
13. **`locale/bs.js`** -> AI Confidence: **99.29%**
14. **`locale/es-do.js`** -> AI Confidence: **99.29%**
15. **`locale/fr-ca.js`** -> AI Confidence: **99.29%**
16. **`locale/fr-ch.js`** -> AI Confidence: **99.29%**
17. **`locale/fr.js`** -> AI Confidence: **99.29%**
18. **`locale/hi.js`** -> AI Confidence: **99.29%**
19. **`locale/mi.js`** -> AI Confidence: **99.29%**
20. **`locale/mr.js`** -> AI Confidence: **99.29%**
21. **`locale/nl-be.js`** -> AI Confidence: **99.29%**
22. **`locale/nl.js`** -> AI Confidence: **99.29%**
23. **`locale/ru.js`** -> AI Confidence: **99.29%**
24. **`locale/sl.js`** -> AI Confidence: **99.29%**
25. **`src/locale/fr.js`** -> AI Confidence: **99.29%**
26. **`src/locale/hi.js`** -> AI Confidence: **99.29%**
27. **`src/locale/mi.js`** -> AI Confidence: **99.29%**
28. **`src/locale/mr.js`** -> AI Confidence: **99.29%**
29. **`src/locale/nl-be.js`** -> AI Confidence: **99.29%**
30. **`src/locale/nl.js`** -> AI Confidence: **99.29%**
31. **`src/locale/sl.js`** -> AI Confidence: **99.29%**
32. **`tasks/bump_version.js`** -> AI Confidence: **99.29%**
33. **`templates/default.js`** -> AI Confidence: **99.29%**
34. **`templates/locale-header.js`** -> AI Confidence: **99.29%**
35. **`src/test/locale/cs.js`** -> AI Confidence: **99.2%**
36. **`src/test/locale/it.js`** -> AI Confidence: **99.2%**
37. **`src/test/locale/sk.js`** -> AI Confidence: **99.2%**
38. **`src/lib/units/hour.js`** -> AI Confidence: **99.18%**
39. **`locale/ar-kw.js`** -> AI Confidence: **99.17%**
40. **`locale/ar-ma.js`** -> AI Confidence: **99.17%**
41. **`locale/ar-tn.js`** -> AI Confidence: **99.17%**
42. **`locale/be.js`** -> AI Confidence: **99.17%**
43. **`locale/bm.js`** -> AI Confidence: **99.17%**
44. **`locale/cy.js`** -> AI Confidence: **99.17%**
45. **`locale/da.js`** -> AI Confidence: **99.17%**
46. **`locale/es-mx.js`** -> AI Confidence: **99.17%**
47. **`locale/es-us.js`** -> AI Confidence: **99.17%**
48. **`locale/es.js`** -> AI Confidence: **99.17%**
49. **`locale/eu.js`** -> AI Confidence: **99.17%**
50. **`locale/fi.js`** -> AI Confidence: **99.17%**
51. **`locale/fo.js`** -> AI Confidence: **99.17%**
52. **`locale/hr.js`** -> AI Confidence: **99.17%**
53. **`locale/it.js`** -> AI Confidence: **99.17%**
54. **`locale/mt.js`** -> AI Confidence: **99.17%**
55. **`locale/nb.js`** -> AI Confidence: **99.17%**
56. **`locale/nn.js`** -> AI Confidence: **99.17%**
57. **`locale/oc-lnc.js`** -> AI Confidence: **99.17%**
58. **`locale/se.js`** -> AI Confidence: **99.17%**
59. **`locale/sw.js`** -> AI Confidence: **99.17%**
60. **`locale/tzm-latn.js`** -> AI Confidence: **99.17%**
61. **`locale/tzm.js`** -> AI Confidence: **99.17%**
62. **`locale/uz-latn.js`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `22` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `benchmarks/add.js` (JAVASCRIPT) -> Cumulative Risk: **631.26**
- **Archetype:** `file_cluster_4` (Distance: 11.558 IQR)
- **Magnitude:** 18.48 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9968%), Concurrency (99.9885%), Tech Debt (99.548%)
- **Heaviest Functions:** `generateTestForUnit` (Impact: 2.1), `setup` (Impact: 1.5), `fn` (Impact: 1.5)

### 2. `benchmarks/endOf.js` (JAVASCRIPT) -> Cumulative Risk: **627.89**
- **Archetype:** `file_cluster_4` (Distance: 11.324 IQR)
- **Magnitude:** 17.48 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9885%), State Flux (99.9738%), Tech Debt (99.548%)
- **Heaviest Functions:** `generateTestForUnit` (Impact: 2.1), `setup` (Impact: 1.5), `fn` (Impact: 1.5)

### 3. `benchmarks/startOf.js` (JAVASCRIPT) -> Cumulative Risk: **627.89**
- **Archetype:** `file_cluster_4` (Distance: 11.324 IQR)
- **Magnitude:** 17.48 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9885%), State Flux (99.9738%), Tech Debt (99.548%)
- **Heaviest Functions:** `generateTestForUnit` (Impact: 2.1), `setup` (Impact: 1.5), `fn` (Impact: 1.5)

### 4. `benchmarks/subtract.js` (JAVASCRIPT) -> Cumulative Risk: **627.89**
- **Archetype:** `file_cluster_4` (Distance: 11.324 IQR)
- **Magnitude:** 17.48 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9885%), State Flux (99.9738%), Tech Debt (99.548%)
- **Heaviest Functions:** `generateTestForUnit` (Impact: 2.1), `setup` (Impact: 1.5), `fn` (Impact: 1.5)

### 5. `tasks/transpile.js` (JAVASCRIPT) -> Cumulative Risk: **620.98**
- **Archetype:** `file_cluster_4` (Distance: 10.803 IQR)
- **Magnitude:** 255.96 | **LOC:** 363 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.4177%), State Flux (93.0736%), Concurrency (84.9997%)
- **Heaviest Functions:** `exports` (Impact: 63.1), `transpile` (Impact: 15.2), `done` (Impact: 11.9)

### 6. `src/lib/units/month.js` (JAVASCRIPT) -> Cumulative Risk: **593.52**
- **Archetype:** `file_cluster_13` (Distance: 12.547 IQR)
- **Magnitude:** 219.7 | **LOC:** 341 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (94.1965%)
- **Heaviest Functions:** `addParseToken` (Impact: 27.8), `monthsShortRegex` (Impact: 16.5), `monthsRegex` (Impact: 16.5)

### 7. `src/lib/units/day-of-week.js` (JAVASCRIPT) -> Cumulative Risk: **588.4**
- **Archetype:** `file_cluster_13` (Distance: 13.108 IQR)
- **Magnitude:** 312.04 | **LOC:** 433 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.6215%), Safety Score (97.6799%)
- **Heaviest Functions:** `addWeekParseToken` (Impact: 39.0), `weekdaysRegex` (Impact: 16.5), `weekdaysShortRegex` (Impact: 16.5)

### 8. `benchmarks/zeroFill.js` (JAVASCRIPT) -> Cumulative Risk: **582.72**
- **Archetype:** `file_cluster_8` (Distance: 10.421 IQR)
- **Magnitude:** 51.62 | **LOC:** 44 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.8701%), State Flux (98.9536%)
- **Heaviest Functions:** `zeroFillWhile` (Impact: 8.4), `zeroFillMath` (Impact: 6.8), `zeroFillMath` (Impact: 6.3)

### 9. `src/lib/moment/get-set.js` (JAVASCRIPT) -> Cumulative Risk: **572.31**
- **Archetype:** `file_cluster_13` (Distance: 11.727 IQR)
- **Magnitude:** 120.4 | **LOC:** 118 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (95.2574%), Verification (80.0%), State Flux (78.9182%)
- **Heaviest Functions:** `set` (Impact: 44.0), `get` (Impact: 36.1), `stringSet` (Impact: 9.5)

### 10. `benchmarks/isObjectEmpty.js` (JAVASCRIPT) -> Cumulative Risk: **571.15**
- **Archetype:** `file_cluster_8` (Distance: 11.611 IQR)
- **Magnitude:** 59.66 | **LOC:** 68 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9984%), Cognitive Load (93.1821%)
- **Heaviest Functions:** `isObjectEmpty_getOwnPropertyNames` (Impact: 7.7), `isObjectEmpty_keys` (Impact: 7.7), `isObjectEmpty_forIn` (Impact: 4.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `min/moment-with-locales.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.561 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.404 IQR)
- **Top Global Matches:** file_cluster_8: 12.561, file_cluster_7: 13.123, file_cluster_11: 13.143
- **Magnitude:** 4822.44 | **LOC:** 18473 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.199%), Tech Debt (98.5669%)
**Top Internal Functions/Classes:**
  * `relativeTimeMr` (Impact: 122.7)
  * `processRelativeTime$9` (Impact: 103.2)
  * `translate$5` (Impact: 53.8)
  * `translate$9` (Impact: 52.6)
  * `endOf` (Impact: 48.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2287`, `structural_boundaries: 1191`, `args: 470`, `func_start: 614`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 1501`, `dead_code: 10`, `planned_debt: 7`, `duplicate_logic: 165`, `orphaned_logic: 46`
* *Architecture:* `io: 5`, `api: 1`
* *Defense:* `safety: 378`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `min/locales.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.664 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.425 IQR)
- **Top Global Matches:** file_cluster_8: 11.664, file_cluster_7: 12.29, file_cluster_13: 12.524
- **Magnitude:** 3741.44 | **LOC:** 12801 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.5654%), Tech Debt (95.8756%)
**Top Internal Functions/Classes:**
  * `factory` (Impact: 412.1)
  * `relativeTimeMr` (Impact: 122.7)
  * `processRelativeTime$9` (Impact: 103.2)
    * *Intent:* //! moment.js locale configuration
  * `translate$5` (Impact: 53.8)
  * `translate$9` (Impact: 52.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2144`, `structural_boundaries: 1073`, `args: 394`, `func_start: 382`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 554`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 185`
* *Architecture:* `io: 4`, `api: 23`, `import: 1`
* *Defense:* `safety: 453`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `meteor/moment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.155 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.876 IQR)
- **Top Global Matches:** file_cluster_8: 13.155, file_cluster_11: 13.406, file_cluster_0: 13.556
- **Magnitude:** 2346.94 | **LOC:** 5689 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.0394%), Tech Debt (60.6704%)
**Top Internal Functions/Classes:**
  * `endOf` (Impact: 48.4)
  * `startOf` (Impact: 48.1)
  * `diff` (Impact: 46.4)
  * `localeErasParse` (Impact: 36.0)
  * `as` (Impact: 33.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 890`, `structural_boundaries: 504`, `args: 253`, `func_start: 395`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 1196`, `dead_code: 7`, `planned_debt: 6`, `duplicate_logic: 24`
* *Architecture:* `io: 5`, `api: 28`
* *Defense:* `safety: 126`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `moment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.155 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.876 IQR)
- **Top Global Matches:** file_cluster_8: 13.155, file_cluster_11: 13.406, file_cluster_0: 13.556
- **Magnitude:** 2346.94 | **LOC:** 5689 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.0394%), Tech Debt (60.6704%)
**Top Internal Functions/Classes:**
  * `endOf` (Impact: 48.4)
  * `startOf` (Impact: 48.1)
  * `diff` (Impact: 46.4)
  * `localeErasParse` (Impact: 36.0)
  * `as` (Impact: 33.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 890`, `structural_boundaries: 504`, `args: 253`, `func_start: 395`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 1196`, `dead_code: 7`, `planned_debt: 6`, `duplicate_logic: 24`
* *Architecture:* `io: 5`, `api: 28`
* *Defense:* `safety: 126`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/parse/regex.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.116 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.311 IQR)
- **Top Global Matches:** file_cluster_8: 8.116, file_cluster_13: 8.806, file_cluster_7: 9.074
- **Magnitude:** 654.0 | **LOC:** 85 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.127%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 13`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 1`, `api: 4`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.736
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.032406
  * `Imports (Out-Degree: 1):` is-function, has-own-prop
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/test/moment/create.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.738 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.316 IQR)
- **Top Global Matches:** file_cluster_8: 9.738, file_cluster_7: 10.468, file_cluster_1: 10.599
- **Magnitude:** 329.38 | **LOC:** 2920 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 27.3)
  * `test` (Impact: 16.9)
  * `test` (Impact: 13.5)
  * `test` (Impact: 11.8)
  * `test` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 36`, `args: 60`, `func_start: 182`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 39`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 57`
* *Architecture:* `import: 4`
* *Defense:* `safety: 18`, `test: 316`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` moment, each-own-prop, has-own-prop, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/units/day-of-week.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.108 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.108 IQR)
- **Top Global Matches:** file_cluster_13: 13.108, file_cluster_11: 13.288, file_cluster_8: 13.444
- **Magnitude:** 312.04 | **LOC:** 433 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.9676%), Tech Debt (99.6215%)
**Top Internal Functions/Classes:**
  * `addWeekParseToken` (Impact: 39.0)
  * `weekdaysRegex` (Impact: 16.5)
  * `weekdaysShortRegex` (Impact: 16.5)
  * `weekdaysMinRegex` (Impact: 16.5)
  * `getSetISODayOfWeek` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 49`, `args: 15`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 161`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 10`, `import: 10`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.288
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.011058
  * `Imports (Out-Degree: 7):` index-of, format, regex, to-int, has-own-prop, parsing-flags, utc, token...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/lib/moment/start-end-of.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.113 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.784 IQR)
- **Top Global Matches:** file_cluster_8: 13.113, file_cluster_13: 13.271, file_cluster_11: 13.49
- **Magnitude:** 279.14 | **LOC:** 165 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.8954%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `endOf` (Impact: 48.4)
  * `startOf` (Impact: 48.1)
  * `localStartOfDate` (Impact: 8.4)
  * `utcStartOfDate` (Impact: 8.4)
  * `mod` (Impact: 1.9)
    * *Intent:* // actual modulo - handles negative numbers (for dates before 1970):
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 16`, `args: 5`, `func_start: 9`
* *Risk/State:* `state_mutation: 157`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.00158
  * `Imports (Out-Degree: 2):` aliases, hooks
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/lib/units/era.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.906 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.006 IQR)
- **Top Global Matches:** file_cluster_8: 11.906, file_cluster_13: 11.962, file_cluster_11: 12.307
- **Magnitude:** 272.26 | **LOC:** 294 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.4202%), Tech Debt (42.99%)
**Top Internal Functions/Classes:**
  * `localeErasParse` (Impact: 36.0)
  * `localeEras` (Impact: 20.4)
  * `getEraYear` (Impact: 13.4)
  * `getEraName` (Impact: 11.3)
  * `getEraNarrow` (Impact: 11.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 53`, `args: 17`, `func_start: 39`
* *Risk/State:* `state_mutation: 93`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `import: 8`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.971
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.00316
  * `Imports (Out-Degree: 5):` constants, format, locales, regex, hooks, parsing-flags, token, has-own-prop
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tasks/transpile.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.803 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.167 IQR)
- **Top Global Matches:** file_cluster_4: 10.803, file_cluster_8: 11.158, file_cluster_17: 11.229
- **Magnitude:** 255.96 | **LOC:** 363 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.9181%), Tech Debt (96.4177%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 63.1)
  * `transpile` (Impact: 15.2)
  * `done` (Impact: 11.9)
  * `generateLocales` (Impact: 11.6)
  * `rollupBundle` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 44`, `args: 42`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 40`, `dead_code: 2`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `io: 13`, `api: 2`, `concurrency: 64`, `import: 6`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment-with-locales.custom.js, esperanto, es6-promise, rollup-plugin-babel, , rollup, moment, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/units/month.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.547 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.617 IQR)
- **Top Global Matches:** file_cluster_13: 12.547, file_cluster_11: 12.772, file_cluster_8: 12.999
- **Magnitude:** 219.7 | **LOC:** 341 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.1965%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `addParseToken` (Impact: 27.8)
  * `monthsShortRegex` (Impact: 16.5)
  * `monthsRegex` (Impact: 16.5)
  * `setMonth` (Impact: 15.2)
  * `daysInMonth` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 48`, `args: 15`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 93`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 9`, `import: 15`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.095
  * `Choke Point (Betweenness):` 0.000369 | `Ripple Effect (Closeness):` 0.013787
  * `Imports (Out-Degree: 11):` get-set, format, constants, index-of, is-number, mod, regex, hooks...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/test/moment/locale.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.039 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.548 IQR)
- **Top Global Matches:** file_cluster_8: 9.039, file_cluster_7: 9.863, file_cluster_1: 10.037
- **Magnitude:** 214.94 | **LOC:** 1033 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7747%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 17.3)
  * `test` (Impact: 10.8)
  * `test` (Impact: 8.5)
  * `test` (Impact: 7.9)
  * `test` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 32`, `args: 45`, `func_start: 76`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 20`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 43`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 3`, `test: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` moment, each, index-of, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/duration.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.816 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.139 IQR)
- **Top Global Matches:** file_cluster_8: 8.816, file_cluster_7: 9.681, file_cluster_1: 9.857
- **Magnitude:** 214.06 | **LOC:** 2031 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.8326%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 10.1)
  * `test` (Impact: 4.5)
  * `test` (Impact: 4.2)
  * `test` (Impact: 3.8)
  * `test` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 21`, `args: 52`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 26`, `dead_code: 5`, `duplicate_logic: 51`
* *Architecture:* `import: 2`
* *Defense:* `safety: 5`, `test: 629`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` moment, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/format.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.444 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.842 IQR)
- **Top Global Matches:** file_cluster_8: 9.444, file_cluster_7: 10.172, file_cluster_1: 10.259
- **Magnitude:** 200.7 | **LOC:** 952 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 15.0)
  * `test` (Impact: 8.1)
  * `test` (Impact: 5.5)
  * `test` (Impact: 5.5)
  * `test` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 32`, `args: 44`, `func_start: 99`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 34`, `dead_code: 3`, `duplicate_logic: 44`
* *Architecture:* `import: 3`
* *Defense:* `safety: 2`, `test: 244`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` moment, each-own-prop, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/zones.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.073 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.867 IQR)
- **Top Global Matches:** file_cluster_8: 9.073, file_cluster_7: 9.842, file_cluster_1: 9.894
- **Magnitude:** 196.48 | **LOC:** 823 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8029%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 13.6)
  * `test` (Impact: 9.0)
  * `updateOffset` (Impact: 7.4)
  * `updateOffset` (Impact: 7.3)
  * `updateOffset` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 29`, `args: 37`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 40`, `duplicate_logic: 36`, `orphaned_logic: 1`
* *Architecture:* `import: 2`
* *Defense:* `test: 229`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` moment, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/utc_offset.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.033 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.721 IQR)
- **Top Global Matches:** file_cluster_8: 9.033, file_cluster_7: 9.815, file_cluster_1: 9.893
- **Magnitude:** 193.0 | **LOC:** 895 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.4775%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 13.6)
  * `test` (Impact: 9.0)
  * `updateOffset` (Impact: 7.4)
  * `updateOffset` (Impact: 7.3)
  * `updateOffset` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 27`, `args: 35`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 40`, `duplicate_logic: 35`
* *Architecture:* `import: 2`
* *Defense:* `test: 244`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` moment, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/units/offset.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.96 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.803 IQR)
- **Top Global Matches:** file_cluster_13: 12.96, file_cluster_8: 13.353, file_cluster_11: 13.471
- **Magnitude:** 179.7 | **LOC:** 250 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.095%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `offsetFromString` (Impact: 12.9)
  * `isDaylightSavingTimeShifted` (Impact: 11.4)
  * `cloneWithOffset` (Impact: 9.5)
    * *Intent:* // Return a moment from input, that is local/utc/zone equivalent to model.
  * `hasAlignedHourOffset` (Impact: 5.6)
  * `isUtc` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 43`, `args: 13`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 87`
* *Architecture:* `api: 15`, `import: 15`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.374
  * `Choke Point (Betweenness):` 0.000808 | `Ripple Effect (Closeness):` 0.006319
  * `Imports (Out-Degree: 10):` format, utc, compare-arrays, add-subtract, from-anything, regex, is-date, local...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/lib/moment/compare.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.657 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.483 IQR)
- **Top Global Matches:** file_cluster_13: 13.657, file_cluster_8: 13.929, file_cluster_11: 14.048
- **Magnitude:** 149.82 | **LOC:** 73 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.4286%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isBetween` (Impact: 23.2)
  * `isSame` (Impact: 14.7)
  * `isAfter` (Impact: 12.7)
  * `isBefore` (Impact: 12.7)
  * `isSameOrAfter` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 26`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` aliases, constructor, local
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/add_subtract.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.845 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.347 IQR)
- **Top Global Matches:** file_cluster_8: 9.845, file_cluster_7: 10.564, file_cluster_1: 10.712
- **Magnitude:** 134.44 | **LOC:** 546 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.9208%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 18.2)
  * `test` (Impact: 4.1)
  * `test` (Impact: 3.7)
  * `test` (Impact: 3.3)
  * `test` (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 18`, `args: 17`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 57`, `fragile_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `test: 192`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` moment, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/is_valid.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.27 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.745 IQR)
- **Top Global Matches:** file_cluster_8: 9.27, file_cluster_7: 10.087, file_cluster_1: 10.115
- **Magnitude:** 133.08 | **LOC:** 587 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5558%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 13.5)
  * `test` (Impact: 9.7)
  * `test` (Impact: 9.7)
  * `test` (Impact: 7.0)
  * `test` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 10`, `args: 27`, `func_start: 89`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 9`, `duplicate_logic: 28`
* *Architecture:* `import: 3`
* *Defense:* `safety: 8`, `test: 174`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` moment, each, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/start_end_of.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.082 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.726 IQR)
- **Top Global Matches:** file_cluster_8: 9.082, file_cluster_7: 9.865, file_cluster_1: 10.116
- **Magnitude:** 128.7 | **LOC:** 539 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.7946%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 8.1)
  * `test` (Impact: 8.1)
  * `test` (Impact: 5.6)
  * `test` (Impact: 5.6)
  * `updateOffset` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 27`, `args: 27`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`, `duplicate_logic: 27`
* *Architecture:* `import: 2`
* *Defense:* `test: 264`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` moment, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/moment/get-set.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.727 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.502 IQR)
- **Top Global Matches:** file_cluster_13: 11.727, file_cluster_0: 12.01, file_cluster_11: 12.049
- **Magnitude:** 120.4 | **LOC:** 118 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.096%), Tech Debt (95.2574%)
**Top Internal Functions/Classes:**
  * `set` (Impact: 44.0)
  * `get` (Impact: 36.1)
  * `stringSet` (Impact: 9.5)
  * `makeGetSet` (Impact: 5.7)
  * `stringGet` (Impact: 3.8)
    * *Intent:* // MOMENTS
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 37`, `args: 6`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 9`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.457
  * `Choke Point (Betweenness):` 0.000314 | `Ripple Effect (Closeness):` 0.019747
  * `Imports (Out-Degree: 5):` year, is-function, aliases, priorities, hooks
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/lib/duration/humanize.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.14 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.811 IQR)
- **Top Global Matches:** file_cluster_8: 11.14, file_cluster_13: 11.505, file_cluster_0: 11.633
- **Magnitude:** 120.16 | **LOC:** 115 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.594%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `relativeTime` (Impact: 64.4)
  * `humanize` (Impact: 15.5)
  * `getSetRelativeTimeThreshold` (Impact: 7.6)
    * *Intent:* // This function allows you to set a threshold for relative time strings
  * `getSetRelativeTimeRounding` (Impact: 5.7)
    * *Intent:* // This function allows you to set the rounding function for relative time strings
  * `substituteTimeAgo` (Impact: 5.0)
    * *Intent:* // helper function for moment.fn.from, moment.fn.fromNow, and moment.duration.fn.humanize
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 17`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00316
  * `Imports (Out-Degree: 0):` create
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/lib/create/from-string.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.65 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.923 IQR)
- **Top Global Matches:** file_cluster_8: 9.65, file_cluster_13: 9.996, file_cluster_7: 10.383
- **Magnitude:** 119.94 | **LOC:** 259 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.6944%), Tech Debt (97.3179%)
**Top Internal Functions/Classes:**
  * `configFromISO` (Impact: 39.2)
    * *Intent:* // date from iso format
  * `calculateOffset` (Impact: 10.7)
  * `configFromRFC2822` (Impact: 8.3)
    * *Intent:* // date and time from ref 2822 format
  * `untruncateYear` (Impact: 7.4)
  * `checkWeekday` (Impact: 6.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 31`, `args: 7`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.352
  * `Choke Point (Betweenness):` 0.000233 | `Ripple Effect (Closeness):` 0.010376
  * `Imports (Out-Degree: 6):` month, from-string-and-format, parsing-flags, hooks, day-of-week, date-from-array, deprecate
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/lib/create/from-anything.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.406 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.9 IQR)
- **Top Global Matches:** file_cluster_13: 11.406, file_cluster_8: 11.841, file_cluster_11: 12.185
- **Magnitude:** 117.24 | **LOC:** 118 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.0998%), Tech Debt (98.5241%)
**Top Internal Functions/Classes:**
  * `prepareConfig` (Impact: 27.6)
  * `configFromInput` (Impact: 23.6)
  * `createLocalOrUTC` (Impact: 23.5)
  * `configFromString` (Impact: 5.5)
  * `createFromConfig` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 30`, `args: 5`, `func_start: 10`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 18`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.238
  * `Choke Point (Betweenness):` 0.00159 | `Ripple Effect (Closeness):` 0.012339
  * `Imports (Out-Degree: 14):` from-string, is-object-empty, valid, from-string-and-format, locales, is-number, is-object, from-string-and-array...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `benchmarks/load-missing.js` (JAVASCRIPT) | Magnitude: 4.82 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, import: 2, structural_boundaries: 1, args: 1
- `src/lib/utils/deprecate.js` (JAVASCRIPT) | Magnitude: 45.86 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, branch: 12, structural_boundaries: 10, state_mutation: 10
- `src/lib/units/millisecond.js` (JAVASCRIPT) | Magnitude: 37.76 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 16, func_start: 15, state_mutation: 11
- `src/test/moment/deprecate.js` (JAVASCRIPT) | Magnitude: 5.18 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: func_start: 4, test: 4, indent_spaces: 4, structural_boundaries: 3
- `src/lib/duration/create.js` (JAVASCRIPT) | Magnitude: 77.0 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, branch: 58, structural_boundaries: 19, state_mutation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/lib/moment/now.js` (JAVASCRIPT) | Magnitude: 7.66 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, state_mutation: 3, time_date_logic: 3, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `locale/ku-kmr.js` (JAVASCRIPT) | Magnitude: 0.08 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 100, branch: 21, structural_boundaries: 12, state_mutation: 10
- `src/lib/locale/formats.js` (JAVASCRIPT) | Magnitude: 0.03 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 14, structural_boundaries: 9, branch: 6
- `scripts/locales.js` (JAVASCRIPT) | Magnitude: 108.32 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 37, args: 21, structural_boundaries: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `benchmarks/compare.js` (JAVASCRIPT) | Magnitude: 20.0 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 12, state_mutation: 9, concurrency: 6, indent_spaces: 6
- `benchmarks/endOf.js` (JAVASCRIPT) | Magnitude: 17.48 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, concurrency: 6, state_mutation: 5
- `benchmarks/startOf.js` (JAVASCRIPT) | Magnitude: 17.48 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, concurrency: 6, state_mutation: 5
- `benchmarks/subtract.js` (JAVASCRIPT) | Magnitude: 17.48 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, concurrency: 6, state_mutation: 5
- `benchmarks/add.js` (JAVASCRIPT) | Magnitude: 18.48 | Delta: **0.221 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, state_mutation: 6, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/lib/utils/keys.js` (JAVASCRIPT) | Magnitude: 16.04 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 9, branch: 5, structural_boundaries: 5
- `src/lib/units/hour.js` (JAVASCRIPT) | Magnitude: 86.38 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, func_start: 43, structural_boundaries: 28, state_mutation: 27
- `src/lib/locale/lists.js` (JAVASCRIPT) | Magnitude: 0.07 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 21, state_mutation: 16, branch: 13
- `ender.js` (JAVASCRIPT) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1
- `src/lib/units/week-year.js` (JAVASCRIPT) | Magnitude: 73.98 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 28, func_start: 26, state_mutation: 24

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/lib/create/from-anything.js` -> **Severity: 0.156** (Bridge: 0.0016 * Flux: 98.0268%)
- `src/lib/units/offset.js` -> **Severity: 0.081** (Bridge: 0.0008 * Flux: 100.0%)
- `src/test/helpers/common-locale.js` -> **Severity: 0.051** (Bridge: 0.0005 * Flux: 100.0%)
- `src/lib/units/year.js` -> **Severity: 0.043** (Bridge: 0.0004 * Flux: 99.6731%)
- `src/lib/units/month.js` -> **Severity: 0.037** (Bridge: 0.0004 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/test/qunit.js` -> **Severity: 17.139** (Embedded: 0.3033 * Error Risk: 56.5055%)
- `src/test/helpers/deprecation-handler.js` -> **Severity: 11.086** (Embedded: 0.1532 * Error Risk: 72.343%)
- `src/test/helpers/each.js` -> **Severity: 8.065** (Embedded: 0.1058 * Error Risk: 76.2542%)
- `src/test/helpers/common-locale.js` -> **Severity: 4.974** (Embedded: 0.1102 * Error Risk: 45.1436%)
- `src/test/helpers/object-keys.js` -> **Severity: 4.503** (Embedded: 0.0575 * Error Risk: 78.3421%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/lib/utils/abs-floor.js` -> **Severity: 364.343** (Blast Radius: 8.559 * Doc Risk: 42.5684%)
- `src/lib/utils/to-int.js` -> **Severity: 356.168** (Blast Radius: 6.636 * Doc Risk: 53.6721%)
- `src/lib/parse/token.js` -> **Severity: 348.137** (Blast Radius: 3.736 * Doc Risk: 93.1845%)
- `src/lib/utils/is-function.js` -> **Severity: 267.104** (Blast Radius: 7.166 * Doc Risk: 37.2738%)
- `src/lib/create/parsing-flags.js` -> **Severity: 227.021** (Blast Radius: 3.583 * Doc Risk: 63.3606%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
