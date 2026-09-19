# ARCHITECTURAL_BRIEF: mall
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/macrozheng/mall.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 668 analyzed artifact(s), 66717 LOC.
- **Load-bearing artifact:** `mall-common/src/main/java/com/macro/mall/common/api/CommonResult.java` -- 50 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java` -- pulls in 42 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderExample.java` at magnitude 1648.78 (structural weight, not risk).
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
| Total Artifacts | 719 |
| Analyzed Artifacts (Scanned) | 668 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 51 |
| Total LOC | 66717 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 92.9% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8045 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1131 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2219 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 106 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 525 | 65662 | 78.6% |
| XML | 114 | 0 | 17.1% |
| YAML | 11 | 461 | 1.6% |
| MARKDOWN | 9 | 0 | 1.3% |
| SHELL | 4 | 73 | 0.6% |
| JSON | 2 | 516 | 0.3% |
| PLAINTEXT | 2 | 0 | 0.3% |
| DOCKERFILE | 1 | 5 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.158`
> **Composition Archetype:** `Mid Flat Project` (z +2.16; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 26%, Declarative / Non-Code 20%, State Mutators Files 14%, Parameter Forwarders Files 14%, Type Conversions Files 12%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 657 | 98.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 1.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 51*

**Composition by Extension & Reason:**
- `.jpg`: 12x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.emmx`: 7x Excluded (Unsupported Extension: '.emmx')
- `.pos`: 3x Excluded (Unsupported Extension: '.pos')
- `.rp`: 2x Excluded (Unsupported Extension: '.rp')
- `.conf`: 2x Excluded (Unsupported Extension: '.conf')
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.pdb`: 1x Excluded (Unsupported Extension: '.pdb')
- `.pdm`: 1x Excluded (Unsupported Extension: '.pdm')
- `.sql`: 1x Excluded (Massive Static Asset Blob: 3258 LOC)
- `.java`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Zero-Density Threshold (LOC: 52, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.9 | 4.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.3 | 28.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.1 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 97.1 | 28.0 | 10.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 32.5 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 86.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 53.0 | 92.9 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8316 | 85 | 36 | `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderExample.java` |
| cleanup | 7 | 5 | 0 | `mall-admin/src/main/java/com/macro/mall/controller/OmsOrderController.java` |
| guards | 3487 | 333 | 25 | `mall-mbg/src/main/java/com/macro/mall/model/OmsOrder.java` |
| danger | 10922 | 136 | 56 | `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderExample.java` |
| concurrency | 1769 | 79 | 23 | `mall-mbg/src/main/java/com/macro/mall/model/SmsFlashPromotionExample.java` |
| connectivity | 15300 | 526 | 86 | `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderExample.java` |
| io | 23 | 9 | 0 | `document/sh/mall-admin.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 1 | 0 | `document/sh/Dockerfile` |
| time | 7 | 5 | 0 | `mall-common/src/main/java/com/macro/mall/common/config/BaseRedisConfig.java` |
| serialization | 11 | 3 | 0 | `mall-common/src/main/java/com/macro/mall/common/config/BaseRedisConfig.java` |
| regex | 9 | 5 | 0 | `document/sh/mall-admin.sh` |
| events | 37 | 18 | 0 | `mall-portal/src/main/java/com/macro/mall/portal/service/impl/AlipayServiceImpl.java` |
| tests | 15 | 9 | 0 | `mall-admin/src/test/com/macro/mall/PmsDaoTests.java` |
| docs | 771 | 293 | 3 | `mall-common/src/main/java/com/macro/mall/common/service/RedisService.java` |
| debt | 34 | 12 | 0 | `document/sh/run.sh` |
| mutation | 5896 | 294 | 33 | `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java` |
| dead_code | 773 | 167 | 5 | `mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java` |
| credential | 6 | 2 | 0 | `document/postman/mall-admin.postman_collection.json` |
| threat | 9 | 7 | 0 | `mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java` |
| ml_ai | 795 | 50 | 0 | `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderExample.java` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

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

