# ARCHITECTURAL_BRIEF: Carbon
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/Carbon` |
| **Timestamp** | `2026-08-07T03:52:37.956185+00:00` |
| **Scan Duration** | `2.9s` |
| **Git Branch** | `master` |
| **Git Commit** | `e890471a3494740f7d9326d72ce6a8c559ffee60` |
| **Git Remote** | `https://github.com/briannesbitt/Carbon.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 948 malicious artifacts.

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
| Error & Exception Exposure | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.1 | 1.1 | 0.3 |
| API Exposure | 0.0 | 17.0 | 0.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 20.4 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.9 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 58.6 | 66.7 | 100.0 |
| Instability Exposure | 0.0 | 4.8 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 33.5 | 0.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 8.8 | 6.8 | 2.3 |
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

- `__construct` (@ `src/Carbon/CarbonInterval.php`) -> Impact: **273.8** | LOC: 135
  * *Intent:* * @method $this floorQuarters(int|float $precision = 1) Truncate the current instance quarter with given precision. * @method $this ceilQuarter(int|fl...
- `fromString` (@ `src/Carbon/CarbonInterval.php`) -> Impact: **154.2** | LOC: 165
  * *Intent:* /** * Returns the factor for a given source-to-target couple. * * @param string $source
- `forHumans` (@ `src/Carbon/CarbonInterval.php`) -> Impact: **141.9** | LOC: 200
- `__construct` (@ `src/Carbon/CarbonPeriod.php`) -> Impact: **101.8** | LOC: 130
- `__call` (@ `src/Carbon/CarbonPeriod.php`) -> Impact: **101.0** | LOC: 149
- `translateTimeString` (@ `src/Carbon/Traits/Localization.php`) -> Impact: **88.2** | LOC: 98
- `create` (@ `src/Carbon/Traits/Creator.php`) -> Impact: **62.3** | LOC: 58
- `addUnit` (@ `src/Carbon/Traits/Units.php`) -> Impact: **60.2** | LOC: 84
- `__unserialize` (@ `src/Carbon/CarbonInterval.php`) -> Impact: **51.4** | LOC: 67
  * *Intent:* /** * Allow fluent calls on the setters... CarbonInterval::years(3)->months(5)->day(). * * Note: This is done using the magic method to allow static a...
- `total` (@ `src/Carbon/CarbonInterval.php`) -> Impact: **50.8** | LOC: 95

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Carbon/Lang` | 803 | 11114.2 | 5.76% | 9.07% |
| `src/Carbon` | 19 | 6387.44 | 36.57% | 4.28% |
| `src/Carbon/Traits` | 27 | 4212.68 | 25.63% | 40.15% |
| `__monolith__` | 8 | 631.72 | 7.63% | 12.5% |
| `src/Carbon/Exceptions` | 30 | 528.46 | 18.63% | 2.88% |
| `tests` | 4 | 457.16 | 14.83% | 0.0% |
| `src/Carbon/PHPStan` | 2 | 193.94 | 31.64% | 91.05% |
| `src/Carbon/Laravel` | 1 | 141.38 | 39.63% | 85.37% |
| `tests/Laravel` | 8 | 139.56 | 6.38% | 0.0% |
| `src/Carbon/Constants` | 4 | 120.66 | 4.01% | 0.0% |

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
7. **`src/Carbon/Lang/sr_Latn_ME.php`** -> AI Confidence: **99.31%**
8. **`src/Carbon/Traits/Creator.php`** -> AI Confidence: **99.31%**
9. **`src/Carbon/Traits/Units.php`** -> AI Confidence: **99.31%**
10. **`src/Carbon/Traits/Week.php`** -> AI Confidence: **99.31%**
11. **`tests/AbstractTestCase.php`** -> AI Confidence: **99.31%**
12. **`src/Carbon/Constants/Format.php`** -> AI Confidence: **99.29%**
13. **`src/Carbon/Lang/af.php`** -> AI Confidence: **99.29%**
14. **`src/Carbon/Lang/ar.php`** -> AI Confidence: **99.29%**
15. **`src/Carbon/Lang/ar_DZ.php`** -> AI Confidence: **99.29%**
16. **`src/Carbon/Lang/ar_LY.php`** -> AI Confidence: **99.29%**
17. **`src/Carbon/Lang/ar_MA.php`** -> AI Confidence: **99.29%**
18. **`src/Carbon/Lang/ar_Shakl.php`** -> AI Confidence: **99.29%**
19. **`src/Carbon/Lang/ar_TN.php`** -> AI Confidence: **99.29%**
20. **`src/Carbon/Lang/bm.php`** -> AI Confidence: **99.29%**
21. **`src/Carbon/Lang/br.php`** -> AI Confidence: **99.29%**
22. **`src/Carbon/Lang/bs.php`** -> AI Confidence: **99.29%**
23. **`src/Carbon/Lang/ckb.php`** -> AI Confidence: **99.29%**
24. **`src/Carbon/Lang/da.php`** -> AI Confidence: **99.29%**
25. **`src/Carbon/Lang/el.php`** -> AI Confidence: **99.29%**
26. **`src/Carbon/Lang/eo.php`** -> AI Confidence: **99.29%**
27. **`src/Carbon/Lang/fo.php`** -> AI Confidence: **99.29%**
28. **`src/Carbon/Lang/fr.php`** -> AI Confidence: **99.29%**
29. **`src/Carbon/Lang/ga.php`** -> AI Confidence: **99.29%**
30. **`src/Carbon/Lang/hr.php`** -> AI Confidence: **99.29%**
31. **`src/Carbon/Lang/kk.php`** -> AI Confidence: **99.29%**
32. **`src/Carbon/Lang/km.php`** -> AI Confidence: **99.29%**
33. **`src/Carbon/Lang/ky.php`** -> AI Confidence: **99.29%**
34. **`src/Carbon/Lang/mi.php`** -> AI Confidence: **99.29%**
35. **`src/Carbon/Lang/mt.php`** -> AI Confidence: **99.29%**
36. **`src/Carbon/Lang/nb.php`** -> AI Confidence: **99.29%**
37. **`src/Carbon/Lang/nn.php`** -> AI Confidence: **99.29%**
38. **`src/Carbon/Lang/pl.php`** -> AI Confidence: **99.29%**
39. **`src/Carbon/Lang/pt.php`** -> AI Confidence: **99.29%**
40. **`src/Carbon/Lang/ro.php`** -> AI Confidence: **99.29%**
41. **`src/Carbon/Lang/se.php`** -> AI Confidence: **99.29%**
42. **`src/Carbon/Lang/sq.php`** -> AI Confidence: **99.29%**
43. **`src/Carbon/Lang/sr.php`** -> AI Confidence: **99.29%**
44. **`src/Carbon/Lang/sr_Cyrl.php`** -> AI Confidence: **99.29%**
45. **`src/Carbon/Lang/sw.php`** -> AI Confidence: **99.29%**
46. **`src/Carbon/Lang/tet.php`** -> AI Confidence: **99.29%**
47. **`src/Carbon/Lang/th.php`** -> AI Confidence: **99.29%**
48. **`src/Carbon/Lang/tl.php`** -> AI Confidence: **99.29%**
49. **`src/Carbon/Lang/tzl.php`** -> AI Confidence: **99.29%**
50. **`src/Carbon/Lang/tzm.php`** -> AI Confidence: **99.29%**
51. **`src/Carbon/Lang/tzm_Latn.php`** -> AI Confidence: **99.29%**
52. **`src/Carbon/Lang/ur.php`** -> AI Confidence: **99.29%**
53. **`src/Carbon/Lang/uz.php`** -> AI Confidence: **99.29%**
54. **`src/Carbon/Lang/uz_Latn.php`** -> AI Confidence: **99.29%**
55. **`src/Carbon/Lang/vi.php`** -> AI Confidence: **99.29%**
56. **`src/Carbon/Lang/yo.php`** -> AI Confidence: **99.29%**
57. **`src/Carbon/Lang/zgh.php`** -> AI Confidence: **99.29%**
58. **`src/Carbon/Traits/Localization.php`** -> AI Confidence: **99.25%**
59. **`src/Carbon/AbstractTranslator.php`** -> AI Confidence: **99.24%**
60. **`src/Carbon/CarbonTimeZone.php`** -> AI Confidence: **99.24%**
61. **`src/Carbon/Laravel/ServiceProvider.php`** -> AI Confidence: **99.24%**
62. **`src/Carbon/Traits/Mixin.php`** -> AI Confidence: **99.24%**
63. **`src/Carbon/Traits/Test.php`** -> AI Confidence: **99.23%**
64. **`phpdoc.php`** -> AI Confidence: **99.22%**
65. **`src/Carbon/Traits/Comparison.php`** -> AI Confidence: **99.18%**
66. **`src/Carbon/Traits/Converter.php`** -> AI Confidence: **99.18%**
67. **`src/Carbon/Traits/IntervalStep.php`** -> AI Confidence: **99.18%**
68. **`src/Carbon/Lang/be.php`** -> AI Confidence: **99.17%**
69. **`src/Carbon/Lang/cy.php`** -> AI Confidence: **99.17%**
70. **`src/Carbon/Lang/fy.php`** -> AI Confidence: **99.17%**
71. **`src/Carbon/Lang/gd.php`** -> AI Confidence: **99.17%**
72. **`src/Carbon/Lang/it.php`** -> AI Confidence: **99.17%**
73. **`src/Carbon/Lang/pap.php`** -> AI Confidence: **99.17%**
74. **`src/Carbon/Lang/sr_Cyrl_ME.php`** -> AI Confidence: **99.17%**
75. **`src/Carbon/Lang/tr.php`** -> AI Confidence: **99.17%**
76. **`src/Carbon/Lang/aa_DJ.php`** -> AI Confidence: **99.16%**
77. **`src/Carbon/Lang/aa_ER.php`** -> AI Confidence: **99.16%**
78. **`src/Carbon/Lang/aa_ER@saaho.php`** -> AI Confidence: **99.16%**
79. **`src/Carbon/Lang/aa_ET.php`** -> AI Confidence: **99.16%**
80. **`src/Carbon/Lang/af_NA.php`** -> AI Confidence: **99.16%**
81. **`src/Carbon/Lang/agq.php`** -> AI Confidence: **99.16%**
82. **`src/Carbon/Lang/agr_PE.php`** -> AI Confidence: **99.16%**
83. **`src/Carbon/Lang/ak_GH.php`** -> AI Confidence: **99.16%**
84. **`src/Carbon/Lang/am_ET.php`** -> AI Confidence: **99.16%**
85. **`src/Carbon/Lang/an_ES.php`** -> AI Confidence: **99.16%**
86. **`src/Carbon/Lang/anp_IN.php`** -> AI Confidence: **99.16%**
87. **`src/Carbon/Lang/ar_IN.php`** -> AI Confidence: **99.16%**
88. **`src/Carbon/Lang/ar_SS.php`** -> AI Confidence: **99.16%**
89. **`src/Carbon/Lang/as_IN.php`** -> AI Confidence: **99.16%**
90. **`src/Carbon/Lang/asa.php`** -> AI Confidence: **99.16%**
91. **`src/Carbon/Lang/ast.php`** -> AI Confidence: **99.16%**
92. **`src/Carbon/Lang/ayc_PE.php`** -> AI Confidence: **99.16%**
93. **`src/Carbon/Lang/az_AZ.php`** -> AI Confidence: **99.16%**
94. **`src/Carbon/Lang/az_Cyrl.php`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13527` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Carbon/Traits/Creator.php` (PHP) -> Cumulative Risk: **547.18**
- **Archetype:** `file_cluster_13` (Distance: 15.284 IQR)
- **Magnitude:** 678.2 | **LOC:** 932 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.3531%), Tech Debt (92.8934%)
- **Heaviest Functions:** `create` (Impact: 62.3), `__construct` (Impact: 40.3), `createSafe` (Impact: 38.2)

### 2. `src/Carbon/Traits/Difference.php` (PHP) -> Cumulative Risk: **543.59**
- **Archetype:** `file_cluster_13` (Distance: 14.691 IQR)
- **Magnitude:** 421.3 | **LOC:** 856 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9245%), Safety Score (97.9025%)
- **Heaviest Functions:** `diffInMonths` (Impact: 24.3), `calendar` (Impact: 16.8), `diffInDays` (Impact: 15.2)

### 3. `src/Carbon/AbstractTranslator.php` (PHP) -> Cumulative Risk: **525.97**
- **Archetype:** `file_cluster_13` (Distance: 13.957 IQR)
- **Magnitude:** 342.42 | **LOC:** 1300 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (87.6541%), Verification (80.0%)
- **Heaviest Functions:** `setLocale` (Impact: 27.2), `translate` (Impact: 21.4), `get` (Impact: 18.0)

### 4. `src/Carbon/Unit.php` (PHP) -> Cumulative Risk: **523.32**
- **Archetype:** `file_cluster_8` (Distance: 11.319 IQR)
- **Magnitude:** 94.0 | **LOC:** 120 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9645%), Documentation (95.5659%), Verification (80.0%)
- **Heaviest Functions:** `fromName` (Impact: 22.4), `singular` (Impact: 7.9), `plural` (Impact: 7.9)

### 5. `src/Carbon/Traits/Units.php` (PHP) -> Cumulative Risk: **520.3**
- **Archetype:** `file_cluster_13` (Distance: 14.592 IQR)
- **Magnitude:** 321.3 | **LOC:** 473 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.3559%), Verification (80.0%)
- **Heaviest Functions:** `addUnit` (Impact: 60.2), `add` (Impact: 21.7), `sub` (Impact: 21.7)

### 6. `src/Carbon/Laravel/ServiceProvider.php` (PHP) -> Cumulative Risk: **514.95**
- **Archetype:** `file_cluster_13` (Distance: 12.599 IQR)
- **Magnitude:** 141.38 | **LOC:** 179 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (85.3656%), Verification (80.0%)
- **Heaviest Functions:** `updateFallbackLocale` (Impact: 13.4), `updateLocale` (Impact: 11.7), `getLocale` (Impact: 9.3)

### 7. `src/Carbon/Traits/Converter.php` (PHP) -> Cumulative Risk: **514.44**
- **Archetype:** `file_cluster_13` (Distance: 12.479 IQR)
- **Magnitude:** 228.9 | **LOC:** 557 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9928%), State Flux (99.9556%), Verification (80.0%)
- **Heaviest Functions:** `toPeriod` (Impact: 19.3), `toISOString` (Impact: 17.7), `format` (Impact: 12.8)

### 8. `src/Carbon/Traits/Comparison.php` (PHP) -> Cumulative Risk: **510.6**
- **Archetype:** `file_cluster_13` (Distance: 12.591 IQR)
- **Magnitude:** 192.96 | **LOC:** 1362 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9891%), Tech Debt (99.131%), Verification (80.0%)
- **Heaviest Functions:** `isStartOfDay` (Impact: 18.0), `between` (Impact: 10.8), `isStartOfTime` (Impact: 3.7)

### 9. `src/Carbon/Traits/Week.php` (PHP) -> Cumulative Risk: **510.08**
- **Archetype:** `file_cluster_13` (Distance: 16.328 IQR)
- **Magnitude:** 233.8 | **LOC:** 224 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.7588%), Verification (80.0%)
- **Heaviest Functions:** `weekYear` (Impact: 30.4), `week` (Impact: 17.1), `weeksInYear` (Impact: 13.0)

### 10. `src/Carbon/Language.php` (PHP) -> Cumulative Risk: **506.33**
- **Archetype:** `file_cluster_13` (Distance: 13.297 IQR)
- **Magnitude:** 205.22 | **LOC:** 272 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.9297%), Safety Score (81.2178%)
- **Heaviest Functions:** `__construct` (Impact: 10.8), `getVariantName` (Impact: 7.5), `getRegionName` (Impact: 7.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Carbon/CarbonInterval.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.119 IQR)
- **Top Global Matches:** file_cluster_13: 15.119, file_cluster_8: 15.321, file_cluster_7: 15.363
- **Magnitude:** 2571.44 | **LOC:** 3574 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.6741%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 273.8)
    * *Intent:* * @method $this floorQuarters(int|float $precision = 1) Truncate the current instance quarter with g...
  * `fromString` (Impact: 154.2)
    * *Intent:* /** * Returns the factor for a given source-to-target couple. * * @param string $source
  * `forHumans` (Impact: 141.9)
  * `__unserialize` (Impact: 51.4)
    * *Intent:* /** * Allow fluent calls on the setters... CarbonInterval::years(3)->months(5)->day(). * * Note: Thi...
  * `total` (Impact: 50.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 473`, `structural_boundaries: 326`, `args: 105`, `func_start: 99`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1147`
* *Architecture:* `api: 113`, `import: 39`
* *Defense:* `safety: 76`, `doc: 424`, `test: 2`, `immutability_locks: 12`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.909
  * `Choke Point (Betweenness):` 0.000786 | `Ripple Effect (Closeness):` 0.01441
  * `Imports (Out-Degree: 22):` Carbon\Exceptions\UnknownUnitException, Carbon\Exceptions\UnitNotConfiguredException, InvalidArgumentException, DateTime, Carbon\Exceptions\UnknownSetterException, Exception, Carbon\Exceptions\ParseErrorException, Carbon\Exceptions\InvalidCastException...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/Carbon/CarbonPeriod.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.848 IQR)
- **Top Global Matches:** file_cluster_13: 14.848, file_cluster_8: 15.019, file_cluster_7: 15.091
- **Magnitude:** 1909.14 | **LOC:** 2719 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.1275%), Tech Debt (10.4599%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 101.8)
  * `__call` (Impact: 101.0)
  * `initializeSerialization` (Impact: 50.1)
    * *Intent:* /**
  * `__unserialize` (Impact: 50.0)
  * `parseIso8601` (Impact: 29.4)
    * *Intent:* /** * Number of maximum attempts before giving up on finding end date. * * @var int
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 399`, `args: 138`, `func_start: 130`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 698`, `fragile_debt: 3`
* *Architecture:* `api: 135`, `concurrency: 7`, `import: 38`
* *Defense:* `safety: 99`, `doc: 325`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.744
  * `Choke Point (Betweenness):` 0.00021 | `Ripple Effect (Closeness):` 0.007964
  * `Imports (Out-Degree: 19):` 'current'], Carbon\Exceptions\UnknownGetterException, Carbon\Exceptions\EndLessPeriodException, DateTimeInterface, $info['include_end_date'], 
    public function endsAfter(mixed $date = null): bool
    
        return $this->calculateEnd()->greaterThan($this->resolveCarbon($date), _end_date' => function (bool $included): void 
                        $this->excludeEndDate(!$included, 
    public function endsBefore(mixed $date = null): bool
    
        return $this->calculateEnd()->lessThan($this->resolveCarbon($date)...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Localization.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.706 IQR)
- **Top Global Matches:** file_cluster_13: 14.706, file_cluster_11: 14.891, file_cluster_8: 14.895
- **Magnitude:** 727.72 | **LOC:** 748 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.84%), Tech Debt (9.4523%)
**Top Internal Functions/Classes:**
  * `translateTimeString` (Impact: 88.2)
  * `cleanWordFromTranslationString` (Impact: 37.0)
  * `translateNumber` (Impact: 28.1)
  * `setFallbackLocale` (Impact: 25.6)
  * `getTranslationMessageWith` (Impact: 21.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 121`, `args: 40`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 289`, `planned_debt: 1`
* *Architecture:* `api: 35`, `import: 11`
* *Defense:* `safety: 35`, `doc: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.593
  * `Choke Point (Betweenness):` 0.000189 | `Ripple Effect (Closeness):` 0.007
  * `Imports (Out-Degree: 6):` Carbon\TranslatorStrongTypeInterface, StaticLocalization, Carbon\Exceptions\InvalidTypeException, Symfony\Contracts\Translation\LocaleAwareInterface, Carbon\Exceptions\NotLocaleAwareException, Symfony\Component\Translation\TranslatorBagInterface, Carbon\Translator, Carbon\CarbonInterface...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Creator.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.284 IQR)
- **Top Global Matches:** file_cluster_13: 15.284, file_cluster_8: 15.671, file_cluster_11: 15.671
- **Magnitude:** 678.2 | **LOC:** 932 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.2599%), Tech Debt (92.8934%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 62.3)
  * `__construct` (Impact: 40.3)
    * *Intent:* /** * Trait Creator. *
  * `createSafe` (Impact: 38.2)
  * `rawCreateFromFormat` (Impact: 37.9)
    * *Intent:* /** * Create a new safe Carbon instance from a specific date and time. * * If any of $year, $month o...
  * `createStrict` (Impact: 26.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 107`, `args: 29`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 314`, `fragile_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 21`, `import: 21`
* *Defense:* `safety: 35`, `doc: 98`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` true, d
        $isNow = \in_array($time, DateMalformedStringException, 'now'], Exception, DateTimeInterface, LocalFactory, Carbon\Month...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phpdoc.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.398 IQR)
- **Top Global Matches:** file_cluster_8: 13.398, file_cluster_13: 13.526, file_cluster_17: 13.598
- **Magnitude:** 563.88 | **LOC:** 862 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.2651%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compileDoc` (Impact: 34.0)
    * *Intent:* /** * %description% * * @var %type% * * @deprecated %line1%
  * `dumpType` (Impact: 29.1)
  * `cleanClassName` (Impact: 12.9)
  * `dumpParameter` (Impact: 11.8)
  * `getMethodReturnType` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 68`, `args: 12`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 438`, `dead_code: 2`
* *Architecture:* `io: 6`, `api: 2`, `import: 6`
* *Defense:* `safety: 27`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Carbon\Factory, Carbon\Carbon, Carbon\FactoryImmutable, Carbon\CarbonImmutable, Carbon\CarbonInterface, autoload.php'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Difference.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.691 IQR)
- **Top Global Matches:** file_cluster_13: 14.691, file_cluster_8: 14.952, file_cluster_7: 14.969
- **Magnitude:** 421.3 | **LOC:** 856 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.6924%), Tech Debt (99.9245%)
**Top Internal Functions/Classes:**
  * `diffInMonths` (Impact: 24.3)
  * `calendar` (Impact: 16.8)
    * *Intent:* /** * Get the difference by the given interval using a filter closure. * * @param CarbonInterval $ci...
  * `diffInDays` (Impact: 15.2)
  * `diffInYears` (Impact: 13.7)
    * *Intent:* /** * Get the difference as a CarbonInterval instance. * Return relative interval (negative if $abso...
  * `diffFiltered` (Impact: 12.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 66`, `args: 28`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 255`, `fragile_debt: 2`, `orphaned_logic: 12`
* *Architecture:* `api: 24`, `import: 10`
* *Defense:* `safety: 4`, `doc: 123`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` DateInterval, Carbon\Carbon, Carbon\Exceptions\UnknownUnitException, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\Unit, Carbon\CarbonImmutable, DateTimeInterface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/AbstractTestCase.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.895 IQR)
- **Top Global Matches:** file_cluster_13: 12.895, file_cluster_8: 13.088, file_cluster_7: 13.359
- **Magnitude:** 394.72 | **LOC:** 502 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.7246%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assertSameIntervals` (Impact: 36.8)
  * `assertCarbonInterval` (Impact: 27.4)
  * `assertCarbon` (Impact: 16.8)
  * `acceptClosuresFrom` (Impact: 16.5)
  * `assertCarbonTime` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 70`, `args: 26`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 170`, `orphaned_logic: 18`
* *Architecture:* `api: 10`, `import: 20`
* *Defense:* `safety: 19`, `doc: 22`, `test: 17`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.000189 | `Ripple Effect (Closeness):` 0.001047
  * `Imports (Out-Degree: 8):` Carbon\CarbonTimeZone, DateTime, Carbon\CarbonPeriod, AssertObjectHasPropertyTrait, PHPUnit\Framework\TestCase, Carbon\CarbonInterval, Carbon\CarbonImmutable, Tests\PHPUnit\AssertObjectHasPropertyTrait...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Carbon/AbstractTranslator.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.957 IQR)
- **Top Global Matches:** file_cluster_13: 13.957, file_cluster_8: 14.209, file_cluster_7: 14.354
- **Magnitude:** 342.42 | **LOC:** 1300 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.4351%), Tech Debt (70.8158%)
**Top Internal Functions/Classes:**
  * `setLocale` (Impact: 27.2)
  * `translate` (Impact: 21.4)
  * `get` (Impact: 18.0)
    * *Intent:* /** * List of custom localized messages. * * @var array */
  * `resetMessages` (Impact: 16.6)
    * *Intent:* /** * Returns the list of directories translation files are searched in. */
  * `compareChunkLists` (Impact: 9.6)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 78`, `args: 29`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 160`, `orphaned_logic: 8`
* *Architecture:* `api: 17`, `import: 10`
* *Defense:* `safety: 17`, `doc: 46`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $file, ), ReflectionFunction, 
    public function getAvailableLocales(string $prefix = ''): array
    
        return array_unique(array_merge(
            array_map(
                static fn (string $file) => substr($file, ReflectionException, ReflectionProperty, 
    public function getLocalesFiles(string $prefix = ''): array
    
        $files = [], strrpos($file...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Units.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.592 IQR)
- **Top Global Matches:** file_cluster_13: 14.592, file_cluster_0: 14.969, file_cluster_8: 14.998
- **Magnitude:** 321.3 | **LOC:** 473 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.6124%), Tech Debt (71.5257%)
**Top Internal Functions/Classes:**
  * `addUnit` (Impact: 60.2)
  * `add` (Impact: 21.7)
  * `sub` (Impact: 21.7)
  * `rawAddUnit` (Impact: 12.7)
    * *Intent:* /** * Add given units or interval to the current instance. * * @example $date->add('hour', 3) * @exa...
  * `subtract` (Impact: 8.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 47`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 166`, `orphaned_logic: 6`
* *Architecture:* `api: 10`, `import: 12`
* *Defense:* `safety: 20`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` DateInterval, DateMalformedStringException, Carbon\CarbonInterval, Carbon\Exceptions\UnitException, Closure, Carbon\Unit, Carbon\Exceptions\UnsupportedUnitException, ReturnTypeWillChange...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Factory.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.626 IQR)
- **Top Global Matches:** file_cluster_13: 14.626, file_cluster_8: 14.963, file_cluster_11: 15.0
- **Magnitude:** 279.88 | **LOC:** 852 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (41.6556%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__call` (Impact: 28.3)
    * *Intent:* * You should rather consider mid-day is always 12pm, then if you need to test if it's an other * hou...
  * `handleTestNowClosure` (Impact: 21.6)
    * *Intent:* * @method array getDays() Get the days of the week. * @method ?string getFallbackLocale() Get the fa...
  * `setTestNowAndTimezone` (Impact: 20.3)
    * *Intent:* /** * A factory to generate Carbon instances with common settings. * * <autodoc generated by `compos...
  * `setDefaultTimezone` (Impact: 18.6)
  * `matchFormatPattern` (Impact: 14.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 43`, `args: 14`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 124`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 29`, `doc: 74`, `test: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.185
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.010068
  * `Imports (Out-Degree: 2):` DateTimeImmutable, InvalidArgumentException, RuntimeException, Throwable, DateTimeZone, ReflectionMethod, DateTimeInterface, Closure...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Carbon/CarbonTimeZone.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.479 IQR)
- **Top Global Matches:** file_cluster_13: 13.479, file_cluster_8: 13.802, file_cluster_7: 13.936
- **Magnitude:** 261.42 | **LOC:** 337 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.4828%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAbbreviatedName` (Impact: 30.7)
  * `instance` (Impact: 21.4)
  * `toRegionName` (Impact: 20.8)
  * `toRegionTimeZone` (Impact: 15.4)
  * `resolveCarbon` (Impact: 8.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 74`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 86`
* *Architecture:* `api: 23`, `import: 9`
* *Defense:* `safety: 14`, `doc: 34`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.114
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.003351
  * `Imports (Out-Degree: 4):` DateTimeImmutable, Carbon\Exceptions\InvalidTimeZoneException, Throwable, Exception, Carbon\Traits\LocalFactory, DateTimeZone, Carbon\Exceptions\InvalidCastException, DateTimeInterface...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Modifiers.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.762 IQR)
- **Top Global Matches:** file_cluster_8: 11.762, file_cluster_7: 11.921, file_cluster_13: 12.099
- **Magnitude:** 235.72 | **LOC:** 477 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1082%), Tech Debt (64.0795%)
**Top Internal Functions/Classes:**
  * `nextOrPreviousDay` (Impact: 9.3)
    * *Intent:* /** * Modify to the next occurrence of a given modifier such as a day of * the week. If no modifier ...
  * `change` (Impact: 7.7)
  * `next` (Impact: 7.2)
    * *Intent:* /**
  * `previous` (Impact: 7.2)
    * *Intent:* /**
  * `nthOfQuarter` (Impact: 5.6)
    * *Intent:* /** * Modify to the last occurrence of a given day of the week * in the current quarter. If no dayOf...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 98`, `args: 29`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 62`, `high_risk_execution: 1`, `state_mutation: 95`, `orphaned_logic: 12`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `doc: 90`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Carbon\Exceptions\InvalidFormatException, ReturnTypeWillChange, Carbon\CarbonInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Week.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.328 IQR)
- **Top Global Matches:** file_cluster_13: 16.328, file_cluster_8: 16.414, file_cluster_7: 16.491
- **Magnitude:** 233.8 | **LOC:** 224 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.1092%), Tech Debt (73.1059%)
**Top Internal Functions/Classes:**
  * `weekYear` (Impact: 30.4)
    * *Intent:* /** * Trait Week. * * week and ISO week number, year and count in year. * * Depends on the following...
  * `week` (Impact: 17.1)
  * `weeksInYear` (Impact: 13.0)
  * `isoWeekYear` (Impact: 6.4)
  * `isoWeek` (Impact: 6.4)
    * *Intent:* /** * Get the number of weeks of the current week-year using given first day of week and first * day...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 22`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 147`, `orphaned_logic: 3`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 18`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` 
    public function isoWeekYear($year = null, act,  Jan 6).
     *
     * @param int|null $year      if null, 
    public function isoWeek($week = null, d in the first week. Or use ISO format if no settings
     * given.
     *
     * @param int|null $year      if null, Carbon\CarbonInterval, $dayOfYear = null)
    
        return $this->week(
            $week, $dayOfYear = null)
    
        $date = $this...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Converter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.479 IQR)
- **Top Global Matches:** file_cluster_13: 12.479, file_cluster_8: 12.689, file_cluster_7: 12.848
- **Magnitude:** 228.9 | **LOC:** 557 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.3659%), Tech Debt (99.9928%)
**Top Internal Functions/Classes:**
  * `toPeriod` (Impact: 19.3)
    * *Intent:* /** * Format the instance as RFC850 *
  * `toISOString` (Impact: 17.7)
    * *Intent:* /** * Format the instance as ISO8601 * * @example
  * `format` (Impact: 12.8)
  * `__toString` (Impact: 11.1)
  * `getTimeFormatByPrecision` (Impact: 6.5)
    * *Intent:* /** * Format the instance as date
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 87`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 55`, `orphaned_logic: 26`
* *Architecture:* `api: 34`, `import: 12`
* *Defense:* `safety: 7`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ToStringFormat, Carbon\Carbon, Carbon\CarbonInterface, DateTimeImmutable, Carbon\CarbonInterval, Carbon\Exceptions\UnitException, DateTime, Carbon\CarbonImmutable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Language.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.297 IQR)
- **Top Global Matches:** file_cluster_13: 13.297, file_cluster_8: 13.347, file_cluster_7: 13.532
- **Magnitude:** 205.22 | **LOC:** 272 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.3059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 10.8)
  * `getVariantName` (Impact: 7.5)
    * *Intent:* /**
  * `getRegionName` (Impact: 7.1)
  * `getNames` (Impact: 5.6)
  * `getIsoDescription` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 52`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `api: 33`, `import: 3`
* *Defense:* `safety: 9`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.167
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00566
  * `Imports (Out-Degree: 0):` regions.php', languages.php', JsonSerializable
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Carbon/FactoryImmutable.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.279 IQR)
- **Top Global Matches:** file_cluster_13: 14.279, file_cluster_8: 14.624, file_cluster_7: 14.636
- **Magnitude:** 201.7 | **LOC:** 195 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.5165%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setCurrentClock` (Impact: 6.4)
  * `getInstance` (Impact: 5.4)
  * `sleep` (Impact: 4.5)
    * *Intent:* /**
  * `getDefaultInstance` (Impact: 3.7)
  * `getCurrentClock` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 51`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 1`, `state_mutation: 163`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 4`, `doc: 65`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.855
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01614
  * `Imports (Out-Degree: 0):` Symfony\Component\Clock\NativeClock, Symfony\Component\Clock\ClockInterface, DateTimeZone, DateTimeInterface, Closure, Symfony\Contracts\Translation\TranslatorInterface
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Comparison.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.591 IQR)
- **Top Global Matches:** file_cluster_13: 12.591, file_cluster_8: 12.801, file_cluster_7: 12.972
- **Magnitude:** 192.96 | **LOC:** 1362 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.0511%), Tech Debt (99.131%)
**Top Internal Functions/Classes:**
  * `isStartOfDay` (Impact: 18.0)
    * *Intent:* /** * Determines if the instance is less (before) than another * * @example * ``` * Carbon::parse('2...
  * `between` (Impact: 10.8)
    * *Intent:* /**
  * `isStartOfTime` (Impact: 3.7)
    * *Intent:* /**
  * `isEndOfTime` (Impact: 3.7)
    * *Intent:* /** * Determines if the instance is between two others, bounds included. * * @example * ``` * Carbon...
  * `eq` (Impact: 2.2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 93`, `args: 35`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 65`, `orphaned_logic: 16`
* *Architecture:* `api: 31`, `import: 15`
* *Defense:* `safety: 3`, `doc: 48`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` DateInterval, Carbon\Month, '2018-08-01', Carbon\FactoryImmutable, InvalidArgumentException, BackedEnum, * we recommend to use the explicit methods ->betweenIncluded() or ->betweenExcluded() instead.
     *
     * @example
     * ```
     * Carbon::parse('2018-07-25')->between('2018-07-14', Carbon\Unit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Rounding.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.671 IQR)
- **Top Global Matches:** file_cluster_13: 13.671, file_cluster_8: 13.865, file_cluster_7: 14.027
- **Magnitude:** 192.88 | **LOC:** 227 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.4504%), Tech Debt (55.3094%)
**Top Internal Functions/Classes:**
  * `roundUnit` (Impact: 45.4)
  * `ceilWeek` (Impact: 10.6)
  * `roundWeek` (Impact: 2.8)
  * `floor` (Impact: 2.6)
    * *Intent:* /**
  * `ceil` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 30`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 109`, `orphaned_logic: 3`
* *Architecture:* `api: 9`, `import: 5`
* *Defense:* `safety: 3`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` DateInterval, IntervalRounding, Carbon\Exceptions\UnknownUnitException, Carbon\WeekDay, Carbon\CarbonInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Options.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.738 IQR)
- **Top Global Matches:** file_cluster_13: 14.738, file_cluster_8: 15.039, file_cluster_17: 15.057
- **Magnitude:** 167.54 | **LOC:** 218 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.653%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `settings` (Impact: 33.7)
    * *Intent:* /**
  * `addExtraDebugInfos` (Impact: 18.6)
  * `getSettings` (Impact: 13.5)
    * *Intent:* /** * Function to call instead of format.
  * `__debugInfo` (Impact: 9.9)
  * `isLocalStrictModeEnabled` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 24`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 80`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 26`, `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.527
  * `Choke Point (Betweenness):` 0.000159 | `Ripple Effect (Closeness):` 0.009693
  * `Imports (Out-Degree: 2):` Carbon\CarbonInterface, Throwable, Localization, DateTimeInterface, StaticOptions
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Mixin.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.932 IQR)
- **Top Global Matches:** file_cluster_13: 12.932, file_cluster_8: 13.218, file_cluster_11: 13.423
- **Magnitude:** 160.04 | **LOC:** 240 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (44.9998%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadMixinTrait` (Impact: 37.4)
  * `cannotBeAMixinMethod` (Impact: 15.4)
    * *Intent:* * Mix another object into the class. * * @example * ``` * Carbon::mixin(new class { * public functio...
  * `loadMixinClass` (Impact: 10.9)
    * *Intent:* /**
  * `getMixableMethods` (Impact: 8.5)
  * `bindMacroContext` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 50`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 57`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 16`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.288
  * `Choke Point (Betweenness):` 9.4e-05 | `Ripple Effect (Closeness):` 0.00917
  * `Imports (Out-Degree: 2):` Generator, ReflectionNamedType, Carbon\CarbonInterface, ReflectionException, Carbon\CarbonInterval, Throwable, d to handle error if not converted into exceptions
                    $closure = @$closureBase->bindTo($context, ReflectionMethod...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Carbon/WrapperClock.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.081 IQR)
- **Top Global Matches:** file_cluster_13: 13.081, file_cluster_8: 13.341, file_cluster_11: 13.556
- **Magnitude:** 150.74 | **LOC:** 188 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.3786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sleep` (Impact: 13.2)
  * `withTimeZone` (Impact: 11.0)
  * `getFactory` (Impact: 8.2)
  * `addSeconds` (Impact: 8.2)
  * `nowAsCarbon` (Impact: 7.7)
    * *Intent:* /** * @template T of CarbonInterface
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 53`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 64`
* *Architecture:* `api: 13`, `import: 7`
* *Defense:* `safety: 15`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.718
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.009139
  * `Imports (Out-Degree: 1):` Psr\Clock\ClockInterface, DateTimeImmutable, Symfony\Component\Clock\ClockInterface, DateTime, RuntimeException, DateTimeZone, DateTimeInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Carbon/Laravel/ServiceProvider.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.599 IQR)
- **Top Global Matches:** file_cluster_13: 12.599, file_cluster_8: 12.909, file_cluster_7: 13.216
- **Magnitude:** 141.38 | **LOC:** 179 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.6315%), Tech Debt (85.3656%)
**Top Internal Functions/Classes:**
  * `updateFallbackLocale` (Impact: 13.4)
  * `updateLocale` (Impact: 11.7)
  * `getLocale` (Impact: 9.3)
  * `getFallbackLocale` (Impact: 9.3)
  * `boot` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 41`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`, `orphaned_logic: 5`
* *Architecture:* `api: 7`, `import: 10`
* *Defense:* `safety: 12`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\Carbon, Illuminate\Support\Carbon, Carbon\CarbonInterval, Illuminate\Support\Facades\Date, Throwable, Carbon\CarbonImmutable, Carbon\CarbonPeriod, Illuminate\Events\Dispatcher...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Timestamp.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.722 IQR)
- **Top Global Matches:** file_cluster_8: 12.722, file_cluster_7: 12.891, file_cluster_13: 12.937
- **Magnitude:** 123.48 | **LOC:** 193 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.9392%), Tech Debt (83.2643%)
**Top Internal Functions/Classes:**
  * `getIntegerAndDecimalParts` (Impact: 11.5)
    * *Intent:* /** * Returns the timestamp with millisecond precision. * * @return int */
  * `createFromTimestampMsUTC` (Impact: 7.6)
  * `createFromTimestamp` (Impact: 4.5)
  * `createFromTimestampMs` (Impact: 4.4)
  * `createFromTimestampUTC` (Impact: 2.5)
    * *Intent:* /** * Create a Carbon instance from a timestamp and set the timezone (UTC by default). *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 33`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 71`, `orphaned_logic: 5`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DateTimeZone
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/PHPStan/MacroExtension.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.792 IQR)
- **Top Global Matches:** file_cluster_13: 13.792, file_cluster_8: 14.421, file_cluster_11: 14.447
- **Magnitude:** 121.94 | **LOC:** 138 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.3083%), Tech Debt (82.0978%)
**Top Internal Functions/Classes:**
  * `getMethod` (Impact: 30.5)
  * `hasMethod` (Impact: 7.6)
  * `__construct` (Impact: 2.1)
    * *Intent:* /** * Class MacroExtension. *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 31`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 77`, `orphaned_logic: 3`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `safety: 9`, `doc: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` PHPStan\Reflection\MethodsClassReflectionExtension, Carbon\FactoryImmutable, ReflectionFunction, PHPStan\Reflection\ClassReflection, InvalidArgumentException, PHPStan\Reflection\MethodReflection, Throwable, PHPStan\Type\ClosureTypeFactory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Boundaries.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.178 IQR)
- **Top Global Matches:** file_cluster_8: 12.178, file_cluster_13: 12.271, file_cluster_7: 12.314
- **Magnitude:** 116.54 | **LOC:** 470 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.7659%), Tech Debt (99.9993%)
**Top Internal Functions/Classes:**
  * `startOf` (Impact: 5.7)
    * *Intent:* /** * Resets the date to end of the decade and time to 23:59:59.999999 * * @example * ``` * echo Car...
  * `endOf` (Impact: 5.7)
    * *Intent:* /** * Resets the date to the first day of the century and the time to 00:00:00 * * @example * ```
  * `startOfWeek` (Impact: 5.3)
  * `endOfWeek` (Impact: 5.3)
    * *Intent:* /** * Resets the date to end of the quarter and time to 23:59:59.999999 * * @example * ``` * echo Ca...
  * `startOfQuarter` (Impact: 2.0)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 60`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `orphaned_logic: 20`
* *Architecture:* `api: 26`, `import: 3`
* *Defense:* `safety: 4`, `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carbon\WeekDay, Carbon\Exceptions\UnknownUnitException, Carbon\Unit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `tests/Laravel/EventDispatcher.php` (PHP) | Magnitude: 13.64 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, branch: 1, class_start: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `lazy/Carbon/TranslatorStrongType.php` (PHP) | Magnitude: 40.76 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, state_mutation: 18, structural_boundaries: 16, branch: 8
- `tests/CarbonImmutable/Fixtures/Mixin.php` (PHP) | Magnitude: 0.02 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 13, state_mutation: 11, api: 5
- `src/Carbon/Carbon.php` (PHP) | Magnitude: 4.18 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 810, structural_boundaries: 11, indent_spaces: 5, import: 4
- `src/Carbon/Month.php` (PHP) | Magnitude: 42.88 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, branch: 22, structural_boundaries: 14, state_mutation: 9
- `src/Carbon/CarbonImmutable.php` (PHP) | Magnitude: 19.76 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 815, indent_spaces: 29, structural_boundaries: 19, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/Carbon/Traits/DeprecatedPeriodProperties.php` (PHP) | Magnitude: 22.3 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 22, api: 7, indent_spaces: 7, structural_boundaries: 5
- `src/Carbon/Traits/Macro.php` (PHP) | Magnitude: 39.3 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 16, doc: 15, args: 9
- `tests/Laravel/EventDispatcherBase.php` (PHP) | Magnitude: 14.56 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 6, branch: 4, state_mutation: 3
- `lazy/Carbon/MessageFormatter/MessageFormatterMapperWeakType.php` (PHP) | Magnitude: 9.24 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 10, branch: 4, args: 3
- `src/Carbon/Lang/en_HK.php` (PHP) | Magnitude: 12.08 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, branch: 1, doc: 1, import: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Carbon/CarbonInterval.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 2571.44
- `src/Carbon/CarbonPeriod.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 1909.14
- `src/Carbon/Traits/Localization.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 727.72
- `src/Carbon/Traits/Creator.php` -> **Sam Anglin** (100.0% isolated ownership) | Magnitude: 678.2
- `phpdoc.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 563.88

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

- `src/Carbon/FactoryImmutable.php` -> **Severity: 1.613** (Embedded: 0.0161 * Error Risk: 99.9634%)
- `src/Carbon/CarbonInterval.php` -> **Severity: 1.335** (Embedded: 0.0144 * Error Risk: 92.6167%)
- `src/Carbon/Factory.php` -> **Severity: 0.786** (Embedded: 0.0101 * Error Risk: 78.0314%)
- `src/Carbon/Traits/IntervalRounding.php` -> **Severity: 0.782** (Embedded: 0.0098 * Error Risk: 80.0911%)
- `src/Carbon/Exceptions/ParseErrorException.php` -> **Severity: 0.737** (Embedded: 0.0087 * Error Risk: 84.6913%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Carbon/Carbon.php` -> **Severity: 176.764** (Blast Radius: 10.592 * Doc Risk: 16.6884%)
- `src/Carbon/WeekDay.php` -> **Severity: 149.695** (Blast Radius: 1.634 * Doc Risk: 91.6124%)
- `src/Carbon/Unit.php` -> **Severity: 147.458** (Blast Radius: 1.543 * Doc Risk: 95.5659%)
- `src/Carbon/Exceptions/InvalidArgumentException.php` -> **Severity: 143.784** (Blast Radius: 24.476 * Doc Risk: 5.8745%)
- `src/Carbon/CarbonInterval.php` -> **Severity: 141.416** (Blast Radius: 7.909 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
