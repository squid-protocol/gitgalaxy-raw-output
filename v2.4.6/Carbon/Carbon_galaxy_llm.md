# ARCHITECTURAL_BRIEF: Carbon
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/Carbon` |
| **Timestamp** | `2026-08-03T19:30:38.050755+00:00` |
| **Scan Duration** | `3.16s` |
| **Git Branch** | `master` |
| **Git Commit** | `e890471a3494740f7d9326d72ce6a8c559ffee60` |
| **Git Remote** | `https://github.com/briannesbitt/Carbon.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 948 malicious artifacts.

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
| Total Artifacts | 2034 |
| Analyzed Artifacts (Scanned) | 956 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1078 |
| Total LOC | 27728 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 47.0% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4747 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4234 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1274 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 947 | 27567 | 99.1% |
| YAML | 3 | 32 | 0.3% |
| MARKDOWN | 2 | 0 | 0.2% |
| XML | 2 | 0 | 0.2% |
| BATCH | 1 | 4 | 0.1% |
| JSON | 1 | 125 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.049`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 550 | 57.5% |
| file_cluster_13 | 403 | 42.2% |
| file_cluster_1 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1078*

**Composition by Extension & Reason:**
- `.php`: 1031x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Saturation: Line 28 exceeds 500 chars), 2x Excluded (Saturation: Line 26 exceeds 500 chars)
- `.yml`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 4x Excluded (Unsupported Extension: '.neon')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dist`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (Binary Format Detected)
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 85.2 | 7.8 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.9 | 1.1 | 0.3 |
| API Exposure | 0.0 | 17.0 | 0.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 51.9 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.9 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 58.6 | 66.7 | 100.0 |
| Instability Exposure | 0.0 | 4.8 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 33.5 | 0.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 14.6 | 12.3 | 12.3 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `phpdoc.php` (Hits: 6)
- `tests/remove-comments-in-switch.php` (Hits: 2)
- `bin/carbon` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **InvalidArgumentException.php** (`src/Carbon/Exceptions/InvalidArgumentException.php`) — 22 inbound connections
2. **Carbon.php** (`src/Carbon/Carbon.php`) — 20 inbound connections
3. **CarbonImmutable.php** (`src/Carbon/CarbonImmutable.php`) — 15 inbound connections
4. **CarbonInterval.php** (`src/Carbon/CarbonInterval.php`) — 14 inbound connections
5. **FactoryImmutable.php** (`src/Carbon/FactoryImmutable.php`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **so.php** (`src/Carbon/Lang/so.php`) — 97 outbound dependencies
2. **ku.php** (`src/Carbon/Lang/ku.php`) — 93 outbound dependencies
3. **lzh_TW.php** (`src/Carbon/Lang/lzh_TW.php`) — 93 outbound dependencies
4. **yi_US.php** (`src/Carbon/Lang/yi_US.php`) — 92 outbound dependencies
5. **ksh.php** (`src/Carbon/Lang/ksh.php`) — 88 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__construct` (@ `src/Carbon/CarbonInterval.php`) -> Impact: **2064.8** | LOC: 135
  * *Intent:* * @method $this floorQuarters(int|float $precision = 1) Truncate the current instance quarter with given precision. * @method $this ceilQuarter(int|fl...
- `__construct` (@ `src/Carbon/CarbonPeriod.php`) -> Impact: **673.3** | LOC: 130
- `fromString` (@ `src/Carbon/CarbonInterval.php`) -> Impact: **519.2** | LOC: 165
  * *Intent:* /** * Returns the factor for a given source-to-target couple. * * @param string $source
- `forHumans` (@ `src/Carbon/CarbonInterval.php`) -> Impact: **471.7** | LOC: 200
- `__unserialize` (@ `src/Carbon/CarbonPeriod.php`) -> Impact: **326.0** | LOC: 80
- `translateTimeString` (@ `src/Carbon/Traits/Localization.php`) -> Impact: **313.5** | LOC: 98
- `__unserialize` (@ `src/Carbon/CarbonInterval.php`) -> Impact: **291.4** | LOC: 67
  * *Intent:* /** * Allow fluent calls on the setters... CarbonInterval::years(3)->months(5)->day(). * * Note: This is done using the magic method to allow static a...
- `__call` (@ `src/Carbon/CarbonPeriod.php`) -> Impact: **288.0** | LOC: 149
- `rawCreateFromFormat` (@ `src/Carbon/Traits/Creator.php`) -> Impact: **229.9** | LOC: 38
  * *Intent:* /** * Create a new safe Carbon instance from a specific date and time. * * If any of $year, $month or $day are set to null their now() values will * b...
- `addUnit` (@ `src/Carbon/Traits/Units.php`) -> Impact: **200.2** | LOC: 84

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__construct` (@ `src/Carbon/CarbonInterval.php`) -> **O(2^N) [Recursive]**
  * *Intent:* * @method $this floorQuarters(int|float $precision = 1) Truncate the current instance quarter with given precision. * @method $this ceilQuarter(int|fl...
- `__construct` (@ `src/Carbon/CarbonPeriod.php`) -> **O(2^N) [Recursive]**
- `__unserialize` (@ `src/Carbon/CarbonPeriod.php`) -> **O(2^N) [Recursive]**
- `locale` (@ `src/Carbon/Traits/Localization.php`) -> **O(2^N) [Recursive]**
- `__unserialize` (@ `src/Carbon/CarbonInterval.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Allow fluent calls on the setters... CarbonInterval::years(3)->months(5)->day(). * * Note: This is done using the magic method to allow static a...
- `cast` (@ `src/Carbon/CarbonPeriod.php`) -> **O(2^N) [Recursive]**
- `cast` (@ `src/Carbon/Traits/Cast.php`) -> **O(2^N) [Recursive]**
- `rawCreateFromFormat` (@ `src/Carbon/Traits/Creator.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Create a new safe Carbon instance from a specific date and time. * * If any of $year, $month or $day are set to null their now() values will * b...
- `acceptClosuresFrom` (@ `tests/AbstractTestCase.php`) -> **O(2^N) [Recursive]**
- `format` (@ `lazy/Carbon/MessageFormatter/MessageFormatterMapperStrongType.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * This file is part of the Carbon package. * * (c) Brian Nesbitt <brian@nesbot.com> * * For the full copyright and license information, please vie...

### Highest Data Gravity (Database Complexity)
- `forHumans` (@ `src/Carbon/CarbonInterval.php`) -> DB Complexity: **64**
- `__construct` (@ `src/Carbon/CarbonInterval.php`) -> DB Complexity: **47**
  * *Intent:* * @method $this floorQuarters(int|float $precision = 1) Truncate the current instance quarter with given precision. * @method $this ceilQuarter(int|fl...
- `addUnit` (@ `src/Carbon/Traits/Units.php`) -> DB Complexity: **36**
- `__construct` (@ `src/Carbon/CarbonPeriod.php`) -> DB Complexity: **35**
- `roundUnit` (@ `src/Carbon/Traits/Rounding.php`) -> DB Complexity: **34**
- `fromString` (@ `src/Carbon/CarbonInterval.php`) -> DB Complexity: **31**
  * *Intent:* /** * Returns the factor for a given source-to-target couple. * * @param string $source
- `total` (@ `src/Carbon/CarbonInterval.php`) -> DB Complexity: **29**
- `create` (@ `src/Carbon/Traits/Creator.php`) -> DB Complexity: **28**
- `__unserialize` (@ `src/Carbon/CarbonInterval.php`) -> DB Complexity: **26**
  * *Intent:* /** * Allow fluent calls on the setters... CarbonInterval::years(3)->months(5)->day(). * * Note: This is done using the magic method to allow static a...
- `translateTimeString` (@ `src/Carbon/Traits/Localization.php`) -> DB Complexity: **26**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Carbon` | 19 | 13139.24 | 36.66% | 4.28% |
| `src/Carbon/Lang` | 803 | 11114.2 | 5.76% | 9.07% |
| `src/Carbon/Traits` | 27 | 7578.08 | 26.32% | 40.15% |
| `__monolith__` | 8 | 815.42 | 7.68% | 12.5% |
| `tests` | 4 | 715.46 | 14.83% | 0.0% |
| `src/Carbon/Exceptions` | 30 | 683.76 | 18.63% | 2.88% |
| `src/Carbon/PHPStan` | 2 | 265.34 | 31.64% | 91.05% |
| `src/Carbon/Laravel` | 1 | 255.58 | 39.63% | 85.37% |
| `tests/Laravel` | 8 | 173.86 | 6.38% | 0.0% |
| `lazy/Carbon` | 4 | 122.72 | 18.05% | 47.14% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/Carbon/Lang/be_BY.php` -> **100.0%** Exposure
- `src/Carbon/Lang/de_BE.php` -> **100.0%** Exposure
- `src/Carbon/Lang/de_DE.php` -> **100.0%** Exposure
- `src/Carbon/Lang/de_LU.php` -> **100.0%** Exposure
- `src/Carbon/Lang/el_CY.php` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/carbon` -> **100.0%** Exposure
- `lazy/Carbon/TranslatorStrongType.php` -> **100.0%** Exposure
- `phpdoc.php` -> **100.0%** Exposure
- `src/Carbon/AbstractTranslator.php` -> **100.0%** Exposure
- `src/Carbon/CarbonInterval.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/Carbon/Traits/Converter.php` -> **26** Orphaned Functions | **0** Duplicates
- `src/Carbon/Traits/Boundaries.php` -> **20** Orphaned Functions | **0** Duplicates
- `tests/AbstractTestCase.php` -> **18** Orphaned Functions | **0** Duplicates
- `src/Carbon/Traits/Comparison.php` -> **16** Orphaned Functions | **0** Duplicates
- `src/Carbon/PHPStan/MacroMethodReflection.php` -> **14** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/Carbon/Lang/so.php`** -> AI Confidence: **99.48%**
2. **`src/Carbon/CarbonInterval.php`** -> AI Confidence: **99.31%**
3. **`src/Carbon/CarbonPeriod.php`** -> AI Confidence: **99.31%**
4. **`src/Carbon/Factory.php`** -> AI Confidence: **99.31%**
5. **`src/Carbon/Lang/nl_AW.php`** -> AI Confidence: **99.31%**
6. **`src/Carbon/Lang/nl_NL.php`** -> AI Confidence: **99.31%**
7. **`src/Carbon/Traits/Creator.php`** -> AI Confidence: **99.31%**
8. **`src/Carbon/Traits/Units.php`** -> AI Confidence: **99.31%**
9. **`src/Carbon/Traits/Week.php`** -> AI Confidence: **99.31%**
10. **`tests/AbstractTestCase.php`** -> AI Confidence: **99.31%**
11. **`src/Carbon/Constants/Format.php`** -> AI Confidence: **99.29%**
12. **`src/Carbon/Lang/af.php`** -> AI Confidence: **99.29%**
13. **`src/Carbon/Lang/ar.php`** -> AI Confidence: **99.29%**
14. **`src/Carbon/Lang/ar_DZ.php`** -> AI Confidence: **99.29%**
15. **`src/Carbon/Lang/ar_LY.php`** -> AI Confidence: **99.29%**
16. **`src/Carbon/Lang/ar_MA.php`** -> AI Confidence: **99.29%**
17. **`src/Carbon/Lang/ar_Shakl.php`** -> AI Confidence: **99.29%**
18. **`src/Carbon/Lang/ar_TN.php`** -> AI Confidence: **99.29%**
19. **`src/Carbon/Lang/bm.php`** -> AI Confidence: **99.29%**
20. **`src/Carbon/Lang/br.php`** -> AI Confidence: **99.29%**
21. **`src/Carbon/Lang/bs.php`** -> AI Confidence: **99.29%**
22. **`src/Carbon/Lang/ckb.php`** -> AI Confidence: **99.29%**
23. **`src/Carbon/Lang/da.php`** -> AI Confidence: **99.29%**
24. **`src/Carbon/Lang/el.php`** -> AI Confidence: **99.29%**
25. **`src/Carbon/Lang/eo.php`** -> AI Confidence: **99.29%**
26. **`src/Carbon/Lang/fo.php`** -> AI Confidence: **99.29%**
27. **`src/Carbon/Lang/fr.php`** -> AI Confidence: **99.29%**
28. **`src/Carbon/Lang/ga.php`** -> AI Confidence: **99.29%**
29. **`src/Carbon/Lang/hr.php`** -> AI Confidence: **99.29%**
30. **`src/Carbon/Lang/kk.php`** -> AI Confidence: **99.29%**
31. **`src/Carbon/Lang/km.php`** -> AI Confidence: **99.29%**
32. **`src/Carbon/Lang/ky.php`** -> AI Confidence: **99.29%**
33. **`src/Carbon/Lang/mi.php`** -> AI Confidence: **99.29%**
34. **`src/Carbon/Lang/mt.php`** -> AI Confidence: **99.29%**
35. **`src/Carbon/Lang/nb.php`** -> AI Confidence: **99.29%**
36. **`src/Carbon/Lang/nn.php`** -> AI Confidence: **99.29%**
37. **`src/Carbon/Lang/pl.php`** -> AI Confidence: **99.29%**
38. **`src/Carbon/Lang/pt.php`** -> AI Confidence: **99.29%**
39. **`src/Carbon/Lang/ro.php`** -> AI Confidence: **99.29%**
40. **`src/Carbon/Lang/se.php`** -> AI Confidence: **99.29%**
41. **`src/Carbon/Lang/sq.php`** -> AI Confidence: **99.29%**
42. **`src/Carbon/Lang/sr.php`** -> AI Confidence: **99.29%**
43. **`src/Carbon/Lang/sr_Cyrl.php`** -> AI Confidence: **99.29%**
44. **`src/Carbon/Lang/sw.php`** -> AI Confidence: **99.29%**
45. **`src/Carbon/Lang/tet.php`** -> AI Confidence: **99.29%**
46. **`src/Carbon/Lang/th.php`** -> AI Confidence: **99.29%**
47. **`src/Carbon/Lang/tl.php`** -> AI Confidence: **99.29%**
48. **`src/Carbon/Lang/tzl.php`** -> AI Confidence: **99.29%**
49. **`src/Carbon/Lang/tzm.php`** -> AI Confidence: **99.29%**
50. **`src/Carbon/Lang/tzm_Latn.php`** -> AI Confidence: **99.29%**
51. **`src/Carbon/Lang/ur.php`** -> AI Confidence: **99.29%**
52. **`src/Carbon/Lang/uz.php`** -> AI Confidence: **99.29%**
53. **`src/Carbon/Lang/uz_Latn.php`** -> AI Confidence: **99.29%**
54. **`src/Carbon/Lang/vi.php`** -> AI Confidence: **99.29%**
55. **`src/Carbon/Lang/yo.php`** -> AI Confidence: **99.29%**
56. **`src/Carbon/Lang/zgh.php`** -> AI Confidence: **99.29%**
57. **`src/Carbon/Traits/Localization.php`** -> AI Confidence: **99.25%**
58. **`src/Carbon/CarbonTimeZone.php`** -> AI Confidence: **99.24%**
59. **`src/Carbon/Lang/sr_Latn_ME.php`** -> AI Confidence: **99.24%**
60. **`src/Carbon/Laravel/ServiceProvider.php`** -> AI Confidence: **99.24%**
61. **`src/Carbon/Traits/Mixin.php`** -> AI Confidence: **99.24%**
62. **`src/Carbon/Traits/Test.php`** -> AI Confidence: **99.23%**
63. **`src/Carbon/Lang/sr_Cyrl_BA.php`** -> AI Confidence: **99.18%**
64. **`src/Carbon/Lang/sr_Cyrl_XK.php`** -> AI Confidence: **99.18%**
65. **`src/Carbon/Lang/sr_Latn_BA.php`** -> AI Confidence: **99.18%**
66. **`src/Carbon/Lang/sr_Latn_XK.php`** -> AI Confidence: **99.18%**
67. **`src/Carbon/Traits/Comparison.php`** -> AI Confidence: **99.18%**
68. **`src/Carbon/Traits/Converter.php`** -> AI Confidence: **99.18%**
69. **`src/Carbon/Traits/IntervalStep.php`** -> AI Confidence: **99.18%**
70. **`src/Carbon/Lang/be.php`** -> AI Confidence: **99.17%**
71. **`src/Carbon/Lang/cy.php`** -> AI Confidence: **99.17%**
72. **`src/Carbon/Lang/fy.php`** -> AI Confidence: **99.17%**
73. **`src/Carbon/Lang/gd.php`** -> AI Confidence: **99.17%**
74. **`src/Carbon/Lang/it.php`** -> AI Confidence: **99.17%**
75. **`src/Carbon/Lang/pap.php`** -> AI Confidence: **99.17%**
76. **`src/Carbon/Lang/tr.php`** -> AI Confidence: **99.17%**
77. **`src/Carbon/AbstractTranslator.php`** -> AI Confidence: **99.16%**
78. **`src/Carbon/Lang/aa_DJ.php`** -> AI Confidence: **99.16%**
79. **`src/Carbon/Lang/aa_ER.php`** -> AI Confidence: **99.16%**
80. **`src/Carbon/Lang/aa_ER@saaho.php`** -> AI Confidence: **99.16%**
81. **`src/Carbon/Lang/aa_ET.php`** -> AI Confidence: **99.16%**
82. **`src/Carbon/Lang/af_NA.php`** -> AI Confidence: **99.16%**
83. **`src/Carbon/Lang/agq.php`** -> AI Confidence: **99.16%**
84. **`src/Carbon/Lang/agr_PE.php`** -> AI Confidence: **99.16%**
85. **`src/Carbon/Lang/ak_GH.php`** -> AI Confidence: **99.16%**
86. **`src/Carbon/Lang/am_ET.php`** -> AI Confidence: **99.16%**
87. **`src/Carbon/Lang/an_ES.php`** -> AI Confidence: **99.16%**
88. **`src/Carbon/Lang/anp_IN.php`** -> AI Confidence: **99.16%**
89. **`src/Carbon/Lang/ar_IN.php`** -> AI Confidence: **99.16%**
90. **`src/Carbon/Lang/ar_SS.php`** -> AI Confidence: **99.16%**
91. **`src/Carbon/Lang/as_IN.php`** -> AI Confidence: **99.16%**
92. **`src/Carbon/Lang/asa.php`** -> AI Confidence: **99.16%**
93. **`src/Carbon/Lang/ast.php`** -> AI Confidence: **99.16%**
94. **`src/Carbon/Lang/ayc_PE.php`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `phpdoc.php` -> **100.0%** Exposure
- `src/Carbon/AbstractTranslator.php` -> **100.0%** Exposure
- `src/Carbon/CarbonInterval.php` -> **100.0%** Exposure
- `src/Carbon/CarbonPeriod.php` -> **100.0%** Exposure
- `src/Carbon/CarbonTimeZone.php` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `tests/remove-comments-in-switch.php` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `lazy/Carbon/MessageFormatter/MessageFormatterMapperWeakType.php` -> **100.0%** Exposure
- `lazy/Carbon/TranslatorStrongType.php` -> **100.0%** Exposure
- `lazy/Carbon/TranslatorWeakType.php` -> **100.0%** Exposure
- `phpdoc.php` -> **100.0%** Exposure
- `src/Carbon/AbstractTranslator.php` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13527` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Carbon/Traits/Creator.php` (PHP) -> Cumulative Risk: **807.89**
- **Archetype:** `file_cluster_13` (Distance: 15.277 IQR)
- **Magnitude:** 1400.0 | **LOC:** 932 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `rawCreateFromFormat` (Impact: 229.9), `__construct` (Impact: 192.3), `create` (Impact: 181.1)

### 2. `src/Carbon/Traits/Week.php` (PHP) -> Cumulative Risk: **784.91**
- **Archetype:** `file_cluster_13` (Distance: 16.328 IQR)
- **Magnitude:** 423.0 | **LOC:** 224 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `weekYear` (Impact: 142.4), `week` (Impact: 65.0), `weeksInYear` (Impact: 25.1)

### 3. `src/Carbon/Traits/Units.php` (PHP) -> Cumulative Risk: **777.02**
- **Archetype:** `file_cluster_13` (Distance: 14.592 IQR)
- **Magnitude:** 616.6 | **LOC:** 473 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `addUnit` (Impact: 200.2), `add` (Impact: 81.7), `sub` (Impact: 81.7)

### 4. `src/Carbon/Traits/Rounding.php` (PHP) -> Cumulative Risk: **769.5**
- **Archetype:** `file_cluster_13` (Distance: 13.674 IQR)
- **Magnitude:** 326.98 | **LOC:** 227 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `roundUnit` (Impact: 146.0), `ceilWeek` (Impact: 25.3), `floor` (Impact: 7.5)

### 5. `src/Carbon/PHPStan/MacroExtension.php` (PHP) -> Cumulative Risk: **765.05**
- **Archetype:** `file_cluster_13` (Distance: 13.788 IQR)
- **Magnitude:** 171.24 | **LOC:** 138 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getMethod` (Impact: 72.0), `hasMethod` (Impact: 14.6), `__construct` (Impact: 2.9)

### 6. `src/Carbon/Traits/Difference.php` (PHP) -> Cumulative Risk: **736.88**
- **Archetype:** `file_cluster_13` (Distance: 14.691 IQR)
- **Magnitude:** 557.8 | **LOC:** 856 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `calendar` (Impact: 55.8), `diffInMonths` (Impact: 46.3), `diffInDays` (Impact: 29.2)

### 7. `src/Carbon/Traits/Converter.php` (PHP) -> Cumulative Risk: **732.89**
- **Archetype:** `file_cluster_13` (Distance: 12.46 IQR)
- **Magnitude:** 365.0 | **LOC:** 557 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9928%)
- **Heaviest Functions:** `format` (Impact: 48.8), `toPeriod` (Impact: 37.3), `toISOString` (Impact: 34.9)

### 8. `src/Carbon/Traits/Timestamp.php` (PHP) -> Cumulative Risk: **730.36**
- **Archetype:** `file_cluster_8` (Distance: 12.722 IQR)
- **Magnitude:** 148.28 | **LOC:** 193 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getIntegerAndDecimalParts` (Impact: 21.9), `createFromTimestampMsUTC` (Impact: 11.1), `createFromTimestampMs` (Impact: 6.4)

### 9. `src/Carbon/CarbonPeriod.php` (PHP) -> Cumulative Risk: **725.75**
- **Archetype:** `file_cluster_13` (Distance: 14.835 IQR)
- **Magnitude:** 3910.54 | **LOC:** 2719 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__construct` (Impact: 673.3), `__unserialize` (Impact: 326.0), `__call` (Impact: 288.0)

### 10. `src/Carbon/Laravel/ServiceProvider.php` (PHP) -> Cumulative Risk: **724.78**
- **Archetype:** `file_cluster_13` (Distance: 12.582 IQR)
- **Magnitude:** 255.58 | **LOC:** 179 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `getLocale` (Impact: 35.3), `getFallbackLocale` (Impact: 35.2), `updateFallbackLocale` (Impact: 31.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Carbon/CarbonInterval.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.118 IQR)
- **Top Global Matches:** file_cluster_13: 15.118, file_cluster_8: 15.323, file_cluster_7: 15.365
- **Magnitude:** 6181.24 | **LOC:** 3574 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (47.8187%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 2064.8 | O(2^N) | DB: 47)
    * *Intent:* * @method $this floorQuarters(int|float $precision = 1) Truncate the current instance quarter with g...
  * `fromString` (Impact: 519.2 | O(N^6) | DB: 31)
    * *Intent:* /** * Returns the factor for a given source-to-target couple. * * @param string $source
  * `forHumans` (Impact: 471.7 | O(N^6) | DB: 64)
  * `__unserialize` (Impact: 291.4 | O(2^N) | DB: 26)
    * *Intent:* /** * Allow fluent calls on the setters... CarbonInterval::years(3)->months(5)->day(). * * Note: Thi...
  * `total` (Impact: 142.8 | O(N^5) | DB: 29)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 489`, `structural_boundaries: 348`, `args: 106`, `func_start: 99`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1147`
* *Architecture:* `api: 113`, `import: 39`
* *Defense:* `safety: 76`, `doc: 424`, `test: 2`, `immutability_locks: 12`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.909
  * `Choke Point (Betweenness):` 0.000786 | `Ripple Effect (Closeness):` 0.01441
  * `Imports (Out-Degree: 22):` Carbon\Exceptions\InvalidIntervalException, Carbon\Exceptions\UnknownGetterException, Throwable, Exception, MagicParameter, Options, LocalFactory, ReflectionException...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/Carbon/CarbonPeriod.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.835 IQR)
- **Top Global Matches:** file_cluster_13: 14.835, file_cluster_8: 15.008, file_cluster_7: 15.08
- **Magnitude:** 3910.54 | **LOC:** 2719 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (47.1929%), Tech Debt (10.4599%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 673.3 | O(2^N) | DB: 35)
  * `__unserialize` (Impact: 326.0 | O(2^N) | DB: 11)
  * `__call` (Impact: 288.0 | O(N^5) | DB: 9)
  * `initializeSerialization` (Impact: 122.1 | O(N^4) | DB: 3)
    * *Intent:* /**
  * `parseIso8601` (Impact: 91.3 | O(N^4) | DB: 17)
    * *Intent:* /** * Number of maximum attempts before giving up on finding end date. * * @var int
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 434`, `args: 138`, `func_start: 130`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 698`, `fragile_debt: 3`
* *Architecture:* `api: 135`, `concurrency: 7`, `import: 38`
* *Defense:* `safety: 99`, `doc: 325`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.744
  * `Choke Point (Betweenness):` 0.00021 | `Ripple Effect (Closeness):` 0.007964
  * `Imports (Out-Degree: 19):` 
    public function endsAfter(mixed $date = null): bool
    
        return $this->calculateEnd()->greaterThan($this->resolveCarbon($date), Throwable, 'current' => [$this, _start_date' => $values['include_start_date'] ?? true, 'locale'], Carbon\Exceptions\UnreachableException, Countable, _start_date' => [$this...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Localization.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.716 IQR)
- **Top Global Matches:** file_cluster_13: 14.716, file_cluster_11: 14.897, file_cluster_8: 14.908
- **Magnitude:** 1484.42 | **LOC:** 748 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (42.5368%), Tech Debt (9.4523%)
**Top Internal Functions/Classes:**
  * `translateTimeString` (Impact: 313.5 | O(N^6) | DB: 26)
  * `setFallbackLocale` (Impact: 99.5 | O(N^6) | DB: 5)
  * `locale` (Impact: 98.3 | O(2^N) | DB: 5)
  * `translateNumber` (Impact: 80.1 | O(N^5) | DB: 16)
  * `cleanWordFromTranslationString` (Impact: 73.3 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 123`, `args: 40`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 289`, `planned_debt: 1`
* *Architecture:* `api: 35`, `import: 11`
* *Defense:* `safety: 35`, `doc: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.593
  * `Choke Point (Betweenness):` 0.000189 | `Ripple Effect (Closeness):` 0.007
  * `Imports (Out-Degree: 6):` Carbon\Translator, Carbon\Exceptions\InvalidTypeException, Symfony\Contracts\Translation\TranslatorInterface, Carbon\CarbonInterface, Carbon\TranslatorStrongTypeInterface, Carbon\Language, Closure, Symfony\Component\Translation\TranslatorBagInterface...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Creator.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.277 IQR)
- **Top Global Matches:** file_cluster_13: 15.277, file_cluster_11: 15.664, file_cluster_8: 15.667
- **Magnitude:** 1400.0 | **LOC:** 932 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (43.3254%), Tech Debt (92.8934%)
**Top Internal Functions/Classes:**
  * `rawCreateFromFormat` (Impact: 229.9 | O(2^N) | DB: 11)
    * *Intent:* /** * Create a new safe Carbon instance from a specific date and time. * * If any of $year, $month o...
  * `__construct` (Impact: 192.3 | O(2^N) | DB: 10)
    * *Intent:* /** * Trait Creator. *
  * `create` (Impact: 181.1 | O(N^5) | DB: 28)
  * `createSafe` (Impact: 111.8 | O(N^5) | DB: 12)
  * `createStrict` (Impact: 51.6 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 118`, `args: 30`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 314`, `fragile_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 21`, `import: 21`
* *Defense:* `safety: 35`, `doc: 98`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` DateTimeImmutable, Exception, Carbon\CarbonInterface, LocalFactory, [null, DateMalformedStringException, '', true...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phpdoc.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.364 IQR)
- **Top Global Matches:** file_cluster_8: 13.364, file_cluster_13: 13.481, file_cluster_17: 13.54
- **Magnitude:** 744.08 | **LOC:** 862 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (37.6829%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dumpType` (Impact: 113.2 | O(2^N) | DB: 4)
  * `compileDoc` (Impact: 106.7 | O(N^5) | DB: 16)
    * *Intent:* /** * %description% * * @var %type% * * @deprecated %line1%
  * `dumpParameter` (Impact: 22.2 | O(N^3) | DB: 7)
  * `cleanClassName` (Impact: 19.0 | O(N^2) | DB: 3)
  * `dumpValue` (Impact: 8.5 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 103`, `args: 12`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 438`, `dead_code: 2`
* *Architecture:* `io: 6`, `api: 2`, `import: 6`
* *Defense:* `safety: 27`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` autoload.php', Carbon\Carbon, Carbon\FactoryImmutable, Carbon\CarbonInterface, Carbon\CarbonImmutable, Carbon\Factory
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/AbstractTestCase.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.881 IQR)
- **Top Global Matches:** file_cluster_13: 12.881, file_cluster_8: 13.076, file_cluster_7: 13.348
- **Magnitude:** 649.52 | **LOC:** 502 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (17.7246%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `acceptClosuresFrom` (Impact: 94.4 | O(2^N) | DB: 1)
  * `assertSameIntervals` (Impact: 70.8 | O(N^3) | DB: 6)
  * `assertCarbonInterval` (Impact: 52.7 | O(N^3) | DB: 9)
  * `assertCarbon` (Impact: 31.8 | O(N^3) | DB: 6)
  * `assertCarbonTime` (Impact: 25.9 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 76`, `args: 26`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 170`, `orphaned_logic: 18`
* *Architecture:* `api: 10`, `import: 20`
* *Defense:* `safety: 19`, `doc: 22`, `test: 17`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.000189 | `Ripple Effect (Closeness):` 0.001047
  * `Imports (Out-Degree: 8):` ErrorException, Throwable, RecursiveIteratorIterator, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\CarbonPeriod, Carbon\Carbon, DateTime...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Units.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.592 IQR)
- **Top Global Matches:** file_cluster_13: 14.592, file_cluster_0: 14.969, file_cluster_8: 14.998
- **Magnitude:** 616.6 | **LOC:** 473 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (38.6124%), Tech Debt (71.5257%)
**Top Internal Functions/Classes:**
  * `addUnit` (Impact: 200.2 | O(N^6) | DB: 36)
  * `add` (Impact: 81.7 | O(2^N) | DB: 7)
  * `sub` (Impact: 81.7 | O(2^N) | DB: 7)
  * `rawAddUnit` (Impact: 30.7 | O(N^4))
    * *Intent:* /** * Add given units or interval to the current instance. * * @example $date->add('hour', 3) * @exa...
  * `subtract` (Impact: 16.4 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 47`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 166`, `orphaned_logic: 6`
* *Architecture:* `api: 10`, `import: 12`
* *Defense:* `safety: 20`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Carbon\CarbonConverterInterface, Carbon\CarbonInterval, Carbon\Exceptions\InvalidIntervalException, Carbon\Unit, Carbon\Exceptions\UnitException, DateMalformedStringException, Carbon\Exceptions\InvalidFormatException, Carbon\CarbonInterface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/AbstractTranslator.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.95 IQR)
- **Top Global Matches:** file_cluster_13: 13.95, file_cluster_8: 14.202, file_cluster_7: 14.348
- **Magnitude:** 588.92 | **LOC:** 1300 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (36.4351%), Tech Debt (70.8158%)
**Top Internal Functions/Classes:**
  * `setLocale` (Impact: 124.2 | O(2^N) | DB: 15)
  * `translate` (Impact: 51.6 | O(N^4) | DB: 7)
  * `resetMessages` (Impact: 46.0 | O(N^5) | DB: 8)
    * *Intent:* /** * Returns the list of directories translation files are searched in. */
  * `get` (Impact: 43.7 | O(N^4) | DB: 5)
    * *Intent:* /** * List of custom localized messages. * * @var array */
  * `compareChunkLists` (Impact: 22.6 | O(N^4) | DB: 4)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 82`, `args: 29`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 160`, `orphaned_logic: 8`
* *Architecture:* `api: 17`, `import: 10`
* *Defense:* `safety: 17`, `doc: 46`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $file, 
    public function getAvailableLocales(string $prefix = ''): array
    
        return array_unique(array_merge(
            array_map(
                static fn (string $file) => substr($file, -4), Throwable, ), Carbon\MessageFormatter\MessageFormatterMapper, strrpos($file, $this->getLocalesFiles($prefix)...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Difference.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.691 IQR)
- **Top Global Matches:** file_cluster_13: 14.691, file_cluster_8: 14.952, file_cluster_7: 14.969
- **Magnitude:** 557.8 | **LOC:** 856 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (44.6924%), Tech Debt (99.9245%)
**Top Internal Functions/Classes:**
  * `calendar` (Impact: 55.8 | O(N^6) | DB: 8)
    * *Intent:* /** * Get the difference by the given interval using a filter closure. * * @param CarbonInterval $ci...
  * `diffInMonths` (Impact: 46.3 | O(N^3) | DB: 17)
  * `diffInDays` (Impact: 29.2 | O(N^3) | DB: 15)
  * `diffInYears` (Impact: 25.6 | O(N^3) | DB: 14)
    * *Intent:* /** * Get the difference as a CarbonInterval instance. * Return relative interval (negative if $abso...
  * `diffFiltered` (Impact: 23.2 | O(N^3) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 66`, `args: 28`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 255`, `fragile_debt: 2`, `orphaned_logic: 12`
* *Architecture:* `api: 24`, `import: 10`
* *Defense:* `safety: 4`, `doc: 123`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\CarbonInterval, Carbon\Exceptions\UnknownUnitException, Carbon\Unit, Carbon\CarbonPeriod, Carbon\Carbon, Carbon\CarbonInterface, Carbon\CarbonImmutable, Closure...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Factory.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.621 IQR)
- **Top Global Matches:** file_cluster_13: 14.621, file_cluster_8: 14.96, file_cluster_11: 14.992
- **Magnitude:** 490.98 | **LOC:** 852 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (42.0565%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__call` (Impact: 80.3 | O(N^5) | DB: 8)
    * *Intent:* * You should rather consider mid-day is always 12pm, then if you need to test if it's an other * hou...
  * `handleTestNowClosure` (Impact: 61.5 | O(N^5) | DB: 7)
    * *Intent:* * @method array getDays() Get the days of the week. * @method ?string getFallbackLocale() Get the fa...
  * `setDefaultTimezone` (Impact: 44.6 | O(N^4) | DB: 6)
  * `matchFormatPattern` (Impact: 40.9 | O(N^3) | DB: 4)
  * `setTestNowAndTimezone` (Impact: 39.3 | O(N^3) | DB: 7)
    * *Intent:* /** * A factory to generate Carbon instances with common settings. * * <autodoc generated by `compos...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 48`, `args: 14`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 124`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 29`, `doc: 74`, `test: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.185
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.010068
  * `Imports (Out-Degree: 2):` DateTimeImmutable, Throwable, DateTimeZone, Symfony\Contracts\Translation\TranslatorInterface, RuntimeException, InvalidArgumentException, Closure, ReflectionMethod...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Carbon/CarbonTimeZone.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.483 IQR)
- **Top Global Matches:** file_cluster_13: 13.483, file_cluster_8: 13.807, file_cluster_7: 13.941
- **Magnitude:** 468.12 | **LOC:** 337 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (37.882%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAbbreviatedName` (Impact: 89.5 | O(N^5) | DB: 7)
  * `instance` (Impact: 51.4 | O(N^4) | DB: 6)
  * `toRegionName` (Impact: 49.3 | O(N^4) | DB: 8)
  * `cast` (Impact: 30.6 | O(2^N))
  * `toRegionTimeZone` (Impact: 30.1 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 75`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 86`
* *Architecture:* `api: 23`, `import: 9`
* *Defense:* `safety: 14`, `doc: 34`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.114
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.003351
  * `Imports (Out-Degree: 4):` DateTimeImmutable, Throwable, DateTimeZone, Exception, LocalFactory, Carbon\Traits\LocalFactory, Carbon\Exceptions\InvalidTimeZoneException, Carbon\Exceptions\InvalidCastException...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Week.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.328 IQR)
- **Top Global Matches:** file_cluster_13: 16.328, file_cluster_8: 16.414, file_cluster_7: 16.491
- **Magnitude:** 423.0 | **LOC:** 224 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (40.1092%), Tech Debt (73.1059%)
**Top Internal Functions/Classes:**
  * `weekYear` (Impact: 142.4 | O(2^N) | DB: 20)
    * *Intent:* /** * Trait Week. * * week and ISO week number, year and count in year. * * Depends on the following...
  * `week` (Impact: 65.0 | O(2^N) | DB: 10)
  * `weeksInYear` (Impact: 25.1 | O(N^3) | DB: 11)
  * `isoWeekYear` (Impact: 12.4 | O(N^3) | DB: 3)
  * `isoWeek` (Impact: 12.4 | O(N^3) | DB: 3)
    * *Intent:* /** * Get the number of weeks of the current week-year using given first day of week and first * day...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 22`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 147`, `orphaned_logic: 3`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 18`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` if not null, 
    public function week($week = null, 
    public function isoWeeksInYear($dayOfWeek = null, $dayOfYear ?? static::THURSDAY, Carbon\CarbonInterval, $dayOfWeek ?? static::MONDAY, 
    public function weeksInYear($dayOfWeek = null, $dayOfYear = null)
    
        $date = $this...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Converter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.46 IQR)
- **Top Global Matches:** file_cluster_13: 12.46, file_cluster_8: 12.673, file_cluster_7: 12.834
- **Magnitude:** 365.0 | **LOC:** 557 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (33.3659%), Tech Debt (99.9928%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 48.8 | O(2^N) | DB: 2)
  * `toPeriod` (Impact: 37.3 | O(N^3) | DB: 8)
    * *Intent:* /** * Format the instance as RFC850 *
  * `toISOString` (Impact: 34.9 | O(N^3) | DB: 4)
    * *Intent:* /** * Format the instance as ISO8601 * * @example
  * `__toString` (Impact: 31.9 | O(N^5) | DB: 1)
  * `getTimeFormatByPrecision` (Impact: 12.5 | O(N^3))
    * *Intent:* /** * Format the instance as date
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 99`, `args: 35`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 55`, `orphaned_logic: 26`
* *Architecture:* `api: 34`, `import: 12`
* *Defense:* `safety: 7`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Carbon\CarbonInterval, DateTimeImmutable, Carbon\Exceptions\UnitException, ToStringFormat, Carbon\CarbonPeriod, Carbon\Carbon, DateTime, Carbon\CarbonInterface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Options.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.738 IQR)
- **Top Global Matches:** file_cluster_13: 14.738, file_cluster_8: 15.039, file_cluster_17: 15.057
- **Magnitude:** 357.14 | **LOC:** 218 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (41.653%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `settings` (Impact: 161.7 | O(2^N) | DB: 12)
    * *Intent:* /**
  * `addExtraDebugInfos` (Impact: 45.5 | O(N^4) | DB: 1)
  * `getSettings` (Impact: 31.7 | O(N^4) | DB: 4)
    * *Intent:* /** * Function to call instead of format.
  * `__debugInfo` (Impact: 22.9 | O(N^4) | DB: 2)
  * `isLocalStrictModeEnabled` (Impact: 7.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 24`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 80`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 26`, `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.527
  * `Choke Point (Betweenness):` 0.000159 | `Ripple Effect (Closeness):` 0.009693
  * `Imports (Out-Degree: 2):` StaticOptions, Throwable, Localization, Carbon\CarbonInterface, DateTimeInterface
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Modifiers.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.845 IQR)
- **Top Global Matches:** file_cluster_8: 11.845, file_cluster_7: 11.981, file_cluster_13: 12.155
- **Magnitude:** 353.42 | **LOC:** 477 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (28.2845%), Tech Debt (64.0795%)
**Top Internal Functions/Classes:**
  * `change` (Impact: 45.8 | O(N^3) | DB: 2)
  * `next` (Impact: 27.3 | O(2^N) | DB: 3)
    * *Intent:* /**
  * `nextOrPreviousDay` (Impact: 17.9 | O(N^3) | DB: 5)
    * *Intent:* /** * Modify to the next occurrence of a given modifier such as a day of * the week. If no modifier ...
  * `previous` (Impact: 13.9 | O(N^3) | DB: 3)
    * *Intent:* /**
  * `modify` (Impact: 10.7 | O(2^N))
    * *Intent:* /** * Get the maximum instance between a given instance (default now) and the current instance.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 98`, `args: 29`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 62`, `high_risk_execution: 1`, `state_mutation: 95`, `orphaned_logic: 12`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `doc: 90`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Carbon\CarbonInterface, Carbon\Exceptions\InvalidFormatException, ReturnTypeWillChange
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Mixin.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.914 IQR)
- **Top Global Matches:** file_cluster_13: 12.914, file_cluster_8: 13.204, file_cluster_11: 13.407
- **Magnitude:** 330.44 | **LOC:** 240 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (44.9998%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadMixinTrait` (Impact: 122.4 | O(N^6) | DB: 13)
  * `cannotBeAMixinMethod` (Impact: 43.5 | O(N^5) | DB: 2)
    * *Intent:* * Mix another object into the class. * * @example * ``` * Carbon::mixin(new class { * public functio...
  * `loadMixinClass` (Impact: 25.9 | O(N^4) | DB: 2)
    * *Intent:* /**
  * `mixin` (Impact: 24.3 | O(2^N))
  * `getMixableMethods` (Impact: 20.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 58`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 57`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 16`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.288
  * `Choke Point (Betweenness):` 9.4e-05 | `Ripple Effect (Closeness):` 0.00917
  * `Imports (Out-Degree: 2):` Carbon\CarbonInterval, ReflectionNamedType, Generator, Throwable, Carbon\CarbonPeriod, Carbon\CarbonInterface, Closure, ReflectionMethod...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Rounding.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.674 IQR)
- **Top Global Matches:** file_cluster_13: 13.674, file_cluster_8: 13.871, file_cluster_7: 14.036
- **Magnitude:** 326.98 | **LOC:** 227 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (45.4504%), Tech Debt (55.3094%)
**Top Internal Functions/Classes:**
  * `roundUnit` (Impact: 146.0 | O(N^6) | DB: 34)
  * `ceilWeek` (Impact: 25.3 | O(N^4) | DB: 3)
  * `floor` (Impact: 7.5 | O(2^N) | DB: 1)
    * *Intent:* /**
  * `ceil` (Impact: 7.5 | O(2^N) | DB: 1)
  * `round` (Impact: 5.4 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 36`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 109`, `orphaned_logic: 3`
* *Architecture:* `api: 9`, `import: 5`
* *Defense:* `safety: 3`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carbon\Exceptions\UnknownUnitException, IntervalRounding, Carbon\WeekDay, Carbon\CarbonInterface, DateInterval
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Comparison.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.591 IQR)
- **Top Global Matches:** file_cluster_13: 12.591, file_cluster_8: 12.801, file_cluster_7: 12.972
- **Magnitude:** 298.86 | **LOC:** 1362 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (37.0511%), Tech Debt (99.131%)
**Top Internal Functions/Classes:**
  * `isStartOfDay` (Impact: 82.0 | O(2^N) | DB: 11)
    * *Intent:* /** * Determines if the instance is less (before) than another * * @example * ``` * Carbon::parse('2...
  * `between` (Impact: 20.8 | O(N^3) | DB: 3)
    * *Intent:* /**
  * `isStartOfTime` (Impact: 5.4 | O(N^2))
    * *Intent:* /**
  * `isEndOfTime` (Impact: 5.4 | O(N^2))
    * *Intent:* /** * Determines if the instance is between two others, bounds included. * * @example * ``` * Carbon...
  * `isWeekend` (Impact: 3.9 | O(N^3))
    * *Intent:* /** * Determines if the instance is greater (after) than another * * @example * ``` * Carbon::parse(...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 93`, `args: 35`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 65`, `orphaned_logic: 16`
* *Architecture:* `api: 31`, `import: 15`
* *Defense:* `safety: 3`, `doc: 48`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Carbon\CarbonConverterInterface, Carbon\Month, Carbon\Unit, Carbon\WeekDay, * we recommend to use the explicit methods ->betweenIncluded() or ->betweenExcluded() instead.
     *
     * @example
     * ```
     * Carbon::parse('2018-07-25')->between('2018-07-14', BackedEnum, '2018-08-01', Carbon\FactoryImmutable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Language.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.297 IQR)
- **Top Global Matches:** file_cluster_13: 13.297, file_cluster_8: 13.347, file_cluster_7: 13.532
- **Magnitude:** 270.72 | **LOC:** 272 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (37.3059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 25.8 | O(N^4) | DB: 5)
  * `getVariantName` (Impact: 14.5 | O(N^3) | DB: 2)
    * *Intent:* /**
  * `getNames` (Impact: 10.8 | O(N^3))
  * `regions` (Impact: 10.7 | O(2^N))
    * *Intent:* /** * Get the list of the known languages.
  * `getRegionName` (Impact: 10.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 52`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `api: 33`, `import: 3`
* *Defense:* `safety: 9`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.167
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00566
  * `Imports (Out-Degree: 0):` JsonSerializable, regions.php', languages.php'
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Carbon/WrapperClock.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.078 IQR)
- **Top Global Matches:** file_cluster_13: 13.078, file_cluster_8: 13.339, file_cluster_11: 13.553
- **Magnitude:** 261.44 | **LOC:** 188 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (53.3786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sleep` (Impact: 49.2 | O(2^N) | DB: 4)
  * `withTimeZone` (Impact: 41.0 | O(2^N) | DB: 3)
  * `addSeconds` (Impact: 15.2 | O(N^3) | DB: 6)
  * `getFactory` (Impact: 15.1 | O(N^3) | DB: 3)
  * `nowAsCarbon` (Impact: 15.1 | O(N^3) | DB: 3)
    * *Intent:* /** * @template T of CarbonInterface
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 56`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 64`
* *Architecture:* `api: 13`, `import: 7`
* *Defense:* `safety: 15`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.718
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.009139
  * `Imports (Out-Degree: 1):` Symfony\Component\Clock\ClockInterface, DateTimeImmutable, DateTimeZone, DateTime, RuntimeException, DateTimeInterface, Psr\Clock\ClockInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Carbon/Laravel/ServiceProvider.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.582 IQR)
- **Top Global Matches:** file_cluster_13: 12.582, file_cluster_8: 12.896, file_cluster_7: 13.204
- **Magnitude:** 255.58 | **LOC:** 179 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (39.6315%), Tech Debt (85.3656%)
**Top Internal Functions/Classes:**
  * `getLocale` (Impact: 35.3 | O(2^N) | DB: 2)
  * `getFallbackLocale` (Impact: 35.2 | O(2^N) | DB: 1)
  * `updateFallbackLocale` (Impact: 31.6 | O(N^4) | DB: 3)
  * `updateLocale` (Impact: 27.3 | O(N^4) | DB: 3)
  * `boot` (Impact: 18.2 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 46`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`, `orphaned_logic: 5`
* *Architecture:* `api: 7`, `import: 10`
* *Defense:* `safety: 12`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\CarbonInterval, Illuminate\Events\EventDispatcher, Throwable, Carbon\CarbonPeriod, Carbon\Carbon, Carbon\CarbonImmutable, Illuminate\Support\Carbon, Illuminate\Contracts\Events\Dispatcher...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/FactoryImmutable.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.33 IQR)
- **Top Global Matches:** file_cluster_13: 14.33, file_cluster_8: 14.675, file_cluster_7: 14.687
- **Magnitude:** 230.6 | **LOC:** 195 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (45.1687%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sleep` (Impact: 16.5 | O(2^N))
    * *Intent:* /**
  * `setCurrentClock` (Impact: 12.4 | O(N^3) | DB: 2)
  * `getInstance` (Impact: 8.0 | O(N^2))
  * `now` (Impact: 7.5 | O(2^N) | DB: 1)
  * `getDefaultInstance` (Impact: 5.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 52`, `args: 10`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 1`, `state_mutation: 163`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 4`, `doc: 65`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.855
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01614
  * `Imports (Out-Degree: 0):` Symfony\Component\Clock\ClockInterface, DateTimeZone, Symfony\Contracts\Translation\TranslatorInterface, Closure, DateTimeInterface, Symfony\Component\Clock\NativeClock
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Carbon/Unit.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.319 IQR)
- **Top Global Matches:** file_cluster_8: 11.319, file_cluster_7: 11.783, file_cluster_13: 11.854
- **Magnitude:** 184.2 | **LOC:** 120 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (69.339%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fromName` (Impact: 74.3 | O(N^6) | DB: 5)
  * `singular` (Impact: 18.9 | O(N^4) | DB: 1)
  * `plural` (Impact: 18.9 | O(N^4) | DB: 1)
  * `toName` (Impact: 6.2 | O(N^2))
  * `toNameIfUnit` (Impact: 6.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 27`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `api: 14`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004188
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Boundaries.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.178 IQR)
- **Top Global Matches:** file_cluster_8: 12.178, file_cluster_13: 12.271, file_cluster_7: 12.314
- **Magnitude:** 182.34 | **LOC:** 470 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (15.7659%), Tech Debt (99.9993%)
**Top Internal Functions/Classes:**
  * `startOf` (Impact: 21.3 | O(2^N) | DB: 2)
    * *Intent:* /** * Resets the date to end of the decade and time to 23:59:59.999999 * * @example * ``` * echo Car...
  * `endOf` (Impact: 21.3 | O(2^N) | DB: 2)
    * *Intent:* /** * Resets the date to the first day of the century and the time to 00:00:00 * * @example * ```
  * `startOfWeek` (Impact: 12.7 | O(N^4) | DB: 1)
  * `endOfWeek` (Impact: 12.7 | O(N^4) | DB: 1)
    * *Intent:* /** * Resets the date to end of the quarter and time to 23:59:59.999999 * * @example * ``` * echo Ca...
  * `startOfQuarter` (Impact: 2.9 | O(N^2) | DB: 1)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 60`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `orphaned_logic: 20`
* *Architecture:* `api: 26`, `import: 3`
* *Defense:* `safety: 4`, `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carbon\Exceptions\UnknownUnitException, Carbon\Unit, Carbon\WeekDay
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/PHPStan/MacroExtension.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.788 IQR)
- **Top Global Matches:** file_cluster_13: 13.788, file_cluster_8: 14.419, file_cluster_11: 14.443
- **Magnitude:** 171.24 | **LOC:** 138 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (40.3083%), Tech Debt (82.0978%)
**Top Internal Functions/Classes:**
  * `getMethod` (Impact: 72.0 | O(N^4) | DB: 24)
  * `hasMethod` (Impact: 14.6 | O(N^3) | DB: 1)
  * `__construct` (Impact: 2.9 | O(N^2) | DB: 2)
    * *Intent:* /** * Class MacroExtension. *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 33`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 77`, `orphaned_logic: 3`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `safety: 9`, `doc: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` PHPStan\Reflection\ReflectionProvider, Throwable, Carbon\FactoryImmutable, PHPStan\Reflection\ClassReflection, Carbon\CarbonInterface, Closure, InvalidArgumentException, ReflectionFunction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `tests/Laravel/EventDispatcher.php` (PHP) | Magnitude: 13.64 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, branch: 1, class_start: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/CarbonImmutable/Fixtures/Mixin.php` (PHP) | Magnitude: 0.03 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 13, state_mutation: 11, api: 5
- `src/Carbon/Carbon.php` (PHP) | Magnitude: 5.08 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 810, structural_boundaries: 11, indent_spaces: 5, import: 4
- `src/Carbon/Month.php` (PHP) | Magnitude: 65.28 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, branch: 22, structural_boundaries: 14, state_mutation: 9
- `lazy/Carbon/TranslatorStrongType.php` (PHP) | Magnitude: 84.36 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, state_mutation: 18, structural_boundaries: 17, branch: 8
- `src/Carbon/CarbonImmutable.php` (PHP) | Magnitude: 29.26 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 815, indent_spaces: 29, structural_boundaries: 19, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/Carbon/Traits/DeprecatedPeriodProperties.php` (PHP) | Magnitude: 22.3 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 22, api: 7, indent_spaces: 7, structural_boundaries: 5
- `src/Carbon/Traits/Macro.php` (PHP) | Magnitude: 79.2 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 16, doc: 15, args: 9
- `tests/Laravel/EventDispatcherBase.php` (PHP) | Magnitude: 21.46 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 6, branch: 4, state_mutation: 3
- `lazy/Carbon/MessageFormatter/MessageFormatterMapperWeakType.php` (PHP) | Magnitude: 23.94 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 11, branch: 4, args: 3
- `src/Carbon/Lang/en_HK.php` (PHP) | Magnitude: 12.08 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, branch: 1, doc: 1, import: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Carbon/CarbonInterval.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 6181.24
- `src/Carbon/CarbonPeriod.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 3910.54
- `src/Carbon/Traits/Localization.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 1484.42
- `src/Carbon/Traits/Creator.php` -> **Sam Anglin** (100.0% isolated ownership) | Magnitude: 1400.0
- `phpdoc.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 744.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Carbon/CarbonInterval.php` -> **Severity: 0.079** (Bridge: 0.0008 * Flux: 100.0%)
- `src/Carbon/CarbonPeriod.php` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 100.0%)
- `src/Carbon/Traits/Localization.php` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 100.0%)
- `src/Carbon/Traits/Options.php` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 100.0%)
- `src/Carbon/Traits/Mixin.php` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Carbon/FactoryImmutable.php` -> **Severity: 1.613** (Embedded: 0.0161 * Error Risk: 99.9595%)
- `src/Carbon/CarbonInterval.php` -> **Severity: 0.94** (Embedded: 0.0144 * Error Risk: 65.2433%)
- `src/Carbon/Factory.php` -> **Severity: 0.475** (Embedded: 0.0101 * Error Risk: 47.1569%)
- `src/Carbon/Traits/Localization.php` -> **Severity: 0.347** (Embedded: 0.007 * Error Risk: 49.5424%)
- `src/Carbon/Exceptions/ParseErrorException.php` -> **Severity: 0.335** (Embedded: 0.0087 * Error Risk: 38.5591%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Carbon/CarbonInterval.php` -> **Severity: 724.074** (Blast Radius: 7.909 * Doc Risk: 91.5507%)
- `src/Carbon/CarbonPeriod.php` -> **Severity: 274.4** (Blast Radius: 2.744 * Doc Risk: 100.0%)
- `src/Carbon/Exceptions/InvalidArgumentException.php` -> **Severity: 271.566** (Blast Radius: 24.476 * Doc Risk: 11.0952%)
- `src/Carbon/Traits/LocalFactory.php` -> **Severity: 270.455** (Blast Radius: 2.73 * Doc Risk: 99.0679%)
- `src/Carbon/CarbonTimeZone.php` -> **Severity: 211.397** (Blast Radius: 2.114 * Doc Risk: 99.9984%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
