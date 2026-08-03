# ARCHITECTURAL_BRIEF: mall
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/mall` |
| **Timestamp** | `2026-08-03T21:05:18.475676+00:00` |
| **Scan Duration** | `2.6s` |
| **Git Branch** | `master` |
| **Git Commit** | `d9501e97a78eb2bb0ae8eaa273eeb1cfc7c5d386` |
| **Git Remote** | `https://github.com/macrozheng/mall.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 530 malicious artifacts.

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
| Error & Exception Exposure | 0.0 | 99.3 | 32.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.6 | 2.3 | 80.0 |
| API Exposure | 0.0 | 16.5 | 6.1 | 4.3 | 0.0 |
| Concurrency Exposure | 0.0 | 54.8 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 78.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.2 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 86.0 | 1.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 54.8 | 55.5 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 41.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `search` (@ `mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java`) -> Impact: **288.8** | LOC: 61
- `calcCartPromotion` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java`) -> Impact: **152.8** | LOC: 82
- `cancelOrder` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) -> Impact: **126.9** | LOC: 34
- `getRequestIp` (@ `mall-common/src/main/java/com/macro/mall/common/util/RequestUtil.java`) -> Impact: **126.4** | LOC: 30
  * *Intent:* /** * 请求工具类 * Created by macro on 2020/10/8. */
- `listCart` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java`) -> Impact: **106.7** | LOC: 56
- `getCouponOrderItemByRelation` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) -> Impact: **97.5** | LOC: 29
- `updatePassword` (@ `mall-admin/src/main/java/com/macro/mall/controller/UmsAdminController.java`) -> Impact: **95.9** | LOC: 14
- `list` (@ `mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java`) -> Impact: **93.5** | LOC: 33
- `generateOrder` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) -> Impact: **91.8** | LOC: 157
- `doFilter` (@ `mall-security/src/main/java/com/macro/mall/security/component/DynamicSecurityFilter.java`) -> Impact: **71.2** | LOC: 24

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `updateNote` (@ `mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java`) -> **O(2^N) [Recursive]**
- `list` (@ `mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java`) -> **O(2^N) [Recursive]**
- `list` (@ `mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnApplyController.java`) -> **O(2^N) [Recursive]**
- `updateStatus` (@ `mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java`) -> **O(2^N) [Recursive]**
- `list` (@ `mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java`) -> **O(2^N) [Recursive]**
- `updateShowStatus` (@ `mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java`) -> **O(2^N) [Recursive]**
- `updateFactoryStatus` (@ `mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java`) -> **O(2^N) [Recursive]**
- `getList` (@ `mall-admin/src/main/java/com/macro/mall/controller/PmsProductAttributeController.java`) -> **O(2^N) [Recursive]**
- `update` (@ `mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java`) -> **O(2^N) [Recursive]**
- `getList` (@ `mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `generateOrder` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) -> DB Complexity: **58**
- `calcCartPromotion` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java`) -> DB Complexity: **19**
- `updateStatus` (@ `mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java`) -> DB Complexity: **17**
- `updateReceiverInfo` (@ `mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java`) -> DB Complexity: **14**
- `add` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java`) -> DB Complexity: **10**
- `convertProductRelatedInfo` (@ `mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java`) -> DB Complexity: **10**
- `createBucketPolicyConfigDto` (@ `mall-admin/src/main/java/com/macro/mall/controller/MinioController.java`) -> DB Complexity: **9**
- `updateMoneyInfo` (@ `mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderServiceImpl.java`) -> DB Complexity: **9**
- `policy` (@ `mall-admin/src/main/java/com/macro/mall/service/impl/OssServiceImpl.java`) -> DB Complexity: **9**
- `create` (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberReadHistoryServiceImpl.java`) -> DB Complexity: **9**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `mall-mbg/src/main/java/com/macro/mall/model` | 152 | 78322.6 | 5.75% | 41.73% |
| `mall-mbg/src/main/java/com/macro/mall/mapper` | 76 | 3456.76 | 5.21% | 0.0% |
| `mall-admin/src/main/java/com/macro/mall/controller` | 31 | 3266.82 | 5.79% | 14.69% |
| `mall-portal/src/main/java/com/macro/mall/portal/service/impl` | 15 | 2815.0 | 26.2% | 74.06% |
| `mall-admin/src/main/java/com/macro/mall/service/impl` | 31 | 2220.88 | 20.66% | 93.01% |
| `mall-portal/src/main/java/com/macro/mall/portal/controller` | 13 | 1045.08 | 7.51% | 0.0% |
| `mall-admin/src/main/java/com/macro/mall/service` | 31 | 999.65 | 4.45% | 0.0% |
| `mall-mbg/src/main/resources/com/macro/mall/mapper` | 76 | 799.52 | 5.0% | 0.0% |
| `mall-search/src/main/java/com/macro/mall/search/service/impl` | 1 | 519.92 | 26.44% | 95.6% |
| `mall-admin/src/main/java/com/macro/mall/dto` | 29 | 507.94 | 4.65% | 0.0% |

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
- `mall-common/src/main/java/com/macro/mall/common/service/impl/RedisServiceImpl.java` -> **0** Orphaned Functions | **14** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionExample.java` -> **0** Orphaned Functions | **13** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionSessionExample.java` -> **0** Orphaned Functions | **13** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttributeExample.java` -> **0** Orphaned Functions | **12** Duplicates
- `mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java` -> **10** Orphaned Functions | **0** Duplicates

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

### Exploit Generation Surface
- `mall-admin/src/main/java/com/macro/mall/bo/AdminUserDetails.java` -> **100.0%** Exposure
- `mall-admin/src/main/java/com/macro/mall/config/MallSecurityConfig.java` -> **100.0%** Exposure
- `mall-admin/src/main/java/com/macro/mall/controller/CmsSubjectController.java` -> **100.0%** Exposure
- `mall-admin/src/main/java/com/macro/mall/controller/MinioController.java` -> **100.0%** Exposure
- `mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `mall-admin/src/main/java/com/macro/mall/config/MallSecurityConfig.java` -> **100.0%** Exposure
- `mall-admin/src/main/java/com/macro/mall/controller/MinioController.java` -> **100.0%** Exposure
- `mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java` -> **100.0%** Exposure
- `mall-admin/src/main/java/com/macro/mall/controller/OmsOrderReturnReasonController.java` -> **100.0%** Exposure
- `mall-admin/src/main/java/com/macro/mall/controller/PmsBrandController.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `14` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2907` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java` (JAVA) -> Cumulative Risk: **844.07**
- **Archetype:** `file_cluster_13` (Distance: 11.738 IQR)
- **Magnitude:** 170.62 | **LOC:** 163 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), Logic Bomb (99.9999%)
- **Heaviest Functions:** `notify` (Impact: 40.2), `query` (Impact: 36.2), `pay` (Impact: 23.8)

### 2. `mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductAttributeServiceImpl.java` (JAVA) -> Cumulative Risk: **812.74**
- **Archetype:** `file_cluster_13` (Distance: 10.57 IQR)
- **Magnitude:** 111.3 | **LOC:** 102 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.91%)
- **Heaviest Functions:** `delete` (Impact: 46.0), `create` (Impact: 18.6), `getProductAttrInfo` (Impact: 6.9)

### 3. `mall-portal/src/main/java/com/macro/mall/portal/service/impl/MemberAttentionServiceImpl.java` (JAVA) -> Cumulative Risk: **811.31**
- **Archetype:** `file_cluster_13` (Distance: 10.283 IQR)
- **Magnitude:** 80.3 | **LOC:** 88 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.8729%)
- **Heaviest Functions:** `add` (Impact: 41.6), `delete` (Impact: 3.6), `detail` (Impact: 3.6)

### 4. `mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java` (JAVA) -> Cumulative Risk: **807.46**
- **Archetype:** `file_cluster_13` (Distance: 10.655 IQR)
- **Magnitude:** 266.6 | **LOC:** 288 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getResourceList` (Impact: 27.5), `login` (Impact: 27.0), `updateRole` (Impact: 27.0)

