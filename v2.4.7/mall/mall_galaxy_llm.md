# ARCHITECTURAL_BRIEF: mall
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/mall` |
| **Timestamp** | `2026-08-07T05:08:35.511791+00:00` |
| **Scan Duration** | `2.41s` |
| **Git Branch** | `master` |
| **Git Commit** | `d9501e97a78eb2bb0ae8eaa273eeb1cfc7c5d386` |
| **Git Remote** | `https://github.com/macrozheng/mall.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 530 malicious artifacts.

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
| Total Artifacts | 719 |
| Analyzed Artifacts (Scanned) | 669 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 50 |
| Total LOC | 66769 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 93.0% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8048 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1131 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.0116 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 106 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 525 | 65662 | 78.5% |
| XML | 114 | 0 | 17.0% |
| YAML | 12 | 513 | 1.8% |
| MARKDOWN | 9 | 0 | 1.3% |
| SHELL | 4 | 73 | 0.6% |
| JSON | 2 | 516 | 0.3% |
| PLAINTEXT | 2 | 0 | 0.3% |
| DOCKERFILE | 1 | 5 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.461`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 379 | 56.7% |
| file_cluster_13 | 215 | 32.1% |
| file_cluster_0 | 42 | 6.3% |
| file_cluster_16 | 22 | 3.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 1.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 50*

**Composition by Extension & Reason:**
- `.jpg`: 12x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.pos"')
- `.emmx`: 7x Excluded (Unsupported Extension: '.emmx')
- `.rp`: 2x Excluded (Unsupported Extension: '.rp')
- `.conf`: 2x Excluded (Unsupported Extension: '.conf')
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.pdb`: 1x Excluded (Unsupported Extension: '.pdb')
- `.pdm`: 1x Excluded (Unsupported Extension: '.pdm')
- `.sql`: 1x Excluded (Massive Static Asset Blob: 3258 LOC)
- `.java`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 7.1 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 32.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.7 | 2.3 | 2.3 |
| API Exposure | 0.0 | 17.3 | 6.1 | 4.3 | 0.0 |
| Concurrency Exposure | 0.0 | 54.8 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 78.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.2 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 86.0 | 1.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 45.7 | 27.9 | 0.8 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `document/sh/mall-admin.sh` (Hits: 3)
- `document/sh/mall-portal.sh` (Hits: 3)
- `document/sh/mall-search.sh` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CommonResult.java** (`mall-common/src/main/java/com/macro/mall/common/api/CommonResult.java`) — 50 inbound connections
2. **CommonPage.java** (`mall-common/src/main/java/com/macro/mall/common/api/CommonPage.java`) — 34 inbound connections
3. **PmsProduct.java** (`mall-mbg/src/main/java/com/macro/mall/model/PmsProduct.java`) — 20 inbound connections
4. **PmsBrand.java** (`mall-mbg/src/main/java/com/macro/mall/model/PmsBrand.java`) — 14 inbound connections
5. **UmsMember.java** (`mall-mbg/src/main/java/com/macro/mall/model/UmsMember.java`) — 12 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **EsProductServiceImpl.java** (`mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java`) — 42 outbound dependencies
2. **UmsAdminServiceImpl.java** (`mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java`) — 35 outbound dependencies
3. **UmsMemberServiceImpl.java** (`mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberServiceImpl.java`) — 30 outbound dependencies
4. **UmsAdminController.java** (`mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java`) — 24 outbound dependencies
5. **OmsPortalOrderServiceImpl.java** (`mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `calcCartPromotion` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java`) -> Impact: **50.7** | LOC: 83
- `search` (@ `mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java`) -> Impact: **50.7** | LOC: 62
- `getRequestIp` (@ `mall-common/src/main/java/com/macro/mall/common/util/RequestUtil.java`) -> Impact: **43.1** | LOC: 30
  * *Intent:* /** * 请求工具类 * Created by macro on 2020/10/8. */
