# ARCHITECTURAL_BRIEF: moment
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/moment` |
| **Timestamp** | `2026-08-03T20:06:10.339555+00:00` |
| **Scan Duration** | `2.96s` |
| **Git Branch** | `develop` |
| **Git Commit** | `18aba135ab927ffe7f868ee09276979bed6993a6` |
| **Git Remote** | `https://github.com/moment/moment.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 622 malicious artifacts.

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
> **Architectural Drift Z-Score:** `7.857`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 565 | 89.1% |
| file_cluster_13 | 53 | 8.4% |
| file_cluster_4 | 6 | 0.9% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 15.8 | 6.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 8.0 | 2.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 23.7 | 2.3 | 0.0 |
| API Exposure | 0.0 | 13.2 | 2.3 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 31.6 | 14.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 40.2 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 95.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 51.9 | 64.2 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 26.0 | 4.9 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 34.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `moment` (@ `moment.d.ts`) -> Impact: **2473.2** | LOC: 717
- `moment` (@ `ts3.1-typings/moment.d.ts`) -> Impact: **2472.6** | LOC: 705
- `factory` (@ `min/locales.js`) -> Impact: **1226.2** | LOC: 1730
- `factory` (@ `locale/sl.js`) -> Impact: **705.9** | LOC: 174
- `factory` (@ `locale/ru.js`) -> Impact: **574.5** | LOC: 214
- `processRelativeTime` (@ `src/locale/sl.js`) -> Impact: **557.6** | LOC: 83
- `factory` (@ `locale/cs.js`) -> Impact: **433.6** | LOC: 184
- `factory` (@ `locale/sk.js`) -> Impact: **413.5** | LOC: 147
- `translate` (@ `src/locale/is.js`) -> Impact: **395.1** | LOC: 75
- `factory` (@ `locale/bs.js`) -> Impact: **383.9** | LOC: 161

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `defineLocale` (@ `src/lib/locale/locales.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // mark as not found to avoid repeating expensive file require call causing high CPU // when trying to find en-US, en_US, en-us for every format call
- `toISOString` (@ `meteor/moment.js`) -> **O(2^N) [Recursive]**
- `moment` (@ `meteor/moment.js`) -> **O(2^N) [Recursive]**
- `toISOString` (@ `min/moment-with-locales.js`) -> **O(2^N) [Recursive]**
- `moment` (@ `min/moment-with-locales.js`) -> **O(2^N) [Recursive]**
- `toISOString` (@ `moment.js`) -> **O(2^N) [Recursive]**
- `moment` (@ `moment.js`) -> **O(2^N) [Recursive]**
- `from` (@ `meteor/moment.js`) -> **O(2^N) [Recursive]**
- `offset` (@ `meteor/moment.js`) -> **O(2^N) [Recursive]**
- `eifelerRegelAppliesToNumber` (@ `min/locales.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Returns true if the word before the given number loses the '-n' ending. * e.g. 'an 10 Deeg' but 'a 5 Deeg' * * @param number {integer} * @return...

### Highest Data Gravity (Database Complexity)
- `exports` (@ `tasks/transpile.js`) -> DB Complexity: **57**
- `endOf` (@ `meteor/moment.js`) -> DB Complexity: **26**
- `startOf` (@ `meteor/moment.js`) -> DB Complexity: **26**
- `endOf` (@ `min/moment-with-locales.js`) -> DB Complexity: **26**
- `startOf` (@ `min/moment-with-locales.js`) -> DB Complexity: **26**
- `endOf` (@ `moment.js`) -> DB Complexity: **26**
- `startOf` (@ `moment.js`) -> DB Complexity: **26**
- `endOf` (@ `src/lib/moment/start-end-of.js`) -> DB Complexity: **26**
- `startOf` (@ `src/lib/moment/start-end-of.js`) -> DB Complexity: **26**
- `factory` (@ `min/locales.js`) -> DB Complexity: **23**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `min` | 2 | 14630.88 | 29.82% | 82.54% |
| `src/test/moment` | 52 | 4280.14 | 4.46% | 0.0% |
| `__monolith__` | 14 | 4225.73 | 10.13% | 12.04% |
| `meteor` | 4 | 3873.56 | 27.18% | 13.04% |
| `src/lib/units` | 21 | 2140.7 | 39.72% | 39.37% |
| `src/lib/moment` | 19 | 1775.18 | 48.91% | 9.17% |
| `src/lib/create` | 12 | 1096.98 | 33.75% | 36.7% |
| `src/lib/duration` | 13 | 718.56 | 37.88% | 0.0% |
| `src/lib/parse` | 2 | 695.04 | 28.94% | 0.0% |
| `src/lib/utils` | 27 | 497.02 | 23.71% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `benchmarks/isObjectEmpty.js` -> **100.0%** Exposure
- `benchmarks/query.js` -> **100.0%** Exposure
- `benchmarks/zeroFill.js` -> **100.0%** Exposure
- `src/lib/units/hour.js` -> **100.0%** Exposure
- `src/lib/units/millisecond.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `meteor/export.js` -> **100.0%** Exposure
- `src/lib/duration/abs.js` -> **100.0%** Exposure
- `src/lib/duration/constructor.js` -> **100.0%** Exposure
- `src/lib/duration/get.js` -> **100.0%** Exposure
- `src/lib/duration/iso-string.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `min/locales.js` -> **0** Orphaned Functions | **141** Duplicates
- `min/moment-with-locales.js` -> **37** Orphaned Functions | **89** Duplicates
- `src/test/moment/create.js` -> **0** Orphaned Functions | **53** Duplicates
- `src/test/moment/duration.js` -> **0** Orphaned Functions | **51** Duplicates
- `src/test/moment/locale.js` -> **0** Orphaned Functions | **41** Duplicates

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

### Obfuscation & Evasion Surface
- `src/test/locale/ar-ly.js` -> **100.0%** Exposure
- `src/test/locale/ar.js` -> **100.0%** Exposure
- `src/test/locale/be.js` -> **100.0%** Exposure
- `src/test/locale/fa.js` -> **100.0%** Exposure
- `src/test/locale/ku.js` -> **100.0%** Exposure
### Exploit Generation Surface
- `locale/el.js` -> **100.0%** Exposure
- `locale/it.js` -> **100.0%** Exposure
- `locale/ru.js` -> **100.0%** Exposure
- `meteor/moment.js` -> **100.0%** Exposure
- `min/locales.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `scripts/npm_prepublish.sh` -> **99.9998%** Exposure
### Algorithmic DoS Exposure
- `benchmarks/zeroFill.js` -> **100.0%** Exposure
- `locale/it.js` -> **100.0%** Exposure
- `meteor/moment.js` -> **100.0%** Exposure
- `min/locales.js` -> **100.0%** Exposure
- `min/moment-with-locales.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `22` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/lib/units/day-of-week.js` (JAVASCRIPT) -> Cumulative Risk: **854.9**
- **Archetype:** `file_cluster_13` (Distance: 13.121 IQR)
- **Magnitude:** 484.14 | **LOC:** 433 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `addWeekParseToken` (Impact: 151.1), `weekdaysRegex` (Impact: 32.1), `weekdaysShortRegex` (Impact: 32.1)

### 2. `src/lib/units/month.js` (JAVASCRIPT) -> Cumulative Risk: **821.14**
- **Archetype:** `file_cluster_13` (Distance: 12.567 IQR)
- **Magnitude:** 388.3 | **LOC:** 341 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `addParseToken` (Impact: 101.0), `setMonth` (Impact: 70.6), `monthsShortRegex` (Impact: 32.1)

### 3. `benchmarks/zeroFill.js` (JAVASCRIPT) -> Cumulative Risk: **792.75**
- **Archetype:** `file_cluster_8` (Distance: 10.395 IQR)
- **Magnitude:** 43.62 | **LOC:** 44 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9892%)
- **Heaviest Functions:** `setup` (Impact: 11.9), `setup` (Impact: 11.1), `fn` (Impact: 2.4)

### 4. `benchmarks/isObjectEmpty.js` (JAVASCRIPT) -> Cumulative Risk: **781.74**
- **Archetype:** `file_cluster_8` (Distance: 11.604 IQR)
- **Magnitude:** 87.36 | **LOC:** 68 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9997%)
- **Heaviest Functions:** `isObjectEmpty_getOwnPropertyNames` (Impact: 18.3), `isObjectEmpty_keys` (Impact: 18.3), `isObjectEmpty_forIn` (Impact: 8.9)

### 5. `src/lib/units/week-year.js` (JAVASCRIPT) -> Cumulative Risk: **764.24**
- **Archetype:** `file_cluster_8` (Distance: 10.616 IQR)
- **Magnitude:** 90.88 | **LOC:** 129 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9498%)
- **Heaviest Functions:** `getSetWeekYearHelper` (Impact: 20.2), `addWeekParseToken` (Impact: 4.8), `setWeekAll` (Impact: 4.1)

### 6. `src/lib/moment/start-end-of.js` (JAVASCRIPT) -> Cumulative Risk: **759.22**
- **Archetype:** `file_cluster_8` (Distance: 13.113 IQR)
- **Magnitude:** 444.84 | **LOC:** 165 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `endOf` (Impact: 138.5), `startOf` (Impact: 115.7), `localStartOfDate` (Impact: 12.4)

### 7. `src/lib/moment/compare.js` (JAVASCRIPT) -> Cumulative Risk: **758.05**
- **Archetype:** `file_cluster_13` (Distance: 13.657 IQR)
- **Magnitude:** 198.22 | **LOC:** 73 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `isBetween` (Impact: 45.5), `isSame` (Impact: 28.6), `isAfter` (Impact: 18.8)

### 8. `meteor/moment.js` (JAVASCRIPT) -> Cumulative Risk: **753.97**
- **Archetype:** `file_cluster_8` (Distance: 13.162 IQR)
- **Magnitude:** 3835.54 | **LOC:** 5689 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9996%)
- **Heaviest Functions:** `endOf` (Impact: 161.0), `startOf` (Impact: 138.2), `localeErasParse` (Impact: 121.0)

### 9. `src/locale/it.js` (JAVASCRIPT) -> Cumulative Risk: **753.05**
- **Archetype:** `file_cluster_8` (Distance: 11.756 IQR)
- **Magnitude:** 0.14 | **LOC:** 107 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `lastWeek` (Impact: 49.7), `sameDay` (Impact: 13.3), `nextDay` (Impact: 13.3)

### 10. `moment.js` (JAVASCRIPT) -> Cumulative Risk: **752.38**
- **Archetype:** `file_cluster_8` (Distance: 13.162 IQR)
- **Magnitude:** 3835.54 | **LOC:** 5689 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9996%)
- **Heaviest Functions:** `endOf` (Impact: 161.0), `startOf` (Impact: 138.2), `localeErasParse` (Impact: 121.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `min/locales.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.663 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.365 IQR)
- **Top Global Matches:** file_cluster_8: 11.663, file_cluster_7: 12.29, file_cluster_13: 12.526
- **Magnitude:** 7627.24 | **LOC:** 12801 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (12.5654%), Tech Debt (85.9074%)
**Top Internal Functions/Classes:**
  * `factory` (Impact: 1226.2 | O(N^6) | DB: 23)
  * `relativeTimeMr` (Impact: 359.7 | O(N^5) | DB: 1)
  * `processRelativeTime$9` (Impact: 301.1 | O(N^5) | DB: 2)
    * *Intent:* //! moment.js locale configuration
  * `translate$5` (Impact: 178.8 | O(N^6) | DB: 1)
  * `translate$9` (Impact: 152.7 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2144`, `structural_boundaries: 1073`, `args: 394`, `func_start: 382`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 554`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 141`
* *Architecture:* `io: 4`, `api: 19`, `import: 1`
* *Defense:* `safety: 453`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `min/moment-with-locales.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.531 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.258 IQR)
- **Top Global Matches:** file_cluster_8: 12.531, file_cluster_7: 13.106, file_cluster_11: 13.127
- **Magnitude:** 7003.64 | **LOC:** 18473 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (47.0695%), Tech Debt (79.1629%)
**Top Internal Functions/Classes:**
  * `relativeTimeMr` (Impact: 359.7 | O(N^5) | DB: 1)
  * `translate$5` (Impact: 178.8 | O(N^6) | DB: 1)
  * `endOf` (Impact: 161.0 | O(N^6) | DB: 26)
  * `startOf` (Impact: 138.2 | O(N^5) | DB: 26)
  * `translate$3` (Impact: 135.1 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2287`, `structural_boundaries: 1191`, `args: 470`, `func_start: 614`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 1503`, `dead_code: 10`, `planned_debt: 7`, `duplicate_logic: 89`, `orphaned_logic: 37`
* *Architecture:* `io: 5`, `api: 1`
* *Defense:* `safety: 378`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `meteor/moment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.162 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.86 IQR)
- **Top Global Matches:** file_cluster_8: 13.162, file_cluster_11: 13.413, file_cluster_0: 13.564
- **Magnitude:** 3835.54 | **LOC:** 5689 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (94.0942%), Tech Debt (52.1737%)
**Top Internal Functions/Classes:**
  * `endOf` (Impact: 161.0 | O(N^6) | DB: 26)
  * `startOf` (Impact: 138.2 | O(N^5) | DB: 26)
  * `localeErasParse` (Impact: 121.0 | O(N^6) | DB: 2)
  * `diff` (Impact: 112.4 | O(N^4) | DB: 3)
  * `toISOString` (Impact: 105.4 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 890`, `structural_boundaries: 504`, `args: 253`, `func_start: 395`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 1196`, `dead_code: 7`, `planned_debt: 6`, `duplicate_logic: 21`
* *Architecture:* `io: 5`, `api: 28`
* *Defense:* `safety: 126`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `moment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.162 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.86 IQR)
- **Top Global Matches:** file_cluster_8: 13.162, file_cluster_11: 13.413, file_cluster_0: 13.564
- **Magnitude:** 3835.54 | **LOC:** 5689 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (94.0942%), Tech Debt (52.1737%)
**Top Internal Functions/Classes:**
  * `endOf` (Impact: 161.0 | O(N^6) | DB: 26)
  * `startOf` (Impact: 138.2 | O(N^5) | DB: 26)
  * `localeErasParse` (Impact: 121.0 | O(N^6) | DB: 2)
  * `diff` (Impact: 112.4 | O(N^4) | DB: 3)
  * `toISOString` (Impact: 105.4 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 890`, `structural_boundaries: 504`, `args: 253`, `func_start: 395`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 1196`, `dead_code: 7`, `planned_debt: 6`, `duplicate_logic: 21`
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.127%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 13`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 1`, `api: 4`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.736
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.032406
  * `Imports (Out-Degree: 1):` has-own-prop, is-function
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/lib/units/day-of-week.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.121 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.107 IQR)
- **Top Global Matches:** file_cluster_13: 13.121, file_cluster_11: 13.301, file_cluster_8: 13.453
- **Magnitude:** 484.14 | **LOC:** 433 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (82.9676%), Tech Debt (99.6215%)
**Top Internal Functions/Classes:**
  * `addWeekParseToken` (Impact: 151.1 | O(N^4) | DB: 17)
  * `weekdaysRegex` (Impact: 32.1 | O(N^3) | DB: 7)
  * `weekdaysShortRegex` (Impact: 32.1 | O(N^3) | DB: 7)
  * `weekdaysMinRegex` (Impact: 32.1 | O(N^3) | DB: 7)
  * `getSetISODayOfWeek` (Impact: 19.0 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 49`, `args: 15`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 161`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.288
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.011058
  * `Imports (Out-Degree: 7):` get-set, is-array, regex, has-own-prop, token, format, utc, to-int...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/test/moment/create.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.786 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.281 IQR)