- `search` **(Many-Argument Workhorses)** (@ `mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java`) -> Impact: **45.4** | LOC: 62
- `listCart` **(Compute Cores)** (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/UmsMemberCouponServiceImpl.java`) -> Impact: **37.5** | LOC: 57
- `generateOrder` **(I/O & Config Routines)** (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) -> Impact: **35.9** | LOC: 158
- `getCouponOrderItemByRelation` **(Stateful Encapsulated Methods)** (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java`) -> Impact: **33.5** | LOC: 29
  * *Intent:* /** * 获取与优惠券有关系的下单商品 * * @param couponHistoryDetail 优惠券详情 * @param orderItemList 下单商品 * @param type 使用关系类型：0->相关分类；1->指定商品 */
- `calcCartPromotion` **(Compute Cores)** (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPromotionServiceImpl.java`) -> Impact: **31.0** | LOC: 83
- `search` **(Many-Argument Workhorses)** (@ `mall-portal/src/main/java/com/macro/mall/portal/service/impl/PmsPortalProductServiceImpl.java`) -> Impact: **30.5** | LOC: 28
- `list` **(Many-Argument Workhorses)** (@ `mall-admin/src/main/java/com/macro/mall/service/impl/SmsHomeAdvertiseServiceImpl.java`) -> Impact: **28.6** | LOC: 34
- `getRequestIp` **(Defensive Guards)** (@ `mall-common/src/main/java/com/macro/mall/common/util/RequestUtil.java`) -> Impact: **22.7** | LOC: 30
  * *Intent:* /** * 获取请求真实IP地址 */
- `convertProductRelatedInfo` **(Type Conversions)** (@ `mall-search/src/main/java/com/macro/mall/search/service/impl/EsProductServiceImpl.java`) -> Impact: **17.6** | LOC: 40
  * *Intent:* /** * 将返回结果转换为对象 */
- `list` **(Many-Argument Workhorses)** (@ `mall-admin/src/main/java/com/macro/mall/service/impl/PmsProductServiceImpl.java`) -> Impact: **15.3** | LOC: 26

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `mall-mbg/src/main/java/com/macro/mall/model` | 152 | 37948.4 | 8.67% | 0.0% |
| `mall-mbg/src/main/java/com/macro/mall/mapper` | 76 | 1517.76 | 0.0% | 47.37% |
| `mall-portal/src/main/java/com/macro/mall/portal/service/impl` | 15 | 1399.6 | 25.26% | 73.9% |
| `mall-admin/src/main/java/com/macro/mall/service/impl` | 31 | 1308.98 | 19.53% | 84.71% |
| `mall-admin/src/main/java/com/macro/mall/controller` | 31 | 858.02 | 5.18% | 62.17% |
| `mall-mbg/src/main/resources/com/macro/mall/mapper` | 76 | 799.52 | 0.0% | 0.0% |
| `mall-admin/src/main/java/com/macro/mall/service` | 31 | 482.68 | 0.0% | 0.0% |
| `mall-admin/src/main/java/com/macro/mall/dto` | 29 | 475.94 | 0.0% | 0.0% |
| `mall-portal/src/main/java/com/macro/mall/portal/controller` | 13 | 354.58 | 6.94% | 81.36% |
| `mall-portal/src/main/java/com/macro/mall/portal/domain` | 19 | 310.2 | 0.3% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `mall-mbg/src/main/java/com/macro/mall/mapper/CmsHelpCategoryMapper.java` -> **100.0%** Exposure
- `mall-mbg/src/main/java/com/macro/mall/mapper/CmsHelpMapper.java` -> **100.0%** Exposure
- `mall-mbg/src/main/java/com/macro/mall/mapper/CmsPrefrenceAreaProductRelationMapper.java` -> **100.0%** Exposure
- `mall-mbg/src/main/java/com/macro/mall/mapper/CmsSubjectCategoryMapper.java` -> **100.0%** Exposure
- `mall-mbg/src/main/java/com/macro/mall/mapper/CmsSubjectCommentMapper.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `mall-admin/src/main/java/com/macro/mall/service/impl/OmsOrderReturnApplyServiceImpl.java` -> **100.0%** Exposure
- `mall-common/src/main/java/com/macro/mall/common/api/CommonPage.java` -> **100.0%** Exposure
- `mall-common/src/main/java/com/macro/mall/common/config/BaseRedisConfig.java` -> **100.0%** Exposure
- `mall-common/src/main/java/com/macro/mall/common/exception/GlobalExceptionHandler.java` -> **100.0%** Exposure
- `mall-common/src/main/java/com/macro/mall/common/util/RequestUtil.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java` -> **11** Orphaned Functions | **0** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/mapper/CmsHelpMapper.java` -> **11** Orphaned Functions | **0** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/mapper/CmsTopicMapper.java` -> **11** Orphaned Functions | **0** Duplicates
- `mall-mbg/src/main/java/com/macro/mall/mapper/PmsCommentMapper.java` -> **11** Orphaned Functions | **0** Duplicates
- `mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminCacheServiceImpl.java` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2925` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1648.78 | **LOC:** 3011 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.603; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.3%), Connectivity (formerly Api Exposure) (93.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (15.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 605`, `args: 594`, `func_start: 594`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 661`, `state_mutation: 26`
* *Architecture:* `api: 602`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.603
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1430.22 | **LOC:** 2601 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 1.748; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.3%), Connectivity (formerly Api Exposure) (97.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (17.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 523`, `args: 512`, `func_start: 512`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 567`, `state_mutation: 26`
* *Architecture:* `api: 520`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004491
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderReturnApplyExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1094.74 | **LOC:** 1971 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.582; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.3%), Connectivity (formerly Api Exposure) (90.6%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (21.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 397`, `args: 386`, `func_start: 386`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 419`, `state_mutation: 26`
* *Architecture:* `api: 394`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsOrderItemExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 865.44 | **LOC:** 1540 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.2%), Connectivity (formerly Api Exposure) (82.5%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (27.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 310`, `args: 300`, `func_start: 300`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 321`, `state_mutation: 26`
* *Architecture:* `api: 308`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 829.9 | **LOC:** 1447 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.554; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.2%), Connectivity (formerly Api Exposure) (86.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (31.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addCriterionForJDBCDate` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterionForJDBCDate` **(Encapsulated Accessors)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 298`, `args: 279`, `func_start: 279`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 300`, `state_mutation: 27`
* *Architecture:* `api: 287`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Date, java.util.Iterator, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsCartItemExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 769.58 | **LOC:** 1361 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.554; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.2%), Connectivity (formerly Api Exposure) (87.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (31.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 275`, `args: 264`, `func_start: 264`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 279`, `state_mutation: 26`
* *Architecture:* `api: 272`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/SmsCouponExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 742.78 | **LOC:** 1311 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.2%), Connectivity (formerly Api Exposure) (81.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (32.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 265`, `args: 254`, `func_start: 254`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 269`, `state_mutation: 26`
* *Architecture:* `api: 262`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberStatisticsInfoExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 662.78 | **LOC:** 1161 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.7%), Mutation Surface (formerly State Flux) (37.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 235`, `args: 224`, `func_start: 224`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 235`, `state_mutation: 26`
* *Architecture:* `api: 232`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/CmsSubjectExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 657.6 | **LOC:** 1150 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 1.748; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.1%), Connectivity (formerly Api Exposure) (85.3%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (38.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 232`, `args: 222`, `func_start: 222`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 231`, `state_mutation: 26`
* *Architecture:* `api: 230`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsCommentExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 631.0 | **LOC:** 1100 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.1%), Mutation Surface (formerly State Flux) (40.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 222`, `args: 212`, `func_start: 212`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 219`, `state_mutation: 26`
* *Architecture:* `api: 220`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberLevelExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 577.6 | **LOC:** 1000 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 1.844; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.1%), Connectivity (formerly Api Exposure) (87.5%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (45.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 202`, `args: 192`, `func_start: 192`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 197`, `state_mutation: 26`
* *Architecture:* `api: 200`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.844
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004491
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/SmsHomeAdvertiseExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 556.36 | **LOC:** 960 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 1.748; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Connectivity (formerly Api Exposure) (83.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (47.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 194`, `args: 184`, `func_start: 184`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 187`, `state_mutation: 26`
* *Architecture:* `api: 192`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductAttributeExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 545.62 | **LOC:** 939 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 1.582; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Connectivity (formerly Api Exposure) (82.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (49.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 189`, `args: 180`, `func_start: 180`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 183`, `state_mutation: 26`
* *Architecture:* `api: 188`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductOperateLogExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 540.3 | **LOC:** 931 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.2%), Mutation Surface (formerly State Flux) (49.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 189`, `args: 178`, `func_start: 178`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 181`, `state_mutation: 26`
* *Architecture:* `api: 186`, `import: 4`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsProductCategoryExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 524.38 | **LOC:** 899 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.8%), Mutation Surface (formerly State Flux) (51.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 181`, `args: 172`, `func_start: 172`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 173`, `state_mutation: 26`
* *Architecture:* `api: 180`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/CmsTopicExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 519.04 | **LOC:** 890 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.6%), Mutation Surface (formerly State Flux) (52.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 180`, `args: 170`, `func_start: 170`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 26`
* *Architecture:* `api: 178`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsSkuStockExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 519.04 | **LOC:** 890 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 1.675; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Connectivity (formerly Api Exposure) (82.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (52.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 180`, `args: 170`, `func_start: 170`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 26`
* *Architecture:* `api: 178`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/SmsCouponHistoryExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 519.04 | **LOC:** 890 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 1.748; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.0%), Connectivity (formerly Api Exposure) (82.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (52.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 180`, `args: 170`, `func_start: 170`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 26`
* *Architecture:* `api: 178`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/OmsCompanyAddressExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 508.5 | **LOC:** 869 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 1.748; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.9%), Connectivity (formerly Api Exposure) (81.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (53.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 175`, `args: 166`, `func_start: 166`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 165`, `state_mutation: 26`
* *Architecture:* `api: 174`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMemberReceiveAddressExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 508.5 | **LOC:** 869 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 1.632; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.9%), Connectivity (formerly Api Exposure) (81.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (53.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 175`, `args: 166`, `func_start: 166`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 165`, `state_mutation: 26`
* *Architecture:* `api: 174`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.632
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsAdminExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 503.16 | **LOC:** 860 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 1.748; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.9%), Connectivity (formerly Api Exposure) (81.6%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (54.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 174`, `args: 164`, `func_start: 164`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 163`, `state_mutation: 26`
* *Architecture:* `api: 172`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002994
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mall-portal/src/main/java/com/macro/mall/portal/service/impl/OmsPortalOrderServiceImpl.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 502.78 | **LOC:** 795 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 1.023; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.9%)
- **Documentation Coverage:** 54.7619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateOrder` **(I/O & Config Routines)** (Impact: 35.9)
  * `getCouponOrderItemByRelation` **(Stateful Encapsulated Methods)** (Impact: 33.5)
    * *Intent:* /** * 获取与优惠券有关系的下单商品 * * @param couponHistoryDetail 优惠券详情 * @param orderItemList 下单商品 * @param type ...
  * `list` **(Generic / Templated Code)** (Impact: 14.1)
  * `cancelOrder` **(Compute Cores)** (Impact: 13.1)
  * `getUseIntegrationAmount` **(Stateful Encapsulated Methods)** (Impact: 12.4)
    * *Intent:* /** * 获取可用积分抵扣金额 * * @param useIntegration 使用的积分数量 * @param totalAmount 订单总金额 * @param currentMember...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 128`, `args: 32`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 117`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 13`, `import: 19`
* *Defense:* `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` cn.hutool.core.bean.BeanUtil, cn.hutool.core.collection.CollUtil, com.github.pagehelper.PageHelper, com.macro.mall.common.api.CommonPage, com.macro.mall.common.exception.Asserts, com.macro.mall.common.service.RedisService, com.macro.mall.mapper.*, com.macro.mall.model.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsPermissionExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 492.44 | **LOC:** 840 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.9%), Mutation Surface (formerly State Flux) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 170`, `args: 160`, `func_start: 160`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 26`
* *Architecture:* `api: 168`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/PmsBrandExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 492.42 | **LOC:** 839 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 1.82; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.9%), Connectivity (formerly Api Exposure) (85.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (56.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 169`, `args: 160`, `func_start: 160`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 26`
* *Architecture:* `api: 168`, `import: 2`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004491
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mall-mbg/src/main/java/com/macro/mall/model/UmsMenuExample.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 455.12 | **LOC:** 770 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.7%), Mutation Surface (formerly State Flux) (61.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `addCriterion` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `addCriterion` **(Encapsulated Accessors)** (Impact: 4.5)
  * `Criterion` **(Stateful Encapsulated Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 156`, `args: 146`, `func_start: 146`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 143`, `state_mutation: 26`
* *Architecture:* `api: 154`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001497
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Date, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `mall-admin/src/main/java/com/macro/mall/controller/PmsProductCategoryController.java` -> Churn: **85.96%** | Cog Load: 6.7928% | Debt: 79.9552%
- `mall-admin/src/main/java/com/macro/mall/controller/SmsCouponController.java` -> Churn: **80.59%** | Cog Load: 5.2607% | Debt: 96.4329%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `mall-admin/src/main/java/com/macro/mall/service/impl/UmsAdminServiceImpl.java` -> **macro** (100.0% isolated ownership) | Magnitude: 139.1

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `mall-demo/src/main/java/com/macro/mall/demo/dto/PmsBrandDto.java` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 84.5869%)
- `mall-security/src/main/java/com/macro/mall/security/util/JwtTokenUtil.java` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 88.768%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `mall-common/src/main/java/com/macro/mall/common/api/CommonResult.java` -> **Severity: 5.652** (Embedded: 0.0748 * Error Risk: 75.5086%)
- `mall-common/src/main/java/com/macro/mall/common/api/CommonPage.java` -> **Severity: 3.751** (Embedded: 0.0512 * Error Risk: 73.2041%)
- `mall-mbg/src/main/java/com/macro/mall/model/PmsProduct.java` -> **Severity: 2.296** (Embedded: 0.0353 * Error Risk: 65.1074%)
- `mall-mbg/src/main/java/com/macro/mall/model/PmsBrand.java` -> **Severity: 1.348** (Embedded: 0.0216 * Error Risk: 62.3356%)
- `mall-mbg/src/main/java/com/macro/mall/model/UmsMember.java` -> **Severity: 1.217** (Embedded: 0.0192 * Error Risk: 63.4924%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `mall-mbg/src/main/java/com/macro/mall/model/PmsProduct.java` -> **Severity: 904.7** (Blast Radius: 9.047 * Doc Risk: 100.0%)
- `mall-mbg/src/main/java/com/macro/mall/model/UmsMember.java` -> **Severity: 772.8** (Blast Radius: 7.728 * Doc Risk: 100.0%)
- `mall-common/src/main/java/com/macro/mall/common/api/CommonPage.java` -> **Severity: 661.833** (Blast Radius: 7.942 * Doc Risk: 83.3333%)
- `mall-mbg/src/main/java/com/macro/mall/model/UmsResource.java` -> **Severity: 641.1** (Blast Radius: 6.411 * Doc Risk: 100.0%)
- `mall-mbg/src/main/java/com/macro/mall/model/PmsProductCategory.java` -> **Severity: 624.9** (Blast Radius: 6.249 * Doc Risk: 100.0%)

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