### 5. `mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java` (JAVA) -> Cumulative Risk: **793.22**
- **Archetype:** `file_cluster_13` (Distance: 10.689 IQR)
- **Magnitude:** 519.92 | **LOC:** 290 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.82%)
- **Heaviest Functions:** `search` (Impact: 288.8), `convertProductRelatedInfo` (Impact: 63.5), `recommend` (Impact: 38.2)

### 6. `mall-admin/src/main/java/com/macro/mall/service/impl/PmsBrandServiceImpl.java` (JAVA) -> Cumulative Risk: **784.68**
- **Archetype:** `file_cluster_13` (Distance: 10.137 IQR)
- **Magnitude:** 78.58 | **LOC:** 114 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9965%)
- **Heaviest Functions:** `listBrand` (Impact: 14.1), `createBrand` (Impact: 9.4), `updateBrand` (Impact: 7.7)

### 7. `mall-admin/src/main/java/com/macro/mall/service/impl/UmsMenuServiceImpl.java` (JAVA) -> Cumulative Risk: **784.61**
- **Archetype:** `file_cluster_13` (Distance: 10.987 IQR)
- **Magnitude:** 88.54 | **LOC:** 107 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9862%)
- **Heaviest Functions:** `updateLevel` (Impact: 28.7), `covertMenuNode` (Impact: 9.1), `treeList` (Impact: 5.4)