- **Top Global Matches:** file_cluster_8: 9.786, file_cluster_7: 10.511, file_cluster_1: 10.643
- **Magnitude:** 473.28 | **LOC:** 2920 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (3.8483%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 49.8 | O(N^3))
  * `test` (Impact: 42.9 | O(N^6) | DB: 2)
  * `test` (Impact: 25.6 | O(N^3))
  * `test` (Impact: 22.2 | O(N^3) | DB: 1)
  * `test` (Impact: 17.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 36`, `args: 60`, `func_start: 182`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 43`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 53`
* *Architecture:* `import: 4`
* *Defense:* `safety: 18`, `test: 316`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` each-own-prop, qunit, has-own-prop, moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/units/era.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.927 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.006 IQR)
- **Top Global Matches:** file_cluster_8: 11.927, file_cluster_13: 11.981, file_cluster_11: 12.325
- **Magnitude:** 467.66 | **LOC:** 294 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (78.4202%), Tech Debt (42.99%)
**Top Internal Functions/Classes:**
  * `localeErasParse` (Impact: 121.0 | O(N^6) | DB: 2)
  * `localeEras` (Impact: 49.0 | O(N^4) | DB: 2)
  * `getEraYear` (Impact: 31.6 | O(N^4) | DB: 5)
  * `getEraName` (Impact: 21.7 | O(N^3) | DB: 3)
  * `getEraNarrow` (Impact: 21.7 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 53`, `args: 17`, `func_start: 39`
* *Risk/State:* `state_mutation: 93`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `import: 8`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.971
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.00316
  * `Imports (Out-Degree: 5):` regex, has-own-prop, locales, constants, token, hooks, format, parsing-flags
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/lib/moment/start-end-of.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.113 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.784 IQR)
- **Top Global Matches:** file_cluster_8: 13.113, file_cluster_13: 13.271, file_cluster_11: 13.49
- **Magnitude:** 444.84 | **LOC:** 165 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (82.8954%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `endOf` (Impact: 138.5 | O(N^5) | DB: 26)
  * `startOf` (Impact: 115.7 | O(N^4) | DB: 26)
  * `localStartOfDate` (Impact: 12.4 | O(N^2))
  * `utcStartOfDate` (Impact: 12.4 | O(N^2))
  * `mod` (Impact: 1.9 | O(N^1))
    * *Intent:* // actual modulo - handles negative numbers (for dates before 1970):
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 16`, `args: 5`, `func_start: 9`
* *Risk/State:* `state_mutation: 157`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.00158
  * `Imports (Out-Degree: 2):` hooks, aliases
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/lib/units/month.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.567 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.466 IQR)
- **Top Global Matches:** file_cluster_13: 12.567, file_cluster_11: 12.79, file_cluster_8: 13.012
- **Magnitude:** 388.3 | **LOC:** 341 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (78.245%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `addParseToken` (Impact: 101.0 | O(N^4) | DB: 13)
  * `setMonth` (Impact: 70.6 | O(2^N) | DB: 1)
  * `monthsShortRegex` (Impact: 32.1 | O(N^3) | DB: 7)
  * `monthsRegex` (Impact: 32.1 | O(N^3) | DB: 7)
  * `daysInMonth` (Impact: 17.9 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 48`, `args: 15`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 93`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.095
  * `Choke Point (Betweenness):` 0.000369 | `Ripple Effect (Closeness):` 0.013787
  * `Imports (Out-Degree: 11):` get-set, is-array, regex, mod, has-own-prop, is-leap-year, constants, is-number...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/test/moment/locale.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.049 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.522 IQR)
- **Top Global Matches:** file_cluster_8: 9.049, file_cluster_7: 9.879, file_cluster_1: 10.047
- **Magnitude:** 337.24 | **LOC:** 1033 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.7795%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 64.1 | O(2^N))
  * `test` (Impact: 21.5 | O(2^N) | DB: 1)
  * `test` (Impact: 15.1 | O(N^2))
  * `test` (Impact: 14.9 | O(N^3))
  * `module` (Impact: 14.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 32`, `args: 45`, `func_start: 76`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 20`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 41`
* *Architecture:* `import: 4`
* *Defense:* `safety: 3`, `test: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` index-of, each, qunit, moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tasks/transpile.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.845 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.907 IQR)
- **Top Global Matches:** file_cluster_4: 10.845, file_cluster_8: 11.198, file_cluster_17: 11.29
- **Magnitude:** 293.26 | **LOC:** 363 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (67.8158%), Tech Debt (11.4794%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 175.7 | O(N^6) | DB: 57)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 44`, `args: 42`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 40`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 13`, `api: 2`, `concurrency: 69`, `import: 6`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , esperanto, rollup-plugin-babel, path, moment, moment-with-locales.custom.js, es6-promise, rollup
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/duration.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.816 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.139 IQR)
- **Top Global Matches:** file_cluster_8: 8.816, file_cluster_7: 9.681, file_cluster_1: 9.857
- **Magnitude:** 272.46 | **LOC:** 2031 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (2.8325%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 23.1 | O(N^4) | DB: 1)
  * `test` (Impact: 8.4 | O(2^N))
  * `test` (Impact: 6.2 | O(N^2))
  * `test` (Impact: 5.9 | O(N^2) | DB: 1)
  * `test` (Impact: 5.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 21`, `args: 52`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 26`, `dead_code: 5`, `duplicate_logic: 51`
* *Architecture:* `import: 2`
* *Defense:* `safety: 5`, `test: 629`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qunit, moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `moment.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.269 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.757 IQR)
- **Top Global Matches:** file_cluster_8: 11.269, file_cluster_7: 11.519, file_cluster_1: 11.829
- **Magnitude:** 257.73 | **LOC:** 797 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (9.7913%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `moment` (Impact: 2473.2 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 155`, `args: 263`, `func_start: 253`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 13`
* *Architecture:* `api: 80`
* *Defense:* `safety: 17`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ts3.1-typings/moment.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.927 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.753 IQR)
- **Top Global Matches:** file_cluster_8: 10.927, file_cluster_7: 11.166, file_cluster_1: 11.472
- **Magnitude:** 257.15 | **LOC:** 786 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (10.0424%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `moment` (Impact: 2472.6 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 149`, `args: 262`, `func_start: 252`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 13`
* *Architecture:* `api: 75`
* *Defense:* `safety: 5`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/format.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.448 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.757 IQR)
- **Top Global Matches:** file_cluster_8: 9.448, file_cluster_7: 10.176, file_cluster_1: 10.262
- **Magnitude:** 235.2 | **LOC:** 952 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (4.0936%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 21.9 | O(N^2) | DB: 1)
  * `test` (Impact: 18.5 | O(N^4) | DB: 9)
  * `test` (Impact: 8.7 | O(N^3) | DB: 1)
  * `test` (Impact: 8.1 | O(N^2) | DB: 1)
  * `test` (Impact: 8.1 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 32`, `args: 44`, `func_start: 99`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 34`, `dead_code: 3`, `duplicate_logic: 38`
* *Architecture:* `import: 3`
* *Defense:* `safety: 2`, `test: 244`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` each-own-prop, qunit, moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/moment/get-set.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.756 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.209 IQR)
- **Top Global Matches:** file_cluster_13: 11.756, file_cluster_0: 12.04, file_cluster_11: 12.07
- **Magnitude:** 231.3 | **LOC:** 118 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (41.096%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `set` (Impact: 107.0 | O(N^4) | DB: 1)
  * `get` (Impact: 70.7 | O(N^3) | DB: 1)
  * `stringSet` (Impact: 18.2 | O(N^3) | DB: 1)
  * `makeGetSet` (Impact: 10.9 | O(N^3))
  * `stringGet` (Impact: 5.5 | O(N^2))
    * *Intent:* // MOMENTS
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 37`, `args: 6`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 9`, `dead_code: 2`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.457
  * `Choke Point (Betweenness):` 0.000314 | `Ripple Effect (Closeness):` 0.019747
  * `Imports (Out-Degree: 5):` year, aliases, is-function, hooks, priorities
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/test/moment/zones.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.072 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.799 IQR)
- **Top Global Matches:** file_cluster_8: 9.072, file_cluster_7: 9.841, file_cluster_1: 9.894
- **Magnitude:** 223.08 | **LOC:** 823 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (4.8983%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 25.7 | O(N^3) | DB: 1)
  * `test` (Impact: 19.4 | O(N^4) | DB: 2)
  * `test` (Impact: 12.4 | O(N^3) | DB: 4)
  * `test` (Impact: 6.7 | O(2^N))
  * `test` (Impact: 6.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 29`, `args: 37`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 40`, `duplicate_logic: 32`
* *Architecture:* `import: 2`
* *Defense:* `test: 229`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qunit, moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/units/offset.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.967 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.803 IQR)
- **Top Global Matches:** file_cluster_13: 12.967, file_cluster_8: 13.36, file_cluster_11: 13.478
- **Magnitude:** 215.0 | **LOC:** 250 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (71.095%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cloneWithOffset` (Impact: 22.5 | O(N^4) | DB: 1)
    * *Intent:* // Return a moment from input, that is local/utc/zone equivalent to model.
  * `isDaylightSavingTimeShifted` (Impact: 21.8 | O(N^3) | DB: 7)
  * `offsetFromString` (Impact: 19.0 | O(N^2) | DB: 1)
  * `offset` (Impact: 14.7 | O(2^N) | DB: 2)
    * *Intent:* // FORMATTING
  * `hasAlignedHourOffset` (Impact: 8.2 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 43`, `args: 13`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 87`
* *Architecture:* `api: 15`, `import: 15`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.374
  * `Choke Point (Betweenness):` 0.000808 | `Ripple Effect (Closeness):` 0.006319
  * `Imports (Out-Degree: 10):` is-date, is-undefined, regex, zero-fill, local, compare-arrays, token, from-anything...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/test/moment/utc_offset.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.035 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.655 IQR)
- **Top Global Matches:** file_cluster_8: 9.035, file_cluster_7: 9.816, file_cluster_1: 9.895
- **Magnitude:** 214.6 | **LOC:** 895 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (4.5659%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 25.7 | O(N^3) | DB: 1)
  * `test` (Impact: 19.4 | O(N^4) | DB: 2)
  * `test` (Impact: 12.4 | O(N^3) | DB: 4)
  * `test` (Impact: 7.5 | O(N^3) | DB: 1)
  * `test` (Impact: 5.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 27`, `args: 35`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 40`, `duplicate_logic: 31`
* *Architecture:* `import: 2`
* *Defense:* `test: 244`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qunit, moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/create/from-string.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.693 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.806 IQR)
- **Top Global Matches:** file_cluster_8: 9.693, file_cluster_13: 10.045, file_cluster_7: 10.423
- **Magnitude:** 214.24 | **LOC:** 259 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (37.6944%), Tech Debt (44.6274%)
**Top Internal Functions/Classes:**
  * `configFromISO` (Impact: 111.9 | O(N^5) | DB: 1)
    * *Intent:* // date from iso format
  * `calculateOffset` (Impact: 20.6 | O(N^3) | DB: 1)
  * `checkWeekday` (Impact: 15.8 | O(N^4) | DB: 1)
  * `configFromRFC2822` (Impact: 15.2 | O(N^3) | DB: 1)
    * *Intent:* // date and time from ref 2822 format
  * `untruncateYear` (Impact: 10.8 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 31`, `args: 7`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.352
  * `Choke Point (Betweenness):` 0.000233 | `Ripple Effect (Closeness):` 0.010376
  * `Imports (Out-Degree: 6):` from-string-and-format, parsing-flags, day-of-week, hooks, month, deprecate, date-from-array
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/lib/duration/humanize.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.14 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.811 IQR)
- **Top Global Matches:** file_cluster_8: 11.14, file_cluster_13: 11.505, file_cluster_0: 11.633
- **Magnitude:** 202.66 | **LOC:** 115 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (56.594%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `relativeTime` (Impact: 127.0 | O(N^3) | DB: 1)
  * `humanize` (Impact: 29.4 | O(N^3) | DB: 4)
  * `getSetRelativeTimeThreshold` (Impact: 11.0 | O(N^2))
    * *Intent:* // This function allows you to set a threshold for relative time strings
  * `getSetRelativeTimeRounding` (Impact: 8.3 | O(N^2))
    * *Intent:* // This function allows you to set the rounding function for relative time strings
  * `substituteTimeAgo` (Impact: 5.0 | O(N^1))
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

### `src/lib/moment/compare.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.657 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.483 IQR)
- **Top Global Matches:** file_cluster_13: 13.657, file_cluster_8: 13.929, file_cluster_11: 14.048
- **Magnitude:** 198.22 | **LOC:** 73 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (87.4286%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isBetween` (Impact: 45.5 | O(N^3) | DB: 6)
  * `isSame` (Impact: 28.6 | O(N^3) | DB: 5)
  * `isAfter` (Impact: 18.8 | O(N^2) | DB: 4)
  * `isBefore` (Impact: 18.8 | O(N^2) | DB: 4)
  * `isSameOrAfter` (Impact: 3.6 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 26`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` local, aliases, constructor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/moment/is_valid.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.274 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.7 IQR)
- **Top Global Matches:** file_cluster_8: 9.274, file_cluster_7: 10.091, file_cluster_1: 10.119
- **Magnitude:** 184.98 | **LOC:** 587 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.5432%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 25.6 | O(N^3))
  * `test` (Impact: 14.0 | O(N^2))
  * `test` (Impact: 14.0 | O(N^2))
  * `test` (Impact: 12.2 | O(N^3) | DB: 1)
  * `test` (Impact: 8.9 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 10`, `args: 27`, `func_start: 89`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 9`, `duplicate_logic: 26`
* *Architecture:* `import: 3`
* *Defense:* `safety: 8`, `test: 174`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` each, qunit, moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/moment/format.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.388 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.329 IQR)
- **Top Global Matches:** file_cluster_13: 12.388, file_cluster_8: 12.562, file_cluster_11: 12.855
- **Magnitude:** 176.7 | **LOC:** 79 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (69.9395%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `toISOString` (Impact: 88.1 | O(2^N) | DB: 6)
  * `inspect` (Impact: 16.6 | O(N^2) | DB: 8)
    * *Intent:* /**
  * `format` (Impact: 10.8 | O(N^3) | DB: 3)
  * `toString` (Impact: 1.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 52`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` hooks, format, is-function
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `benchmarks/load-missing.js` (JAVASCRIPT) | Magnitude: 6.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, import: 2, structural_boundaries: 1, args: 1
- `src/lib/units/millisecond.js` (JAVASCRIPT) | Magnitude: 41.16 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 16, func_start: 15, state_mutation: 11
- `src/lib/utils/deprecate.js` (JAVASCRIPT) | Magnitude: 97.16 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, branch: 12, state_mutation: 12, structural_boundaries: 10
- `src/test/moment/deprecate.js` (JAVASCRIPT) | Magnitude: 4.18 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: func_start: 4, test: 4, indent_spaces: 4, structural_boundaries: 3
- `src/test/helpers/each-own-prop.js` (JAVASCRIPT) | Magnitude: 3.02 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, func_start: 2, import: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/lib/moment/now.js` (JAVASCRIPT) | Magnitude: 11.16 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, state_mutation: 3, time_date_logic: 3, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `locale/ku-kmr.js` (JAVASCRIPT) | Magnitude: 0.09 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 100, branch: 21, structural_boundaries: 12, state_mutation: 10
- `src/lib/locale/formats.js` (JAVASCRIPT) | Magnitude: 0.05 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 14, structural_boundaries: 9, branch: 6
- `scripts/locales.js` (JAVASCRIPT) | Magnitude: 127.32 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 39, args: 21, structural_boundaries: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `benchmarks/endOf.js` (JAVASCRIPT) | Magnitude: 15.28 | Delta: **0.225 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, concurrency: 6, state_mutation: 5
- `benchmarks/startOf.js` (JAVASCRIPT) | Magnitude: 15.28 | Delta: **0.225 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, concurrency: 6, state_mutation: 5
- `benchmarks/subtract.js` (JAVASCRIPT) | Magnitude: 15.28 | Delta: **0.225 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, concurrency: 6, state_mutation: 5
- `benchmarks/add.js` (JAVASCRIPT) | Magnitude: 16.28 | Delta: **0.229 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, state_mutation: 6, concurrency: 6
- `benchmarks/set.js` (JAVASCRIPT) | Magnitude: 16.26 | Delta: **0.296 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 7, state_mutation: 6, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/lib/utils/keys.js` (JAVASCRIPT) | Magnitude: 23.84 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 9, branch: 5, structural_boundaries: 5
- `src/lib/units/hour.js` (JAVASCRIPT) | Magnitude: 103.48 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, func_start: 43, structural_boundaries: 28, state_mutation: 27
- `src/lib/locale/lists.js` (JAVASCRIPT) | Magnitude: 0.1 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 21, state_mutation: 16, branch: 13
- `ender.js` (JAVASCRIPT) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1
- `src/lib/units/week-year.js` (JAVASCRIPT) | Magnitude: 90.88 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
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

- `src/test/helpers/deprecation-handler.js` -> **Severity: 9.882** (Embedded: 0.1532 * Error Risk: 64.4828%)
- `src/test/qunit.js` -> **Severity: 2.139** (Embedded: 0.3033 * Error Risk: 7.052%)
- `src/test/helpers/each.js` -> **Severity: 2.018** (Embedded: 0.1058 * Error Risk: 19.0858%)
- `src/lib/parse/token.js` -> **Severity: 1.479** (Embedded: 0.0324 * Error Risk: 45.625%)
- `src/lib/moment/get-set.js` -> **Severity: 1.284** (Embedded: 0.0197 * Error Risk: 65.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/lib/units/aliases.js` -> **Severity: 486.946** (Blast Radius: 5.032 * Doc Risk: 96.7699%)
- `src/lib/create/from-anything.js` -> **Severity: 415.433** (Blast Radius: 5.238 * Doc Risk: 79.3113%)
- `src/lib/utils/abs-floor.js` -> **Severity: 399.419** (Blast Radius: 8.559 * Doc Risk: 46.6666%)
- `src/lib/utils/to-int.js` -> **Severity: 398.155** (Blast Radius: 6.636 * Doc Risk: 59.9993%)
- `src/lib/parse/token.js` -> **Severity: 373.595** (Blast Radius: 3.736 * Doc Risk: 99.9986%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