- `list` (@ `mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java`) -> Impact: **38.4** | LOC: 34
- `listCart` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java`) -> Impact: **37.5** | LOC: 57
- `generateOrder` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) -> Impact: **35.9** | LOC: 158
- `getCouponOrderItemByRelation` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) -> Impact: **33.5** | LOC: 29
- `search` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalProductServiceImpl.java`) -> Impact: **30.5** | LOC: 28
- `convertProductRelatedInfo` (@ `mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java`) -> Impact: **26.6** | LOC: 40
- `cancelOrder` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) -> Impact: **21.3** | LOC: 35

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `mall-mbg/src/main/java/com/macro/mall/model` | 152 | 57443.0 | 5.74% | 45.91% |
| `mall-mbg/src/main/java/com/macro/mall/mapper` | 76 | 3456.76 | 5.21% | 0.0% |
| `mall-portal/src/main/java/com/macro/mall/portal/service/impl` | 15 | 1627.1 | 26.2% | 84.04% |
| `mall-admin/src/main/java/com/macro/mall/service/impl` | 31 | 1538.78 | 20.53% | 94.62% |
| `mall-admin/src/main/java/com/macro/mall/service` | 31 | 999.65 | 4.45% | 0.0% |
| `mall-admin/src/main/java/com/macro/mall/controller` | 31 | 851.02 | 5.82% | 7.26% |
| `mall-mbg/src/main/resources/com/macro/mall/mapper` | 76 | 799.52 | 5.0% | 0.0% |
| `mall-admin/src/main/java/com/macro/mall/dto` | 29 | 507.94 | 4.65% | 0.0% |
| `mall-portal/src/main/java/com/macro/mall/portal/service` | 15 | 479.41 | 4.7% | 0.0% |
| `mall-portal/src/main/java/com/macro/mall/portal/controller` | 13 | 359.28 | 7.51% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `mall-common/src/main/java/com/macro/mall/common/api/CommonResult.java` -> **100.0%** Exposure
- `mall-common/src/main/java/com/macro/mall/common/exception/ApiException.java` -> **100.0%** Exposure
- `mall-common/src/main/java/com/macro/mall/common/exception/Asserts.java` -> **100.0%** Exposure
- `mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java` -> **100.0%** Exposure
- `mall-security/src/main/java/com/macro/mall/security/config/CommonSecurityConfig.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java` -> **100.0%** Exposure
- `mall-common/src/main/java/com/macro/mall/common/api/CommonPage.java` -> **100.0%** Exposure
- `mall-common/src/main/java/com/macro/mall/common/config/BaseRedisConfig.java` -> **100.0%** Exposure
- `mall-security/src/main/java/com/macro/mall/security/component/RestAuthenticationEntryPoint.java` -> **100.0%** Exposure
- `mall-security/src/main/java/com/macro/mall/security/component/RestfulAccessDeniedHandler.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionExample.java` -> **0** Orphaned Functions | **16** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionSessionExample.java` -> **0** Orphaned Functions | **16** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberExample.java` -> **0** Orphaned Functions | **16** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttributeExample.java` -> **0** Orphaned Functions | **15** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/model/PmsProductExample.java` -> **0** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`** -> AI Confidence: **99.31%**
2. **`mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java`** -> AI Confidence: **99.24%**
3. **`mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java`** -> AI Confidence: **99.24%**
4. **`mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java`** -> AI Confidence: **99.24%**
5. **`mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCacheServiceImpl.java`** -> AI Confidence: **99.24%**
6. **`mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java`** -> AI Confidence: **99.24%**
7. **`mall-common/src/main/java/com/macro/mall/common/util/RequestUtil.java`** -> AI Confidence: **99.2%**
8. **`mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java`** -> AI Confidence: **99.18%**
9. **`mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java`** -> AI Confidence: **99.18%**
10. **`mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java`** -> AI Confidence: **99.18%**
11. **`mall-admin/src/main/java/com/macro/mall/controller/UmsResourceCategoryController.java`** -> AI Confidence: **99.18%**
12. **`mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java`** -> AI Confidence: **99.18%**
13. **`mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java`** -> AI Confidence: **99.18%**
14. **`mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java`** -> AI Confidence: **99.18%**
15. **`mall-common/src/main/java/com/macro/mall/common/exception/GlobalExceptionHandler.java`** -> AI Confidence: **99.18%**
16. **`mall-mbg/src/main/java/com/macro/mall/CommentGenerator.java`** -> AI Confidence: **99.18%**
17. **`mall-security/src/main/java/com/macro/mall/security/component/DynamicAccessDecisionManager.java`** -> AI Confidence: **99.18%**
18. **`mall-security/src/main/java/com/macro/mall/security/util/JwtTokenUtil.java`** -> AI Confidence: **99.18%**
19. **`mall-admin/src/main/java/com/macro/mall/controller/MinioController.java`** -> AI Confidence: **99.16%**
20. **`mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java`** -> AI Confidence: **99.16%**
21. **`mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java`** -> AI Confidence: **99.16%**
22. **`mall-admin/src/main/java/com/macro/mall/service/impl/SmsCouponServiceImpl.java`** -> AI Confidence: **99.16%**
23. **`mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java`** -> AI Confidence: **99.16%**
24. **`mall-demo/src/main/java/com/macro/mall/demo/controller/DemoController.java`** -> AI Confidence: **99.16%**
25. **`mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalProductServiceImpl.java`** -> AI Confidence: **99.16%**
26. **`mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java`** -> AI Confidence: **99.16%**
27. **`mall-admin/src/main/java/com/macro/mall/controller/CmsPrefrenceAreaController.java`** -> AI Confidence: **99.09%**
28. **`mall-admin/src/main/java/com/macro/mall/controller/CmsSubjectController.java`** -> AI Confidence: **99.09%**
29. **`mall-admin/src/main/java/com/macro/mall/controller/OmsCompanyAddressController.java`** -> AI Confidence: **99.09%**
30. **`mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java`** -> AI Confidence: **99.09%**
31. **`mall-admin/src/main/java/com/macro/mall/controller/OssController.java`** -> AI Confidence: **99.09%**
32. **`mall-admin/src/main/java/com/macro/mall/controller/SmsCouponHistoryController.java`** -> AI Confidence: **99.09%**
33. **`mall-admin/src/main/java/com/macro/mall/controller/UmsMemberLevelController.java`** -> AI Confidence: **99.09%**
34. **`mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java`** -> AI Confidence: **99.09%**
35. **`mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeCategoryServiceImpl.java`** -> AI Confidence: **99.09%**
36. **`mall-admin/src/main/java/com/macro/mall/service/impl/PmsSkuStockServiceImpl.java`** -> AI Confidence: **99.09%**
37. **`mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionServiceImpl.java`** -> AI Confidence: **99.09%**
38. **`mall-admin/src/main/java/com/macro/mall/service/impl/SmsFlashPromotionSessionServiceImpl.java`** -> AI Confidence: **99.09%**
39. **`mall-admin/src/test/com/macro/mall/PmsDaoTests.java`** -> AI Confidence: **99.09%**
40. **`mall-common/src/main/java/com/macro/mall/common/config/BaseRedisConfig.java`** -> AI Confidence: **99.09%**
41. **`mall-common/src/main/java/com/macro/mall/common/config/BaseSwaggerConfig.java`** -> AI Confidence: **99.09%**
42. **`mall-demo/src/main/java/com/macro/mall/demo/config/SecurityConfig.java`** -> AI Confidence: **99.09%**
43. **`mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java`** -> AI Confidence: **99.09%**
44. **`mall-demo/src/main/java/com/macro/mall/demo/service/impl/DemoServiceImpl.java`** -> AI Confidence: **99.09%**
45. **`mall-portal/src/main/java/com/macro/mall/portal/controller/AlipayController.java`** -> AI Confidence: **99.09%**
46. **`mall-portal/src/main/java/com/macro/mall/portal/controller/HomeController.java`** -> AI Confidence: **99.09%**
47. **`mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderController.java`** -> AI Confidence: **99.09%**
48. **`mall-portal/src/main/java/com/macro/mall/portal/controller/OmsPortalOrderReturnApplyController.java`** -> AI Confidence: **99.09%**
49. **`mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalBrandController.java`** -> AI Confidence: **99.09%**
50. **`mall-portal/src/main/java/com/macro/mall/portal/controller/PmsPortalProductController.java`** -> AI Confidence: **99.09%**
51. **`mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalBrandServiceImpl.java`** -> AI Confidence: **99.09%**
52. **`mall-search/src/main/java/com/macro/mall/search/domain/EsProduct.java`** -> AI Confidence: **99.09%**
53. **`mall-search/src/test/java/com/macro/mall/search/MallSearchApplicationTests.java`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `14` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2907` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java` (JAVA) -> Cumulative Risk: **600.5**
- **Archetype:** `file_cluster_13` (Distance: 10.577 IQR)
- **Magnitude:** 163.8 | **LOC:** 288 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.4981%), Tech Debt (97.7023%), Safety Score (83.7953%)
- **Heaviest Functions:** `login` (Impact: 11.5), `updateRole` (Impact: 11.4), `updatePassword` (Impact: 10.9)

### 2. `mall-mbg/src/main/java/com/macro/mall/model/PmsProductCategoryAttributeRelationExample.java` (JAVA) -> Cumulative Risk: **552.69**
- **Archetype:** `file_cluster_8` (Distance: 9.599 IQR)
- **Magnitude:** 345.16 | **LOC:** 379 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9777%), Safety Score (96.4493%)
- **Heaviest Functions:** `super` (Impact: 12.4), `Criterion` (Impact: 8.6), `addCriterion` (Impact: 7.0)

### 3. `mall-mbg/src/main/java/com/macro/mall/model/CmsPrefrenceAreaProductRelationExample.java` (JAVA) -> Cumulative Risk: **552.65**
- **Archetype:** `file_cluster_8` (Distance: 9.598 IQR)
- **Magnitude:** 344.16 | **LOC:** 379 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9777%), Safety Score (96.4493%)
- **Heaviest Functions:** `super` (Impact: 12.4), `Criterion` (Impact: 8.6), `addCriterion` (Impact: 7.0)

### 4. `mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectProductRelationExample.java` (JAVA) -> Cumulative Risk: **552.65**
- **Archetype:** `file_cluster_8` (Distance: 9.598 IQR)
- **Magnitude:** 344.16 | **LOC:** 379 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9777%), Safety Score (96.4493%)
- **Heaviest Functions:** `super` (Impact: 12.4), `Criterion` (Impact: 8.6), `addCriterion` (Impact: 7.0)

### 5. `mall-mbg/src/main/java/com/macro/mall/model/UmsAdminRoleRelationExample.java` (JAVA) -> Cumulative Risk: **552.65**
- **Archetype:** `file_cluster_8` (Distance: 9.598 IQR)
- **Magnitude:** 344.16 | **LOC:** 379 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9777%), Safety Score (96.4493%)
- **Heaviest Functions:** `super` (Impact: 12.4), `Criterion` (Impact: 8.6), `addCriterion` (Impact: 7.0)

### 6. `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberMemberTagRelationExample.java` (JAVA) -> Cumulative Risk: **552.65**
- **Archetype:** `file_cluster_8` (Distance: 9.598 IQR)
- **Magnitude:** 344.16 | **LOC:** 379 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9777%), Safety Score (96.4493%)
- **Heaviest Functions:** `super` (Impact: 12.4), `Criterion` (Impact: 8.6), `addCriterion` (Impact: 7.0)

### 7. `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberProductCategoryRelationExample.java` (JAVA) -> Cumulative Risk: **552.65**
- **Archetype:** `file_cluster_8` (Distance: 9.598 IQR)
- **Magnitude:** 344.16 | **LOC:** 379 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9777%), Safety Score (96.4493%)
- **Heaviest Functions:** `super` (Impact: 12.4), `Criterion` (Impact: 8.6), `addCriterion` (Impact: 7.0)

### 8. `mall-mbg/src/main/java/com/macro/mall/model/UmsRoleMenuRelationExample.java` (JAVA) -> Cumulative Risk: **552.65**
- **Archetype:** `file_cluster_8` (Distance: 9.598 IQR)
- **Magnitude:** 344.16 | **LOC:** 379 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9777%), Safety Score (96.4493%)
- **Heaviest Functions:** `super` (Impact: 12.4), `Criterion` (Impact: 8.6), `addCriterion` (Impact: 7.0)

### 9. `mall-mbg/src/main/java/com/macro/mall/model/UmsRolePermissionRelationExample.java` (JAVA) -> Cumulative Risk: **552.65**
- **Archetype:** `file_cluster_8` (Distance: 9.598 IQR)
- **Magnitude:** 344.16 | **LOC:** 379 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9777%), Safety Score (96.4493%)
- **Heaviest Functions:** `super` (Impact: 12.4), `Criterion` (Impact: 8.6), `addCriterion` (Impact: 7.0)

### 10. `mall-mbg/src/main/java/com/macro/mall/model/UmsRoleResourceRelationExample.java` (JAVA) -> Cumulative Risk: **552.65**
- **Archetype:** `file_cluster_8` (Distance: 9.598 IQR)
- **Magnitude:** 344.16 | **LOC:** 379 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9777%), Safety Score (96.4493%)
- **Heaviest Functions:** `super` (Impact: 12.4), `Criterion` (Impact: 8.6), `addCriterion` (Impact: 7.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.478 IQR)
- **Top Global Matches:** file_cluster_8: 9.478, file_cluster_16: 10.029, file_cluster_7: 10.134
- **Magnitude:** 2643.28 | **LOC:** 3011 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8159%), Tech Debt (24.0839%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 605`, `args: 594`, `func_start: 1163`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 661`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 1181`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.603
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.44 IQR)
- **Top Global Matches:** file_cluster_8: 9.44, file_cluster_16: 9.984, file_cluster_7: 10.095
- **Magnitude:** 2282.32 | **LOC:** 2601 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.9159%), Tech Debt (33.3223%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 523`, `args: 512`, `func_start: 999`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 567`, `state_mutation: 18`, `duplicate_logic: 15`
* *Architecture:* `api: 1015`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004491
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal, java.util.Date
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderReturnApplyExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.435 IQR)
- **Top Global Matches:** file_cluster_8: 9.435, file_cluster_16: 9.975, file_cluster_7: 10.082
- **Magnitude:** 1735.24 | **LOC:** 1971 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1568%), Tech Debt (39.3513%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 397`, `args: 386`, `func_start: 747`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 419`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 765`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderItemExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.493 IQR)
- **Top Global Matches:** file_cluster_8: 9.493, file_cluster_16: 10.008, file_cluster_7: 10.129
- **Magnitude:** 1358.34 | **LOC:** 1540 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.4466%), Tech Debt (53.7116%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 310`, `args: 300`, `func_start: 575`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 321`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 593`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.559 IQR)
- **Top Global Matches:** file_cluster_8: 9.559, file_cluster_16: 10.05, file_cluster_7: 10.181
- **Magnitude:** 1282.0 | **LOC:** 1447 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9489%), Tech Debt (72.3763%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `addCriterionForJDBCDate` (Impact: 8.6)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 298`, `args: 279`, `func_start: 531`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 300`, `state_mutation: 21`, `duplicate_logic: 16`
* *Architecture:* `api: 548`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Iterator, java.util.List, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsCartItemExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.4 IQR)
- **Top Global Matches:** file_cluster_8: 9.4, file_cluster_16: 9.914, file_cluster_7: 10.037
- **Magnitude:** 1201.28 | **LOC:** 1361 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.6265%), Tech Debt (62.2026%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 275`, `args: 264`, `func_start: 503`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 279`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 521`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/SmsCouponExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.455 IQR)
- **Top Global Matches:** file_cluster_8: 9.455, file_cluster_16: 9.949, file_cluster_7: 10.087
- **Magnitude:** 1156.48 | **LOC:** 1311 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.6866%), Tech Debt (64.8631%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 265`, `args: 254`, `func_start: 483`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 269`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 501`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberStatisticsInfoExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.433 IQR)
- **Top Global Matches:** file_cluster_8: 9.433, file_cluster_16: 9.913, file_cluster_7: 10.062
- **Magnitude:** 1024.88 | **LOC:** 1161 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9018%), Tech Debt (73.4449%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 235`, `args: 224`, `func_start: 423`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 235`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 441`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.352 IQR)
- **Top Global Matches:** file_cluster_8: 9.352, file_cluster_16: 9.854, file_cluster_7: 9.987
- **Magnitude:** 1017.3 | **LOC:** 1150 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9205%), Tech Debt (74.1142%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 232`, `args: 222`, `func_start: 419`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 231`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 437`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsCommentExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.357 IQR)
- **Top Global Matches:** file_cluster_8: 9.357, file_cluster_16: 9.86, file_cluster_7: 9.989
- **Magnitude:** 973.9 | **LOC:** 1100 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0088%), Tech Debt (77.1056%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 222`, `args: 212`, `func_start: 399`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 219`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 417`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberLevelExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.416 IQR)
- **Top Global Matches:** file_cluster_8: 9.416, file_cluster_16: 9.895, file_cluster_7: 10.042
- **Magnitude:** 885.7 | **LOC:** 1000 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2158%), Tech Debt (83.0342%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 202`, `args: 192`, `func_start: 359`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 197`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 377`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.844
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004491
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/SmsHomeAdvertiseExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.37 IQR)
- **Top Global Matches:** file_cluster_8: 9.37, file_cluster_16: 9.858, file_cluster_7: 9.997
- **Magnitude:** 851.26 | **LOC:** 960 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3126%), Tech Debt (85.3147%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 194`, `args: 184`, `func_start: 343`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 187`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 361`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttributeExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.338 IQR)
- **Top Global Matches:** file_cluster_8: 9.338, file_cluster_16: 9.822, file_cluster_7: 9.967
- **Magnitude:** 831.32 | **LOC:** 939 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3678%), Tech Debt (92.6%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 189`, `args: 180`, `func_start: 335`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 183`, `state_mutation: 18`, `duplicate_logic: 15`
* *Architecture:* `api: 351`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductOperateLogExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.633 IQR)
- **Top Global Matches:** file_cluster_8: 9.633, file_cluster_16: 10.089, file_cluster_7: 10.242
- **Magnitude:** 824.4 | **LOC:** 931 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.388%), Tech Debt (86.8971%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 189`, `args: 178`, `func_start: 331`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 181`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 349`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductCategoryExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.344 IQR)
- **Top Global Matches:** file_cluster_8: 9.344, file_cluster_16: 9.833, file_cluster_7: 9.971
- **Magnitude:** 798.88 | **LOC:** 899 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.4801%), Tech Debt (88.6131%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 181`, `args: 172`, `func_start: 319`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 173`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 337`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/CmsTopicExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.386 IQR)
- **Top Global Matches:** file_cluster_8: 9.386, file_cluster_16: 9.865, file_cluster_7: 10.009
- **Magnitude:** 789.94 | **LOC:** 890 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5061%), Tech Debt (89.06%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 180`, `args: 170`, `func_start: 315`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 333`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsSkuStockExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.507 IQR)
- **Top Global Matches:** file_cluster_8: 9.507, file_cluster_16: 9.977, file_cluster_7: 10.123
- **Magnitude:** 789.94 | **LOC:** 890 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5061%), Tech Debt (89.06%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 180`, `args: 170`, `func_start: 315`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 333`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.math.BigDecimal
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/SmsCouponHistoryExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.386 IQR)
- **Top Global Matches:** file_cluster_8: 9.386, file_cluster_16: 9.865, file_cluster_7: 10.009
- **Magnitude:** 789.94 | **LOC:** 890 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5061%), Tech Debt (89.06%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 180`, `args: 170`, `func_start: 315`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 333`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsCompanyAddressExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.346 IQR)
- **Top Global Matches:** file_cluster_8: 9.346, file_cluster_16: 9.846, file_cluster_7: 9.972
- **Magnitude:** 773.4 | **LOC:** 869 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5722%), Tech Debt (90.1157%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 175`, `args: 166`, `func_start: 307`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 165`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 325`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberReceiveAddressExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.346 IQR)
- **Top Global Matches:** file_cluster_8: 9.346, file_cluster_16: 9.846, file_cluster_7: 9.972
- **Magnitude:** 773.4 | **LOC:** 869 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5722%), Tech Debt (90.1157%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 175`, `args: 166`, `func_start: 307`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 165`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 325`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.632
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsAdminExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.388 IQR)
- **Top Global Matches:** file_cluster_8: 9.388, file_cluster_16: 9.878, file_cluster_7: 10.01
- **Magnitude:** 764.46 | **LOC:** 860 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6004%), Tech Debt (90.5374%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 174`, `args: 164`, `func_start: 303`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 163`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 321`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsPermissionExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.396 IQR)
- **Top Global Matches:** file_cluster_8: 9.396, file_cluster_16: 9.876, file_cluster_7: 10.017
- **Magnitude:** 746.54 | **LOC:** 840 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6676%), Tech Debt (91.4711%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 170`, `args: 160`, `func_start: 295`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 313`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsBrandExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.358 IQR)
- **Top Global Matches:** file_cluster_8: 9.358, file_cluster_16: 9.843, file_cluster_7: 9.982
- **Magnitude:** 746.52 | **LOC:** 839 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6719%), Tech Debt (91.528%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 169`, `args: 160`, `func_start: 295`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 313`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004491
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMenuExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.418 IQR)
- **Top Global Matches:** file_cluster_8: 9.418, file_cluster_16: 9.887, file_cluster_7: 10.034
- **Magnitude:** 685.22 | **LOC:** 770 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.9354%), Tech Debt (94.3702%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 156`, `args: 146`, `func_start: 267`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 143`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 285`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/CmsMemberReportExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.439 IQR)
- **Top Global Matches:** file_cluster_8: 9.439, file_cluster_16: 9.901, file_cluster_7: 10.05
- **Magnitude:** 632.86 | **LOC:** 710 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2154%), Tech Debt (96.3478%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 12.4)
  * `Criterion` (Impact: 8.6)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 7.0)
  * `addCriterion` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 144`, `args: 134`, `func_start: 243`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 129`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 261`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `mall-admin/src/main/java/com/macro/mall/dto/OssPolicyResult.java` (JAVA) | Magnitude: 17.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, decorators: 8, encapsulation: 6, structural_boundaries: 5
- `mall-admin/src/main/java/com/macro/mall/dto/PmsProductQueryParam.java` (JAVA) | Magnitude: 17.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, decorators: 8, encapsulation: 6, structural_boundaries: 5
- `mall-admin/src/main/java/com/macro/mall/dto/OmsUpdateStatusParam.java` (JAVA) | Magnitude: 17.5 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, decorators: 10, encapsulation: 8, structural_boundaries: 6
- `mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java` (JAVA) | Magnitude: 23.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, decorators: 25, structural_boundaries: 23, import: 15
- `mall-admin/src/main/java/com/macro/mall/dto/OmsReturnApplyQueryParam.java` (JAVA) | Magnitude: 17.4 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, decorators: 8, encapsulation: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java` (JAVA) | Magnitude: 41.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 13, doc: 9, args: 8, func_start: 8
- `mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java` (JAVA) | Magnitude: 35.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 39, decorators: 26, import: 18
- `mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java` (JAVA) | Magnitude: 20.76 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 20, decorators: 18, api: 11
- `mall-admin/src/main/java/com/macro/mall/dto/PmsBrandParam.java` (JAVA) | Magnitude: 17.64 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, decorators: 15, structural_boundaries: 8, encapsulation: 8
- `mall-portal/src/main/java/com/macro/mall/portal/service/OmsPortalOrderReturnApplyService.java` (JAVA) | Magnitude: 17.74 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `mall-admin/src/main/java/com/macro/mall/dao/UmsRoleDao.java` (JAVA) | Magnitude: 16.2 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 4, import: 4, args: 3
- `mall-admin/src/main/java/com/macro/mall/service/SmsHomeBrandService.java` (JAVA) | Magnitude: 31.73 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 6, indent_spaces: 6, structural_boundaries: 5, args: 5
- `mall-admin/src/main/java/com/macro/mall/service/SmsHomeNewProductService.java` (JAVA) | Magnitude: 31.73 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 6, indent_spaces: 6, structural_boundaries: 5, args: 5
- `mall-admin/src/main/java/com/macro/mall/service/SmsHomeRecommendProductService.java` (JAVA) | Magnitude: 31.73 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 6, indent_spaces: 6, structural_boundaries: 5, args: 5
- `mall-admin/src/main/java/com/macro/mall/service/SmsHomeRecommendSubjectService.java` (JAVA) | Magnitude: 31.73 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 6, indent_spaces: 6, structural_boundaries: 5, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `document/sh/Dockerfile` (DOCKERFILE) | Magnitude: 13.6 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ipc_rpc_bridges: 2, func_start: 1, class_start: 1, io: 1
- `mall-demo/src/main/java/com/macro/mall/demo/bo/AdminUserDetails.java` (JAVA) | Magnitude: 33.52 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 18, api: 14, func_start: 8
- `mall-mbg/src/main/java/com/macro/mall/mapper/CmsMemberReportMapper.java` (JAVA) | Magnitude: 36.56 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, args: 7, indent_spaces: 7, func_start: 5
- `mall-portal/src/test/java/com/macro/mall/portal/MallPortalApplicationTests.java` (JAVA) | Magnitude: 4.58 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 3, api: 2, decorators: 2
- `mall-portal/src/main/java/com/macro/mall/portal/domain/MemberDetails.java` (JAVA) | Magnitude: 37.68 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 19, api: 16, func_start: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java` -> **macro** (100.0% isolated ownership) | Magnitude: 163.8

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `mall-portal/src/main/java/com/macro/mall/portal/service/OmsCartItemService.java` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 88.5385%)
- `mall-admin/src/main/java/com/macro/mall/dto/SmsCouponParam.java` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 88.5385%)
- `mall-portal/src/main/java/com/macro/mall/portal/domain/CartProduct.java` -> **Severity: 0.004** (Bridge: 0.0001 * Flux: 52.4979%)
- `mall-common/src/main/java/com/macro/mall/common/config/BaseRedisConfig.java` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `mall-portal/src/main/java/com/macro/mall/portal/domain/PromotionProduct.java` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 56.6274%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `mall-common/src/main/java/com/macro/mall/common/api/CommonResult.java` -> **Severity: 5.141** (Embedded: 0.0748 * Error Risk: 68.6797%)
- `mall-common/src/main/java/com/macro/mall/common/api/CommonPage.java` -> **Severity: 3.751** (Embedded: 0.0512 * Error Risk: 73.2041%)
- `mall-mbg/src/main/java/com/macro/mall/model/PmsProduct.java` -> **Severity: 2.296** (Embedded: 0.0353 * Error Risk: 65.1074%)
- `mall-mbg/src/main/java/com/macro/mall/model/PmsBrand.java` -> **Severity: 1.348** (Embedded: 0.0216 * Error Risk: 62.3356%)
- `mall-mbg/src/main/java/com/macro/mall/model/UmsMember.java` -> **Severity: 1.217** (Embedded: 0.0192 * Error Risk: 63.4924%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `mall-common/src/main/java/com/macro/mall/common/api/CommonResult.java` -> **Severity: 1356.49** (Blast Radius: 13.622 * Doc Risk: 99.5808%)
- `mall-mbg/src/main/java/com/macro/mall/model/PmsProduct.java` -> **Severity: 904.7** (Blast Radius: 9.047 * Doc Risk: 100.0%)
- `mall-mbg/src/main/java/com/macro/mall/model/UmsMember.java` -> **Severity: 772.798** (Blast Radius: 7.728 * Doc Risk: 99.9998%)
- `mall-common/src/main/java/com/macro/mall/common/api/CommonPage.java` -> **Severity: 755.397** (Blast Radius: 7.942 * Doc Risk: 95.1142%)
- `mall-mbg/src/main/java/com/macro/mall/model/UmsResource.java` -> **Severity: 641.054** (Blast Radius: 6.411 * Doc Risk: 99.9929%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