### 8. `mall-admin/src/main/java/com/macro/mall/service/impl/UmsRoleServiceImpl.java` (JAVA) -> Cumulative Risk: **782.28**
- **Archetype:** `file_cluster_13` (Distance: 10.295 IQR)
- **Magnitude:** 87.78 | **LOC:** 120 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9934%)
- **Heaviest Functions:** `allocMenu` (Impact: 11.1), `allocResource` (Impact: 11.1), `list` (Impact: 8.4)

### 9. `mall-portal/src/main/java/com/macro/mall/portal/service/impl/HomeServiceImpl.java` (JAVA) -> Cumulative Risk: **779.77**
- **Archetype:** `file_cluster_13` (Distance: 9.987 IQR)
- **Magnitude:** 125.38 | **LOC:** 177 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9914%)
- **Heaviest Functions:** `getHomeFlashPromotion` (Impact: 25.2), `getFlashPromotion` (Impact: 11.8), `getFlashPromotionSession` (Impact: 11.8)

### 10. `mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java` (JAVA) -> Cumulative Risk: **779.66**
- **Archetype:** `file_cluster_13` (Distance: 12.086 IQR)
- **Magnitude:** 90.4 | **LOC:** 79 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `updateStatus` (Impact: 25.8), `delete` (Impact: 3.6), `getItem` (Impact: 3.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.398 IQR)
- **Top Global Matches:** file_cluster_8: 9.398, file_cluster_16: 9.982, file_cluster_7: 10.08
- **Magnitude:** 2053.68 | **LOC:** 3011 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (5.8149%), Tech Debt (12.1315%)
**Top Internal Functions/Classes:**
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
  * `clear` (Impact: 6.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 605`, `args: 594`, `func_start: 1163`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 661`, `state_mutation: 18`, `duplicate_logic: 5`
* *Architecture:* `api: 843`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.603
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.371 IQR)
- **Top Global Matches:** file_cluster_8: 9.371, file_cluster_16: 9.943, file_cluster_7: 10.048
- **Magnitude:** 1963.12 | **LOC:** 2601 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (5.9152%), Tech Debt (16.0161%)
**Top Internal Functions/Classes:**
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
  * `clear` (Impact: 6.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 523`, `args: 512`, `func_start: 999`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 567`, `state_mutation: 18`, `duplicate_logic: 7`
* *Architecture:* `api: 759`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004491
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderReturnApplyExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.389 IQR)
- **Top Global Matches:** file_cluster_8: 9.389, file_cluster_16: 9.95, file_cluster_7: 10.054
- **Magnitude:** 1830.04 | **LOC:** 1971 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.1572%), Tech Debt (15.3835%)
**Top Internal Functions/Classes:**
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
  * `clear` (Impact: 6.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 397`, `args: 386`, `func_start: 747`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 419`, `state_mutation: 18`, `duplicate_logic: 5`
* *Architecture:* `api: 635`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.553 IQR)
- **Top Global Matches:** file_cluster_8: 9.553, file_cluster_16: 10.048, file_cluster_7: 10.178
- **Magnitude:** 1755.6 | **LOC:** 1447 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.953%), Tech Debt (31.6826%)
**Top Internal Functions/Classes:**
  * `addCriterionForJDBCDate` (Impact: 20.6 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterionForJDBCDate` (Impact: 17.1 | O(N^4))
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 298`, `args: 279`, `func_start: 533`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 300`, `state_mutation: 21`, `duplicate_logic: 8`
* *Architecture:* `api: 525`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.Iterator, java.util.List, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderItemExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.473 IQR)
- **Top Global Matches:** file_cluster_8: 9.473, file_cluster_16: 10.0, file_cluster_7: 10.122
- **Magnitude:** 1736.14 | **LOC:** 1540 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.449%), Tech Debt (18.5238%)
**Top Internal Functions/Classes:**
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
  * `clear` (Impact: 6.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 310`, `args: 300`, `func_start: 575`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 321`, `state_mutation: 18`, `duplicate_logic: 5`
* *Architecture:* `api: 549`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsCartItemExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.395 IQR)
- **Top Global Matches:** file_cluster_8: 9.395, file_cluster_16: 9.916, file_cluster_7: 10.041
- **Magnitude:** 1698.28 | **LOC:** 1361 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.6307%), Tech Debt (20.6384%)
**Top Internal Functions/Classes:**
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
  * `clear` (Impact: 6.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 275`, `args: 264`, `func_start: 503`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 279`, `state_mutation: 18`, `duplicate_logic: 5`
* *Architecture:* `api: 513`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/SmsCouponExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.453 IQR)
- **Top Global Matches:** file_cluster_8: 9.453, file_cluster_16: 9.953, file_cluster_7: 10.093
- **Magnitude:** 1679.98 | **LOC:** 1311 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.6914%), Tech Debt (21.3714%)
**Top Internal Functions/Classes:**
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
  * `clear` (Impact: 6.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 265`, `args: 254`, `func_start: 483`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 269`, `state_mutation: 18`, `duplicate_logic: 5`
* *Architecture:* `api: 501`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberStatisticsInfoExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.435 IQR)
- **Top Global Matches:** file_cluster_8: 9.435, file_cluster_16: 9.914, file_cluster_7: 10.064
- **Magnitude:** 1515.88 | **LOC:** 1161 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.9066%), Tech Debt (55.1227%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 235`, `args: 224`, `func_start: 423`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 235`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 441`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.353 IQR)
- **Top Global Matches:** file_cluster_8: 9.353, file_cluster_16: 9.856, file_cluster_7: 9.988
- **Magnitude:** 1505.3 | **LOC:** 1150 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.9254%), Tech Debt (55.7801%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 232`, `args: 222`, `func_start: 419`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 231`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 437`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsCommentExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.358 IQR)
- **Top Global Matches:** file_cluster_8: 9.358, file_cluster_16: 9.861, file_cluster_7: 9.991
- **Magnitude:** 1440.5 | **LOC:** 1100 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.0142%), Tech Debt (58.8349%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 222`, `args: 212`, `func_start: 399`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 219`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 417`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberLevelExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.417 IQR)
- **Top Global Matches:** file_cluster_8: 9.417, file_cluster_16: 9.896, file_cluster_7: 10.043
- **Magnitude:** 1307.9 | **LOC:** 1000 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.2225%), Tech Debt (65.5805%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 202`, `args: 192`, `func_start: 359`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 197`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 377`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.844
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004491
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/SmsHomeAdvertiseExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.371 IQR)
- **Top Global Matches:** file_cluster_8: 9.371, file_cluster_16: 9.86, file_cluster_7: 9.999
- **Magnitude:** 1256.66 | **LOC:** 960 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.3199%), Tech Debt (68.4934%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 194`, `args: 184`, `func_start: 343`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 187`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 361`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttributeExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.338 IQR)
- **Top Global Matches:** file_cluster_8: 9.338, file_cluster_16: 9.823, file_cluster_7: 9.968
- **Magnitude:** 1227.52 | **LOC:** 939 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.3756%), Tech Debt (82.0752%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 189`, `args: 180`, `func_start: 335`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 183`, `state_mutation: 18`, `duplicate_logic: 12`
* *Architecture:* `api: 351`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductOperateLogExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.634 IQR)
- **Top Global Matches:** file_cluster_8: 9.634, file_cluster_16: 10.09, file_cluster_7: 10.243
- **Magnitude:** 1216.0 | **LOC:** 931 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.3958%), Tech Debt (70.6486%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 189`, `args: 178`, `func_start: 331`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 181`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 349`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductCategoryExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.345 IQR)
- **Top Global Matches:** file_cluster_8: 9.345, file_cluster_16: 9.834, file_cluster_7: 9.973
- **Magnitude:** 1178.28 | **LOC:** 899 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.4886%), Tech Debt (73.1334%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 181`, `args: 172`, `func_start: 319`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 173`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 337`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/CmsTopicExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.387 IQR)
- **Top Global Matches:** file_cluster_8: 9.387, file_cluster_16: 9.866, file_cluster_7: 10.01
- **Magnitude:** 1164.74 | **LOC:** 890 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.5149%), Tech Debt (73.8091%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 180`, `args: 170`, `func_start: 315`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 333`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsSkuStockExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.508 IQR)
- **Top Global Matches:** file_cluster_8: 9.508, file_cluster_16: 9.979, file_cluster_7: 10.124
- **Magnitude:** 1164.74 | **LOC:** 890 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.5149%), Tech Debt (73.8091%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 180`, `args: 170`, `func_start: 315`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 333`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.math.BigDecimal, java.util.ArrayList
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/SmsCouponHistoryExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.387 IQR)
- **Top Global Matches:** file_cluster_8: 9.387, file_cluster_16: 9.866, file_cluster_7: 10.01
- **Magnitude:** 1164.74 | **LOC:** 890 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.5149%), Tech Debt (73.8091%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 180`, `args: 170`, `func_start: 315`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 333`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsCompanyAddressExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.347 IQR)
- **Top Global Matches:** file_cluster_8: 9.347, file_cluster_16: 9.847, file_cluster_7: 9.973
- **Magnitude:** 1140.6 | **LOC:** 869 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.5814%), Tech Debt (75.458%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 175`, `args: 166`, `func_start: 307`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 165`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 325`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberReceiveAddressExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.347 IQR)
- **Top Global Matches:** file_cluster_8: 9.347, file_cluster_16: 9.847, file_cluster_7: 9.973
- **Magnitude:** 1140.6 | **LOC:** 869 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.5814%), Tech Debt (75.458%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 175`, `args: 166`, `func_start: 307`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 165`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 325`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.632
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsAdminExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.389 IQR)
- **Top Global Matches:** file_cluster_8: 9.389, file_cluster_16: 9.879, file_cluster_7: 10.011
- **Magnitude:** 1127.06 | **LOC:** 860 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.6098%), Tech Debt (76.1391%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 174`, `args: 164`, `func_start: 303`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 163`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 321`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsPermissionExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.397 IQR)
- **Top Global Matches:** file_cluster_8: 9.397, file_cluster_16: 9.877, file_cluster_7: 10.018
- **Magnitude:** 1099.94 | **LOC:** 840 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.6776%), Tech Debt (77.6975%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 170`, `args: 160`, `func_start: 295`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 313`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList, java.util.Date
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsBrandExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.359 IQR)
- **Top Global Matches:** file_cluster_8: 9.359, file_cluster_16: 9.844, file_cluster_7: 9.983
- **Magnitude:** 1099.92 | **LOC:** 839 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.682%), Tech Debt (77.7949%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 169`, `args: 160`, `func_start: 295`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 313`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004491
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.358 IQR)
- **Top Global Matches:** file_cluster_13: 12.358, file_cluster_16: 12.431, file_cluster_8: 12.436
- **Magnitude:** 1020.88 | **LOC:** 795 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (31.6451%), Tech Debt (34.2379%)
**Top Internal Functions/Classes:**
  * `cancelOrder` (Impact: 126.9 | O(2^N) | DB: 1)
  * `getCouponOrderItemByRelation` (Impact: 97.5 | O(N^5) | DB: 6)
  * `generateOrder` (Impact: 91.8 | O(N^5) | DB: 58)
  * `list` (Impact: 42.0 | O(N^4) | DB: 8)
  * `cancelTimeOutOrder` (Impact: 36.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 128`, `args: 31`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 190`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 13`, `import: 19`
* *Defense:* `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.macro.mall.portal.domain.*, java.text.SimpleDateFormat, org.springframework.util.CollectionUtils, com.macro.mall.portal.service.*, com.macro.mall.portal.dao.PortalOrderItemDao, java.math.BigDecimal, java.math.RoundingMode, cn.hutool.core.collection.CollUtil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMenuExample.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.419 IQR)
- **Top Global Matches:** file_cluster_8: 9.419, file_cluster_16: 9.888, file_cluster_7: 10.035
- **Magnitude:** 1008.02 | **LOC:** 770 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.9476%), Tech Debt (83.0849%)
**Top Internal Functions/Classes:**
  * `Criterion` (Impact: 20.6 | O(N^4))
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 17.1 | O(N^4) | DB: 1)
  * `addCriterion` (Impact: 15.3 | O(N^4) | DB: 1)
  * `createCriteria` (Impact: 8.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 156`, `args: 146`, `func_start: 267`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 143`, `state_mutation: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 285`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList, java.util.Date
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
- `mall-portal/src/main/java/com/macro/mall/portal/controller/UmsMemberCouponController.java` (JAVA) | Magnitude: 49.82 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, decorators: 25, structural_boundaries: 23, import: 15
- `mall-admin/src/main/java/com/macro/mall/dto/OmsReturnApplyQueryParam.java` (JAVA) | Magnitude: 17.4 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, decorators: 8, encapsulation: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `mall-admin/src/main/java/com/macro/mall/service/OmsOrderService.java` (JAVA) | Magnitude: 41.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 13, doc: 9, args: 8, func_start: 8
- `mall-demo/src/main/java/com/macro/mall/demo/controller/RestTemplateDemoController.java` (JAVA) | Magnitude: 64.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 39, decorators: 26, import: 18
- `mall-admin/src/main/java/com/macro/mall/validator/FlagValidator.java` (JAVA) | Magnitude: 15.98 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 7, branch: 6, func_start: 4, api: 4
- `mall-demo/src/main/java/com/macro/mall/demo/validator/FlagValidator.java` (JAVA) | Magnitude: 15.98 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 7, branch: 6, func_start: 4, api: 4
- `mall-portal/src/main/java/com/macro/mall/portal/controller/MemberReadHistoryController.java` (JAVA) | Magnitude: 86.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 20, decorators: 18, api: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `mall-admin/src/main/java/com/macro/mall/dao/UmsRoleDao.java` (JAVA) | Magnitude: 26.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 4, import: 4, args: 3
- `mall-admin/src/main/java/com/macro/mall/dao/UmsAdminRoleRelationDao.java` (JAVA) | Magnitude: 29.6 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, doc: 5, import: 5, args: 4
- `mall-admin/src/main/java/com/macro/mall/service/SmsHomeBrandService.java` (JAVA) | Magnitude: 31.73 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 6, indent_spaces: 6, structural_boundaries: 5, args: 5
- `mall-admin/src/main/java/com/macro/mall/service/SmsHomeNewProductService.java` (JAVA) | Magnitude: 31.73 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 6, indent_spaces: 6, structural_boundaries: 5, args: 5
- `mall-admin/src/main/java/com/macro/mall/service/SmsHomeRecommendProductService.java` (JAVA) | Magnitude: 31.73 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 6, indent_spaces: 6, structural_boundaries: 5, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `mall-mbg/src/main/java/com/macro/mall/mapper/CmsMemberReportMapper.java` (JAVA) | Magnitude: 36.56 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, args: 7, func_start: 7, indent_spaces: 7
- `document/sh/Dockerfile` (DOCKERFILE) | Magnitude: 13.6 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ipc_rpc_bridges: 2, func_start: 1, class_start: 1, io: 1
- `mall-demo/src/main/java/com/macro/mall/demo/bo/AdminUserDetails.java` (JAVA) | Magnitude: 45.92 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 18, api: 14, func_start: 8
- `mall-portal/src/test/java/com/macro/mall/portal/MallPortalApplicationTests.java` (JAVA) | Magnitude: 4.28 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 3, api: 2, decorators: 2
- `mall-demo/src/main/java/com/macro/mall/demo/MallDemoApplication.java` (JAVA) | Magnitude: 4.78 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 3, api: 2, import: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java` -> Churn: **55.38%** | Cog Load: 7.2417% | Debt: 79.8343%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `mall-admin/src/main/java/com/macro/mall/controller/PmsProductController.java` -> **macro** (100.0% isolated ownership) | Magnitude: 307.48
- `mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java` -> **macro** (100.0% isolated ownership) | Magnitude: 266.6
- `mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java` -> **macro** (100.0% isolated ownership) | Magnitude: 196.66
- `mall-admin/src/main/java/com/macro/mall/controller/UmsMenuController.java` -> **macro** (100.0% isolated ownership) | Magnitude: 164.38
- `mall-admin/src/main/java/com/macro/mall/controller/UmsRoleController.java` -> **macro** (100.0% isolated ownership) | Magnitude: 127.42

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

- `mall-common/src/main/java/com/macro/mall/common/api/CommonResult.java` -> **Severity: 1361.706** (Blast Radius: 13.622 * Doc Risk: 99.9637%)
- `mall-mbg/src/main/java/com/macro/mall/model/PmsProduct.java` -> **Severity: 904.7** (Blast Radius: 9.047 * Doc Risk: 100.0%)
- `mall-common/src/main/java/com/macro/mall/common/api/CommonPage.java` -> **Severity: 786.49** (Blast Radius: 7.942 * Doc Risk: 99.0292%)
- `mall-mbg/src/main/java/com/macro/mall/model/UmsMember.java` -> **Severity: 772.8** (Blast Radius: 7.728 * Doc Risk: 100.0%)
- `mall-mbg/src/main/java/com/macro/mall/model/UmsResource.java` -> **Severity: 641.098** (Blast Radius: 6.411 * Doc Risk: 99.9997%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
